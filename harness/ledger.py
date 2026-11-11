"""Evidence plumbing: source registry, citation rendering, claim ledger, report finalization, QA checks.

The key idea: URLs in the final report come from the API's own citation objects, never from
text the model wrote. A model can hallucinate a URL in prose; it cannot fake a citation block.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

STATUSES = ["confirmed", "corrected", "unverified", "estimate", "inference"]
NEEDS_SOURCE = {"confirmed", "corrected", "estimate"}
REF_ORDER = [f"B{i}" for i in range(1, 9)] + [f"Q{i}" for i in range(1, 18)]
RISKY_REFS = {"Q5", "Q6", "Q13", "Q14", "Q17"} | {f"B{i}" for i in range(1, 9)}
CLAIM_ID = r"C-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{3}"


# ---------------------------------------------------------------- sources
class SourceRegistry:
    """Run-wide registry of every source that was cited or fetched. IDs are stable within a run."""

    def __init__(self, path: Path):
        self.path = path
        self.data: dict[str, dict] = json.loads(path.read_text()) if path.exists() else {}

    def add(self, url: str, title: str | None, run_date: str, **meta) -> str:
        url = (url or "").strip()
        if url not in self.data:
            self.data[url] = {"id": f"S{len(self.data) + 1}", "url": url, "title": title or "",
                              "accessed": run_date, "cited_texts": [], "seen_in": []}
        rec = self.data[url]
        if title and not rec["title"]:
            rec["title"] = title
        for k, v in meta.items():
            if v and k in ("page_age", "retrieved_at"):
                rec[k] = v
            elif v and k == "cited_text" and v not in rec["cited_texts"] and len(rec["cited_texts"]) < 12:
                rec["cited_texts"].append(v)
            elif v and k == "seen_in" and v not in rec["seen_in"]:
                rec["seen_in"].append(v)
        return rec["id"]

    def by_id(self) -> dict[str, dict]:
        return {r["id"]: r for r in self.data.values()}

    def save(self) -> None:
        self.path.write_text(json.dumps(self.data, indent=1))


def render_with_markers(blocks: list[dict], reg: SourceRegistry, run_date: str, owner: str
                        ) -> tuple[str, dict[str, list[str]], list[dict]]:
    """Turn assistant blocks into Markdown where each cited text block ends with {S12} markers.

    Returns (markdown, quotes_by_source_id, consulted_search_results)."""
    fetched: list[dict] = []
    consulted: list[dict] = []
    for b in blocks:
        if b.get("type") == "web_fetch_tool_result":
            c = b.get("content") or {}
            if c.get("type") == "web_fetch_result":
                doc = c.get("content") or {}
                rec = {"url": c.get("url", ""), "title": doc.get("title") or "",
                       "retrieved_at": c.get("retrieved_at")}
                fetched.append(rec)
                reg.add(rec["url"], rec["title"], run_date, retrieved_at=rec["retrieved_at"], seen_in=owner)
        elif b.get("type") == "web_search_tool_result":
            c = b.get("content")
            if isinstance(c, list):
                for r in c:
                    consulted.append({"url": r.get("url"), "title": r.get("title"), "page_age": r.get("page_age")})

    quotes: dict[str, list[str]] = defaultdict(list)
    out: list[str] = []
    for b in blocks:
        if b.get("type") != "text":
            continue
        text = b.get("text", "")
        ids: list[str] = []
        for c in b.get("citations") or []:
            sid = None
            if c.get("url"):
                page_age = next((r.get("page_age") for r in consulted if r.get("url") == c["url"]), None)
                sid = reg.add(c["url"], c.get("title"), run_date, cited_text=c.get("cited_text"),
                              page_age=page_age, seen_in=owner)
            else:  # citation into a fetched document
                doc = next((d for d in fetched if d["title"] and d["title"] == c.get("document_title")), None)
                idx = c.get("document_index")
                if doc is None and isinstance(idx, int) and 0 <= idx < len(fetched):
                    doc = fetched[idx]
                if doc:
                    sid = reg.add(doc["url"], doc["title"], run_date, cited_text=c.get("cited_text"), seen_in=owner)
            if sid:
                if sid not in ids:
                    ids.append(sid)
                if c.get("cited_text") and c["cited_text"] not in quotes[sid]:
                    quotes[sid].append(c["cited_text"])
        out.append(text + ("".join(f" {{{i}}}" for i in ids) if ids else ""))
    return "".join(out), dict(quotes), consulted


# ---------------------------------------------------------------- claims
CLAIMS_SCHEMA = {
    "type": "object",
    "properties": {
        "claims": {"type": "array", "items": {
            "type": "object",
            "properties": {
                "ref": {"type": "string", "description": "Brief item such as B2 or Q6"},
                "status": {"type": "string", "enum": STATUSES},
                "statement": {"type": "string"},
                "source_ids": {"type": "array", "items": {"type": "string"}},
                "time_sensitive": {"type": "boolean"},
                "next_check": {"type": "string"},
            },
            "required": ["ref", "status", "statement", "source_ids", "time_sensitive", "next_check"],
            "additionalProperties": False}},
        "open_questions": {"type": "array", "items": {
            "type": "object",
            "properties": {"ref": {"type": "string"}, "question": {"type": "string"},
                           "next_check": {"type": "string"}},
            "required": ["ref", "question", "next_check"], "additionalProperties": False}},
    },
    "required": ["claims", "open_questions"],
    "additionalProperties": False,
}

EXTRACT_INSTRUCTIONS = """You convert a research worker's notes into a claim list. You are a careful clerk, not an analyst.
Rules:
1. Create one claim for every tagged paragraph in the Findings section, and one inference claim for every [inference] statement in the Answer summary.
2. Keep the worker's status tag. Keep the statement's meaning and precision. Do not add facts.
3. source_ids: copy only the {S..} markers attached to that paragraph (write them as S12, without braces). Never add an ID that is not attached to that paragraph.
4. ref: the brief item in the tag (B1 to B8, Q1 to Q17). If none is given, use the work package's main ref.
5. time_sensitive: true for prices, plan limits, model availability, regions, product features, certifications, legal status, user counts.
6. next_check: copy the worker's "Next check" for unverified claims, otherwise an empty string.
7. open_questions: every item in the Open questions section."""


def normalize_ref(ref: str, default: str) -> str:
    m = re.search(r"\b([BQ])\s*0*(\d{1,2})\b", ref or "", flags=re.I)
    if m:
        return f"{m.group(1).upper()}{int(m.group(2))}"
    m = re.search(r"\b(question|baseline)\s*0*(\d{1,2})\b", ref or "", flags=re.I)
    if m:
        return ("Q" if m.group(1).lower() == "question" else "B") + str(int(m.group(2)))
    return default


def validate_claims(wp_id: str, default_ref: str, extracted: dict, marker_ids: set[str],
                    quotes: dict[str, list[str]]) -> tuple[list[dict], list[dict]]:
    """Deterministic checks the model cannot talk its way around."""
    claims = []
    for n, c in enumerate(extracted.get("claims", []), start=1):
        sids = [s.strip("{} ").upper() for s in c.get("source_ids", [])]
        bad = [s for s in sids if s not in marker_ids]
        sids = [s for s in sids if s in marker_ids]
        status = c.get("status", "unverified")
        notes = []
        if bad:
            notes.append(f"dropped source ids not attached by the API: {', '.join(bad)}")
        if status in NEEDS_SOURCE and not sids:
            status = "unverified"
            notes.append("no API citation attached; downgraded to unverified")
            c["next_check"] = c.get("next_check") or "Find and cite a primary source for this statement."
        claims.append({
            "id": f"C-{wp_id.replace('WP-', 'WP')}-{n:03d}",
            "wp": wp_id, "ref": normalize_ref(c.get("ref", ""), default_ref),
            "status": status, "statement": c.get("statement", "").strip(),
            "source_ids": sids, "quotes": {s: quotes.get(s, [])[:3] for s in sids},
            "time_sensitive": bool(c.get("time_sensitive")), "next_check": c.get("next_check", ""),
            "notes": "; ".join(notes)})
    oq = [{"wp": wp_id, "ref": normalize_ref(q.get("ref", ""), default_ref),
           "question": q.get("question", ""), "next_check": q.get("next_check", "")}
          for q in extracted.get("open_questions", [])]
    return claims, oq


# ---------------------------------------------------------------- verification
VERDICTS_SCHEMA = {
    "type": "object",
    "properties": {"verdicts": {"type": "array", "items": {
        "type": "object",
        "properties": {
            "claim_id": {"type": "string"},
            "verdict": {"type": "string", "enum": ["supported", "partially_supported", "not_supported",
                                                   "unreachable", "secondary_only"]},
            "evidence_quote": {"type": "string"}, "corrected_statement": {"type": "string"},
            "better_source_url": {"type": "string"}, "page_date": {"type": "string"},
            "notes": {"type": "string"}},
        "required": ["claim_id", "verdict", "evidence_quote", "corrected_statement",
                     "better_source_url", "page_date", "notes"],
        "additionalProperties": False}}},
    "required": ["verdicts"], "additionalProperties": False,
}


def select_for_verification(claims: list[dict], scope: str) -> list[dict]:
    out = []
    for c in claims:
        if c["status"] not in NEEDS_SOURCE or not c["source_ids"]:
            continue
        if scope == "risky" and not (c["time_sensitive"] or c["status"] in ("corrected", "estimate")
                                     or c["ref"] in RISKY_REFS):
            continue
        out.append(c)
    return out


def apply_verdict(c: dict, v: dict | None, reg: SourceRegistry, run_date: str, verifier_ids: list[str]) -> dict:
    c = dict(c)
    c["final_statement"] = c["statement"]
    c["final_status"] = c["status"]
    c["final_source_ids"] = list(c["source_ids"])
    if v is None:
        c["verdict"] = "not_checked" if c["status"] in NEEDS_SOURCE and c["source_ids"] else "n/a"
        return c
    verdict = v.get("verdict", "unreachable")
    c.update(verdict=verdict, evidence_quote=v.get("evidence_quote", ""), page_date=v.get("page_date", ""),
             verifier_notes=v.get("notes", ""))
    better = (v.get("better_source_url") or "").strip()
    better_id = reg.add(better, None, run_date, seen_in="verify") if better.startswith("http") else None
    corrected = (v.get("corrected_statement") or "").strip()
    if verdict == "partially_supported":
        c["final_statement"] = corrected or c["statement"]
    elif verdict == "not_supported":
        if corrected and (better_id or v.get("evidence_quote")):
            c["final_status"] = "corrected"
            c["final_statement"] = corrected
            c["final_source_ids"] = [better_id] if better_id else c["source_ids"]
        else:
            c["final_status"] = "unverified"
            c["next_check"] = v.get("notes") or "Cited source did not support this claim; find a primary source."
    elif verdict == "unreachable":
        if better_id and not corrected:
            c["final_source_ids"] = [better_id]
        else:
            c["final_status"] = "unverified"
            c["next_check"] = "Source could not be loaded during verification; open it by hand: " + \
                              ", ".join(c["source_ids"])
    if better_id and better_id not in c["final_source_ids"] and c["final_status"] != "unverified":
        c["final_source_ids"].append(better_id)
    for sid in verifier_ids:
        if sid not in c["final_source_ids"] and c["final_status"] != "unverified":
            c["final_source_ids"].append(sid)
    if c["final_status"] == "unverified":
        # A source that failed verification must never appear as support in the report.
        c["rejected_source_ids"] = c["final_source_ids"]
        c["final_source_ids"] = []
    return c


def render_ledger(claims: list[dict], open_qs: list[dict], reg: SourceRegistry) -> str:
    by_id = reg.by_id()
    groups: dict[str, list[dict]] = defaultdict(list)
    for c in claims:
        groups[c["ref"]].append(c)
    lines = ["# Verified claim ledger", "",
             "Status is the final status after independent verification. Verdict is the verifier's finding.", ""]
    for ref in REF_ORDER + sorted(set(groups) - set(REF_ORDER)):
        if ref not in groups:
            continue
        lines += [f"## {ref}", ""]
        for c in groups[ref]:
            srcs = ", ".join(f"{s} ({urlparse(by_id[s]['url']).netloc})" for s in c["final_source_ids"] if s in by_id)
            extra = f" Next check: {c['next_check']}" if c["final_status"] == "unverified" and c.get("next_check") \
                and "next check" not in c["final_statement"].lower() else ""
            lines.append(f"- [{c['id']}] ({c['final_status']}; verdict {c.get('verdict', 'n/a')}) "
                         f"{c['final_statement']}" + (f" Sources: {srcs}." if srcs else "") + extra)
        lines.append("")
    lines += ["## Open questions from research and verification", ""]
    for q in open_qs:
        lines.append(f"- ({q['ref']}, {q['wp']}) {q['question']} Next check: {q['next_check']}")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- report finalization
def strip_dashes(text: str) -> tuple[str, int]:
    n = text.count("\u2014") + text.count("\u2013")
    text = re.sub(r"(\d)\s*\u2013\s*(\d)", r"\1 to \2", text)
    text = re.sub(r"\s*\u2014\s*", ", ", text)
    text = text.replace("\u2013", "-")
    return text, n


def finalize_report(traceable: str, claims: list[dict], reg: SourceRegistry) -> tuple[str, dict]:
    """Replace claim IDs with numbered sources, enforce unverified tagging, build section 9."""
    cmap = {c["id"]: c for c in claims}
    by_id = reg.by_id()
    order: list[str] = []
    stats = {"unknown_ids": set(), "unverified_tags_added": 0, "citations": 0}

    def repl_group(m: re.Match, line: str) -> str:
        ids = re.findall(CLAIM_ID, m.group(0))
        nums, unverified, analysis = [], False, False
        for cid in ids:
            c = cmap.get(cid)
            if not c:
                stats["unknown_ids"].add(cid)
                continue
            stats["citations"] += 1
            if c["final_status"] == "unverified":
                unverified = True
            if c["final_status"] == "inference" and not c["final_source_ids"]:
                analysis = True
            for sid in c["final_source_ids"]:
                if sid in by_id:
                    if sid not in order:
                        order.append(sid)
                    nums.append(order.index(sid) + 1)
        label = ", ".join(f"S{n}" for n in sorted(set(nums)))
        parts = []
        if unverified and "unverified" not in line.lower():
            parts.append("(unverified)")
            stats["unverified_tags_added"] += 1
        if label:
            parts.append(f"[{label}]")
        elif analysis:
            parts.append("[analysis]")
        elif unverified:
            parts.append("[no source]")
        else:
            parts.append("[unknown citation]")
        return " ".join(parts)

    out_lines = []
    pattern = re.compile(rf"\[\s*{CLAIM_ID}(?:\s*[,;]\s*{CLAIM_ID})*\s*\]")
    for line in traceable.splitlines():
        out_lines.append(pattern.sub(lambda m, l=line: repl_group(m, l), line))
    body, dashes = strip_dashes("\n".join(out_lines))
    body = re.sub(r"(?ms)^#{1,3}\s*9\.?\s*Sources.*\Z", "", body).rstrip()
    src_lines = ["", "## 9. Sources", ""]
    for n, sid in enumerate(order, start=1):
        r = by_id[sid]
        dates = f"accessed {r['accessed']}"
        if r.get("page_age"):
            dates += f", page dated {r['page_age']}"
        title = r["title"] or urlparse(r["url"]).netloc
        src_lines.append(f"S{n}. {title}. {r['url']} ({dates})")
    stats["unknown_ids"] = sorted(stats["unknown_ids"])
    stats["dashes_replaced"] = dashes
    stats["sources_listed"] = len(order)
    return body + "\n" + "\n".join(src_lines) + "\n", stats


def section_text(md: str, n: int) -> str:
    """Body of top-level section n: from its heading to the next heading at the same or higher level."""
    m = re.search(rf"(?m)^(#{{1,3}})\s*{n}\.?\s+\S.*$", md)
    if not m:
        return ""
    level = len(m.group(1))
    rest = md[m.end():]
    nxt = re.search(rf"(?m)^#{{1,{level}}}\s", rest)
    return rest[:nxt.start()] if nxt else rest


def deterministic_checks(traceable: str, final: str, stats: dict, claims: list[dict]) -> list[str]:
    out = []
    for n in range(1, 10):
        ok = re.search(rf"(?m)^#{{1,3}}\s*{n}\.?\s+\S", final)
        out.append(f"[{'pass' if ok else 'FAIL'}] Section {n} heading present")
    sec3 = section_text(traceable, 3)
    missing_q = [n for n in range(1, 18)
                 if not re.search(rf"(?mi)^(#{{2,4}}\s*|\*\*)?(Q|Question\s*)?{n}[.:)]?\s", sec3)]
    out.append(f"[{'pass' if not missing_q else 'FAIL'}] Questions 1 to 17 answered in section 3"
               + (f" (missing: {missing_q})" if missing_q else ""))
    missing_b = [f"B{i}" for i in range(1, 9) if f"B{i}" not in traceable]
    out.append(f"[{'pass' if not missing_b else 'WARN'}] Baseline items B1 to B8 referenced"
               + (f" (missing: {missing_b})" if missing_b else ""))
    out.append(f"[{'pass' if not stats['unknown_ids'] else 'FAIL'}] Every cited claim ID exists in the ledger"
               + (f" (unknown: {stats['unknown_ids']})" if stats["unknown_ids"] else ""))
    out.append(f"[info] {stats['citations']} claim citations, {stats['sources_listed']} sources listed")
    out.append(f"[{'pass' if not stats['unverified_tags_added'] else 'WARN'}] Unverified claims labeled by the writer"
               + (f" ({stats['unverified_tags_added']} labels added by the harness)" if stats["unverified_tags_added"] else ""))
    out.append(f"[{'pass' if not stats['dashes_replaced'] else 'WARN'}] No em or en dashes"
               + (f" ({stats['dashes_replaced']} replaced)" if stats["dashes_replaced"] else ""))
    cited = set(re.findall(CLAIM_ID, traceable))
    weak = [c["id"] for c in claims if c["final_status"] == "unverified" and c["ref"] in RISKY_REFS and c["id"] not in cited]
    out.append(f"[info] {len(weak)} unverified claims on high-risk items are not mentioned in the report"
               + (f": {', '.join(weak[:25])}" if weak else ""))
    return out
