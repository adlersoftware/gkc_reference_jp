import json
import os

TYPES = r"D:\dev\gkc_ref\build\types.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
OUT = r"D:\dev\gkc_ref\build\pickups_manifest.json"
NOTES = r"D:\dev\gkc_ref\build\notes"

GROUPS = [
    ("p1", ["pickUpObject", "pickUpManager", "playerPickupIconManager", "pickUpsScreenInfo"]),
    ("p2", ["pickupType", "chestSystem", "dropPickUpSystem", "explosiveBarrel", "crate",
            "weaponPickup", "weaponAttachmentPickup", "meleeWeaponPickup",
            "meleeWeaponConsumablePickup", "meleeShieldPickup", "generalPickup", "ammoPickup"]),
]


def main():
    types = [t for t in json.load(open(TYPES, encoding="utf-8")) if not t["IsEditor"] and not t["IsNested"]]
    picks = {}
    for t in types:
        if not t["File"].startswith("PickUps/"):
            continue
        ms = [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]
        if not ms:
            continue
        path = os.path.join(ROOT, t["File"].replace("/", os.sep))
        picks[t["Name"]] = {
            "type": t["Name"],
            "file": t["File"],
            "abs": path,
            "methods": [{"sig": m["Signature"], "line": m["Line"]} for m in ms],
        }

    json.dump(picks, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("types", len(picks), "methods", sum(len(v["methods"]) for v in picks.values()))

    assigned = set()
    for batch, names in GROUPS:
        payload = []
        for n in names:
            r = picks[n]
            assigned.add(n)
            payload.append({"type": n, "file": r["abs"], "methods": r["methods"]})
        path = os.path.join(NOTES, f"input_{batch}.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(batch, len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)

    print("unassigned:", [n for n in picks if n not in assigned])


if __name__ == "__main__":
    main()
