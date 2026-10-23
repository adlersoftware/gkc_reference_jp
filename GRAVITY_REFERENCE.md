# Gravity メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Gravity/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **9 型 / 185 メソッド**
- 注釈付き: **185 メソッド**（100%）
- 生成元: 各 `.cs` の実装。重力方向の変更、無重力エリア、車両の重力制御。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`gravitySystem`](reference/Gravity/gravitySystem.md) | プレイヤーの重力方向・無重力モード・自由浮遊モードを管理する中核コンポーネント。サーフェス探索、重力パワー、零重力ルームとの連携、カメラやモデルの回転、イベント発火までを担う。 | 96/96 |
| [`zeroGravityRoomSystem`](reference/Gravity/zeroGravityRoomSystem.md) | 範囲内のオブジェクトとキャラクターの重力を通常/無重力/カスタム方向へ切り替える重力ルーム。頂点ポリゴンで室内判定を行い、入退室時に重力設定や音、力を適用する。 | 30/30 |
| [`vehicleGravityControl`](reference/Gravity/vehicleGravityControl.md) | 車両用の重力制御で、カメラ方向へのサーフェス探索・法線への回転・親設定・重力値の一時変更を扱う。`gravityObjectManager`を継承する。 | 27/27 |
| [`artificialObjectGravity`](reference/Gravity/artificialObjectGravity.md) | Rigidbodyを持つオブジェクトに`useGravity`を使わず独自方向の重力力を与え、接地判定と摩擦材を管理するコンポーネント。 | 13/13 |
| [`setGravity`](reference/Gravity/setGravity.md) | トリガーやアニメーション付きの矢印として、範囲内のプレイヤー・NPC・車両・Rigidbodyの重力方向を一括変更する。中心点、無重力、カスタム重力値、親設定などをまとめて適用できる。 | 6/6 |
| [`gravityObjectManager`](reference/Gravity/gravityObjectManager.md) | 重力系コンポーネントの共通インターフェースとなる基底クラス。各メソッドは既定値(空・false・`null`)を返すだけで、派生クラスが上書きする。 | 6/6 |
| [`parentAssignedSystem`](reference/Gravity/parentAssignedSystem.md) | 重力の親として使うGameObjectを保持し、必要なら自身で補完して返す小さなコンポーネント。 | 3/3 |
| [`updateCharacterGravityTriggerSystem`](reference/Gravity/updateCharacterGravityTriggerSystem.md) | トリガーに入ったキャラクターの重力法線を、指定Transformの上方向へ切り替えるコンポーネント。 | 2/2 |
| [`zeroGravityRoomObjectChecker`](reference/Gravity/zeroGravityRoomObjectChecker.md) | 無重力ルームとの紐付けを保持し、現在のルームへオブジェクトを追加するための小さな補助コンポーネント。 | 2/2 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

