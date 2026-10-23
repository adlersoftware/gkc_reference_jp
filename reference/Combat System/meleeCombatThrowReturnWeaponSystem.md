# meleeCombatThrowReturnWeaponSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/meleeCombatThrowReturnWeaponSystem.cs:7`

**概要**: 掴んだ近接武器の投擲・帰還・テレポートを制御し、`continueThrowObjectCoroutine` で剛体に力を加え、`returnObjectCoroutine` で手元へ補間移動させる。表面ごとの音・ダメージ・イベントやスタミナ消費も扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Throw Object Enabled | `throwObjectEnabled` | `bool` | true | – |
| Return Object Enabled | `returnObjectEnabled` | `bool` | true | – |
| Player On Ground To Activate Throw | `playerOnGroundToActivateThrow` | `bool` | – | – |
| Throw Objects Force Mode | `throwObjectsForceMode` | `ForceMode` | – | – |
| Throw Objects Layer To Check | `throwObjectsLayerToCheck` | `LayerMask` | – | – |
| Use Spline To Return Object | `useSplineToReturnObject` | `bool` | – | – |
| Spline To Return Object | `splineToReturnObject` | `BezierSpline` | – | – |
| Disable Drop Object When Thrown Or Returning | `disableDropObjectWhenThrownOrReturning` | `bool` | – | – |
| Moving Objects Tag | `movingObjectsTag` | `string` | "moving" | – |
| General Damage On Surface Detected On Throw | `generalDamageOnSurfaceDetectedOnThrow` | `float` | 1 | – |
| Apply Damage On Surface Detected On Return Enabled | `applyDamageOnSurfaceDetectedOnReturnEnabled` | `bool` | true | – |
| Apply Damage On Object Return Path Enabled | `applyDamageOnObjectReturnPathEnabled` | `bool` | true | – |
| General Damage Multiplier On Object Return | `generalDamageMultiplierOnObjectReturn` | `float` | 1 | – |
| General Damage Multiplier On Return Path | `generalDamageMultiplierOnReturnPath` | `float` | 1 | – |
| Use Hold To Throw Object On All Weapons On2 5d Enabled | `useHoldToThrowObjectOnAllWeaponsOn2_5dEnabled` | `bool` | true | – |
| Use Hold To Throw Object On All Weapons On3d Locked View Enabled | `useHoldToThrowObjectOnAllWeaponsOn3dLockedViewEnabled` | `bool` | true | – |
| Calculate Throw Direction Before Throw Animation Enabled | `calculateThrowDirectionBeforeThrowAnimationEnabled` | `bool` | – | – |

### Follow Object On Throw Melee Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check If Object To Follow On Throw Melee Weapon | `checkIfObjectToFollowOnThrowMeleeWeapon` | `bool` | – | – |
| Extra Weapon On Air Time If Object To Follow Detected | `extraWeaponOnAirTimeIfObjectToFollowDetected` | `float` | 6 | – |

### Throw Object Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Throw Return Object | `useEventsOnThrowReturnObject` | `bool` | – | – |
| Event On Throw Object | `eventOnThrowObject` | `UnityEvent` | – | – |
| Event On Return Object | `eventOnReturnObject` | `UnityEvent` | – | – |
| Event On Drop Object When Is Thrown | `eventOnDropObjectWhenIsThrown` | `UnityEvent` | – | – |

### Teleport Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Teleport Player On Throw Enabled | `teleportPlayerOnThrowEnabled` | `bool` | true | – |
| Grab Melee Weapon On Teleport Position Reached | `grabMeleeWeaponOnTeleportPositionReached` | `bool` | true | – |
| Teleport Speed | `teleportSpeed` | `float` | 10 | – |
| Camera Fov On Teleport | `cameraFovOnTeleport` | `float` | 70 | – |
| Camera Fov On Teleport Speed | `cameraFovOnTeleportSpeed` | `float` | 5 | – |
| Min Distance To Stop Teleport | `minDistanceToStopTeleport` | `float` | 1 | – |
| Teleport Instantly To Position | `teleportInstantlyToPosition` | `bool` | – | – |
| Use Smooth Camera Follow State On Teleport | `useSmoothCameraFollowStateOnTeleport` | `bool` | true | – |
| Smooth Camera Follow Duration | `smoothCameraFollowDuration` | `float` | 3 | – |
| Event On Start Teleport | `eventOnStartTeleport` | `UnityEvent` | – | – |
| Event On End Teleport | `eventOnEndTeleport` | `UnityEvent` | – | – |

### Stamina Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Stamina On Throw Object Enabled | `useStaminaOnThrowObjectEnabled` | `bool` | true | – |
| Throw Object Stamina State | `throwObjectStaminaState` | `string` | "Throw Grabbed Object" | – |
| Stamina To Use On Throw Object | `staminaToUseOnThrowObject` | `float` | 10 | – |
| Custom Refill Stamina Delay After Throw | `customRefillStaminaDelayAfterThrow` | `float` | – | – |
| Use Stamina On Return Object Enabled | `useStaminaOnReturnObjectEnabled` | `bool` | true | – |
| Return Object Stamina State | `returnObjectStaminaState` | `string` | "Return Grabbed Object" | – |
| Stamina To Use On Return Object | `staminaToUseOnReturnObject` | `float` | 10 | – |
| Custom Refill Stamina Delay After Return | `customRefillStaminaDelayAfterReturn` | `float` | – | – |

### Hold Throw Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Action Active Animator Name | `actionActiveAnimatorName` | `string` | "Action Active" | – |
| Hold Throw Melee Weapon Animator Name | `holdThrowMeleeWeaponAnimatorName` | `string` | "Action ID" | – |
| Hold Throw Melee Weapon Animator ID | `holdThrowMeleeWeaponAnimatorID` | `int` | – | – |
| Use Strafe On Hold Throw Weapon | `useStrafeOnHoldThrowWeapon` | `bool` | – | – |
| Set New Camera State On Third Person | `setNewCameraStateOnThirdPerson` | `bool` | – | – |
| New Camera State On Third Person | `newCameraStateOnThirdPerson` | `string` | – | – |
| Return To Previuos View On End | `returnToPreviuosViewOnEnd` | `bool` | true | – |
| Located Enemy Icon Name | `locatedEnemyIconName` | `string` | "Melee Located Enemy Icon" | – |
| Use Sound On Target Located On Hold Throw Weapon | `useSoundOnTargetLocatedOnHoldThrowWeapon` | `bool` | – | – |
| Sound On Target Located On Hold Throw Weapon | `soundOnTargetLocatedOnHoldThrowWeapon` | `AudioClip` | – | – |
| On Target Located On Hold Throw Weapon Audio Element | `onTargetLocatedOnHoldThrowWeaponAudioElement` | `AudioElement` | – | – |
| Pause Damage Reaction During Weapon Hold Enabled | `pauseDamageReactionDuringWeaponHoldEnabled` | `bool` | – | – |
| Use Events On Hold Throw Weapon | `useEventsOnHoldThrowWeapon` | `bool` | – | – |
| Event On Start Hold Throw Weapon | `eventOnStartHoldThrowWeapon` | `UnityEvent` | – | – |
| Event On End Hold Throw Weapon | `eventOnEndHoldThrowWeapon` | `UnityEvent` | – | – |
| Use Event On Target Located On Hold Throw Weapon | `useEventOnTargetLocatedOnHoldThrowWeapon` | `bool` | – | – |
| Event On Target Located On Hold Throw Weapon | `eventOnTargetLocatedOnHoldThrowWeapon` | `UnityEvent` | – | – |

### Locked Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Head Track Body Weight On Aim | `headTrackBodyWeightOnAim` | `float` | 1 | – |
| Custom Aim Reticle Name | `customAimReticleName` | `string` | "Reticle 1" | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Sphere Color | `sphereColor` | `Color` | Color.green | – |
| Cube Color | `cubeColor` | `Color` | Color.blue | – |
| Show Debug Draw | `showDebugDraw` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Object Thrown | `objectThrown` | `bool` | – | – |
| Object Thrown Travelling To Target | `objectThrownTravellingToTarget` | `bool` | – | – |
| Continue Objec Throw Activated | `continueObjecThrowActivated` | `bool` | – | – |
| Returning Thrown Object | `returningThrownObject` | `bool` | – | – |
| Attack Input Paused For Stamina | `attackInputPausedForStamina` | `bool` | – | – |
| Throw Object Input Paused For Stamina | `throwObjectInputPausedForStamina` | `bool` | – | – |
| Object To Follow Found | `objectToFollowFound` | `bool` | – | – |
| Object To Follow | `objectToFollow` | `Transform` | – | – |
| Current Object To Follow From Hold Throw Weapon | `currentObjectToFollowFromHoldThrowWeapon` | `Transform` | – | – |
| Teleport In Process | `teleportInProcess` | `bool` | – | – |
| Throw Weapon Action Paused | `throwWeaponActionPaused` | `bool` | – | – |
| Surface Deteceted On Object Thrown | `surfaceDetecetedOnObjectThrown` | `GameObject` | – | – |
| Surface Detected | `surfaceDetected` | `bool` | – | – |
| Surface Not Found | `surfaceNotFound` | `bool` | – | – |
| Located Enemies | `locatedEnemies` | `List<Transform>` | new List<Transform> () | – |
| Temporal Located Enemies | `temporalLocatedEnemies` | `List<Transform>` | new List<Transform> () | – |
| Check Body Aim State Active | `checkBodyAimStateActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Grabbed Object Melee Attack System | `mainGrabbedObjectMeleeAttackSystem` | `grabbedObjectMeleeAttackSystem` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Grab Objects | `mainGrabObjects` | `grabObjects` | – | – |
| Main Stamina System | `mainStaminaSystem` | `staminaSystem` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Main Slice System | `mainSliceSystem` | `sliceSystem` | – | – |
| Main Player Teleport System | `mainPlayerTeleportSystem` | `playerTeleportSystem` | – | – |
| Player Controller Game Object | `playerControllerGameObject` | `GameObject` | – | – |
| Hand Position Reference | `handPositionReference` | `Transform` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |

### Melee Weapon Components Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Grabbed Object Transform | `currentGrabbedObjectTransform` | `Transform` | – | – |
| Current Melee Weapon | `currentMeleeWeapon` | `grabPhysicalObjectMeleeAttackSystem` | – | – |
| Current Object Rigidbody | `currentObjectRigidbody` | `Rigidbody` | – | – |
| Current Grabbed Weapon Info | `currentGrabbedWeaponInfo` | `grabbedObjectMeleeAttackSystem.grabbedWeaponInfo` | – | – |
| Object Rotation Point | `objectRotationPoint` | `Transform` | – | – |
| Current Grab Physical Object System | `currentGrabPhysicalObjectSystem` | `grabPhysicalObjectSystem` | – | – |
| Object Rotation Point Parent | `objectRotationPointParent` | `Transform` | – | – |
| Current Hit Combat | `currentHitCombat` | `hitCombat` | – | – |
| Main Dual Wield Melee Weapon Object System | `mainDualWieldMeleeWeaponObjectSystem` | `dualWieldMeleeWeaponObjectSystem` | – | – |
| Raycast Check Transfrom | `raycastCheckTransfrom` | `Transform` | – | – |
| Current Hit Combat Box Collider | `currentHitCombatBoxCollider` | `BoxCollider` | – | – |
| Target List To Track Active | `targetListToTrackActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setNewGrabPhysicalObjectSystem(grabPhysicalObjectSystem newGrabPhysicalObjectSystem)` | `currentGrabPhysicalObjectSystem` を設定するだけ。 |
| `setCurrentGrabbedWeaponInfo(grabbedObjectMeleeAttackSystem.grabbedWeaponInfo newCurrentGrabbedWeaponInfo)` | `currentGrabbedWeaponInfo` を設定するだけ。 |
| `setNewGrabPhysicalObjectMeleeAttackSystem(grabPhysicalObjectMeleeAttackSystem newGrabPhysicalObjectMeleeAttackSystem)` | 武器システムを登録し、Transform・剛体・回転点・`hitCombat`・コライダーを取得する。 |
| `removeGrabPhysicalObjectMeleeAttackSystem()` | 武器関連の参照を null にし、ホールド投擲状態を解除する。 |
| `setThrowWeaponActionPausedState(bool state)` | `throwWeaponActionPaused` を設定するだけ。 |
| `inputPressDownThrowObject()` | 押下開始として `setPressDownOrUpOnThrowObject(true)` を呼び、照準や投擲を始める。 |
| `inputPressUpThrowObject()` | 押上として `setPressDownOrUpOnThrowObject(false)` を呼び、タップ/長押しで投擲や帰還を行う。 |
| `stopUpdateLocateTargetsCoroutine()` | 対象探索コルーチンを止め、3Dフリーカメラ以外では照準状態を解除する。 |
| `playSound(AudioElement newClip)` | `AudioElement` が null でなければ `AudioPlayer.PlayOneShot` で再生する。 |
| `inputThrowOrReturnObject()` | 状態と入力可否を確認し、未投擲なら `throwObject`、投擲済みなら `returnObject` を呼ぶ。 |
| `inputActivateTeleport()` | 各状態とテレポート有効設定を確認してから `activateTeleport` を呼ぶ。 |
| `throwObject()` | 投擲設定と状態を確認し、`throwObjectCoroutine` を開始する。 |
| `setObjectThrownState(bool state)` | 自身と武器システムの投擲状態フラグを設定する。 |
| `continueThrowObject()` | 投擲コルーチンを差し替え、掴みが無効なら状態を戻し、有効なら物理投擲を実行する。 |
| `checkSurfaceOnThrowWeapon(GameObject objectToCheck)` | 回転点から対象へレイキャストし、表面名と位置を求めて表面処理へ渡す。 |
| `returnObject()` | 帰還条件を満たせば `returnObjectCoroutine` を開始し、武器を手元へ戻す。 |
| `getLastTimeObjectReturn()` | `lastTimeObjectReturn` を返すだけ。 |
| `checkEventOnThrowOrReturnObject(bool state)` | 設定が有効なら投擲/帰還イベントを発火する。 |
| `cancelThrowObject()` | 投擲コルーチンを止め、投擲状態・シールド・ホールド照準を解除する。 |
| `activateTeleport()` | 表面オフセットを加味した位置へプレイヤーをテレポートし、監視コルーチンを開始する。 |
| `stopActivateTeleportCoroutine()` | テレポートコルーチンを止め、`teleportInProcess` を false にする。 |
| `setThrowObjectEnabledState(bool state)` | `throwObjectEnabled` を設定するだけ。 |
| `setReturnObjectEnabledState(bool state)` | `returnObjectEnabled` を設定するだけ。 |
| `setApplyDamageOnSurfaceDetectedOnReturnEnabledState(bool state)` | `applyDamageOnSurfaceDetectedOnReturnEnabled` を設定するだけ。 |
| `setApplyDamageOnObjectReturnPathEnabledState(bool state)` | `applyDamageOnObjectReturnPathEnabled` を設定するだけ。 |
| `setGeneralDamageMultiplierOnObjectReturnValue(float newValue)` | `generalDamageMultiplierOnObjectReturn` を設定するだけ。 |
| `setGeneralDamageMultiplierOnReturnPathValue(float newValue)` | `generalDamageMultiplierOnReturnPath` を設定するだけ。 |
| `setGeneralDamageOnSurfaceDetectedOnThrowValue(float newValue)` | `generalDamageOnSurfaceDetectedOnThrow` を設定するだけ。 |
| `setObjectThrownTravellingToTargetState(bool state)` | `objectThrownTravellingToTarget` を設定するだけ。 |
| `isObjectThrownTravellingToTarget()` | `objectThrownTravellingToTarget` を返すだけ。 |
| `isContinueObjecThrowActivated()` | `continueObjecThrowActivated` を返すだけ。 |
| `isReturningThrownObject()` | `returningThrownObject` を返すだけ。 |
| `getLastTimeObjectThrown()` | `lastTimeObjectThrown` を返すだけ。 |
| `isCurrentWeaponThrown()` | `objectThrown` を返すだけ。 |
| `setThrowObjectInputPausedForStaminaState(bool state)` | `throwObjectInputPausedForStamina` を設定するだけ。 |
| `stopThrowStateOnRemoveMeleeWeapon()` | 投擲中ならコルーチン停止とドロップイベント・状態復元を行い、投擲フラグを解除する。 |
| `setSurfacecNotFoundState(bool state)` | `surfaceNotFound` を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnThrowObject` | `UnityEvent` | – |
| `eventOnReturnObject` | `UnityEvent` | – |
| `eventOnDropObjectWhenIsThrown` | `UnityEvent` | – |
| `eventOnStartTeleport` | `UnityEvent` | – |
| `eventOnEndTeleport` | `UnityEvent` | – |
| `eventOnStartHoldThrowWeapon` | `UnityEvent` | – |
| `eventOnEndHoldThrowWeapon` | `UnityEvent` | – |
| `eventOnTargetLocatedOnHoldThrowWeapon` | `UnityEvent` | – |
