# Hide System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Hide System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **3 型 / 29 メソッド**
- 注釈付き: **29 メソッド**（100%）
- 生成元: 各 `.cs` の実装。物陰に隠れる仕組み。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`hideCharacterFixedPlaceSystem`](reference/Hide%20System/hideCharacterFixedPlaceSystem.md) | 固定の隠れ場所で、プレイヤーの隠れ/表示に応じてAI可視状態・FOV・コライダー・状態アイコン・UI・イベントを切り替えるシステム。 | 12/12 |
| [`hideCharacterFixedPlaceSystemPlayerManagement`](reference/Hide%20System/hideCharacterFixedPlaceSystemPlayerManagement.md) | プレイヤー側で現在の固定隠れ場所とフリー隠れゾーンを保持し、隠れ中のカメラ入力要求を委譲する管理コンポーネント。 | 10/10 |
| [`hideFromEnemiesSystem`](reference/Hide%20System/hideFromEnemiesSystem.md) | フリー隠れゾーンのトリガー内にいるキャラクターを管理し、AI可視状態・状態アイコン・敵のターゲットを切り替えるコンポーネント。 | 7/7 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

