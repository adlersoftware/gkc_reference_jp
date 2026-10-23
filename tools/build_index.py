import json
import os
from collections import defaultdict

ROOT = r"D:\dev\gkc_ref"
TYPES = os.path.join(ROOT, "build", "types.json")
NOTES = os.path.join(ROOT, "notes", "method_notes.json")
OUT = os.path.join(ROOT, "REFERENCES.md")

# system -> reference file
FILE_MAP = {
    "Player": "PLAYER_REFERENCE.md",
    "Camera": "CAMERA_REFERENCE.md",
    "Weapons": "WEAPONS_REFERENCE.md",
    "Inventory": "INVENTORY_REFERENCE.md",
    "Health": "HEALTH_REFERENCE.md",
    "AI": "AI_REFERENCE.md",
    "Dialog System": "DIALOG_EVENT_REFERENCE.md",
    "Event System": "DIALOG_EVENT_REFERENCE.md",
    "Action System": "ACTION_REFERENCE.md",
    "Save System": "SAVE_REFERENCE.md",
    "Abilities System": "ABILITIES_REFERENCE.md",
    "Objectives Mission System": "OBJECTIVES_REFERENCE.md",
    "Vehicles": "VEHICLES_REFERENCE.md",
    "PickUps": "PICKUPS_REFERENCE.md",
    "Stats System": "STATS_REFERENCE.md",
    "Combat System": "COMBAT_REFERENCE.md",
    "Devices": "DEVICES_REFERENCE.md",
    "Input": "INPUT_REFERENCE.md",
    "Skills System": "SKILLS_REFERENCE.md",
    "Crafting System": "CRAFTING_REFERENCE.md",
    "Grab Objects": "GRAB_OBJECTS_REFERENCE.md",
    "Others": "OTHERS_REFERENCE.md",
    "Map": "MAP_REFERENCE.md",
    "Powers": "POWERS_REFERENCE.md",
    "Menu": "MENU_REFERENCE.md",
    "Gravity": "GRAVITY_REFERENCE.md",
    "Game Manager": "GAME_MANAGER_REFERENCE.md",
    "Turn Based Combat": "TURN_BASED_COMBAT_REFERENCE.md",
    "Override System": "OVERRIDE_SYSTEM_REFERENCE.md",
    "Character Aspect Customization System": "CHARACTER_ASPECT_REFERENCE.md",
    "Point And Click": "POINT_AND_CLICK_REFERENCE.md",
    "Vendor System": "VENDOR_REFERENCE.md",
    "Localization System": "LOCALIZATION_REFERENCE.md",
    "Head Track": "HEAD_TRACK_REFERENCE.md",
    "Climb System": "CLIMB_REFERENCE.md",
    "Puzzles": "PUZZLES_REFERENCE.md",
    "Experience System": "EXPERIENCE_REFERENCE.md",
    "Foot Step": "FOOT_STEP_REFERENCE.md",
    "Tutorial System": "TUTORIAL_REFERENCE.md",
    "Hide System": "HIDE_REFERENCE.md",
    "Demo": "DEMO_REFERENCE.md",
    "Level Manager": "LEVEL_MANAGER_REFERENCE.md",
    "Pooling System": "POOLING_REFERENCE.md",
    "Condition System": "CONDITION_REFERENCE.md",
    "Ladder System": "LADDER_REFERENCE.md",
    "Mobile": "MOBILE_REFERENCE.md",
    "Checkpoint": "CHECKPOINT_REFERENCE.md",
    "Audio": "AUDIO_REFERENCE.md",
    "Panel Info System": "PANEL_INFO_REFERENCE.md",
    "Decal": "DECAL_REFERENCE.md",
    "Online System": "ONLINE_REFERENCE.md",
}


def main():
    types = json.load(open(TYPES, encoding="utf-8"))
    notes = json.load(open(NOTES, encoding="utf-8"))

    stats = defaultdict(lambda: [0, 0, 0])
    for t in types:
        if t["IsEditor"] or t["IsNested"]:
            continue
        system = t["File"].split("/")[0]
        ms = [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]
        if not ms:
            continue
        sigs = {m["Signature"] for m in ms}
        have = sigs & set(notes.get(t["Name"], {}).get("methods", {}))
        stats[system][0] += 1
        stats[system][1] += len(sigs)
        stats[system][2] += len(have)

    lines = ["# GKC 3.77h システム別リファレンス索引\n",
             "全 51 システムのメソッド注釈（日本語）への入口です。各システム 1 ファイルで、"
             "型ごとの概要と public メソッドの一行解説を収録しています。\n"]

    total_types = sum(v[0] for v in stats.values())
    total_methods = sum(v[1] for v in stats.values())
    total_notes = sum(v[2] for v in stats.values())
    lines.append(f"- 型: **{total_types:,}** / メソッド: **{total_methods:,}** / 注釈: **{total_notes:,}**"
                 f"（{total_notes / max(total_methods,1) * 100:.0f}%）\n")

    lines.append("| システム | 型 | メソッド | 注釈 | ファイル |")
    lines.append("| --- | --- | --- | --- | --- |")
    for system in sorted(stats, key=lambda s: -stats[s][1]):
        n_types, n_methods, n_notes = stats[system]
        fname = FILE_MAP.get(system, "")
        link = f"[`{fname}`]({fname})" if fname else "–"
        lines.append(f"| {system} | {n_types} | {n_methods:,} | {n_notes:,} | {link} |")
    lines.append("")

    lines.append("## 読み方\n")
    lines.append("- 各ファイルの「型の一覧」から、型ごとのページ（`reference/<システム>/<型名>.md`）に移動できます。\n")
    lines.append("- 型ページには「インスペクター設定」「公開メソッド（注釈付き）」「Unity イベント」が入っています。\n")
    lines.append("- 注釈は実装を読んで書いた一行説明です。空実装は「本体が空で何もしない」と明記しています。\n")

    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote REFERENCES.md", total_types, total_methods, total_notes)


if __name__ == "__main__":
    main()
