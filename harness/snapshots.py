"""Deterministic data snapshots.

Some official sources are APIs that return JSON (for example the Azure Retail Prices API), and
the web fetch tool is only documented for text, HTML, and PDF. For those, the harness itself
fetches the data, stores the raw response in the run (runs/<id>/snapshots/), and hands it to
Claude as search_result blocks with citations on. Claude then cites the API URL like any other
source, and the stored snapshot is the evidence a reviewer or the verifier can check.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

AZURE_RETAIL = "https://prices.azure.com/api/retail/prices"
AZURE_FIELDS = ["serviceName", "productName", "skuName", "meterName", "unitPrice", "unitOfMeasure",
                "tierMinimumUnits", "armRegionName", "effectiveStartDate"]
MAX_PAGES = 5


def _ssl_context() -> ssl.SSLContext:
    # Some Python builds (MacPorts, python.org) ship without a usable CA store. certifi comes
    # with the Anthropic SDK's dependencies, so prefer it when present.
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def _get_json(url: str, attempts: int = 6) -> dict:
    """GET with backoff. The Retail Prices API throttles bursts with HTTP 429."""
    ctx = _ssl_context()
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "nihilo-icm-research"})
            with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504) or i == attempts - 1:
                raise
            wait = float(e.headers.get("Retry-After") or 0) or min(60, 2 ** (i + 1))
            time.sleep(wait)
    raise RuntimeError("unreachable")


def snapshot_url(spec: dict) -> str:
    if "azure_retail_filter" in spec:
        return f"{AZURE_RETAIL}?$filter=" + urllib.parse.quote(spec["azure_retail_filter"], safe="'")
    raise ValueError(f"Unknown snapshot spec: {spec}")


def fetch(spec: dict, out_dir: Path) -> dict:
    """Fetch once per run; later stages and reruns reuse the stored copy."""
    url = snapshot_url(spec)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / (hashlib.sha1(url.encode()).hexdigest()[:12] + ".json")
    if path.exists():
        return json.loads(path.read_text())
    items, next_url, pages = [], url, 0
    while next_url and pages < MAX_PAGES:
        data = _get_json(next_url)
        items += data.get("Items", [])
        next_url = data.get("NextPageLink")
        pages += 1
        time.sleep(1)  # be polite to a public, unauthenticated API
    snap = {"title": spec["title"], "url": url, "file": path.name,
            "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "pages": pages, "truncated": bool(next_url), "items": items}
    path.write_text(json.dumps(snap, indent=1))
    return snap


def as_search_result(snap: dict) -> dict:
    """One text block per price row, so a citation points at the exact rows used."""
    head = (f"Azure Retail Prices API, the official Microsoft retail price list (USD, pay-as-you-go list "
            f"prices, before discounts or free grants unless a row shows them). Retrieved by the research "
            f"harness at {snap['retrieved_at']}. Query: {snap['url']}\nColumns: " + " | ".join(AZURE_FIELDS))
    blocks = [{"type": "text", "text": head}]
    for it in snap["items"]:
        blocks.append({"type": "text", "text": " | ".join(str(it.get(f, "")) for f in AZURE_FIELDS)})
    if snap["truncated"]:
        blocks.append({"type": "text", "text": "More result pages exist and were not retrieved."})
    if not snap["items"]:
        blocks.append({"type": "text", "text": "The query returned no rows."})
    return {"type": "search_result", "source": snap["url"], "title": snap["title"],
            "content": blocks, "citations": {"enabled": True}}
