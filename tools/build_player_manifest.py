import json, os

TYPES = r"D:\dev\gkc_ref\build\types.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
OUT = r"D:\dev\gkc_ref\build\player_manifest.json"


def pub_methods(t):
    return [
        m for m in t["Methods"]
        if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]
    ]


def main():
    types = json.load(open(TYPES, encoding="utf-8"))
    rows = []
    for t in types:
        if t["IsEditor"] or t["IsNested"]:
            continue
        if not t["File"].startswith("Player/"):
            continue
        ms = pub_methods(t)
        if not ms:
            continue
        path = os.path.join(ROOT, t["File"].replace("/", os.sep))
        rows.append({
            "type": t["Name"],
            "file": t["File"],
            "abs": path,
            "kb": os.path.getsize(path) // 1024,
            "methods": [
                {"sig": m["Signature"], "line": m["Line"], "ret": m["ReturnType"]}
                for m in ms
            ],
        })
    rows.sort(key=lambda r: -len(r["methods"]))
    json.dump(rows, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)

    print("types", len(rows), "methods", sum(len(r["methods"]) for r in rows))
    for r in rows:
        print(f'{len(r["methods"]):4d} {r["kb"]:5d}KB {r["file"]}')


if __name__ == "__main__":
    main()
