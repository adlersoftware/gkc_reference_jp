import json
import os
from collections import defaultdict

ROOT = r"D:\dev\gkc_ref"
MANIFESTS = [
    (os.path.join(ROOT, "build", "player_manifest.json"), "Player フォルダ"),
    (os.path.join(ROOT, "build", "core_manifest.json"), "プレイヤー中核（Player 外）"),
]
NOTES = os.path.join(ROOT, "notes", "method_notes.json")
TYPES = os.path.join(ROOT, "build", "types.json")
OUT = os.path.join(ROOT, "PLAYER_REFERENCE.md")


def main():
    notes = json.load(open(NOTES, encoding="utf-8"))
    types = {t["Name"]: t for t in json.load(open(TYPES, encoding="utf-8"))}

    def system_of(name):
        return types[name]["File"].split("/")[0]

    total_methods = total_notes = 0
    sections = []
    for path, label in MANIFESTS:
        if not os.path.exists(path):
            continue
        data = json.load(open(path, encoding="utf-8"))
        rows = list(data.values()) if isinstance(data, dict) else data
        groups = defaultdict(list)
        for r in rows:
            name = r["type"]
            n_notes = len(notes.get(name, {}).get("methods", {}))
            n_methods = len(r["methods"])
            total_methods += n_methods
            total_notes += min(n_notes, n_methods)
            folder = os.path.dirname(r["file"]).replace("\\", "/")
            sub = folder.split("/", 1)[1] if "/" in folder else "（直下）"
            groups[sub].append((name, n_methods, n_notes))
        sections.append((label, groups))

    lines = []
    lines.append("# Player 関連コンポーネント メソッドリファレンス\n")
    lines.append(
        "プレイヤーを構成するコンポーネントの public メソッドについて、実装を読んで"
        "日本語の一行解説を付けたものです（GKC 3.77h）。\n"
    )
    type_count = sum(len(r) for _, g in sections for r in g.values())
    lines.append(f"- 対象: **{type_count} 型 / {total_methods:,} メソッド**")
    lines.append(f"- 注釈付き: **{total_notes:,} メソッド**（{total_notes / max(total_methods, 1) * 100:.0f}%）")
    lines.append("- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。\n")

    for label, groups in sections:
        lines.append(f"# {label}\n")
        for group in sorted(groups):
            entries = sorted(groups[group], key=lambda x: -x[1])
            lines.append(f"## {group}\n")
            lines.append("| 型 | 概要 | 注釈 |")
            lines.append("| --- | --- | --- |")
            for type_name, n_methods, n_notes in entries:
                summary = notes.get(type_name, {}).get("summary", "")
                link = f"[`{type_name}`](reference/{system_of(type_name).replace(' ', '%20')}/{type_name}.md)"
                lines.append(f"| {link} | {summary or '–'} | {n_notes}/{n_methods} |")
            lines.append("")

    lines.append("# 注釈の読み方\n")
    lines.append(
        "- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。\n"
        "- コルーチン・アニメーション待ち・イベント発火を伴うものは、その旨を文中に書いています。\n"
        "- 引数の意味が名前から自明でない場合のみ、引数に触れています。\n"
        "- 本体が長いメソッドは主要な効果のみを要約しています。\n"
        "- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。\n"
    )

    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote", OUT, f"notes={total_notes}/{total_methods}")


if __name__ == "__main__":
    main()
