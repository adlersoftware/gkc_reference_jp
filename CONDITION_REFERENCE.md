# Condition System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Condition System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **3 型 / 16 メソッド**
- 注釈付き: **16 メソッド**（100%）
- 生成元: 各 `.cs` の実装。条件判定と結果実行。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`GKCConditionInfo`](reference/Condition%20System/GKCConditionInfo.md) | トリガーに進入したプレイヤーを対象に条件判定を行う基底コンポーネントで、完了/未完了イベントとコルーチンによる毎フレーム判定、トリガー出入りのイベントを提供する。実際の条件内容は派生クラスで実装する。 | 11/11 |
| [`GKCConditionSystem`](reference/Condition%20System/GKCConditionSystem.md) | プレイヤー側に置かれ、トリガーで登録された`GKCConditionInfo`の判定呼び出しを代行するコンポーネント。`conditionSystemEnabled`がfalseの間は登録も判定も行わない。 | 3/3 |
| [`simpleFireWeaponsConditionSystem`](reference/Condition%20System/simpleFireWeaponsConditionSystem.md) | `IKWeaponSystem`の状態(エイム中、一人称/三人称、フルボディアウェアネス、現在武器)から条件結果を判定し、完了/未完了イベントを実行する。`conditionResultCompleteIfAnyConditionTrue`でカメラ/エイム系条件のANDとORを切り替える。 | 2/2 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

