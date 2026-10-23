import json
import os

TYPES = r"D:\dev\gkc_ref\build\types.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
OUT = r"D:\dev\gkc_ref\build\camera_manifest.json"
NOTES = r"D:\dev\gkc_ref\build\notes"

GROUPS = [
    ("cm1", ["vehicleCameraController", "cameraControllerManager", "headBob",
             "cameraCaptureSystem", "cameraWaypointSystem"]),
]


def main():
    types = [t for t in json.load(open(TYPES, encoding="utf-8")) if not t["IsEditor"] and not t["IsNested"]]
    cam = {}
    for t in types:
        if not t["File"].startswith("Camera/"):
            continue
        ms = [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]
        if not ms:
            continue
        path = os.path.join(ROOT, t["File"].replace("/", os.sep))
        cam[t["Name"]] = {
            "type": t["Name"],
            "file": t["File"],
            "abs": path,
            "methods": [{"sig": m["Signature"], "line": m["Line"]} for m in ms],
        }

    json.dump(cam, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("types", len(cam), "methods", sum(len(v["methods"]) for v in cam.values()))

    assigned = set()
    for batch, names in GROUPS:
        payload = [{"type": n, "file": cam[n]["abs"], "methods": cam[n]["methods"]} for n in names]
        assigned.update(names)
        path = os.path.join(NOTES, f"input_{batch}.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(batch, len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)

    leftover = sorted(n for n in cam if n not in assigned and n != "playerCamera")
    payload = [{"type": n, "file": cam[n]["abs"], "methods": cam[n]["methods"]} for n in leftover]
    path = os.path.join(NOTES, "input_cm2.json")
    json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("cm2", len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)


if __name__ == "__main__":
    main()
