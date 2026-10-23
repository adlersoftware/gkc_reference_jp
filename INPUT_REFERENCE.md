# Input メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Input/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **13 型 / 358 メソッド**
- 注釈付き: **358 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

`inputManager` がグローバルなキー割り当て（アクション名・軸・タッチ・リバインド・保存）を持ち、`playerInputManager` がプレイヤーごとの入力問い合わせ窓口、`inputActionManager` が Action System の入力を担当します。

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerInputManager`](reference/Input/playerInputManager.md) | プレイヤーごとの入力抽象化コンポーネントで、`inputManager`から移動・カメラ軸、アクション、タッチ、ゲームパッドの状態を取得する。`multiAxesList`のアクション判定と`buttonEvent`発火、入力の有効/停止、タッチパネル操作を担当する。 | 146/146 |
| [`inputManager`](reference/Input/inputManager.md) | GKCの全入力を一元管理するMonoBehaviourで、アクショングループ(`multiAxes`)ごとにキーボード・ゲームパッド・タッチの割り当てを保持する。リバインドUIの生成、押下判定、設定の保存/読み込み、タッチボタン管理も担う。 | 116/116 |
| [`inputActionManager`](reference/Input/inputActionManager.md) | `multiAxesList` の各アクションを毎フレーム判定してイベントを発火し、移動軸とマウス軸の値を公開する。手動制御・入力の上書き・タッチ操作との切替も扱う。 | 28/28 |
| [`playerInputPanelSystem`](reference/Input/playerInputPanelSystem.md) | タッチパネルとアクション画面の表示切替をまとめて管理するコンポーネント。`inputPanelUISystem` を介して画面を出し入れし、ゲームパッド・キーボード別のパネルを切り替える。 | 28/28 |
| [`mouseCursorController`](reference/Input/mouseCursorController.md) | ゲームパッドの軸入力でマウスカーソルを動かすコントローラ。右/左スティックの入力を`SetCursorPos` で実カーソルへ反映し、表示状態と速度を管理する。 | 13/13 |
| [`editControlPosition`](reference/Input/editControlPosition.md) | タッチボタンをドラッグで移動させ、その位置をファイルへ保存・読み込みする編集コンポーネント。編集モードの開始・取消と既定位置への復帰を提供する。 | 11/11 |
| [`inputPanelUISystem`](reference/Input/inputPanelUISystem.md) | 入力パネルのGameObjectとアクション画面情報を保持し、`playerInputPanelSystem` と相互に参照し合うUI側コンポーネント。 | 3/3 |
| [`pressMultipleKeysActionInputSystem`](reference/Input/pressMultipleKeysActionInputSystem.md) | 複数キーの同時押しや順番押しを数え、規定数に達したらイベントを発火するシステム。 | 3/3 |
| [`touchButtonEventSystem`](reference/Input/touchButtonEventSystem.md) | UIのタッチボタン押下・解放を検知してUnityEventを発火する。無効化時に押下中なら解放イベントを送って状態を戻す。 | 3/3 |
| [`actionInputDelaySystem`](reference/Input/actionInputDelaySystem.md) | 入力の押下・解放から一定時間後にイベントを発火する遅延システム。長押し判定の`hold`と、離した時判定の`up`を切り替えて使う。 | 2/2 |
| [`playerInputPauseSystem`](reference/Input/playerInputPauseSystem.md) | カテゴリ単位で入力アクションを停止・再開し、停止前の有効状態を覚えておくコンポーネント。 | 2/2 |
| [`touchButtonColorChangeSystem`](reference/Input/touchButtonColorChangeSystem.md) | タッチボタンの`RawImage` 色を通常時と押下時で切り替えるだけの小コンポーネント。 | 2/2 |
| [`inputDoubleClickEventSystem`](reference/Input/inputDoubleClickEventSystem.md) | クリック回数と制限時間から連打を判定し、規定回数に達したらイベントを発火する。全クリック共通の制限時間を使う方式にも切り替えられる。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- キー割り当ての変更・アクション解決・タッチ/ゲームパッド処理・セーブ/ロードを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

