import json
import os

TYPES = r"D:\dev\gkc_ref\build\types.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
OUT = r"D:\dev\gkc_ref\build\input_manifest.json"
NOTES = r"D:\dev\gkc_ref\build\notes"

GROUPS = [
    ("in1", ["playerInputManager"]),
    ("in2", ["inputManager"]),
]


def main():
    types = [t for t in json.load(open(TYPES, encoding="utf-8")) if not t["IsEditor"] and not t["IsNested"]]
    inp = {}
    for t in types:
        if not t["File"].startswith("Input/"):
            continue
        ms = [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]
        if not ms:
            continue
        path = os.path.join(ROOT, t["File"].replace("/", os.sep))
        inp[t["Name"]] = {
            "type": t["Name"],
            "file": t["File"],
            "abs": path,
            "methods": [{"sig": m["Signature"], "line": m["Line"]} for m in ms],
        }

    json.dump(inp, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("types", len(inp), "methods", sum(len(v["methods"]) for v in inp.values()))

    assigned = set()
    for batch, names in GROUPS:
        payload = [{"type": n, "file": inp[n]["abs"], "methods": inp[n]["methods"]} for n in names]
        assigned.update(names)
        path = os.path.join(NOTES, f"input_{batch}.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(batch, len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)

    leftover = sorted(n for n in inp if n not in assigned)
    payload = [{"type": n, "file": inp[n]["abs"], "methods": inp[n]["methods"]} for n in leftover]
    path = os.path.join(NOTES, "input_in3.json")
    json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("in3", len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)


if __name__ == "__main__":
    main()
