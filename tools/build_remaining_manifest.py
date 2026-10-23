import glob
import json
import os

NOTES = r"D:\dev\gkc_ref\build\notes"
OUT = r"D:\dev\gkc_ref\build\remaining_manifest.json"


def main():
    merged = {}
    for path in sorted(glob.glob(os.path.join(NOTES, "input_rm*.json"))):
        data = json.load(open(path, encoding="utf-8"))
        for r in data:
            merged[r["type"]] = {
                "type": r["type"],
                "file": r["file"],
                "abs": r["file"],
                "methods": [{"sig": m["sig"], "line": m["line"]} for m in r["methods"]],
            }
    json.dump(merged, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
    print("types", len(merged), "methods", sum(len(v["methods"]) for v in merged.values()))


if __name__ == "__main__":
    main()
