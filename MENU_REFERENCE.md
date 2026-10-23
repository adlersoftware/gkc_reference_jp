# Menu メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Menu/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **10 型 / 189 メソッド**
- 注釈付き: **189 メソッド**（100%）
- 生成元: 各 `.cs` の実装。ポーズメニュー、インゲームメニュー、シーンロード。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`menuPause`](reference/Menu/menuPause.md) | ポーズ・ポーズメニュー・プレイヤーメニューを一元管理する中心コンポーネント。時間停止、カーソルとカメラ、HUD、タッチ操作、ブラー、各イベントの発火をまとめて切り替える。 | 138/138 |
| [`ingameMenuPanel`](reference/Menu/ingameMenuPanel.md) | インゲームメニューの1パネルを表す基底クラス。開閉時に`menuPause`へ状態を通知し、表示・イベント・パネル移動・キャンバスのソート順を制御する。 | 23/23 |
| [`homeMenu`](reference/Menu/homeMenu.md) | ホームメニュー用の簡易メニュー管理。サブメニューの開閉とシーン読み込み、ゲーム終了処理を提供する。 | 8/8 |
| [`openMenuSystem`](reference/Menu/openMenuSystem.md) | メニューの開閉を遅延付きコルーチンで実行し、対象プレイヤーの`menuPause`へポーズ画面や入力の状態を反映する。 | 8/8 |
| [`sceneLoadSystem`](reference/Menu/sceneLoadSystem.md) | シーン選択メニューのスロット生成と読み込みを担当。リストのシーン番号を連番で振り直すユーティリティも持つ。 | 6/6 |
| [`simpleUIButtonInfo`](reference/Menu/simpleUIButtonInfo.md) | ボタンの表示名などを保持するだけの小さな情報コンポーネント。 | 2/2 |
| [`GKCLoadingScreenSystem`](reference/Menu/GKCLoadingScreenSystem.md) | 非同期シーン読み込み中のロード画面を制御し、読み込み完了後にキー入力を待ってシーンを有効化する。 | 1/1 |
| [`resetScrollRectOnEnable`](reference/Menu/resetScrollRectOnEnable.md) | 有効化時にレイアウトを再構築し、スクロール位置を指定値へ戻す。 | 1/1 |
| [`customActionOpenMenuSystem`](reference/Menu/customActionOpenMenuSystem.md) | 外部からメニュー開閉処理を差し込むための基底クラス。 | 1/1 |
| [`setCanvasParentSystem`](reference/Menu/setCanvasParentSystem.md) | パネルの親を指定先へ付け替え、位置・回転・スケールを初期化する。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

