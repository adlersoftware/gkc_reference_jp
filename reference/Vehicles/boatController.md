# boatController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `vehicleController`
- **ソース**: `Vehicles/Vehicle Controllers/boatController.cs:5`

**概要**: 水面オブジェクトの浮力と帆・風の状態で進むボート用コントローラ。帆と風検知の切替イベント、船体密度の増減、ジャンプ台連携を持つ。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Parts | `vehicleParts` | `otherVehicleParts` | – | – |
| Settings | `settings` | `vehicleSettings` | – | – |

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Move Forward Speed Multiplier | `moveForwardSpeedMultiplier` | `float` | – | – |
| Move Backward Speed Multiplier | `moveBackwardSpeedMultiplier` | `float` | – | – |
| Forward Movement Lerp Speed | `forwardMovementLerpSpeed` | `float` | 0.8f | – |
| Air Control Amount | `airControlAmount` | `float` | – | – |
| Air Control Rotation Amount | `airControlRotationAmount` | `float` | 4 | – |
| Brake Force | `brakeForce` | `float` | 5 | – |
| Roll Rotation Speed | `rollRotationSpeed` | `float` | 5 | – |
| Roll Rotation Reversed | `rollRotationReversed` | `bool` | – | – |
| Rotation Extra Forward Movement | `rotationExtraForwardMovement` | `float` | 0.4f | – |
| Rotation Lerp Speed | `rotationLerpSpeed` | `float` | 0.6f | – |

### Density Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Density Enabled | `changeDensityEnabled` | `bool` | true | – |
| Density Change Amount | `densityChangeAmount` | `float` | 0.05f | – |
| Density Clamp Values | `densityClampValues` | `Vector2` | – | – |

### Orientation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Max Angle Range For Proper Orientation Forces | `maxAngleRangeForProperOrientationForces` | `float` | 45 | – |
| Auto Orientate Up On Water | `autoOrientateUpOnWater` | `bool` | – | – |
| Min Angle To Auto Orientate Up On Water | `minAngleToAutoOrientateUpOnWater` | `float` | – | – |
| Auto Orientate Up Force Amount On Water | `autoOrientateUpForceAmountOnWater` | `float` | – | – |
| Auto Orientate Up On Air | `autoOrientateUpOnAir` | `bool` | – | – |
| Min Angle To Auto Orientate Up On Air | `minAngleToAutoOrientateUpOnAir` | `float` | – | – |
| Auto Orientate Up Force Amount On Air | `autoOrientateUpForceAmountOnAir` | `float` | – | – |

### Wind Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Wind State | `checkWindState` | `bool` | – | – |
| Sail Active | `sailActive` | `bool` | – | – |
| Ignore Wind Forces If Not Driving Boat | `ignoreWindForcesIfNotDrivingBoat` | `bool` | – | – |
| Add Wind Force If Sail Not Active | `addWindForceIfSailNotActive` | `bool` | – | – |
| Wind Force Multiplier If Sail Not Active | `windForceMultiplierIfSailNotActive` | `float` | 0.5f | – |
| Sail Transform | `sailTransform` | `Transform` | – | – |
| Sail Direction Transform | `sailDirectionTransform` | `Transform` | – | – |
| Sail Wind Speed Multiplier | `sailWindSpeedMultiplier` | `float` | – | – |
| Sail Rotation Speed | `sailRotationSpeed` | `float` | – | – |
| Sail Rotation Clamp | `sailRotationClamp` | `float` | – | – |
| Sail Rotation Amount | `sailRotationAmount` | `float` | – | – |
| Check Boat Orientation On Wind | `checkBoatOrientationOnWind` | `bool` | – | – |
| Max Angle To Reduce Speed On Incorrect Wind Direction | `maxAngleToReduceSpeedOnIncorrectWindDirection` | `float` | – | – |
| Reduce Speed On Incorrect Wind Direction Multiplier | `reduceSpeedOnIncorrectWindDirectionMultiplier` | `float` | – | – |
| Show Wind Direction Object | `showWindDirectionObject` | `bool` | – | – |
| Wind Direction Rotation Speed | `windDirectionRotationSpeed` | `float` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Active Wind Detection | `eventOnActiveWindDetection` | `UnityEvent` | – | – |
| Event On Deactive Wind Detection | `eventOnDeactiveWindDetection` | `UnityEvent` | – | – |
| Event On Active Sail | `eventOnActiveSail` | `UnityEvent` | – | – |
| Event On Deactive Sail | `eventOnDeactiveSail` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Any On Ground | `anyOnGround` | `bool` | – | – |
| Normal Angle | `normalAngle` | `float` | – | – |
| Properly Oriented Up | `properlyOrientedUp` | `bool` | – | – |
| Wind Air Speed Multiplier | `windAirSpeedMultiplier` | `float` | – | – |
| Wind Angle | `windAngle` | `float` | – | – |
| Regular Wind Angle | `regularWindAngle` | `float` | – | – |
| Sail Looking Right | `sailLookingRight` | `bool` | – | – |
| Force To Apply | `forceToApply` | `Vector3` | – | – |
| Reduced Speed On Incorrect Wind Multiplier | `reducedSpeedOnIncorrectWindMultiplier` | `float` | – | – |
| Boat Angle With Wind | `boatAngleWithWind` | `float` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Object On Water | `mainObjectOnWater` | `objectOnWater` | – | – |
| External Rotation Force Point Transform | `externalRotationForcePointTransform` | `Transform` | – | – |
| Main Wind On Object State | `mainWindOnObjectState` | `windOnObjectState` | – | – |
| Wind Direction Transform | `windDirectionTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkEventOnWindStateChange(bool state)` | `state`に応じて風検知の有効／無効イベントを発火するだけ。 |
| `checkEventOnSailStateChange(bool state)` | `state`に応じて帆の有効／無効イベントを発火するだけ。 |
| `useVehicleJumpPlatform(Vector3 direction)` | `direction`に質量を掛けた力を`ForceMode.Impulse`で加え、ジャンプ台の跳ね上げを与える。 |
| `useJumpPlatformParable(Vector3 direction)` | `direction`を`ForceMode.VelocityChange`で加え、質量非依存の跳ね上げを与える。 |
| `setNewJumpPower(float newJumpPower)` | `jumpPower`を`newJumpPower`×100に変換して設定するだけ。 |
| `setOriginalJumpPower()` | `jumpPower`を保存済みの`originalJumpPower`に戻すだけ。 |
| `setCanJumpState(bool state)` | ジャンプ可否`canJump`を`state`にするだけ。 |
| `setSailActiveState(bool state)` | `sailActive`を更新し、帆の有効／無効イベントを発火する。 |
| `setWindCheckState(bool state)` | `checkWindState`を更新し、風検知の有効／無効イベントを発火する。 |
| `inputToggleWindCheckState()` | 運転中なら風検知の有効状態を反転させる。 |
| `inputToggleSailActive()` | 運転中なら帆の展開状態を反転させる。 |
| `inputIncreaseDensity()` | 運転中かつ密度変更が有効なら、水面オブジェクトの密度を上限まで`densityChangeAmount`ずつ増やす。 |
| `inputDecreaseDensity()` | 運転中かつ密度変更が有効なら、水面オブジェクトの密度を下限まで`densityChangeAmount`ずつ減らす。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnActiveWindDetection` | `UnityEvent` | – |
| `eventOnDeactiveWindDetection` | `UnityEvent` | – |
| `eventOnActiveSail` | `UnityEvent` | – |
| `eventOnDeactiveSail` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`Awake()`, `Start()`, `changeGravityControlUse(bool state)`, `changeVehicleState()`, `disableVehicle()`, `inputHoldOrReleaseBrake(bool holdingButton)`, `inputHoldOrReleaseTurbo(bool holdingButton)`, `inputJump()`, `inputSetTurnOnState()`, `isDrivingActive()`, `isVehicleOnGround()`, `setEngineOnOrOffState()`, `setTurnOffState(bool previouslyTurnedOn)`, `setTurnOnState()`, `turnOnOrOff(bool state, bool previouslyTurnedOn)`, `updateMovingState()`, `usingBoosting()`, `vehicleUpdate()`

</details>

## 内部型

- `otherVehicleParts`（class）
- `vehicleSettings`（class）
