# Foot Step メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Foot Step/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **6 型 / 37 メソッド**
- 注釈付き: **37 メソッド**（100%）
- 生成元: 各 `.cs` の実装。足音の再生制御。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`footStepManager`](reference/Foot%20Step/footStepManager.md) | 足音の種類（地形テクスチャやサーフェス名）ごとに効果音・足跡・パーティクル・ノイズを再生し、足音状態リストで音量や状態遷移を制御するマネージャー。 | 23/23 |
| [`noiseSystem`](reference/Foot%20Step/noiseSystem.md) | オブジェクトが発する騒音を周囲へ通知するコンポーネントで、表面のデカール設定から可否を判定し、ノイズ信号やノイズメッシュを発生させる。 | 5/5 |
| [`footStep`](reference/Foot%20Step/footStep.md) | 片足ごとの足音コンポーネントで、設定した音量範囲のランダム音量で足音を再生し、有効状態の切り替えや遅延切り替えを提供する。 | 4/4 |
| [`noiseMeshSystem`](reference/Foot%20Step/noiseMeshSystem.md) | シングルトンとしてノイズの広がりを表すメッシュを生成し、指定倍率まで拡大させてから破棄するマネージャー。 | 2/2 |
| [`customNoiseSystem`](reference/Foot%20Step/customNoiseSystem.md) | 名前付きのノイズ状態リストを持ち、指定した状態の半径やデシベルでノイズ検知・ノイズメッシュ・イベントを発生させるコンポーネント。 | 2/2 |
| [`footStepSurfaceSystem`](reference/Foot%20Step/footStepSurfaceSystem.md) | オブジェクトの表面名を保持するだけの小さなコンポーネントで、足音マネージャーがサーフェス別の音を選ぶために参照する。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

