# Objectives Mission System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Objectives Mission System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **8 型 / 168 メソッド**
- 注釈付き: **168 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

ミッションは「メイン目標 + サブ目標」の階層で構成され、`objectiveManager` が個々の目標、`objectiveEventSystem` / `objectiveLogSystem` が状態変化とログ、`objectiveStationUISystem` が目標ステーションの UI を担当します。

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`objectiveEventSystem`](reference/Objectives%20Mission%20System/objectiveEventSystem.md) | ミッション1件の目標状態を保持するコンポーネント。サブ目標の達成・解除、制限時間、完了や中断、報酬、HUD/マップ表示、ログ・セーブ連携を担う。 | 43/43 |
| [`objectiveLogSystem`](reference/Objectives%20Mission%20System/objectiveLogSystem.md) | プレイヤーの目標ログメニューを管理するコンポーネント。ミッションスロットの生成・削除、選択内容の表示、メニュー開閉、達成・報酬状態の記録を担う。 | 35/35 |
| [`objectiveStationUISystem`](reference/Objectives%20Mission%20System/objectiveStationUISystem.md) | ステーションとキャラクターの目標パネルを管理するUI。ミッション一覧の生成・選択・受注・報酬取得と、完了/受注メッセージの表示を担う。 | 25/25 |
| [`objectiveManager`](reference/Objectives%20Mission%20System/objectiveManager.md) | シーン内の全ステーションとミッションを束ねるシングルトンマネージャ。IDとシーンでミッションを検索し、遠隔からの達成・中断処理を取り次ぐ。 | 18/18 |
| [`screenObjectivesSystem`](reference/Objectives%20Mission%20System/screenObjectivesSystem.md) | シーン内の目標アイコンを一元管理するシングルトン。目標の追加/削除、ID採番、色変更、マップ連携、各プレイヤーUIへの配信を行う。 | 14/14 |
| [`playerScreenObjectivesSystem`](reference/Objectives%20Mission%20System/playerScreenObjectivesSystem.md) | プレイヤーごとの目標アイコン(HUD)を生成・削除する。距離や画面内外の表示、色変更、マップアイコン追加、表示の一時停止を担う。 | 12/12 |
| [`objectiveStationSystem`](reference/Objectives%20Mission%20System/objectiveStationSystem.md) | ステーションのミッション一覧と進行インデックスを保持する。プレイヤーUIへの受け渡し、ミッション状態の確認、レベル内ミッションの収集を行う。 | 11/11 |
| [`setMissionSubObjectiveStateRemotelySystem`](reference/Objectives%20Mission%20System/setMissionSubObjectiveStateRemotelySystem.md) | 遠隔イベントなどからミッションのサブ目標完了やキャンセルを`objectiveManager`へ指示するコンポーネント。カウンター方式やリモートイベントにも対応する。 | 10/10 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 目標状態の遷移・ログ更新・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

