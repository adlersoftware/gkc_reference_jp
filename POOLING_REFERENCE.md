# Pooling System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Pooling System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **3 型 / 19 メソッド**
- 注釈付き: **19 メソッド**（100%）
- 生成元: 各 `.cs` の実装。オブジェクトプール。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`GKC_PoolingElement`](reference/Pooling%20System/GKC_PoolingElement.md) | プール対象オブジェクトに付ける基底コンポーネントで、生成位置/回転、生成・破棄時のイベント、プーリング管理の有効/無効切り替えを提供する。状態確認用メソッドは派生クラスでの上書きを前提とした空実装。 | 12/12 |
| [`GKC_PoolingAIManager`](reference/Pooling%20System/GKC_PoolingAIManager.md) | シーン内の`GKC_PoolingElementAI`を収集してリスト管理し、全AIのプーリング管理を一括で有効/無効にするコンポーネント。収集や切り替えの後はシーン更新を通知する。 | 6/6 |
| [`GKC_SimplePoolPreloadSystem`](reference/Pooling%20System/GKC_SimplePoolPreloadSystem.md) | `poolObjectPreloadInfoList`に登録したプレハブを、`Start`時に`GKC_PoolingSystem.Preload`で指定個数だけ事前生成するプリロード用コンポーネント。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

