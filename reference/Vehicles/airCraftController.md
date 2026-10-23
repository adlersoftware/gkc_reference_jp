# airCraftController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `vehicleController`
- **ソース**: `Vehicles/Vehicle Controllers/airCraftController.cs:7`

**概要**: 航空機用コントローラ。ピッチ・ヨー・ロール入力、離着陸ギアと翼のアニメーション、エンジン／風／離着陸音、トレイルの表示を扱う。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Parts | `vehicleParts` | `otherVehicleParts` | – | – |
| Settings | `settings` | `airCraftSettings` | – | – |
| Non Realistic Settings | `nonRealisticSettings` | `airCraftNonRealisticSettings` | – | – |
| Realistic Settings | `realisticSettings` | `airCraftRealisticSettings` | – | – |
| Acceleration Speed | `accelerationSpeed` | `float` | – | – |
| Realistic Movements | `realisticMovements` | `bool` | – | – |
| Max Engine Power | `maxEnginePower` | `float` | 40 | – |
| Lift Amount | `liftAmount` | `float` | 0.002f | – |
| Stop Lift At Speed | `stopLiftAtSpeed` | `float` | 300 | – |
| Pitch Force | `pitchForce` | `float` | 0.75f | – |
| Yaw Force | `yawForce` | `float` | 0.75f | – |
| Roll Force | `rollForce` | `float` | 0.75f | – |
| Banked Turn Force | `bankedTurnForce` | `float` | 0.5f | – |
| Aero Dynamic Force | `aeroDynamicForce` | `float` | 0.02f | – |
| Banked Turn Pitch | `bankedTurnPitch` | `float` | 0.5f | – |
| Banked Roll Force | `bankedRollForce` | `float` | 0.1f | – |
| Banked Pitch Force | `bankedPitchForce` | `float` | 0.1f | – |
| Brakes Force | `brakesForce` | `float` | 20 | – |
| Throttle Change Speed | `throttleChangeSpeed` | `float` | 0.3f | – |
| Drag Increase Factor | `dragIncreaseFactor` | `float` | 0.001f | – |
| Boost Multiplier | `boostMultiplier` | `float` | – | – |
| Boost Acceleration Speed | `boostAccelerationSpeed` | `float` | – | – |
| Current Boost | `currentBoost` | `float` | – | – |
| Engine Master Volume | `engineMasterVolume` | `float` | 0.5f | Range (0f, 1f) |
| Wind Master Volume | `windMasterVolume` | `float` | 0.5f | Range (0f, 1f) |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Landing | `landing` | `bool` | – | – |
| Take Off | `takeOff` | `bool` | – | – |
| Engines On | `enginesOn` | `bool` | – | – |
| Can Land | `canLand` | `bool` | – | – |
| Roll Input | `rollInput` | `float` | – | – |
| Pitch Input | `pitchInput` | `float` | – | – |
| Yaw Input | `yawInput` | `float` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Interface Info | `interfaceInfo` | `shipInterfaceInfo` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `resetInputValues()` | ピッチ・ヨー・ロール入力と速度系の値をゼロにリセットする。 |
| `enableOrDisableTrailsState(bool state)` | 全トレイルの`time`を`trailsTime`（無効時0）へ補間するコルーチンで、呼び出し側が実行する。 |
| `playAnimation(bool forward, GameObject obj, string name)` | `useAnimations`が有効なら、`obj`の`Animation`で`name`を順再生／逆再生する。 |
| `setTurnOnStateSound()` | エンジン音と風切り音をループ再生し、始動音を一度鳴らす。 |
| `setTurnOffStateSound(bool previouslyTurnedOn)` | `previouslyTurnedOn`がtrueなら、エンジン音と風切り音を止めて停止音を鳴らす。 |
| `inputSetRotateToLeftState(bool state)` | 運転中ならロール方向を1（左）に設定し、3D移動でなければ0に戻す。 |
| `inputSetRotateToRightState(bool state)` | 運転中ならロール方向を-1（右）に設定し、3D移動でなければ0に戻す。 |
| `inputLandOrTakeOff()` | 運転中かつエンジン始動中なら、離陸／着陸処理`landingOrTakeOffAirCraft`を呼ぶ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`Awake()`, `InitializeAudioElements()`, `Start()`, `changeVehicleState()`, `disableVehicle()`, `inputHoldOrReleaseBrake(bool holdingButton)`, `inputHoldOrReleaseTurbo(bool holdingButton)`, `inputSetTurnOnState()`, `isDrivingActive()`, `setCollisionDetected(Collision currentCollision)`, `setEngineOnOrOffState()`, `setTurnOffState(bool previouslyTurnedOn)`, `turnOnOrOff(bool state, bool previouslyTurnedOn)`, `usingBoosting()`, `vehicleUpdate()`

</details>

## 内部型

- `otherVehicleParts`（class）
- `airCraftSettings`（class）
- `airCraftNonRealisticSettings`（class）
- `airCraftRealisticSettings`（class）
- `exhaustsParticlesInfo`（class）
