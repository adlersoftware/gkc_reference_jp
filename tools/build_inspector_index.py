import json
import os
from collections import defaultdict

ROOT = r"D:\dev\gkc_ref"
EDITORS = os.path.join(ROOT, "build", "editors.json")
TYPES = os.path.join(ROOT, "build", "types.json")
NOTES = os.path.join(ROOT, "notes", "field_notes.json")
OUT = os.path.join(ROOT, "INSPECTOR_REFERENCE.md")

SYSTEM_NOTES = {
    "Player": "プレイヤーの移動・状態・入力・IK・カメラ連携。",
    "Camera": "視点、カメラステート、車両カメラ、カットシーン、エフェクト。",
    "Weapons": "射撃・近接武器、IK、投射物、アタッチメント。",
    "Inventory": "所持品、装備、銀行、通貨、重量、UI。",
    "Vehicles": "車両 HUD、運転 IK、車載武器、車種別コントローラ。",
    "Map": "マップ生成・表示・マップオブジェクト。",
    "Grab Objects": "物を掴む・運ぶ・投げる・近接攻撃。",
    "Others": "共通ユーティリティ、スポナー、スキャナー、UI 補助。",
    "Health": "体力・シールド・HP バー・被弾演出。",
    "Abilities System": "アビリティ、スタミナ、酸素、ダッシュ、グラップリング。",
    "Input": "キー割り当て、アクション判定、タッチ、カーソル。",
    "Combat System": "近接武器、素手コンボ、投擲、スライス、盾。",
    "Devices": "扉、端末、南京錠、エレベータ、固定カメラ、監視カメラ。",
    "Save System": "スロット保存、保存データ、シーン要素の状態。",
    "Powers": "テレキネシス、時間操作、重力操作などの特殊能力。",
    "Menu": "ポーズメニュー、インゲームメニュー、シーンロード。",
    "Gravity": "重力方向の変更、無重力エリア、車両の重力制御。",
    "Game Manager": "ゲーム全体の管理（ポーズ、設定、シーン）。",
    "Turn Based Combat": "ターン制戦闘の進行とコマンド選択。",
    "Action System": "汎用アクション、共有アクション。",
    "AI": "索敵、ナビゲーション、攻撃ブレイン、ファクション。",
    "Objectives Mission System": "ミッション、目標ログ、目標ステーション UI。",
}


def main():
    editors = json.load(open(EDITORS, encoding="utf-8"))
    types = {t["Name"]: t for t in json.load(open(TYPES, encoding="utf-8"))}
    notes = json.load(open(NOTES, encoding="utf-8"))

    per_system = defaultdict(list)
    total = 0
    for name, ed in editors.items():
        t = types.get(name)
        if not t or t.get("IsEditor"):
            continue
        field_names = {f["Name"] for f in t["Fields"]}
        props = []
        for sec in ed["sections"]:
            for f in sec["fields"]:
                if f["prop"] in field_names and f["prop"] not in props:
                    props.append(f["prop"])
        if not props:
            continue
        covered = [p for p in props if p in notes.get(name, {})]
        if not covered:
            continue
        system = t["File"].split("/")[0]
        per_system[system].append((name, len(covered), t["File"]))
        total += len(covered)

    systems = sorted(per_system, key=lambda s: (-sum(x[1] for x in per_system[s]), s))

    lines = ["# インスペクター設定 日本語解説索引\n"]
    lines.append(
        "カスタムエディタで表示される設定項目に、コードの使われ方から書いた日本語の一行説明を付けました。"
        "説明は各コンポーネントページの「インスペクター設定」表の「補足」列に入っています。\n"
    )
    lines.append(f"- 対象: **{len(systems)} システム / {sum(len(v) for v in per_system.values())} コンポーネント / {total:,} 項目**\n")

    lines.append("## システム一覧\n")
    lines.append("| システム | コンポーネント | 項目数 |")
    lines.append("| --- | --- | --- |")
    for system in systems:
        n_components = len(per_system[system])
        n_fields = sum(x[1] for x in per_system[system])
        anchor = system.lower().replace(" ", "-")
        lines.append(f"| [{system}](#{anchor}) | {n_components} | {n_fields:,} |")

    for system in systems:
        entries = sorted(per_system[system], key=lambda x: (-x[1], x[0]))
        n_fields = sum(x[1] for x in entries)
        lines.append(f"\n## {system}\n")
        note = SYSTEM_NOTES.get(system)
        if note:
            lines.append(note + "\n")
        lines.append(f"`{system}/` — {len(entries)} コンポーネント / {n_fields:,} 項目\n")
        lines.append("| コンポーネント | 項目数 | ソース |")
        lines.append("| --- | --- | --- |")
        for name, n, path in entries:
            link = f"[`{name}`](reference/{system.replace(' ', '%20')}/{name}.md)"
            lines.append(f"| {link} | {n} | `{path}` |")

    lines.append("\n## 読み方\n")
    lines.append("- 「補足」列の先頭が日本語説明で、その後に `[Tooltip]` や表示条件が続きます。\n")
    lines.append("- 「表示条件」は、そのチェックがオンのときだけ表示される項目です。\n")
    lines.append("- 未使用の項目は「実行時参照なし」などと明記しています。\n")

    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote", OUT, "systems", len(systems), "fields", total)


if __name__ == "__main__":
    main()
