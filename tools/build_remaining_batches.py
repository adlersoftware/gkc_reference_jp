import json
import os
from collections import defaultdict

TYPES = r"D:\dev\gkc_ref\build\types.json"
NOTES = r"D:\dev\gkc_ref\notes\method_notes.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
OUTDIR = r"D:\dev\gkc_ref\build\notes"
PLAN = r"D:\dev\gkc_ref\build\remaining_plan.json"

CORE = ["Player", "AI", "Dialog System", "Event System", "Weapons", "Action System",
        "Inventory", "Save System", "Abilities System", "Objectives Mission System",
        "Vehicles", "PickUps", "Stats System", "Camera", "Combat System", "Devices",
        "Health", "Input", "Skills System", "Crafting System"]


def main():
    types = [t for t in json.load(open(TYPES, encoding="utf-8")) if not t["IsEditor"] and not t["IsNested"]]
    notes = json.load(open(NOTES, encoding="utf-8"))

    per_system = defaultdict(list)
    for t in types:
        system = t["File"].split("/")[0]
        if system in CORE:
            continue
        ms = [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]
        if not ms:
            continue
        have = notes.get(t["Name"], {}).get("methods", {})
        if len(have) >= len(ms):
            continue
        per_system[system].append({
            "type": t["Name"],
            "file": t["File"],
            "abs": os.path.join(ROOT, t["File"].replace("/", os.sep)),
            "methods": [{"sig": m["Signature"], "line": m["Line"]} for m in ms],
        })

    # plan: per system, chunk big ones
    plan = []
    small = []
    for system, items in sorted(per_system.items(), key=lambda kv: -sum(len(v["methods"]) for v in kv[1])):
        items.sort(key=lambda r: -len(r["methods"]))
        total = sum(len(v["methods"]) for v in items)
        if total <= 200:
            small.append((system, items))
            continue
        chunk, size = [], 0
        for it in items:
            if chunk and size + len(it["methods"]) > 160:
                plan.append((system, chunk))
                chunk, size = [], 0
            chunk.append(it)
            size += len(it["methods"])
        if chunk:
            plan.append((system, chunk))

    # pack small systems into batches (max 4 systems, <=200 methods)
    batch, size, systems = [], 0, 0
    for system, items in small:
        m = sum(len(v["methods"]) for v in items)
        if batch and (size + m > 200 or systems >= 4):
            plan.append(("+".join(s for s, _ in batch), [it for _, items2 in batch for it in items2]))
            batch, size, systems = [], 0, 0
        batch.append((system, items))
        size += m
        systems += 1
    if batch:
        plan.append(("+".join(s for s, _ in batch), [it for _, items2 in batch for it in items2]))

    plan.sort(key=lambda p: -sum(len(v["methods"]) for v in p[1]))

    os.makedirs(OUTDIR, exist_ok=True)
    out = []
    for i, (label, items) in enumerate(plan, 1):
        payload = [{"type": it["type"], "file": it["abs"], "methods": it["methods"]} for it in items]
        path = os.path.join(OUTDIR, f"input_rm{i}.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        n = sum(len(p["methods"]) for p in payload)
        out.append({"batch": f"rm{i}", "label": label, "types": len(payload), "methods": n, "file": path})
        print(f"rm{i:<3d} methods={n:<4d} types={len(payload):<3d} {label}")

    json.dump(out, open(PLAN, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("batches", len(out), "methods", sum(o["methods"] for o in out))


if __name__ == "__main__":
    main()
