# vehicleAINavMesh

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `AINavMesh`
- **ソース**: `Vehicles/AI/vehicleAINavMesh.cs:7`

**概要**: NavMesh上を走るAI車両の追従・巡回路・回避・ブレーキ制御をまとめたコンポーネント。入力値の上書きや目標の再評価も行う。

## インスペクター設定

### Vehicle AI Navmesh Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle AI Active | `vehicleAIActive` | `bool` | true | – |
| Use Navmesh Active | `useNavmeshActive` | `bool` | – | – |
| Auto Brake On Remove Target | `autoBrakeOnRemoveTarget` | `bool` | – | – |
| Check Current Target State Enabled | `checkCurrentTargetStateEnabled` | `bool` | – | – |
| Check Current Target State Rate | `checkCurrentTargetStateRate` | `float` | 0.3f | – |
| M Cautious Speed Factor | `m_CautiousSpeedFactor` | `float` | 0.05f | Range (0, 1) |
| M Cautious Max Angle | `m_CautiousMaxAngle` | `float` | 50f | Range (0, 180) |
| M Cautious Max Distance | `m_CautiousMaxDistance` | `float` | 100f | – |
| M Cautious Angular Velocity Factor | `m_CautiousAngularVelocityFactor` | `float` | 30f | – |
| M Steer Sensitivity | `m_SteerSensitivity` | `float` | 0.05f | – |
| M Accel Sensitivity | `m_AccelSensitivity` | `float` | 0.04f | – |
| M Brake Sensitivity | `m_BrakeSensitivity` | `float` | 1f | – |
| M Lateral Wander Distance | `m_LateralWanderDistance` | `float` | 3f | – |
| M Lateral Wander Speed | `m_LateralWanderSpeed` | `float` | 0.1f | – |
| M Accel Wander Amount | `m_AccelWanderAmount` | `float` | 0.1f | Range (0, 1) |
| M Accel Wander Speed | `m_AccelWanderSpeed` | `float` | 0.1f | – |
| M Brake Condition | `m_BrakeCondition` | `BrakeCondition` | BrakeCondition.TargetDistance | – |
| M Stop When Target Reached | `m_StopWhenTargetReached` | `bool` | false | – |
| M Reach Target Threshold | `m_ReachTargetThreshold` | `float` | 2 | – |
| Max Speed | `maxSpeed` | `float` | – | – |

### Obstacle Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Obstacle In Front Layermask | `obstacleInFrontLayermask` | `LayerMask` | – | – |
| Obstacle In Front Raycast Distance | `obstacleInFrontRaycastDistance` | `float` | 2 | – |
| Obstacle In Front Raycast Offset | `obstacleInFrontRaycastOffset` | `float` | 2 | – |
| Stop If Certain Obstacle Layer Detected | `stopIfCertainObstacleLayerDetected` | `bool` | – | – |
| Layermask To Stop If Detected | `layermaskToStopIfDetected` | `LayerMask` | – | – |
| Capsule Cast Radius To Stop If Detected | `capsuleCastRadiusToStopIfDetected` | `float` | – | – |
| Capsule Cast Distance To Stop If Detected | `capsuleCastDistanceToStopIfDetected` | `float` | – | – |

### Reverse Direction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Reversing Accelereation Duration | `reversingAccelereationDuration` | `float` | 3 | – |
| Min Wait To Activate Reversing | `minWaitToActivateReversing` | `float` | 2 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Vehicle Debug Print | `showVehicleDebugPrint` | `bool` | – | – |
| Current Input Values | `currentInputValues` | `Vector2` | – | – |
| Driving | `driving` | `bool` | – | – |
| Using Track Active | `usingTrackActive` | `bool` | – | – |
| Reversing Active Temporaly | `reversingActiveTemporaly` | `bool` | – | – |
| Obstacle To Stop Detected | `obstacleToStopDetected` | `bool` | – | – |
| Current Target Is Character | `currentTargetIsCharacter` | `bool` | – | – |
| Current Target Is Vehicle | `currentTargetIsVehicle` | `bool` | – | – |
| Current Target Is Driving | `currentTargetIsDriving` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Input Action Manager | `mainInputActionManager` | `inputActionManager` | – | – |
| M Rigidbody | `m_Rigidbody` | `Rigidbody` | – | – |
| M Target | `m_Target` | `Transform` | – | – |
| Vehicle Transform | `vehicleTransform` | `Transform` | – | – |
| Main Vehicle Hud Manager | `mainVehicleHudManager` | `vehicleHUDManager` | – | – |
| AI Patrol Manager | `AIPatrolManager` | `AIPatrolSystem` | – | – |
| Explanation | `explanation` | `string` | "Enable the field Use Navmesh Active … | TextArea (3, 10) |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableAIObject(bool state)` | AIオブジェクトのアクティブを切り替え、一時停止と使用状態を反映し、無効化時はAI運転中なら中断して入力をゼロにする。 |
| `enableOrDisableAIObjectWithoutActivatingDrivingState(bool state)` | 運転状態を変えずに同じ切り替えを行い、使用状態だけを反映する。 |
| `setUsedByAIState(bool state)` | `mainVehicleHudManager.setUsedByAIState`に委譲するだけ。 |
| `setUsedByAIStateWithoutActivatingDrvingState(bool state)` | `mainVehicleHudManager`の同名メソッドに委譲するだけ。 |
| `enableOrDisablePatrolState(bool state)` | 巡回マネージャがあるとき、開始なら一時停止を解いて最寄り点と巡回復帰を設定し、終了なら一時停止する。 |
| `SetTarget(Transform target)` | `m_Target`を新しいターゲットに差し替え、走行状態を有効にする。 |
| `setDrivingState(bool state)` | `driving`を設定し、反転状態やステア方向、反転時刻の記録をリセットする。 |
| `setUsingTrackActive(bool state)` | `usingTrackActive`を設定するだけ。 |
| `setVehicleAIActiveState(bool state)` | `vehicleAIActive`を設定するだけ。 |
| `setAutoBrakeOnRemoveTargetState(bool state)` | `autoBrakeOnRemoveTarget`を設定するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`Start()`, `checkStateOnSetTarget()`, `removeTarget()`, `setPatrolTarget(Transform newTarget)`, `updateAICameraInputValues()`, `updateAIControllerInputValues()`

</details>

## 内部型

- `BrakeCondition`（enum）
