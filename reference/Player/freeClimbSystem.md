# freeClimbSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `externalControllerBehavior`
- **ソース**: `Player/Extra Movements/freeClimbSystem.cs:6`

**概要**: 壁面を自由に登るフリークライムを制御する外部コントローラ。レイキャストで登れる面を検出し、`externalControllerBehavior` として移動・アニメーション・カメラを登攀状態へ切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Climb Enabled | `climbEnabled` | `bool` | true | – |
| Climb Check Can Be Used | `climbCheckCanBeUsed` | `bool` | true | – |
| Min Distance To Surface To Grab Surface On Ground | `minDistanceToSurfaceToGrabSurfaceOnGround` | `float` | 0.8f | – |
| Min Distance To Surface To Grab Surface On Air | `minDistanceToSurfaceToGrabSurfaceOnAir` | `float` | 1 | – |
| Activate Climb State Directly On Press Input | `activateClimbStateDirectlyOnPressInput` | `bool` | – | – |
| Can Activate Climb On Player On Ground | `canActivateClimbOnPlayerOnGround` | `bool` | true | – |
| Ignore Activate Climb State On Next Surface Detected Active | `ignoreActivateClimbStateOnNextSurfaceDetectedActive` | `bool` | – | – |
| Surface Offset | `surfaceOffset` | `float` | 0.05f | – |
| Min Wait Time Since Last Time Action Active To Climb | `minWaitTimeSinceLastTimeActionActiveToClimb` | `float` | 0.6f | – |

### Climb Method Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Raycast Detection To Climb | `useRaycastDetectionToClimb` | `bool` | true | – |
| Main Climb Detection Collision System | `mainClimbDetectionCollisionSystem` | `climbDetectionCollisionSystem` | – | – |
| Climb Detection Collision Position Offset | `climbDetectionCollisionPositionOffset` | `Vector3` | – | – |
| Update Rigidbody Position Smoothly On Detection Collision | `updateRigidbodyPositionSmoothlyOnDetectionCollision` | `bool` | true | – |
| Min Delay To Adjust Detection Collision | `minDelayToAdjustDetectionCollision` | `float` | 1 | – |
| Adjust To Found Surface Speed | `adjustToFoundSurfaceSpeed` | `float` | 4 | – |
| Adjust To Found Surface Offset | `adjustToFoundSurfaceOffset` | `float` | 0.3f | – |

### Reset Rotation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Reset Player Rotation Speed | `resetPlayerRotationSpeed` | `float` | 5 | – |
| Rotate Camera To Player Rotation On Climb Active Enabled | `rotateCameraToPlayerRotationOnClimbActiveEnabled` | `bool` | true | – |
| Use Camera Offset On Climb Active Enabled | `useCameraOffsetOnClimbActiveEnabled` | `bool` | – | – |
| Camera Offset On Climb Active | `cameraOffsetOnClimbActive` | `Vector3` | – | – |
| Camera Offset On Climb Active Lerp Speed | `cameraOffsetOnClimbActiveLerpSpeed` | `float` | – | – |

### Stop Climb Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Offset To Check If Stop Climb State On Raycast | `offsetToCheckIfStopClimbStateOnRaycast` | `float` | 1 | – |
| Min Time To Stop Climb If Not Surface Found | `minTimeToStopClimbIfNotSurfaceFound` | `float` | 0.3f | – |
| Max Raycast Distance To Stop Climb | `maxRaycastDistanceToStopClimb` | `float` | 0.75f | – |

### Surface Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Raycast Layermask | `raycastLayermask` | `LayerMask` | – | – |
| Raycast Distance | `raycastDistance` | `float` | 0.6f | – |
| Raycast Distance To Check To Activate Climb On Ground | `raycastDistanceToCheckToActivateClimbOnGround` | `float` | 0.9f | – |
| Raycast Distance To Check To Activate Climb On Air | `raycastDistanceToCheckToActivateClimbOnAir` | `float` | 0.9f | – |
| Vertical Raycast Offset | `verticalRaycastOffset` | `float` | 1 | – |
| Use Climb Zone Detection Raycast | `useClimbZoneDetectionRaycast` | `bool` | – | – |
| Up Offset To Detect Surface On Movement Input | `upOffsetToDetectSurfaceOnMovementInput` | `float` | 0.5f | – |
| Down Offset To Detect Surface On Movement Input | `downOffsetToDetectSurfaceOnMovementInput` | `float` | 0.2f | – |
| Right Offset To Detect Surface On Movement Input | `rightOffsetToDetectSurfaceOnMovementInput` | `float` | 0.2f | – |
| Left Offset To Detect Surface On Movement Input | `leftOffsetToDetectSurfaceOnMovementInput` | `float` | 0.2f | – |

### Surface To Ignore Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Surfaces To Ignore Tags | `useSurfacesToIgnoreTags` | `bool` | – | – |
| Surfaces To Ignore Tags List | `surfacesToIgnoreTagsList` | `List<string>` | new List<string> () | – |
| Use Surfaces To Check Tags On Climb By Input | `useSurfacesToCheckTagsOnClimbByInput` | `bool` | – | – |
| Surfaces To Check Tags On Climb By Input List | `surfacesToCheckTagsOnClimbByInputList` | `List<string>` | new List<string> () | – |
| Check For Climb Surface Zone System On Climb Input | `checkForClimbSurfaceZoneSystemOnClimbInput` | `bool` | – | – |
| Avoid Movement Toward Surfaces To Ignore | `avoidMovementTowardSurfacesToIgnore` | `bool` | – | – |
| Stop Climb If Surface To Ignore Detected | `stopClimbIfSurfaceToIgnoreDetected` | `bool` | – | – |
| Avoid Movement Toward No Climb Zones | `avoidMovementTowardNoClimbZones` | `bool` | – | – |
| Ignore Rigidbodies | `ignoreRigidbodies` | `bool` | – | – |

### Surface In Front Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Surface For Lower Body Enabled | `checkSurfaceForLowerBodyEnabled` | `bool` | true | – |
| Use Hang State On No Surface On Lower Body | `useHangStateOnNoSurfaceOnLowerBody` | `bool` | true | – |
| Lower Body Raycast Offset | `lowerBodyRaycastOffset` | `float` | 0.5f | – |
| Upper Body Raycast Offset | `upperBodyRaycastOffset` | `float` | 1.5f | – |

### Surface In Top And Bottom Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Surface Above Player Enabled | `checkSurfaceAbovePlayerEnabled` | `bool` | true | – |
| Above Player Raycast Offset | `abovePlayerRaycastOffset` | `float` | 0.5f | – |
| Check Surface Below Player Enabled | `checkSurfaceBelowPlayerEnabled` | `bool` | true | – |
| Below Player Raycast Offset | `belowPlayerRaycastOffset` | `float` | -0.2f | – |

### Surface Sides Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Sides Enabled | `checkSidesEnabled` | `bool` | true | – |
| Raycast Distance To Check Sides | `raycastDistanceToCheckSides` | `float` | 0.8f | – |
| Check Close Sides Enabled | `checkCloseSidesEnabled` | `bool` | true | – |
| Raycast Distance To Check Close Sides | `raycastDistanceToCheckCloseSides` | `float` | 0.7f | – |

### Slide Down Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slide Down Enabled | `slideDownEnabled` | `bool` | true | – |
| Slide Down Speed Third Person | `slideDownSpeedThirdPerson` | `float` | 10 | – |
| Slide Down Speed First Person | `SlideDownSpeedFirstPerson` | `float` | 10 | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Movement Curve | `useMovementCurve` | `bool` | true | – |
| Main Movement Curve | `mainMovementCurve` | `AnimationCurve` | – | – |
| Use Velocity Curve | `useVelocityCurve` | `bool` | true | – |
| Main Velocity Curve | `mainVelocityCurve` | `AnimationCurve` | – | – |
| Stop Climb At Min Angle On Surface | `stopClimbAtMinAngleOnSurface` | `bool` | true | – |
| Min Angle To Stop Climb | `minAngleToStopClimb` | `float` | -50 | – |
| Stop Climb At Max Angle On Surface | `stopClimbAtMaxAngleOnSurface` | `bool` | true | – |
| Max Angle To Stop Climb | `maxAngleToStopClimb` | `float` | 50 | – |
| Min Time Angle Limit Reached To Stop Climb | `minTimeAngleLimitReachedToStopClimb` | `float` | 1 | – |
| Disable Climb State On Damage Received Enabled | `disableClimbStateOnDamageReceivedEnabled` | `bool` | – | – |

### Climb Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Climb Movement Speed Third Person | `climbMovementSpeedThirdPerson` | `float` | 5 | – |
| Climb Movement Speed First Person | `climbMovementSpeedFirstPerson` | `float` | 5 | – |
| Climb Velocity Third Person | `climbVelocityThirdPerson` | `float` | 5 | – |
| Climb Velocity First Person | `climbVelocityFirstPerson` | `float` | 5 | – |
| Climb Rotation Speed Third Person | `climbRotationSpeedThirdPerson` | `float` | 200 | – |
| Climb Rotation Speed First Person | `climbRotationSpeedFirstPerson` | `float` | 100 | – |

### Speed Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Climb Turbo Speed | `climbTurboSpeed` | `float` | 2 | – |
| Impulse On Jump | `impulseOnJump` | `Vector3` | – | – |
| Max Velocity Change Slide | `maxVelocityChangeSlide` | `float` | – | – |
| Jump Rotation Speed Third Person | `jumpRotationSpeedThirdPerson` | `float` | 1 | – |
| Jump Rotation Speed First Person | `jumpRotationSpeedFirstPerson` | `float` | 0.5f | – |

### Weapons Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Keep Weapons | `keepWeapons` | `bool` | – | – |
| Draw Weapons If Carried Previously | `drawWeaponsIfCarriedPreviously` | `bool` | – | – |

### Third Person Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Action ID | `actionID` | `int` | 5654231 | – |
| Free Climb Animator Name | `freeClimbAnimatorName` | `string` | "Free Climb" | – |
| Check If Climb Hang On Air For Action | `checkIfClimbHangOnAirForAction` | `bool` | true | – |
| Free Climb Hang From Air Action ID | `freeClimbHangFromAirActionID` | `int` | 5654232 | – |
| Check If Climb Hang On Ground For Action | `checkIfClimbHangOnGroundForAction` | `bool` | true | – |
| Free Climb Hang From Ground Action ID | `freeClimbHangFromGroundActionID` | `int` | 5654233 | – |
| Min Delay To Use Movement Input On Climb Start | `minDelayToUseMovementInputOnClimbStart` | `float` | 0.5f | – |
| External Controlle Behavior Active Animator Name | `externalControlleBehaviorActiveAnimatorName` | `string` | "External Behavior Active" | – |
| Action ID Animator Name | `actionIDAnimatorName` | `string` | "Action ID" | – |
| Horizontal Animator Name | `horizontalAnimatorName` | `string` | "Horizontal Action" | – |
| Vertical Animator Name | `verticalAnimatorName` | `string` | "Vertical Action" | – |
| Input Lerp Speed | `inputLerpSpeed` | `float` | 3 | – |

### Third Person Camera State Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Camera State On Third Person | `setNewCameraStateOnThirdPerson` | `bool` | – | – |
| New Camera State On Third Person | `newCameraStateOnThirdPerson` | `string` | – | – |

### Climb Top Part Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Climb Surface Action System Transform | `climbSurfaceActionSystemTransform` | `Transform` | – | – |
| Max Angle Difference On Surface To Climb | `maxAngleDifferenceOnSurfaceToClimb` | `float` | 20 | – |
| Check Top Surface Raycast Offset | `checkTopSurfaceRaycastOffset` | `float` | 1.3f | – |
| Climb Surface Top Speed | `climbSurfaceTopSpeed` | `float` | 2 | – |
| Event To Activate Climb Surface Action System | `eventToActivateClimbSurfaceActionSystem` | `eventParameters.eventToCallWithGameObject` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Check If Detect Climb Active | `checkIfDetectClimbActive` | `bool` | – | – |
| Climb Active | `climbActive` | `bool` | – | – |
| Is First Person Active | `isFirstPersonActive` | `bool` | – | – |
| Carrying Weapons Previously | `carryingWeaponsPreviously` | `bool` | – | – |
| Climb Paused | `climbPaused` | `bool` | – | – |
| Activate Climb State On Next Surface Detected Active | `activateClimbStateOnNextSurfaceDetectedActive` | `bool` | – | – |
| Sliding Down Active | `slidingDownActive` | `bool` | – | – |
| Activate Auto Slide Down On Surface | `activateAutoSlideDownOnSurface` | `bool` | – | – |
| Sliding Down Result | `slidingDownResult` | `bool` | – | – |
| Player Parent Assigned | `playerParentAssigned` | `bool` | – | – |
| Adjusting Player To Surface Collision Detection | `adjustingPlayerToSurfaceCollisionDetection` | `bool` | – | – |

### Surfaces Detected Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Surface Angle | `surfaceAngle` | `float` | – | – |
| Surface Found On Side | `surfaceFoundOnSide` | `bool` | – | – |
| Surface Found On Close Side | `surfaceFoundOnCloseSide` | `bool` | – | – |
| Surface Found On Regular Raycast | `surfaceFoundOnRegularRaycast` | `bool` | – | – |
| Upper Body Surface Detected | `upperBodySurfaceDetected` | `bool` | – | – |
| Lower Body Surface Detected | `lowerBodySurfaceDetected` | `bool` | – | – |
| Surface Detected Above Player | `surfaceDetectedAbovePlayer` | `bool` | – | – |
| Surfafe Detected Below Player | `surfafeDetectedBelowPlayer` | `bool` | – | – |
| Climb Contact Count | `climbContactCount` | `int` | – | – |
| Contact Normal | `contactNormal` | `Vector3` | – | – |
| Last Climb Normal | `lastClimbNormal` | `Vector3` | – | – |
| Angle Difference With Surface | `angleDifferenceWithSurface` | `float` | – | – |
| Surface Detected On Movement Input Raycast | `surfaceDetectedOnMovementInputRaycast` | `bool` | – | – |

### Movement Input Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Vertical Movement | `currentVerticalMovement` | `float` | – | – |
| Current Horizontal Movement | `currentHorizontalMovement` | `float` | – | – |
| Raw Axis Values | `rawAxisValues` | `Vector2` | – | – |
| Moving | `moving` | `bool` | – | – |
| Movement Input Pressed | `movementInputPressed` | `bool` | – | – |
| Climb State Activated By Input | `climbStateActivatedByInput` | `bool` | – | – |
| Movement Input Paused Active | `movementInputPausedActive` | `bool` | – | – |
| Movement Input Disabled On Surface | `movementInputDisabledOnSurface` | `bool` | – | – |
| Cancel Movement Input Active | `cancelMovementInputActive` | `bool` | – | – |
| Turbo Active | `turboActive` | `bool` | – | – |
| Pause Turbo Active | `pauseTurboActive` | `bool` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |

### First Person Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On First Person | `useEventsOnFirstPerson` | `bool` | – | – |
| Event On Start First Person | `eventOnStartFirstPerson` | `UnityEvent` | – | – |
| Event On End First Person | `eventOnEndFirstPerson` | `UnityEvent` | – | – |

### Third Person Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Third Person | `useEventsOnThirdPerson` | `bool` | – | – |
| Event On Start Third Person | `eventOnStartThirdPerson` | `UnityEvent` | – | – |
| Event On End Third Person | `eventOnEndThirdPerson` | `UnityEvent` | – | – |

### Other Events

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Check For Climb State Active | `eventOnCheckForClimbStateActive` | `UnityEvent` | – | – |
| Event On Stop Check For Climb State Active | `eventOnStopCheckForClimbStateActive` | `UnityEvent` | – | – |
| Event On Climb State Active | `eventOnClimbStateActive` | `UnityEvent` | – | – |
| Event On Stop Climb State Active | `eventOnStopClimbStateActive` | `UnityEvent` | – | – |
| Event Before Checking For Climb State Active | `eventBeforeCheckingForClimbStateActive` | `UnityEvent` | – | – |

### Turbo Events

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Turbo | `useEventOnTurbo` | `bool` | – | – |
| Event On Start Turbo | `eventOnStartTurbo` | `UnityEvent` | – | – |
| Event On End Turbo | `eventOnEndTurbo` | `UnityEvent` | – | – |
| Event On Regular Climb Speed | `eventOnRegularClimbSpeed` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Player Camera Transform | `playerCameraTransform` | `Transform` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |
| Stop Climb To Walk On Surface Action Name | `stopClimbToWalkOnSurfaceActionName` | `string` | "Stop Climb To Walk On Surface" | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateClimbContactCount(int newValue)` | `climbContactCount` を設定するだけ。 |
| `updateContactNormal(Vector3 newValue)` | `contactNormal` を設定するだけ。 |
| `updateLastClimbNormal(Vector3 newValue)` | `lastClimbNormal` を設定するだけ。 |
| `isSlidingDownActive()` | `slidingDownActive` の値を返すだけ。 |
| `isPlayerMoving()` | `moving` の値を返すだけ。 |
| `getCurrentClimbTurboSpeed()` | `currentClimbTurboSpeed` の値を返すだけ。 |
| `isTurboActive()` | `turboActive` の値を返すだけ。 |
| `isPauseTurboActive()` | `pauseTurboActive` の値を返すだけ。 |
| `getCurrentNormal()` | `mainPlayerController.getCurrentNormal` の値をそのまま返す。 |
| `setClimbImpulseForce(Vector3 forceAmount, bool useCameraDirection)` | クランプした速度変化を記録してRigidbodyへ加える（`useCameraDirection` は未使用）。 |
| `stopClimbFromDamageReceived()` | ダメージで停止する設定時のみ、登攀中なら `stopClimbAndDetectState` で登攀を終了する。 |
| `setJumpActive(Vector3 newImpulseOnJumpAmount)` | 登攀中なら解除し、y成分を上・z成分を前方としてジャンプ力を加え、回転処理とカメラリセットを行う。 |
| `setMovementInputDisabledOnSurfaceState(bool state)` | `movementInputDisabledOnSurface` を設定するだけ。 |
| `setCheckIfDetectClimbActiveState(bool state)` | 有効性や使用可否を確認し、検出状態を切り替えて外部ビヘイビア登録・落下ダメージ停止・各種イベントを更新する。 |
| `setClimbActiveState(bool state)` | 登攀状態を切り替え、接地判定・Animator・武器入力・足音・カメラ・親子付け・イベントをまとめて更新する。 |
| `setClimbEnabledState(bool state)` | falseなら登攀と検出を停止し、`climbEnabled` を設定する。 |
| `setClimbCheckCanBeUsedState(bool state)` | `climbCheckCanBeUsed` を設定するだけ。 |
| `setClimbEnabledState()` | `originalClimbEnabled` を渡して `setClimbEnabledState` を呼ぶだけ。 |
| `setOriginalClimbEnabledState()` | 登攀中なら検出を止めた上で、`originalClimbEnabled` に戻す。 |
| `enableCheckIfDetectClimbActiveStateExternally()` | 既に検出中でなければ `setCheckIfDetectClimbActiveState` をtrueで呼ぶ。 |
| `disableCheckIfDetectClimbActiveStateExternally()` | 検出中の場合のみ `setCheckIfDetectClimbActiveState` をfalseで呼ぶ。 |
| `checkEventsOnStateChange(bool state)` | 一人称か三人称かに応じた設定が有効なら、開始/終了イベントを発火する。 |
| `setClimbPausedState(bool state)` | trueなら登攀中でも停止させ、`climbPaused` を設定する。 |
| `rotateCharacterOnJump()` | 既存の回転コルーチンを止めて `rotateCharacterOnJumpCoroutine` を開始する。 |
| `rotateCharacterOnJumpCoroutine()` | 一人称ならカメラ、それ以外はプレイヤーを `jumpRotationSpeed` 基準で目標方向へ補間回転する。 |
| `resetPlayerRotation()` | 既存コルーチンを止めて `resetPlayerRotationCoroutine` を開始する。 |
| `resetCameraRotation()` | 既存コルーチンを止めて `resetCameraRotationCoroutine` を開始する。 |
| `setActivateClimbStateOnNextSurfaceDetectedActiveState(bool state)` | 無視フラグを確認して設定し、前方の面検出コルーチンを開始または停止する。 |
| `stopCheckIfSurfaceDetectedInFrontCoroutine()` | 面検出コルーチンを停止するだけ。 |
| `activateGrabSurface()` | 検出が有効なら登攀開始可否を判定し、次の面検出フラグを解除して登攀状態をトグルする。 |
| `inputSetSlideDownState(bool state)` | 登攀中などの条件を満たすとき `slidingDownActive` を設定し、`currentIDValue` を-1にする。 |
| `inputGrabSurface()` | 入力可否などを確認し、直接登攀設定なら検出のオン/オフ、そうでなければ `activateGrabSurface` を呼ぶ。 |
| `inpuSetIncreaseClimbSpeedState(bool state)` | 各種条件を満たすとき `increaseClimbSpeedActive` を設定するだけ。 |
| `setClimbEnabledStateFromEditor(bool state)` | 有効状態を設定し、コンポーネントを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartFirstPerson` | `UnityEvent` | – |
| `eventOnEndFirstPerson` | `UnityEvent` | – |
| `eventOnStartThirdPerson` | `UnityEvent` | – |
| `eventOnEndThirdPerson` | `UnityEvent` | – |
| `eventOnCheckForClimbStateActive` | `UnityEvent` | – |
| `eventOnStopCheckForClimbStateActive` | `UnityEvent` | – |
| `eventOnClimbStateActive` | `UnityEvent` | – |
| `eventOnStopClimbStateActive` | `UnityEvent` | – |
| `eventBeforeCheckingForClimbStateActive` | `UnityEvent` | – |
| `eventOnStartTurbo` | `UnityEvent` | – |
| `eventOnEndTurbo` | `UnityEvent` | – |
| `eventOnRegularClimbSpeed` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkChangeCameraViewStateOnExternalControllerBehavior()`, `checkIfResumeExternalControllerState()`, `disableExternalControllerState()`, `setCurrentPlayerActionSystemCustomActionCategoryID()`, `setExternalForceActiveState(bool state)`, `setExternalForceEnabledState(bool state)`, `setExtraImpulseForce(Vector3 forceAmount, bool useCameraDirection)`, `setJumpActiveForExternalForce()`, `updateControllerBehavior()`

</details>
