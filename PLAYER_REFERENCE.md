# Player 関連コンポーネント メソッドリファレンス

プレイヤーを構成するコンポーネントの public メソッドについて、実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **72 型 / 2,843 メソッド**
- 注釈付き: **2,843 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

# Player フォルダ

## Animator IK

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`IKSystem`](reference/Player/IKSystem.md) | AnimatorのIK（手・肘・頭・体幹）の重みと目標位置を制御し、武器の抜刀/納刀・運転・把持・ジップラインなど各状態に応じた手の配置を切り替える。 | 59/59 |
| [`handsOnMeleeWeaponIKSystem`](reference/Player/handsOnMeleeWeaponIKSystem.md) | 近接武器を持っているときに両手を武器へ合わせるIKコンポーネント。`handInfoList` の手ごとの目標と重みを使い、多忙状態では重みを滑らかに落とす。 | 10/10 |
| [`handsOnSurfaceIKSystem`](reference/Player/handsOnSurfaceIKSystem.md) | 手を壁や床などの表面に合わせるIKコンポーネント。表面レイキャストで手の目標を決め、手ごとの重みを補間して適用する。 | 10/10 |
| [`OnAnimatorIKComponent`](reference/Player/OnAnimatorIKComponent.md) | IKコンポーネントの基底クラス。更新可否フラグと、派生クラスが上書きする仮想メソッド（状態設定・手の有効化・キャラクター要素設定）を提供する。 | 9/9 |
| [`IKFootSystem`](reference/Player/IKFootSystem.md) | 足のIKコンポーネント。脚の長さと足のオフセット初期値を算出し、接地レイキャストに合わせて足と腰の位置を補正する。 | 7/7 |

## Character Builder

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`buildPlayer`](reference/Player/buildPlayer.md) | キャラクターモデルの差し替え（ビルド）と、テンプレート化された設定リスト（AI種別、敵/中立、武器など）を新キャラクターへ適用するエディタ/ランタイム両用のビルダー。 | 31/31 |
| [`ragdollBuilder`](reference/Player/ragdollBuilder.md) | 人型モデルのボーンからラグドール用のジョイント・リジッドボディ・コライダーを構築/削除するビルダー。構築後は `ragdollActivator` の各リストを更新する。 | 15/15 |
| [`bodyMountPointsSystem`](reference/Player/bodyMountPointsSystem.md) | 武器や装備をキャラクターの各部位へ取り付けるためのマウントポイントを管理する。名前から人型ボーンやカスタムボーンを解決し、子オブジェクトの親子付けとオフセットを適用する。 | 11/11 |
| [`characterModelListManager`](reference/Player/characterModelListManager.md) | キャラクターモデルをリストから差し替えるコンポーネント。ID・名前・前後移動で選択し、BuildPlayer 経由でモデルの再構築、装備、身長、ラグドール設定を更新する。 | 7/7 |
| [`adjustCharacterHeightSystem`](reference/Player/adjustCharacterHeightSystem.md) | キャラクターの身長に合わせて、モデル/カプセル/武器/カメラピボット/追加コライダーなどを一括調整するコンポーネント。エディタと実行時の両方で使える。 | 6/6 |
| [`characterModelElementInfo`](reference/Player/characterModelElementInfo.md) | 差し替え用キャラクターモデルの付加情報を保持するコンポーネント。Animator、人型ボーン、装備データ、身長設定などをまとめ、ボーンを自動取得できる。 | 2/2 |

## Extra Movements

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`freeClimbSystem`](reference/Player/freeClimbSystem.md) | 壁面を自由に登るフリークライムを制御する外部コントローラ。レイキャストで登れる面を検出し、`externalControllerBehavior` として移動・アニメーション・カメラを登攀状態へ切り替える。 | 34/34 |
| [`slideSystem`](reference/Player/slideSystem.md) | 斜面やスライドゾーンでのスライディング移動を制御する外部コントローラ。状態に応じて接地判定・Animator・カメラ・重力法線への張り付きを切り替え、終了時は勢いを加えて解除する。 | 21/21 |
| [`climbRopeSystem`](reference/Player/climbRopeSystem.md) | ロープやパイプを上下に移動する登攀を制御する外部コントローラ。上下端Transform間でプレイヤーを移動させ、ジャンプ・ターボ・親子付け・カメラ状態を切り替える。 | 18/18 |
| [`externalControllerBehavior`](reference/Player/externalControllerBehavior.md) | フリークライムやスライドなど、通常移動とは別にプレイヤーを制御する「外部コントローラ」の基底クラス。既定実装はほぼ空で、派生クラスが各仮想メソッドを上書きして挙動を実装する。 | 18/18 |
| [`jetpackSystem`](reference/Player/jetpackSystem.md) | `externalControllerBehavior` を継承したジェットパック用モード。装備/使用状態、燃料、ターボ、推力パーティクル、IK、カメラFOV、HUD表示を一括して制御する。 | 16/16 |
| [`swimSystem`](reference/Player/swimSystem.md) | `externalControllerBehavior` を継承した水泳モード。水面/潜水の判定、上下移動、ターボ、カメラ状態、水に入るトリガーのリストを管理する。 | 16/16 |
| [`wallSlideJumpSystem`](reference/Player/wallSlideJumpSystem.md) | 壁に沿って滑り落ちるスライドと壁ジャンプを扱う `externalControllerBehavior`。壁検出の有効化、スライド状態に応じたアニメ・武器・カメラの切替、ジャンプ時の回転を行う。 | 16/16 |
| [`railSystem`](reference/Player/railSystem.md) | ベジェスプラインに沿って移動するレールモードを提供する `externalControllerBehavior`。レール状態、ターボ、進行方向の反転可否、開始位置への調整を管理する。 | 13/13 |
| [`walkOnBalanceSystem`](reference/Player/walkOnBalanceSystem.md) | 細い足場の上をウェイポイントに沿って歩くバランス移動モードを提供する `externalControllerBehavior`。開始時に最寄り地点と進行方向を決め、ターボやプレイヤーの子化も扱う。 | 13/13 |
| [`flySystem`](reference/Player/flySystem.md) | 空中を自由に飛ぶ飛行モードを提供する `externalControllerBehavior`。上下移動、ターボ、ダッシュID、IK、カメラFOV、COM回転のリセットを扱う。 | 11/11 |
| [`wallRunningSystem`](reference/Player/wallRunningSystem.md) | 壁に沿って走るウォールランニングを提供する `externalControllerBehavior`。左右の壁判定、ジャンプ用インパルス、アニメーション、カメラ状態、COM補正を管理する。 | 11/11 |
| [`bulletTimeFiringSystem`](reference/Player/bulletTimeFiringSystem.md) | バレットタイム中の射撃姿勢やジャンプ・起き上がり動作を扱う `OnAnimatorIKComponent`。移動状態に応じてアニメーション、起き上がり方向イベント、時間スケールを切り替える。 | 9/9 |
| [`climbDetectionCollisionSystem`](reference/Player/climbDetectionCollisionSystem.md) | フリークライム用の衝突判定オブジェクト。プレイヤーのコライダーの代わりに物理判定を行い、クライム面への接触状態を検出して公開する。 | 9/9 |
| [`paragliderSystem`](reference/Player/paragliderSystem.md) | パラグライダーで滑空するモードを提供する `externalControllerBehavior`。重力と上昇力を調整して落下を緩め、カメラや接地アニメーションも切り替える。 | 9/9 |
| [`freeFallCharacterActivator`](reference/Player/freeFallCharacterActivator.md) | 落下速度に応じてフリーフォール状態へ切り替えるコンポーネント。落下ターボや通常状態への復帰、開始判定のリセットを扱う。 | 6/6 |
| [`freeClimbZoneSystem`](reference/Player/freeClimbZoneSystem.md) | フリークライム可能なゾーン。プレイヤーがトリガーへ入退場したときにクライム検出の有効化と自動掴みを行い、親子付けの設定も公開する。 | 5/5 |
| [`externalControllerBehaviorManager`](reference/Player/externalControllerBehaviorManager.md) | 名前付きの外部コントローラ動作を一括管理するコンポーネント。動作開始時に武器を退避し入力を止め、終了時に武器やIKを復帰させる。 | 4/4 |
| [`playerSphereModeSystem`](reference/Player/playerSphereModeSystem.md) | プレイヤーが球体になって転がる「スフィアモード」への切替を扱う。車両情報を選択し、状態変更コルーチンを起動する。 | 3/3 |
| [`rollOnLandingSystem`](reference/Player/rollOnLandingSystem.md) | 空中で入力すると着地時にローリングする「着地ロール」を扱う。入力の受付時間と空中時間を判定し、コルーチンでロールを実行する。 | 3/3 |
| [`climbRopeTriggerMatchSystem`](reference/Player/climbRopeTriggerMatchSystem.md) | 縄登り用の入退場トリガーを、プレイヤーの `climbRopeSystem` に登録/解除するマッチング用コンポーネント。 | 1/1 |
| [`climbRopeTriggerSystem`](reference/Player/climbRopeTriggerSystem.md) | 縄登りゾーン。プレイヤーが入ると上下端や親子設定を `climbRopeSystem` に渡して開始し、退場時に解除する。 | 1/1 |
| [`portableClimbRopeTriggerSystem`](reference/Player/portableClimbRopeTriggerSystem.md) | 設置型の縄の長さと向きを自動調整するコンポーネント。表面の有無や傾斜を確認し、レイキャスト結果に合わせてロープを伸縮させる。 | 1/1 |
| [`portableWalkOnBalanceTriggerSystem`](reference/Player/portableWalkOnBalanceTriggerSystem.md) | 設置型のバランス足場。表面の傾斜や位置に合わせて自身の向きを調整し、レイキャストで足場の長さをスケールさせる。 | 1/1 |
| [`railTriggerSystem`](reference/Player/railTriggerSystem.md) | レールモードの開始/終了トリガー。入場時にスプラインと移動時間を渡し、退場時にレールを解除する。 | 1/1 |
| [`simpleWaypointSystem`](reference/Player/simpleWaypointSystem.md) | ウェイポイントの Transform リストを保持して公開するだけのコンポーネント。 | 1/1 |
| [`slideZoneSystem`](reference/Player/slideZoneSystem.md) | スライド（滑走）ゾーンのトリガー。入場時にスライド設定をプレイヤーへ渡し、退場時にスライドを終了させる。 | 1/1 |
| [`swimTriggerSystem`](reference/Player/swimTriggerSystem.md) | 水泳ゾーンのトリガー。プレイヤーの泳ぎ状態を開始/終了させ、車両が水に入った際の処理も行う。 | 1/1 |
| [`walkOnBalanceTriggerSystem`](reference/Player/walkOnBalanceTriggerSystem.md) | バランス移動ゾーンのトリガー。入場時にウェイポイントや親子設定をプレイヤーへ渡して移動を開始し、退場時に解除する。 | 1/1 |
| [`wallSlideJumpZoneSystem`](reference/Player/wallSlideJumpZoneSystem.md) | 壁スライド用ゾーンのトリガー。入場時に滑り落ち速度と減速設定を適用して検出を有効化し、退場時に元へ戻す。 | 1/1 |

## Generic Model Controller

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`customCharacterControllerBase`](reference/Player/customCharacterControllerBase.md) | キャラクターモデルのコントローラ設定（Animatorパラメータ、カプセルコライダー、移動速度、カメラ状態、AI値など）を保持し、派生クラスが上書きできる仮想メソッド群を提供する基底クラス。 | 53/53 |
| [`customCharacterControllerManager`](reference/Player/customCharacterControllerManager.md) | 蜘蛛や狼などの「カスタムキャラクターコントローラ」への切替を管理するコンポーネント。名前で状態を選択し、プレハブの生成、開始/終了イベント、メッシュ表示、カプセル値の同期を行う。 | 14/14 |
| [`AIMountManager`](reference/Player/AIMountManager.md) | AIの乗り物（マウント）を呼び出したりテレポートさせたりする管理コンポーネント。プレイヤーとの距離に応じてリモートイベントを送る。 | 3/3 |
| [`customCharacterControllerBaseBuilder`](reference/Player/customCharacterControllerBaseBuilder.md) | カスタムキャラクターコントローラへ設定リストを適用するビルダー。設定ごとの UnityEvent を呼び、対象コンポーネントを更新する。 | 3/3 |
| [`setCustomCharacterStateTriggerSystem`](reference/Player/setCustomCharacterStateTriggerSystem.md) | トリガーに入ったプレイヤーのカスタムキャラクター状態を切り替えるコンポーネント。通常キャラに戻すか、指定名の状態を適用する。 | 1/1 |
| [`spiderCharacterController`](reference/Player/spiderCharacterController.md) | 蜘蛛型のカスタムキャラクターコントローラ。`vehicleController` を継承し、蜘蛛固有の入力停止フラグを持つ。 | 1/1 |
| [`wolfCharacterController`](reference/Player/wolfCharacterController.md) | 狼型のカスタムキャラクターコントローラ。`vehicleController` を継承し、表面へ向けたモデルの回転や位置補正を行う。 | 1/1 |

## States

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`characterPropertiesSystem`](reference/Player/characterPropertiesSystem.md) | キャラクターに付与された状態（炎上・毒など）の有効化をまとめるコンポーネント。名前が一致する `characterStateAffectedInfo` へ処理を委譲する。 | 6/6 |
| [`characterStateAffectedInfo`](reference/Player/characterStateAffectedInfo.md) | キャラクターに付与する状態効果の基底クラス。実際の効果は派生クラスが仮想メソッドを上書きして実装する。 | 3/3 |
| [`setCharacterAffectedState`](reference/Player/setCharacterAffectedState.md) | 衝突したプレイヤーへ状態効果を付与する小さなコンポーネント。対象の `characterPropertiesSystem` に名前・時間・量を渡す。 | 1/1 |

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerController`](reference/Player/playerController.md) | プレイヤーの移動・回転・ジャンプ・接地判定・カメラ方向注視やIK・メッシュ・各種状態フラグを統括する中核コンポーネント。武器やカメラなど外部マネージャーへの問い合わせと設定を公開する。 | 611/611 |
| [`playerComponentsManager`](reference/Player/playerComponentsManager.md) | プレイヤーを構成する各コンポーネントへの参照を1か所に集約し、他スクリプトへgetterで公開するハブ。自身は処理を持たず、参照の受け渡しだけを担う。 | 97/97 |
| [`ragdollActivator`](reference/Player/ragdollActivator.md) | 死亡・転倒時のラグドール（物理）とアニメーションの切り替え、起き上がり・復活、死亡音や死亡メニューの制御を担う。ボーン・コライダー・Rigidbodyの一覧を保持し、外部から力や速度を加える窓口も提供する。 | 73/73 |
| [`usingDevicesSystem`](reference/Player/usingDevicesSystem.md) | プレイヤー周囲のデバイス（乗り物・拾得物・スイッチなど）をトリガーやレイキャストで検出し、一覧管理・最寄り選択・`activateDevice` 送信・アイコンやキー表示などのUI更新を行う。 | 72/72 |
| [`playerStatesManager`](reference/Player/playerStatesManager.md) | プレイヤーのモード（`playersMode`）と操作モード（`playerControlList`）の切り替え、モードメニューの開閉、各コンポーネントの一括有効化/無効化を担う管理クラス。 | 48/48 |
| [`upperBodyRotationSystem`](reference/Player/upperBodyRotationSystem.md) | 武器の照準方向へ上半身を曲げるIK制御。`objectToFollow` への角度を求め、しきい値・曲げ倍率・最大角でクランプして回転ポイントを補間する。 | 33/33 |
| [`quickPlayerModeChangeSystem`](reference/Player/quickPlayerModeChangeSystem.md) | 武器・能力・格闘などの「クイックモード」と、装備スロットに相当する「セレクション」の入力切替をまとめて扱うコンポーネント。モード名/セレクション名で現在の選択を切り替え、切替時イベントや射撃・ブロックの停止を行う。 | 18/18 |
| [`playerStateSystem`](reference/Player/playerStateSystem.md) | プレイヤーの状態を名前で管理するコンポーネント。優先度と割り込み可否を見て状態を切り替え、開始/終了イベントと持続時間コルーチンを扱う。 | 12/12 |
| [`genericRagdollBuilder`](reference/Player/genericRagdollBuilder.md) | 人型に限らない汎用ラグドールを、ボーンTransformのリストから構築・削除するビルダー。構築後は `ragdollActivator` へボーン/リジッドボディ/コライダーを登録する。 | 11/11 |
| [`multipleInteractionSystem`](reference/Player/multipleInteractionSystem.md) | 1つのオブジェクトに複数種別のインタラクション（デバイス）を持たせ、プレイヤーごとの利用登録や入退場イベントを管理する。コライダーとタグの有効/無効も切り替える。 | 11/11 |
| [`characterStateIconSystem`](reference/Player/characterStateIconSystem.md) | キャラクターの状態に応じて、一人称/三人称用のアイコン表示と効果音を切り替えるコンポーネント。状態名から該当エントリを探して表示を更新する。 | 10/10 |
| [`doubleJumpAnimationTrigger`](reference/Player/doubleJumpAnimationTrigger.md) | 通常ジャンプと二段ジャンプの際に、Animator のトリガーを送って専用アニメーションを再生するコンポーネント。状態に応じて再生可否を判定する。 | 7/7 |
| [`remotePlayerNavmeshOverride`](reference/Player/remotePlayerNavmeshOverride.md) | リモートプレイヤーのNavMesh目的地や有効状態を外部から操作するためのプロキシ。処理は `mainPlayerNavMeshSystem` へ委譲する。 | 6/6 |
| [`remotePlayerNavmeshOverrideSystem`](reference/Player/remotePlayerNavmeshOverrideSystem.md) | シーン内の `remotePlayerNavmeshOverride` を探して、リモートプレイヤーのNavMesh有効化と目的地（ウェイポイントまたはTransform）を設定する。 | 4/4 |
| [`playerIdleSystem`](reference/Player/playerIdleSystem.md) | 待機（idle）アニメーションの開始/停止と、再生するidleのインデックスを管理するコンポーネント。 | 3/3 |
| [`spriteAnimatorSystem`](reference/Player/spriteAnimatorSystem.md) | 3Dキャラクターを2Dスプライト表示へ切り替えるコンポーネント。Animator と SpriteAnimator、メッシュ、武器表示、ルートモーションを排他的に切り替える。 | 3/3 |
| [`AddPlayerSpawned`](reference/Player/AddPlayerSpawned.md) | 生成されたプレイヤーを `playerCharactersManager` に登録する小さなコンポーネント。`Start` で自身を自動登録する。 | 1/1 |
| [`stairAdherenceSystem`](reference/Player/stairAdherenceSystem.md) | 階段の昇降判定値をプレイヤーへ適用する小さなコンポーネント。最小/最大値と地面吸着力を渡す。 | 1/1 |

# プレイヤー中核（Player 外）

## Player Camera

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerCamera`](reference/Camera/playerCamera.md) | プレイヤーのカメラ全体を管理するコンポーネントで、三人称/一人称/フルボディアウェアネス(FBA)の視点切替、フリー/ロックオンカメラの状態、ピボットとメインカメラの位置・回転、頭ボブ、リーン、マウスホイールでの距離変更、シェイクやノイズなどを制御する。入力用ラッパーとエディタ用ヘルパーも多数持つ。 | 344/344 |

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerWeaponsManager`](reference/Weapons/playerWeaponsManager.md) | プレイヤーの武器（`IKWeaponSystem`）一覧を保持し、抜刀・納刀、照準、射撃、両手武器、リロード、HUD、アタッチメント、耐久値をまとめて管理する MonoBehaviour。入力系メソッドは入力管理から呼ばれる入口で、Editor 系はインスペクタ操作を補助する。 | 551/551 |
| [`inventoryManager`](reference/Inventory/inventoryManager.md) | プレイヤーの所持品`inventoryList`を保持し、拾得・使用・装備と解除・ドロップ・合成・耐久度・スロットUI・イベント通知を扱うインベントリの中核コンポーネントです。アイテム定義やプレハブは`mainInventoryListManager`から取得し、クイックアクセス枠やポーズメニューとも連携します。 | 256/256 |
| [`health`](reference/Health/health.md) | キャラクターや車両の体力を管理する`healthManagement`派生コンポーネントで、`healthAmount`の増減、シールド、弱点（部位）ごとのダメージ倍率、被弾・死亡・復活イベント、ヘルスバー表示、ラグドール連携をまとめて扱う。 | 173/173 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- コルーチン・アニメーション待ち・イベント発火を伴うものは、その旨を文中に書いています。
- 引数の意味が名前から自明でない場合のみ、引数に触れています。
- 本体が長いメソッドは主要な効果のみを要約しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

