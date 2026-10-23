# Puzzles メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Puzzles/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **5 型 / 46 メソッド**
- 注釈付き: **46 メソッド**（100%）
- 生成元: 各 `.cs` の実装。パズル系の仕掛けと状態管理。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`puzzleSystem`](reference/Puzzles/puzzleSystem.md) | ドラッグ可能なオブジェクトを掴んで回転や距離変更を行い、所定数配置すると解決するパズル装置。プレイヤー入力とイベントで状態を管理する。 | 19/19 |
| [`puzzleSystemPlayerManagement`](reference/Puzzles/puzzleSystemPlayerManagement.md) | プレイヤー側で使用中の`puzzleSystem`を保持し、入力をそこへ転送する窓口コンポーネント。 | 8/8 |
| [`pianoSystem`](reference/Puzzles/pianoSystem.md) | 鍵盤を名前で識別して発音と押下アニメーションを行い、曲データの自動演奏もできるコンポーネント。 | 7/7 |
| [`placeObjectSystem`](reference/Puzzles/placeObjectSystem.md) | 対象オブジェクトがトリガー内で条件を満たすと、所定位置へ移動させて配置済みにするコンポーネント。 | 7/7 |
| [`pressObjectsInOrderSystem`](reference/Puzzles/pressObjectsInOrderSystem.md) | 決められた順序で押される位置を判定し、順序を間違えるとリセットする仕組み。使用中は毎フレーム入力を監視する。 | 5/5 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

