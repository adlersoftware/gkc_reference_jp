# carController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `vehicleController`
- **ソース**: `Vehicles/Vehicle Controllers/carController.cs:6`

**概要**: 車輪コライダーと`Rigidbody`で走行する四輪車両のコントローラ。車体のリーン、ギアとエンジン音、スキッド痕、ブースト、乗降時の揺れ、転倒時の自動復帰を扱う。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Wheels List | `wheelsList` | `List<Wheels>` | new List<Wheels> () | – |
| Gears List | `gearsList` | `List<Gears>` | new List<Gears> () | – |
| Other Car Parts | `otherCarParts` | `OtherCarParts` | – | – |
| Settings | `settings` | `carSettings` | – | – |
| Rotate Vehicle Upward | `rotateVehicleUpward` | `bool` | true | – |
| Min Inclination To Rotate Vehicle | `minInclinationToRotateVehicle` | `float` | 60 | – |
| Rotate Vehicle Upward Speed | `rotateVehicleUpwardSpeed` | `float` | 3 | – |
| Bounce Vehicle On Passenger Getting On Off | `bounceVehicleOnPassengerGettingOnOff` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Gear | `currentGear` | `int` | – | – |
| Current Rear RPM | `currentRearRPM` | `float` | 0 | – |
| Current RPM | `currentRPM` | `float` | 0 | – |
| Any On Ground | `anyOnGround` | `bool` | – | – |
| External Brake Active | `externalBrakeActive` | `bool` | – | – |
| Reversing | `reversing` | `bool` | – | – |
| Pause Auto Rotation Active State | `pauseAutoRotationActiveState` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Skid Marks Manager | `skidMarksManager` | `skidsManager` | – | – |
| Interface Info | `interfaceInfo` | `shipInterfaceInfo` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `vehicleBounceMovement(float horizontalLeanAmount, float verticalLeanAmount)` | 乗降時に車体を水平・垂直方向へ指定量傾けるコルーチンを開始する（無効時は何もしない）。 |
| `rotateVehicle()` | 進行中の回転を止め、`currentNormal`に合わせて車体を起こし速度をゼロにするコルーチンを開始する。 |
| `useVehicleJumpPlatform(Vector3 direction)` | `direction`に質量を掛けた力を`ForceMode.Impulse`で加え、ジャンプ台の跳ね上げを与える。 |
| `useJumpPlatformParable(Vector3 direction)` | `direction`を`ForceMode.VelocityChange`で加え、質量非依存の跳ね上げを与える。 |
| `setJumpPower(float newJumpPower)` | `jumpPower`を`newJumpPower`で直接上書きするだけ。 |
| `setNewJumpPower(float newJumpPower)` | `jumpPower`を`newJumpPower`×100に変換して設定するだけ。 |
| `setOriginalJumpPower()` | `jumpPower`を保存済みの`originalJumpPower`に戻すだけ。 |
| `setMaxSpeed(float maxSpeedValue)` | 最高前進速度`maxForwardSpeed`を`maxSpeedValue`にするだけ。 |
| `setMaxAcceleration(float maxAccelerationValue)` | エンジントルク`settings.engineTorque`を`maxAccelerationValue`にするだけ。 |
| `setMaxBrakePower(float maxBrakePower)` | ブレーキ力`settings.brake`を`maxBrakePower`にするだけ。 |
| `setMaxTurboPower(float maxTurboPower)` | ブースト倍率`maxBoostMultiplier`を`maxTurboPower`にするだけ。 |
| `setCanJumpState(bool state)` | ジャンプ可否`canJump`を`state`にするだけ。 |
| `setRotateVehicleUpwardState(bool state)` | 転倒時の自動復帰を行う`rotateVehicleUpward`を`state`にするだけ。 |
| `setPreserveDirectionWhileInAirState(bool state)` | 空中で進行方向を保持する`preserveDirectionWhileInAir`を`state`にするだけ。 |
| `setPauseAutoRotationActiveState(bool state)` | 自動復帰回転を止める`pauseAutoRotationActiveState`を`state`にするだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`Awake()`, `InitializeAudioElements()`, `Start()`, `activateAutoBrakeOnGetOff()`, `changeGravityControlUse(bool state)`, `changeVehicleState()`, `disableVehicle()`, `endBrakeVehicleToStopCompletely()`, `getCurrentSpeed()`, `inputHoldOrReleaseBrake(bool holdingButton)`, `inputHoldOrReleaseJump(bool holdingButton)`, `inputHoldOrReleaseTurbo(bool holdingButton)`, `inputHorn()`, `inputJump()`, `inputSetTurnOnState()`, `isDrivingActive()`, `isVehicleOnGround()`, `passengerGettingOnOff()`, `pressHorn()`, `setCollisionDetected(Collision currentCollision)`, `setEngineOnOrOffState()`, `setTurnOffState(bool previouslyTurnedOn)`, `setTurnOnState()`, `startBrakeVehicleToStopCompletely()`, `turnOnOrOff(bool state, bool previouslyTurnedOn)`, `usingBoosting()`, `vehicleUpdate()`

</details>

## 内部型

- `Gears`（class）
- `Wheels`（class）
- `OtherCarParts`（class）
- `carSettings`（class）
