#!/usr/bin/env python3
"""Build the standalone HTML file from catalog.json and index.template.html.

Requires only Python 3's standard library.
"""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
catalog = json.loads((HERE / "catalog.json").read_text(encoding="utf-8"))
assert catalog["drugs"] and catalog["sources"]
ids = [x["id"] for x in catalog["drugs"]]
assert len(ids) == len(set(ids)), "Duplicate program id"
for drug in catalog["drugs"]:
    assert drug["refs"], f"Missing source links for {drug['name']}"
    assert drug["claims"], f"Missing factual claims for {drug['name']}"
    for claim in drug["claims"]:
        assert claim["refs"], f"Unsourced claim for {drug['name']}"
        for key in claim["refs"]:
            assert key in catalog["sources"], f"Unknown source {key}"
    for key in drug["refs"]:
        assert key in catalog["sources"], f"Unknown source {key}"
for source in catalog["sources"].values():
    assert source["url"].startswith("https://"), source
for update in catalog["updates"]:
    assert update["refs"], "Unsourced news update"
json_text = json.dumps(catalog, ensure_ascii=False, separators=(",", ":"))
# Prevent closing the JSON script element via its data.
json_text = json_text.replace("</", "<\\/")
html = (HERE / "index.template.html").read_text(encoding="utf-8").replace("__CATALOG_JSON__", json_text)
(HERE / "index.html").write_text(html, encoding="utf-8")
print(f"Built index.html: {len(catalog['drugs'])} programs, {len(catalog['sources'])} source records")
