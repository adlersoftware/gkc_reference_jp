# bowSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/bowSystem.cs:6`

**概要**: 弓専用コンポーネント。構え、矢の装填、引き絞り、発射、矢種切替、空中弾丸時間を制御する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Regular Bow Movement ID | `regularBowMovementID` | `int` | – | – |
| Loaded Bow Movement ID | `loadedBowMovementID` | `int` | – | – |
| Activate Strafe Only When Aiming Bow | `activateStrafeOnlyWhenAimingBow` | `bool` | – | – |
| Target Rotation | `targetRotation` | `float` | – | – |
| Min Time To Shoot Arrows | `minTimeToShootArrows` | `float` | 2 | – |
| Min Time To Aim Bow | `minTimeToAimBow` | `float` | 1.5f | – |
| Arrows Managed By Inventory | `arrowsManagedByInventory` | `bool` | – | – |
| Activate Bow Collision When Aiming | `activateBowCollisionWhenAiming` | `bool` | – | – |
| Stop Aim Bow On Landing | `stopAimBowOnLanding` | `bool` | – | – |
| Reset Arrow Index On Bow State Change Enabled | `resetArrowIndexOnBowStateChangeEnabled` | `bool` | true | – |
| Activate Aiming State On Player Controller Enabled | `activateAimingStateOnPlayerControllerEnabled` | `bool` | true | – |

### Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Draw Holster Action Animations | `useDrawHolsterActionAnimations` | `bool` | true | – |
| Draw Bow Action Name | `drawBowActionName` | `string` | "Draw Bow" | – |
| Holster Bow Action Name | `holsterBowActionName` | `string` | "Holster Bow" | – |
| Load Arrow Action Name | `loadArrowActionName` | `string` | "Load Arrow" | – |
| Fire Arrow Action Name | `fireArrowActionName` | `string` | "Fire Arrow" | – |

### Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Ignore Tags | `useCustomIgnoreTags` | `bool` | – | – |
| Custom Tags To Ignore List | `customTagsToIgnoreList` | `List<string>` | new List<string> () | – |

### Third Person Camera State Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Camera State On Third Person | `setNewCameraStateOnThirdPerson` | `bool` | – | – |
| New Camera State On Third Person | `newCameraStateOnThirdPerson` | `string` | – | – |
| Set New Camera State On FBA | `setNewCameraStateOnFBA` | `bool` | – | – |
| New Camera State On FBA | `newCameraStateOnFBA` | `string` | "Full Body Awareness Aim Bow" | – |

### Fire Bow Without Aim Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Fire Bow Without Aim Enabled | `canFireBowWithoutAimEnabled` | `bool` | – | – |
| Delay To Fire Bow Without Aim | `delayToFireBowWithoutAim` | `float` | – | – |
| Auto Fire Arrows Without Aim | `autoFireArrowsWithoutAim` | `bool` | – | – |
| Wait Time To Stop Auto Fire | `waitTimeToStopAutoFire` | `float` | 0.5f | – |
| Set Camera State If No Aim Input Used Enabled | `setCameraStateIfNoAimInputUsedEnabled` | `bool` | – | – |

### Bow Weapon Types List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Bow Weapon System Info List | `bowWeaponSystemInfoList` | `List<bowWeaponSystemInfo>` | new List<bowWeaponSystemInfo> () | – |
| Current Bow Weapon ID | `currentBowWeaponID` | `int` | – | – |

### Bullet Time Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Bullet Time On Air | `activateBulletTimeOnAir` | `bool` | – | – |
| Bullet Time Scale | `bulletTimeScale` | `float` | – | – |
| Animation Speed On Bullet Time | `animationSpeedOnBulletTime` | `float` | 1 | – |
| Reduce Gravity Multipler On Bullet Time On Air | `reduceGravityMultiplerOnBulletTimeOnAir` | `bool` | – | – |
| Gravity Multipler On Bullet Time On Air | `gravityMultiplerOnBulletTimeOnAir` | `float` | – | – |
| Use Bullet Time On Bow Externally Enabled | `useBulletTimeOnBowExternallyEnabled` | `bool` | – | – |
| Use Event On Bullet Time | `useEventOnBulletTime` | `bool` | – | – |
| Event On Bullet Time Start | `eventOnBulletTimeStart` | `UnityEvent` | – | – |
| Event On Bullet Time End | `eventOnBulletTimeEnd` | `UnityEvent` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Upper Body Rotation System To Aim | `useUpperBodyRotationSystemToAim` | `bool` | true | – |
| Set New Upper Body Rotation Values | `setNewUpperBodyRotationValues` | `bool` | – | – |
| Horizontal Bending Multiplier | `horizontalBendingMultiplier` | `float` | 1 | – |
| Vertical Bending Multiplier | `verticalBendingMultiplier` | `float` | 1 | – |
| Extra Upper Body Rotation | `extraUpperBodyRotation` | `float` | 90 | – |
| Head Track Body Weight On Aim | `headTrackBodyWeightOnAim` | `float` | 1 | – |
| Can Move While Using Bow Enabled | `canMoveWhileUsingBowEnabled` | `bool` | true | – |
| Cancel Bow State On Empty Arrows Wait Delay | `cancelBowStateOnEmptyArrowsWaitDelay` | `float` | 0.5f | – |

### Durability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Durability | `ignoreDurability` | `bool` | – | – |
| General Attack Durability Multiplier | `generalAttackDurabilityMultiplier` | `float` | 1 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Bow Active | `bowActive` | `bool` | – | – |
| Bow Loaded Active | `bowLoadedActive` | `bool` | – | – |
| Arrow Is Fired | `arrowIsFired` | `bool` | – | – |
| Aiming Bow Active | `aimingBowActive` | `bool` | – | – |
| Arrows Available To Fire | `arrowsAvailableToFire` | `bool` | true | – |
| Check Arrows On Inventory | `checkArrowsOnInventory` | `bool` | – | – |
| Aim Input Pressed Down | `aimInputPressedDown` | `bool` | – | – |
| Bullet Time On Air Active | `bulletTimeOnAirActive` | `bool` | – | – |
| Aim Input Pressed On Fire Arrow Without Aim | `aimInputPressedOnFireArrowWithoutAim` | `bool` | – | – |
| Fire Arrow Without Aim Active | `fireArrowWithoutAimActive` | `bool` | – | – |
| Cancel Bow Coroutine Active | `cancelBowCoroutineActive` | `bool` | – | – |
| Last Time Pull Bow | `lastTimePullBow` | `float` | – | – |
| Current Multiple Arrow Type Index | `currentMultipleArrowTypeIndex` | `int` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Bow Enabled | `eventOnBowEnabled` | `UnityEvent` | – | – |
| Event On Bow Disabled | `eventOnBowDisabled` | `UnityEvent` | – | – |
| Event On Start Aim | `eventOnStartAim` | `UnityEvent` | – | – |
| Event On End Aim | `eventOnEndAim` | `UnityEvent` | – | – |
| Event On Fire Arrow | `eventOnFireArrow` | `UnityEvent` | – | – |
| Event On Cancel Load Bow On Stop Aim | `eventOnCancelLoadBowOnStopAim` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Action System | `mainPlayerActionSystem` | `playerActionSystem` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Upper Body Rotation System | `mainUpperBodyRotationSystem` | `upperBodyRotationSystem` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |
| Current Simple Weapon System | `currentSimpleWeaponSystem` | `simpleWeaponSystem` | – | – |
| Position To Place Arrow | `positionToPlaceArrow` | `Transform` | – | – |
| Arrow Position Reference | `arrowPositionReference` | `Transform` | – | – |
| Main Grabbed Object Melee Attack System | `mainGrabbedObjectMeleeAttackSystem` | `grabbedObjectMeleeAttackSystem` | – | – |
| Current Bow Holder System | `currentBowHolderSystem` | `bowHolderSystem` | – | – |
| Arrow Mesh Prefab | `arrowMeshPrefab` | `GameObject` | – | – |
| Arrow Mesh | `arrowMesh` | `GameObject` | – | – |
| Main Arrow Manager | `mainArrowManager` | `arrowManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateBowStateCoroutine()` | 弓状態更新コルーチンを停止し、接地判定フラグを false にする。 |
| `setBowLoadedState(bool state)` | 矢を装填した状態を設定し、移動ID・ストレイフ・IK・頭トラッキング・構え・イベントを一括更新する。 |
| `resetLastAmountOfFiredProjectiles()` | `lastAmountOfFiredProjectiles` を 0 にするだけ。 |
| `getLastAmountOfFiredProjectiles()` | `lastAmountOfFiredProjectiles` を返すだけ。 |
| `fireLoadedArrow()` | 発射アクションを再生し、イベント・所持矢の消費・耐久値減少・発射数加算を行う。 |
| `checkIfArrowsFoundOnInventoryToCancelBowState()` | インベントリの矢を確認し、撃てない場合は遅延後に弓状態を解除するコルーチンを開始する。 |
| `activateLoadBowAction()` | 照準中で矢がある場合のみ、矢を装填するカスタムアクションを実行する。 |
| `setAimBowState(bool state)` | 弓が有効なら照準状態を設定し、開始/終了イベント・カメラ・コライダー・弾丸時間を更新する。 |
| `setTimeBulletOnBowSystemExternally(bool state)` | 外部用設定が有効なら、弓使用中または解除時に `setTimeBulletOnBowSystem` を呼ぶ。 |
| `setBowActiveState(bool state)` | 弓の使用状態を切り替え、所持弓のID・矢種・各種イベント・コルーチンを更新する。 |
| `cancelBowLoadedStateIfActive()` | 弓が有効なら `cancelBowState` を呼び、照準入力フラグを下ろす。 |
| `cancelBowState()` | 装填中なら `setBowLoadedState(false)` を呼ぶだけ。 |
| `checkSetExtraRotationCoroutine(bool state)` | 既存コルーチンを止め、上半身の追加回転を補間するコルーチンを開始する。 |
| `stopCheckIfPlayerOnGroundCoroutine()` | 接地判定コルーチンを停止するだけ。 |
| `checkSpawnArrowInPlayerHand()` | 矢メッシュが未生成なら、プレハブを生成して `positionToPlaceArrow` に親子付けする。 |
| `checkBowHolderLoadArrow()` | 照準中でなければ矢位置表示を消し、照準中なら弓ホルダーの装填イベントを呼ぶ。 |
| `checkBowHolderFireArrow()` | 現在の弓ホルダーを取得し、発射イベントを呼ぶ。 |
| `checkUsePullBowMultipliersOnFireArrow()` | 引き絞り時間から威力とダメージ倍率を計算し、直近に発射した矢に設定する。 |
| `checkBowEventOnStartAim()` | 弓ホルダーを取得し、照準開始イベントを呼ぶ。 |
| `checkBowEventOnEndAim()` | 弓ホルダーを取得し、照準終了イベントを呼ぶ。 |
| `checkEventOnCancelBowAction()` | 弓ホルダーを取得し、弓アクション中止イベントを呼ぶ。 |
| `setCurrentBowWeaponSystemByID(int bowWeaponID)` | ID が一致する弓設定を選択し、武器有効化・矢表示・選択イベントを実行、他は解除する。 |
| `fireCurrentBowWeapon()` | 弓が有効なら現在の簡易武器の押下・離し入力で矢を発射する。 |
| `setPullBowState(bool state)` | 引き絞り開始時刻を記録または 0 に戻し、最大引きイベントの状態も更新する。 |
| `setArrowsAvailableToFireState(bool state)` | `arrowsAvailableToFire` を設定するだけ。 |
| `setPositionToPlaceArrowActiveState(bool state)` | `positionToPlaceArrow` のアクティブ状態を切り替えるだけ。 |
| `canUseWeaponsInput()` | プレイヤーが移動可能かつ多忙でなければ true を返す。 |
| `setIgnoreUseDrawHolsterActionAnimationsState(bool state)` | `ignoreUseDrawHolsterActionAnimations` を設定するだけ。 |
| `setUseDrawHolsterActionAnimationsState(bool state)` | `useDrawHolsterActionAnimations` を設定するだけ。 |
| `setArrowsManagedByInventoryState(bool state)` | `arrowsManagedByInventory` を設定するだけ。 |
| `setOriginalArrowsManagedByInventoryState()` | 保存していた初期値に `arrowsManagedByInventory` を戻す。 |
| `isAimingBowActive()` | `aimingBowActive` を返すだけ。 |
| `inputSetAimBowState(bool state)` | しゃがみ中は立ち上がりを試み、非照準発射中でなければ `setAimState` に委譲してフラグを初期化する。 |
| `inputFireArrow()` | 時間条件を満たし装填済みなら発射し、そうでなければ非照準発射を開始する。 |
| `inputStopFireArrowWithoutAim()` | 非照準発射を止め、必要なら照準を解除して各フラグを戻す。 |
| `inputChangeArrowType()` | 照準中でなければ矢種インデックスを次へ進め、弓設定を切り替えて所持数を更新する。 |
| `inputSetTimeBulletOnBowSystem(bool state)` | 弓が有効なら `setTimeBulletOnBowSystemExternally` に委譲するだけ。 |
| `inputToggleTimeBulletOnBowSystem()` | 現在の弾丸時間状態を反転して `inputSetTimeBulletOnBowSystem` を呼ぶ。 |
| `changeArrowTypeByIndex(int newIndex)` | 指定インデックスの矢種に切り替え、弓設定と所持数表示を更新する。 |
| `setUseUpperBodyRotationSystemToAimState(bool state)` | `useUpperBodyRotationSystemToAim` を設定するだけ。 |
| `setUseDrawHolsterActionAnimationsStateFromEditor(bool state)` | 状態を設定してから `updateComponent` で更新する。 |
| `setUseUpperBodyRotationSystemToAimStateFromEditor(bool state)` | 状態を設定してから `updateComponent` で更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent` と `updateDirtyScene` で更新するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnBulletTimeStart` | `UnityEvent` | – |
| `eventOnBulletTimeEnd` | `UnityEvent` | – |
| `eventOnBowEnabled` | `UnityEvent` | – |
| `eventOnBowDisabled` | `UnityEvent` | – |
| `eventOnStartAim` | `UnityEvent` | – |
| `eventOnEndAim` | `UnityEvent` | – |
| `eventOnFireArrow` | `UnityEvent` | – |
| `eventOnCancelLoadBowOnStopAim` | `UnityEvent` | – |

## 内部型

- `bowWeaponSystemInfo`（class）
- `arrowSurfaceTypeInfo`（class）
