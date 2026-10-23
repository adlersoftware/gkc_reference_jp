# ragdollActivator

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/ragdollActivator.cs:7`

**概要**: 死亡・転倒時のラグドール（物理）とアニメーションの切り替え、起き上がり・復活、死亡音や死亡メニューの制御を担う。ボーン・コライダー・Rigidbodyの一覧を保持し、外部から力や速度を加える窓口も提供する。

**公式ドキュメント抜粋**（[Ragdoll Activator](../../docs/player-controller-components/player-controller/ragdoll-activator.md)）

> It manages the ragdoll configured in the character when it dies or the ragdoll state is triggered by external events. It also allows using death animations instead of activating the ragdoll directly.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Type Of Death | `typeOfDeath` | `deathType` | – | 死亡時にラグドールとアニメーションのどちらを使うか。 |
| Time To Get Up | `timeToGetUp` | `float` | – | 転倒してから自動で立ち上がるまでの待ち秒数。 |
| Check Player On Ground To Get Up | `checkPlayerOnGroundToGetUp` | `bool` | true | オンにすると地面に着いた時だけ死亡タイマーを進める。 |
| Get Up Delay | `getUpDelay` | `float` | 2 | 立ち上がり開始後、操作を戻すまでの待ち秒数。 |
| Use Death Sound | `useDeathSound` | `bool` | true | オンにすると死亡時に効果音を再生する。 |
| Death Sound | `deathSound` | `AudioClip` | – | 死亡時に再生する効果音のクリップ。 / 表示条件: `useDeathSound` がオンのとき |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | 死亡音を再生するオーディオソース。 / 表示条件: `useDeathSound` がオンのとき |
| Death Sound Audio Element | `deathSoundAudioElement` | `AudioElement` | – | 死亡音を再生するためのオーディオ要素。 / 表示条件: `useDeathSound` がオンのとき |
| Check If Character On Air On Death | `checkIfCharacterOnAirOnDeath` | `bool` | true | オンにすると死亡時に空中かを判定してラグドールを選ぶ。 |
| Min Distance To Check If Character On Air | `minDistanceToCheckIfCharacterOnAir` | `float` | 2 | 空中判定に使う地面までのレイキャスト距離。 / 表示条件: `checkIfCharacterOnAirOnDeath` がオンのとき |
| Can Move Character On Ragdoll State | `canMoveCharacterOnRagdollState` | `bool` | – | オンにするとラグドール中に入力で体を動かせる。 |
| Move Character On Ragdoll State Force Amount | `moveCharacterOnRagdollStateForceAmount` | `float` | – | ラグドール中に体へ加える移動フォースの量。 / 表示条件: `canMoveCharacterOnRagdollState` がオンのとき |
| Move Character On Ragdoll State Force Mode | `moveCharacterOnRagdollStateForceMode` | `ForceMode` | – | その移動フォースの加え方（`ForceMode`）。 / 表示条件: `canMoveCharacterOnRagdollState` がオンのとき |
| Checkpoint Manager State Enabled | `checkpointManagerStateEnabled` | `bool` | true | オンにするとチェックポイント復帰の判定を有効にする。 |
| Set Ragdoll State On Start | `setRagdollStateOnStart` | `bool` | – | オンにするとシーン開始時にラグドール状態になる。 |
| Pause Get Up State On Ragdoll On Start | `pauseGetUpStateOnRagdollOnStart` | `bool` | – | 開始時ラグドールで立ち上がりを止めたままにする。 / 表示条件: `setRagdollStateOnStart` がオンのとき |
| Ragdoll On Start Force | `ragdollOnStartForce` | `float` | 10 | 開始時ラグドールで体を押すランダム方向の力の強さ。 / 表示条件: `setRagdollStateOnStart` がオンのとき |
| Set Sleep State On Start | `setSleepStateOnStart` | `bool` | – | オンにすると開始時に倒れて眠った状態になる。 |
| Use Duration For Sleep State On Start | `useDurationForSleepStateOnStart` | `bool` | – | オンにすると開始時の睡眠状態に時間制限を付ける。 / 表示条件: `setSleepStateOnStart` がオンのとき |
| Duration For Sleep State On Start | `durationForSleepStateOnStart` | `float` | – | 開始時の睡眠状態が続く時間を秒で指定する。 / 表示条件: `setSleepStateOnStart` がオンのとき |

### Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Get Up From Belly Animator Name | `getUpFromBellyAnimatorName` | `string` | "Get Up From Belly" | うつ伏せから立ち上がるアニメーターのステート名。 |
| Get Up From Back Animator Name | `getUpFromBackAnimatorName` | `string` | "Get Up From Back" | 仰向けから立ち上がるアニメーターのステート名。 |
| Death Animator Name | `deathAnimatorName` | `string` | "Dead" | 死亡時に切り替えるアニメーターのステート名。 |
| Death Animation ID | `deathAnimationID` | `int` | 1534 | 死亡時に`Action ID`へ設定するアニメーション番号。 |
| Action ID Animator Name | `actionIDAnimatorName` | `string` | "Action ID" | アニメーション番号を渡す整数パラメーター名。 |
| Use Get Up From Belly After Death Active | `useGetUpFromBellyAfterDeathActive` | `bool` | – | オンにすると死亡後はうつ伏せ起き上がりを使う。 |
| Activate Ragdoll After Death | `activateRagdollAfterDeath` | `bool` | – | オンにすると死亡アニメーション後にラグドール化する。 |
| Delay To Activate Ragdoll After Death | `delayToActivateRagdollAfterDeath` | `float` | – | 死亡してからラグドール化するまでの遅延秒数。 / 表示条件: `activateRagdollAfterDeath` がオンのとき |
| Enable Animator Layer On Death | `enableAnimatorLayerOnDeath` | `bool` | – | オンにすると死亡時に指定アニメーター層を有効にする。 |
| Animator Layer To Enable Name | `animatorLayerToEnableName` | `string` | – | 死亡時に有効にするアニメーター層の名前。 / 表示条件: `enableAnimatorLayerOnDeath` がオンのとき |

### Ragdoll Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ragdoll To Mecanim Blend Time | `ragdollToMecanimBlendTime` | `float` | 0.5f | ラグドールからアニメーションへ戻す補間の秒数。 / 表示条件: `manager.typeOfDeath == ragdollActivator.deathType.ragdoll` |
| Layer | `layer` | `LayerMask` | – | 地面判定などに使うレイヤーマスク。 / 表示条件: `manager.typeOfDeath == ragdollActivator.deathType.ragdoll` |
| Max Ragdoll Velocity | `maxRagdollVelocity` | `float` | – | ラグドールの腰の落下速度を制限する上限値。 / 表示条件: `manager.typeOfDeath == ragdollActivator.deathType.ragdoll` |
| Max Velocity To Get Up | `maxVelocityToGetUp` | `float` | – | 立ち上がりを許可する腰の速度の上限値。 / 表示条件: `manager.typeOfDeath == ragdollActivator.deathType.ragdoll` |
| Extra Force On Ragdoll | `extraForceOnRagdoll` | `float` | – | 死亡時にラグドールの部位へ加える力の大きさ。 / 表示条件: `manager.typeOfDeath == ragdollActivator.deathType.ragdoll` |

### Ragdoll Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Enter Ragdoll | `eventOnEnterRagdoll` | `UnityEvent` | – | ラグドール状態に入ったときに呼ばれるイベント。 / 表示条件: `showEventsSettings` がオンのとき |
| Event On Exit Ragdoll | `eventOnExitRagdoll` | `UnityEvent` | – | ラグドール状態から戻ったときに呼ばれるイベント。 / 表示条件: `showEventsSettings` がオンのとき |
| Event On Death | `eventOnDeath` | `UnityEvent` | – | 死亡メニューのタイマー終了時に呼ばれるイベント。 / 表示条件: `showEventsSettings` がオンのとき |
| Event On Resurrect | `eventOnResurrect` | `UnityEvent` | – | 死亡から復活して立ち上がったときに呼ばれるイベント。 / 表示条件: `showEventsSettings` がオンのとき |

### Receive Damage On Impact Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ragdoll Can Receive Damage On Impact | `ragdollCanReceiveDamageOnImpact` | `bool` | – | オンにするとラグドール中の衝撃でダメージを受ける。 |
| Min Time To Receive Damage On Impact | `minTimeToReceiveDamageOnImpact` | `float` | – | ラグドール化直後の衝撃ダメージを無効にする秒数。 / 表示条件: `ragdollCanReceiveDamageOnImpact` がオンのとき |
| Min Velocity To Receive Damage On Impact | `minVelocityToReceiveDamageOnImpact` | `float` | – | ダメージが発生する衝撃速度のしきい値。 / 表示条件: `ragdollCanReceiveDamageOnImpact` がオンのとき |
| Receive Damage On Impact Multiplier | `receiveDamageOnImpactMultiplier` | `float` | – | 衝撃速度に掛けてダメージ量を決める倍率。 / 表示条件: `ragdollCanReceiveDamageOnImpact` がオンのとき |
| Min Tim To Receive Impact Damage Again | `minTimToReceiveImpactDamageAgain` | `float` | – | 連続で衝撃ダメージを受けるまでの間隔秒数。 / 表示条件: `ragdollCanReceiveDamageOnImpact` がオンのとき |

### Player Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Time To Show Menu | `timeToShowMenu` | `float` | – | 死亡してから死亡メニューを出すまでの秒数。 / 表示条件: `usedByAI` がオフのとき |

### AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Used By AI | `usedByAI` | `bool` | – | オンにするとAI用に扱いプレイヤー向け処理を省く。 |
| Tag For Colliders | `tagForColliders` | `string` | – | ラグドール時にコライダーへ付けるタグ。 |
| Set Layer On Ragdoll State | `setLayerOnRagdollState` | `bool` | – | オンにするとラグドール時にコライダーの層を変える。 |
| Layer On Ragdoll State | `layerOnRagdollState` | `string` | – | ラグドール時に設定するレイヤー名。 / 表示条件: `setLayerOnRagdollState` がオンのとき |

### Ragdoll State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player State | `playerState` | `healthState` | – | 生存・死亡・転倒の現在の体力状態を示す値。 |
| Current State | `currentState` | `ragdollState` | ragdollState.animated | 通常・ラグドール・復帰補間の現在状態を示す値。 |

### Player Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Body | `characterBody` | `GameObject` | – | キャラクター本体のトランスフォームの参照。 / 表示条件: `showComponents` がオンのとき |
| Root Motion | `rootMotion` | `Transform` | – | ラグドール時に根元となる腰のトランスフォーム。 / 表示条件: `showComponents` がオンのとき |
| Head Transform | `headTransform` | `Transform` | – | 立ち上がり方向の計算に使う頭のトランスフォーム。 / 表示条件: `showComponents` がオンのとき |
| Left Foot Transform | `leftFootTransform` | `Transform` | – | 立ち上がり方向の計算に使う左足のトランスフォーム。 / 表示条件: `showComponents` がオンのとき |
| Right Foot Transform | `rightFootTransform` | `Transform` | – | 立ち上がり方向の計算に使う右足のトランスフォーム。 / 表示条件: `showComponents` がオンのとき |
| Hips Rigidbody | `hipsRigidbody` | `Rigidbody` | – | ラグドールの腰にあたるリジッドボディ。 / 表示条件: `showComponents` がオンのとき |
| Player COM | `playerCOM` | `Transform` | – | キャラクター本体を親子付けする中心位置の参照。 / 表示条件: `showComponents` がオンのとき |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | 死亡時に武器状態を切り替える武器マネージャー。 / 表示条件: `showComponents` がオンのとき |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | カメラ位置の基準になるメインカメラのトランスフォーム。 / 表示条件: `showComponents` がオンのとき |
| States Manager | `statesManager` | `playerStatesManager` | – | 死亡時にプレイヤー状態を更新するステート管理。 / 表示条件: `showComponents` がオンのとき |
| Health Manager | `healthManager` | `health` | – | 死亡判定やダメージ処理を行う体力管理の参照。 / 表示条件: `showComponents` がオンのとき |
| Main Collider | `mainCollider` | `Collider` | – | ラグドール中に無効化するメインコライダー。 / 表示条件: `showComponents` がオンのとき |
| Player Input | `playerInput` | `playerInputManager` | – | 死亡中に入力を止めるための入力管理の参照。 / 表示条件: `showComponents` がオンのとき |
| Main Animator | `mainAnimator` | `Animator` | – | 死亡や立ち上がりのアニメーションを制御する。 / 表示条件: `showComponents` がオンのとき |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | 死亡時に移動や操作を止めるコントローラー管理。 / 表示条件: `showComponents` がオンのとき |
| Camera Manager | `cameraManager` | `playerCamera` | – | 死亡時のカメラ挙動を制御するカメラ管理の参照。 / 表示条件: `showComponents` がオンのとき |
| Powers Manager | `powersManager` | `otherPowers` | – | 死亡時にパワー使用を止めるパワー管理の参照。 / 表示条件: `showComponents` がオンのとき |
| Gravity Manager | `gravityManager` | `gravitySystem` | – | 死亡時の重力やゼロ重力を扱う重力管理の参照。 / 表示条件: `showComponents` がオンのとき |
| IK System Manager | `IKSystemManager` | `IKSystem` | – | 体の中心位置を取得するIKシステムの参照。 / 表示条件: `showComponents` がオンのとき |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | 死亡時の速度を保存するメインのリジッドボディ。 / 表示条件: `showComponents` がオンのとき |
| Steps Manager | `stepsManager` | `footStepManager` | – | 死亡時に足音を止める足音管理の参照。 / 表示条件: `showComponents` がオンのとき |
| Combat Manager | `combatManager` | `closeCombatSystem` | – | 死亡時に近接攻撃の判定を止める戦闘管理。 / 表示条件: `showComponents` がオンのとき |
| Main Ragdoll Builder | `mainRagdollBuilder` | `ragdollBuilder` | – | ラグドールの骨やコライダー構成を提供するビルダー。 / 表示条件: `showComponents` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `onGround` | `bool` | – | – |
| `canMove` | `bool` | true | – |
| `bodyParts` | `List<bodyPart>` | new List<bodyPart> () | – |
| `colliderBodyParts` | `List<Collider>` | new List<Collider> () | – |
| `rigidbodyBodyParts` | `List<Rigidbody>` | new List<Rigidbody> () | – |
| `extraRagdollsInfoList` | `List<extraRagdollsInfo>` | new List<extraRagdollsInfo> () | – |
| `checkGetUpPaused` | `bool` | – | – |
| `ragdollAdded` | `bool` | – | – |
| `showComponents` | `bool` | – | – |
| `ignoreIfRagdollOnGroundToShowDeathMenu` | `bool` | – | – |
| `usingExtraRagdollActive` | `bool` | – | – |
| `currentExtraRagdollActiveIndex` | `int` | -1 | – |
| `skeleton` | `GameObject` | – | – |
| `currentHipsRigidbody` | `Rigidbody` | – | – |
| `currentRootMotion` | `Transform` | – | – |
| `currentCharacterBody` | `Transform` | – | – |
| `forceQuickGetUpOnCharacter` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setAdjustPositionToGroundSmoothlyActiveState(bool state)` | `adjustPositionToGroundSmoothlyActive` フラグを設定するだけ。 |
| `deathDirection(Vector3 dir)` | 死亡時の弾道方向 `damageDirection` を保存するだけ。 |
| `die(Vector3 pos)` | 死亡時に `eventOnEnterRagdoll` を発火し、武器を落として死亡音を鳴らし、死亡タイプに応じた演出を開始する。 |
| `setUseDeathSoundState(bool state)` | `useDeathSound` フラグを設定するだけ。 |
| `checkLastCheckpoint()` | `setcheckToGetUpState` を呼ぶだけのラッパー。 |
| `setForceQuickGetUpOnCharacterState(bool state)` | `forceQuickGetUpOnCharacter` フラグを設定するだけ。 |
| `setActivateQuickGetUpInsteadOfRegularGetUpState(bool state)` | `activateQuickGetUpInsteadOfRegularGetUp` フラグを設定するだけ。 |
| `setcheckToGetUpState()` | AIなら `getUp`、人間ならチェックポイント復帰を試し、使えなければ強制クイック起立か `resurrect` で復活させる。 |
| `getUp()` | クイック起立指定なら `quickGetUp` へ回し、死亡中は復活させたうえでコライダー・足音・武器・入力・ラグドールを元に戻す。 |
| `quickGetUp()` | ラグドールを即解除してルートモーションを戻し、操作・カメラ・武器・`deadState` を復帰させる即時起立処理。 |
| `enableComponentsFromGettingUp(bool isFirstPersonActive)` | 起立時にプレイヤー制御・重力・カメラ・パワー・コライダーをまとめて復帰させる。 |
| `reactiveMainCollider()` | メインコライダーを一度無効化して再度有効化し、当たり判定を再認識させる。 |
| `damageToFall()` | 転倒処理としてラグドールを有効化し、状態設定・`eventOnEnterRagdoll`発火・足音停止・起き上がりタイマーを行う。 |
| `dropOrPickCamera(bool state)` | カメラを地面へ落とす/一人称ピボットへ戻すコルーチンを開始し、既存の同コルーチンは停止する。 |
| `enableOrDisableRagdoll(bool value)` | `value` に応じてラグドール遷移とアニメーション遷移を切り替え、死亡中はボーンコライダーのタグを変更する。 |
| `setTransitionToRagdoll()` | ボディを親から切り離して物理を有効化し、アニメーターを止めて `currentState` を `ragdolled` にする。 |
| `setTransitionToAnimation()` | ラグドール位置を保存して物理を止め、`blendToAnim` へ移して仰向け/うつ伏せに応じた起き上がりアニメを設定する。 |
| `setOverrideNotUseGraviytOnRagdollActiveState(bool state)` | `overrideNotUseGraviytOnRagdollActive` フラグを設定するだけ。 |
| `setOverrideUseGraviytOnRagdollActiveState(bool state)` | `overrideUseGraviytOnRagdollActive` フラグを設定するだけ。 |
| `enableOrDisableRagdollTriggerState(bool state, string newLayer)` | ボーンコライダーをトリガーとして有効/無効にし、有効時は `newLayer`、無効時はDefaultレイヤーへ戻す。 |
| `enableRagdollTriggerState(string newLayer)` | `enableOrDisableRagdollTriggerState(true, newLayer)` を呼ぶだけ。 |
| `disableRagdollTriggerStateIfActive()` | トリガー状態が有効なときだけ `enableOrDisableRagdollTriggerState(false, "")` で解除する。 |
| `enableOrDisableRagdollPhysics(bool state)` | `setKinematic(!state)` を呼び、ラグドールの物理演算を有効/無効にする。 |
| `enableOrDisableRagdollGravityState(bool state)` | 全ボーンRigidbodyの `useGravity` を `state` に揃える。 |
| `setVelocityToRagdollInDirection(Vector3 forceDirection)` | 全ボーンRigidbodyの `linearVelocity` を `forceDirection` に設定する。 |
| `setApplyForceOnRagdollActiveState(bool state)` | `applyForceOnRagdollActive` フラグを設定するだけ。 |
| `getBodyColliderList()` | 追加ラグドール使用中ならそのコライダー一覧、そうでなければ通常の一覧を返す。 |
| `ignoreCollisionWithBodyColliderList(List<Collider> colliderList)` | 渡したコライダー群と全ボーンコライダーの衝突を `Physics.IgnoreCollision` で無視させる。 |
| `setBodyColliderList()` | `mainRagdollBuilder` の各ボーンからコライダー一覧を再構築する。 |
| `setBodyRigidbodyList()` | `mainRagdollBuilder` の各ボーンからRigidbody一覧を再構築する。 |
| `setBodyParts()` | `mainRagdollBuilder` のボーンTransformから `bodyPart` 一覧を再構築する。 |
| `getBodyRigidbodyList()` | 使用中のラグドールのRigidbody一覧を返す。 |
| `setModelAndSkeletonParentInsideCharacter()` | 死亡/転倒中のみ、キャラクターボディを `playerCOM` 配下、ルートモーションをスケルトン配下へ戻す。 |
| `setCharacterBodyParentOut()` | `currentCharacterBody` を親から切り離すだけ。 |
| `setCharacterBody(GameObject newCharacterBody, Animator currentAnimator)` | 新しいボディとAnimatorからHips・頭・足のTransform、HipsのRigidbody、スケルトンを取得し直す。 |
| `setCharacterBodyActiveState(bool state)` | `characterBody` のアクティブ状態を `state` に切り替えるだけ。 |
| `setCustomForceOnMainHipsRigidbody(Vector3 forceDirection)` | Hipsへ加えるカスタム力を保存し、非ゼロなら有効フラグを立てる。 |
| `resetLastTimeMoved()` | プレイヤー制御・カメラ・パワー・武器の最終操作時刻をリセットする。 |
| `getBodyPartsList()` | 使用中のラグドールの `bodyPart` 一覧を返す。 |
| `getBodyPartsTransformList()` | `bodyParts` のTransformだけを集めた新しいリストを返す。 |
| `pushCharacter(Vector3 direction)` | Hips位置を `damagePos` に保存し、`damageDirection` を設定して `damageToFall` を呼ぶ。 |
| `setForceRegularLayerState(bool state)` | `forceRegularLayerState` フラグを設定するだけ。 |
| `pushCharacterWithoutForce()` | 力を加える設定を一時的に切ってから `damageToFall` を呼び、勢いなしで転倒させる。 |
| `pushCharacterWithoutForceAfterDeath()` | 力を加えない状態で `enableOrDisableRagdoll(true)` を呼び、ラグドールを有効化する。 |
| `pushCharacterWithoutForceXAmountOfTime(float newValue)` | カスタム起き上がり時間を設定してから、力を加えずに転倒させる。 |
| `pushFullCharacterCheckingIfCharaterBusy()` | 運転中や多忙時を除き、ラグドール中はHipsを上へ、そうでなければ前上方へ押す。 |
| `pushFullCharacter(Vector3 direction)` | `pushAllBodyParts` を立てて `pushCharacter` を呼び、全身で押される転倒を行う。 |
| `pushFullCharacterXAmountOfTime(float newValue, Vector3 direction)` | 起き上がり時間を指定してから `pushFullCharacter` を呼ぶ。 |
| `pushHipsRigidobdy(Vector3 direction)` | ラグドール中のみ、質量を掛けた衝撃力をHipsのRigidbodyへ加える。 |
| `pushCharacterOnLastVelocity(float speedMultiplier)` | メインRigidbodyの速度に倍率を掛けた方向へ `pushFullCharacter` する。 |
| `getRootMotion()` | `currentRootMotion` を返すだけ。 |
| `getHipsRigidbody()` | `currentHipsRigidbody` を返すだけ。 |
| `sedateCharacter(float sedateDelay, bool sedateUntilReceiveDamage, float sedateDuration)` | 指定遅延の後に鎮静状態を始めるコルーチンを起動し、既存コルーチンは停止する。 |
| `stopSedateStateCoroutine()` | 鎮静コルーチンを停止し、`sedateActive` をfalseにして `health` の鎮静状態も解除する。 |
| `setImpactReceivedInfo(Vector3 impactVelocity, Collider impactCollider)` | ラグドール中に外部コライダーから十分な速度でぶつかると、速度×倍率の継続ダメージを `health` に与える。 |
| `checkDrawWeaponsWhenResurrect()` | 死亡前に武器を持っていた場合、設定に従って復活時に武器モードを再開する。 |
| `setCheckGetUpPausedState(bool state)` | `checkGetUpPaused` を設定し、解除時は起き上がりタイマーを `timeToGetUp` に戻す。 |
| `disabledCheckGetUpPaused()` | `checkGetUpPaused` をfalseにするだけ。 |
| `setIgnoreIfRagdollOnGroundToShowDeathMenuState(bool state)` | `ignoreIfRagdollOnGroundToShowDeathMenu` フラグを設定するだけ。 |
| `setIgnoreIfRagdollOnGroundToShowDeathMenuOnNextDeathState(bool state)` | 死亡中でなければ「次の死亡時に死亡メニューを出さない」フラグを設定する。 |
| `setUsedByAIState(bool state)` | `usedByAI` フラグを設定するだけ。 |
| `setDeathWithRagdollActiveState(bool state)` | `state` に応じて `typeOfDeath` を `ragdoll` か `mecanim` に切り替える。 |
| `setDeathAnimationID(int newValue)` | `deathAnimationID` を設定するだけ。 |
| `isRagdollActive()` | `currentState` が `ragdolled` かどうかを返す。 |
| `checkIfDisableRagdollActivatorComponent()` | `activateRagdollAfterDeath` が無効なら、このコンポーネントを無効化する。 |
| `setRagdollOnExternalParent(Transform newParent)` | `ragdollExternalParent` を設定するだけ。 |
| `setPauseAnimatorStatesToGetUpState(bool state)` | `pauseAnimatorStatesToGetUp` フラグを設定するだけ。 |
| `setExtraForceOnRagdollValue(float newValue)` | `extraForceOnRagdoll` を設定するだけ。 |
| `setStateToGetUpOnAirActive(bool state)` | `stateToGetUpOnAirActive` フラグを設定するだけ。 |
| `addNewExtraRagdollInfo(GameObject newCharacterBody, string ragdollName, List<Transform> bonesList, List<Rigidbody> rigidbodyList, List<Collider> colliderList, Transform hipsTransform, float rotationYOffsetValue, bool addingRagdollOnEditorTime)` | 同名の既存項目があれば再利用し、ボーン・Rigidbody・コライダー・Hips・Y回転補正を追加ラグドール情報として登録する。 |
| `setCurrentRagdollInfo(string ragdollName)` | 指定名の追加ラグドールを現在の使用対象に切り替え、Hips・ルートモーション・ボディを差し替える（空文字なら通常に戻す）。 |
| `setUseDeathSoundStateFromEditor(bool state)` | `useDeathSound` を設定し、エディタ用にコンポーネントを更新する。 |
| `setDeathWithRagdollActiveStateFromEditor(bool state)` | 死亡タイプを切り替えたうえで、エディタ用にコンポーネントを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnEnterRagdoll` | `UnityEvent` | – |
| `eventOnExitRagdoll` | `UnityEvent` | – |
| `eventOnDeath` | `UnityEvent` | – |
| `eventOnResurrect` | `UnityEvent` | – |

## 内部型

- `healthState`（enum）
- `ragdollState`（enum）
- `deathType`（enum）
- `bodyPart`（class）
- `extraRagdollsInfo`（class）
