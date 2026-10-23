# flyingController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `vehicleController`
- **ソース**: `Vehicles/Vehicle Controllers/flyingController.cs:6`

**概要**: 上下・左右・ロールで飛ぶ飛行ビークルのコントローラ。高さ入力、ロール入力、エンジン音と排気／ブーストパーティクルを扱う。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Time To Flip | `timeToFlip` | `float` | 2 | – |
| Audio Engine Speed | `audioEngineSpeed` | `float` | – | – |
| Engine Min Volume | `engineMinVolume` | `float` | 0.5f | – |
| Engine Max Volume | `engineMaxVolume` | `float` | 1 | – |
| Min Audio Pitch | `minAudioPitch` | `float` | 0.5f | – |
| Max Audio Pitch | `maxAudioPitch` | `float` | 1.2f | – |
| Max Speed | `maxSpeed` | `float` | 30 | – |
| Velocity Change Speed | `velocityChangeSpeed` | `float` | 10 | – |
| Stability Force | `stabilityForce` | `float` | 2 | – |
| Stability Speed | `stabilitySpeed` | `float` | 2 | – |
| Forward Speed | `forwardSpeed` | `float` | 15 | – |
| Right Speed | `rightSpeed` | `float` | 15 | – |
| Up Speed | `upSpeed` | `float` | 15 | – |
| Roll Rotation Speed | `rollRotationSpeed` | `float` | 5 | – |
| Engine Arm Rotation Amount Forward | `engineArmRotationAmountForward` | `float` | – | – |
| Engine Arm Rotation Amount Right | `engineArmRotationAmountRight` | `float` | – | – |
| Engine Arm Extra Rotation Amount | `engineArmExtraRotationAmount` | `float` | – | – |
| Engine Arm Rotation Speed | `engineArmRotationSpeed` | `float` | – | – |
| Engine Rotation Speed | `engineRotationSpeed` | `float` | 10 | – |
| Ground Raycast Distance | `groundRaycastDistance` | `float` | – | – |
| Hover Force | `hoverForce` | `float` | 5 | – |
| Hover Foece On Air | `hoverFoeceOnAir` | `float` | 2 | – |
| Rotate Force | `rotateForce` | `float` | 5 | – |
| Extra Hover Speed | `extraHoverSpeed` | `float` | 2 | – |
| Increase Height If Surface Below Found | `increaseHeightIfSurfaceBelowFound` | `bool` | – | – |
| Raycast Distance To Check Surface Below | `raycastDistanceToCheckSurfaceBelow` | `float` | 5 | – |
| Min Distance To Increase Height | `minDistanceToIncreaseHeight` | `float` | 4 | – |
| Surface Below Raycast Position | `surfaceBelowRaycastPosition` | `Transform` | – | – |

### Vehicle Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Other Car Parts | `otherCarParts` | `otherVehicleParts` | – | – |
| Settings | `settings` | `vehicletSettings` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Height Input | `heightInput` | `float` | – | – |
| Roll Direction | `rollDirection` | `float` | – | – |
| Ground Found | `groundFound` | `bool` | – | – |
| New Velocity | `newVelocity` | `Vector3` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Left Engine Transform | `leftEngineTransform` | `Transform` | – | – |
| Right Engine Transform | `rightEngineTransform` | `Transform` | – | – |
| Left Engine Arm Transform | `leftEngineArmTransform` | `Transform` | – | – |
| Right Engine Arm Transform | `rightEngineArmTransform` | `Transform` | – | – |
| Ground Raycast Position | `groundRaycastPosition` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopVehicleParticles()` | 通常・強排気の粒子を停止し、ブースト粒子のループを解除する。 |
| `inputIncreaseHeightState(bool state)` | 運転中なら`heightInput`を1／0に設定し、ホバーボード経由ならジャンプ力を与えて離脱する。 |
| `inputDecreaseHeightState(bool state)` | 運転中なら`heightInput`を-1／0に設定するだけ。 |
| `inputSetRotateToLeftState(bool state)` | 運転中なら`rollDirection`を1にし、3D移動でなければ0へ戻す。 |
| `inputSetRotateToRightState(bool state)` | 運転中なら`rollDirection`を-1にし、3D移動でなければ0へ戻す。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`Awake()`, `InitializeAudioElements()`, `Start()`, `changeGravityControlUse(bool state)`, `changeVehicleState()`, `disableVehicle()`, `endBrakeVehicleToStopCompletely()`, `getCurrentSpeed()`, `inputHoldOrReleaseTurbo(bool holdingButton)`, `inputHorn()`, `inputSetTurnOnState()`, `isDrivingActive()`, `setCollisionDetected(Collision currentCollision)`, `setEngineOnOrOffState()`, `setTurnOffState(bool previouslyTurnedOn)`, `setTurnOnState()`, `startBrakeVehicleToStopCompletely()`, `turnOnOrOff(bool state, bool previouslyTurnedOn)`, `updateMovingState()`, `usingBoosting()`, `vehicleUpdate()`

</details>

## 内部型

- `otherVehicleParts`（class）
- `vehicletSettings`（class）
