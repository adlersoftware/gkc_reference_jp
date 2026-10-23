import json
import os

TYPES = r"D:\dev\gkc_ref\build\types.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
OUT = r"D:\dev\gkc_ref\build\action_manifest.json"
NOTES = r"D:\dev\gkc_ref\build\notes"

GROUPS = [
    ("ac1", ["playerActionSystem", "actionSystem", "customActionSystemTrigger",
             "characterActionSystemChecker", "activateActionOnCharactersOnScene"]),
    ("ac2", ["sharedActionSystem", "sharedActionButtonActivator", "sharedActionZone",
             "sharedActionSystemRemoteActivator", "sharedActionZoneManager", "sharedActionZoneTrigger"]),
]


def main():
    types = [t for t in json.load(open(TYPES, encoding="utf-8")) if not t["IsEditor"] and not t["IsNested"]]
    action = {}
    for t in types:
        if not t["File"].startswith("Action System/"):
            continue
        ms = [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]
        if not ms:
            continue
        path = os.path.join(ROOT, t["File"].replace("/", os.sep))
        action[t["Name"]] = {
            "type": t["Name"],
            "file": t["File"],
            "abs": path,
            "methods": [{"sig": m["Signature"], "line": m["Line"]} for m in ms],
        }

    json.dump(action, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("types", len(action), "methods", sum(len(v["methods"]) for v in action.values()))

    for batch, names in GROUPS:
        payload = []
        for n in names:
            r = action[n]
            payload.append({"type": n, "file": r["abs"], "methods": r["methods"]})
        path = os.path.join(NOTES, f"input_{batch}.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(batch, len(payload), "types", sum(len(p["methods"]) for p in payload), "->", path)

    assigned = {n for _, names in GROUPS for n in names}
    print("unassigned:", [n for n in action if n not in assigned])


if __name__ == "__main__":
    main()
