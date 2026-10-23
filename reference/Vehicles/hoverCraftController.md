# hoverCraftController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `vehicleController`
- **ソース**: `Vehicles/Vehicle Controllers/hoverCraftController.cs:6`

**概要**: ホバーエンジンの推力で浮上するホバークラフト用コントローラ。浮上用レイキャスト、ジャンプ入力の保持、ブースト、パーティクルを扱う。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Max Steering Torque | `maxSteeringTorque` | `float` | 1400 | – |
| Roll On Turns | `rollOnTurns` | `float` | 10 | – |
| Roll On Turns Torque | `rollOnTurnsTorque` | `float` | 20 | – |
| Steer Braking Torque | `steerBrakingTorque` | `float` | 1400 | – |
| Braking Torque | `brakingTorque` | `float` | – | – |
| Pitch Compensation Torque | `pitchCompensationTorque` | `float` | – | – |
| Roll Compensation Torque | `rollCompensationTorque` | `float` | 10 | – |
| Time To Flip | `timeToFlip` | `float` | 2 | – |
| Audio Engine Speed | `audioEngineSpeed` | `float` | – | – |
| Engine Min Volume | `engineMinVolume` | `float` | 0.5f | – |
| Engine Max Volume | `engineMaxVolume` | `float` | 1 | – |
| Min Audio Pitch | `minAudioPitch` | `float` | 0.5f | – |
| Max Audio Pitch | `maxAudioPitch` | `float` | 1.2f | – |
| Max Forward Acceleration | `maxForwardAcceleration` | `float` | 20 | – |
| Max Reverse Acceleration | `maxReverseAcceleration` | `float` | 15 | – |
| Max Braking Deceleration | `maxBrakingDeceleration` | `float` | 30 | – |
| Auto Braking Deceleration | `autoBrakingDeceleration` | `float` | – | – |
| Max Speed | `maxSpeed` | `float` | 30 | – |
| Acceleration Curve | `accelerationCurve` | `AnimationCurve` | – | – |
| Vertical Reduction | `verticalReduction` | `float` | 10 | – |
| Max Pitch Angle | `maxPitchAngle` | `float` | 45 | – |
| Extra Rigidbody Force | `extraRigidbodyForce` | `Vector3` | – | – |
| Min Steer Input Idle | `minSteerInputIdle` | `float` | 0.4f | – |
| Min Steer Input Moving | `minSteerInputMoving` | `float` | 0.4f | – |

### Hovercraft Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hover Engine List | `hoverEngineList` | `List<hoverEngineSettings>` | new List<hoverEngineSettings> () | – |
| Other Car Parts | `otherCarParts` | `OtherCarParts` | – | – |
| Settings | `settings` | `hoverCraftSettings` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Any On Ground | `anyOnGround` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `useVehicleJumpPlatform(Vector3 direction)` | `jumpInputPressed`を0.5秒立て、`direction`×質量のImpulseを与える。 |
| `useJumpPlatformParable(Vector3 direction)` | `direction`を`ForceMode.VelocityChange`で加え、質量非依存の跳ね上げを与える。 |
| `setNewJumpPower(float newJumpPower)` | `jumpPower`を`newJumpPower`×100に変換して設定するだけ。 |
| `setOriginalJumpPower()` | `jumpPower`を保存済みの`originalJumpPower`に戻すだけ。 |
| `setCanJumpState(bool state)` | ジャンプ可否`canJump`を`state`にするだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`Awake()`, `InitializeAudioElements()`, `Start()`, `changeGravityControlUse(bool state)`, `changeVehicleState()`, `disableVehicle()`, `endBrakeVehicleToStopCompletely()`, `getCurrentSpeed()`, `inputHoldOrReleaseBrake(bool holdingButton)`, `inputHoldOrReleaseTurbo(bool holdingButton)`, `inputHorn()`, `inputJump()`, `inputSetTurnOnState()`, `isDrivingActive()`, `setCollisionDetected(Collision currentCollision)`, `setEngineOnOrOffState()`, `setTurnOffState(bool previouslyTurnedOn)`, `setTurnOnState()`, `startBrakeVehicleToStopCompletely()`, `turnOnOrOff(bool state, bool previouslyTurnedOn)`, `updateCameraSteerState()`, `usingBoosting()`, `vehicleUpdate()`

</details>

## 内部型

- `hoverEngineSettings`（class）
- `OtherCarParts`（class）
- `hoverCraftSettings`（class）
