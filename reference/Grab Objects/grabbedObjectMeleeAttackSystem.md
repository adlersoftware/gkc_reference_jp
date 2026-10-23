# grabbedObjectMeleeAttackSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Grab Objects/grabbedObjectMeleeAttackSystem.cs:8`

**概要**: プレイヤーが把持した近接武器の攻撃・ガード・シールド・投擲・切断を統括するコンポーネント。`grabbedWeaponInfo`の設定に従い、攻撃コルーチン、ダメージトリガー、移動設定、各種イベントを実行する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grabbed Object Melee Attack Enabled | `grabbedObjectMeleeAttackEnabled` | `bool` | true | 掴んだ武器での近接攻撃システム全体を有効にする。 |
| Can Grab Melee Objects Enabled | `canGrabMeleeObjectsEnabled` | `bool` | true | 近接武器として使えるオブジェクトを掴めるようにする。 |
| General Attack Damage Multiplier | `generalAttackDamageMultiplier` | `float` | 1 | 全攻撃のダメージ値に掛ける倍率。 |
| Player On Ground To Activate Attack | `playerOnGroundToActivateAttack` | `bool` | true | ONで地上にいるときだけ攻撃できるようにする。 |
| Disable Grab Objects Input When Carrying Melee Weapon | `disableGrabObjectsInputWhenCarryingMeleeWeapon` | `bool` | – | 武器を所持している間はオブジェクトを掴む入力を止める。 |
| Use Throw Return Melee Weapon System Enabled | `useThrowReturnMeleeWeaponSystemEnabled` | `bool` | – | 武器の投擲と手元への返却機能を有効にする。 |
| Place Trigger In Front Of Character On All Attacks | `placeTriggerInFrontOfCharacterOnAllAttacks` | `bool` | – | 全攻撃でダメージ判定をキャラクターの前方に配置する。 |
| Draw Melee Weapon If Attack Input Pressed Enabled | `drawMeleeWeaponIfAttackInputPressedEnabled` | `bool` | – | 攻撃入力時に武器を抜く。未所持なら何もしない。 |
| Use Quick Draw If Attack Input Pressed | `useQuickDrawIfAttackInputPressed` | `bool` | – | 攻撃入力で抜く際に抜刀アニメーションを省略する。 / 表示条件: `drawMeleeWeaponIfAttackInputPressedEnabled` がオンのとき |
| Min Wait Time To Use Single Attack Type | `minWaitTimeToUseSingleAttackType` | `float` | 0.4f | 同種の攻撃が1つだけのときの再使用待ち時間（秒）。 |
| Use Attack Input Stack | `useAttackInputStack` | `bool` | – | 攻撃入力を予約して順番に実行できるようにする。 |
| Max Amount Of Attack Input Stack | `maxAmountOfAttackInputStack` | `int` | – | 予約として受け付ける攻撃入力の最大数。 / 表示条件: `useAttackInputStack` がオンのとき |
| Use Attack Types | `useAttackTypes` | `bool` | – | 武器ごとに攻撃タイプを分けて入力に対応させる。 |

### Surface Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Surface Info Enabled | `checkSurfaceInfoEnabled` | `bool` | true | 攻撃命中時に表面情報を判定して効果を出す。 |
| Surface Info On Melee Attack Name For Not Found | `surfaceInfoOnMeleeAttackNameForNotFound` | `string` | "Regular" | 表面情報が見つからない場合に使う名前。 |
| Surface Info On Melee Attack Name For Swing On Air | `surfaceInfoOnMeleeAttackNameForSwingOnAir` | `string` | "Swing On Air" | 空振り時に使う表面情報の名前。 |

### Damage Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Layer To Detect Surfaces | `useCustomLayerToDetectSurfaces` | `bool` | – | 表面判定に使うレイヤーを独自に指定する。 |
| Custom Layer To Detect Surfaces | `customLayerToDetectSurfaces` | `LayerMask` | – | 表面判定に使うカスタムレイヤーマスク。 |
| Use Custom Ignore Tags | `useCustomIgnoreTags` | `bool` | – | 表面判定から除外するタグを独自に指定する。 |
| Check Surfaces With Capsule Raycast Enabled | `checkSurfacesWithCapsuleRaycastEnabled` | `bool` | true | ダメージ判定時にカプセルレイキャストで表面を探す。 |
| Ignore Get Health From Damaging Objects | `ignoreGetHealthFromDamagingObjects` | `bool` | true | 与ダメージに応じた体力回復（武器設定）を無視する。 |
| Ignore Get Health From Damaging Objects On Weapon Info | `ignoreGetHealthFromDamagingObjectsOnWeaponInfo` | `bool` | true | 攻撃情報側の体力回復設定を無視する。 |
| Ignore Cut Mode On Melee Weapon Attack | `ignoreCutModeOnMeleeWeaponAttack` | `bool` | true | 攻撃時のカット（切断）モード発動を無効にする。 |
| Check Trigger Surfaces On Melee Attacks | `checkTriggerSurfacesOnMeleeAttacks` | `bool` | true | トリガーコライダーも表面判定の対象に含める。 |

### Block Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Block Mode Enabled | `blockModeEnabled` | `bool` | true | ガード（ブロック）機能を有効にする。 |
| General Block Protection Multiplier | `generalBlockProtectionMultiplier` | `float` | 1 | ガード時のダメージ軽減量に掛ける倍率。 |
| Cancel Block Reaction State Name | `cancelBlockReactionStateName` | `string` | "Disable Has Exit Time State" | ガード反応を打ち切るAnimatorのbool名。 |
| Ignore Deflect Projectiles On Attack On All Weapons | `ignoreDeflectProjectilesOnAttackOnAllWeapons` | `bool` | – | 全武器で攻撃時の弾き返しを無効にする。 |
| Ignore Deflect Projectiles On Block On All Weapons | `ignoreDeflectProjectilesOnBlockOnAllWeapons` | `bool` | – | 全武器でガード時の弾き返しを無効にする。 |

### Shield Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shield Can Be Used Without Melee Weapon | `shieldCanBeUsedWithoutMeleeWeapon` | `bool` | – | 近接武器がなくてもシールドを使えるようにする。 |
| Right Hand Mount Point | `rightHandMountPoint` | `Transform` | – | 右手の装着位置を表す参照Transform。 |
| Left Hand Mount Point | `leftHandMountPoint` | `Transform` | – | 左手の装着位置を表す参照Transform。 |
| Shield Right Hand Mount Point | `shieldRightHandMountPoint` | `Transform` | – | シールドを構える右手の装着位置。 |
| Shield Left Hand Mount Point | `shieldLeftHandMountPoint` | `Transform` | – | シールドを構える左手の装着位置。 |
| Shield Back Mount Point | `shieldBackMountPoint` | `Transform` | – | シールドを背中にしまう位置の参照。 |
| Event To Activate Melee Mode When Using Shield Without Melee Weapon | `eventToActivateMeleeModeWhenUsingShieldWithoutMeleeWeapon` | `UnityEvent` | – | 武器なしでシールドを使う際に呼ぶイベント。 |

### Block Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Update Character Surface On Block On | `eventToUpdateCharacterSurfaceOnBlockOn` | `UnityEvent` | – | ガード開始時にキャラクター表面を更新するイベント。 |
| Event To Update Character Surface On Block Off | `eventToUpdateCharacterSurfaceOnBlockOff` | `UnityEvent` | – | ガード終了時にキャラクター表面を更新するイベント。 |

### Stamina Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Stamina On Attack Enabled | `useStaminaOnAttackEnabled` | `bool` | true | 攻撃時にスタミナを消費させる。 |
| Attack Stamina State Name | `attackStaminaStateName` | `string` | "Melee Attack With Grabbed Object" | 攻撃で消費するスタミナの状態名。 |
| General Stamina Use Multiplier | `generalStaminaUseMultiplier` | `float` | 1 | 攻撃のスタミナ消費量に掛ける倍率。 |

### Cutting Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Cutting Mode Enabled | `cuttingModeEnabled` | `bool` | true | 武器のカット（切断）モードを有効にする。 |
| Event On Cutting Mode Start | `eventOnCuttingModeStart` | `UnityEvent` | – | カットモード開始時に呼び出すイベント。 |
| Event On Cutting Mode End | `eventOnCuttingModeEnd` | `UnityEvent` | – | カットモード終了時に呼び出すイベント。 |

### Match Target Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Match Target System On Attack | `useMatchTargetSystemOnAttack` | `bool` | – | 攻撃時にターゲット位置へ合わせる処理を使う。 |
| Ignore Attack Setting To Match Target | `ignoreAttackSettingToMatchTarget` | `bool` | – | 攻撃ごとの設定を無視して常に位置合わせする。 |
| Main Match Player To Target System | `mainMatchPlayerToTargetSystem` | `matchPlayerToTargetSystem` | – | 攻撃時の位置合わせを行うシステムの参照。 |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Melee Combat Axes Input Name | `mainMeleeCombatAxesInputName` | `string` | "Grab Objects" | ブロック入力の判定に使うアクションカテゴリ名。 |
| Main Melee Combat Block Input Name | `mainMeleeCombatBlockInputName` | `string` | "Block Attack" | ブロック入力の判定に使うボタンアクション名。 |
| Ignore Use Draw Keep Weapon Animation | `ignoreUseDrawKeepWeaponAnimation` | `bool` | – | 武器の抜刀・納刀アニメーションを無視する。 |
| Weapons Can Be Stolen From Character | `weaponsCanBeStolenFromCharacter` | `bool` | true | 所持武器を敵に奪われることを許可する。 |

### Weapon Durability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Durability On Attack Enabled | `checkDurabilityOnAttackEnabled` | `bool` | – | 攻撃時に武器の耐久度を減らす。 |
| Check Durability On Block Enabled | `checkDurabilityOnBlockEnabled` | `bool` | – | ガード時に武器の耐久度を減らす。 |
| General Attack Durability Multiplier | `generalAttackDurabilityMultiplier` | `float` | 1 | 攻撃時の耐久度消費に掛ける倍率。 |
| General Block Durability Multiplier | `generalBlockDurabilityMultiplier` | `float` | 1 | ガード時の耐久度消費に掛ける倍率。 |
| Use Event On Durability Empty On Melee Weapon | `useEventOnDurabilityEmptyOnMeleeWeapon` | `bool` | – | 武器の耐久度が尽きた時にイベントを呼ぶ。 |
| Event On Durability Empty On Melee Weapon | `eventOnDurabilityEmptyOnMeleeWeapon` | `UnityEvent` | – | 武器の耐久度が尽きた時に実行するイベント。 / 表示条件: `useEventOnDurabilityEmptyOnMeleeWeapon` がオンのとき |
| Use Event On Durability Empty On Block | `useEventOnDurabilityEmptyOnBlock` | `bool` | – | ガードで耐久度が尽きた時にイベントを呼ぶ。 |
| Event On Durability Empty On Block | `eventOnDurabilityEmptyOnBlock` | `UnityEvent` | – | ガードで耐久度が尽きた時に実行するイベント。 / 表示条件: `useEventOnDurabilityEmptyOnBlock` がオンのとき |

### Weapon Extra Action Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Extra Action Icon Texture | `showExtraActionIconTexture` | `bool` | – | 武器の追加アクションのアイコンをUIに表示する。 |
| Extra Action Icon Game Object | `extraActionIconGameObject` | `GameObject` | – | 追加アクションのアイコンを表示するUIオブジェクト。 |
| Extra Action Raw Image | `extraActionRawImage` | `RawImage` | – | 追加アクションのアイコンを描画する`RawImage`。 |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | 攻撃処理のログをコンソールに出力する。 |
| Show Debug Draw | `showDebugDraw` | `bool` | – | 攻撃判定のレイキャストをシーンビューに描画する。 |
| Grabbed Object Melee Attack Active | `grabbedObjectMeleeAttackActive` | `bool` | – | 近接攻撃システムが有効かを示す状態フラグ。 |
| Carrying Object | `carryingObject` | `bool` | – | 現在オブジェクトを掴んでいるかを示す状態。 |
| Attack In Process | `attackInProcess` | `bool` | – | 攻撃モーションの実行中かを示す状態。 |
| Current Attack Index | `currentAttackIndex` | `int` | – | 現在再生している攻撃のインデックス。 |
| Block Active | `blockActive` | `bool` | – | 現在ガード中かを示すデバッグ用の状態フラグ。 |
| Block Active Previously | `blockActivePreviously` | `bool` | – | 直前のフレームでガード中だったかを示す状態。 |
| Reduced Block Damage Protection Active | `reducedBlockDamageProtectionActive` | `bool` | – | 軽減後のガード耐性値を使用中かを示す状態。 |
| Can Cancel Block To Start Attack Active | `canCancelBlockToStartAttackActive` | `bool` | – | ガードを中断して攻撃に移れる状態かを示す。 |
| Block Input Paused | `blockInputPaused` | `bool` | – | ガード入力が一時停止中かを示す状態。 |
| Shield Active | `shieldActive` | `bool` | – | シールドを構えているかを示す状態。 |
| Carrying Shield | `carryingShield` | `bool` | – | シールドを所持しているかを示す状態。 |
| Current Shield Name | `currentShieldName` | `string` | – | 現在使用しているシールドの名前。 |
| Current Shield Game Object | `currentShieldGameObject` | `GameObject` | – | 現在使用中のシールドのGameObject参照。 |
| Current Shield Hand Mount Point Transform Reference | `currentShieldHandMountPointTransformReference` | `Transform` | – | 構えたシールドの手元位置を表す参照Transform。 |
| Current Shield Back Mount Point Transform Reference | `currentShieldBackMountPointTransformReference` | `Transform` | – | 納めたシールドの背中位置を表す参照Transform。 |
| Current Hit Combat | `currentHitCombat` | `hitCombat` | – | 攻撃判定に使う`hitCombat`の参照。 |
| Dual Wield Hit Combat | `dualWieldHitCombat` | `hitCombat` | – | 二刀流の2本目の攻撃判定に使う`hitCombat`。 |
| Main Dual Wield Melee Weapon Object System | `mainDualWieldMeleeWeaponObjectSystem` | `dualWieldMeleeWeaponObjectSystem` | – | 二刀流の武器動作を制御するシステムの参照。 |
| Object Thrown | `objectThrown` | `bool` | – | 武器を投擲中かを示す状態フラグ。 |
| Cutting Mode Active | `cuttingModeActive` | `bool` | – | カットモードが実行中かを示す状態。 |
| Attack Input Paused For Stamina | `attackInputPausedForStamina` | `bool` | – | スタミナ不足で攻撃入力が止まっている状態。 |
| Damage Trigger In Process | `damageTriggerInProcess` | `bool` | – | ダメージ判定の有効化処理中かを示す状態。 |
| Melee Attack Input Paused | `meleeAttackInputPaused` | `bool` | – | 近接攻撃の入力が一時停止中かを示す状態。 |
| Is Dual Wield Weapon | `isDualWieldWeapon` | `bool` | – | 現在の武器が二刀流かを示す状態フラグ。 |
| Throw Weapon Action Paused | `throwWeaponActionPaused` | `bool` | – | 武器投擲アクションが停止中かを示す状態。 |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Attack | `useEventsOnAttack` | `bool` | – | 攻撃開始・終了時にイベントを呼ぶ。 |
| Event On Attack Start | `eventOnAttackStart` | `UnityEvent` | – | 攻撃開始時に実行するイベント。 |
| Event On Attack End | `eventOnAttackEnd` | `UnityEvent` | – | 攻撃終了時に実行するイベント。 |
| Use Events On Block Damage | `useEventsOnBlockDamage` | `bool` | – | ガード開始・解除時にイベントを呼ぶ。 |
| Event On Block Activate | `eventOnBlockActivate` | `UnityEvent` | – | ガード開始時に実行するイベント。 |
| Event On Block Deactivate | `eventOnBlockDeactivate` | `UnityEvent` | – | ガード解除時に実行するイベント。 |
| Use Events On Grab Drop Object | `useEventsOnGrabDropObject` | `bool` | – | オブジェクトの掴み・解放時にイベントを呼ぶ。 |
| Event On Grab Object | `eventOnGrabObject` | `UnityEvent` | – | オブジェクトを掴んだ時に実行するイベント。 |
| Event On Drop Object | `eventOnDropObject` | `UnityEvent` | – | オブジェクトを離した時に実行するイベント。 |
| Use Events On Attack Cant Be Blocked | `useEventsOnAttackCantBeBlocked` | `bool` | – | ガード不可の攻撃時にイベントを呼ぶ。 |
| Event On Attack Cant Be Blocked | `eventOnAttackCantBeBlocked` | `UnityEvent` | – | ガード不可の攻撃時に実行するイベント。 |
| Hide Inventory Quick Access Slots When Carrying Melee Weapon | `hideInventoryQuickAccessSlotsWhenCarryingMeleeWeapon` | `bool` | – | 武器所持中にインベントリのクイック枠を隠す。 |
| Event On Hide Inventory Quick Access Slots | `eventOnHideInventoryQuickAccessSlots` | `UnityEvent` | – | クイックアクセス枠を隠す時に呼ぶイベント。 |
| Event On Show Inventory Quick Access Slots | `eventOnShowInventoryQuickAccessSlots` | `UnityEvent` | – | クイックアクセス枠を表示する時に呼ぶイベント。 |
| Use Event To Activate Parry State If Attack In Process | `useEventToActivateParryStateIfAttackInProcess` | `bool` | – | 攻撃中にパリィ状態へ移行するイベントを使う。 |
| Event To Activate Parry State If Attack In Process | `eventToActivateParryStateIfAttackInProcess` | `UnityEvent` | – | 攻撃中に呼び出してパリィ状態にするイベント。 / 表示条件: `useEventToActivateParryStateIfAttackInProcess` がオンのとき |
| Use Event On Attack Blocked Perfectly | `useEventOnAttackBlockedPerfectly` | `bool` | – | パーフェクトガード時にイベントを呼ぶ。 |
| Event On Attack Blocked Perfectly | `eventOnAttackBlockedPerfectly` | `UnityEvent` | – | パーフェクトガード時に実行するイベント。 / 表示条件: `useEventOnAttackBlockedPerfectly` がオンのとき |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Grabbed Object Transform | `currentGrabbedObjectTransform` | `Transform` | – | 現在掴んでいるオブジェクトのTransform参照。 |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | 投射物の返却方向の基準となるカメラTransform。 |
| Hand Position Reference | `handPositionReference` | `Transform` | – | 手の位置を表す参照Transform。 |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | 表面ヒット時の効果音を再生するAudioSource。 |
| Parent To Place Trigger In Front Of Character | `parentToPlaceTriggerInFrontOfCharacter` | `Transform` | – | ダメージ判定を前方へ置く際の親Transform。 |
| Parent To Place Trigger In Front Of Character FBA | `parentToPlaceTriggerInFrontOfCharacterFBA` | `Transform` | – | フルボディアウェアネス時に判定を前方へ置く親。 |
| Main Remote Event System | `mainRemoteEventSystem` | `remoteEventSystem` | – | 武器のリモートイベントを送るための参照。 |
| Player Controller Game Object | `playerControllerGameObject` | `GameObject` | – | プレイヤー本体のGameObject参照。 |
| Main Player Controller | `mainPlayerController` | `playerController` | – | プレイヤー制御コンポーネントの参照。 |
| Main Grab Objects | `mainGrabObjects` | `grabObjects` | – | オブジェクトを掴む処理を行う`grabObjects`の参照。 |
| Main Health | `mainHealth` | `health` | – | プレイヤーの体力を管理する`health`の参照。 |
| Main Slice System | `mainSliceSystem` | `sliceSystem` | – | カットモードで使う`sliceSystem`の参照。 |
| Main Animator | `mainAnimator` | `Animator` | – | 攻撃やガードのアニメーションを制御するAnimator。 |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | ストレイフ切替を通知する`findObjectivesSystem`の参照。 |
| Main Melee Weapons Grabbed Manager | `mainMeleeWeaponsGrabbedManager` | `meleeWeaponsGrabbedManager` | – | 武器を管理する`meleeWeaponsGrabbedManager`の参照。 |
| Player Input | `playerInput` | `playerInputManager` | – | 入力状態を取得する`playerInputManager`の参照。 |
| Main Melee Combat Throw Return Weapon System | `mainMeleeCombatThrowReturnWeaponSystem` | `meleeCombatThrowReturnWeaponSystem` | – | 武器の投擲と返却を処理するシステムの参照。 |
| Main Stamina System | `mainStaminaSystem` | `staminaSystem` | – | 攻撃時のスタミナ消費を扱うシステムの参照。 |
| Main Melee UI System | `mainMeleeUISystem` | `meleeUISystem` | – | 武器名やアイコンを表示する近接武器UIの参照。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `meleeAttackTypes` | `List<string>` | new List<string> () | – |
| `customTagsToIgnoreList` | `List<string>` | new List<string> () | – |
| `grabbedWeaponInfoList` | `List<grabbedWeaponInfo>` | new List<grabbedWeaponInfo> () | – |
| `surfaceInfoOnMeleeAttackList` | `List<surfaceInfoOnMeleeAttack>` | new List<surfaceInfoOnMeleeAttack> () | – |
| `useRightHandMountPointForShieldActive` | `bool` | – | – |
| `meleeAttackTypesAmount` | `List<int>` | new List<int> () | – |
| `extraTriggerMultiplierScaleOnAllMeleeAttacksActive` | `bool` | – | – |
| `extraTriggerMultiplierScaleOnAllMeleeAttacksAmount` | `float` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateSurfacesSoundInfo()` | `surfaceInfoOnMeleeAttackList`の効果音から`AudioElement`を再構築し`mainAudioSource`を設定する。 |
| `stopUpdateCoroutine()` | 攻撃入力スタック監視用の`updateCoroutine`が動いていれば停止する。 |
| `isGrabbedObjectMeleeAttackEnabled()` | `grabbedObjectMeleeAttackEnabled`の値をそのまま返す。 |
| `isCanGrabMeleeObjectsEnabled()` | `canGrabMeleeObjectsEnabled`の値をそのまま返す。 |
| `getRightHandMountPoint()` | 右手用の武器装着位置`rightHandMountPoint`を返す。 |
| `getLeftHandMountPoint()` | 左手用の武器装着位置`leftHandMountPoint`を返す。 |
| `checkGrabbedMeleeWeaponLocalPositionRotationValues()` | カスタム参照設定時、把持武器のローカル位置と回転を設定値または参照`Transform`に合わせる。 |
| `checkKeepMeleeWeaponLocalPositionRotationValues()` | `customReferencePositionToKeepObject`が有効なら、しまう武器のローカル姿勢をその値に合わせる。 |
| `isUseCustomGrabbedWeaponReferencePositionActive()` | 現在武器情報の`useCustomGrabbedWeaponReferencePosition`を返し、無ければ`false`。 |
| `isUseGrabbedWeaponReferenceValuesActive()` | 現在武器情報の`useGrabbedWeaponReferenceValues`を返し、無ければ`false`。 |
| `getGrabbedWeaponReferenceValuesPosition()` | `useGrabbedWeaponReferenceValues`が有効なら把持位置を返し、それ以外は`Vector3.zero`。 |
| `getGrabbedWeaponReferenceValuesEuler()` | `useGrabbedWeaponReferenceValues`が有効なら把持角度を返し、それ以外は`Vector3.zero`。 |
| `isUseReferenceToKeepObjectValuesActive()` | 現在武器情報の`useReferenceToKeepObjectValues`を返し、無ければ`false`。 |
| `getReferenceToKeepObjectValuesPosition()` | `useGrabbedWeaponReferenceValues`が有効ならしまう位置を返す(判定は把持側フラグ)。 |
| `getReferenceToKeepObjectValuesEuler()` | `useGrabbedWeaponReferenceValues`が有効ならしまう角度を返す(判定は把持側フラグ)。 |
| `getCustomGrabbedWeaponReferencePosition()` | `useCustomGrabbedWeaponReferencePosition`が有効なら参照`Transform`を返し、無ければ`null`。 |
| `getCustomReferencePositionToKeepObject()` | `useCustomReferencePositionToKeepObject`が有効なら参照`Transform`を返し、無ければ`null`。 |
| `setNewGrabPhysicalObjectSystem(grabPhysicalObjectSystem newGrabPhysicalObjectSystem)` | `currentGrabPhysicalObjectSystem`を差し替え、投擲返却システムにも同じ参照を渡す。 |
| `setCheckDrawKeepWeaponAnimationPauseState(bool state)` | `checkDrawKeepWeaponAnimationPauseState`を設定するだけ。 |
| `activateStartDrawAnimation()` | 抜刀アニメを開始して武器メッシュを消し、体側メッシュを表示する。 |
| `activateEndDrawAnimation()` | 抜刀完了時に武器メッシュを出して体側を消し、最後の武器姿勢と親を保存する。 |
| `enableOrDisableWeaponMeshActiveState(bool state)` | 武器情報があるとき、現在武器のメッシュ表示状態を切り替える。 |
| `activateStartKeepAnimation()` | しまうアニメを開始し、条件外やポーズ時は保存した武器情報を消す。 |
| `removeDrawKeepWeaponAnimationInfo()` | 最後に使った武器と親の保存情報を`null`に消す。 |
| `placeLastWeaponOnCharacterHand()` | 最後の武器を元の親と姿勢へ戻し、当たり判定を切って`Rigidbody`をキネマティックにする。 |
| `activateEndKeepAnimation()` | 武器を親から外して非アクティブ化し、当たり判定と把持トリガーを戻して保存情報を消す。 |
| `setNewGrabPhysicalObjectMeleeAttackSystem(grabPhysicalObjectMeleeAttackSystem newGrabPhysicalObjectMeleeAttackSystem)` | 新しい近接武器を現在武器として初期化し、当たり判定・移動設定・イベント・UIを一括更新する。 |
| `getLastTimeDrawMeleeWeapon()` | 最後に近接武器を抜いた時刻を返す。 |
| `getMeleeAttackTypesAmount()` | 攻撃タイプごとの攻撃数リストを返す。 |
| `setRemoveWeaponsFromManagerState(bool state)` | `removeWeaponsFromManager`を設定するだけ。 |
| `removeGrabPhysicalObjectMeleeAttackSystem()` | 把持中の近接武器を解除し、コルーチン停止・ガード/切断/シールド解除・イベント発火・UI非表示を行う。 |
| `enableOrDisableMainMeleeUISystem(bool state)` | `mainMeleeUISystem`があれば近接UIの表示を切り替える。 |
| `getGrabbedWeaponInfoByName(string weaponInfoName)` | 名前が一致する武器情報を返し、見つからなければ`null`。 |
| `checkUpdateCustomReferencePositionsToKeepMeshValues(grabPhysicalObjectMeleeAttackSystem newGrabPhysicalObjectMeleeAttackSystem)` | 渡した武器システムに、武器情報のしまうメッシュ参照位置の値を反映する。 |
| `drawOrKeepMeleeWeapon()` | 武器管理が有効なとき、抜刀/しまう入力をマネージャへ委譲する。 |
| `drawOrKeepMeleeWeaponWithoutCheckingInputActive()` | 入力状態を確認せず抜刀/しまうをマネージャへ委譲する。 |
| `drawMeleeWeaponGrabbedCheckingAnimationDelay()` | アニメ遅延を考慮した抜刀処理をマネージャへ委譲する。 |
| `checkToKeepWeapon()` | しまう処理をマネージャへそのまま委譲する。 |
| `checkToKeepWeaponWithoutCheckingInputActive()` | 入力確認なしのしまう処理をマネージャへ委譲する。 |
| `checkIfDropThrownWeaponWhenUsingDevice()` | デバイス使用中に投擲武器を落とす判定をマネージャへ委譲する。 |
| `setAttackInputPausedForStaminaState(bool state)` | スタミナ攻撃使用が有効なときだけ`attackInputPausedForStamina`を設定する。 |
| `setThrowObjectInputPausedForStaminaState(bool state)` | 投擲返却システム有効時、投擲入力のスタミナ停止状態を設定する。 |
| `canActivateAttack()` | 次攻撃までの待ち時間が0または経過していれば`true`を返す。 |
| `resetCurrentAttackByIndex()` | `currentAttackByIndex`を0に戻す。 |
| `activateGrabbedObjectMeleeAttackByIndex()` | 現在インデックスの攻撃タイプで攻撃し、インデックスを次へ進める。 |
| `activateNextAttackIgnoringWaitingTimes()` | 攻撃中に待ち時間を無視して同じ攻撃タイプを再実行する。 |
| `checkResetAttackInputStack()` | 入力スタック使用中かつ有効なら攻撃入力スタックを消去する。 |
| `resetAttackInputStack()` | 攻撃入力スタックのリストと有効・完了フラグを初期化する。 |
| `activateGrabbedObjectMeleeAttack(string attackType)` | 指定攻撃タイプの攻撃を条件判定のうえ開始し、ダメージ設定と攻撃・トリガーコルーチンを起動する。 |
| `resetAttackIndex()` | `currentAttackIndex`と待ち時間を0に戻す。 |
| `setNextAttackIndex()` | ランダム設定なら乱数、そうでなければ加算で攻撃インデックスを進める。 |
| `stopActivateGrabbedObjectMeleeAttackCoroutine()` | 攻撃コルーチン`attackCoroutine`を停止する。 |
| `stopActivateDamageTriggerCoroutine()` | ダメージトリガーのコルーチンを停止する。 |
| `stopActivateDamageDualWieldTriggerCoroutine()` | 二刀流側のダメージトリガーコルーチンを停止する。 |
| `enableOrDisableDualWieldMeleeWeaponObject(bool state)` | 二刀流武器のとき、二刀流オブジェクトの有効状態を切り替える。 |
| `resetActivateDamageTriggerCoroutine()` | ダメージトリガー実行中なら、前回起動から0.05秒後にメインと二刀流のコルーチンを再起動する。 |
| `getCharacterHumanBone(HumanBodyBones boneToFind)` | 指定の`HumanBodyBones`に対応するボーン`Transform`をプレイヤーから取得する。 |
| `getCurrentGrabbedObjectTransform()` | 把持中オブジェクトの`Transform`を返す。 |
| `getCurrentMeleeWeaponTypeName()` | 現在の武器情報の`Name`を返し、無ければ空文字。 |
| `getCurrentMeleeWeaponName()` | 現在の武器オブジェクト名を返し、無ければ空文字。 |
| `canWeaponsBeStolenFromCharacter()` | `weaponsCanBeStolenFromCharacter`を返す。 |
| `setCanWeaponsBeStolenFromCharacter(bool state)` | `weaponsCanBeStolenFromCharacter`を設定するだけ。 |
| `isSecondaryAbilityActiveOnCurrentWeapon()` | 武器情報と武器があるとき、現在武器のセカンダリ能力が有効か返す。 |
| `disableCurrentAttackInProcess()` | 実行中の攻撃を中断して当たり判定を止め、キャンセルイベント発火と投擲中止まで行う。 |
| `checkDurabilityOnAttackOnCurrentWeapon(bool ignoreDurability, float extraDurabilityMultiplier)` | 耐久チェック有効かつ無視しないとき倍率を掛けて武器耐久を減らし、尽きたらイベントを呼ぶ。 |
| `repairObjectFully(string weaponName)` | 指定した武器名のオブジェクトをマネージャ経由で完全修理する。 |
| `checkDurabilityOnBlock()` | ガード時にシールドか武器の耐久を減らし、尽きたらイベントを発火する。 |
| `checkOnAttackBlocked()` | ガード成功時、武器情報の設定値ぶん体力を最大値まで回復する。 |
| `checkOnAttackBlockedPerfectly()` | パリィ成功時に設定値ぶん体力を回復し、`eventOnAttackBlockedPerfectly`を発火する。 |
| `setGetHealthFromPerfectBlocksActiveState(bool state)` | `getHealthFromPerfectBlocksActive`を設定するだけ。 |
| `setHealthAmountFromPerfectBlocksValue(float newValue)` | `healthAmountFromPerfectBlocksValue`を設定するだけ。 |
| `checkIfBlockInputIsCurrentlyInUse()` | ガード入力が押されていなければガード状態を解除する。 |
| `disableBlockStateInProcess()` | ガード中なら前回ガードフラグを消してガードを解除する。 |
| `disableBlockActiveState()` | `inputDeactivateBlock`を呼び出してガードを解除する。 |
| `checkEventsOnBlockDamage(bool state)` | イベント使用時、ガード開始/終了に対応するイベントを発火する。 |
| `checkEventsToUpdateCharacterSurfaceOnBlockStateChange()` | 武器所持時、ガード状態に応じてキャラ表面更新イベントを発火する。 |
| `checkIfBlockActive()` | ガード中ならガード状態を再適用する。 |
| `setBlockActiveState(bool state)` | ガード可否を判定し、移動設定・ダメージ軽減値・リアクションIDを反映してガードとイベントを切り替える。 |
| `updateRegularBlockDamageProtectionValue()` | 通常のガードダメージ軽減値を再適用する。 |
| `updateReducedBlockDamageProtectionValue()` | 軽減版のガードダメージ軽減値を再適用する。 |
| `setBlockDamageProtectionValue(bool state)` | 軽減ガードの有効状態を設定し、ガード中なら体力側の軽減値を更新する。 |
| `disableBlockInputPausedStateWithDuration(float pauseDuration)` | 指定秒数だけガード入力を止めるコルーチンを開始する。 |
| `setBlockInputPausedState(bool state)` | `blockInputPaused`を設定するだけ。 |
| `setCanCancelBlockToStartAttackActiveState(bool state)` | `canCancelBlockToStartAttackActive`を設定するだけ。 |
| `setShieldProtectionValues(float blockDamageProtectionAmount, float reducedBlockDamageProtectionAmount, bool useMaxBlockRangeAngleValue, float maxBlockRangeAngleAmount)` | シールド用のガード軽減値・軽減版・最大角度の使用可否と角度を保存する。 |
| `setShieldActiveState(bool state)` | シールド有効状態を設定し、武器なし時の空武器装備やメッシュ表示・親設定まで更新する。 |
| `getEmptyWeaponToUseOnlyShield()` | シールド専用の空武器名を返し、無ければ空文字。 |
| `setShieldActiveFieldValueDirectly(bool state)` | `shieldActive`を直接設定しアニメータ状態を更新する。 |
| `drawOrSheatheShield(bool state)` | シールド所持時、表示と親を切り替え、ガード中なら解除する。 |
| `setUseRightHandMountPointForShieldActiveState(bool state)` | `useRightHandMountPointForShieldActive`を設定するだけ。 |
| `setShieldParentState(bool state)` | シールドを手または背中のマウントへ親子付けし、ローカル姿勢をコピーする。 |
| `checkIfCarryingShieldActive()` | シールド所持状態を`setShieldActiveState`へ渡して反映する。 |
| `setShieldInfo(string newShieldName, GameObject newShieldGameObject, Transform newShieldHandMountPointTransformReference, Transform newShieldBackMountPointTransformReference, bool shieldCarriedOnRightArm, bool state)` | シールド名・オブジェクト・マウント参照・所持状態を保存し、非所持時は空武器を無効化する。 |
| `checkIfCanUseMeleeWeaponPrefabByName(string weaponName)` | 指定名の近接武器プレハブが使用可能かマネージャへ問い合わせる。 |
| `getCurrentNumberOfWeaponsAvailable()` | 利用可能な武器数をマネージャから取得する。 |
| `dropMeleeWeaponsExternallyWithoutResult()` | 武器所持時のみ、結果を返さず把持オブジェクトを落とす。 |
| `dropMeleeWeaponsExternallyWithoutResultAndDestroyIt()` | 攻撃を中断して武器を落とし、その武器オブジェクトを破棄する。 |
| `dropMeleeWeaponsExternally()` | 武器所持時のみ落として`true`、それ以外は`false`を返す。 |
| `drawNextWeaponAvailable()` | 次に利用可能な武器を抜くようマネージャへ委譲する。 |
| `drawRandomWeaponFromPrefabList(string previousWeaponName)` | 前回武器名を渡し、プレハブ一覧からランダムに武器を抜かせる。 |
| `resetStartWithWeaponCheckedOnCharacterSpawn()` | スポーン時の初期武器チェック済み状態をマネージャ経由で戻す。 |
| `resumeState()` | 攻撃終了状態へ戻し、当たり判定の姿勢・スケール・装甲・入力停止・イベントを復元する。 |
| `checkEventsOnAttack(bool state)` | イベント使用時、攻撃開始/終了イベントを発火する。 |
| `checkEventWhenKeepingOrDrawingMeleeWeapon(bool state)` | 武器と武器情報のしまう/抜くイベントを状態に応じて発火する。 |
| `setRemoteEventOnCurrentMeleeWeapon(string remoteEventName)` | 所持中の武器の`remoteEventSystem`で指定イベントを呼ぶ。 |
| `setRemoteEventsOnCurrentMeleeWeapon(List<string> remoteEventNameList, GameObject weaponObject)` | 指定オブジェクトの`remoteEventSystem`で複数イベントを順に呼ぶ。 |
| `setDamageTypeAndReactionInfo(string newBuffObjectName)` | 武器へダメージタイプとリアクション情報を設定し、成功可否を返す。 |
| `activateReturnProjectilesOnContact()` | 武器に弾き返し情報を渡し、弾き返しイベントを発火する。 |
| `setNewMeleeWeaponAttackInfoTemplate(string templateName)` | 攻撃中でなければ名前一致の攻撃情報テンプレートを適用する。 |
| `setNextMeleeWeaponAttackInfoTemplate()` | 攻撃情報テンプレートのインデックスを次へ進めて適用する。 |
| `inputSetNextMeleeWeaponAttackInfoTemplate()` | 次の攻撃情報テンプレートへ切り替える入力処理。 |
| `checkGrabbedWeaponInfoStateAtStart(string weaponInfoName, bool checkIfWeaponThrown)` | 武器情報を名前で取得し、投擲中判定を除いて移動設定・イベント・リモートイベントを適用する。 |
| `checkGrabbedWeaponInfoStateAtEnd()` | 武器情報を解除し、ストレイフ・各ID・スプリントを戻して破棄イベントを発火する。 |
| `checkLookAtTargetActiveState()` | ターゲット注視状態に応じてストレイフを切り替え、シールドガード状態を更新する。 |
| `checkLookAtTargetDeactivateState()` | ターゲット注視解除時にストレイフを止め、シールドガード状態を更新する。 |
| `setStrafeModeOnAISystemState(bool state)` | AI制御システムがあればストレイフモード状態を設定する。 |
| `setStrafeModeState(bool state, int strafeID)` | ストレイフの有効状態と`strafeID`をプレイヤーに設定する。 |
| `setCurrentCrouchIDValue(int crouchID)` | プレイヤーの現在のしゃがみIDを設定する。 |
| `isStrafeModeActive()` | プレイヤーのストレイフモードが有効か返す。 |
| `getCurrentStrafeID()` | プレイヤーの現在のストレイフIDを返す。 |
| `getCurrentCrouchID()` | プレイヤーの現在のしゃがみIDを返す。 |
| `isActionActive()` | プレイヤーがアクション実行中か返す。 |
| `setObjectThrownState(bool state)` | `objectThrown`を設定するだけ。 |
| `setGrabbedObjectClonnedColliderEnabledState(bool state)` | 把持オブジェクトの複製コライダーの有効状態をマネージャ経由で設定する。 |
| `setDamageDetectedOnDualWieldTriggerById(int attackID)` | 二刀流用フラグを立てて被弾検出処理を呼び、フラグを戻す。 |
| `setDamageDetectedOnTriggerById(int attackID)` | 攻撃IDに対応する被弾イベントとリモートイベントを発火し、表面判定を実行する。 |
| `setNoDamageDetectedOnDualWieldTriggerById(GameObject objectDeteted)` | 二刀流フラグを立てて`checkSurfaceFoundOnAttack(true)`を呼ぶ。引数は未使用。 |
| `setNoDamageDetectedOnTriggerById(GameObject objectDetected)` | `checkSurfaceFoundOnAttack(true)`を呼ぶだけで引数は未使用。 |
| `setPressDownState()` | 武器情報の押し込みイベントを発火する。 |
| `setPressUpState()` | 武器情報の離しイベントを発火する。 |
| `inputSetPressDownState()` | 各種入力条件を満たすとき押し込みイベントを発火する。 |
| `inputSetPressUpState()` | 各種入力条件を満たすとき離しイベントを発火する。 |
| `inputActivateBlock()` | 条件確認後、攻撃中なら再開予約のみ、それ以外はガードを開始する。 |
| `inputDeactivateBlock()` | 条件確認後、ガード中ならガード状態を解除する。 |
| `inputSetNextExtraActionOnMeleeWeapon()` | 現在武器の追加アクションを次へ切り替え、アイコン表示を更新する。 |
| `enableExtraActionByName(string actionName)` | 指定名の追加アクションを有効化する。 |
| `disableExtraActionByName(string actionName)` | 指定名の追加アクションを無効化する。 |
| `enableOrDisableExtraActionByName(string actionName, bool state)` | 武器所持かつ追加アクション使用時に、指定名の有効状態を切り替える。 |
| `inputActivateCurrentExtraActionOnMeleeWeapon()` | 投擲アクション停止フラグが立っているときのみ、条件確認のうえ現在の追加アクションを実行する。 |
| `setThrowWeaponActionPausedState(bool state)` | 投擲アクション停止フラグを設定し、投擲システムにも伝える。 |
| `inputThrowOrReturnObject()` | 投擲/返却入力を投擲システムへ委譲する。 |
| `inputPressDownThrowObject()` | 投擲ボタン押下入力を投擲システムへ委譲する。 |
| `inputPressUpThrowObject()` | 投擲ボタン離し入力を投擲システムへ委譲する。 |
| `inputEnableOrDisableCuttingMode()` | ガード/攻撃中などを除き、切断モード切替可否を確認して切断モードを反転する。 |
| `inputActivateTeleport()` | テレポート入力を投擲システムへ委譲する。 |
| `enableOrDisableCuttingMode(bool state)` | 切断モードを切り替え、開始/終了イベントとシールドの親を更新する。 |
| `checkObjectsDetectedOnCuttingMode()` | 切断モード中に検出物ごとに表面情報と耐久を処理する。 |
| `checkEventOnGrabDropObject(bool state)` | クイックアクセス枠の表示切替と把持/破棄イベントを実行する。 |
| `checkEventsIfObjectGrabbed()` | 武器所持中なら把持イベントを発火する。 |
| `checKEventsHideShowInventoryQuickAccessSlots(bool state)` | 設定有効時、武器所持に応じてクイックアクセス枠の表示イベントを発火する。 |
| `setThrowObjectEnabledState(bool state)` | 投擲返却システム有効時、投擲の有効状態を設定する。 |
| `setReturnObjectEnabledState(bool state)` | 投擲返却システム有効時、返却の有効状態を設定する。 |
| `setApplyDamageOnSurfaceDetectedOnReturnEnabledState(bool state)` | 投擲返却システム有効時、返却時の表面ダメージ適用可否を設定する。 |
| `setApplyDamageOnObjectReturnPathEnabledState(bool state)` | 投擲返却システム有効時、返却経路のダメージ適用可否を設定する。 |
| `setGeneralDamageMultiplierOnObjectReturnValue(float newValue)` | 投擲返却システム有効時、返却時のダメージ倍率を設定する。 |
| `setGeneralDamageMultiplierOnReturnPathValue(float newValue)` | 投擲返却システム有効時、返却経路のダメージ倍率を設定する。 |
| `setGeneralDamageOnSurfaceDetectedOnThrowValue(float newValue)` | 投擲返却システム有効時、投擲時の表面ダメージ値を設定する。 |
| `setCuttingModeEnabledState(bool state)` | `cuttingModeEnabled`を設定するだけ。 |
| `setBlockModeEnabledState(bool state)` | `blockModeEnabled`を設定するだけ。 |
| `setGeneralBlockProtectionMultiplierValue(float newValue)` | `generalBlockProtectionMultiplier`を設定するだけ。 |
| `setUseStaminaOnAttackEnabledState(bool state)` | `useStaminaOnAttackEnabled`を設定するだけ。 |
| `setGeneralStaminaUseMultiplierValue(float newValue)` | `generalStaminaUseMultiplier`を設定するだけ。 |
| `getGeneralStaminaUseMultiplier()` | `generalStaminaUseMultiplier`を返す。 |
| `setGeneralAttackDamageMultiplierValue(float newValue)` | `generalAttackDamageMultiplier`を設定するだけ。 |
| `generalAttackDamageMultiplierIncreaseStat(float extraValue)` | `generalAttackDamageMultiplier`に値を加算する。 |
| `initializeGeneralAttackDamageMultiplierStatAmount(float newValue)` | `generalAttackDamageMultiplier`を初期値で上書きする。 |
| `getGeneralAttackDamageMultiplierValue()` | `generalAttackDamageMultiplier`を返す。 |
| `isObjectThrownTravellingToTarget()` | 投擲返却システム有効時、投げた武器が目標へ飛翔中か返す。 |
| `isAttackInProcess()` | `attackInProcess`を返す。 |
| `isCuttingModeActive()` | `cuttingModeActive`を返す。 |
| `checkIfActivateParryStateIfAttackInProcess()` | 武器所持かつ攻撃中か完了後0.5秒以内ならパリィ状態イベントを発火する。 |
| `isBlockActive()` | `blockActive`を返す。 |
| `canUseWeaponsInput()` | プレイヤーが多忙か近接格闘攻撃中なら武器入力不可として`false`を返す。 |
| `playerIsBusy()` | デバイス使用中やメニュー/サブメニュー表示中は`true`を返す(ターン制は除く)。 |
| `getLastTimeObjectReturn()` | 投擲返却システム有効時、最後に返却した時刻を返す。 |
| `getLastTimeObjectThrown()` | 投擲返却システム有効時、最後に投擲した時刻を返す。 |
| `isCurrentWeaponThrown()` | `objectThrown`を返す。 |
| `setMeleeAttackInputPausedState(bool state)` | `meleeAttackInputPaused`を設定するだけ。 |
| `disableMeleeAttackInputPausedStateWithDuration(float pauseDuration)` | 指定秒数だけ近接攻撃入力を停止するコルーチンを開始する。 |
| `isCarryingObject()` | `carryingObject`を返す。 |
| `checkIfCurrentWeaponignoreUseIKOnHands()` | 武器所持時、現在武器が手のIKを無視する設定か返す。 |
| `isCurrentWeaponIsCarriedOnRightHand()` | 武器所持時、右手で持っているか返す。 |
| `isAimingBowActive()` | `aimingBowActive`を返す。 |
| `setAimBowState(bool state)` | `aimingBowActive`を設定するだけ。 |
| `getCurrentGrabPhysicalObjectMeleeAttackSystem()` | 現在の近接武器システムを返す。 |
| `checkSurfaceFoundOnAttack(bool surfaceLocated)` | 攻撃の表面ヒットを解決し、切断・押し出し・体力回復・表面イベントを処理して表面別効果と耐久へ渡す。 |
| `checkSurfaceFoundOnAttackToProcess(string surfaceName, bool surfaceLocated, Vector3 attackPosition, Vector3 attackNormal, bool ignoreBounceEvent, bool ignoreSoundOnSurface)` | 表面名に一致する設定を探し、効果音・バウンスイベント・パーティクルを再生する。 |
| `setMeleeAttackSoundPausedState(bool state)` | `meleeAttackSoundPaused`を設定するだけ。 |
| `addEventOnDamageInfoList(string weaponTypeName)` | 指定武器情報に、IDが現在数となる被弾イベント要素を追加する。 |
| `setIgnoreCutModeOnMeleeWeaponAttackState(bool state)` | `ignoreCutModeOnMeleeWeaponAttack`を設定するだけ。 |
| `setCheckDurabilityOnAttackEnabledState(bool state)` | `checkDurabilityOnAttackEnabled`を設定するだけ。 |
| `setCheckDurabilityOnBlockEnabledState(bool state)` | `checkDurabilityOnBlockEnabled`を設定するだけ。 |
| `setGeneralAttackDurabilityMultiplier(float newValue)` | `generalAttackDurabilityMultiplier`を設定するだけ。 |
| `setGeneralBlockDurabilityMultiplier(float newValue)` | `generalBlockDurabilityMultiplier`を設定するだけ。 |
| `setIgnoreUseDrawKeepWeaponAnimationState(bool state)` | `ignoreUseDrawKeepWeaponAnimation`を設定するだけ。 |
| `setOriginalIgnoreUseDrawKeepWeaponAnimationState()` | `Start`で保存した元の抜刀/しまうアニメ無視設定に戻す。 |
| `setUseMatchTargetSystemOnAttackState(bool state)` | `useMatchTargetSystemOnAttack`を設定するだけ。 |
| `setOriginaloriginalUseMatchTargetSystemOnAttackState()` | `Start`で保存した元のマッチターゲット設定に戻す。 |
| `enableOrDisableUseAttackInputStack(bool state)` | `useAttackInputStack`を設定するだけ。 |
| `setPlaceTriggerInFrontOfCharacterOnAllAttacksState(bool state)` | `placeTriggerInFrontOfCharacterOnAllAttacks`を設定するだけ。 |
| `setExtraTriggerMultiplierScaleOnAllMeleeAttacksActiveState(bool state, float value)` | 全攻撃のトリガー拡大の有効状態と倍率値を設定する。 |
| `setCheckDurabilityOnAttackEnabledStateFromEditor(bool state)` | エディタ用に攻撃耐久チェック設定を反映し、コンポーネントを更新する。 |
| `setCheckDurabilityOnBlockEnabledStateFromEditor(bool state)` | エディタ用にガード耐久チェック設定を反映し、コンポーネントを更新する。 |
| `setGeneralAttackDurabilityMultiplierFromEditor(float newValue)` | エディタ用に攻撃耐久倍率を反映し、コンポーネントを更新する。 |
| `setGeneralBlockDurabilityMultiplierFromEditor(float newValue)` | エディタ用にガード耐久倍率を反映し、コンポーネントを更新する。 |
| `setCustomIgnoreTagsForCharacterFromEditor()` | プレイヤーのタグを無視タグに設定し、コンポーネントを更新する。 |
| `setUseMatchTargetSystemOnAttackStateFromEditor(bool state)` | エディタ用にマッチターゲット設定を反映し、コンポーネントを更新する。 |
| `setIgnoreCutModeOnMeleeWeaponAttackStateFromEditor(bool state)` | エディタ用に切断モード無視設定を反映し、コンポーネントを更新する。 |
| `setIgnoreUseDrawKeepWeaponAnimationStateFromEditor(bool state)` | エディタ用に抜刀/しまうアニメ無視設定を反映し、コンポーネントを更新する。 |
| `enableOrDisableUseAttackInputStackFromEditor(bool state)` | エディタ用に攻撃入力スタック設定を反映し、コンポーネントを更新する。 |
| `updateGrabbedWeaponReferenceValuesOnAllWeaponInfoList()` | 全武器情報の参照`Transform`のローカル姿勢を位置・角度の値へコピーし、コンポーネントを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCuttingModeStart` | `UnityEvent` | – |
| `eventOnCuttingModeEnd` | `UnityEvent` | – |
| `eventToActivateMeleeModeWhenUsingShieldWithoutMeleeWeapon` | `UnityEvent` | – |
| `eventOnDurabilityEmptyOnMeleeWeapon` | `UnityEvent` | – |
| `eventOnDurabilityEmptyOnBlock` | `UnityEvent` | – |
| `eventOnAttackStart` | `UnityEvent` | – |
| `eventOnAttackEnd` | `UnityEvent` | – |
| `eventOnBlockActivate` | `UnityEvent` | – |
| `eventOnBlockDeactivate` | `UnityEvent` | – |
| `eventToUpdateCharacterSurfaceOnBlockOn` | `UnityEvent` | – |
| `eventToUpdateCharacterSurfaceOnBlockOff` | `UnityEvent` | – |
| `eventOnGrabObject` | `UnityEvent` | – |
| `eventOnDropObject` | `UnityEvent` | – |
| `eventOnAttackCantBeBlocked` | `UnityEvent` | – |
| `eventOnHideInventoryQuickAccessSlots` | `UnityEvent` | – |
| `eventOnShowInventoryQuickAccessSlots` | `UnityEvent` | – |
| `eventToActivateParryStateIfAttackInProcess` | `UnityEvent` | – |
| `eventOnAttackBlockedPerfectly` | `UnityEvent` | – |

## 内部型

- `grabbedWeaponInfo`（class）
- `eventOnDamageInfo`（class）
- `surfaceInfoOnMeleeAttack`（class）
- `rangeAttackInfo`（class）
