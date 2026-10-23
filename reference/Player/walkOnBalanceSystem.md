# walkOnBalanceSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `externalControllerBehavior`
- **ソース**: `Player/Extra Movements/walkOnBalanceSystem.cs:6`

**概要**: 細い足場の上をウェイポイントに沿って歩くバランス移動モードを提供する `externalControllerBehavior`。開始時に最寄り地点と進行方向を決め、ターボやプレイヤーの子化も扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| System Enabled | `systemEnabled` | `bool` | true | – |
| Look Direction Speed | `lookDirectionSpeed` | `float` | – | – |
| Look Direction Speed FBA | `lookDirectionSpeedFBA` | `float` | 10 | – |
| Reset Player Rotation Speed | `resetPlayerRotationSpeed` | `float` | 5 | – |
| Adjust Player To Movement Speed | `adjustPlayerToMovementSpeed` | `float` | 5 | – |
| Movement Speed | `movementSpeed` | `float` | 5 | – |
| Turbo Speed | `turboSpeed` | `float` | 4 | – |
| Delay To Resume Movement On Reverse Direction | `delayToResumeMovementOnReverseDirection` | `float` | 0.7f | – |
| Stop Movement If Last Point Reached | `stopMovementIfLastPointReached` | `bool` | true | – |
| Stop Movement If First Point Reached | `stopMovementIfFirstPointReached` | `bool` | true | – |

### Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Force Mode | `useForceMode` | `bool` | – | – |
| Rail Force Mode | `railForceMode` | `ForceMode` | – | – |
| Turbo Enabled | `turboEnabled` | `bool` | – | – |
| Speed On Aim Multiplier | `speedOnAimMultiplier` | `float` | – | – |

### Jump Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Jump Enabled | `canJumpEnabled` | `bool` | – | – |
| Jump On End State Enabled | `jumpOnEndStateEnabled` | `bool` | true | – |
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

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fall After Delay If Not Moving | `fallAfterDelayIfNotMoving` | `bool` | – | – |
| Delay To Fall If Not Moving | `delayToFallIfNotMoving` | `float` | – | – |
| Fall After Delay If Moving | `fallAfterDelayIfMoving` | `bool` | – | – |
| Delay To Fall If Moving | `delayToFallIfMoving` | `float` | – | – |
| Action ID To Fall | `actionIDToFall` | `int` | 4548931 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Movement Paused Debug | `movementPausedDebug` | `bool` | – | – |
| Movement System Active | `movementSystemActive` | `bool` | – | – |
| Turbo Active | `turboActive` | `bool` | – | – |
| Target Direction | `targetDirection` | `Vector3` | – | – |
| Current Target Direction | `currentTargetDirection` | `Vector3` | – | – |
| Adjusting Player To Movement | `adjustingPlayerToMovement` | `bool` | – | – |
| Moving On Forward Direction | `movingOnForwardDirection` | `bool` | – | – |
| Moving On Backward Direction | `movingOnBackwardDirection` | `bool` | – | – |
| Current Waypoint Index | `currentWaypointIndex` | `int` | – | – |
| Next Target Waypoint Index | `nextTargetWaypointIndex` | `int` | – | – |
| Vertical Input | `verticalInput` | `float` | – | – |
| Movement Direction Multiplier | `movementDirectionMultiplier` | `float` | 1 | – |
| Jump On End State | `jumpOnEndState` | `bool` | – | – |
| Current Simple Waypoint System | `currentSimpleWaypointSystem` | `simpleWaypointSystem` | – | – |
| Current Way Points | `currentWayPoints` | `List<Transform>` | new List<Transform> () | – |

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
| `setImpulseForce(Vector3 forceAmount, bool useCameraDirection)` | 最大速度変更量を計算しつつ、実際は `impulseForce` をそのまま速度変更として `AddForce` に渡す。 |
| `setJumpActive(Vector3 newImpulseOnJumpAmount)` | 移動モード中なら解除し、上方向と前方向を合成したインパルスでジャンプさせる。 |
| `setMovementSystemActivestate(bool state)` | バランス移動状態を切り替え、開始時は最寄りウェイポイントと進行方向を算出し、接地判定・カメラ・イベント・子化まで更新する。 |
| `setMovementEnabledState(bool state)` | false なら移動モードを解除してから `systemEnabled` を設定する。 |
| `enableOrDisableTurbo(bool state)` | ターボ状態を切り替え、使用時は開始/終了イベントを送出し、解除時はカメラシェイクを止める。 |
| `setCanUseTurboPausedState(bool state)` | false でターボ中なら解除し、`canUseTurboPausedState` を設定する。 |
| `inputChangeTurboState(bool state)` | 移動モード中かつターボ有効なら `enableOrDisableTurbo` を呼ぶ。 |
| `setCurrentWaypoint(simpleWaypointSystem newSimpleWaypointSystem)` | ウェイポイントシステムを設定し、null でなければその `wayPoints` を取得する。 |
| `adjustPlayerToMovementOnStart(Vector3 initialPosition)` | 既存の回転コルーチンを止め、`adjustPlayerToMovementOnStartCoroutine` を開始する。 |
| `resetPlayerRotation()` | 既存の回転コルーチンを止め、`resetPlayerRotationCoroutine` を開始する。 |
| `getClosestPosition(Vector3 position)` | 最も近いウェイポイントを探して `currentWaypointIndex` を更新し、その位置を返す。 |
| `setSetPlayerAsChildStateState(bool state, Transform newPlayerParentTransform)` | `setPlayerAsChildActive` と `playerParentTransform` を設定するだけ。 |
| `setJumpOnEndState(bool state)` | `jumpOnEndState` を設定するだけ。 |

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
