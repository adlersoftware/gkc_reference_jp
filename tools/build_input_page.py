import json
import os

ROOT = r"D:\dev\gkc_ref"
MANIFEST = os.path.join(ROOT, "build", "input_manifest.json")
NOTES = os.path.join(ROOT, "notes", "method_notes.json")
OUT = os.path.join(ROOT, "INPUT_REFERENCE.md")


def main():
    notes = json.load(open(NOTES, encoding="utf-8"))
    data = json.load(open(MANIFEST, encoding="utf-8"))
    rows = list(data.values()) if isinstance(data, dict) else data

    total_methods = total_notes = 0
    entries = []
    for r in rows:
        name = r["type"]
        n_notes = len(notes.get(name, {}).get("methods", {}))
        n_methods = len(r["methods"])
        total_methods += n_methods
        total_notes += min(n_notes, n_methods)
        entries.append((name, n_methods, n_notes))
    entries.sort(key=lambda x: -x[1])

    lines = []
    lines.append("# Input メソッドリファレンス\n")
    lines.append(
        "`Assets/Game Kit Controller/Scripts/Input/` 以下のコンポーネントについて、public メソッドの実装を読んで"
        "日本語の一行解説を付けたものです（GKC 3.77h）。\n"
    )
    lines.append(f"- 対象: **{len(rows)} 型 / {total_methods:,} メソッド**")
    lines.append(f"- 注釈付き: **{total_notes:,} メソッド**（{total_notes / max(total_methods, 1) * 100:.0f}%）")
    lines.append("- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。\n")
    lines.append(
        "`inputManager` がグローバルなキー割り当て（アクション名・軸・タッチ・リバインド・保存）を持ち、"
        "`playerInputManager` がプレイヤーごとの入力問い合わせ窓口、`inputActionManager` が Action System の入力を担当します。\n"
    )

    lines.append("| 型 | 概要 | 注釈 |")
    lines.append("| --- | --- | --- |")
    for name, n_methods, n_notes in entries:
        summary = notes.get(name, {}).get("summary", "")
        link = f"[`{name}`](reference/Input/{name}.md)"
        lines.append(f"| {link} | {summary or '–'} | {n_notes}/{n_methods} |")
    lines.append("")

    lines.append("# 注釈の読み方\n")
    lines.append(
        "- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。\n"
        "- キー割り当ての変更・アクション解決・タッチ/ゲームパッド処理・セーブ/ロードを伴うものは、その旨を書いています。\n"
        "- 空実装は「本体が空で何もしない」と明記しています。\n"
        "- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。\n"
    )

    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote", OUT, f"types={len(rows)} notes={total_notes}/{total_methods}")


if __name__ == "__main__":
    main()
