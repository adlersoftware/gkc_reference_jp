# Climb System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Climb System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **3 型 / 47 メソッド**
- 注釈付き: **47 メソッド**（100%）
- 生成元: 各 `.cs` の実装。はしご・崖のぼり。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`climbLedgeSystem`](reference/Climb%20System/climbLedgeSystem.md) | レッジの検出から掴み・登攀・ジャンプ・落下までをレイキャストとアニメーションで制御し、状態に応じてプレイヤーを停止・復帰させる。 | 45/45 |
| [`ledgeZoneSystem`](reference/Climb%20System/ledgeZoneSystem.md) | レッジゾーンのトリガーで、プレイヤーの登攀可否やレイキャスト距離などを一時的に切り替える。 | 1/1 |
| [`autoGrabLedgeTriggerSystem`](reference/Climb%20System/autoGrabLedgeTriggerSystem.md) | トリガーに入ったプレイヤーへ、指定した`ledgeTransform`への自動掴みを要求する。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

