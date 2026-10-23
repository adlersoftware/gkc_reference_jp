import json
import os

TYPES = r"D:\dev\gkc_ref\build\types.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
OUT = r"D:\dev\gkc_ref\build\crafting_manifest.json"
NOTES = r"D:\dev\gkc_ref\build\notes"

GROUPS = [
    ("cr1", ["craftingSystem", "craftingUISystem", "durabilityInfo"]),
    ("cr2", ["craftingPlacementSystem", "craftingStationSystem", "energyStationSystem",
             "materialsZoneSystem", "materialExtractionStationSystem", "craftedObjectPlacedHelper",
             "craftingSocket", "simpleBreakObject", "craftingWorkbenchSystem", "processStationSystem",
             "materialExtractionStationUISystem", "craftingZoneSystem"]),
]


def main():
    types = [t for t in json.load(open(TYPES, encoding="utf-8")) if not t["IsEditor"] and not t["IsNested"]]
    craft = {}
    for t in types:
        if not t["File"].startswith("Crafting System/"):
            continue
        ms = [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]
        if not ms:
            continue
        path = os.path.join(ROOT, t["File"].replace("/", os.sep))
        craft[t["Name"]] = {
            "type": t["Name"],
            "file": t["File"],
            "abs": path,
            "methods": [{"sig": m["Signature"], "line": m["Line"]} for m in ms],
        }

    json.dump(craft, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("types", len(craft), "methods", sum(len(v["methods"]) for v in craft.values()))

    for batch, names in GROUPS:
        payload = [{"type": n, "file": craft[n]["abs"], "methods": craft[n]["methods"]} for n in names]
        path = os.path.join(NOTES, f"input_{batch}.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(batch, len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)


if __name__ == "__main__":
    main()
