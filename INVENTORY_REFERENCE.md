# Inventory コンポーネント メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Inventory/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **26 型 / 629 メソッド**
- 注釈付き: **629 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

中心は `inventoryManager`（所持品・装備・ドロップ）で、UI は `inventoryListManager` / `inventoryQuickAccessSlotsSystem` / `inventoryBankUISystem`、データは `inventoryInfo` / `inventoryObject` が担います。

## インベントリ中核

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`inventoryManager`](reference/Inventory/inventoryManager.md) | プレイヤーの所持品`inventoryList`を保持し、拾得・使用・装備と解除・ドロップ・合成・耐久度・スロットUI・イベント通知を扱うインベントリの中核コンポーネントです。アイテム定義やプレハブは`mainInventoryListManager`から取得し、クイックアクセス枠やポーズメニューとも連携します。 | 256/256 |
| [`inventoryBankUISystem`](reference/Inventory/inventoryBankUISystem.md) | プレイヤー在庫とインベントリバンクの間でアイテムを移す UI を管理するコンポーネント。メニューの開閉、アイコン生成、ドラッグ&ドロップや数量指定、カメラの回転/ズームを扱う。 | 49/49 |
| [`inventoryListManager`](reference/Inventory/inventoryListManager.md) | インベントリのカテゴリと `inventoryInfo` の一覧を保持・編集するマネージャ。名前からの検索、カテゴリ/オブジェクトの追加・削除、プレハブ生成、一覧の保存/読み込みを提供する。 | 43/43 |
| [`useInventoryObject`](reference/Inventory/useInventoryObject.md) | インベントリの必要オブジェクトを使って装置や鍵を解錠するコンポーネント。使用型（メニュー/ボタン/自動/サイド）ごとの選択処理と、解錠イベント・効果音・遅延イベントを管理する。 | 39/39 |
| [`inventoryCharacterCustomizationSystem`](reference/Inventory/inventoryCharacterCustomizationSystem.md) | 防具・服ピースの装備/解除と外見カスタマイズメニューを制御するコンポーネント。装備時のステータス/スキル/耐性/アビリティ適用、フルセット判定、ピースのドロップと耐久値の保存を担う。 | 37/37 |
| [`inventoryBankSystem`](reference/Inventory/inventoryBankSystem.md) | 銀行（ベンダー）在庫を保持し、開閉アニメ・効果音・メニュー表示を制御するコンポーネント。在庫リストの生成/追加/削除、ランダム排出、空イベント、外部のメインバンクへの委譲を担う。 | 18/18 |
| [`inventoryManagerInfo`](reference/Inventory/inventoryManagerInfo.md) | プレイヤーのインベントリ情報（スロット数・無限スロット・保存/読込設定・最後の武器名・空状態）を保持する基底コンポーネント。多くの処理は派生クラス向けの空実装として用意されている。 | 18/18 |
| [`inventoryWeightManager`](reference/Inventory/inventoryWeightManager.md) | プレイヤーの所持重量と重量上限を管理するコンポーネント。インベントリ全体の重量を集計して UI とイベントに反映し、オブジェクトを運べるかも判定する。 | 12/12 |
| [`playerInventoryCategoriesListManager`](reference/Inventory/playerInventoryCategoriesListManager.md) | インベントリのカテゴリ一覧パネルと、カテゴリ選択によるスロット表示の絞り込みを管理する UI コンポーネント。複数カテゴリの同時選択にも対応する。 | 12/12 |
| [`inventoryBankManager`](reference/Inventory/inventoryBankManager.md) | インベントリの「銀行（倉庫）」側の在庫リストを管理するコンポーネント。起動時に `inventoryListManager` から在庫を複製し、名前指定で追加・数量取得・削除とエディタ用ヘルパーを提供する。 | 11/11 |
| [`currencySystem`](reference/Inventory/currencySystem.md) | 所持金 `currentMoneyAmount` を保持し、加算・使用・所持金パネル表示・`playerStatsSystem` への反映をまとめて行う通貨管理コンポーネント。金額変化時には文字列付きイベントも発火する。 | 9/9 |
| [`inventoryObject`](reference/Inventory/inventoryObject.md) | シーン上のインベントリアイテム（`inventoryInfo` を保持）から、`objectOnInventory` の新挙動系メソッドを呼び出すラッパー。実処理はすべて `mainObjectOnInventory` に委譲する。 | 8/8 |
| [`simpleInventoryContentManager`](reference/Inventory/simpleInventoryContentManager.md) | インベントリ内容を簡易リスト `simpleInventoryInfoList` として保持し、武器・弾薬の数量同期やセーブ用リスト生成を行うコンポーネント。 | 8/8 |
| [`getObjectFromInventorySystem`](reference/Inventory/getObjectFromInventorySystem.md) | プレイヤーのインベントリに対象オブジェクトが何個あるかを確認し、使用（消費）やイベント発火を行うコンポーネント。判定には `extraInventoryObjectAmount` を加味した残量を使う。 | 6/6 |
| [`inventoryCaptureManager`](reference/Inventory/inventoryCaptureManager.md) | `UNITY_EDITOR` 時のみ有効なエディタ用 `EditorWindow`。インベントリアイテムのアイコン用キャプチャを撮影して PNG 保存し、`inventoryListManager` に設定する。 | 6/6 |
| [`inventoryInfo`](reference/Inventory/inventoryInfo.md) | インベントリ 1 オブジェクト分のデータを保持するシリアライズ可能クラス。名前・アイコン・数量・使用可否・武器情報・重量などをまとめ、コピー用コンストラクタも持つ。 | 4/4 |
| [`carryPhysicallyObjectFromInventory`](reference/Inventory/carryPhysicallyObjectFromInventory.md) | `objectOnInventory` を継承し、インベントリから取り出したオブジェクトをプレイヤーに物理的に持たせる処理を担当する。掴む／落とす瞬間のインタラクションパネル表示の切り替えも行う。 | 3/3 |
| [`getInventoryObjectSystem`](reference/Inventory/getInventoryObjectSystem.md) | シーン上に置かれ、プレイヤーへ指定のインベントリオブジェクト（または複数リスト）を付与する取得ポイント。付与は `applyDamage.giveInventoryObjectToCharacter` に委譲する。 | 3/3 |
| [`inventoryObjectToEquipInfo`](reference/Inventory/inventoryObjectToEquipInfo.md) | 装備対象オブジェクト用の基底 `MonoBehaviour`。3 メソッドとも virtual で、既定実装は false を返すか何もしないだけ。 | 3/3 |
| [`inventoryCaptureManagerTransparent`](reference/Inventory/inventoryCaptureManagerTransparent.md) | `UNITY_EDITOR` 時のみ有効な、背景透過アイコン生成用コンポーネント。白背景と黒背景の 2 枚からアルファを算出して透過 PNG を書き出す。 | 1/1 |
| [`inventoryMenuPanelsSystem`](reference/Inventory/inventoryMenuPanelsSystem.md) | インベントリ内の複数パネルを名前で切り替えるステート管理コンポーネント。選択中のパネルだけを有効にし、位置・スケール調整やイベント発火を行う。 | 1/1 |
| [`inventoryPrefabCreationSystem`](reference/Inventory/inventoryPrefabCreationSystem.md) | `createInventoryPrefabObject` だけを持つ基底 `MonoBehaviour`。本体は空で、継承先でインベントリ用プレハブ生成を実装するための土台。 | 1/1 |
| [`inventorySlotOptionsButtons`](reference/Inventory/inventorySlotOptionsButtons.md) | インベントリスロットのオプション（使用・装備・破棄など）ボタンの表示を一括制御する UI コンポーネント。有効ボタン数に合わせてパネルの高さも再計算する。 | 1/1 |

## 拾い物の挙動

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`objectOnInventory`](reference/Inventory/objectOnInventory.md) | インベントリ上のオブジェクト挙動を派生クラス向けに定義する基底コンポーネント。使用・結合・装備の空実装と、リモートイベント/アビリティ/ステータス/レシピ/条件判定の共通処理を提供する。 | 19/19 |
| [`weaponOnInventory`](reference/Inventory/weaponOnInventory.md) | `objectOnInventory` を継承した武器用の挙動。ピックアップ時に残弾を武器へ引き継ぎ、ドロップ時に弾倉数を保存する。 | 2/2 |

## クイックアクセス

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`inventoryQuickAccessSlotsSystem`](reference/Inventory/inventoryQuickAccessSlotsSystem.md) | クイックアクセススロットの生成・表示・選択を管理するコンポーネント。番号キーやマウスホイールからのスロット選択、武器の装備/解除、HUD 上のスロット表示の切り替えを扱う。 | 59/59 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- UI スロット生成・アイコン更新・選択状態・イベント発火・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

