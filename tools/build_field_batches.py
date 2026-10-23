import json
import os

EDITORS = r"D:\dev\gkc_ref\build\editors.json"
TYPES = r"D:\dev\gkc_ref\build\types.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
OUTDIR = r"D:\dev\gkc_ref\build\fields"
PLAN = r"D:\dev\gkc_ref\build\fields_plan.json"
CHUNK = 170


def main():
    editors = json.load(open(EDITORS, encoding="utf-8"))
    types = {t["Name"]: t for t in json.load(open(TYPES, encoding="utf-8"))}

    chunks = []
    for name, ed in editors.items():
        t = types.get(name)
        if not t:
            continue
        rows = []
        for sec in ed["sections"]:
            for f in sec["fields"]:
                rows.append({"field": f["prop"], "label": f.get("label") or "", "section": sec["title"]})
        if not rows:
            continue
        base = {"type": name, "file": os.path.join(ROOT, t["File"].replace("/", os.sep)), "source": t["File"]}
        for i in range(0, len(rows), CHUNK):
            part = rows[i:i + CHUNK]
            chunks.append({"type": name, "file": base["file"], "source": base["source"],
                           "part": i // CHUNK + 1, "total_parts": (len(rows) + CHUNK - 1) // CHUNK,
                           "fields": part})

    chunks.sort(key=lambda c: (c["type"], c["part"]))

    os.makedirs(OUTDIR, exist_ok=True)
    batches, cur, size = [], [], 0
    for c in chunks:
        n = len(c["fields"])
        if cur and (size + n > 200 or len(cur) >= 4 or any(x["type"] == c["type"] for x in cur)):
            batches.append(cur)
            cur, size = [], 0
        cur.append(c)
        size += n
    if cur:
        batches.append(cur)

    plan = []
    for i, batch in enumerate(batches, 1):
        path = os.path.join(OUTDIR, f"input_f{i}.json")
        json.dump(batch, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        n = sum(len(c["fields"]) for c in batch)
        names = [f"{c['type']}#{c['part']}" for c in batch]
        plan.append({"batch": f"f{i}", "types": len(batch), "fields": n, "file": path, "components": names})
        print(f"f{i:<3d} fields={n:<4d} {names}")

    json.dump(plan, open(PLAN, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("batches", len(plan), "fields", sum(p["fields"] for p in plan))


if __name__ == "__main__":
    main()
