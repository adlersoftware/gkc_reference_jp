# railSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `externalControllerBehavior`
- **ソース**: `Player/Extra Movements/railSystem.cs:6`

**概要**: ベジェスプラインに沿って移動するレールモードを提供する `externalControllerBehavior`。レール状態、ターボ、進行方向の反転可否、開始位置への調整を管理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Rail System Enabled | `railSystemEnabled` | `bool` | true | – |
| Look Direction Speed | `lookDirectionSpeed` | `float` | – | – |
| Reset Player Rotation Speed | `resetPlayerRotationSpeed` | `float` | 5 | – |
| Adjust Player To Rail Speed | `adjustPlayerToRailSpeed` | `float` | 5 | – |

### Reverse Direction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Change Direction Enabled | `canChangeDirectionEnabled` | `bool` | – | – |
| Min Wait To Change Direction | `minWaitToChangeDirection` | `float` | 0.8f | – |
| Delay To Reverse Direction | `delayToReverseDirection` | `float` | 1 | – |
| Delay To Resume Movement On Reverse Direction | `delayToResumeMovementOnReverseDirection` | `float` | 0.5f | – |
| Reduce Slide Speed On Reversing Direction | `reduceSlideSpeedOnReversingDirection` | `bool` | – | – |
| Reduce Slide Speed On Reversing Direction Multiplier | `reduceSlideSpeedOnReversingDirectionMultiplier` | `float` | 0.2f | – |

### Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Force Mode | `useForceMode` | `bool` | – | – |
| Rail Force Mode | `railForceMode` | `ForceMode` | – | – |
| Turbo Enabled | `turboEnabled` | `bool` | – | – |
| Turbo Speed | `turboSpeed` | `float` | – | – |
| Speed On Aim Multiplier | `speedOnAimMultiplier` | `float` | – | – |

### Speed Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Adjust Speed Based On Inclination | `adjustSpeedBasedOnInclination` | `bool` | – | – |
| Speed Multiplier On Inclination Up | `speedMultiplierOnInclinationUp` | `float` | – | – |
| Speed Multiplier On Inclination Down | `speedMultiplierOnInclinationDown` | `float` | – | – |
| Min Inclination Difference To Affect Speed | `minInclinationDifferenceToAffectSpeed` | `float` | – | – |
| Speed Multiplier On Inclination Lerp | `speedMultiplierOnInclinationLerp` | `float` | – | – |

### Jump Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Jump Enabled | `canJumpEnabled` | `bool` | – | – |
| Impulse On Jump | `impulseOnJump` | `Vector3` | – | – |
| End Of Surface Impulse | `endOfSurfaceImpulse` | `Vector3` | – | – |
| Max Velocity Change On Jump | `maxVelocityChangeOnJump` | `float` | – | – |

### Third Person Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Action ID | `actionID` | `int` | 08632946 | – |
| External Controlle Behavior Active Animator Name | `externalControlleBehaviorActiveAnimatorName` | `string` | "External Behavior Active" | – |
| Action ID Animator Name | `actionIDAnimatorName` | `string` | "Action ID" | – |
| Horizontal Animator Name | `horizontalAnimatorName` | `string` | "Horizontal Action" | – |
| Input Lerp Speed | `inputLerpSpeed` | `float` | 3 | – |

### Third Person Camera State Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Camera State On Third Person | `setNewCameraStateOnThirdPerson` | `bool` | – | – |
| New Camera State On Third Person | `newCameraStateOnThirdPerson` | `string` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Movement On Rail Paused Debug | `movementOnRailPausedDebug` | `bool` | – | – |
| Rail System Active | `railSystemActive` | `bool` | – | – |
| Bezier Duration | `bezierDuration` | `float` | – | – |
| Turbo Active | `turboActive` | `bool` | – | – |
| Target Direction | `targetDirection` | `Vector3` | – | – |
| Current Spline | `currentSpline` | `BezierSpline` | – | – |
| Moving Forward | `movingForward` | `bool` | – | – |
| Adjusting Player To Rail | `adjustingPlayerToRail` | `bool` | – | – |
| Progress | `progress` | `float` | 0 | – |
| Progress Target | `progressTarget` | `float` | 0 | – |
| Player Aiming | `playerAiming` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On State Enabled | `eventOnStateEnabled` | `UnityEvent` | – | – |
| Event On State Disabled | `eventOnStateDisabled` | `UnityEvent` | – | – |
| Event Before Activating State | `eventBeforeActivatingState` | `UnityEvent` | – | – |
| Event Before Deactivating State | `eventBeforeDeactivatingState` | `UnityEvent` | – | – |
| Use Event Use Turbo | `useEventUseTurbo` | `bool` | – | – |
| Event On Star Turbo | `eventOnStarTurbo` | `UnityEvent` | – | – |
| Event On End Turbo | `eventOnEndTurbo` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Player Camera Transform | `playerCameraTransform` | `Transform` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setImpulseForce(Vector3 forceAmount, bool useCameraDirection)` | 最大速度変更量を計算しつつ、実際は `impulseForce` をそのまま `AddForce` で速度変更として適用する。 |
| `setJumpActive(Vector3 newImpulseOnJumpAmount)` | レール中なら解除し、上方向と前方向を合成したインパルスでジャンプさせる。 |
| `setRailSystemActivestate(bool state)` | レール状態を切り替え、接地判定・アニメーション・カメラ・頭追従・各種イベント・ターボ解除まで更新する。 |
| `setRailEnabledState(bool state)` | false ならレールを解除してから `railSystemEnabled` を設定する。 |
| `enableOrDisableTurbo(bool state)` | ターボ状態を切り替え、使用時は開始/終了イベントを送出する。 |
| `setCanUseTurboPausedState(bool state)` | false でターボ中なら解除し、`canUseTurboPausedState` を設定する。 |
| `inputChangeTurboState(bool state)` | レール中かつターボ有効なら `enableOrDisableTurbo` を呼ぶ。 |
| `setCanChangeDirectionEnabledState(bool state)` | `canChangeDirectionEnabled` を設定するだけ。 |
| `setOriginalCanChangeDirectionEnabled()` | 保存値 `originalCanChangeDirectionEnabled` で方向反転設定を戻す。 |
| `setCurrentSpline(BezierSpline newSpline)` | `currentSpline` を設定するだけ。 |
| `setCurrentBezierDuration(float newValue)` | `bezierDuration` を設定するだけ。 |
| `adjustPlayerToRailOnStart(Vector3 initialPosition)` | 既存の回転コルーチンを止め、`adjustPlayerToRailOnStartCoroutine` を開始する。 |
| `resetPlayerRotation()` | 既存の回転コルーチンを止め、`resetPlayerRotationCoroutine` を開始する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStateEnabled` | `UnityEvent` | – |
| `eventOnStateDisabled` | `UnityEvent` | – |
| `eventBeforeActivatingState` | `UnityEvent` | – |
| `eventBeforeDeactivatingState` | `UnityEvent` | – |
| `eventOnStarTurbo` | `UnityEvent` | – |
| `eventOnEndTurbo` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`disableExternalControllerState()`, `setCurrentPlayerActionSystemCustomActionCategoryID()`, `setExternalForceActiveState(bool state)`, `setExternalForceEnabledState(bool state)`, `setExtraImpulseForce(Vector3 forceAmount, bool useCameraDirection)`, `setJumpActiveForExternalForce()`, `updateControllerBehavior()`

</details>
