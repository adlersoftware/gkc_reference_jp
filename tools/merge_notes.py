import glob
import json
import os

NOTES_DIR = r"D:\dev\gkc_ref\build\notes"
MANIFESTS = [
    r"D:\dev\gkc_ref\build\player_manifest.json",
    r"D:\dev\gkc_ref\build\core_manifest.json",
    r"D:\dev\gkc_ref\build\ai_manifest.json",
    r"D:\dev\gkc_ref\build\dialog_event_manifest.json",
    r"D:\dev\gkc_ref\build\weapons_manifest.json",
    r"D:\dev\gkc_ref\build\action_manifest.json",
    r"D:\dev\gkc_ref\build\inventory_manifest.json",
    r"D:\dev\gkc_ref\build\save_manifest.json",
    r"D:\dev\gkc_ref\build\abilities_manifest.json",
    r"D:\dev\gkc_ref\build\objectives_manifest.json",
    r"D:\dev\gkc_ref\build\vehicles_manifest.json",
    r"D:\dev\gkc_ref\build\pickups_manifest.json",
    r"D:\dev\gkc_ref\build\stats_manifest.json",
    r"D:\dev\gkc_ref\build\camera_manifest.json",
    r"D:\dev\gkc_ref\build\combat_manifest.json",
    r"D:\dev\gkc_ref\build\devices_manifest.json",
    r"D:\dev\gkc_ref\build\health_manifest.json",
    r"D:\dev\gkc_ref\build\input_manifest.json",
    r"D:\dev\gkc_ref\build\skills_manifest.json",
    r"D:\dev\gkc_ref\build\crafting_manifest.json",
    r"D:\dev\gkc_ref\build\remaining_manifest.json",
]
OUT = r"D:\dev\gkc_ref\notes\method_notes.json"


def load_manifest():
    rows = {}
    for path in MANIFESTS:
        if not os.path.exists(path):
            continue
        data = json.load(open(path, encoding="utf-8"))
        items = data.items() if isinstance(data, dict) else [(r["type"], r) for r in data]
        for name, r in items:
            rows[name] = r
    return rows


def main():
    manifest = load_manifest()
    merged = {}
    for path in sorted(glob.glob(os.path.join(NOTES_DIR, "out_*.json"))):
        try:
            data = json.load(open(path, encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            print("skip", os.path.basename(path), exc)
            continue
        for entry in data:
            t = entry["type"]
            slot = merged.setdefault(t, {"summary": "", "methods": {}})
            if entry.get("summary"):
                slot["summary"] = entry["summary"].strip()
            for k, v in entry.get("methods", {}).items():
                if v:
                    slot["methods"][k] = v.strip()

    total = annotated = 0
    incomplete = []
    for t, r in manifest.items():
        sigs = {m["sig"] for m in r["methods"]}
        have = set(merged.get(t, {}).get("methods", {}))
        total += len(sigs)
        annotated += len(sigs & have)
        if len(have) < len(sigs):
            incomplete.append((t, len(have), len(sigs)))
        extra = have - sigs
        if extra:
            print(f"  {t}: {len(extra)} keys not in manifest")

    print(f"annotated {annotated}/{total} methods across {len(merged)} types")
    if incomplete:
        print("incomplete:", incomplete)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(merged, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
