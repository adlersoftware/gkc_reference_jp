# Skills System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Skills System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **2 型 / 47 メソッド**
- 注釈付き: **47 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

`playerSkillsSystem` がスキルカテゴリ・解放状態・スキルポイントを保持し、`playerSkillsUISystem` がスキルツリー UI（スロット生成・選択・ポイント表示）を担当します。

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerSkillsSystem`](reference/Skills%20System/playerSkillsSystem.md) | プレイヤーのスキルツリーを保持し、カテゴリ／スキルの値・Bool・レベル・解放状態とスキルポイント消費を管理する中核コンポーネント。テンプレートとの保存・読み込み、初期化イベント、ステータス増加、エディタ用の一括操作も備える。 | 33/33 |
| [`playerSkillsUISystem`](reference/Skills%20System/playerSkillsUISystem.md) | スキルメニューUIを制御し、カテゴリ／スロットの表示切替、選択中スキル情報の表示、必要ポイントの消費確認とスロット解放を行う。`playerSkillsSystem` と `playerExperienceSystem` を参照して表示とポイント消費を同期する。 | 14/14 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- スキルポイント消費・解放状態・UI スロット更新・イベント発火を伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

