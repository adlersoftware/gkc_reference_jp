import json
import os
from collections import defaultdict

ROOT = r"D:\dev\gkc_ref"
TYPES = os.path.join(ROOT, "build", "types.json")
NOTES = os.path.join(ROOT, "notes", "method_notes.json")

# system folder -> (output file, Japanese title, one-line description)
SYSTEMS = {
    "Grab Objects": ("GRAB_OBJECTS", "Grab Objects", "物を掴む・運ぶ・投げる・近接攻撃までを担う物理グラブ系。"),
    "Others": ("OTHERS", "Others", "共通ユーティリティ、スポナー、スキャナー、UI 補助など雑多なコンポーネント群。"),
    "Map": ("MAP", "Map", "マップ生成・表示・マップオブジェクト情報。"),
    "Powers": ("POWERS", "Powers", "テレキネシス、時間操作、重力操作などの特殊能力。"),
    "Menu": ("MENU", "Menu", "ポーズメニュー、インゲームメニュー、シーンロード。"),
    "Gravity": ("GRAVITY", "Gravity", "重力方向の変更、無重力エリア、車両の重力制御。"),
    "Game Manager": ("GAME_MANAGER", "Game Manager", "ゲーム全体の管理（ポーズ、設定、シーン、入力設定の保存）。"),
    "Turn Based Combat": ("TURN_BASED_COMBAT", "Turn Based Combat", "ターン制戦闘の進行とコマンド選択。"),
    "Override System": ("OVERRIDE_SYSTEM", "Override System", "キャラクター制御の上書き（乗車・デバイス使用中など）。"),
    "Character Aspect Customization System": ("CHARACTER_ASPECT", "Character Aspect Customization System", "見た目パーツ（アーマー・服）の差し替え。"),
    "Point And Click": ("POINT_AND_CLICK", "Point And Click", "ポイント＆クリック操作。"),
    "Vendor System": ("VENDOR", "Vendor System", "売買（ベンダー）の在庫・価格・UI。"),
    "Localization System": ("LOCALIZATION", "Localization System", "多言語テーブルとキー解決。"),
    "Head Track": ("HEAD_TRACK", "Head Track", "頭部の注視（IK）。"),
    "Climb System": ("CLIMB", "Climb System", "はしご・崖のぼり。"),
    "Puzzles": ("PUZZLES", "Puzzles", "パズル系の仕掛けと状態管理。"),
    "Experience System": ("EXPERIENCE", "Experience System", "経験値・レベル。"),
    "Foot Step": ("FOOT_STEP", "Foot Step", "足音の再生制御。"),
    "Tutorial System": ("TUTORIAL", "Tutorial System", "チュートリアル表示と進行。"),
    "Hide System": ("HIDE", "Hide System", "物陰に隠れる仕組み。"),
    "Demo": ("DEMO", "Demo", "デモシーン専用の補助スクリプト。"),
    "Level Manager": ("LEVEL_MANAGER", "Level Manager", "シーン遷移とレベル管理。"),
    "Pooling System": ("POOLING", "Pooling System", "オブジェクトプール。"),
    "Condition System": ("CONDITION", "Condition System", "条件判定と結果実行。"),
    "Ladder System": ("LADDER", "Ladder System", "はしごの昇降。"),
    "Mobile": ("MOBILE", "Mobile", "モバイル向け UI・入力補助。"),
    "Checkpoint": ("CHECKPOINT", "Checkpoint", "チェックポイントとリスポーン。"),
    "Audio": ("AUDIO", "Audio", "サウンド再生と AudioSource 管理。"),
    "Panel Info System": ("PANEL_INFO", "Panel Info System", "パネル表示情報の管理。"),
    "Decal": ("DECAL", "Decal", "デカール描画。"),
    "Online System": ("ONLINE", "Online System", "ネットワーク連携。"),
}

EXISTING = [
    ("Player / Camera / Weapons / Inventory / Health", "PLAYER_REFERENCE.md"),
    ("AI", "AI_REFERENCE.md"),
    ("Dialog / Event", "DIALOG_EVENT_REFERENCE.md"),
    ("Weapons", "WEAPONS_REFERENCE.md"),
    ("Action System", "ACTION_REFERENCE.md"),
    ("Inventory", "INVENTORY_REFERENCE.md"),
    ("Save System", "SAVE_REFERENCE.md"),
    ("Abilities System", "ABILITIES_REFERENCE.md"),
    ("Objectives Mission System", "OBJECTIVES_REFERENCE.md"),
    ("Vehicles", "VEHICLES_REFERENCE.md"),
    ("PickUps", "PICKUPS_REFERENCE.md"),
    ("Stats System", "STATS_REFERENCE.md"),
    ("Camera", "CAMERA_REFERENCE.md"),
    ("Combat System", "COMBAT_REFERENCE.md"),
    ("Devices", "DEVICES_REFERENCE.md"),
    ("Health", "HEALTH_REFERENCE.md"),
    ("Input", "INPUT_REFERENCE.md"),
    ("Skills System", "SKILLS_REFERENCE.md"),
    ("Crafting System", "CRAFTING_REFERENCE.md"),
]


def main():
    types = json.load(open(TYPES, encoding="utf-8"))
    notes = json.load(open(NOTES, encoding="utf-8"))

    by_system = defaultdict(list)
    for t in types:
        if t["IsEditor"] or t["IsNested"]:
            continue
        system = t["File"].split("/")[0]
        if system not in SYSTEMS:
            continue
        ms = [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]
        if not ms:
            continue
        by_system[system].append(t)

    summary_rows = []
    for system, (fname, title, desc) in SYSTEMS.items():
        entries = by_system.get(system, [])
        if not entries:
            continue
        entries.sort(key=lambda t: -len(t["Methods"]))
        total_methods = total_notes = 0
        groups = defaultdict(list)
        for t in entries:
            n_methods = len([m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]])
            n_notes = len(notes.get(t["Name"], {}).get("methods", {}))
            total_methods += n_methods
            total_notes += min(n_notes, n_methods)
            folder = os.path.dirname(t["File"]).replace("\\", "/")
            sub = folder.split("/", 1)[1] if "/" in folder else "（直下）"
            groups[sub].append((t["Name"], n_methods, n_notes))

        lines = [f"# {title} メソッドリファレンス\n"]
        lines.append(
            f"`Assets/Game Kit Controller/Scripts/{system}/` 以下のコンポーネントについて、public メソッドの実装を読んで"
            "日本語の一行解説を付けたものです（GKC 3.77h）。\n"
        )
        lines.append(f"- 対象: **{len(entries)} 型 / {total_methods:,} メソッド**")
        lines.append(f"- 注釈付き: **{total_notes:,} メソッド**（{total_notes / max(total_methods, 1) * 100:.0f}%）")
        lines.append(f"- 生成元: 各 `.cs` の実装。{desc}\n")

        for group in sorted(groups):
            lines.append(f"## {group}\n")
            lines.append("| 型 | 概要 | 注釈 |")
            lines.append("| --- | --- | --- |")
            for name, n_methods, n_notes in sorted(groups[group], key=lambda x: -x[1]):
                summary = notes.get(name, {}).get("summary", "")
                link = f"[`{name}`](reference/{system.replace(' ', '%20')}/{name}.md)"
                lines.append(f"| {link} | {summary or '–'} | {n_notes}/{n_methods} |")
            lines.append("")

        lines.append("# 注釈の読み方\n")
        lines.append(
            "- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。\n"
            "- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。\n"
            "- 空実装は「本体が空で何もしない」と明記しています。\n"
            "- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。\n"
        )

        out = os.path.join(ROOT, f"{fname}_REFERENCE.md")
        with open(out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(lines) + "\n")
        summary_rows.append((title, fname, len(entries), total_methods, total_notes))
        print(f"wrote {fname}_REFERENCE.md  types={len(entries)} methods={total_methods} notes={total_notes}")

    # master index
    idx = ["# GKC 3.77h システム別リファレンス索引\n",
           "各システムのメソッド注釈（日本語）への入口です。\n"]
    idx.append("| システム | 型 | メソッド | 注釈 | ファイル |")
    idx.append("| --- | --- | --- | --- | --- |")
    for title, fname, n_types, n_methods, n_notes in sorted(summary_rows, key=lambda x: -x[2 + 1]):
        idx.append(f"| {title} | {n_types} | {n_methods:,} | {n_notes:,} | [`{fname}_REFERENCE.md`]({fname}_REFERENCE.md) |")
    idx.append("")
    idx.append("## 既存の統合ファイル\n")
    for label, fname in EXISTING:
        idx.append(f"- {label}: [`{fname}`]({fname})")
    idx.append("")
    with open(os.path.join(ROOT, "REFERENCES.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(idx) + "\n")
    print("wrote REFERENCES.md")


if __name__ == "__main__":
    main()
