import json
import os
from collections import defaultdict

ROOT = r"D:\dev\gkc_ref"
MANIFEST = os.path.join(ROOT, "build", "combat_manifest.json")
NOTES = os.path.join(ROOT, "notes", "method_notes.json")
OUT = os.path.join(ROOT, "COMBAT_REFERENCE.md")

GROUP_LABELS = {
    "Combat System": "戦闘中核",
    "Combat System/Melee Combat System": "近接戦闘",
    "Combat System/Melee Combat System/Slice System": "スライス／破砕",
}


def main():
    notes = json.load(open(NOTES, encoding="utf-8"))
    data = json.load(open(MANIFEST, encoding="utf-8"))
    rows = list(data.values()) if isinstance(data, dict) else data

    groups = defaultdict(list)
    total_methods = total_notes = 0
    for r in rows:
        name = r["type"]
        n_notes = len(notes.get(name, {}).get("methods", {}))
        n_methods = len(r["methods"])
        total_methods += n_methods
        total_notes += min(n_notes, n_methods)
        folder = os.path.dirname(r["file"]).replace("\\", "/")
        groups[folder].append((name, n_methods, n_notes))

    lines = []
    lines.append("# Combat System メソッドリファレンス\n")
    lines.append(
        "`Assets/Game Kit Controller/Scripts/Combat System/` 以下のコンポーネントについて、public メソッドの実装を読んで"
        "日本語の一行解説を付けたものです（GKC 3.77h）。\n"
    )
    lines.append(f"- 対象: **{len(rows)} 型 / {total_methods:,} メソッド**")
    lines.append(f"- 注釈付き: **{total_notes:,} メソッド**（{total_notes / max(total_methods, 1) * 100:.0f}%）")
    lines.append("- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。\n")
    lines.append(
        "`meleeWeaponsGrabbedManager` が近接武器の装備・攻撃・投擲をまとめ、`closeCombatSystem` が素手の"
        "コンボ、`sliceSystem` がメッシュ切断、`matchPlayerToTargetSystem` が攻撃時の位置合わせを担当します。\n"
    )

    for folder in sorted(groups, key=lambda f: (f.count("/"), f != "Combat System", f)):
        entries = sorted(groups[folder], key=lambda x: -x[1])
        label = GROUP_LABELS.get(folder, folder)
        lines.append(f"## {label}\n")
        lines.append("| 型 | 概要 | 注釈 |")
        lines.append("| --- | --- | --- |")
        for type_name, n_methods, n_notes in entries:
            summary = notes.get(type_name, {}).get("summary", "")
            link = f"[`{type_name}`](reference/Combat%20System/{type_name}.md)"
            lines.append(f"| {link} | {summary or '–'} | {n_notes}/{n_methods} |")
        lines.append("")

    lines.append("# 注釈の読み方\n")
    lines.append(
        "- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。\n"
        "- 攻撃状態・ダメージ・IK/アニメーション・イベント発火・コルーチンを伴うものは、その旨を書いています。\n"
        "- 空実装は「本体が空で何もしない」と明記しています。\n"
        "- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。\n"
    )

    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote", OUT, f"types={len(rows)} notes={total_notes}/{total_methods}")


if __name__ == "__main__":
    main()
