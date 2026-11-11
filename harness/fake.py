"""Offline stand-in for anthropic.AsyncAnthropic, used by --dry-run and the tests.

It returns responses shaped like the real Messages API (server tool blocks, citations,
pause_turn, structured JSON) so every stage can be exercised without spending money.
It knows nothing about ICM; its content is placeholder text.
"""
from __future__ import annotations

import copy
import json
import re


class _Final:
    def __init__(self, d: dict):
        self._d = d

    def model_dump(self, **_):
        return copy.deepcopy(self._d)


class _Resp:
    headers = {"request-id": "req_fake"}


class _Stream:
    def __init__(self, d: dict):
        self._d = d
        self.response = _Resp()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *a):
        return False

    async def get_final_message(self):
        return _Final(self._d)


def _usage(searches=0, fetches=0):
    return {"input_tokens": 1200, "output_tokens": 600, "cache_read_input_tokens": 3000,
            "cache_creation_input_tokens": 0,
            "server_tool_use": {"web_search_requests": searches, "web_fetch_requests": fetches}}


def _msg(model, content, stop="end_turn", **u):
    return {"id": "msg_fake", "type": "message", "role": "assistant", "model": model,
            "content": content, "stop_reason": stop, "usage": _usage(**u)}


def _user_text(kwargs) -> str:
    c = kwargs["messages"][0]["content"]
    return c if isinstance(c, str) else json.dumps(c)


class _Messages:
    def stream(self, **kwargs):
        return _Stream(self._respond(kwargs))

    def _respond(self, kw: dict) -> dict:
        model = kw["model"]
        user = _user_text(kw)
        fmt = (kw.get("output_config") or {}).get("format")
        tools = [t["name"] for t in kw.get("tools", [])]
        if fmt:
            return _msg(model, [{"type": "text", "text": json.dumps(self._structured(fmt["schema"], user))}])
        if "web_search" in tools and "Claims citing this source" in user:
            return self._verify(model, user)
        if "web_search" in tools:
            return self._research(model, user, len(kw["messages"]))
        stage = re.search(r'stage="([\w-]+)"', user).group(1)
        return _msg(model, [{"type": "text", "text": self._doc(stage, user)}])

    # ----------------------------------------------------------- research
    def _research(self, model, user, n_messages):
        wp = re.search(r"id: (WP-[\w]+)", user).group(1)
        if n_messages == 1:  # first request pauses mid-search, to exercise pause_turn handling
            return _msg(model, [
                {"type": "thinking", "thinking": "plan", "signature": "sig"},
                {"type": "server_tool_use", "id": "srvtoolu_1", "name": "web_search", "input": {"query": wp}},
                {"type": "web_search_tool_result", "tool_use_id": "srvtoolu_1", "content": [
                    {"type": "web_search_result", "url": f"https://example.com/{wp}/a", "title": f"{wp} source A",
                     "encrypted_content": "x", "page_age": "October 1, 2026"}]},
            ], stop="pause_turn", searches=1)
        refs = re.findall(r"^- ([BQ]\d+)$", user, flags=re.M) or ["Q1"]
        url_a, url_b = f"https://example.com/{wp}/a", f"https://docs.example.org/{wp}/b"
        content = [
            {"type": "server_tool_use", "id": "srvtoolu_2", "name": "web_fetch", "input": {"url": url_b}},
            {"type": "web_fetch_tool_result", "tool_use_id": "srvtoolu_2", "content": {
                "type": "web_fetch_result", "url": url_b, "retrieved_at": "2026-11-10T12:00:00Z",
                "content": {"type": "document", "title": f"{wp} doc B",
                            "source": {"type": "text", "media_type": "text/plain", "data": "..."}}}},
            {"type": "text", "text": "### Findings\n\n"},
        ]
        for r in refs:
            content += [
                {"type": "text", "text": f"[confirmed {r}] Placeholder fact one for {r}.",
                 "citations": [{"type": "web_search_result_location", "url": url_a, "title": f"{wp} source A",
                                "cited_text": f"quoted text for {r}", "encrypted_index": "x"}]},
                {"type": "text", "text": "\n\n"},
                {"type": "text", "text": f"[estimate {r}] Placeholder estimate for {r}.",
                 "citations": [{"type": "char_location", "document_index": 0, "document_title": f"{wp} doc B",
                                "cited_text": "a number", "start_char_index": 0, "end_char_index": 8}]},
                {"type": "text", "text": f"\n\n[confirmed {r}] Uncited statement for {r}.\n\n"
                                         f"[unverified {r}] Unknown thing. Next check: open the vendor page.\n\n"},
            ]
        content.append({"type": "text", "text": "### Open questions\n\n- One open question. Next check: ask the vendor.\n"})
        return _msg(model, content, searches=1, fetches=1)

    # ----------------------------------------------------------- verify
    def _verify(self, model, user):
        ids = re.findall(r"^- (C-[\w-]+?-\d{3}) \|", user, flags=re.M)
        cycle = ["supported", "partially_supported", "not_supported", "unreachable", "supported"]
        verdicts = []
        for i, cid in enumerate(ids):
            v = cycle[i % len(cycle)]
            verdicts.append({"claim_id": cid, "verdict": v, "evidence_quote": "page sentence" if v != "unreachable" else "",
                             "corrected_statement": "A weaker corrected statement." if v in ("partially_supported", "not_supported") else "",
                             "better_source_url": "", "page_date": "", "notes": "fake verifier"})
        text = "Checked the page.\n\n```json\n" + json.dumps({"verdicts": verdicts}) + "\n```\n"
        return _msg(model, [{"type": "text", "text": text}], fetches=1)

    # ----------------------------------------------------------- structured
    def _structured(self, schema, user):
        props = schema.get("properties", {})
        if "claims" in props:
            claims = []
            for m in re.finditer(r"\[(confirmed|corrected|unverified|estimate|inference)\s*([BQ]\d+)?\]\s*([^\[{\n]+)((?:\s*\{S\d+\})*)", user):
                sids = re.findall(r"S\d+", m.group(4))
                claims.append({"ref": m.group(2) or "", "status": m.group(1), "statement": m.group(3).strip(),
                               "source_ids": sids + (["S999"] if not claims else []),  # one invented id, must be dropped
                               "time_sensitive": m.group(1) == "estimate",
                               "next_check": "open the vendor page" if m.group(1) == "unverified" else ""})
            return {"claims": claims, "open_questions": [{"ref": "", "question": "One open question.", "next_check": "ask the vendor"}]}
        return {"verdicts": []}

    # ----------------------------------------------------------- documents
    def _doc(self, stage, user):
        ids = re.findall(r"\[(C-[\w-]+?-\d{3})\]", user)
        cite = lambda i: f"[{ids[i % len(ids)]}]" if ids else ""  # noqa: E731
        if stage == "01-plan":
            return "## Coverage table\n\n| Requirement | Package |\n|---|---|\n| B1 | WP-B1 |\n\n## Gaps\n\nNone found (fake).\n"
        if stage == "04-architect":
            return ("## 4. Hosting model comparison\n\n| Row | Nihilo-hosted | Client-tenant | Hybrid |\n|---|---|---|---|\n"
                    f"| Data residency | x {cite(0)} | y | z |\n\n## 5. Candidate architectures and decision matrix\n\n"
                    "```mermaid\nflowchart LR\n  U[User] --> A[Agent runtime]\n```\n\n"
                    "## 6. Recommendation\n\nPick candidate B [inference].\n\n## 7. Prototype plan\n\nBuild the smallest thing.\n")
        if stage == "05-synthesize":
            q = "\n\n".join(f"### {n}. Question {n}\n\nAnswer text {cite(n)}." for n in range(1, 18))
            b = "\n".join(f"| B{n} | confirmed | {cite(n)} |" for n in range(1, 9))
            return (f"# ICM as an enterprise service\n\n## 1. Executive summary\n\nRecommend B \u2014 with caveats {cite(0)}.\n\n"
                    f"## 2. Baseline validation\n\n| Item | Status | Sources |\n|---|---|---|\n{b}\n\n"
                    f"## 3. Answers to questions 1 to 17\n\n{q}\n\n## 4. Hosting model comparison\n\nTable.\n\n"
                    "## 5. Candidate architectures\n\nDiagrams.\n\n## 6. Recommendation\n\nB.\n\n## 7. Prototype plan\n\nPlan.\n\n"
                    "## 8. Open questions\n\n- Item. Next check: x.\n")
        return "## Most likely wrong\n\n1. Placeholder.\n\n## Fix list\n\n1. Placeholder.\n"


class _Beta:
    def __init__(self):
        self.messages = _Messages()


class FakeAsyncAnthropic:
    def __init__(self, *a, **k):
        self.beta = _Beta()
