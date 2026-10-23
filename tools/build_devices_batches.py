import json
import os

TYPES = r"D:\dev\gkc_ref\build\types.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
OUT = r"D:\dev\gkc_ref\build\devices_manifest.json"
NOTES = r"D:\dev\gkc_ref\build\notes"

GROUPS = [
    ("dv1", ["lockedCameraSystem", "electronicDevice", "doorSystem", "radioSystem", "deviceStringAction"]),
    ("dv2", ["hologramDoor", "examineObjectSystem", "padlockSystem", "waypointPlatform",
             "elevatorSystem", "accessTerminal"]),
]


def main():
    types = [t for t in json.load(open(TYPES, encoding="utf-8")) if not t["IsEditor"] and not t["IsNested"]]
    dev = {}
    for t in types:
        if not t["File"].startswith("Devices/"):
            continue
        ms = [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]
        if not ms:
            continue
        path = os.path.join(ROOT, t["File"].replace("/", os.sep))
        dev[t["Name"]] = {
            "type": t["Name"],
            "file": t["File"],
            "abs": path,
            "methods": [{"sig": m["Signature"], "line": m["Line"]} for m in ms],
        }

    json.dump(dev, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("types", len(dev), "methods", sum(len(v["methods"]) for v in dev.values()))

    assigned = set()
    for batch, names in GROUPS:
        payload = [{"type": n, "file": dev[n]["abs"], "methods": dev[n]["methods"]} for n in names]
        assigned.update(names)
        path = os.path.join(NOTES, f"input_{batch}.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(batch, len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)

    leftover = sorted(n for n in dev if n not in assigned)
    payload = [{"type": n, "file": dev[n]["abs"], "methods": dev[n]["methods"]} for n in leftover]
    path = os.path.join(NOTES, "input_dv3.json")
    json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("dv3", len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)


if __name__ == "__main__":
    main()
