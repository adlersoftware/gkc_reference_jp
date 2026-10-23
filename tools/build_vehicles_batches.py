import json
import os

TYPES = r"D:\dev\gkc_ref\build\types.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
OUT = r"D:\dev\gkc_ref\build\vehicles_manifest.json"
NOTES = r"D:\dev\gkc_ref\build\notes"

SPLIT = [
    ("v1", [("vehicleHUDManager", 0, 97)]),
    ("v2", [("vehicleHUDManager", 97, 193)]),
    ("v3", [("vehicleController", None, None), ("IKDrivingSystem", None, None)]),
    ("v4", [("vehicleWeaponSystem", None, None), ("GKCSimpleRiderSystem", None, None), ("playerHUDManager", None, None)]),
    ("v5", [("carController", None, None), ("boatController", None, None), ("motorBikeController", None, None),
            ("airCraftController", None, None), ("sphereController", None, None), ("hoverCraftController", None, None),
            ("hoverBoardController", None, None), ("flyingController", None, None),
            ("hoverBoardAnimationSystem", None, None), ("vehicleBuilder", None, None)]),
]


def main():
    types = [t for t in json.load(open(TYPES, encoding="utf-8")) if not t["IsEditor"] and not t["IsNested"]]
    veh = {}
    for t in types:
        if not t["File"].startswith("Vehicles/"):
            continue
        ms = [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]
        if not ms:
            continue
        path = os.path.join(ROOT, t["File"].replace("/", os.sep))
        veh[t["Name"]] = {
            "type": t["Name"],
            "file": t["File"],
            "abs": path,
            "methods": [{"sig": m["Signature"], "line": m["Line"]} for m in ms],
        }

    json.dump(veh, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("types", len(veh), "methods", sum(len(v["methods"]) for v in veh.values()))

    assigned = set()
    for batch, specs in SPLIT:
        payload = []
        for name, start, end in specs:
            r = veh[name]
            ms = r["methods"][start:end] if start is not None else r["methods"]
            assigned.add(name)
            payload.append({"type": name, "file": r["abs"], "methods": ms})
        path = os.path.join(NOTES, f"input_{batch}.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(batch, len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)

    leftover = sorted(n for n in veh if n not in assigned)
    payload = [{"type": n, "file": veh[n]["abs"], "methods": veh[n]["methods"]} for n in leftover]
    path = os.path.join(NOTES, "input_v6.json")
    json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("v6", len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)
    print(leftover)


if __name__ == "__main__":
    main()
