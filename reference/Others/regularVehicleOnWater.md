# regularVehicleOnWater

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `FloatingObject`
- **ソース**: `Others/regularVehicleOnWater.cs:6`

**概要**: 水上を走る車両向けに、乗員の水中判定や浮力、水面の上下で発火するイベントを扱う。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Water State Enabled | `checkWaterStateEnabled` | `bool` | true | – |
| Min Distance To Sink Vehicle On Water | `minDistanceToSinkVehicleOnWater` | `float` | 1 | – |
| Min Distance To Check If Vehicle Above Surface | `minDistanceToCheckIfVehicleAboveSurface` | `float` | 1.2f | – |
| Turn Off Vehicle On Water Enabled | `turnOffVehicleOnWaterEnabled` | `bool` | – | – |
| Apply Damage If Vehicle Below Water Enabled | `applyDamageIfVehicleBelowWaterEnabled` | `bool` | – | – |
| Apply Damage If Vehicle Below Water Rate | `applyDamageIfVehicleBelowWaterRate` | `float` | – | – |
| Apply Damage If Vehicle Below Water Amount | `applyDamageIfVehicleBelowWaterAmount` | `float` | – | – |
| Sink Vehicle After Delay Enabled | `sinkVehicleAfterDelayEnabled` | `bool` | true | – |
| Wait Time Before Sinking | `waitTimeBeforeSinking` | `float` | 3 | – |
| Sinking Rate | `sinkingRate` | `float` | 0.1f | – |
| Sinking Amount | `sinkingAmount` | `float` | 0.5f | – |
| Enable Underwater State On Passengers On Vehicle Below Water State | `enableUnderwaterStateOnPassengersOnVehicleBelowWaterState` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Is Vehicle Below Water Level | `isVehicleBelowWaterLevel` | `bool` | – | – |
| Current Distance To Surface | `currentDistanceToSurface` | `float` | – | – |
| Vehicle Is Sinking | `vehicleIsSinking` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Vehicle Below Or Above Surface | `useEventsOnVehicleBelowOrAboveSurface` | `bool` | – | – |
| Events On Vehicle Above Surface | `eventsOnVehicleAboveSurface` | `UnityEvent` | – | – |
| Events On Vehicle Below Surface | `eventsOnVehicleBelowSurface` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Game Object | `vehicleGameObject` | `GameObject` | – | – |
| Main Vehicle Controller | `mainVehicleController` | `vehicleController` | – | – |
| Main Vehicle HUD Manager | `mainVehicleHUDManager` | `vehicleHUDManager` | – | – |
| Main Vehicle Gravity Control | `mainVehicleGravityControl` | `vehicleGravityControl` | – | – |
| Vehicle Max Water Level Transform | `vehicleMaxWaterLevelTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `disableVehiclePassengerUnderwaterStateWithoutCallingEvents()` | `mainVehicleHUDManager`の乗員一覧を回り、各乗員の`vehiclePassengerUnderwater`をイベント無しで解除する。 |
| `checkVehiclePassengersState()` | `vehicleIsSinking`が`true`の時だけ、乗員を水中状態にする。 |
| `checkEventStateOnBeloworAboveSurface(bool state)` | `useEventsOnVehicleBelowOrAboveSurface`が`true`の時、`state`に応じて水面上下のイベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventsOnVehicleAboveSurface` | `UnityEvent` | – |
| `eventsOnVehicleBelowSurface` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkObjectStateOnWater()`, `checkObjectStateOnWaterEnterOrExit(bool state)`

</details>
