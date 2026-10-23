# Save System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Save System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **20 型 / 160 メソッド**
- 注釈付き: **160 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

`saveGameSystem` がスロット単位でセーブデータ（`BinaryFormatter` による `.txt`）を読み書きし、`save*Info` クラスが各システムの状態をシリアライズ可能な形に変換します。`Elements On Scene` はシーン上のオブジェクト個別の状態を保存します。

## セーブ中核

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`saveGameSystem`](reference/Save%20System/saveGameSystem.md) | セーブステーションのUIとセーブ/ロード処理を束ねる管理コンポーネント。スロット一覧を`BinaryFormatter`で`.txt`へ読み書きし、各`saveInfo`へ個別データの保存・読込を委譲する。 | 45/45 |
| [`saveGameInfoHelper`](reference/Save%20System/saveGameInfoHelper.md) | セーブの有無を調べてイベントを発火し、`PlayerPrefs`の`saveNumber`を管理する補助コンポーネント。 | 3/3 |

## 保存データクラス

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`saveGameInfo`](reference/Save%20System/saveGameInfo.md) | 各コンポーネント固有のデータをセーブ/ロードするための基底クラス。全メソッドが空の`virtual`で、派生クラスによる上書きを前提とする。 | 8/8 |
| [`saveInventoryBankInfo`](reference/Save%20System/saveInventoryBankInfo.md) | インベントリバンクの在庫（名前・数量・カテゴリ／要素インデックス）を保存し、ロード時に`inventoryListElement`の新しいリストとして復元する。 | 5/5 |
| [`savePlayerInventoryInfo`](reference/Save%20System/savePlayerInventoryInfo.md) | プレイヤーインベントリの全アイテム情報（数量・装備・耐久度・弾数）とスロット数・クラフト情報を保存し、ロード時に復元する。 | 5/5 |
| [`saveVendorInfo`](reference/Save%20System/saveVendorInfo.md) | ベンダー在庫の数量・価格・売値・購入最小レベル・スポーン設定を保存し、ロード時にベンダー在庫として復元する。 | 5/5 |
| [`saveElementsOnSceneInfo`](reference/Save%20System/saveElementsOnSceneInfo.md) | シーン上の`elementOnScene`のアクティブ状態・位置・回転・統計値・プレハブIDを保存し、ロード時に既存要素へ適用、必要ならプレハブから生成する。 | 4/4 |
| [`saveMissionsInfo`](reference/Save%20System/saveMissionsInfo.md) | `objectiveLogSystem`のミッション進行（ID・シーン・受注／進行／完了状態・サブ目標・報酬文言）を保存し、ロード時にミッション状態を再構築する。 | 4/4 |
| [`saveDialogInfo`](reference/Save%20System/saveDialogInfo.md) | `dialogManager`の対話進行（`dialogContentSystem`ごとの現在インデックス）をスロット／プレイヤー別に保存し、ロード時に完了位置を復元する。 | 3/3 |
| [`savePlayerBlendshapesInfo`](reference/Save%20System/savePlayerBlendshapesInfo.md) | プレイヤーのブレンドシェイプ値・アクセサリ・`characterModelID`を保存し、ロード時にキャラクターカスタマイズへ反映する。 | 3/3 |
| [`savePlayerOptionsInfo`](reference/Save%20System/savePlayerOptionsInfo.md) | `playerOptionsEditorSystem`の各オプション現在値（スクロールバー／スライダー／トグル／ドロップダウン）を保存・復元する。 | 3/3 |
| [`savePlayerWeaponsInfo`](reference/Save%20System/savePlayerWeaponsInfo.md) | プレイヤー武器の有効状態・現在装備・残弾・アタッチメント構成を保存し、ロード時に各武器へ反映する。 | 3/3 |
| [`saveSkillsInfo`](reference/Save%20System/saveSkillsInfo.md) | `playerSkillsSystem`のカテゴリ別スキル状態（解放・有効・完了・現在値・レベル）を保存し、ロード時に復元する。 | 3/3 |
| [`saveStatsInfo`](reference/Save%20System/saveStatsInfo.md) | `playerStatsSystem`の各ステータスの現在値とbool状態を保存し、ロード時に`ignoreStatInitializationOnLoadGame`を除いて復元する。 | 3/3 |
| [`saveMeleeWeaponsInfo`](reference/Save%20System/saveMeleeWeaponsInfo.md) | 拾得済み近接武器を`weaponPrefabIndex`と現在装備フラグで保存し、ロード時にプレハブから武器を再生成する。 | 2/2 |
| [`saveTravelStationInfo`](reference/Save%20System/saveTravelStationInfo.md) | 発見済みトラベルステーションの遷移先シーン番号と`levelManagerID`を保存し、ロード時に発見リストへ戻す。 | 2/2 |

## シーン要素の状態保存

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`elementOnScene`](reference/Save%20System/elementOnScene.md) | シーン上の1オブジェクトの位置・回転・アクティブ状態・統計値をセーブ対象として保持するコンポーネント。読込時はイベント発火とTransform復元を行い、`elementOnSceneManager`と連携する。 | 30/30 |
| [`elementOnSceneManager`](reference/Save%20System/elementOnSceneManager.md) | シーン内の`elementOnScene`をID付きで一覧管理するシングルトン。保存時の未登録要素の収集、IDの採番、一時状態の保持、エディタ用の一括設定を担当する。 | 21/21 |
| [`elementOnSceneHelper`](reference/Save%20System/elementOnSceneHelper.md) | `elementOnScene`の処理を外部から呼ぶための中継コンポーネント。`checkElementOnSceneEnabled`がfalse、または参照がnullなら何もしない。 | 6/6 |
| [`elementsOnSceneData`](reference/Save%20System/elementsOnSceneData.md) | `elementsOnSceneInfo`のリストを保持するScriptableObjectで、プレハブIDとプレハブ名から要素プレハブを検索する。 | 2/2 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- ファイル入出力・スロット番号・JSON 変換・シーン上のオブジェクト復元を伴うものは、その旨を書いています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

