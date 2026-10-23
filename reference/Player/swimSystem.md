# swimSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `externalControllerBehavior`
- **ソース**: `Player/Extra Movements/swimSystem.cs:6`

**概要**: `externalControllerBehavior` を継承した水泳モード。水面/潜水の判定、上下移動、ターボ、カメラ状態、水に入るトリガーのリストを管理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Swim System Enabled | `swimSystemEnabled` | `bool` | true | – |
| Layer For Ground Detection | `layerForGroundDetection` | `LayerMask` | – | – |
| Ground Detection Raycast Distance | `groundDetectionRaycastDistance` | `float` | 1 | – |
| Ground Detection Raycast Distance On Water | `groundDetectionRaycastDistanceOnWater` | `float` | 0.1f | – |
| Max Distance To Walk On Water | `maxDistanceToWalkOnWater` | `float` | 1 | – |

### Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Swim ID | `swimID` | `int` | – | – |
| Regular ID | `regularID` | `int` | 1 | – |
| Swim State ID | `swimStateID` | `int` | 0 | – |
| Dive State ID | `diveStateID` | `int` | 1 | – |
| Moving Up State ID | `movingUpStateID` | `int` | 1 | – |
| Moving Down State ID | `movingDownStateID` | `int` | 1 | – |
| Moving Up Forward State ID | `movingUpForwardStateID` | `float` | 1.5f | – |
| Moving Down Forward State ID | `movingDownForwardStateID` | `float` | 2.5f | – |
| Regular Idle ID | `regularIdleID` | `int` | 0 | – |

### Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Force Mode | `useForceMode` | `bool` | – | – |
| Swim Force Mode | `swimForceMode` | `ForceMode` | – | – |
| Move Up And Down Enabled | `moveUpAndDownEnabled` | `bool` | – | – |
| Turbo Enabled | `turboEnabled` | `bool` | – | – |
| Water Friction | `waterFriction` | `float` | – | – |
| Max Swim Velocity | `maxSwimVelocity` | `float` | – | – |
| Swim Turbo Speed | `swimTurboSpeed` | `float` | – | – |
| Swim Force | `swimForce` | `float` | – | – |
| Swim Move Up Speed | `swimMoveUpSpeed` | `float` | – | – |
| Swim Move Down Speed | `swimMoveDownSpeed` | `float` | – | – |
| Swim Speed On Aim Multiplier | `swimSpeedOnAimMultiplier` | `float` | – | – |
| Auto Adjust Distance To Swim Surface Speed | `autoAdjustDistanceToSwimSurfaceSpeed` | `float` | 2 | – |
| Auto Adjust Distance To Swim Surface | `autoAdjustDistanceToSwimSurface` | `float` | 1.6f | – |
| First Person Speed Multiplier | `firstPersonSpeedMultiplier` | `float` | 1 | – |
| Add Force If Dead On Water | `addForceIfDeadOnWater` | `bool` | – | – |
| Force Direction If Dead On Water | `forceDirectionIfDeadOnWater` | `Vector3` | -Vector3.up | – |
| Force Amount If Dead On Water | `forceAmountIfDeadOnWater` | `float` | 5 | – |

### Return To Surface On Enter Water Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Initial State On Surface On Enter Water | `setInitialStateOnSurfaceOnEnterWater` | `bool` | true | – |
| Use Max Speed To Move To Surface On Swim Enabled | `useMaxSpeedToMoveToSurfaceOnSwimEnabled` | `bool` | – | – |
| Max Speed To Move To Surface On Swim Enabled | `maxSpeedToMoveToSurfaceOnSwimEnabled` | `float` | 20 | – |
| Min Speed To Set Swim On Surface State | `minSpeedToSetSwimOnSurfaceState` | `float` | 5 | – |
| Cancel Return To Surface If Input Pressed | `cancelReturnToSurfaceIfInputPressed` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Min Distance For Swim Surface | `minDistanceForSwimSurface` | `float` | 0.2f | – |
| Delay To Reset Velocity When Reaching Surface From Moving Input | `delayToResetVelocityWhenReachingSurfaceFromMovingInput` | `float` | 0.4f | – |
| Keep Swim State Active On Death | `keepSwimStateActiveOnDeath` | `bool` | – | – |
| Check Ground Distance On Swim On Surface | `checkGroundDistanceOnSwimOnSurface` | `bool` | true | – |
| Raycast Distance To Check On Swim On Surface | `raycastDistanceToCheckOnSwimOnSurface` | `float` | 1 | – |
| Check If Player Is On Water Inside Vehicles | `checkIfPlayerIsOnWaterInsideVehicles` | `bool` | – | – |

### Jump Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Jump When Swimming On Surface | `canJumpWhenSwimmingOnSurface` | `bool` | – | – |
| Jump Force On Surface | `jumpForceOnSurface` | `float` | – | – |
| Only Climb On Close Surfaces | `onlyClimbOnCloseSurfaces` | `bool` | – | – |
| Max Angle Difference On Surface To Climb | `maxAngleDifferenceOnSurfaceToClimb` | `float` | 90 | – |
| Max Climb Surface Height | `maxClimbSurfaceHeight` | `float` | 4 | – |
| Allow Jump On Swim If No Close Surface To Climb Found | `allowJumpOnSwimIfNoCloseSurfaceToClimbFound` | `bool` | – | – |
| Climb Surface Action System Transform | `climbSurfaceActionSystemTransform` | `Transform` | – | – |
| Event To Activate Climb Surface Action System | `eventToActivateClimbSurfaceActionSystem` | `eventParameters.eventToCallWithGameObject` | – | – |

### Swim Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Swim Vertical Speed Multiplier | `swimVerticalSpeedMultiplier` | `float` | – | – |
| Swim Horizontal Speed Multiplier | `swimHorizontalSpeedMultiplier` | `float` | – | – |

### Dive Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dive Vertical Speed Multiplier | `diveVerticalSpeedMultiplier` | `float` | – | – |
| Dive Horizontal Speed Multiplier | `diveHorizontalSpeedMultiplier` | `float` | – | – |

### Third Person Camera State Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Camera State On Third Person | `setNewCameraStateOnThirdPerson` | `bool` | – | – |
| New Camera State On Third Person | `newCameraStateOnThirdPerson` | `string` | – | – |
| Return To Previuos View On Swim End | `returnToPreviuosViewOnSwimEnd` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Swim System Active | `swimSystemActive` | `bool` | – | – |
| Turbo Active | `turboActive` | `bool` | – | – |
| Moving Up | `movingUp` | `bool` | – | – |
| Moving Down | `movingDown` | `bool` | – | – |
| Currently On Surface | `currentlyOnSurface` | `bool` | – | – |
| Currently Diving | `currentlyDiving` | `bool` | – | – |
| Overriding Movement To Surface Active | `overridingMovementToSurfaceActive` | `bool` | – | – |
| Target Direction | `targetDirection` | `Vector3` | – | – |
| Current Horizontal Movement | `currentHorizontalMovement` | `float` | – | – |
| Current Vertical Movement | `currentVerticalMovement` | `float` | – | – |
| Check If Close To Surface | `checkIfCloseToSurface` | `bool` | – | – |
| Player Is Moving | `playerIsMoving` | `bool` | – | – |
| Current Distance To Surface | `currentDistanceToSurface` | `float` | – | – |
| Checking To Activate Movement To Surface Automatically Active | `checkingToActivateMovementToSurfaceAutomaticallyActive` | `bool` | – | – |
| Current Stat ID | `currentStatID` | `float` | – | – |
| Walking On Water | `walkingOnWater` | `bool` | – | – |
| Total Force | `totalForce` | `Vector3` | – | – |
| Extra Force | `extraForce` | `Vector3` | – | – |
| Camera Below Water | `cameraBelowWater` | `bool` | – | – |
| Swim Forces Paused | `swimForcesPaused` | `bool` | – | – |
| Current Look Angle | `currentLookAngle` | `float` | – | – |
| Look Direction Angle | `lookDirectionAngle` | `float` | – | – |
| Checking If Player Not Moving Inside Vehicle Active | `checkingIfPlayerNotMovingInsideVehicleActive` | `bool` | – | – |
| Swim Trigger List | `swimTriggerList` | `List<Collider>` | new List<Collider> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On State Enabled | `eventOnStateEnabled` | `UnityEvent` | – | – |
| Event On State Disabled | `eventOnStateDisabled` | `UnityEvent` | – | – |
| Use Event On Walking On Water | `useEventOnWalkingOnWater` | `bool` | – | – |
| Event On Walking On Water | `eventOnWalkingOnWater` | `UnityEvent` | – | – |
| Use Events On Dive State Change | `useEventsOnDiveStateChange` | `bool` | – | – |
| Event On Start Dive | `eventOnStartDive` | `UnityEvent` | – | – |
| Event On End Dive | `eventOnEndDive` | `UnityEvent` | – | – |
| Use Event On Change Swim To Dive | `useEventOnChangeSwimToDive` | `bool` | – | – |
| Event On Change Swim To Dive | `eventOnChangeSwimToDive` | `UnityEvent` | – | – |
| Use Event On Change Dive To Swim | `useEventOnChangeDiveToSwim` | `bool` | – | – |
| Event On Change Dive To Swim | `eventOnChangeDiveToSwim` | `UnityEvent` | – | – |
| Event Before Activating Swim System | `eventBeforeActivatingSwimSystem` | `UnityEvent` | – | – |
| Event Before Deactivating Swim System | `eventBeforeDeactivatingSwimSystem` | `UnityEvent` | – | – |
| Use Event On Camera Underwater Effect | `useEventOnCameraUnderwaterEffect` | `bool` | – | – |
| Event On Camera Under Water Start | `eventOnCameraUnderWaterStart` | `UnityEvent` | – | – |
| Event On Camera Under Water End | `eventOnCameraUnderWaterEnd` | `UnityEvent` | – | – |
| Use Event Use Turbo On Swim | `useEventUseTurboOnSwim` | `bool` | – | – |
| Event On Star Turbo On Swim | `eventOnStarTurboOnSwim` | `UnityEvent` | – | – |
| Event On End Turbo On Swim | `eventOnEndTurboOnSwim` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Player Camera Transform | `playerCameraTransform` | `Transform` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Player Input | `playerInput` | `playerInputManager` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |
| Main Player Collider | `mainPlayerCollider` | `Collider` | – | – |
| Swim Collider | `swimCollider` | `Collider` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Ragdoll Activator | `mainRagdollActivator` | `ragdollActivator` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopCheckIfPlayerNotOnVehicleCoroutine()` | `checkIfPlayerNotOnVehicleCoroutine` が null でなければ停止するだけ。 |
| `setSwimSystemActivestate(bool state)` | 泳ぎ状態を切り替え、車両乗車時の判定コルーチン、水面歩行判定、コライダー無視、カメラ状態、各種フラグを更新する。 |
| `enableOrDisableTurbo(bool state)` | ターボを切り替え、飛行ターボ設定・空中速度値・開始/終了イベントを更新する。 |
| `setCanUseTurboPausedState(bool state)` | false でターボ中なら解除し、`canUseTurboPausedState` を設定する。 |
| `inputChangeTurboState(bool state)` | 上書き移動中は無視し、泳ぎ中でターボ有効なら `enableOrDisableTurbo` を呼ぶ。 |
| `inputMoveUp(bool state)` | 泳ぎ中の上昇入力。水面ではジャンプやクライム判定を行い、最後に上昇移動を有効化する。 |
| `inputMoveDown(bool state)` | 泳ぎ中の下降入力で下降移動を有効化し、未潜水なら `setDivingState(true)` にする。 |
| `setSwimZoneTransform(Transform newSwimZoneTransform)` | `currentSwimZoneTransform` を設定するだけ。 |
| `setSwimTrigger(Collider newSwimTrigger)` | トリガーを設定し、null でないかを `currentSwimTriggerLocated` に反映する。 |
| `isSwimTriggerListEmpty()` | `swimTriggerList` が空かどうかを返す。 |
| `addSwimTrigger(Collider newTrigger)` | null でも重複でもなければ `swimTriggerList` に追加する。 |
| `removeSwimTrigger(Collider newTrigger)` | `swimTriggerList` に含まれていれば削除する。 |
| `clearSwimTriggerList()` | `swimTriggerList` を空にする。 |
| `setCurrentWaterSurfaceSystem(waterSurfaceSystem newWaterSurfaceSystem)` | 水面システムを設定し、null でなければ動的更新フラグを true にする。 |
| `setDivingState(bool state)` | 潜水/浮上状態を切り替え、`currentlyOnSurface`、潜水イベント、状態ID、表面到達フラグを更新する。 |
| `setEnableExternalForceOnSwimModeState(bool state)` | 泳ぎ中のみ、プレイヤーへ外部力設定をそのまま転送する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStateEnabled` | `UnityEvent` | – |
| `eventOnStateDisabled` | `UnityEvent` | – |
| `eventOnWalkingOnWater` | `UnityEvent` | – |
| `eventOnStartDive` | `UnityEvent` | – |
| `eventOnEndDive` | `UnityEvent` | – |
| `eventOnChangeSwimToDive` | `UnityEvent` | – |
| `eventOnChangeDiveToSwim` | `UnityEvent` | – |
| `eventBeforeActivatingSwimSystem` | `UnityEvent` | – |
| `eventBeforeDeactivatingSwimSystem` | `UnityEvent` | – |
| `eventOnCameraUnderWaterStart` | `UnityEvent` | – |
| `eventOnCameraUnderWaterEnd` | `UnityEvent` | – |
| `eventOnStarTurboOnSwim` | `UnityEvent` | – |
| `eventOnEndTurboOnSwim` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkPauseStateDuringExternalForceOrBehavior()`, `checkResumeStateAfterExternalForceOrBehavior()`, `disableExternalControllerState()`, `setCurrentPlayerActionSystemCustomActionCategoryID()`, `updateControllerBehavior()`

</details>
