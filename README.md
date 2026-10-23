# Game Kit Controller — リファレンス調査とオフラインミラー

対象アセット: `D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts`
確認したバージョン: **GKC 3.77h**（`Scripts/Editor/assetVersionWindow.cs` の表記）
プロジェクト: Unity **6000.4.12f1**

---

## 結論

**「API リファレンス」と呼べる公式資料は存在しません。**
あるのは ①同梱 PDF（3.7 / 112 ページ / スクリーンショット中心）②公式 GitBook（318 ページ、ほぼ 2022 年更新）③チェンジログ ④フォーラム・Discord・YouTube ⑤ソースコードそのもの、です。

公式ドキュメントは「コンポーネントの画面説明 + 画像」が中心で、テキストは薄いままです。
（GitBook ミラー実測: 318 ページ合計 455 KB、中央値 0.6 KB/ページ、202 ページが 1 KB 未満）

---

## 1. 公式ソース一覧

| 種別 | 場所 | 内容 | 鮮度 |
|---|---|---|---|
| 同梱 PDF（本命） | `Assets/Game Kit Controller/Documentation/Game Kit Controller Documentation 3.7 First steps and basic use.pdf` | 112 ページ / 25 MB。セットアップ、キャラクター作成、武器、マップ、マルチプレイ、UI、AI、既知の問題 | 3.7（2022 頃）。現行 3.77h とほぼ同世代 |
| 公式 GitBook | https://game-kit-controller.gitbook.io/docs/ | 318 ページ。主要システム / プレイヤーコンポーネント / 追加マネージャ / AI / 統合 | 大半 2022 年、FAQ のみ 2025-01 |
| 旧 PDF | `Documentation/Old documentation/Game Kit Controller Documentation 2.4d.pdf` | 2.4d 版。作者が「first steps 以外は古い」と明記 | 2.4d |
| チェンジログ | `Documentation/Changelog/*.pdf`（2.4c〜3.6） | バージョンごとの追加点。テキストが最も密 | 3.6 まで |
| 統合資料 | `Documentation/Integrations/`（EBS 3.7 / Emerald AI / Universal AI / UMA） | 外部アセット連携手順 | 3.7 系 |
| 公式フォーラム | https://discussions.unity.com/t/released-game-kit-controller-engine-with-melee-weapons-vehicles-crafting-more-3-76/595741 | 作者サポート。3.77h の変更点はここ/Discord | 現行 |
| Discord | https://discord.gg/kUpeRZ8 | 実質一次情報。※アセット内の URL は二重連結で壊れている | 現行 |
| YouTube | https://youtu.be/lZB_5b4tUm0?list=PLYVCbGEtbhxVjZ9C41fwTDynTpVkCP9iA | チュートリアル動画プレイリスト | — |
| 公開リポジトリ | https://github.com/sr3888/GKC-Public-Repository | デモ用アニメーション・Slice/Limb Hacker・Mirror 連携。**ドキュメントではない** | 3.78 まで |

エディタ内: メニュー **Game Kit Controller > About GKC** に上記リンクのボタンがあります。

---

## 2. コード側の「リファレンス密度」

| 指標 | 実測値 |
|---|---|
| C# ファイル | 1,127 |
| 行数 | 493,752 行（15.8 MB） |
| 型宣言（class/struct/enum/interface） | 1,667 |
| MonoBehaviour | 645 |
| `///` XML ドキュメント行 | **127**（全体の 0.03%） |
| `[Tooltip]` | 45 |
| `HelpBox` 呼び出し | 88 |
| asmdef | 0（全て Assembly-CSharp） |
| namespace あり | 24 ファイルのみ（ほぼグローバル名前空間） |
| デモシーン / プレハブ | 78 / 1,867 |

→ クラス名・フィールド名・インスペクタ表示が実質的な仕様書です。

---

## 3. このワークスペースに作ったもの

```
GUIDE.md                   リファレンスの読み方・設計前提・呼び出し例（まずこれ）
REFERENCES.md              全 51 システムの索引（各システム 1 ファイル）
INSPECTOR_REFERENCE.md     インスペクター設定の日本語解説索引（103 コンポーネント / 約 4,100 項目）
*_REFERENCE.md             システム別のメソッド注釈（日本語・1 行ずつ）
PLAYER_REFERENCE.md        統合版（Player / Camera / Weapons / Inventory / Health）
reference/                 3.77h ソース由来のリファレンス（998 型 / 3.2 MB）
  _INDEX.md                システム別の全型一覧（設定数・API 数付き）
  <システム>/<型名>.md      インスペクター設定（日本語説明付き） + 公開メソッド + Unity イベント
  gkc_api.json             型名 / 継承 / ファイル / 件数の索引
notes/
  method_notes.json        メソッド注釈の元データ（型サマリ + メソッド説明）
  field_notes.json         インスペクター項目の日本語説明（元データ）
docs/                      GitBook 全 318 ページの Markdown ミラー
  _INDEX.md                ページ一覧（階層ツリー）
  index.md                 Welcome ページ
  llms.txt                 GitBook 公式の全ページ索引
sources/
  gkc_3.7_documentation.txt  同梱 PDF をテキスト化（112 ページ、読みやすく整形）
  pdf_text_raw.txt           抽出そのまま（ページ区切り付き）
tools/
  GkcExtract/              Roslyn で全 .cs を解析し types.json を生成
  parse_editors.py         カスタムエディタからインスペクター構成・表示条件を抽出
  generate_reference.py    Markdown リファレンス生成
  mirror_docs.py           GitBook → Markdown 取得（並列 6、.md エンドポイント使用）
  postprocess_docs.py      バナー除去・索引再生成
  extract_pdf.py           PDF テキスト抽出（ToUnicode CMap 対応の自作パーサ）
  clean_pdf_text.py        1 文字ずつバラけた PDF テキストの整形
```

補足:
- GitBook は各ページ URL に `.md` を付けると Markdown が返ります。`/docs/llms.txt` が全ページ索引です。
- PDF 抽出テキストは画像（スクリーンショット）を含みません。図が必要なら PDF を直接参照してください。
- 再生成: GitBook は `python tools/mirror_docs.py` → `postprocess_docs.py`、リファレンスは `GUIDE.md` の「8. 再生成」。

---

## 4. 次にやると効くこと

1. **インスペクター項目の意味** — 完了（103 コンポーネント / 約 4,100 項目）。
2. **チェンジログの横断索引** — 3.03〜3.6 の PDF から「どのバージョンで何が入ったか」を検索可能に。
3. **デモシーン逆引き表** — 78 シーン × 使用コンポーネントの対応表（「この機能の実例はどのシーンか」が引ける）。
