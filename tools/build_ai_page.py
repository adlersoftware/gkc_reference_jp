import json
import os
from collections import defaultdict

ROOT = r"D:\dev\gkc_ref"
MANIFEST = os.path.join(ROOT, "build", "ai_manifest.json")
NOTES = os.path.join(ROOT, "notes", "method_notes.json")
TYPES = os.path.join(ROOT, "build", "types.json")
OUT = os.path.join(ROOT, "AI_REFERENCE.md")


def main():
    notes = json.load(open(NOTES, encoding="utf-8"))
    types = {t["Name"]: t for t in json.load(open(TYPES, encoding="utf-8"))}
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
        sub = folder.split("/", 1)[1] if "/" in folder else "（直下）"
        groups[sub].append((name, n_methods, n_notes))

    lines = []
    lines.append("# AI コンポーネント メソッドリファレンス\n")
    lines.append(
        "`Assets/Game Kit Controller/Scripts/AI/` 以下のコンポーネントについて、public メソッドの実装を読んで"
        "日本語の一行解説を付けたものです（GKC 3.77h）。\n"
    )
    lines.append(f"- 対象: **{len(rows)} 型 / {total_methods:,} メソッド**")
    lines.append(f"- 注釈付き: **{total_notes:,} メソッド**（{total_notes / max(total_methods, 1) * 100:.0f}%）")
    lines.append("- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。\n")
    lines.append(
        "AI は「知覚（`findObjectivesSystem`）→ 判断（各 `*SystemBrain`）→ 移動（`AINavMesh`）→ "
        "攻撃（武器/近接/能力）」の分業構成です。\n"
    )

    for group in sorted(groups):
        entries = sorted(groups[group], key=lambda x: -x[1])
        lines.append(f"## {group}\n")
        lines.append("| 型 | 概要 | 注釈 |")
        lines.append("| --- | --- | --- |")
        for type_name, n_methods, n_notes in entries:
            summary = notes.get(type_name, {}).get("summary", "")
            link = f"[`{type_name}`](reference/AI/{type_name}.md)"
            lines.append(f"| {link} | {summary or '–'} | {n_notes}/{n_methods} |")
        lines.append("")

    lines.append("# 注釈の読み方\n")
    lines.append(
        "- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。\n"
        "- コルーチン・アニメーション待ち・イベント発火・NavMeshAgent 操作を伴うものは、その旨を文中に書いています。\n"
        "- 引数の意味が名前から自明でない場合のみ、引数に触れています。\n"
        "- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。\n"
    )

    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote", OUT, f"types={len(rows)} notes={total_notes}/{total_methods}")


if __name__ == "__main__":
    main()
