# climbRopeSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `externalControllerBehavior`
- **ソース**: `Player/Extra Movements/climbRopeSystem.cs:6`

**概要**: ロープやパイプを上下に移動する登攀を制御する外部コントローラ。上下端Transform間でプレイヤーを移動させ、ジャンプ・ターボ・親子付け・カメラ状態を切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| System Enabled | `systemEnabled` | `bool` | true | – |
| Look Direction Speed | `lookDirectionSpeed` | `float` | – | – |
| Reset Player Rotation Speed | `resetPlayerRotationSpeed` | `float` | 5 | – |
| Adjust Player To Movement Speed | `adjustPlayerToMovementSpeed` | `float` | 5 | – |
| Movement Up Speed | `movementUpSpeed` | `float` | 5 | – |
| Movement Up Turbo Speed | `movementUpTurboSpeed` | `float` | 10 | – |
| Movement Down Speed | `movementDownSpeed` | `float` | 10 | – |
| Movement Down Turbo Speed | `movementDownTurboSpeed` | `float` | 15 | – |
| Movement Amount Multiplier Up | `movementAmountMultiplierUp` | `float` | 1 | – |
| Movement Amount Multiplier Down | `movementAmountMultiplierDown` | `float` | 1 | – |
| Jump Rotation Speed Third Person | `jumpRotationSpeedThirdPerson` | `float` | 1 | – |
| Jump Rotation Speed First Person | `jumpRotationSpeedFirstPerson` | `float` | 0.5f | – |
| Stop Climb On Top Reached | `stopClimbOnTopReached` | `bool` | – | – |
| Stop C Limb On Bottom Reached | `stopCLimbOnBottomReached` | `bool` | – | – |
| Check Climb Rope Trigger Match System List On Jump | `checkClimbRopeTriggerMatchSystemListOnJump` | `bool` | – | – |
| Min Angle With Climb Rope Trigger Match System | `minAngleWithClimbRopeTriggerMatchSystem` | `float` | – | – |
| Min Distance To Reach Top Or Bottom | `minDistanceToReachTopOrBottom` | `float` | 0.18f | – |

### Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Force Mode | `useForceMode` | `bool` | – | – |
| Rail Force Mode | `railForceMode` | `ForceMode` | – | – |
| Turbo Enabled | `turboEnabled` | `bool` | – | – |
| Speed On Aim Multiplier | `speedOnAimMultiplier` | `float` | – | – |
| Set Main Collider As Trigger On State Active | `setMainColliderAsTriggerOnStateActive` | `bool` | – | – |

### Jump Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Jump Enabled | `canJumpEnabled` | `bool` | – | – |
| Impulse On Jump | `impulseOnJump` | `Vector3` | – | – |
| End Of Surface Top Impulse | `endOfSurfaceTopImpulse` | `Vector3` | – | – |
| End Of Surface Bottom Impulse | `endOfSurfaceBottomImpulse` | `Vector3` | – | – |
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
| Movement Paused Debug | `movementPausedDebug` | `bool` | – | – |
| Movement System Active | `movementSystemActive` | `bool` | – | – |
| Turbo Active | `turboActive` | `bool` | – | – |
| Target Direction | `targetDirection` | `Vector3` | – | – |
| Adjusting Player To Movement | `adjustingPlayerToMovement` | `bool` | – | – |
| Moving On Forward Direction | `movingOnForwardDirection` | `bool` | – | – |
| Moving On Backward Direction | `movingOnBackwardDirection` | `bool` | – | – |
| Vertical Input | `verticalInput` | `float` | – | – |
| Horizontal Input | `horizontalInput` | `float` | – | – |
| Movement Direction Multiplier | `movementDirectionMultiplier` | `float` | 1 | – |
| Moving Up | `movingUp` | `bool` | – | – |
| Moving Down | `movingDown` | `bool` | – | – |
| Rotating Horizontally | `rotatingHorizontally` | `bool` | – | – |
| Set Player As Child Active | `setPlayerAsChildActive` | `bool` | – | – |
| Player Parent Transform | `playerParentTransform` | `Transform` | – | – |
| Bottom Transform | `bottomTransform` | `Transform` | – | – |
| Top Transform | `topTransform` | `Transform` | – | – |
| Climb Rope Trigger Match System List | `climbRopeTriggerMatchSystemList` | `List<climbRopeTriggerMatchSystem>` | new List<climbRopeTriggerMatchSystem> () | – |

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
| `setImpulseForce(Vector3 forceAmount, bool useCameraDirection)` | クランプした速度をプレイヤーに記録してRigidbodyへ加える（`useCameraDirection` は未使用）。 |
| `setJumpActive(Vector3 newImpulseOnJumpAmount)` | 移動システム中なら停止し、近接するトリガーへの方向も考慮したジャンプ力を加えて回転を開始する。 |
| `setMovementSystemActivestate(bool state)` | 有効性や死亡などを確認し、移動状態・外部ビヘイビア登録・接地/Animator・カメラ・親子付け・イベントを切り替える。 |
| `setMovementEnabledState(bool state)` | falseなら移動システムを停止させ、`systemEnabled` を設定する。 |
| `enableOrDisableTurbo(bool state)` | 状態が変わる場合に `turboActive` を設定し、開始/終了イベントとカメラ揺れの停止を処理する。 |
| `setCanUseTurboPausedState(bool state)` | falseでターボ中ならターボを止め、`canUseTurboPausedState` を設定する。 |
| `inputChangeTurboState(bool state)` | 移動中かつターボ有効なら `enableOrDisableTurbo` を呼ぶ。 |
| `setTransformElements(Transform newBottomTransform, Transform newTopTransform)` | 下端と上端のTransformを設定するだけ。 |
| `setSetPlayerAsChildStateState(bool state, Transform newPlayerParentTransform)` | 親子付けフラグと親Transformを設定するだけ。 |
| `setCurrentClimbRopeTriggerSystem(climbRopeTriggerSystem newClimbRopeTriggerSystem)` | `currentClimbRopeTriggerSystem` を設定するだけ。 |
| `adjustPlayerToMovementOnStart(Vector3 initialPosition, Vector3 movementDirection)` | 既存コルーチンを止め、開始位置と移動方向で位置・回転を補間するコルーチンを開始する。 |
| `resetPlayerRotation()` | 既存コルーチンを止めて `resetPlayerRotationCoroutine` を開始する。 |
| `rotateCharacterOnJump()` | 既存コルーチンを止めて `rotateCharacterOnJumpCoroutine` を開始する。 |
| `rotateCharacterOnJumpCoroutine()` | `currentDirectionToRotatePlayer` 方向へプレイヤーかカメラを補間回転し、必要なら回転リセットする。 |
| `addClimbRopeTriggerMatchSystem(climbRopeTriggerMatchSystem newClimbRopeTriggerMatchSystem)` | 未登録なら `climbRopeTriggerMatchSystemList` に追加するだけ。 |
| `removeClimbRopeTriggerMatchSystem(climbRopeTriggerMatchSystem newClimbRopeTriggerMatchSystem)` | 登録済みならリストから削除するだけ。 |
| `setNewClimbActionID(int newValue)` | `actionID` を設定するだけ。 |
| `setOriginalClimbActionID()` | `originalActionID` に戻すだけ。 |

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
