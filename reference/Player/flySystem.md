# flySystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `externalControllerBehavior`
- **ソース**: `Player/Extra Movements/flySystem.cs:6`

**概要**: 空中を自由に飛ぶ飛行モードを提供する `externalControllerBehavior`。上下移動、ターボ、ダッシュID、IK、カメラFOV、COM回転のリセットを扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fly Mode Enabled | `flyModeEnabled` | `bool` | true | – |
| Fly Force | `flyForce` | `float` | – | – |
| Air Friction | `airFriction` | `float` | 5 | – |
| Max Fly Velocity | `maxFlyVelocity` | `float` | 50 | – |
| Fly Horizontal Speed Multiplier | `flyHorizontalSpeedMultiplier` | `float` | 1 | – |
| Fly Vertical Speed Multiplier | `flyVerticalSpeedMultiplier` | `float` | 2 | – |
| Use Force Mode | `useForceMode` | `bool` | true | – |
| Fly Force Mode | `flyForceMode` | `ForceMode` | – | – |

### Vertical Movement Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Move Up And Down Enabled | `moveUpAndDownEnabled` | `bool` | true | – |
| Fly Move Up Speed | `flyMoveUpSpeed` | `float` | 2 | – |
| Fly Move Down Speed | `flyMoveDownSpeed` | `float` | 2 | – |

### Dash Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Dash ID | `setNewDashID` | `bool` | – | – |
| New Dash ID | `newDashID` | `int` | – | – |

### Turbo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Turbo Enabled | `turboEnabled` | `bool` | true | – |
| Fly Turbo Speed | `flyTurboSpeed` | `float` | – | – |

### Locked Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Fly Movement Direction Locked Camera | `useCustomFlyMovementDirectionLockedCamera` | `bool` | – | – |
| Custom Fly Movement Direction Locked Camera | `customFlyMovementDirectionLockedCamera` | `Transform` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fly Rotation Speed Toward Camera Direction | `flyRotationSpeedTowardCameraDirection` | `float` | 10 | – |
| Fly Speed On Aim Multiplier | `flySpeedOnAimMultiplier` | `float` | 0.5f | – |
| Shake Camera State Name | `shakeCameraStateName` | `string` | "Use Fly Turbo" | – |

### Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Regular Air ID | `regularAirID` | `int` | -1 | – |
| Flying ID | `flyingID` | `int` | 4 | – |
| Flying Mode Name | `flyingModeName` | `string` | "Flying Mode" | – |
| Use IK Flying | `useIKFlying` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fly Mode Active | `flyModeActive` | `bool` | – | – |
| Turbo Active | `turboActive` | `bool` | – | – |
| Player Is Moving | `playerIsMoving` | `bool` | – | – |
| Moving Up | `movingUp` | `bool` | – | – |
| Moving Down | `movingDown` | `bool` | – | – |
| Velocity Magnitude | `velocityMagnitude` | `float` | – | – |
| Fly Forces Paused | `flyForcesPaused` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On State Enabled | `eventOnStateEnabled` | `UnityEvent` | – | – |
| Event On State Disabled | `eventOnStateDisabled` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| IK Manager | `IKManager` | `IKSystem` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Player Camera Transform | `playerCameraTransform` | `Transform` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Main Dash System | `mainDashSystem` | `dashSystem` | – | – |
| COM | `COM` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableFlyingMode(bool state)` | 飛行状態を切り替え、外部コントローラ、IK、airID、ダッシュ、イベント、COM回転を更新する。 |
| `enableOrDisableTurbo(bool state)` | ターボを設定し、飛行ターボ、カメラFOV、カメラシェイク、空中速度IDを切り替える。 |
| `resetCOMRotation()` | 既存のCOM回転コルーチンを止め、`resetCOMRotationCoroutine` を開始する。 |
| `resetCOMRotationCoroutine()` | `COM` のローカル回転を identity へ Slerp で徐々に戻す。 |
| `inputChangeTurboState(bool state)` | 飛行中かつターボ有効なら `enableOrDisableTurbo` を呼ぶ。 |
| `inputMoveUp(bool state)` | 飛行中かつ上下移動が有効なら `enableOrDisableVerticalMovementUp` を呼ぶ。 |
| `inputMoveDown(bool state)` | 飛行中かつ上下移動が有効なら `enableOrDisableVerticalMovementDown` を呼ぶ。 |
| `setFlyModeEnabledState(bool state)` | 飛行中なら解除してから `flyModeEnabled` を設定する。 |
| `setOriginalFlyModeEnabledState()` | 保存値 `originalFlyModeEnabled` で `setFlyModeEnabledState` を呼ぶだけ。 |
| `setEnableExternalForceOnFlyModeState(bool state)` | 飛行中のみプレイヤーへ外部力設定を転送する。 |
| `setFlyModeEnabledStateFromEditor(bool state)` | 値を設定してから `updateComponent` を呼ぶ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStateEnabled` | `UnityEvent` | – |
| `eventOnStateDisabled` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkPauseStateDuringExternalForceOrBehavior()`, `checkResumeStateAfterExternalForceOrBehavior()`, `disableExternalControllerState()`, `setCurrentPlayerActionSystemCustomActionCategoryID()`, `updateControllerBehavior()`

</details>
