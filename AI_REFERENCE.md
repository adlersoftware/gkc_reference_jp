# AI コンポーネント メソッドリファレンス

`Assets/Game Kit Controller/Scripts/AI/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **43 型 / 817 メソッド**
- 注釈付き: **817 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

AI は「知覚（`findObjectivesSystem`）→ 判断（各 `*SystemBrain`）→ 移動（`AINavMesh`）→ 攻撃（武器/近接/能力）」の分業構成です。

## Close Combat

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`AICloseCombatSystemBrain`](reference/AI/AICloseCombatSystemBrain.md) | 素手のクローズコンバットAIの行動ブレイン。間合い管理とコンボ攻撃、ブロック・回避・ランダム移動の抽選を制御する。 | 47/47 |

## Custom AI Behavior

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`AIBehaviorInfo`](reference/AI/AIBehaviorInfo.md) | カスタムAI行動の基底クラスで、武器・攻撃・ターン制戦闘・乗り物などの状態変更を受け取る窓口を定義する。全メソッドは空の`virtual`で、実際の処理は派生コンポーネントが上書きして実装する。 | 47/47 |
| [`AIFireWeaponsSystemBrain`](reference/AI/AIFireWeaponsSystemBrain.md) | 射撃武器で戦うAIの行動ブレイン。ターゲットとの距離に応じて抜刀・照準・射撃・武器切替を制御し、武器が無ければ探索や窃取も行う。 | 47/47 |
| [`AIPowersSystemBrain`](reference/AI/AIPowersSystemBrain.md) | パワー（照準・射撃）系の攻撃をAIから操作するブレインで、照準/射撃入力の送信と攻撃間隔を制御する。ランダム歩行・ロール・強制攻撃タイマー、戦闘イベント、ターン制戦闘フラグも併せて管理する。 | 38/38 |
| [`AIAbilitiesSystemBrain`](reference/AI/AIAbilitiesSystemBrain.md) | `playerAbilitiesSystem` をAIから操作し、能力リストから次の能力を選んで発動するブレイン。距離・角度・確率・クールダウンを判定し、能力ごとの押下保持/トグルや継続時間、開始/終了イベントを扱う。 | 33/33 |
| [`AITurnBasedCombatSystemBrain`](reference/AI/AITurnBasedCombatSystemBrain.md) | ターン制戦闘で手番キャラクターの攻撃コマンドを自動選択するブレインで、カテゴリとコマンドを確率・前回使用・ステータス消費で抽選する。`characterToReceiveOrders` 経由で発注し、手番の開始/終了や位置合わせ、死亡時の手番送りも処理する。 | 24/24 |
| [`simpleAIAction`](reference/AI/simpleAIAction.md) | カスタムAI行動の基底クラス。有効時のみ開始/終了イベントとコルーチンを管理し、継続時間の経過か外部呼び出しで終了する。 | 7/7 |
| [`handleVehicleAIBehavior`](reference/AI/handleVehicleAIBehavior.md) | AIが車両を探して乗り降りする行動を扱う。更新コルーチンで車両探索・搭乗・降車を監視し、`usingDevicesManager`経由で運転席に乗せる。 | 6/6 |
| [`AIAimRotationManager`](reference/AI/AIAimRotationManager.md) | 名前付きの照準回転状態をカメラや旋回速度へ適用し、必要に応じてランダムな照準オフセットを付与する。 | 5/5 |
| [`useAbilitySimpleAIAction`](reference/AI/useAbilitySimpleAIAction.md) | `AIAbilitiesSystemBrain`から指定名のアビリティを発動し、終了後にカメラと注視状態を戻すAIアクション。 | 2/2 |
| [`useCustomAbilitySimpleAIAction`](reference/AI/useCustomAbilitySimpleAIAction.md) | 指定名のアビリティを待ち時間後に発動し、対象の注視とNavMeshの一時停止を制御するAIアクション。 | 2/2 |
| [`shootBowSimpleAIAction`](reference/AI/shootBowSimpleAIAction.md) | `bowSystem`を操作して弓を射るAIアクションで、射撃時間や発射数、連射間隔を設定できる。 | 1/1 |
| [`shootFireWeaponSimpleAIAction`](reference/AI/shootFireWeaponSimpleAIAction.md) | `playerWeaponsManager`を通じて銃器を射撃するAIアクションで、射撃時間や発射数を設定できる。 | 1/1 |
| [`shootPowerSimpleAIAction`](reference/AI/shootPowerSimpleAIAction.md) | `otherPowers`を通じて特殊能力の発動入力を送るAIアクションで、発動時間や発射数を設定できる。 | 1/1 |

## Custom Orders

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`customOrderBehavior`](reference/AI/customOrderBehavior.md) | 注文ビヘイビアの基底クラスで、対象の取得や注文実行、ボタン表示条件を派生クラスが上書きする。 | 5/5 |
| [`characterToReceiveOrders`](reference/AI/characterToReceiveOrders.md) | 注文名ごとにイベント・継続時間・簡易AIアクションを登録し、キャラクターが注文を受け付ける仕組みを提供する。 | 4/4 |
| [`customOrderBehaviorToAttack`](reference/AI/customOrderBehaviorToAttack.md) | 攻撃注文用に、プレイヤーのロックオン対象や画面内の敵から攻撃対象を選ぶビヘイビア。 | 3/3 |
| [`customOrderBehaviorToFollow`](reference/AI/customOrderBehaviorToFollow.md) | 追従注文用に、ロックオン中や画面内の対象を選び、無ければ注文発行者を返すビヘイビア。 | 3/3 |
| [`customOrderBehaviorToUseAbility`](reference/AI/customOrderBehaviorToUseAbility.md) | アビリティ使用注文用に、ロックオン中や画面内の対象を選んで攻撃対象とするビヘイビア。 | 3/3 |
| [`customOrderBehaviorToHide`](reference/AI/customOrderBehaviorToHide.md) | 隠れ注文用に、シーン内の`AIHidePositionsManager`が持つ隠れ位置から対象を選ぶビヘイビア。 | 1/1 |

## Faction

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`characterFactionManager`](reference/AI/characterFactionManager.md) | キャラクターの所属factionを管理するコンポーネント。factionSystemへの登録、味方/敵/中立の判定、検出済み敵リストの保持を行い、判定処理はほぼfactionSystemへ委譲する。 | 34/34 |
| [`factionSystem`](reference/AI/factionSystem.md) | ゲーム全体のfaction定義と関係(味方/敵/中立)を保持するシングルトン。登録キャラクターのリストを使い、関係判定・変更、警告、対象解除を各キャラへ配信する。 | 26/26 |

## Melee Combat System

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`AIMeleeCombatSystemBrain`](reference/AI/AIMeleeCombatSystemBrain.md) | 近接武器AIの行動ブレイン。武器の抜刀・攻撃コンボ・ブロック・パリィカウンターを管理し、武器が無ければ探索や窃取を行う。 | 46/46 |

## Turret

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`manageAITarget`](reference/AI/manageAITarget.md) | タレットの視界トリガー情報から敵factionを判定し、最も近い敵を目標として取得する。視界半径の拡大、factionへの警告、イベント発火、ハッキング結果の反映までを担う。 | 19/19 |
| [`AITurret`](reference/AI/AITurret.md) | タレットの武器選択・発砲・旋回と、プレイヤーによる遠隔操作、死亡時の分解処理を担う。目標判定はmanageAITargetに委ね、選択武器の有効化と付随イベントを切り替える。 | 17/17 |
| [`enemyLaser`](reference/AI/enemyLaser.md) | タレットなどが放つレーザーの描画とダメージ処理を行うコンポーネント。レイキャストの命中点にスパークと煙を出し、設定された所有者名義でダメージを与える。 | 1/1 |

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`findObjectivesSystem`](reference/AI/findObjectivesSystem.md) | AIキャラクターの索敵と目標選択を担うMonoBehaviour。FOVトリガーやレイキャストで敵を検出して脅威確認・敵リスト管理・徘徊や巡回・相棒追従・ノイズ反応・攻撃タイプ別の距離制御までをまとめて行い、実際の移動や攻撃は`AINavMesh`と各`AIBehaviorInfo`へ委譲する。 | 200/200 |
| [`AINavMesh`](reference/AI/AINavMesh.md) | `NavMeshAgent`でAIキャラクターを移動させる中核コンポーネント。ターゲットや巡回地点の管理、経路計算、動的障害物回避、ジャンプ、パートナー追従、死亡・停止状態を扱う。 | 105/105 |
| [`friendListManager`](reference/AI/friendListManager.md) | プレイヤーの仲間リストと命令メニューを管理するコンポーネント。仲間の追加/削除、個別・全体命令の送信、メニュー開閉、全滅時のチーム蘇生を担当する。 | 27/27 |
| [`AIPatrolSystem`](reference/AI/AIPatrolSystem.md) | `AIWayPointPatrol`の巡回リストを使い、最寄り・次・ランダムなウェイポイントを選んで待ち時間コルーチンを挟みながら`AINavMesh`の目標と速度を更新する。 | 11/11 |
| [`AIAroundManager`](reference/AI/AIAroundManager.md) | 周囲のAI（`findObjectivesSystem`）を登録し、1体ずつ攻撃を許可する制御を行うマネージャ。一定間隔のコルーチンで待機状態、ランダムウォーク、動的障害物検出を切り替える。 | 8/8 |
| [`changeAIAttackModeByDistance`](reference/AI/changeAIAttackModeByDistance.md) | ターゲットとの距離に応じてAIの攻撃モードを近距離/遠距離（ランダム選択可）へ切り替え、距離が離れている時はスプリントさせるコンポーネント。 | 8/8 |
| [`AIWayPointPatrol`](reference/AI/AIWayPointPatrol.md) | 巡回経路（パトロールとウェイポイント）のTransform階層を編集するための補助コンポーネント。`patrolList`を保持し、地点の追加・削除、地面への吸着、シーンへの反映を行う。 | 7/7 |
| [`eventOnTargetDetectedFaction`](reference/AI/eventOnTargetDetectedFaction.md) | 陣営名ごとに登録したUnityEventを、対象の検知・解除のタイミングで発火させるコンポーネント。 | 6/6 |
| [`AIViewTriggerSystem`](reference/AI/AIViewTriggerSystem.md) | トリガーの進入・退出時に、UnityEventの呼び出しと`findObjectivesSystem`への容疑者登録/解除を行う。 | 4/4 |
| [`fieldOfViewMeshSystem`](reference/AI/fieldOfViewMeshSystem.md) | AIの視界範囲を扇形メッシュとして可視化するコンポーネント。レイキャストで視界形状を生成し、状態に応じて表示の有無やメッシュ色を切り替える。 | 4/4 |
| [`AIWalkToPosition`](reference/AI/AIWalkToPosition.md) | 指定位置までAIを歩かせ、到達やプレイヤー死亡時にNavMesh設定とAI状態を元へ戻す。 | 3/3 |
| [`addPatrolSystemToAI`](reference/AI/addPatrolSystemToAI.md) | インスペクタのボタンからAIへ巡回システムや`AIWayPointPatrol`を追加・割り当てするエディタ補助。 | 3/3 |
| [`brainwashAIState`](reference/AI/brainwashAIState.md) | キャラクターを洗脳して陣営・タグ・名前・パートナーを変更するステートで、`GKC_Utils`の処理へ設定を渡す。 | 2/2 |
| [`objectSignalForTargetToAI`](reference/AI/objectSignalForTargetToAI.md) | このオブジェクトをAIの検出対象として通知するコンポーネント。ノイズシグナルを一定間隔または単発で送り、単一AIの追跡状態を監視する。 | 2/2 |
| [`sleepingStateIconSystem`](reference/AI/sleepingStateIconSystem.md) | 睡眠状態のキャラクターの頭上に「Z」アイコンを生成し、上昇・拡大・色変化させて睡眠演出を行うシステム。 | 2/2 |
| [`AIHidePositionsManager`](reference/AI/AIHidePositionsManager.md) | AIが隠れる位置のリスト`hidePositionList`を保持し、シーン上にギズモで隠れ場所を表示する管理コンポーネント。 | 1/1 |
| [`animalAINavmesh`](reference/AI/animalAINavmesh.md) | 動物AI用に、AIの移動入力を入力上書きと`playerControllerManager`の移動へ変換する派生クラス。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- コルーチン・アニメーション待ち・イベント発火・NavMeshAgent 操作を伴うものは、その旨を文中に書いています。
- 引数の意味が名前から自明でない場合のみ、引数に触れています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

