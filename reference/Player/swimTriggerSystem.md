# swimTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/swimTriggerSystem.cs:5`

**概要**: 水泳ゾーンのトリガー。プレイヤーの泳ぎ状態を開始/終了させ、車両が水に入った際の処理も行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Check | `tagToCheck` | `string` | – | – |
| Swim Zone Active | `swimZoneActive` | `bool` | true | – |
| Update Surface Transform Dynamically | `updateSurfaceTransformDynamically` | `bool` | – | – |

### Vehicle Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Vehicles On Entering Water | `checkVehiclesOnEnteringWater` | `bool` | – | – |
| Disable Vehicles Interaction On Enter Water | `disableVehiclesInteractionOnEnterWater` | `bool` | – | – |
| Eject Passengers On Vehicle On Enter Water | `ejectPassengersOnVehicleOnEnterWater` | `bool` | – | – |
| Explode Vehicles After X Time | `explodeVehiclesAfterXTime` | `bool` | – | – |
| Time To Explode Vehicles After X Time | `timeToExplodeVehiclesAfterXTime` | `float` | – | – |
| Set Vehicle Gravity Force | `setVehicleGravityForce` | `bool` | – | – |
| New Vehicle Gravity Force | `newVehicleGravityForce` | `float` | – | – |
| Reduce Vehicle Speed On Enter Water | `reduceVehicleSpeedOnEnterWater` | `bool` | – | – |
| Reduced Vehicle Speed Multiplier | `reducedVehicleSpeedMultiplier` | `float` | – | – |
| Vehicle Layer To Check | `vehicleLayerToCheck` | `LayerMask` | – | – |
| Check Vehicles On Exiting Water | `checkVehiclesOnExitingWater` | `bool` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Events | `useRemoteEvents` | `bool` | – | – |
| Use Remote Event On Swim Start | `useRemoteEventOnSwimStart` | `bool` | – | – |
| Remote Event Name List On Swim Start | `remoteEventNameListOnSwimStart` | `List<string>` | new List<string> () | – |
| Use Remote Event On Swim End | `useRemoteEventOnSwimEnd` | `bool` | – | – |
| Remote Event Name List On Swim End | `remoteEventNameListOnSwimEnd` | `List<string>` | new List<string> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Detected List | `vehicleDetectedList` | `List<GameObject>` | new List<GameObject> () | – |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.red | – |
| Gizmo Radius | `gizmoRadius` | `float` | 0.1f | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Swim Zone Transform | `swimZoneTransform` | `Transform` | – | – |
| Main Water Surface System | `mainWaterSurfaceSystem` | `waterSurfaceSystem` | – | – |
| Main Trigger | `mainTrigger` | `Collider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | 入場時に泳ぎを開始し、退場時に最後のトリガーなら終了する。車両には水没処理も行う。 |
