# Turn Based Combat メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Turn Based Combat/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **4 型 / 126 メソッド**
- 注釈付き: **126 メソッド**（100%）
- 生成元: 各 `.cs` の実装。ターン制戦闘の進行とコマンド選択。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`turnBasedCombatUISystem`](reference/Turn%20Based%20Combat/turnBasedCombatUISystem.md) | ターン制戦闘のUIと進行を管理するコンポーネント。コマンド選択、ターゲット選択、チーム情報の構築、ターン送り、戦闘開始・終了やインベントリ使用のUI処理を担う。 | 49/49 |
| [`turnBasedCombatActionsSystem`](reference/Turn%20Based%20Combat/turnBasedCombatActionsSystem.md) | 各キャラクターのターン制戦闘アクション用コンポーネント。戦闘中の位置調整や注文実行を担い、ターン送りやUI更新などはメインの戦闘システムへ委譲する。 | 35/35 |
| [`turnBasedCombatSystem`](reference/Turn%20Based%20Combat/turnBasedCombatSystem.md) | ターン制戦闘のシングルトン管理コンポーネント。戦闘の開始・終了、カメラ状態、チーム位置データやリスポーン位置を管理し、詳細処理はUIシステムへ委譲する。 | 33/33 |
| [`turnBasedCombatTeamInfo`](reference/Turn%20Based%20Combat/turnBasedCombatTeamInfo.md) | 1チーム分のキャラクターリストとチーム設定を保持するコンポーネント。リーダー判定、敗北イベントや相手チームへの報酬・経験値付与を扱う。 | 9/9 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

