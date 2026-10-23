# mainRiderSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/mainRiderSystem.cs:5`

**概要**: 車両のライダー（搭乗者）まわりの共通インターフェース。派生クラスが上書きする前提で、多くの仮想メソッドは空実装かnull/false/0を返す。

## インスペクター設定

### Main Rider Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Is External Vehicle Controller | `isExternalVehicleController` | `bool` | – | – |
| Vehicle Only For One Player | `vehicleOnlyForOnePlayer` | `bool` | true | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `isVehicleOnlyForOnePlayerActive()` | `vehicleOnlyForOnePlayer`の値を返すだけ。 |
| `getVehicleCameraGameObject()` | 基底では`null`を返す仮想メソッド。 |
| `getVehicleGravityControl()` | 基底では`null`を返す仮想メソッド。 |
| `getVehicleGameObject()` | 基底では`null`を返す仮想メソッド。 |
| `setTriggerToDetect(Collider newCollider)` | 本体が空で何もしない。 |
| `setPlayerVisibleInVehicleState(bool state)` | 本体が空で何もしない。 |
| `setResetCameraRotationWhenGetOnState(bool state)` | 本体が空で何もしない。 |
| `setEjectPlayerWhenDestroyedState(bool state)` | 本体が空で何もしない。 |
| `getCustomVehicleTransform()` | 基底では`null`を返す仮想メソッド。 |
| `setEnteringOnVehicleFromDistanceState(bool state)` | 本体が空で何もしない。 |
| `setCurrentPassenger(GameObject passenger)` | 本体が空で何もしない。 |
| `getCurrentDriver()` | 基底では`null`を返す仮想メソッド。 |
| `isBeingDrivenActive()` | 基底では`false`を返す仮想メソッド。 |
| `getVehicleRadius()` | 基底では`0`を返す仮想メソッド。 |
| `checkIfDetectSurfaceBelongToVehicle(Collider surfaceFound)` | 基底では`false`を返す仮想メソッド。 |
| `getVehicleCollider()` | 基底では`null`を返す仮想メソッド。 |
