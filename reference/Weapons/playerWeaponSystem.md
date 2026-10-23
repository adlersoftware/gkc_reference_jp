# playerWeaponSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/playerWeaponSystem.cs:8`

**概要**: 個々の武器オブジェクトに付くコンポーネントで、`weaponInfo`(`weaponSettings`)に持つ装弾数・残弾・発射レート・威力・弾・サウンド・耐久値などの設定を保持し、`playerWeaponsManager` と `IKWeaponSystem` への参照を通じて射撃・リロード・HUD・耐久に関わる値を管理する。ここに載るメソッドは他コンポーネントやエディタから設定値を読み書きするための薄いアクセサが中心。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Fire Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer To Check | `layer` | `LayerMask` | – | 射撃レイキャストが当たり判定するレイヤー。 / 表示条件: `showWeaponSettings.boolValue \|\| showAllSettings.boolValue` |

### Weapon Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Game Object | `playerControllerGameObject` | `GameObject` | – | 装備位置やコライダー取得に使うプレイヤー本体。 / 表示条件: `showWeaponSettings.boolValue \|\| showAllSettings.boolValue` |
| Player Camera Game Object | `playerCameraGameObject` | `GameObject` | – | 弾道計算や照準に使うカメラ側のGameObject。 / 表示条件: `showWeaponSettings.boolValue \|\| showAllSettings.boolValue` |

### Weapon Place On Player's Body Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Human Body Bones Enum | `useHumanBodyBonesEnum` | `bool` | – | ONなら親ボーンを`HumanBodyBones`で指定する。 / 表示条件: `showWeaponSettings.boolValue \|\| showAllSettings.boolValue` |
| Weapon Parent Bone | `weaponParentBone` | `HumanBodyBones` | – | 武器を親子付ける人間ボーンの種類。 / 表示条件: `showWeaponSettings.boolValue \|\| showAllSettings.boolValue && useHumanBodyBonesEnum.boolValue` |
| Use Mount Point For Weapon Parent | `useMountPointForWeaponParent` | `bool` | – | ONなら武器の親をマウントポイント名で指定する。 / 表示条件: `showWeaponSettings.boolValue \|\| showAllSettings.boolValue` |
| Mount Point Name For Weapon Parent | `mountPointNameForWeaponParent` | `string` | – | 武器を親子付けるマウントポイントの名前。 / 表示条件: `showWeaponSettings.boolValue \|\| showAllSettings.boolValue && useMountPointForWeaponParent.boolValue` |

### Projectile Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Projectiles Pool Enabled | `projectilesPoolEnabled` | `bool` | true | ONにすると発射体や薬莢をプールで再利用する。 / 表示条件: `showProjectileSettings.boolValue \|\| showAllSettings.boolValue` |
| Max Amount Of Pool Elements On Weapon | `maxAmountOfPoolElementsOnWeapon` | `int` | 30 | 武器ごとにプールへ保持する最大要素数。 / 表示条件: `showProjectileSettings.boolValue \|\| showAllSettings.boolValue` |
| Weapon Projectile | `weaponProjectile` | `GameObject` | – | 発射時に生成する発射体のプレハブ。 / 表示条件: `showProjectileSettings.boolValue \|\| showAllSettings.boolValue` |
| Check For Extra Colliders On Weapon Owner If Detected | `checkForExtraCollidersOnWeaponOwnerIfDetected` | `bool` | – | ONなら追加コライダーも自キャラ判定に含める。 / 表示条件: `showProjectileSettings.boolValue \|\| showAllSettings.boolValue` |
| Ignore Trigger On Raycast Enabled | `ignoreTriggerOnRaycastEnabled` | `bool` | true | ONなら射撃レイキャストでトリガーを無視する。 / 表示条件: `showProjectileSettings.boolValue \|\| showAllSettings.boolValue` |

### Push Characters Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Effects Source | `weaponEffectsSource` | `AudioSource` | – | 発射音などの効果音を再生する`AudioSource`。 / 表示条件: `showSoundAndParticlesSettings.boolValue \|\| showAllSettings.boolValue` |

### Sound Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Out Of Ammo | `outOfAmmo` | `AudioClip` | – | 残弾切れ時に再生する`AudioClip`。 / 表示条件: `showSoundAndParticlesSettings.boolValue \|\| showAllSettings.boolValue` |
| Out Of Ammo Audio Element | `outOfAmmoAudioElement` | `AudioElement` | – | 残弾切れ音のクリップと再生設定を保持する要素。 / 表示条件: `showSoundAndParticlesSettings.boolValue \|\| showAllSettings.boolValue` |

### Dual Weapon Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Set Dual Weapon | `useEventOnSetDualWeapon` | `bool` | – | ONにすると二丁持ち設定時にイベントを呼ぶ。 / 表示条件: `showEventsSettings.boolValue \|\| showAllSettings.boolValue` |
| Event On Set Right Weapon | `eventOnSetRightWeapon` | `UnityEvent` | – | 右手側の武器として設定された時に呼ぶイベント。 / 表示条件: `showEventsSettings.boolValue \|\| showAllSettings.boolValue && useEventOnSetDualWeapon.boolValue` |
| Event On Set Left Weapon | `eventOnSetLeftWeapon` | `UnityEvent` | – | 左手側の武器として設定された時に呼ぶイベント。 / 表示条件: `showEventsSettings.boolValue \|\| showAllSettings.boolValue && useEventOnSetDualWeapon.boolValue` |

### Single Weapon Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Set Single Weapon | `useEventOnSetSingleWeapon` | `bool` | – | ONにすると単体武器の設定時にイベントを呼ぶ。 / 表示条件: `showEventsSettings.boolValue \|\| showAllSettings.boolValue` |
| Event On Set Single Weapon | `eventOnSetSingleWeapon` | `UnityEvent` | – | 単体武器として設定された時に呼ぶイベント。 / 表示条件: `showEventsSettings.boolValue \|\| showAllSettings.boolValue && useEventOnSetSingleWeapon.boolValue` |

### Remote Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | ONなら発射体の命中先へリモートイベントを送る。 / 表示条件: `showEventsSettings.boolValue \|\| showAllSettings.boolValue && showRemoteEventsSettings` |
| Use Remote Event On Objects Found On Explosion | `useRemoteEventOnObjectsFoundOnExplosion` | `bool` | – | ONなら爆発の範囲内へリモートイベントを送る。 / 表示条件: `showEventsSettings.boolValue \|\| showAllSettings.boolValue && showRemoteEventsSettings` |
| Remote Event Name On Explosion | `remoteEventNameOnExplosion` | `string` | – | 爆発時に送るリモートイベントの名前。 / 表示条件: `showRemoteEventsSettings && useRemoteEventOnObjectsFoundOnExplosion.boolValue` |

### Durability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Object Durability | `useObjectDurability` | `bool` | – | ONにすると攻撃でこの武器の耐久度を消費する。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue` |
| Durability Used On Attack | `durabilityUsedOnAttack` | `float` | 1 | 1回の攻撃で減らす耐久度の量。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue` |
| Main Durability Info | `mainDurabilityInfo` | `durabilityInfo` | – | 耐久度の値や名前を保持する情報。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue` |

### Scorch from Decal Manager

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Decal Manager Name | `mainDecalManagerName` | `string` | "Decal Manager" | シーンに無い時に生成する`decalManager`の名前。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue` |

### Shoot Noise Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Noise Mesh Manager Name | `mainNoiseMeshManagerName` | `string` | "Noise Mesh Manager" | 射撃ノイズ用メッシュマネージャーの名前。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue` |

### Mark Targets Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Mark Targets | `canMarkTargets` | `bool` | – | ONにするとこの武器でターゲットをマークできる。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue` |

### Tag List To Mark Targets

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Mark Target Name | `markTargetName` | `string` | – | マークした対象に表示するアイコンの名前。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue && canMarkTargets.boolValue` |
| Max Distance To Mark Targets | `maxDistanceToMarkTargets` | `float` | – | マーク判定のレイキャストを届かせる距離。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue && canMarkTargets.boolValue` |
| Mark Targets Layer | `markTargetsLayer` | `LayerMask` | – | マーク判定のレイキャストが対象とするレイヤー。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue && canMarkTargets.boolValue` |
| Can Mark Targets On First Person | `canMarkTargetsOnFirstPerson` | `bool` | – | ONにすると一人称視点でもマークできる。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue && canMarkTargets.boolValue` |
| Can Mark Targets On Third Person | `canMarkTargetsOnThirdPerson` | `bool` | – | ONにすると三人称視点でもマークできる。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue && canMarkTargets.boolValue` |
| Aim On First Person To Mark Target | `aimOnFirstPersonToMarkTarget` | `bool` | – | ONなら一人称でエイム中のみマークできる。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue && canMarkTargets.boolValue` |
| Use Mark Target Sound | `useMarkTargetSound` | `bool` | – | ONにするとマーク成功時に効果音を鳴らす。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue && canMarkTargets.boolValue` |
| Mark Target Sound | `markTargetSound` | `AudioClip` | – | マーク成功時に再生する`AudioClip`。 / 表示条件: `canMarkTargets.boolValue && useMarkTargetSound.boolValue` |
| Mark Target Audio Element | `markTargetAudioElement` | `AudioElement` | – | マーク音のクリップと再生設定を保持する要素。 / 表示条件: `canMarkTargets.boolValue && useMarkTargetSound.boolValue` |

### Enable/Disable Abilities on Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Abilities List To Enable On Weapon | `useAbilitiesListToEnableOnWeapon` | `bool` | – | ONならこの武器の選択時に能力を有効化する。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue` |
| Use Abilities List To Disable On Weapon | `useAbilitiesListToDisableOnWeapon` | `bool` | – | ONならこの武器を外した時に能力を無効化する。 / 表示条件: `showOtherSettings.boolValue \|\| showAllSettings.boolValue` |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `weaponSettings` | `weaponInfo` | – | – |
| `reloadingWithAnimationActive` | `bool` | – | – |
| `reloading` | `bool` | – | – |
| `carryingWeaponInThirdPerson` | `bool` | – | – |
| `carryingWeaponInFirstPerson` | `bool` | – | – |
| `aimingInThirdPerson` | `bool` | – | – |
| `aimingInFirstPerson` | `bool` | – | – |
| `impactDecalList` | `string []` | – | – |
| `impactDecalIndex` | `int` | – | – |
| `impactDecalName` | `string` | – | – |
| `tagListToMarkTargets` | `List<string>` | new List<string> () | – |
| `IKWeaponManager` | `IKWeaponSystem` | – | – |
| `weaponsManager` | `playerWeaponsManager` | – | – |
| `parable` | `launchTrayectory` | – | – |
| `playerCollider` | `Collider` | – | – |
| `FBAWeaponColliderAssigned` | `bool` | – | – |
| `FBAWeaponCollider` | `Collider` | – | – |
| `headColliderOnFBAAssigned` | `bool` | – | – |
| `headColliderOnFBA` | `Collider` | – | – |
| `mainCamera` | `Camera` | – | – |
| `mainCameraTransform` | `Transform` | – | – |
| `weaponAnimation` | `Animation` | – | – |
| `remoteEventNameList` | `List<string>` | new List<string> () | – |
| `abilitiesListToEnableOnWeapon` | `List<string>` | new List<string> () | – |
| `abilitiesListToDisableOnWeapon` | `List<string>` | new List<string> () | – |
| `weaponCrossingSurface` | `bool` | – | – |
| `showAllSettings` | `bool` | – | – |
| `showHUDSettings` | `bool` | – | – |
| `showWeaponSettings` | `bool` | – | – |
| `showProjectileSettings` | `bool` | – | – |
| `showAmmoSettings` | `bool` | – | – |
| `showEventsSettings` | `bool` | – | – |
| `showFireTypeSettings` | `bool` | – | – |
| `showSoundAndParticlesSettings` | `bool` | – | – |
| `showOtherSettings` | `bool` | – | – |
| `weaponObjectActive` | `bool` | true | – |
| `currentWeapon` | `bool` | – | – |
| `weaponUpdateActive` | `bool` | – | – |
| `fullBodyAwarenessActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `initializeComponents()` | 初回のみ、武器名の付与、元設定値の保存、弾数初期化、`keepPositions`生成、HUD無効化、IK初期化を行う。 |
| `isWeaponUpdateActive()` | `weaponUpdateActive`を返すだけで、更新コルーチンが動作中かを示す。 |
| `activateWeaponUpdate()` | 動作中なら更新コルーチンを再開始し、`weaponUpdateActive`をtrueにする。 |
| `stopActivateWeaponUpdate()` | `updateWeaponCoroutine`を停止し、`weaponUpdateActive`をfalseにする。 |
| `setWeaponCarryStateAtOnce(bool state)` | 一人称と三人称の携帯状態を同じ`state`に揃えて設定するだけ。 |
| `setWeaponCarryState(bool thirdPersonCarry, bool firstPersonCarry)` | 両視点の携帯状態を設定し、パラボラや能力確認、描画・収納イベント、効果音、待機IDを更新する。 |
| `setPauseDrawKeepWeaponSound()` | 次回の`setWeaponCarryState`で描画・収納音を鳴らさないフラグを立てるだけ。 |
| `setWeaponAimState(bool thirdPersonAim, bool firstPersonAim)` | 両視点の照準状態を設定し、空なら自動リロード、パラボラ・能力・照準イベント・スナイパーサイトを更新する。 |
| `checkWeaponDrawEvents()` | 一人称か三人称かに応じて、対応する描画開始／収納アクションを実行する。 |
| `checkWeaponDrawEventsOnFullBodyAwarenessChangeState()` | FBA切替時に、前の視点の収納アクションと新しい視点の描画アクションを実行する。 |
| `checkWeaponAimEvents()` | 一人称か三人称かに応じて、対応する照準開始／解除アクションを実行する。 |
| `checkWeaponEventsAfterReload()` | FBA中なら描画イベント、そうでなければ照準イベントを再実行するだけ。 |
| `setIgnoreSniperSightActiveState(bool state)` | trueなら先にスナイパーサイトを更新し、その後`ignoreSniperSightActive`を設定する。 |
| `checkSniperSightUsedOnWeapon()` | 無視フラグ中は何もせず、一人称／三人称の照準状態を`IKWeaponManager`へ渡してサイトを切り替える。 |
| `setFullBodyAwarenessActiveState(bool state)` | `fullBodyAwarenessActive`を設定するだけ。 |
| `getIKWeaponSystem()` | `IKWeaponManager`を返すだけ。 |
| `weaponIsMoving()` | `IKWeaponManager.isWeaponMoving`に問い合わせて返すだけ。 |
| `isWeaponOnRecoil()` | `IKWeaponManager.isWeaponOnRecoil`に問い合わせて返すだけ。 |
| `isAimingWeapon()` | 一人称か三人称のどちらかで照準中かを返す。 |
| `isAimingInThirdPerson()` | 三人称で照準中かを返すだけ。 |
| `carryingWeapon()` | 一人称か三人称のどちらかで携帯中かを返す。 |
| `isShootingBurst()` | バースト射撃中かを返すだけ。 |
| `resetLastAmountOfFiredProjectiles()` | `lastAmountOfFiredProjectiles`を0に戻すだけ。 |
| `getLastAmountOfFiredProjectiles()` | 直前に発射した弾数を返すだけ。 |
| `checkEventsOnWeaponInput(bool shootAtKeyDown)` | 入力の押下／解放に応じて、対応する武器入力イベントを実行する。 |
| `shootWeapon(bool isThirdPersonView, bool shootAtKeyDown, bool fullbodyAwarenessActive)` | 各種前提を確認して弾を生成し、反動・発砲音・弾薬消費・拡散・命中処理を実行、弾切れ時は空打ち音や武器切替を行う。 |
| `checkWeaponCameraShake()` | 使用中の手を渡して`weaponsManager`のカメラシェイクを実行するだけ。 |
| `checkMeleeAttackShakeInfo()` | 一人称または三人称の近接攻撃用シェイク情報を`weaponsManager`のヘッドボブに設定する。 |
| `checkWeaponAbility(bool keyDown)` | 能力付き武器で、押下ならダウン、解放ならアップのアクションを実行する（FBA時は条件付き）。 |
| `checkWeaponAbilityHoldButton()` | 能力付き武器でホールドボタンのアクションを実行するだけ。 |
| `canUseSecondaryAction()` | 一人称携帯か、設定・三人称照準・FBAの条件を満たす場合にセカンダリ操作を許可する。 |
| `activateSecondaryAction()` | `canUseSecondaryAction`を満たす場合に`secondaryAction`を実行する。 |
| `activateSecondaryActionOnDownPress()` | 使用可能なら`secondaryActionOnDownPress`を実行する。 |
| `activateSecondaryActionOnUpPress()` | 使用可能なら`secondaryActionOnUpPress`を実行する。 |
| `activateSecondaryActionOnUpHold()` | 使用可能なら`secondaryActionOnHoldPress`を実行する。 |
| `activateForwardAcion()` | `forwardActionEvent`を実行し、`IKWeaponManager`の最終移動時刻を更新する。 |
| `activateBackwardAcion()` | `backwardActionEvent`を実行し、`IKWeaponManager`の最終移動時刻を更新する。 |
| `checkEventsOnWeaponActivatedOrDeactivated(bool state)` | `state`に応じて武器の有効化／無効化イベントを実行するだけ。 |
| `removeLocatedEnemiesIcons()` | 捕捉した敵のアイコンを全て削除し、`locatedEnemies`を空にする。 |
| `updateProjectileInfoValues()` | `projectileInfoAssigned`をfalseにし、`setProjectileInfo`で弾情報を作り直す。 |
| `setProjectileInfoAssignedValue(bool state)` | `projectileInfoAssigned`を設定するだけ。 |
| `setSeekerProjectileInfo(Vector3 shootPosition)` | カメラを補完し、索敵設定を渡して`applyDamage`から最寄りの敵を取得して返す。 |
| `setProjectileSpread()` | 携帯視点と照準状態から拡散量を決め、±拡散量のランダムな回転量を返す。 |
| `createShells()` | `shellCreated`をtrueにし、設定に応じて遅延または即時の排莢を行う。 |
| `createShellsWithDelay()` | 既存の排莢コルーチンを止め、視点別の遅延後に排莢するコルーチンを開始する。 |
| `checkDroppedShellsRemoval()` | 排莢の経過時間を加算し、3秒を超えたら殻を破棄またはプールへ戻して状態を初期化する。 |
| `playSound(AudioElement clipSound)` | 再生停止フラグ中は何もせず、効果音用`AudioSource`を割り当てて1回再生する。 |
| `pauseOrResumePlaySoundOnWeapon(bool state)` | `playSound`を止めるための`playSoundPaused`を設定するだけ。 |
| `getAudioSourceFromPool()` | 再生中でない効果音用`AudioSource`を返し、無ければ上限まで生成してリストに追加する。 |
| `setAmmoValues()` | `ammoPerClip`・初期装填数・空開始設定・拡張値を反映し、弾数を初期化する。 |
| `useAmmo()` | 無視フラグが無ければ`clipSize`を1減らし、HUDと`weaponsManager`の弾表示を更新する。 |
| `useAmmo(int amount)` | `amount`を残弾数までに制限して`clipSize`から引き、弾表示を更新する。 |
| `updateAmmoInfo()` | FBA中は何もせず、HUDがあればマガジン数と残弾数（無限なら`Inf`）のテキストを更新する。 |
| `reloadSingleProjectile()` | 弾を1発だけマガジンへ補充し（インベントリ使用時はそちらから消費）、弾表示を更新する。 |
| `checkToUpdateInventoryWeaponAmmoTextFromWeaponSystem()` | `weaponsManager`にインベントリの弾表示更新を依頼するだけ。 |
| `checkToUpdateInventoryWeaponAmmoTextByWeaponNumberKey()` | 自身の武器番号キーを渡してインベントリの弾表示更新を依頼するだけ。 |
| `setInitialProjectilesInMagazine(int newProjectilesInMagazine)` | 初期装填数を保存し、`setAmmoValues`で弾数を計算し直す。 |
| `getProjectilesInMagazine()` | 現在の`clipSize`を返すだけ。 |
| `setRemainAmmoAmount(int newRemainAmmoAmount)` | 値が異なる場合のみ残弾数を設定し、HUDと`auxRemainAmmo`を更新する。 |
| `setIgnoreReloadAnimationAndDelayActiveState(bool state)` | `ignoreReloadAnimationAndDelayActive`を設定するだけ。 |
| `setIgnoreUseAmmoActiveState(bool state)` | `ignoreUseAmmoActive`を設定するだけ。 |
| `reloadWeapon()` | リロード禁止中は何もせず、遅延無視設定なら即座に弾を補充、そうでなければリロードコルーチンを開始する。 |
| `stopReloadCoroutine()` | `reloadCoroutine`を停止するだけ。 |
| `cancelReloadIfActive()` | リロード中ならコルーチンとリロード動作を止め、キャンセルイベントを実行する。 |
| `stopReloadAction()` | 弾数を再計算し、`reloading`をfalseにしてリロードアニメーションを巻き戻す。 |
| `isWeaponReloading()` | `reloading`を返すだけ。 |
| `canUseReloadAnimation()` | 一人称／三人称それぞれのリロードアニメーション許可設定に応じて可否を返す。 |
| `manualReload()` | リロード中でなく、弾を使用し、装填数が上限未満なら`reloadWeapon`を呼ぶ。 |
| `setReloadingWithAnimationActiveState(bool state)` | `reloadingWithAnimationActive`を設定するだけ。 |
| `isReloadingWithAnimationActive()` | `reloadingWithAnimationActive`を返すだけ。 |
| `enableHUD(bool state)` | HUDの有無と設定、両手持ち時の視点別設定を確認して表示を切り替え、弾表示を更新する。 |
| `enableHUDTemporarily(bool state)` | FBA中は常に非表示とし、`useHUD`の範囲でHUD表示だけを切り替える。 |
| `changeHUDPosition(bool thirdPerson)` | 両手持ちか通常かに応じ、`ammoInfoHUD`を視点別・手別の位置へ移動する。 |
| `getWeaponHUDGameObject()` | `weaponSettings.HUD`を返すだけ。 |
| `canIncreaseRemainAmmo()` | `auxRemainAmmo`が`ammoLimit`未満かを返す。 |
| `hasMaximumAmmoAmount()` | 弾数上限が有効で、残弾が上限以上ならtrueを返す。 |
| `hasAmmoLimit()` | `useAmmoLimit`を返すだけ。 |
| `ammoAmountToMaximumLimit()` | 上限までの残り弾数（`ammoLimit - auxRemainAmmo`）を返す。 |
| `getAmmo(int amount)` | 弾薬ピックアップ分を残弾（インベントリ使用時はマガジン）へ加え、空だった場合は自動リロードし、表示を更新する。 |
| `useRemainAmmo(int amount)` | 残弾から`amount`を引き、負にならないよう0で止めて表示を更新する。 |
| `addAuxRemainAmmo(int amount)` | `auxRemainAmmo`に`amount`を加えるだけ。 |
| `hasAnyAmmo()` | 残弾・マガジン・無限弾・弾不使用のいずれかならtrueを返す。 |
| `getAndUpdateAmmo(int amount)` | `getAmmo`を呼んだ後、`weaponsManager.updateAmmo`で表示を更新する。 |
| `remainAmmoInClip()` | `clipSize`が0より大きいかを返すだけ。 |
| `launchCurrentProjectile(GameObject currentProjectile, Rigidbody projectileRigidbody, Vector3 cameraDirection)` | `isKinematic`を解除し、パラボラ速度か`projectileSpeed`の力を加えて発射する。 |
| `checkParableTrayectory(bool usingThirdPerson, bool usingFirstPerson)` | 設定と視点に応じてパラボラ軌道表示を有効／無効にし、発射位置を設定する。 |
| `setCurrentWeaponState(bool state)` | `currentWeapon`を設定し、非選択時は時刻を記録、選択に応じて能力グループを有効／無効化する。 |
| `getWeaponParent()` | 初期の親`Transform`を返すだけ。 |
| `getWeaponsParent()` | `weaponSettings.weaponParent`を返し、無ければnullを返す。 |
| `getMainCameraTransform()` | `mainCameraTransform`を返すだけ。 |
| `setReducedVelocity(float multiplierValue)` | `weaponSpeed`に`multiplierValue`を掛けて減速する。 |
| `setNormalVelocity()` | `weaponSpeed`を保存しておいた`originalWeaponSpeed`に戻す。 |
| `getWeaponSystemAmmoName()` | `weaponSettings.ammoName`を返すだけ。 |
| `getWeaponSystemName()` | `weaponSettings.Name`を返すだけ。 |
| `getWeaponNumberKey()` | `weaponSettings.numberKey`を返すだけ。 |
| `getOriginalWeaponNumberKey()` | `originalNumberKey`を返すだけ。 |
| `getWeaponClipSize()` | 現在の`clipSize`を返すだけ。 |
| `getWeaponOriginalClipSize()` | `originalClipSize`を返すだけ。 |
| `getMagazineSize()` | `ammoPerClip`を返すだけ。 |
| `isCurrentMagazineEmpty()` | `clipSize`が0かを返すだけ。 |
| `isRemainAmmoEmpty()` | `remainAmmo`が0かを返すだけ。 |
| `getCurrentAmmoText()` | 「マガジン数／残弾数」形式の文字列を返し、無限弾なら残弾を`Inf`にする。 |
| `getAllRemainAmmoOnWeapon()` | マガジン数と残弾数の合計を返し、無限弾ならマガジン数のみ返す。 |
| `getRegularRemainAmmo()` | `weaponSettings.remainAmmo`を返すだけ。 |
| `getWeaponIcon()` | `weaponSettings.weaponIcon`を返すだけ。 |
| `getWeaponIConHUD()` | `weaponSettings.weaponIConHUD` のHUD用アイコンを返す。 |
| `getWeaponInventorySlotIcon()` | `weaponSettings.weaponInventorySlotIcon` のインベントリスロット用アイコンを返す。 |
| `setWeaponInventorySlotIcon(Texture newTexture)` | null以外のとき `weaponSettings.weaponInventorySlotIcon` を設定するだけ。 |
| `setWeaponIconHUD(Texture newTexture)` | `newTexture` がnullでなければ `weaponSettings.weaponIConHUD` に設定するだけ。 |
| `setWeaponIcon(Texture newTexture)` | `newTexture` がnullでなければ `weaponSettings.weaponIcon` に設定するだけ。 |
| `setWeaponInventorySlotIconInEditor(Texture newTexture)` | スロットアイコンを設定したうえで `updateComponent` を呼び、シーンとコンポーネントを更新する。 |
| `setWeaponIconHUDInEditor(Texture newTexture)` | HUDアイコンを設定したうえで `updateComponent` を呼ぶ。 |
| `setWeaponIconInEditor(Texture newTexture)` | 武器アイコンを設定したうえで `updateComponent` を呼ぶ。 |
| `setNumberKey(int newNumberKey)` | `originalNumberKey` が-1のとき現在値を保存し、`weaponSettings.numberKey` を更新する。 |
| `enableMuzzleFlashLight()` | `useMuzzleFlash` 有効時のみ、既存コルーチンを止めて点灯コルーチンを開始する。 |
| `checkWeaponShootNoise()` | `silencerActive` なら何もせず、`useNoise` 時に `sendNoiseSignal` とノイズメッシュで通知する。 |
| `setMagazineSize(int magazineSize)` | `weaponSettings.ammoPerClip` を変更し、武器HUDと弾薬表示を更新する。 |
| `getAmmoAmountToRefillMagazine()` | `ammoPerClip` と `clipSize` の差、つまりマガジン補充に必要な弾数を返す。 |
| `getPlayerWeaponsManger()` | 保持している `playerWeaponsManager` の参照を返す。 |
| `setOriginalMagazineSize()` | 装弾数が元値を超えていれば超過分を `remainAmmo` に戻して元の装弾数に設定し、`auxRemainAmmo` も更新する。 |
| `setCurrentProjectilesInMagazine(int newAmount)` | `weaponSettings.clipSize` を `newAmount` にし、武器HUDと弾薬表示を更新する。 |
| `setSilencerState(bool state)` | `silencerActive` フラグを `state` にするだけ。 |
| `setAutomaticFireMode(bool state)` | `weaponSettings.automatic` を `state` にするだけ。 |
| `setOriginalAutomaticFireMode()` | `originalAutomaticMode` の値で自動射撃設定を戻す。 |
| `setFireRate(float newFireRate)` | `weaponSettings.fireRate` を `newFireRate` にするだけ。 |
| `setOriginalFireRate()` | `originalFireRate` の値で発射レートを戻す。 |
| `setProjectileDamage(float newDamage)` | `weaponSettings.projectileDamage` を `newDamage` にするだけ。 |
| `setOriginalProjectileDamage()` | `originalProjectileDamage` の値で弾威力を戻す。 |
| `setWeaponShootSoundEffect(AudioClip newClip)` | 射撃音を `weaponSettings.shootSoundEffect` と `shootAudioElement.clip` の両方に設定する。 |
| `setWeaponImpactSoundEffect(AudioClip newClip)` | 着弾音を設定し、`projectileInfoAssigned` をfalseにして弾情報の再割当を促す。 |
| `setCustomWeaponImpactSoundEffect(AudioClip newClip)` | `customShootSoundEffect` を設定して有効フラグと `impactAudioElement.clip` を更新し、再割当フラグを下ろす。 |
| `setCustomImpactSoundEffect(AudioClip newClip)` | `customImpactSoundEffect` を設定して有効フラグと `shootAudioElement.clip` を更新し、再割当フラグを下ろす。 |
| `setWeaponUseRayCastShoot(bool state)` | `weaponSettings.useRayCastShoot` を `state` にするだけ。 |
| `setOriginalWeaponUseRayCastShoot()` | `originalUseRayCastShootValue` の値でレイキャスト射撃設定を戻す。 |
| `setBurstModeState(bool state)` | `useBurst` を設定し、有効なら `automatic` をtrue、無効なら `originalAutomaticMode` に戻す。 |
| `setOriginalBurstMode()` | `orignalUseBurst` の値でバースト設定を戻す。 |
| `setBurstAmount(int newAmount)` | `weaponSettings.burstAmount` を `newAmount` にするだけ。 |
| `setUsingSightState(bool state)` | `usingSight` フラグを `state` にするだけ。 |
| `setUsingSightFullBodyAwareness(bool state)` | `usingSightFullBodyAwareness` フラグを `state` にするだけ。 |
| `isUsingSightFullBodyAwareness()` | `usingSightFullBodyAwareness` の値を返す。 |
| `setProjectileDamageMultiplier(float multiplier)` | `originalProjectileDamage` に `multiplier` を掛けた値を `projectileDamage` へ設定する。 |
| `setSpreadState(bool state)` | `weaponSettings.useProjectileSpread` を `state` にするだけ。 |
| `setOriginalSpreadState()` | `originalSpreadState` の値で拡散設定を戻す。 |
| `isUsingSight()` | `usingSight` の値を返す。 |
| `setKillOneShotState(bool state)` | `weaponSettings.killInOneShot` を `state` にするだけ。 |
| `setExplosiveAmmoState(bool state)` | `weaponSettings.isExplosive` を `state` にするだけ。 |
| `setOriginalExplosiveAmmoState()` | `originalIsExplosiveState` の値で爆発弾設定を戻す。 |
| `setDamageOverTimeAmmoState(bool state)` | `weaponSettings.damageTargetOverTime` を `state` にするだけ。 |
| `setOriginalDamageOverTimeAmmoState()` | `originalDamageTargetOverTimeState` の値で継続ダメージ弾設定を戻す。 |
| `setRemoveDamageOverTimeAmmoState(bool state)` | `weaponSettings.removeDamageOverTimeState` を設定したうえで `resetAmmoState` を呼ぶ。 |
| `setOriginalRemoveDamageOverTimeAmmoState()` | 元の継続ダメージ除去設定に戻し、その値で `resetAmmoState` を呼ぶ。 |
| `setSedateAmmoState(bool state)` | `weaponSettings.sedateCharacters` を設定したうえで `resetAmmoState` を呼ぶ。 |
| `setOriginalSedateAmmoState()` | `originalSedateCharactersState` に戻し、その値で `resetAmmoState` を呼ぶ。 |
| `resetAmmoState(bool state)` | trueなら弾威力を0にして爆発・継続ダメージを無効化し、falseならそれぞれ元の値へ復元する。 |
| `getFireRate()` | `fireRate` に `getFireRateMultiplierStat` の倍率を掛けて返す。 |
| `setPushCharacterState(bool state)` | `weaponSettings.pushCharacter` を `state` にするだけ。 |
| `setOriginalPushCharacterState()` | `originalPushCharacterState` の値でプッシュ設定を戻す。 |
| `useCustomReticleEnabled()` | `weaponSettings.useCustomReticle` の値を返す。 |
| `getRegularCustomReticle()` | `weaponSettings.regularCustomReticle` のテクスチャを返す。 |
| `useAimCustomReticleEnabled()` | `weaponSettings.useAimCustomReticle` の値を返す。 |
| `getAimCustomReticle()` | `weaponSettings.aimCustomReticle` のテクスチャを返す。 |
| `useDynamicReticleEnabled()` | `weaponSettings.useDynamicReticle` の値を返す。 |
| `getDynamicReticleName()` | `weaponSettings.dynamicReticleName` を返す。 |
| `isUseRemainAmmoFromInventoryActive()` | 武器個別の設定か全武器共通設定のいずれかでインベントリの残弾使用が有効かを返す。 |
| `setNewWeaponProjectile(GameObject newProjectile)` | `weaponProjectile` を `newProjectile` に差し替えるだけ。 |
| `setOriginalWeaponProjectile()` | `weaponProjectile` を `originalWeaponProjectile` に戻すだけ。 |
| `setProjectileWithAbilityState(bool newValue)` | `weaponSettings.projectileWithAbility` を `newValue` にするだけ。 |
| `setOriginalProjectileWithAbilityValue()` | `originalProjectileWithAbilityState` の値でアビリティ付き弾設定を戻す。 |
| `setUsingDualWeaponState(bool state)` | `usingDualWeapon` を設定し、解除時は `eventOnSetSingleWeapon` (有効時) を発火する。 |
| `setUsingRightHandDualWeaponState(bool state)` | `usingRightHandDualWeapon` を設定し、`useEventOnSetDualWeapon` 有効時に左右対応のイベントを発火する。 |
| `resetWeaponMeshTransform()` | 武器メッシュのローカル位置をゼロ、ローカル回転を `Quaternion.identity` に戻す。 |
| `enableOrDisableWeaponMesh(bool state)` | 現在のアクティブ状態が異なる場合のみ `weaponSettings.weaponMesh` のアクティブを `state` に切り替える。 |
| `setWeaponMeshScale(float newValue)` | 武器メッシュのローカルスケールを全軸 `newValue` にする。 |
| `placeMagazineInPlayerHand(bool state)` | マガジンモデルが未生成なら生成し、表示を `state` に合わせ、表示時は `IKWeaponManager` に手元へ配置させる。 |
| `setNewReloadTimeFirstPerson(float newValue)` | `weaponSettings.reloadTimeFirstPerson` を `newValue` にするだけ。 |
| `setInfiniteAmmoValue(bool state)` | `weaponSettings.infiniteAmmo` を `state` にするだけ。 |
| `setOriginalInfiniteAmmo()` | `originalInfiniteAmmo` の値で無限弾薬設定を戻す。 |
| `setSliceObjectsDetectedState(bool state)` | `weaponSettings.sliceObjectsDetected` を `state` にするだけ。 |
| `setOriginalSliceObjectsDetected()` | `originalSliceObjectsDetected` の値で切断設定を戻す。 |
| `setProjectileSpecialActionActiveState(bool state)` | `projectileSpecialActionActive` フラグを `state` にするだけ。 |
| `setProjectileSpecialActionValue(bool state)` | `projectileSpecialActionValue` フラグを `state` にするだけ。 |
| `checkDurabilityOnAttack()` | 耐久有効時、`durabilityUsedOnAttack` 分を減らし、尽きたら `checkEventOnEmptyDurability` を呼ぶ。 |
| `updateDurabilityAmountState()` | 耐久有効時 `mainDurabilityInfo.updateDurabilityAmountState` で状態を更新する。 |
| `initializeDurabilityValue(float newAmount, int currentObjectIndex)` | 耐久設定が有効なら `mainDurabilityInfo` の耐久値を `newAmount` で初期化し、インベントリのオブジェクト番号も設定する。 |
| `setInventoryObjectIndex(int currentObjectIndex)` | 耐久設定が有効なとき `mainDurabilityInfo` にインベントリのオブジェクト番号を設定する。 |
| `getDurabilityAmount()` | 耐久設定が有効なら現在の耐久値を返し、そうでなければ-1を返す。 |
| `repairObjectFully()` | 耐久設定が有効なとき `mainDurabilityInfo.repairObjectFully` で耐久を全回復する。 |
| `breakFullDurabilityOnCurrentWeapon()` | 耐久設定とマネージャ側チェックが有効なとき耐久を0にし、`checkEventOnEmptyDurability` を呼ぶ。 |
| `setDurabilityUsedOnAttackValue(float newValue)` | `durabilityUsedOnAttack` を `newValue` にするだけ。 |
| `setObjectNameFromEditor(string newName)` | 耐久設定が有効なとき `mainDurabilityInfo` のオブジェクト名を設定する。 |
| `setDurabilityAmountFromEditor(float newValue)` | 耐久設定が有効なとき `mainDurabilityInfo` の現在耐久値を設定する。 |
| `setMaxDurabilityAmountFromEditor(float newValue)` | 耐久設定が有効なとき `mainDurabilityInfo` の最大耐久値を設定する。 |
| `setCanGrabObjectsCarryingWeaponsState(bool state)` | `weaponsManager` 側の武器所持中にオブジェクトを掴めるかという設定を `state` にする。 |
| `setOriginalCanGrabObjectsCarryingWeaponsState()` | `weaponsManager` 側で武器所持中のオブジェクト掴み可否を元の設定に戻す。 |
| `setDurabilityUsedOnAttackValueFromEditor(float newValue)` | 攻撃時の耐久消費量を設定したうえで `updateComponent` を呼ぶ。 |
| `setMagazineSizeFromEditor(float newAmount)` | `newAmount` をintに変換して `clipSize` に設定し、`updateComponent` を呼ぶ。 |
| `setRemainAmmoAmountFromEditor(int newRemainAmmoAmount)` | `weaponSettings.remainAmmo` を設定して `updateComponent` を呼ぶ。 |
| `setInfiniteAmmoValueFromEditor(bool state)` | 無限弾薬設定を行ったうえで `updateComponent` を呼ぶ。 |
| `setFireRateFromEditor(float newFireRate)` | 発射レートを設定したうえで `updateComponent` を呼ぶ。 |
| `setProjectileDamageFromEditor(float newDamage)` | 弾威力を設定したうえで `updateComponent` を呼ぶ。 |
| `setCharacter(GameObject pController, GameObject pCamera)` | プレイヤーとカメラのGameObject参照を設定し、`updateComponent` を呼ぶ。 |
| `setWeaponParent(Transform parent, Animator animatorToUse)` | `weaponSettings.weaponParent` を設定し、ボーンやマウントポイントの解決後に `updateComponent` を呼ぶ。 |
| `updateWeaponParentInRuntime(Transform parent, Animator mainAnimtor)` | `setWeaponParent` 後に実行中なら実際に親を付け替え、IKの武器位置をリセットする。 |
| `getWeaponComponents()` | 親や `weaponsManager` から各コンポーネント参照を取得して保持し、`updateComponent` を呼ぶ。 |
| `getImpactListInfo()` | `decalManager` の `impactListInfo` 名を `impactDecalList` に複製し `updateComponent` を呼ぶ。 |
| `setWeaponSystemAmmoName(string newWeaponAmmoName)` | `weaponSettings.ammoName` を設定して `updateComponent` を呼ぶ。 |
| `setWeaponSystemName(string newName)` | `weaponSettings.Name` とIKオブジェクト名を変更し `updateComponent` を呼ぶ。 |
| `renameWeaponAmmo(string currentAmmoName, string newAmmoName)` | `ammoName` が `currentAmmoName` と一致する場合のみ、`currentAmmoName` を再代入して `updateComponent` を呼ぶ。 |
| `updateComponent()` | `GKC_Utils.updateComponent` と `updateDirtyScene` を呼び、このコンポーネントの変更をシーンへ反映させる。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnSetRightWeapon` | `UnityEvent` | – |
| `eventOnSetLeftWeapon` | `UnityEvent` | – |
| `eventOnSetSingleWeapon` | `UnityEvent` | – |
