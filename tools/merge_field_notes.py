import glob
import json
import os

FIELDS = r"D:\dev\gkc_ref\build\fields"
OUT = r"D:\dev\gkc_ref\notes\field_notes.json"


def main():
    merged = {}
    for path in sorted(glob.glob(os.path.join(FIELDS, "out_f*.json"))):
        try:
            data = json.load(open(path, encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            print("skip", os.path.basename(path), exc)
            continue
        for entry in data:
            t = entry["type"]
            slot = merged.setdefault(t, {})
            for k, v in entry.get("fields", {}).items():
                if v:
                    slot[k] = v.strip()

    total = sum(len(v) for v in merged.values())
    print("types", len(merged), "fields", total)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(merged, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
