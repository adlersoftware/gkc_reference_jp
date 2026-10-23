# Action System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Action System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **11 型 / 180 メソッド**
- 注釈付き: **180 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

Action System は「調べる／使う」を汎用化した仕組みです。プレイヤー側の `playerActionSystem` が対象（デバイス・NPC・オブジェクト）の `actionSystem` から行動リストを受け取り、長押し・アイコン・説明を UI に出します。

## Action System

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerActionSystem`](reference/Action%20System/playerActionSystem.md) | プレイヤー側でアクションの開始/終了を管理し、入力停止・カメラ・アニメーション・イベント・コルーチンを制御する中核コンポーネント。カスタムアクションは名前やカテゴリから起動でき、待機リストや破棄/削除の後処理も扱う。 | 82/82 |
| [`actionSystem`](reference/Action%20System/actionSystem.md) | シーン上のデバイスやNPC側に置かれ、アクション情報リスト・プレイヤーリスト・各種イベントを保持してプレイヤーの`playerActionSystem`へアクションを渡すコンポーネント。エディタ用のリスト編集補助も含む。 | 37/37 |
| [`customActionSystemTrigger`](reference/Action%20System/customActionSystemTrigger.md) | トリガーの入退室をフックに、`playerActionSystem`のカスタムアクションを名前指定で開始/停止する補助コンポーネント。角度・距離条件と`actionTransform`の差し替えに対応する。 | 3/3 |
| [`activateActionOnCharactersOnScene`](reference/Action%20System/activateActionOnCharactersOnScene.md) | シーン内の全`playerActionSystem`へ名前指定でカスタムアクションを一括起動するコンポーネント。除外設定・最大距離・リモートイベントに対応する。 | 1/1 |
| [`characterActionSystemChecker`](reference/Action%20System/characterActionSystemChecker.md) | `playerActionSystem`を監視し、指定リストのアクションが検出されたら自動で再生するチェッカー。 | 1/1 |

## Shared Action System

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`sharedActionButtonActivator`](reference/Action%20System/sharedActionButtonActivator.md) | プレイヤー側の共有アクション起動を扱うコンポーネント。アクション名と有効状態を保持し、ランダム指定や一定時間だけの有効化に対応する。 | 16/16 |
| [`sharedActionZone`](reference/Action%20System/sharedActionZone.md) | 特定位置で共有アクションを再生するためのゾーン。対象アクション名、アクション用オブジェクト、距離や角度の条件、初期位置などを保持する。 | 14/14 |
| [`sharedActionSystem`](reference/Action%20System/sharedActionSystem.md) | キャラクター同士で共有するアクションを管理するコンポーネント。アクション名から情報を検索して条件判定を行い、成立するとアクション用オブジェクトを配置して2体のキャラのアクションを同期再生する。 | 12/12 |
| [`sharedActionSystemRemoteActivator`](reference/Action%20System/sharedActionSystemRemoteActivator.md) | AIなどが対象を検出して相手キャラの共有アクションシステムを遠隔起動するコンポーネント。レイキャストや照準、目標システムで相手を探してアクション名を送る。 | 9/9 |
| [`sharedActionZoneManager`](reference/Action%20System/sharedActionZoneManager.md) | シーン内の共有アクションゾーンを一覧管理するコンポーネント。ゾーン全体の有効状態とゾーンリストを保持する。 | 4/4 |
| [`sharedActionZoneTrigger`](reference/Action%20System/sharedActionZoneTrigger.md) | トリガーの進入と退出を検出して、プレイヤーの共有アクション起動状態を切り替えるコンポーネント。タグやレイヤで対象を絞り込める。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 長押し時間・UI アイコン／説明文・イベント発火・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

