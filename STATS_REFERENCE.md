# Stats System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Stats System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **6 型 / 71 メソッド**
- 注釈付き: **71 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

`playerStatsSystem` がキャラクターのステータス（名前付き数値）を保持し、`statType` が 1 項目の定義、`objectStatsSystem` / `objectsStatsSystem` がオブジェクト側のステータスを扱います。

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerStatsSystem`](reference/Stats%20System/playerStatsSystem.md) | キャラクターの数値・boolステータスを`statInfoList`で保持し、増減、上限Clamp、イベント発火、テンプレート保存/読込の中心となるクラス。 | 36/36 |
| [`objectStatsSystem`](reference/Stats%20System/objectStatsSystem.md) | オブジェクト固有のステータスを`statInfoList`で持ち、読み込み時初期化とセーブ用の値取得/設定イベントを提供する。主人公側の`objectsStatsSystem`に登録される。 | 11/11 |
| [`statType`](reference/Stats%20System/statType.md) | ステータス変化を受け取るvirtualフック集で、既定実装はすべて空。派生クラスが初期化・増減・使用・bool切替の処理を実装する。 | 9/9 |
| [`objectsStatsSystem`](reference/Stats%20System/objectsStatsSystem.md) | 複数の`objectStatsSystem`をリストで管理し、名前からの参照や有効状態の切り替えを行う。`increaseStat`は本体が未実装。 | 7/7 |
| [`externalStatsManager`](reference/Stats%20System/externalStatsManager.md) | `playerStatsSystem`への外部更新を中継するクラス。一時的なステータス名を保持し、無効時は何もしない。 | 4/4 |
| [`showValuesOnScreenSystem`](reference/Stats%20System/showValuesOnScreenSystem.md) | ステータス値やインベントリ個数を`Text`へ表示するHUDコンポーネント。パネルの表示制御と前後付加文字を扱う。 | 4/4 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 値の加減算・UI 更新・イベント発火を伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

