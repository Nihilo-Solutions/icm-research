"""Offline tests. Run: python -m pytest -q tests   (or: python tests/test_harness.py)

1. The real Anthropic SDK accepts the request the harness builds, and the harness parses a real
   SDK stream (citations, server tool blocks, fallback block) into the dicts it relies on.
2. The evidence rules hold: invented source IDs are dropped, uncited facts are downgraded,
   unverified claims get labeled, unknown claim IDs are caught, dashes are removed.
3. The whole six-stage pipeline runs end to end against the fake API.
"""
from __future__ import annotations

import asyncio
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import httpx2 as httpx
import anthropic

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "harness"))

from ledger import (SourceRegistry, finalize_report, render_with_markers, strip_dashes,  # noqa: E402
                    validate_claims, apply_verdict)
from llm import Claude, build_tools, system_blocks  # noqa: E402
from workspace import load_config  # noqa: E402


def _sse(events: list[dict]) -> bytes:
    return "".join(f"event: {e['type']}\ndata: {json.dumps(e)}\n\n" for e in events).encode()


SSE_EVENTS = [
    {"type": "message_start", "message": {"id": "msg_1", "type": "message", "role": "assistant",
                                          "model": "claude-opus-4-8", "content": [], "stop_reason": None,
                                          "usage": {"input_tokens": 100, "output_tokens": 1}}},
    {"type": "content_block_start", "index": 0, "content_block": {
        "type": "fallback", "from": {"model": "claude-fable-5-2"}, "to": {"model": "claude-opus-4-8"},
        "trigger": {"type": "refusal", "category": "cyber"}}},
    {"type": "content_block_stop", "index": 0},
    {"type": "content_block_start", "index": 1, "content_block": {
        "type": "server_tool_use", "id": "srvtoolu_1", "name": "web_search", "input": {}}},
    {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"query\": \"owasp llm top 10\"}"}},
    {"type": "content_block_stop", "index": 1},
    {"type": "content_block_start", "index": 2, "content_block": {
        "type": "web_search_tool_result", "tool_use_id": "srvtoolu_1", "content": [
            {"type": "web_search_result", "url": "https://genai.owasp.org/llm-top-10/", "title": "OWASP Top 10 for LLM",
             "encrypted_content": "abc", "page_age": "2025-01-01"}]}},
    {"type": "content_block_stop", "index": 2},
    {"type": "content_block_start", "index": 3, "content_block": {"type": "text", "text": "", "citations": []}},
    {"type": "content_block_delta", "index": 3, "delta": {"type": "text_delta", "text": "[confirmed Q11] The list has ten items."}},
    {"type": "content_block_delta", "index": 3, "delta": {"type": "citations_delta", "citation": {
        "type": "web_search_result_location", "url": "https://genai.owasp.org/llm-top-10/",
        "title": "OWASP Top 10 for LLM", "cited_text": "Top 10 risks", "encrypted_index": "e1"}}},
    {"type": "content_block_stop", "index": 3},
    {"type": "message_delta", "delta": {"stop_reason": "end_turn"},
     "usage": {"output_tokens": 50, "server_tool_use": {"web_search_requests": 1}}},
    {"type": "message_stop"},
]


class _FakeRun:
    def __init__(self, d: Path):
        self.dir = d
        self.events_ = []

    def raw_dir(self, stage):
        p = self.dir / "raw" / stage
        p.mkdir(parents=True, exist_ok=True)
        return p

    def log_event(self, e):
        self.events_.append(e)

    def spent_usd(self):
        return 0.0


def test_real_sdk_request_and_stream_parsing():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["body"] = json.loads(request.content)
        captured["headers"] = dict(request.headers)
        return httpx.Response(200, headers={"content-type": "text/event-stream", "request-id": "req_123"},
                              content=_sse(SSE_EVENTS))

    client = anthropic.AsyncAnthropic(api_key="test", max_retries=0,
                                      http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)))
    cfg = load_config()
    with tempfile.TemporaryDirectory() as td:
        run = _FakeRun(Path(td))
        claude = Claude(run, cfg, client=client)
        res = asyncio.run(claude.turn(
            stage="02-research", name="WP-Q11", model="claude-fable-5-2",
            system=system_blocks([("L0", "rules")], "5m"), user="go",
            tools=build_tools(["web_search", "web_fetch"], cfg), effort="high", max_tokens=1000))
        body, headers = captured["body"], captured["headers"]
        assert body["model"] == "claude-fable-5-2"
        assert body["fallbacks"] == "default"
        assert "server-side-fallback-2026-07-01" in headers.get("anthropic-beta", "")
        assert body["output_config"] == {"effort": "high"}
        assert "temperature" not in body and "thinking" not in body
        assert body["system"][-1]["cache_control"]["type"] == "ephemeral"
        assert {t["name"] for t in body["tools"]} == {"web_search", "web_fetch"}
        # parsing
        assert res.models_served == ["claude-opus-4-8"]
        assert len(res.fallbacks) == 1 and res.fallbacks[0]["from"]["model"] == "claude-fable-5-2"
        assert res.usage["web_search_requests"] == 1
        assert run.events_[-1]["request_id"] == "req_123" and run.events_[-1]["fallback"] is True
        reg = SourceRegistry(Path(td) / "s.json")
        md, quotes, consulted = render_with_markers(res.blocks, reg, "2026-11-10", "WP-Q11")
        assert md.strip() == "[confirmed Q11] The list has ten items. {S1}"
        assert quotes["S1"] == ["Top 10 risks"]
        assert reg.by_id()["S1"]["page_age"] == "2025-01-01"


class _SeqClient:
    """Returns canned responses in order and records each request."""
    def __init__(self, responses):
        self.responses, self.requests = list(responses), []
        outer = self

        class _M:
            def stream(self, **kw):
                outer.requests.append(json.loads(json.dumps(kw, default=str)))
                from fake import _Stream
                return _Stream(outer.responses.pop(0))

        class _B:
            messages = _M()
        self.beta = _B()


def test_max_tokens_restarts_with_bigger_budget_and_never_says_continue():
    from fake import _msg
    thinking_only = _msg("claude-fable-5-2", [{"type": "thinking", "thinking": "", "signature": "s"}], stop="max_tokens")
    good = _msg("claude-fable-5-2", [{"type": "text", "text": "done"}])
    client = _SeqClient([thinking_only, good])
    with tempfile.TemporaryDirectory() as td:
        run = _FakeRun(Path(td))
        claude = Claude(run, load_config(), client=client)
        res = asyncio.run(claude.turn(stage="01-plan", name="plan", model="claude-fable-5-2",
                                      system=system_blocks([("L0", "x")], "5m"), user="go", max_tokens=16000))
    assert res.text == "done"
    assert client.requests[1]["max_tokens"] == 32000
    assert len(client.requests[1]["messages"]) == 1
    assert all("Continue" not in json.dumps(r["messages"]) for r in client.requests)
    assert any(e.get("type") == "retry" for e in run.events_)


def test_claim_validation_rules():
    extracted = {"claims": [
        {"ref": "Q6", "status": "confirmed", "statement": "a", "source_ids": ["S1", "S77"], "time_sensitive": True, "next_check": ""},
        {"ref": "Q6", "status": "confirmed", "statement": "b", "source_ids": [], "time_sensitive": False, "next_check": ""},
        {"ref": "question 7", "status": "inference", "statement": "c", "source_ids": [], "time_sensitive": False, "next_check": ""},
    ], "open_questions": []}
    claims, _ = validate_claims("WP-Q06A", "Q6", extracted, {"S1"}, {"S1": ["q"]})
    assert claims[0]["source_ids"] == ["S1"] and "S77" in claims[0]["notes"]
    assert claims[1]["status"] == "unverified"
    assert claims[2]["status"] == "inference" and claims[2]["ref"] == "Q7"
    assert claims[0]["id"] == "C-WPQ06A-001"


def test_verdicts_and_report_finalization():
    with tempfile.TemporaryDirectory() as td:
        reg = SourceRegistry(Path(td) / "s.json")
        reg.add("https://learn.microsoft.com/x", "MS page", "2026-11-10")
        base = {"wp": "WP-Q06A", "ref": "Q6", "source_ids": ["S1"], "quotes": {}, "time_sensitive": True,
                "next_check": "", "notes": ""}
        ok = apply_verdict({**base, "id": "C-WPQ06A-001", "status": "confirmed", "statement": "fact"},
                           {"verdict": "supported"}, reg, "2026-11-10", [])
        bad = apply_verdict({**base, "id": "C-WPQ06A-002", "status": "confirmed", "statement": "wrong"},
                            {"verdict": "not_supported", "corrected_statement": "", "evidence_quote": ""},
                            reg, "2026-11-10", [])
        assert ok["final_status"] == "confirmed" and bad["final_status"] == "unverified"
        report = ("## 1. Summary\n\nFact here [C-WPQ06A-001]. Wrong thing [C-WPQ06A-002]. "
                  "Ghost [C-WPQ99-001].\n\nRange 5\u201350 \u2014 done.\n")
        final, stats = finalize_report(report, [ok, bad], reg)
        assert "Fact here [S1]." in final
        assert "Wrong thing (unverified) [no source]." in final
        assert stats["unknown_ids"] == ["C-WPQ99-001"]
        assert "5 to 50, done" in final and "\u2014" not in final
        assert "S1. MS page. https://learn.microsoft.com/x (accessed 2026-11-10)" in final


def test_snapshot_search_results_are_cited_to_the_api_url():
    from snapshots import as_search_result, snapshot_url
    url = snapshot_url({"azure_retail_filter": "serviceName eq 'Key Vault' and armRegionName eq 'eastus'"})
    assert url.startswith("https://prices.azure.com/api/retail/prices?$filter=serviceName%20eq%20'Key%20Vault'")
    snap = {"title": "Key Vault", "url": url, "retrieved_at": "2026-11-11T08:00:00+00:00", "truncated": False,
            "items": [{"serviceName": "Key Vault", "meterName": "Operations", "unitPrice": 0.03, "unitOfMeasure": "10K"}]}
    sr = as_search_result(snap)
    assert sr["type"] == "search_result" and sr["citations"] == {"enabled": True} and len(sr["content"]) == 2
    blocks = [{"type": "text", "text": "[confirmed Q6] Key Vault operations cost $0.03 per 10K.",
               "citations": [{"type": "search_result_location", "source": url, "title": "Key Vault",
                              "cited_text": "Key Vault | | | Operations | 0.03 | 10K", "search_result_index": 0,
                              "start_block_index": 1, "end_block_index": 2}]}]
    with tempfile.TemporaryDirectory() as td:
        reg = SourceRegistry(Path(td) / "s.json")
        reg.add(url, "Key Vault", "2026-11-11", snapshot="snapshots/abc.json", seen_in="WP-X1")
        md, quotes, _ = render_with_markers(blocks, reg, "2026-11-11", "WP-X1")
        assert md.endswith("{S1}") and reg.by_id()["S1"]["snapshot"] == "snapshots/abc.json"
        assert quotes["S1"] == ["Key Vault | | | Operations | 0.03 | 10K"]


def test_pricing_uses_total_cache_writes_not_first_iteration_breakdown():
    from llm import Pricing
    pr = Pricing(load_config()["pricing"], "5m")
    usage = {"input_tokens": 14, "output_tokens": 51051, "cache_read_input_tokens": 802957,
             "cache_creation_input_tokens": 397935,
             "cache_creation": {"ephemeral_5m_input_tokens": 1275, "ephemeral_1h_input_tokens": 0},
             "server_tool_use": {"web_search_requests": 16},
             "iterations": [{"cache_creation": {"ephemeral_5m_input_tokens": 1275}}, {"cache_creation": {"ephemeral_5m_input_tokens": 396660}}]}
    assert round(pr.cost("claude-fable-5-2", usage), 2) == 6.34


def test_recover_turn_reuses_paid_research():
    import icm
    with tempfile.TemporaryDirectory() as td:
        class R:
            dir = Path(td)
            events = []
            def raw_dir(self, stage):
                p = Path(td) / "raw" / stage; p.mkdir(parents=True, exist_ok=True); return p
            def log_event(self, e): self.events.append(e)
        r = R()
        d = r.raw_dir("02-research")
        (d / "WP-Q07.a0.00.response.json").write_text(json.dumps({"model": "claude-fable-5-2", "stop_reason": "pause_turn", "content": [{"type": "text", "text": "a"}], "usage": {"output_tokens": 1}}))
        (d / "WP-Q07.a0.01.response.json").write_text(json.dumps({"model": "claude-fable-5-2", "stop_reason": "end_turn", "content": [{"type": "text", "text": "b"}], "usage": {"output_tokens": 2}}))
        (d / "WP-Q07.extract.a0.00.response.json").write_text("{}")
        res = icm.recover_turn(r, "02-research", "WP-Q07")
        assert res.text == "ab" and res.usage["output_tokens"] == 3 and res.cost_usd == 0
        assert icm.recover_turn(r, "02-research", "WP-Q08") is None


def test_strip_dashes():
    assert strip_dashes("a \u2014 b, 1\u20132")[0] == "a, b, 1 to 2"


def test_full_pipeline_dry_run():
    with tempfile.TemporaryDirectory() as td:
        ws = Path(td) / "ws"
        shutil.copytree(ROOT, ws, ignore=shutil.ignore_patterns("runs", "__pycache__", ".git"))
        (ws / "runs").mkdir()
        py = [sys.executable, str(ws / "harness" / "icm.py")]
        subprocess.run(py + ["new", "--label", "t"], check=True, capture_output=True)
        gated = subprocess.run(py + ["run", "02", "--dry-run"], capture_output=True, text=True)
        assert gated.returncode != 0 and "not approved" in gated.stderr + gated.stdout
        r = subprocess.run(py + ["all", "--auto", "--dry-run"], capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
        run_dir = next((ws / "runs").glob("2*"))
        qa = (run_dir / "06-qa" / "output" / "qa.md").read_text()
        assert "[FAIL" not in qa, qa
        report = (run_dir / "05-synthesize" / "output" / "report.md").read_text()
        assert "## 9. Sources" in report and "\u2014" not in report
        manifest = json.loads((run_dir / "manifest.json").read_text())
        assert manifest["context_versions"][0]["files"]["CLAUDE.md"]


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
