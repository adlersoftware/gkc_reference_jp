# Override System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Override System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **5 型 / 73 メソッド**
- 注釈付き: **73 メソッド**（100%）
- 生成元: 各 `.cs` の実装。キャラクター制御の上書き（乗車・デバイス使用中など）。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`overrideInputManager`](reference/Override%20System/overrideInputManager.md) | オーバーライド中の入力を管理するコンポーネント。マルチアクシスとアクションの定義・有効状態、入力の委譲、アクション画面の切替を行う。 | 25/25 |
| [`overrideElementControlSystem`](reference/Override%20System/overrideElementControlSystem.md) | プレイヤーが他のキャラクターや乗り物、Rigidbodyを操作(オーバーライド)する制御系。対象検出、カメラ移動、プレイヤーの停止、開始・終了処理を担う。 | 24/24 |
| [`overrideCameraController`](reference/Override%20System/overrideCameraController.md) | オーバーライド対象を追従する三人称カメラ。マウス入力による回転、カメラ衝突の回避、親子付けや再出現位置を管理する。 | 11/11 |
| [`overrideController`](reference/Override%20System/overrideController.md) | Rigidbodyを操作するためのオーバーライド用コントローラ。カメラ方向の入力で移動・ジャンプ・ブレーキ・ダッシュを行い、対象メッシュの親子付けも扱う。 | 9/9 |
| [`objectToOverrideSystem`](reference/Override%20System/objectToOverrideSystem.md) | オーバーライド可能なオブジェクトに付ける設定コンポーネント。可否フラグと対象、開始・終了時のリモートイベント、外部からの制御開始・終了を提供する。 | 4/4 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

