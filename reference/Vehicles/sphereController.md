# sphereController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `vehicleController`
- **ソース**: `Vehicles/Vehicle Controllers/sphereController.cs:4`

**概要**: 球体を転がす物理ベースのビークルコントローラ。接地・スナップ判定、ジャンプ、壁登り、水中判定、ブーストを扱う。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Parts | `vehicleParts` | `otherVehicleParts` | – | – |
| Settings | `settings` | `vehicleSettings` | – | – |

### Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Max Speed | `maxSpeed` | `float` | 10f | Range (0f, 100f) |
| Max Climb Speed | `maxClimbSpeed` | `float` | 4f | Range (0f, 100f) |
| Max Boost Climb Speed | `maxBoostClimbSpeed` | `float` | 4f | Range (0f, 100f) |
| Max Swim Speed | `maxSwimSpeed` | `float` | 5f | Range (0f, 100f) |
| Max Acceleration | `maxAcceleration` | `float` | 10f | Range (0f, 100f) |
| Max Air Acceleration | `maxAirAcceleration` | `float` | 1f | Range (0f, 100f) |
| Max Climb Acceleration | `maxClimbAcceleration` | `float` | 40f | Range (0f, 100f) |
| Max Swim Acceleration | `maxSwimAcceleration` | `float` | 5f | Range (0f, 100f) |
| Max Air Jumps | `maxAirJumps` | `int` | 0 | Range (0, 5) |
| Max Ground Angle | `maxGroundAngle` | `float` | 25f | Range (0, 90) |
| Max Stairs Angle | `maxStairsAngle` | `float` | 50f | Range (0, 90) |
| Max Climb Angle | `maxClimbAngle` | `float` | 140f | Range (90, 180) |
| Max Snap Speed | `maxSnapSpeed` | `float` | 100f | Range (0f, 100f) |
| Probe Distance | `probeDistance` | `float` | 1f | – |
| Submergence Offset | `submergenceOffset` | `float` | 0.5f | – |
| Submergence Range | `submergenceRange` | `float` | 1f | – |
| Buoyancy | `buoyancy` | `float` | 1f | – |
| Water Drag | `waterDrag` | `float` | 1f | Range (0f, 10f) |
| Swim Threshold | `swimThreshold` | `float` | 0.5f | Range (0.01f, 1f) |
| Probe Mask | `probeMask` | `LayerMask` | -1 | – |
| Stairs Mask | `stairsMask` | `LayerMask` | -1 | – |
| Climb Mask | `climbMask` | `LayerMask` | -1 | – |
| Water Mask | `waterMask` | `LayerMask` | 0 | – |
| Sphere Radius | `sphereRadius` | `float` | 0.5f | – |
| Sphere Align Speed | `sphereAlignSpeed` | `float` | 45 | – |
| Sphere Air Rotation | `sphereAirRotation` | `float` | 0.5f | – |
| Sphere Swim Rotation | `sphereSwimRotation` | `float` | 2f | – |
| Use Climb Enabled | `useClimbEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Any On Ground | `anyOnGround` | `bool` | – | – |
| Steps Since Last Jump | `stepsSinceLastJump` | `int` | – | – |
| Climb Contact Count | `climbContactCount` | `int` | – | – |
| Desires Climbing | `desiresClimbing` | `bool` | – | – |
| Ground Contact Count | `groundContactCount` | `int` | – | – |
| Steep Contact Count | `steepContactCount` | `int` | – | – |
| Steps Since Last Grounded | `stepsSinceLastGrounded` | `int` | – | – |
| Velocity | `velocity` | `Vector3` | – | – |
| Move Input | `moveInput` | `Vector3` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sphere Transform | `sphereTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `preventSnapToGround()` | `stepsSinceLastJump`を-1にし、数ステップの間スナップ・トゥ・グラウンドを抑止する。 |
| `useVehicleJumpPlatform(Vector3 direction)` | `direction`に質量を掛けた力を`ForceMode.Impulse`で加えて跳ね上げる。 |
| `useJumpPlatformParable(Vector3 direction)` | `direction`を`ForceMode.VelocityChange`で加え、質量非依存の跳ね上げを与える。 |
| `setNewJumpPower(float newJumpPower)` | `jumpPower`を`newJumpPower`×100に変換して設定するだけ。 |
| `setOriginalJumpPower()` | `jumpPower`を保存済みの`originalJumpPower`に戻すだけ。 |
| `inputSetClimbState(bool state)` | 運転中かつクライム有効・非水泳なら登り状態を設定し、重力を一時停止する。 |
| `inputToggleClimbState()` | 運転中なら現在の登り状態を反転させる。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`Awake()`, `Start()`, `changeGravityControlUse(bool state)`, `changeVehicleState()`, `disableVehicle()`, `inputHoldOrReleaseBrake(bool holdingButton)`, `inputHoldOrReleaseTurbo(bool holdingButton)`, `inputJump()`, `inputSetTurnOnState()`, `isDrivingActive()`, `setEngineOnOrOffState()`, `setTurnOffState(bool previouslyTurnedOn)`, `setTurnOnState()`, `turnOnOrOff(bool state, bool previouslyTurnedOn)`, `updateMovingState()`, `usingBoosting()`, `vehicleUpdate()`

</details>

## 内部型

- `otherVehicleParts`（class）
- `vehicleSettings`（class）
