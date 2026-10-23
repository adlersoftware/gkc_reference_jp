# playerTeleportSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `abilityInfo`
- **ソース**: `Abilities System/Custom Abilities/playerTeleportSystem.cs:8`

**概要**: プレイヤーのテレポート能力。照準した地点への移動、操作とカメラFOVの制御、フック対象への移動を扱う。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Teleporting Enabled | `teleportingEnabled` | `bool` | – | – |
| Teleport Layer Mask | `teleportLayerMask` | `LayerMask` | – | – |
| Max Distance To Teleport | `maxDistanceToTeleport` | `float` | 100 | – |
| Use Teleport If Surface Not Found | `useTeleportIfSurfaceNotFound` | `bool` | true | – |
| Max Distance To Teleport Air | `maxDistanceToTeleportAir` | `float` | 10 | – |
| Hold Button Time To Activate Teleport | `holdButtonTimeToActivateTeleport` | `float` | 0.4f | – |
| Stop Teleport If Moving | `stopTeleportIfMoving` | `bool` | – | – |
| Add Force If Teleport Stops | `addForceIfTeleportStops` | `bool` | – | – |
| Force If Teleport Stops | `forceIfTeleportStops` | `float` | – | – |
| Can Teleport On Zero Gravity | `canTeleportOnZeroGravity` | `bool` | – | – |
| Teleport Instantly To Position | `teleportInstantlyToPosition` | `bool` | – | – |
| Use Fixed Teleport Hook Points Enabled | `useFixedTeleportHookPointsEnabled` | `bool` | true | – |

### Capsule Cast Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Capsule Cast To Check Target Reached | `useCapsuleCastToCheckTargetReached` | `bool` | true | – |
| Capsule Cast Radius | `capsuleCastRadius` | `float` | 0.5f | – |
| Max Capsule Cast Distance | `maxCapsuleCastDistance` | `float` | 1.3f | – |

### Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Smooth Camera Follow State On Teleport | `useSmoothCameraFollowStateOnTeleport` | `bool` | true | – |
| Smooth Camera Follow Duration | `smoothCameraFollowDuration` | `float` | 3 | – |
| Allow Quick Teleport If Lockon Target Active | `allowQuickTeleportIfLockonTargetActive` | `bool` | – | – |
| Check Lockon Targets Layermask | `checkLockonTargetsLayermask` | `LayerMask` | – | – |

### Movement/Rotation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Teleport Speed | `teleportSpeed` | `float` | 10 | – |
| Rotate Toward Teleport Position | `rotateTowardTeleportPosition` | `bool` | – | – |
| Teleport Rotation Speed | `teleportRotationSpeed` | `float` | 5 | – |
| Min Angle To Rotate Toward Teleport Direction | `minAngleToRotateTowardTeleportDirection` | `float` | 15 | – |

### Effect Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Bullet Time On Teleport | `useBulletTimeOnTeleport` | `bool` | – | – |
| Bullet Time Scale On Teleport | `bulletTimeScaleOnTeleport` | `float` | 0.5f | – |
| Use Teleport Mark | `useTeleportMark` | `bool` | – | – |
| Change Camera Fov On Teleport | `changeCameraFovOnTeleport` | `bool` | – | – |
| Camera Fov On Teleport | `cameraFovOnTeleport` | `float` | – | – |
| Camera Fov On Teleport Speed | `cameraFovOnTeleportSpeed` | `float` | – | – |

### Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Action System On Teleport | `useActionSystemOnTeleport` | `bool` | true | – |
| Action Name Used On Teleport | `actionNameUsedOnTeleport` | `string` | "Teleport Pose" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Teleport Can Be Executed | `teleportCanBeExecuted` | `bool` | – | – |
| Searching For Teleport | `searchingForTeleport` | `bool` | – | – |
| Teleport Surface Found | `teleportSurfaceFound` | `bool` | – | – |
| Teleport In Process | `teleportInProcess` | `bool` | – | – |
| Current Teleport Hook Target | `currentTeleportHookTarget` | `Transform` | – | – |
| Teleport Activate By Hook Target | `teleportActivateByHookTarget` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Start Teleport | `useEventsOnStartTeleport` | `bool` | – | – |
| Events On Start Teleport | `eventsOnStartTeleport` | `UnityEvent` | – | – |
| Use Events On End Teleport | `useEventsOnEndTeleport` | `bool` | – | – |
| Events On End Teleport | `eventsOnEndTeleport` | `UnityEvent` | – | – |

### Component Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Teleport Mark | `teleportMark` | `GameObject` | – | – |
| Player Controller Transform | `playerControllerTransform` | `Transform` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Main Gravity System | `mainGravitySystem` | `gravitySystem` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Time Bullet | `mainTimeBullet` | `timeBullet` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopTeleportInProcess()` | テレポート中か探索中なら実行フラグ・探索状態・マークを戻し、弾丸時間も解除して停止する。 |
| `teleportPlayer(Transform objectToMove, Vector3 teleportPosition, bool checkPositionAngle, bool changeFov, float newFovValue, float fovChangeSpeed, float teleportSpeed, bool rotatePlayerTowardPosition, bool teleportInstantlyToPositionValue, bool useActionSystemOnTeleportValue, bool useSmoothCameraFollowStateOnTeleportValue, float smoothCameraFollowDurationValue, float teleportDistanceOffsetValue, LayerMask layermaskToDetect, bool checkPlayerHeightToTeleportPosition)` | 既存のテレポートを止め、地点・FOV・速度など引数の設定で `teleportPlayerCoroutine` を開始する。 |
| `stopTeleporting()` | `teleportCoroutine` を止めてプレイヤー操作を有効に戻すだけ。 |
| `resumeIfTeleportActive()` | テレポート中なら `stopTeleporting` と `setTeleportEndState` で通常状態へ戻す。 |
| `setTeleportEndState()` | テレポート中なら終了フラグを下げ、使用アクションの停止・FOV復帰・終了イベントを行う。 |
| `setPlayerControlState(bool state)` | 操作可否に応じてプレイヤーの重力・速度・接地判定・摩擦などの制御状態をまとめて切り替える。 |
| `holdTeleport()` | 条件を満たす時だけ `searchingForTeleport` を立て、ボタン押下時刻を記録して照準を開始する。 |
| `releaseTeleport()` | ロックオン対象への即時テレポートも判定し、実行可能なら `teleportPlayer` を呼んで移動を開始する。 |
| `setTeleportingEnabledState(bool state)` | `teleportingEnabled` を設定するだけ。 |
| `isTeleportInProcess()` | `teleportInProcess` を返すだけ。 |
| `isSearchingForTeleport()` | `searchingForTeleport` を返すだけ。 |
| `getTeleportCanBeExecutedState()` | `teleportCanBeExecuted` を返すだけ。 |
| `setTeleportHookTarget(Transform newTarget)` | `useFixedTeleportHookPointsEnabled` の時だけ `currentTeleportHookTarget` を差し替える。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventsOnStartTeleport` | `UnityEvent` | – |
| `eventsOnEndTeleport` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`activateSecondaryActionOnAbility()`, `deactivateAbility()`, `disableAbility()`, `enableAbility()`, `updateAbilityState()`, `useAbilityPressDown()`, `useAbilityPressHold()`, `useAbilityPressUp()`

</details>
