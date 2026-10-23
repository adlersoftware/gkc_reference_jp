import json
import os
from collections import Counter

NOTES = r"D:\dev\gkc_ref\notes\player_method_notes.json"
CORE_MANIFEST = r"D:\dev\gkc_ref\build\core_manifest.json"
PLAYER_MANIFEST = r"D:\dev\gkc_ref\build\player_manifest.json"


def load_manifest():
    rows = {}
    for path in (PLAYER_MANIFEST, CORE_MANIFEST):
        if not os.path.exists(path):
            continue
        data = json.load(open(path, encoding="utf-8"))
        items = data.items() if isinstance(data, dict) else [(r["type"], r) for r in data]
        for name, r in items:
            rows[name] = {"methods": [{"sig": m["sig"]} for m in r["methods"]]}
    return rows


def main():
    notes = json.load(open(NOTES, encoding="utf-8"))
    manifest = load_manifest()

    total = covered = 0
    missing_types = []
    for name, r in manifest.items():
        sigs = {m["sig"] for m in r["methods"]}
        got = set(notes.get(name, {}).get("methods", {}))
        total += len(sigs)
        covered += len(sigs & got)
        if not got:
            missing_types.append(name)

    print(f"coverage: {covered}/{total} ({covered/total*100:.1f}%) over {len(manifest)} types")
    if missing_types:
        print("types without notes:", ", ".join(sorted(missing_types)[:20]),
              f"... (+{max(0, len(missing_types)-20)})")

    texts = Counter()
    short = []
    for name, entry in notes.items():
        for sig, text in entry.get("methods", {}).items():
            texts[text] += 1
            if len(text) < 8:
                short.append((name, sig, text))

    print("duplicate descriptions (>3 uses):")
    for text, count in texts.most_common(6):
        if count > 3:
            print(f"  {count}x {text[:60]}")
    if short:
        print("very short descriptions:", short[:8])

    print("types with summary:", sum(1 for e in notes.values() if e.get("summary")))


if __name__ == "__main__":
    main()
