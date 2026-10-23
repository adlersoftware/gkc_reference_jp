import json
import os

TYPES = r"D:\dev\gkc_ref\build\types.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
OUT = r"D:\dev\gkc_ref\build\weapons_manifest.json"
NOTES = r"D:\dev\gkc_ref\build\notes"

GROUPS = [
    ("w1", [("IKWeaponSystem", 0, 116)]),
    ("w2", [("IKWeaponSystem", 116, 232)]),
    ("w3", [("playerWeaponSystem", 0, 105)]),
    ("w4", [("playerWeaponSystem", 105, 209)]),
    ("w5", [("projectileSystem", None, None), ("simpleWeaponSystem", None, None),
            ("bowSystem", None, None), ("weaponSystem", None, None)]),
    ("w6", [("weaponBuilder", None, None), ("weaponAttachmentSystem", None, None),
            ("gravityGun", None, None), ("surfaceToSlice", None, None),
            ("weaponAnimatorSystem", None, None), ("smartphoneDevice", None, None),
            ("armorSurfaceSystem", None, None)]),
]


def main():
    types = [t for t in json.load(open(TYPES, encoding="utf-8")) if not t["IsEditor"] and not t["IsNested"]]
    weapons = {}
    for t in types:
        if not t["File"].startswith("Weapons/"):
            continue
        ms = [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]
        if not ms:
            continue
        path = os.path.join(ROOT, t["File"].replace("/", os.sep))
        weapons[t["Name"]] = {
            "type": t["Name"],
            "file": t["File"],
            "abs": path,
            "methods": [{"sig": m["Signature"], "line": m["Line"]} for m in ms],
        }

    json.dump(weapons, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("types", len(weapons), "methods", sum(len(v["methods"]) for v in weapons.values()))

    assigned = set()
    for batch, specs in GROUPS:
        payload = []
        for name, start, end in specs:
            r = weapons[name]
            ms = r["methods"][start:end] if start is not None else r["methods"]
            assigned.add(name)
            payload.append({"type": name, "file": r["abs"], "methods": ms})
        path = os.path.join(NOTES, f"input_{batch}.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(batch, len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)

    leftover = [n for n in weapons if n not in assigned and n != "playerWeaponsManager"]
    if leftover:
        payload = [{"type": n, "file": weapons[n]["abs"], "methods": weapons[n]["methods"]} for n in sorted(leftover)]
        path = os.path.join(NOTES, "input_w7.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("w7", len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)


if __name__ == "__main__":
    main()
