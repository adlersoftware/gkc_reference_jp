# Audio メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Audio/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **3 型 / 13 メソッド**
- 注釈付き: **13 メソッド**（100%）
- 生成元: 各 `.cs` の実装。サウンド再生と AudioSource 管理。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`AudioElementHolder`](reference/Audio/AudioElementHolder.md) | `AudioElement`を1つ保持し、`AudioPlayer`の静的APIへ再生・停止などを委譲するコンポーネント。 | 6/6 |
| [`AudioElementHolderPlayer`](reference/Audio/AudioElementHolderPlayer.md) | `AudioElementHolder`への参照を持ち、再生・停止などの呼び出しをそのまま転送するラッパー。 | 6/6 |
| [`AudioManager`](reference/Audio/AudioManager.md) | オーディオ関連のシングルトン。`Instance`を保持し、自身に付いた外部オーディオプレイヤー実装を取得する。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

