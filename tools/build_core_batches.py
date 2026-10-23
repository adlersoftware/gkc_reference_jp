import json, os

TYPES = r"D:\dev\gkc_ref\build\types.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
NOTES = r"D:\dev\gkc_ref\build\notes"

CORE = ["playerCamera", "playerWeaponsManager", "health", "inventoryManager"]

GROUPS = [
    ("c1", [("playerCamera", 0, 172)]),
    ("c2", [("playerCamera", 172, 344)]),
    ("c3", [("playerWeaponsManager", 0, 184)]),
    ("c4", [("playerWeaponsManager", 184, 368)]),
    ("c5", [("playerWeaponsManager", 368, 551)]),
    ("c6", [("health", None, None)]),
    ("c7", [("inventoryManager", None, None)]),
]


def main():
    types = {t["Name"]: t for t in json.load(open(TYPES, encoding="utf-8"))}
    manifest = {}
    for name in CORE:
        t = types[name]
        ms = [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]
        manifest[name] = {
            "type": name,
            "file": t["File"],
            "abs": os.path.join(ROOT, t["File"].replace("/", os.sep)),
            "methods": [{"sig": m["Signature"], "line": m["Line"]} for m in ms],
        }

    json.dump({k: v for k, v in manifest.items()}, open(r"D:\dev\gkc_ref\build\core_manifest.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=0)

    for batch, specs in GROUPS:
        payload = []
        for name, start, end in specs:
            r = manifest[name]
            methods = r["methods"]
            if start is not None:
                methods = methods[start:end]
            payload.append({"type": name, "file": r["abs"],
                            "methods": [{"sig": m["sig"], "line": m["line"]} for m in methods]})
        path = os.path.join(NOTES, f"input_{batch}.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(batch, sum(len(p["methods"]) for p in payload), "methods ->", path)


if __name__ == "__main__":
    main()
