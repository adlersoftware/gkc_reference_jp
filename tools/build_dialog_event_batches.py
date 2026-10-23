import json
import os

TYPES = r"D:\dev\gkc_ref\build\types.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
OUT = r"D:\dev\gkc_ref\build\dialog_event_manifest.json"
NOTES = r"D:\dev\gkc_ref\build\notes"

GROUPS = [
    ("d1", "Dialog System/"),
    ("e1", "Event System/"),
]


def main():
    types = [t for t in json.load(open(TYPES, encoding="utf-8")) if not t["IsEditor"] and not t["IsNested"]]
    manifest = {}
    for prefix in ("Dialog System/", "Event System/"):
        for t in types:
            if not t["File"].startswith(prefix):
                continue
            ms = [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]
            if not ms:
                continue
            manifest[t["Name"]] = {
                "type": t["Name"],
                "file": t["File"],
                "abs": os.path.join(ROOT, t["File"].replace("/", os.sep)),
                "methods": [{"sig": m["Signature"], "line": m["Line"]} for m in ms],
            }

    json.dump(manifest, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("types", len(manifest), "methods", sum(len(v["methods"]) for v in manifest.values()))

    for batch, prefix in GROUPS:
        payload = [{"type": v["type"], "file": v["abs"], "methods": v["methods"]}
                   for k, v in manifest.items() if v["file"].startswith(prefix)]
        path = os.path.join(NOTES, f"input_{batch}.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(batch, len(payload), "types", sum(len(p["methods"]) for p in payload), "methods ->", path)


if __name__ == "__main__":
    main()
