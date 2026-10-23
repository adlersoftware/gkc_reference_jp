import json
import os
from collections import defaultdict

ROOT = r"D:\dev\gkc_ref"
MANIFEST = os.path.join(ROOT, "build", "dialog_event_manifest.json")
NOTES = os.path.join(ROOT, "notes", "method_notes.json")
TYPES = os.path.join(ROOT, "build", "types.json")
OUT = os.path.join(ROOT, "DIALOG_EVENT_REFERENCE.md")

SYSTEMS = [
    ("Dialog System", "会話（ダイアログ）", "`dialogManager` が会話データを保持し、`dialogSystem` が UI と進行、`dialogContentSystem` が 1 会話分の表示を担当します。"),
    ("Event System", "イベント／トリガー", "`eventTriggerSystem` がトリガー入力からイベントを発火し、`remoteEventSystem` が遠隔オブジェクトのイベントを名前で呼び出します。"),
]


def main():
    notes = json.load(open(NOTES, encoding="utf-8"))
    types = {t["Name"]: t for t in json.load(open(TYPES, encoding="utf-8"))}
    data = json.load(open(MANIFEST, encoding="utf-8"))
    rows = list(data.values()) if isinstance(data, dict) else data

    by_system = defaultdict(list)
    total_methods = total_notes = 0
    for r in rows:
        name = r["type"]
        n_notes = len(notes.get(name, {}).get("methods", {}))
        n_methods = len(r["methods"])
        total_methods += n_methods
        total_notes += min(n_notes, n_methods)
        by_system[r["file"].split("/")[0]].append((name, n_methods, n_notes))

    lines = []
    lines.append("# Dialog System / Event System メソッドリファレンス\n")
    lines.append(
        "会話とイベントのコンポーネントについて、public メソッドの実装を読んで"
        "日本語の一行解説を付けたものです（GKC 3.77h）。\n"
    )
    lines.append(f"- 対象: **{len(rows)} 型 / {total_methods:,} メソッド**")
    lines.append(f"- 注釈付き: **{total_notes:,} メソッド**（{total_notes / max(total_methods, 1) * 100:.0f}%）")
    lines.append("- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。\n")

    for system, label, description in SYSTEMS:
        entries = sorted(by_system.get(system, []), key=lambda x: -x[1])
        if not entries:
            continue
        lines.append(f"# {label}（`{system}/`）\n")
        lines.append(description + "\n")
        lines.append("| 型 | 概要 | 注釈 |")
        lines.append("| --- | --- | --- |")
        for type_name, n_methods, n_notes in entries:
            summary = notes.get(type_name, {}).get("summary", "")
            link = f"[`{type_name}`](reference/{system.replace(' ', '%20')}/{type_name}.md)"
            lines.append(f"| {link} | {summary or '–'} | {n_notes}/{n_methods} |")
        lines.append("")

    lines.append("# 注釈の読み方\n")
    lines.append(
        "- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。\n"
        "- UnityEvent の発火、コルーチン（遅延実行）、UI 更新、オブジェクトの有効化を伴うものはその旨を書いています。\n"
        "- 空実装は「本体が空で何もしない」と明記しています。\n"
        "- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。\n"
    )

    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote", OUT, f"types={len(rows)} notes={total_notes}/{total_methods}")


if __name__ == "__main__":
    main()
