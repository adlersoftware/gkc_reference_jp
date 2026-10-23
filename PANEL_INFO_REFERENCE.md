# Panel Info System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Panel Info System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **3 型 / 12 メソッド**
- 注釈付き: **12 メソッド**（100%）
- 生成元: 各 `.cs` の実装。パネル表示情報の管理。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerInfoPanelOnScreenSystem`](reference/Panel%20Info%20System/playerInfoPanelOnScreenSystem.md) | プレイヤーごとに画面上の情報パネルを管理し、対象オブジェクトに追従させてテキストや画像を表示する。画面座標変換・フェード・距離による自動解除も行う。 | 6/6 |
| [`infoPanelOnScreenSystem`](reference/Panel%20Info%20System/infoPanelOnScreenSystem.md) | トリガーに入ったプレイヤーへ表示する情報パネルの設定を持つコンポーネント。パネル名・テキスト・画像・位置を定義し、プレイヤー側の表示システムへ渡す。 | 4/4 |
| [`sliderInfoSystem`](reference/Panel%20Info%20System/sliderInfoSystem.md) | 名前付きのUIスライダーを時間経過で増減させる管理コンポーネント。アクティブ中はコルーチンで値を加算または減算し続ける。 | 2/2 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

