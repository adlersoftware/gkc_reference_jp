# wallRunningSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `externalControllerBehavior`
- **ソース**: `Player/Extra Movements/wallRunningSystem.cs:6`

**概要**: 壁に沿って走るウォールランニングを提供する `externalControllerBehavior`。左右の壁判定、ジャンプ用インパルス、アニメーション、カメラ状態、COM補正を管理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Wall Running Enabled | `wallRunningEnabled` | `bool` | true | – |
| Raycast Layermask | `raycastLayermask` | `LayerMask` | – | – |
| Wall Running Speed | `wallRunningSpeed` | `float` | – | – |
| Wall Sprint Speed | `wallSprintSpeed` | `float` | – | – |
| Wall Running Rotation Speed | `wallRunningRotationSpeed` | `float` | – | – |
| Wall Running Can Be Used | `wallRunningCanBeUsed` | `bool` | true | – |
| Wall Running Impulse On Jump | `wallRunningImpulseOnJump` | `Vector3` | – | – |
| Wall Running Stop Movemment Impulse | `wallRunningStopMovemmentImpulse` | `Vector3` | – | – |
| Wall Running End Of Surface Impulse | `wallRunningEndOfSurfaceImpulse` | `Vector3` | – | – |
| Wall Running Impulse On Jump Camera Direction | `wallRunningImpulseOnJumpCameraDirection` | `Vector3` | – | – |
| Raycast Distance | `raycastDistance` | `float` | 0.6f | – |

### 2.5d Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Raycast Distance2 5d | `raycastDistance2_5d` | `float` | 2 | – |
| Min Wait Time To Adhere To Wall After Last Time2 5d | `minWaitTimeToAdhereToWallAfterLastTime2_5d` | `float` | 1 | – |
| Wall Running Impulse On Jump2 5d | `wallRunningImpulseOnJump2_5d` | `Vector3` | new Vector3 (5, 8, 10) | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check For Obstacles In Front | `checkForObstaclesInFront` | `bool` | true | – |
| Raycast Distance Obstacles In Front | `raycastDistanceObstaclesInFront` | `float` | 1 | – |
| Min Angle For Obstacles In Front | `minAngleForObstaclesInFront` | `float` | 5 | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Down Movement On Wall Running | `useDownMovementOnWallRunning` | `bool` | – | – |
| Down Movement On Wall Running Amount | `downMovementOnWallRunningAmount` | `float` | – | – |
| Delay Down Movement On Wall Running | `delayDownMovementOnWallRunning` | `float` | – | – |
| Use Up And Down Movement On Wall Running | `useUpAndDownMovementOnWallRunning` | `bool` | – | – |
| Up And Down Movement On Wall Running Delay | `upAndDownMovementOnWallRunningDelay` | `float` | – | – |
| Up And Down Movement On Wall Running Amount | `upAndDownMovementOnWallRunningAmount` | `float` | – | – |
| Use Stop Wall Runnig After Delay | `useStopWallRunnigAfterDelay` | `bool` | – | – |
| Stop Wall Running Delay | `stopWallRunningDelay` | `float` | – | – |
| Use Surface Angle Diff To Jump In Camera Direction | `useSurfaceAngleDiffToJumpInCameraDirection` | `bool` | – | – |
| Surface Angle Diff Range To Wall Running | `surfaceAngleDiffRangeToWallRunning` | `Vector2` | – | – |
| Max Velocity Change Wall Running | `maxVelocityChangeWallRunning` | `float` | – | – |
| Keep Weapons On Wall Running | `keepWeaponsOnWallRunning` | `bool` | – | – |
| Draw Weapons If Carried Previously | `drawWeaponsIfCarriedPreviously` | `bool` | – | – |

### Third Person Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Wall Running Right Action Name | `wallRunningRightActionName` | `string` | "Wall Running Right" | – |
| Wall Runnig Left Action Name | `wallRunnigLeftActionName` | `string` | "Wall Running Left" | – |
| Action Active Animator Name | `actionActiveAnimatorName` | `string` | "Action Active" | – |
| Use Character COM Offset | `useCharacterCOMOffset` | `bool` | true | – |
| Rotation Offset On Character COM | `rotationOffsetOnCharacterCOM` | `float` | 10 | – |
| Position Offset On Character COM | `positionOffsetOnCharacterCOM` | `float` | 0.15f | – |
| Offset Adjustment Speed | `offsetAdjustmentSpeed` | `float` | 5 | – |
| Player Rotation To Surface Speed Third Person | `playerRotationToSurfaceSpeedThirdPerson` | `float` | 14 | – |
| Player Rotation To Surface Speed First Person | `playerRotationToSurfaceSpeedFirstPerson` | `float` | 14 | – |
| Player Rotation To Surface Speed FBA | `playerRotationToSurfaceSpeedFBA` | `float` | 3 | – |

### Third Person Camera State Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Camera State On Third Person | `setNewCameraStateOnThirdPerson` | `bool` | – | – |
| New Camera State On Third Person Right Side | `newCameraStateOnThirdPersonRightSide` | `string` | – | – |
| New Camera State On Third Person Left Side | `newCameraStateOnThirdPersonLeftSide` | `string` | – | – |

### Ignore Surface Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Tags To Ignore | `useTagsToIgnore` | `bool` | – | – |
| Tags To Ignore | `tagsToIgnore` | `List<string>` | new List<string> () | – |
| Ignore Rigidbodies | `ignoreRigidbodies` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Wall Running Active | `wallRunningActive` | `bool` | – | – |
| Is First Person Active | `isFirstPersonActive` | `bool` | – | – |
| Wall Running On Right Side | `wallRunningOnRightSide` | `bool` | – | – |
| Wall Running On Left Side | `wallRunningOnLeftSide` | `bool` | – | – |
| Carrying Weapons Previously | `carryingWeaponsPreviously` | `bool` | – | – |
| Current Movement Direction | `currentMovementDirection` | `Vector3` | – | – |
| Extra Y Position | `extraYPosition` | `float` | – | – |
| Player Y Position On Wall Running Start | `playerYPositionOnWallRunningStart` | `float` | – | – |
| Player Velocity | `playerVelocity` | `Vector3` | – | – |
| Check Surface Detected | `checkSurfaceDetected` | `bool` | true | – |
| Is Player Moving On3d World | `isPlayerMovingOn3dWorld` | `bool` | – | – |

### First Person Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Wall Running Start First Person | `eventOnWallRunningStartFirstPerson` | `UnityEvent` | – | – |
| Event On Wall Running To Right First Person | `eventOnWallRunningToRightFirstPerson` | `UnityEvent` | – | – |
| Event On Wall Running To Left First Person | `eventOnWallRunningToLeftFirstPerson` | `UnityEvent` | – | – |
| Event On Wall Running End First Person | `eventOnWallRunningEndFirstPerson` | `UnityEvent` | – | – |

### Third Person Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Wall Running Start Third Person | `eventOnWallRunningStartThirdPerson` | `UnityEvent` | – | – |
| Event On Wall Running To Right Third Person | `eventOnWallRunningToRightThirdPerson` | `UnityEvent` | – | – |
| Event On Wall Running To Left Third Person | `eventOnWallRunningToLeftThirdPerson` | `UnityEvent` | – | – |
| Event On Wall Running End Third Person | `eventOnWallRunningEndThirdPerson` | `UnityEvent` | – | – |

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
| COM | `COM` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setWallRunningImpulseForce(Vector3 forceAmount, bool useCameraDirection)` | カメラまたはプレイヤーの前/上/右方向で力を合成し、左右で符号を変えてクランプした速度変更を適用する。 |
| `setJumpActive()` | 壁走り中ならジャンプ用インパルスを適用し、現在速度を保存して壁走り状態を解除する。 |
| `setWallRunningActiveState(bool state)` | 壁走り状態を切り替え、アニメーションと左右別イベント、武器入力、カメラ状態、足音、COM補正を更新する。 |
| `setWallRunningEnabledState(bool state)` | false かつ壁走り中なら解除して停止インパルスを加え、左右フラグを初期化してから有効状態を設定する。 |
| `setWallRunningCanBeUsedState(bool state)` | `wallRunningCanBeUsed` を設定するだけ。 |
| `setOriginalWallRunningEnabledState()` | 保存値 `originalWallRunningEnabled` で有効状態を戻す。 |
| `setAutoUseDownMovementOnWallRunningActiveState(bool state)` | `autoUseDownMovementOnWallRunningActive` を設定するだけ。 |
| `setAutoUseStopWallRunningAfterDelayState(bool state)` | `autoUseStopWallRunningAfterDelay` を設定するだけ。 |
| `resetCOMRotation()` | COM回転コルーチンを止め、`resetCOMRotationCoroutine` を開始する。 |
| `resetCOMRotationCoroutine()` | `COM` を元の位置と回転へ Slerp で戻し、必要なら遅延後に武器を描画する。 |
| `setWallRunningEnabledStateFromEditor(bool state)` | 値を設定してから `updateComponent` を呼ぶ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnWallRunningStartFirstPerson` | `UnityEvent` | – |
| `eventOnWallRunningToRightFirstPerson` | `UnityEvent` | – |
| `eventOnWallRunningToLeftFirstPerson` | `UnityEvent` | – |
| `eventOnWallRunningEndFirstPerson` | `UnityEvent` | – |
| `eventOnWallRunningStartThirdPerson` | `UnityEvent` | – |
| `eventOnWallRunningToRightThirdPerson` | `UnityEvent` | – |
| `eventOnWallRunningToLeftThirdPerson` | `UnityEvent` | – |
| `eventOnWallRunningEndThirdPerson` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkIfActivateExternalForce()`, `disableExternalControllerState()`, `setCurrentPlayerActionSystemCustomActionCategoryID()`, `setExternalForceActiveState(bool state)`, `setExternalForceEnabledState(bool state)`, `setExtraImpulseForce(Vector3 forceAmount, bool useCameraDirection)`, `setJumpActiveForExternalForce()`, `updateControllerBehavior()`

</details>
