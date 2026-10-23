# Level Manager メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Level Manager/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **3 型 / 20 メソッド**
- 注釈付き: **20 メソッド**（100%）
- 生成元: 各 `.cs` の実装。シーン遷移とレベル管理。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`travelStationUISystem`](reference/Level%20Manager/travelStationUISystem.md) | トラベルステーションのメニューUIを管理し、発見済みステーションのパネル生成・選択・メニュー開閉・移動先シーンのチェックポイント保存を行う。物理ステーションに触れた際は発見パネルを表示する。 | 11/11 |
| [`levelManagerIngame`](reference/Level%20Manager/levelManagerIngame.md) | シーン遷移用のレベルマネージャで、`sceneNumberToLoad`と`levelManagerIDToLoad`の組み合わせで移動先シーンとプレイヤーの出現位置を指定する。`activateChangeOfLevel`でチェックポイントを保存してシーンを読み込む。 | 5/5 |
| [`travelStationSystem`](reference/Level%20Manager/travelStationSystem.md) | シーン内の移動拠点コンポーネントで、移動先ステーションのリスト(`travelStationInfo`)と自身のシーン番号・レベルIDを保持する。プレイヤーが触れるとUI側へ自身を登録し、メニュー開閉を仲介する。 | 4/4 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

