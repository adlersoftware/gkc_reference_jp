"""Parse GKC custom editors to recover the Inspector layout.

GKC components are configured through hand-written Editor classes, so the
Inspector is not the plain field order:

  GUILayout.BeginVertical ("Main Settings", "window");   -> a titled box
  EditorGUILayout.PropertyField (propVar, new GUIContent ("Label"));
  if (!someToggle.boolValue) { ... }                      -> conditional rows

This module recovers: section titles, row labels, and the `if` conditions that
hide/show a row.
"""

import json
import os
import re

SCRIPTS = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
TYPES_JSON = r"D:\dev\gkc_ref\build\types.json"
OUT_JSON = r"D:\dev\gkc_ref\build\editors.json"

CALL_RE = re.compile(
    r'(?P<begin>GUILayout\.BeginVertical\s*\(\s*"(?P<btitle>[^"]*)"\s*,\s*"(?P<bstyle>[^"]*)")'
    r'|(?P<pf_inline>EditorGUILayout\.PropertyField\s*\(\s*serializedObject\.FindProperty\s*\(\s*"(?P<prop_inline>\w+)"\s*\)'
    r'(?:\s*,\s*new\s+GUIContent\s*\(\s*"(?P<label_inline>[^"]*)")?)'
    r'|(?P<pf>EditorGUILayout\.PropertyField\s*\(\s*(?P<var>[A-Za-z_]\w*)\s*(?![\w.])'
    r'(?:\s*,\s*new\s+GUIContent\s*\(\s*"(?P<label>[^"]*)")?)'
)

ASSIGN_RE = re.compile(r'([A-Za-z_]\w*)\s*=\s*serializedObject\.FindProperty\s*\(\s*"(\w+)"\s*\)')
CUSTOM_EDITOR_RE = re.compile(r'\[CustomEditor\s*\(\s*typeof\s*\(\s*([\w\.]+)\s*\)')
IF_RE = re.compile(r'\b(if|else\s+if)\s*\(')


def strip_comments(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r"//[^\n]*", "", text)
    return text


def match_brace(text, open_idx):
    """Index of the '}' matching the '{' at open_idx (or len(text))."""
    depth = 0
    i = open_idx
    while i < len(text):
        c = text[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return len(text)


def condition_blocks(text):
    """[(start, end, condition)] for each `if (...) { ... }` block."""
    blocks = []
    for m in IF_RE.finditer(text):
        open_paren = text.find("(", m.start())
        depth = 0
        close_paren = open_paren
        for i in range(open_paren, min(len(text), open_paren + 400)):
            if text[i] == "(":
                depth += 1
            elif text[i] == ")":
                depth -= 1
                if depth == 0:
                    close_paren = i
                    break
        cond = text[open_paren + 1:close_paren]
        brace = text.find("{", close_paren)
        semi = text.find(";", close_paren)
        if brace == -1 or (semi != -1 and semi < brace):
            continue  # single-statement if without braces: ignore
        end = match_brace(text, brace)
        blocks.append((m.start(), end, cond.strip()))
    return blocks


def parse_editor(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    m = CUSTOM_EDITOR_RE.search(raw)
    if not m:
        return None
    target = m.group(1).split(".")[-1]
    text = strip_comments(raw)

    var_map = {v: p for v, p in ASSIGN_RE.findall(text)}
    blocks = condition_blocks(text)

    sections = []
    current = None
    for call in CALL_RE.finditer(text):
        if call.group("begin"):
            title = call.group("btitle").strip()
            style = call.group("bstyle").strip()
            if style != "window" and title.lower() in ("box", "window", "button", "helpbox", ""):
                continue
            current = {"title": title, "fields": []}
            sections.append(current)
            continue

        prop = call.group("prop_inline") or var_map.get(call.group("var")) or call.group("var")
        label = call.group("label_inline") or call.group("label")
        if not prop:
            continue
        pos = call.start()
        conds = [c for (s, e, c) in blocks if s < pos < e]
        # innermost last; keep at most two for readability
        cond = " && ".join(conds[-2:]) if conds else None
        if current is None:
            current = {"title": "", "fields": []}
            sections.append(current)
        current["fields"].append({"prop": prop, "label": label, "cond": cond})

    sections = [s for s in sections if s["fields"] or s["title"]]
    return {"target": target, "sections": sections}


def main():
    types = json.load(open(TYPES_JSON, encoding="utf-8"))
    by_name = {}
    for t in types:
        by_name.setdefault(t["Name"], t)

    editors = {}
    for root, _dirs, files in os.walk(SCRIPTS):
        if os.sep + "Editor" not in root + os.sep:
            continue
        for name in files:
            if not name.endswith(".cs"):
                continue
            info = parse_editor(os.path.join(root, name))
            if info:
                editors[info["target"]] = info

    with_cond = sum(1 for e in editors.values() for s in e["sections"] for f in s["fields"] if f["cond"])
    total = sum(1 for e in editors.values() for s in e["sections"] for f in s["fields"])
    print(f"editors={len(editors)} rows={total} conditional={with_cond}")

    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump({k: {"target": v["target"], "sections": v["sections"]} for k, v in editors.items()},
                  fh, ensure_ascii=False)


if __name__ == "__main__":
    main()
