# Experience System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Experience System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **2 型 / 38 メソッド**
- 注釈付き: **38 メソッド**（100%）
- 生成元: 各 `.cs` の実装。経験値・レベル。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerExperienceSystem`](reference/Experience%20System/playerExperienceSystem.md) | プレイヤーの経験値・レベル・スキルポイントを管理し、レベルアップ時のパネル表示、ステータス加算とスキル解放、経験値倍率、経験値メニューUIを扱うコンポーネント。 | 35/35 |
| [`objectExperienceSystem`](reference/Experience%20System/objectExperienceSystem.md) | オブジェクトから攻撃したキャラクターへ経験値・金額・インベントリアイテム・レシピなどの報酬を渡し、一度だけ付与する設定も持つコンポーネント。 | 3/3 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

