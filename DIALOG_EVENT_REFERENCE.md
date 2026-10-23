# Dialog System / Event System メソッドリファレンス

会話とイベントのコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **16 型 / 149 メソッド**
- 注釈付き: **149 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

# 会話（ダイアログ）（`Dialog System/`）

`dialogManager` が会話データを保持し、`dialogSystem` が UI と進行、`dialogContentSystem` が 1 会話分の表示を担当します。

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`dialogContentSystem`](reference/Dialog%20System/dialogContentSystem.md) | キャラクター1体分のダイアログ内容（複数の `completeDialogInfo`）を保持するコンポーネント。プレイヤーの `dialogSystem` と連携して開始・終了を切り替え、イベント・AI 停止・アニメータ制御も担当する。 | 31/31 |
| [`dialogSystem`](reference/Dialog%20System/dialogSystem.md) | プレイヤー側でダイアログ UI を表示し、行送り・回答選択・文字送り・音声・アニメーションを制御するコンポーネント。`dialogContentSystem` から受け取った内容でパネルと選択肢を更新する。 | 19/19 |
| [`dialogManager`](reference/Dialog%20System/dialogManager.md) | レベル内の `dialogContentSystem` を一覧管理し、ID とシーン番号で検索・生成するマネージャ。シングルトン `Instance` として初期化される。 | 11/11 |
| [`externalDialogTriggerSystem`](reference/Dialog%20System/externalDialogTriggerSystem.md) | 外部から既存の `dialogContentSystem` のダイアログを開始するトリガー。対象キャラクターやプレイヤーを指定し、`electronicDevice` 経由で会話を開始する。 | 4/4 |
| [`dialogInfo`](reference/Dialog%20System/dialogInfo.md) | 1つのダイアログ行の本文・所有者名・分岐・音声・アニメーション設定を保持するシリアライズ可能クラス。`InitializeAudioElements` は音声クリップを `AudioElement` へ橋渡しする。 | 1/1 |
| [`simpleDialogInfo`](reference/Dialog%20System/simpleDialogInfo.md) | ローカライズ用テンプレートで使う簡易版のダイアログ情報クラス。本文・所有者名・音声・回答リストのみを保持する。 | 1/1 |

# イベント／トリガー（`Event System/`）

`eventTriggerSystem` がトリガー入力からイベントを発火し、`remoteEventSystem` が遠隔オブジェクトのイベントを名前で呼び出します。

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`eventTriggerSystem`](reference/Event%20System/eventTriggerSystem.md) | トリガーの進入/退出を判定し、タグ・レイヤー・対象オブジェクトの条件と要素ごとの遅延を経て、`SendMessage`/`BroadcastMessage`/`UnityEvent`/リモートイベントを実行する。オブジェクト追跡により最初の進入と最後の退出でのみ発火させる。 | 29/29 |
| [`remoteEventSystem`](reference/Event%20System/remoteEventSystem.md) | 名前付きのリモートイベントを、引数なし/float/bool/GameObject/Transform/stringの`UnityEvent`に割り当てて発火する仕組み。イベント単位の有効・無視・発動後無効化と全体の有効状態を管理する。 | 22/22 |
| [`randomEventSystem`](reference/Event%20System/randomEventSystem.md) | 名前指定か乱数で選んだ要素の`UnityEvent`を、全体有効フラグと確率判定を経て発火する。順番に発火するためのインデックスも保持する。 | 9/9 |
| [`eventInfoSystem`](reference/Event%20System/eventInfoSystem.md) | 複数の`UnityEvent`とリモートイベントを、要素ごとの遅延（累積待ち、または同時カウント）付きで順に実行する。実行はコルーチンで行い、途中停止もできる。 | 5/5 |
| [`remoteAnimatorEventTriggerSystem`](reference/Event%20System/remoteAnimatorEventTriggerSystem.md) | `remoteEventSystem.eventInfo`と同じ形式のリストを自前で持ち、名前一致で`UnityEvent`を呼ぶ簡易版。イベント名ごとの有効/無効の切り替えもできる。 | 4/4 |
| [`remoteEventActivator`](reference/Event%20System/remoteEventActivator.md) | 指定したオブジェクト（自分で指定、またはシーン内のプレイヤー）の`remoteEventSystem`に対し、名前と任意の引数（float/bool/GameObject/Transform）付きでリモートイベントを送る。 | 4/4 |
| [`changePlayerStateOnTriggerSystem`](reference/Event%20System/changePlayerStateOnTriggerSystem.md) | トリガーや関数呼び出しを起点に、対象プレイヤーのモード・カメラ・武器・重力・移動などの状態をまとめて変更するコンポーネント。プレイヤーは手動指定またはシーン検索で取得する。 | 3/3 |
| [`eventObjectFoundOnCaptureSystem`](reference/Event%20System/eventObjectFoundOnCaptureSystem.md) | オブジェクトを捕獲・発見した時に`UnityEvent`を1回（設定次第で複数回）呼ぶ小規模コンポーネント。検出オブジェクトを引数で渡すイベントも選べる。 | 3/3 |
| [`remoteEventSocket`](reference/Event%20System/remoteEventSocket.md) | `remoteEventSystem`への参照を保持し、ソケット無効時はnullを返す中継コンポーネント。 | 2/2 |
| [`remoteEventSearcher`](reference/Event%20System/remoteEventSearcher.md) | 名前で設定を選び、シーン全体または半径内から`remoteEventSystem`を持つオブジェクトを探して、ID/名前条件に合うものへリモートイベントを一斉送信する。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- UnityEvent の発火、コルーチン（遅延実行）、UI 更新、オブジェクトの有効化を伴うものはその旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

