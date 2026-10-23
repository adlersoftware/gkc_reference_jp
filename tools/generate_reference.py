"""Render the GKC 3.77h reference from the extracted type/editor JSON.

Output:
  reference/_INDEX.md            system -> component index
  reference/<System>/<Type>.md   one page per component/type
  reference/gkc_api.json         compact machine-readable index
"""

import json
import os
import re
from collections import OrderedDict, defaultdict

BUILD = r"D:\dev\gkc_ref\build"
TYPES_JSON = os.path.join(BUILD, "types.json")
EDITORS_JSON = os.path.join(BUILD, "editors.json")
DOCS = r"D:\dev\gkc_ref\docs"
OUT = r"D:\dev\gkc_ref\reference"

UNITY_CALLBACKS = {
    "Awake", "Start", "Update", "FixedUpdate", "LateUpdate", "OnEnable", "OnDisable", "OnDestroy",
    "OnValidate", "Reset", "OnGUI", "OnDrawGizmos", "OnDrawGizmosSelected", "OnApplicationQuit",
    "OnApplicationPause", "OnApplicationFocus", "OnCollisionEnter", "OnCollisionExit", "OnCollisionStay",
    "OnTriggerEnter", "OnTriggerExit", "OnTriggerStay", "OnControllerColliderHit", "OnParticleCollision",
    "OnMouseDown", "OnMouseUp", "OnMouseDrag", "OnMouseEnter", "OnMouseExit", "OnMouseOver",
    "OnBecameVisible", "OnBecameInvisible", "OnPreRender", "OnPostRender", "OnRenderImage",
    "OnAudioFilterRead", "OnAnimatorIK", "OnAnimatorMove", "OnJointBreak", "OnTransformChildrenChanged",
    "OnTransformParentChanged", "OnCanvasGroupChanged", "OnRectTransformDimensionsChange",
    "OnBeforeTransformParentChanged", "OnDidApplyAnimationProperties", "OnStateEnter", "OnStateExit",
}

UNITY_TYPES = {
    "MonoBehaviour", "ScriptableObject", "Editor", "EditorWindow", "PropertyDrawer", "StateMachineBehaviour",
    "NetworkBehaviour", "Object", "Component", "Behaviour",
}


def esc(s):
    if s is None:
        return ""
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def pretty_label(field_name):
    """Unity-like nicified label: inventoryEnabled -> Inventory Enabled."""
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", field_name)
    s = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", s)
    s = s.replace("_", " ")
    parts = [p for p in s.split(" ") if p]
    return " ".join(p[:1].upper() + p[1:] for p in parts)


def camel_from_title(title):
    words = re.findall(r"[A-Za-z0-9]+", title)
    if not words:
        return ""
    head = words[0][:1].lower() + words[0][1:]
    return head + "".join(w[:1].upper() + w[1:] for w in words[1:])


class Reference:
    def __init__(self):
        self.types = json.load(open(TYPES_JSON, encoding="utf-8"))
        self.editors = json.load(open(EDITORS_JSON, encoding="utf-8"))
        self.by_name = defaultdict(list)
        for t in self.types:
            self.by_name[t["Name"]].append(t)
        self.runtime = [t for t in self.types if not t["IsEditor"]]
        self.docs = self.load_docs()
        self.notes = {}
        notes_path = r"D:\dev\gkc_ref\notes\method_notes.json"
        if os.path.exists(notes_path):
            self.notes = json.load(open(notes_path, encoding="utf-8"))
        self.field_notes = {}
        field_path = r"D:\dev\gkc_ref\notes\field_notes.json"
        if os.path.exists(field_path):
            self.field_notes = json.load(open(field_path, encoding="utf-8"))

    # ---------- docs matching ----------
    def load_docs(self):
        pages = {}
        if not os.path.isdir(DOCS):
            return pages
        for root, _d, files in os.walk(DOCS):
            for name in files:
                if not name.endswith(".md") or name in ("_INDEX.md",):
                    continue
                path = os.path.join(root, name)
                text = open(path, encoding="utf-8", errors="replace").read()
                m = re.search(r"^#\s+(.+)$", text, re.M)
                title = m.group(1).strip() if m else name[:-3]
                body = re.sub(r"^#.*$", "", text, flags=re.M).strip()
                body = re.sub(r"^>.*$", "", body, flags=re.M).strip()
                body = re.sub(r"\{\%.*?\%\}", "", body, flags=re.S)
                body = re.sub(r"!\[.*?\]\(.*?\)", "", body)
                body = re.sub(r"\n{2,}", "\n", body).strip()
                pages[os.path.relpath(path, DOCS).replace(os.sep, "/")] = (title, self.plain(body))
        return pages

    @staticmethod
    def plain(md):
        text = re.sub(r"```.*?```", "", md, flags=re.S)
        text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
        text = re.sub(r"&(?:#x?[0-9A-Fa-f]+|[a-zA-Z]+);", " ", text)
        text = re.sub(r"[*_`#>]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def doc_for(self, type_name):
        best = None
        for path, (title, body) in self.docs.items():
            candidate = camel_from_title(title)
            if candidate == type_name:
                score = 3
            elif type_name.lower() in body.lower():
                score = 1
            else:
                continue
            if best is None or score > best[0]:
                best = (score, path, title, body)
        return best

    # ---------- inheritance ----------
    def base_chain(self, t):
        seen = set()
        cur = t
        while cur:
            for b in cur.get("BaseTypes", []):
                name = b.split("<")[0].split(".")[-1]
                cands = self.by_name.get(name)
                if cands and name not in seen:
                    seen.add(name)
                    yield cands[0]
                    cur = cands[0]
                    break
            else:
                return

    def find_field(self, t, name):
        for f in t["Fields"]:
            if f["Name"] == name:
                return f
        for base in self.base_chain(t):
            for f in base["Fields"]:
                if f["Name"] == name:
                    return f
        return None

    # ---------- inspector ----------
    @staticmethod
    def is_serialized(f):
        mods = f["Modifiers"].split()
        if "const" in mods or "static" in mods or "readonly" in mods:
            return False
        attrs = {a["Name"] for a in f["Attributes"]}
        if "NonSerialized" in attrs or "HideInInspector" in attrs:
            return False
        if "public" in mods:
            return True
        return "SerializeField" in attrs

    def inspector(self, t):
        """Return list of sections: [{title, rows:[{label, field, type, init, note}]}]"""
        ed = self.editors.get(t["Name"])
        serialized = [f for f in t["Fields"] if self.is_serialized(f)]
        used = set()
        sections = []

        if ed and ed["sections"]:
            for sec in ed["sections"]:
                rows = []
                for item in sec["fields"]:
                    f = self.find_field(t, item["prop"])
                    if not f:
                        continue
                    used.add((f["Owner"] if "Owner" in f else t["Name"], f["Name"]))
                    rows.append(self.row(f, item["label"], item.get("cond"), t["Name"]))
                if rows:
                    sections.append({"title": sec["title"], "rows": rows})
        else:
            # default inspector: [Header] groups, declaration order
            cur = {"title": "", "rows": []}
            for f in serialized:
                header = None
                for a in f["Attributes"]:
                    if a["Name"] == "Header":
                        header = re.search(r'"([^"]*)"', a["Text"])
                        header = header.group(1) if header else None
                if header is not None and cur["rows"]:
                    sections.append(cur)
                    cur = {"title": header, "rows": []}
                elif header is not None and not cur["title"]:
                    cur["title"] = header
                cur["rows"].append(self.row(f, None, None, t["Name"]))
            if cur["rows"]:
                sections.append(cur)

        extra = []
        for f in serialized:
            if f["Name"] in {r["field"] for s in sections for r in s["rows"]}:
                continue
            extra.append(self.row(f, None, None, t["Name"]))
        return sections, extra

    @staticmethod
    def explain_cond(cond):
        """Turn `!foo.boolValue` into a Japanese display condition."""
        cond = cond.strip()
        neg = False
        core = cond
        if core.startswith("!") and "&&" not in core:
            neg = True
            core = core[1:].strip()
        m = re.fullmatch(r"\(?\s*([A-Za-z_]\w*)\.boolValue\s*\)?", core)
        if m:
            state = "オフ" if neg else "オン"
            return f"表示条件: `{m.group(1)}` が{state}のとき"
        if not neg and re.fullmatch(r"[A-Za-z_]\w*", core):
            return f"表示条件: `{core}` がオンのとき"
        return f"表示条件: `{cond}`"

    def row(self, f, label, cond=None, type_name=None):
        notes = []
        desc = self.field_notes.get(type_name or "", {}).get(f["Name"])
        if desc:
            notes.append(desc)
        if cond:
            notes.append(self.explain_cond(cond))
        for a in f["Attributes"]:
            if a["Name"] == "Tooltip":
                m = re.search(r'"([^"]*)"', a["Text"])
                if m:
                    notes.append(m.group(1))
            elif a["Name"] in ("Range", "TextArea", "Multiline", "Min"):
                notes.append(a["Text"])
        return {
            "label": label or pretty_label(f["Name"]),
            "field": f["Name"],
            "type": f["Type"],
            "init": f["Init"] or "",
            "note": " / ".join(notes),
            "comment": f.get("Comment") or "",
            "line": f["Line"],
        }

    # ---------- methods ----------
    def split_methods(self, t):
        api, static, callbacks, overrides = [], [], [], []
        for m in t["Methods"]:
            mods = m["Modifiers"]
            if "public" not in mods and "protected" not in mods:
                continue
            name = m["Name"]
            if name in UNITY_CALLBACKS or (name.startswith("On") and m["IsOverride"]):
                callbacks.append(m)
            elif m["IsOverride"]:
                overrides.append(m)
            elif m["IsStatic"]:
                static.append(m)
            else:
                api.append(m)
        return api, static, callbacks, overrides


SYSTEM_NOTES = {
    "Abilities System": "アビリティの定義・実行（クールダウン、コスト、UI 連携）。",
    "Action System": "「乗る・開ける・掴む」などを共通化する汎用アクション機構。",
    "AI": "敵 AI の知覚・ターゲット管理・攻撃・巡回・ナビゲーション。",
    "Audio": "サウンド再生と AudioSource のプール。",
    "Camera": "プレイヤーカメラ、カメラステート、カットシーン、画面揺れ。",
    "Character Aspect Customization System": "見た目（アーマー・服）の差し替えとカスタマイズ。",
    "Checkpoint": "チェックポイントとリスポーン位置の管理。",
    "Climb System": "崖のぼり・はしご・レールスライドなどの移動系。",
    "Combat System": "近接戦闘、ダメージ処理、ヒットリアクション。",
    "Condition System": "フラグ・所持品・体力などの条件判定と結果実行。",
    "Crafting System": "レシピ・素材・作業台によるクラフト。",
    "Decal": "弾痕や足跡などのデカール描画。",
    "Demo": "デモシーン専用の補助スクリプト。",
    "Devices": "端末・スイッチ・ドアなど、調べたり操作したりする装置。",
    "Dialog System": "会話 UI と会話データの再生。",
    "Event System": "汎用イベント／トリガーの連携用。",
    "Experience System": "経験値とレベルの管理。",
    "Foot Step": "足音の再生制御。",
    "Game Manager": "ゲーム全体の管理（ポーズ、設定、シーン）。",
    "Grab Objects": "物理ベースの掴み・運搬。",
    "Gravity": "重力方向の変更や重力操作。",
    "Head Track": "頭部の注視（IK）。",
    "Health": "体力・ダメージ・回復・無敵。",
    "Hide System": "物陰に隠れる／隠れられる仕組み。",
    "Input": "入力マネージャとアクション定義。",
    "Inventory": "所持品・銀行・ベンダー・装備・重量・カテゴリ。",
    "Ladder System": "はしごの昇降。",
    "Level Manager": "シーン／レベルの遷移と管理。",
    "Localization System": "多言語対応。",
    "Map": "マップ表示とマップオブジェクト情報。",
    "Menu": "ポーズ・オプション・セーブなどのメニュー UI。",
    "Mobile": "タッチ操作、ジョイスティック、モバイル UI。",
    "Objectives Mission System": "ミッション／目標の管理と表示。",
    "Online System": "ネットワーク連携（Mirror など）。",
    "Others": "共通ユーティリティと小物。",
    "Override System": "キャラクター制御の上書き（乗車中など）。",
    "Panel Info System": "パネルに表示する情報の管理。",
    "PickUps": "拾えるアイテム。",
    "Player": "プレイヤーコントローラ本体と移動・状態管理。",
    "Point And Click": "ポイント＆クリック操作。",
    "Pooling System": "オブジェクトプール。",
    "Powers": "特殊能力（テレキネシス、時間操作など）。",
    "Puzzles": "パズル系の仕掛け。",
    "Save System": "セーブ／ロード。",
    "Skills System": "スキルツリーとスキルポイント。",
    "Stats System": "ステータス（攻撃力・防御力など）。",
    "Turn Based Combat": "ターン制戦闘。",
    "Tutorial System": "チュートリアル表示。",
    "Vehicles": "乗り物の運転・搭乗。",
    "Vendor System": "売買（ベンダー）。",
    "Weapons": "射撃・近接武器、アタッチメント、弾薬。",
}


def type_kind_jp(ref, t):
    kind = t["Kind"]
    chain = set(t.get("BaseTypes", []))
    for b in ref.base_chain(t):
        chain.update(b.get("BaseTypes", []))
        chain.add(b["Name"])
    if "MonoBehaviour" in chain:
        return "MonoBehaviour（コンポーネント）"
    if "ScriptableObject" in chain:
        return "ScriptableObject（データアセット）"
    if kind == "enum":
        return "enum"
    if kind == "interface":
        return "interface"
    if kind == "struct":
        return "struct"
    return "class"


def render_type(ref, t):
    lines = []
    name = t["Name"]
    lines.append(f"# {name}\n")
    src = f"{t['File']}:{t['Line']}"
    lines.append(f"- **種別**: {type_kind_jp(ref, t)}")
    if t["BaseTypes"]:
        lines.append(f"- **継承 / 実装**: {', '.join('`' + b + '`' for b in t['BaseTypes'])}")
    if t["Namespace"]:
        lines.append(f"- **namespace**: `{t['Namespace']}`")
    lines.append(f"- **ソース**: `{src}`")
    if t["Attributes"]:
        attrs = ", ".join("`" + a["Text"] + "`" for a in t["Attributes"][:6])
        lines.append(f"- **属性**: {attrs}")
    lines.append("")

    summary = ref.notes.get(name, {}).get("summary")
    if summary:
        lines.append(f"**概要**: {summary}\n")

    doc = ref.doc_for(name)
    if t["Doc"]:
        lines.append(f"> {t['Doc']}\n")
    if doc:
        _score, path, title, body = doc
        snippet = body[:900].strip()
        if len(body) > 900:
            snippet += "…"
        lines.append(f"**公式ドキュメント抜粋**（[{title}](../../docs/{path})）\n")
        lines.append(f"> {snippet}\n")

    if t["Kind"] == "enum":
        lines.append("## 値\n")
        lines.append("| 名前 | 値 | 説明 |")
        lines.append("| --- | --- | --- |")
        for m in t["EnumMembers"]:
            lines.append(f"| `{m['Name']}` | {esc(m['Value']) or '–'} | {esc(m['Doc']) or '–'} |")
        lines.append("")
        return "\n".join(lines)

    sections, extra = ref.inspector(t)
    serialized = [f for f in t["Fields"] if ref.is_serialized(f)]
    if sections or extra:
        lines.append("## インスペクター設定\n")
        ed = ref.editors.get(name)
        if ed:
            lines.append("カスタムエディタで表示順・表示名が制御されています。\n")
        for sec in sections:
            title = sec["title"] or "（セクションなし）"
            lines.append(f"### {title}\n")
            lines.append("| ラベル | フィールド | 型 | 既定値 | 補足 |")
            lines.append("| --- | --- | --- | --- | --- |")
            for r in sec["rows"]:
                fields = f"`{r['field']}`"
                note = esc(r["note"]) or esc(r["comment"]) or "–"
                init = esc(r["init"]) or "–"
                if len(init) > 40:
                    init = init[:37] + "…"
                lines.append(f"| {esc(r['label'])} | {fields} | `{esc(r['type'])}` | {init} | {note} |")
            lines.append("")
        if extra:
            lines.append("### その他（コードから設定する項目など）\n")
            lines.append("| フィールド | 型 | 既定値 | 補足 |")
            lines.append("| --- | --- | --- | --- |")
            for r in extra:
                init = esc(r["init"]) or "–"
                if len(init) > 40:
                    init = init[:37] + "…"
                lines.append(f"| `{r['field']}` | `{esc(r['type'])}` | {init} | {esc(r['note']) or '–'} |")
            lines.append("")

    events = [f for f in t["Fields"] if "UnityEvent" in f["Type"]]
    api, static, callbacks, overrides = ref.split_methods(t)

    if api:
        lines.append("## 公開メソッド\n")
        lines.append("| シグネチャ | 説明 |")
        lines.append("| --- | --- |")
        type_notes = ref.notes.get(name, {}).get("methods", {})
        for m in api:
            desc = type_notes.get(m["Signature"]) or m["Doc"] or "–"
            lines.append(f"| `{esc(m['Signature'])}` | {esc(desc)} |")
        lines.append("")
    if static:
        lines.append("## 静的メソッド\n")
        lines.append("| シグネチャ | 説明 |")
        lines.append("| --- | --- |")
        for m in static:
            lines.append(f"| `static {esc(m['ReturnType'])} {esc(m['Signature'])}` | {esc(m['Doc']) or '–'} |")
        lines.append("")
    if events:
        lines.append("## Unity イベント\n")
        lines.append("| フィールド | 型 | 説明 |")
        lines.append("| --- | --- | --- |")
        for f in events:
            tooltip = ""
            for a in f["Attributes"]:
                if a["Name"] == "Tooltip":
                    m = re.search(r'"([^"]*)"', a["Text"])
                    if m:
                        tooltip = m.group(1)
            lines.append(f"| `{f['Name']}` | `{esc(f['Type'])}` | {esc(tooltip) or '–'} |")
        lines.append("")
    if callbacks or overrides:
        lines.append("<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>\n")
        names = sorted({m["Signature"] for m in callbacks + overrides})
        lines.append(", ".join(f"`{esc(n)}`" for n in names))
        lines.append("\n</details>\n")

    nested = [x for x in ref.types if x.get("ContainingType") == name]
    if nested:
        lines.append("## 内部型\n")
        for n in nested:
            lines.append(f"- `{n['Name']}`（{n['Kind']}）")
        lines.append("")

    return "\n".join(lines)


def main():
    ref = Reference()
    os.makedirs(OUT, exist_ok=True)

    groups = defaultdict(list)
    for t in ref.runtime:
        if t["IsNested"]:
            continue
        folder = os.path.dirname(t["File"]).replace("\\", "/")
        system = folder.split("/")[0] if folder else "Root"
        groups[system].append(t)

    index_lines = ["# Game Kit Controller 3.77h リファレンス\n",
                   "インストール済みアセット（`Assets/Game Kit Controller/Scripts`）から自動生成。\n",
                   "各ページは「インスペクター設定」と「公開メソッド」を中心に構成しています。\n"]

    total = 0
    api_json = []
    for system in sorted(groups):
        types = sorted(groups[system], key=lambda x: x["Name"].lower())
        os.makedirs(os.path.join(OUT, system), exist_ok=True)
        index_lines.append(f"\n## {system}（{len(types)}）\n")
        note = SYSTEM_NOTES.get(system)
        if note:
            index_lines.append(f"{note}\n")
        for t in types:
            page = render_type(ref, t)
            with open(os.path.join(OUT, system, t["Name"] + ".md"), "w", encoding="utf-8", newline="\n") as fh:
                fh.write(page)
            total += 1
            desc = ""
            if t["Doc"]:
                desc = t["Doc"].split("\n")[0]
            n_fields = len([f for f in t["Fields"] if ref.is_serialized(f)])
            n_api = len([m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"]])
            meta = f"（設定 {n_fields} / API {n_api}）" if (n_fields or n_api) else ""
            index_lines.append(f"- [`{t['Name']}`]({system.replace(' ', '%20')}/{t['Name']}.md) {meta}".rstrip())
            if desc:
                index_lines.append(f"  {esc(desc)}")
            api_json.append({
                "name": t["Name"],
                "kind": t["Kind"],
                "base": t["BaseTypes"],
                "file": t["File"],
                "line": t["Line"],
                "fields": len([f for f in t["Fields"] if ref.is_serialized(f)]),
                "methods": len([m for m in t["Methods"] if "public" in m["Modifiers"]]),
            })

    with open(os.path.join(OUT, "_INDEX.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(index_lines) + "\n")
    with open(os.path.join(OUT, "gkc_api.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(api_json, fh, ensure_ascii=False, indent=0)

    print("pages:", total, "systems:", len(groups))


if __name__ == "__main__":
    main()
