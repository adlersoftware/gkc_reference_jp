# Tutorial System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Tutorial System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **4 型 / 31 メソッド**
- 注釈付き: **31 メソッド**（100%）
- 生成元: 各 `.cs` の実装。チュートリアル表示と進行。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerTutorialSystem`](reference/Tutorial%20System/playerTutorialSystem.md) | チュートリアルのパネル送り・動画再生・入力停止をまとめて行い、カーソルやカメラ、ポーズ状態をチュートリアル表示に合わせて切り替える管理コンポーネント。 | 21/21 |
| [`tutorialUISystem`](reference/Tutorial%20System/tutorialUISystem.md) | チュートリアルのパネル・動画プレイヤー・音声・`tutorialInfo`リストを保持し、プレイヤー側チュートリアルシステムに参照を渡すUIコンポーネント。 | 7/7 |
| [`tutorialActivatorSystem`](reference/Tutorial%20System/tutorialActivatorSystem.md) | 名前を指定してチュートリアルを起動する小さなコンポーネントで、有効フラグと名前に付ける接尾辞を持つ。 | 2/2 |
| [`tutorialInfo`](reference/Tutorial%20System/tutorialInfo.md) | 1つのチュートリアル定義で、名前・パネル一覧・表示設定・音声や動画の情報・一度だけ再生するフラグを持つシリアライズクラス。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

