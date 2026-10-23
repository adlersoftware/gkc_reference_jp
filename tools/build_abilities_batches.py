import json
import os

TYPES = r"D:\dev\gkc_ref\build\types.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
OUT = r"D:\dev\gkc_ref\build\abilities_manifest.json"
NOTES = r"D:\dev\gkc_ref\build\notes"

GROUPS = [
    ("ab1", ["playerAbilitiesSystem", "playerAbilitiesUISystem", "abilityInfo"]),
    ("ab2", ["staminaSystem", "grapplingHookSystem", "dashSystem", "oxygenSystem", "magicSpellActionSystem"]),
]


def main():
    types = [t for t in json.load(open(TYPES, encoding="utf-8")) if not t["IsEditor"] and not t["IsNested"]]
    ab = {}
    for t in types:
        if not t["File"].startswith("Abilities System/"):
            continue
        ms = [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]
        if not ms:
            continue
        path = os.path.join(ROOT, t["File"].replace("/", os.sep))
        ab[t["Name"]] = {
            "type": t["Name"],
            "file": t["File"],
            "abs": path,
            "methods": [{"sig": m["Signature"], "line": m["Line"]} for m in ms],
        }

    json.dump(ab, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("types", len(ab), "methods", sum(len(v["methods"]) for v in ab.values()))

    assigned = set()
    for batch, names in GROUPS:
        payload = []
        for n in names:
            r = ab[n]
            assigned.add(n)
            payload.append({"type": n, "file": r["abs"], "methods": r["methods"]})
        path = os.path.join(NOTES, f"input_{batch}.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(batch, len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)

    leftover = sorted(n for n in ab if n not in assigned)
    payload = [{"type": n, "file": ab[n]["abs"], "methods": ab[n]["methods"]} for n in leftover]
    path = os.path.join(NOTES, "input_ab3.json")
    json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("ab3", len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)


if __name__ == "__main__":
    main()
