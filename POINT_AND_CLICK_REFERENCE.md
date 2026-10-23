# Point And Click メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Point And Click/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **2 型 / 56 メソッド**
- 注釈付き: **56 メソッド**（100%）
- 生成元: 各 `.cs` の実装。ポイント＆クリック操作。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerNavMeshSystem`](reference/Point%20And%20Click/playerNavMeshSystem.md) | ポイントアンドクリック移動を制御するコンポーネントで、画面クリックのレイキャストから目的地を決め、`NavMeshAgent`の経路計算と移動入力を`playerControllerManager`へ渡します。動的障害物回避、デバイス使用、ウェイポイント、追従対象の管理も行います。 | 44/44 |
| [`pointAndClickElement`](reference/Point%20And%20Click/pointAndClickElement.md) | ポイントアンドクリックで操作できる要素（デバイス・乗り物・味方・敵）に付け、クリック時に使うオブジェクト、移動先、表示テキストを`playerNavMeshSystem`へ提供します。ホバー/使用イベントとトリガー検出も持ちます。 | 12/12 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

