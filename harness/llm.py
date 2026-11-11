"""Thin, auditable wrapper around the Claude Messages API.

What it adds over a bare SDK call:
* pause_turn continuation for long server-side search loops
* server-side fallback when Fable declines (logged, so you know which model answered)
* prompt caching of the shared L0 + L3 system prompt across parallel workers
* a per-run budget guard and spend-cap detection
* every request and response saved to runs/<id>/raw/ and summarized in events.jsonl
"""
from __future__ import annotations

import asyncio
import json
import re
from dataclasses import dataclass, field

import anthropic

from workspace import Run


class BudgetExceeded(RuntimeError):
    pass


class SpendCapReached(RuntimeError):
    pass


@dataclass
class TurnResult:
    blocks: list[dict] = field(default_factory=list)   # every assistant block across continuations
    stop_reason: str = ""
    models_served: list[str] = field(default_factory=list)
    cost_usd: float = 0.0
    usage: dict = field(default_factory=dict)
    refusal: dict | None = None
    fallbacks: list[dict] = field(default_factory=list)

    @property
    def text(self) -> str:
        return "".join(b.get("text", "") for b in self.blocks if b.get("type") == "text")


class Pricing:
    def __init__(self, table: dict, ttl: str):
        self.table = {k: v for k, v in table.items() if isinstance(v, dict)}
        self.search_per_1k = table.get("web_search_per_1k", 10.0)
        self.ttl = ttl
        self.worst = max(self.table.values(), key=lambda p: p["output"])

    def cost(self, model: str, usage: dict) -> float:
        """Estimate the cost of one response.

        cache_creation_input_tokens is the authoritative total. The 5m/1h breakdown in the top-level
        cache_creation object can cover only the first server-side iteration of a long tool loop
        (seen in practice: breakdown 1,275 tokens against a total of 397,935), so it is used only to
        split the total by TTL, never as the total."""
        p = self.table.get(model, self.worst)
        total_w = usage.get("cache_creation_input_tokens") or 0
        w1 = 0
        iters = usage.get("iterations") or []
        if iters:
            w1 = sum(((it.get("cache_creation") or {}).get("ephemeral_1h_input_tokens") or 0) for it in iters)
        elif self.ttl == "1h":
            w1 = total_w
        w1 = min(w1, total_w)
        w5 = total_w - w1
        searches = (usage.get("server_tool_use") or {}).get("web_search_requests") or 0
        return ((usage.get("input_tokens") or 0) * p["input"]
                + (usage.get("output_tokens") or 0) * p["output"]
                + w5 * p["cache_write_5m"] + w1 * p["cache_write_1h"]
                + (usage.get("cache_read_input_tokens") or 0) * p["cache_read"]) / 1e6 \
            + searches * self.search_per_1k / 1000


def build_tools(names: list[str], cfg: dict, max_searches: int = 10, max_fetches: int = 10) -> list[dict]:
    tools = []
    if "web_search" in names:
        ws = cfg["tools"]["web_search"]
        t = {"type": ws["type"], "name": "web_search", "max_uses": max_searches}
        if not ws.get("dynamic_filtering"):
            t["allowed_callers"] = ["direct"]
        if ws.get("blocked_domains"):
            t["blocked_domains"] = ws["blocked_domains"]
        tools.append(t)
    if "web_fetch" in names:
        wf = cfg["tools"]["web_fetch"]
        t = {"type": wf["type"], "name": "web_fetch", "max_uses": max_fetches,
             "citations": {"enabled": True}, "max_content_tokens": wf.get("max_content_tokens", 40000)}
        if not wf.get("dynamic_filtering"):
            t["allowed_callers"] = ["direct"]
        tools.append(t)
    return tools


def system_blocks(texts: list[tuple[str, str]], ttl: str) -> list[dict]:
    """L0 + L3 as system blocks. The cache marker on the last block caches tools + system,
    which is identical for every worker in a stage."""
    blocks = [{"type": "text", "text": f"<{name}>\n{body}\n</{name}>"} for name, body in texts]
    cc = {"type": "ephemeral"} if ttl == "5m" else {"type": "ephemeral", "ttl": "1h"}
    blocks[-1]["cache_control"] = cc
    return blocks


class Claude:
    def __init__(self, run: Run, cfg: dict, client=None):
        self.run = run
        self.cfg = cfg
        self.client = client or anthropic.AsyncAnthropic(
            max_retries=4, timeout=cfg["run"]["request_timeout_s"])
        self.pricing = Pricing(cfg["pricing"], cfg["api"]["cache_ttl"])
        self.budget = float(cfg["run"]["budget_usd"])
        self.sem = asyncio.Semaphore(int(cfg["run"]["concurrency"]))
        self._lock = asyncio.Lock()
        self.spent = run.spent_usd()

    # ------------------------------------------------------------------
    async def turn(self, *, stage: str, name: str, model: str, system: list[dict], user: str,
                   tools: list[dict] | None = None, effort: str = "high", max_tokens: int = 64000,
                   output_format: dict | None = None, allow_fallback: bool = True) -> TurnResult:
        """Run one full assistant turn, following pause_turn continuations.

        If the turn runs out of output tokens before writing any text (thinking ate the budget),
        restart it once from scratch with double the budget. Never ask the model to "continue"
        a cut-off turn: resending a bare thinking block with that request is treated as an attempt
        to extract reasoning and is refused (refusal category reasoning_extraction)."""
        ceiling = int(self.cfg["run"].get("max_tokens_ceiling", 128000))
        max_cont = int(self.cfg["run"]["max_pause_continuations"])
        async with self.sem:
            for attempt in range(2):
                messages: list[dict] = [{"role": "user", "content": user}]
                result = TurnResult()
                for i in range(max_cont + 1):
                    msg = await self._request(stage, f"{name}.a{attempt}.{i:02d}", model, system, messages,
                                              tools, effort, max_tokens, output_format, allow_fallback)
                    result.blocks.extend(msg["content"])
                    result.stop_reason = msg.get("stop_reason") or ""
                    result.models_served.append(msg.get("model", model))
                    for b in msg["content"]:
                        if b.get("type") == "fallback":
                            result.fallbacks.append(b)
                    _accumulate(result.usage, msg.get("usage") or {})
                    result.cost_usd += msg["_cost_usd"]
                    if result.stop_reason == "pause_turn":
                        messages.append({"role": "assistant", "content": msg["content"]})
                        continue
                    if result.stop_reason == "refusal":
                        result.refusal = msg.get("stop_details") or {"type": "refusal"}
                    break
                no_text = not result.text.strip()
                if result.stop_reason == "max_tokens" and no_text and attempt == 0 and max_tokens < ceiling:
                    self.run.log_event({"type": "retry", "stage": stage, "name": name,
                                        "reason": "max_tokens before any text", "old_max_tokens": max_tokens,
                                        "new_max_tokens": min(max_tokens * 2, ceiling),
                                        "wasted_usd": round(result.cost_usd, 4)})
                    max_tokens = min(max_tokens * 2, ceiling)
                    continue
                if result.stop_reason == "max_tokens":
                    self.run.log_event({"type": "warning", "stage": stage, "name": name,
                                        "warning": "output cut off at max_tokens; raise max_tokens for this stage"})
                return result
        return result

    async def extract_json(self, *, stage: str, name: str, model: str, schema: dict,
                           instructions: str, content: str, max_tokens: int = 32000) -> dict:
        """Mechanical structured extraction (no tools, no citations, so JSON outputs are allowed)."""
        sys = [{"type": "text", "text": instructions}]
        res = await self.turn(stage=stage, name=name, model=model, system=sys, user=content,
                              tools=None, effort="medium", max_tokens=max_tokens,
                              output_format={"type": "json_schema", "schema": schema},
                              allow_fallback=False)
        return json.loads(res.text)

    # ------------------------------------------------------------------
    async def _request(self, stage, name, model, system, messages, tools, effort, max_tokens,
                       output_format, allow_fallback) -> dict:
        if getattr(self, "out_of_money", False):
            raise SpendCapReached("Stopped: an earlier request hit the credit or spend limit.")
        async with self._lock:
            if self.spent >= self.budget:
                raise BudgetExceeded(f"Run budget ${self.budget:.2f} reached (spent ${self.spent:.2f}). "
                                     f"Raise run.budget_usd in harness/config.yaml to continue.")
        output_config: dict = {"effort": effort}
        if output_format:
            output_config["format"] = output_format
        kwargs: dict = dict(model=model, max_tokens=max_tokens, system=system, messages=messages,
                            output_config=output_config,
                            cache_control={"type": "ephemeral"})
        if tools:
            kwargs["tools"] = tools
        use_fb = allow_fallback and self.cfg["api"].get("fallbacks", "off") != "off" \
            and model.startswith("claude-fable")
        if use_fb:
            kwargs["fallbacks"] = self.cfg["api"]["fallbacks"]
            kwargs["betas"] = [self.cfg["api"]["fallback_beta"]]

        raw_dir = self.run.raw_dir(stage)
        base, k = name, 1
        while (raw_dir / f"{name}.request.json").exists():
            k += 1
            name = f"{base}.r{k}"
        (raw_dir / f"{name}.request.json").write_text(json.dumps(kwargs, indent=1, default=str))
        try:
            msg, request_id = await self._stream(kwargs)
        except anthropic.BadRequestError as e:
            if "credit balance is too low" in str(e):
                self.out_of_money = True
                raise SpendCapReached("Credit balance too low. Add credit in the Console (Plans & Billing).") from e
            # Some tool versions may not accept allowed_callers; retry once without it.
            if tools and "allowed_callers" in str(e):
                kwargs["tools"] = [{k: v for k, v in t.items() if k != "allowed_callers"} for t in tools]
                msg, request_id = await self._stream(kwargs)
            else:
                self.run.log_event({"type": "api_error", "stage": stage, "name": name, "error": str(e)[:2000]})
                raise
        except anthropic.RateLimitError as e:
            if "enforced_spend_limit_reached" in str(getattr(e, "body", "")) or "spend" in str(e).lower():
                self.out_of_money = True
                raise SpendCapReached(str(e)) from e
            raise
        except anthropic.APIStatusError as e:
            if "credit balance is too low" in str(e):
                self.out_of_money = True
                raise SpendCapReached("Credit balance too low. Add credit in the Console (Plans & Billing).") from e
            raise

        served = msg.get("model", model)
        cost = self.pricing.cost(served, msg.get("usage") or {})
        msg["_cost_usd"] = cost
        async with self._lock:
            self.spent += cost
        (raw_dir / f"{name}.response.json").write_text(json.dumps(msg, indent=1))
        u = msg.get("usage") or {}
        self.run.log_event({
            "type": "api_call", "stage": stage, "name": name, "request_id": request_id,
            "model_requested": model, "model_served": served, "stop_reason": msg.get("stop_reason"),
            "stop_details": msg.get("stop_details"),
            "fallback": any(b.get("type") == "fallback" for b in msg.get("content", [])),
            "input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens"),
            "cache_read": u.get("cache_read_input_tokens"), "cache_write": u.get("cache_creation_input_tokens"),
            "web_search_requests": (u.get("server_tool_use") or {}).get("web_search_requests"),
            "web_fetch_requests": (u.get("server_tool_use") or {}).get("web_fetch_requests"),
            "cost_usd": round(cost, 5), "run_spent_usd": round(self.spent, 4)})
        return msg

    async def _stream(self, kwargs: dict) -> tuple[dict, str | None]:
        """Stream (recommended for long requests) and return the final message as a plain dict,
        dumped by alias so it can be sent back unchanged on continuation."""
        async with self.client.beta.messages.stream(**kwargs) as s:
            final = await s.get_final_message()
            request_id = None
            try:
                request_id = s.response.headers.get("request-id")
            except Exception:
                pass
        return final.model_dump(mode="json", by_alias=True, exclude_none=True), request_id


def _accumulate(total: dict, u: dict) -> None:
    for k in ("input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"):
        total[k] = (total.get(k) or 0) + (u.get(k) or 0)
    stu = u.get("server_tool_use") or {}
    for k in ("web_search_requests", "web_fetch_requests"):
        total[k] = (total.get(k) or 0) + (stu.get(k) or 0)


def last_json_block(text: str) -> dict | None:
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.S)
    for b in reversed(blocks):
        try:
            return json.loads(b)
        except json.JSONDecodeError:
            continue
    return None
