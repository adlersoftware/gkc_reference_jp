# vehicleInteractionPanelSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/vehicleInteractionPanelSystem.cs:6`

**概要**: 近くの車両を検知したときに運転/同乗の入力アイコンや満車表示を出すパネル。入力に応じてプレイヤーを車両へ搭乗させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Interaction Enabled | `vehicleInteractionEnabled` | `bool` | true | – |
| Enter Vehicle As Driver Input Name | `enterVehicleAsDriverInputName` | `string` | "Enter Vehicle As Driver" | – |
| Enter Vehicle As Passenger Input Name | `enterVehicleAsPassengerInputName` | `string` | "Enter Vehicle As Passenger" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Vehicle Detected | `vehicleDetected` | `bool` | – | – |
| Is Vehicle Full | `isVehicleFull` | `bool` | – | – |
| Is Vehicle Being Driven | `isVehicleBeingDriven` | `bool` | – | – |
| Are Passenger Seats Full | `arePassengerSeatsFull` | `bool` | – | – |
| Number Of Vehicle Seats | `numberOfVehicleSeats` | `int` | – | – |
| Current Device Detected | `currentDeviceDetected` | `GameObject` | – | – |
| Previous Device Detected | `previousDeviceDetected` | `GameObject` | – | – |
| Current Vehicle Game Object | `currentVehicleGameObject` | `GameObject` | – | – |
| Current IK Driving System | `currentIKDrivingSystem` | `IKDrivingSystem` | – | – |
| Current Vehicle HUD Manager | `currentVehicleHUDManager` | `vehicleHUDManager` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Using Devices System | `mainUsingDevicesSystem` | `usingDevicesSystem` | – | – |
| Main Player Input Manager | `mainPlayerInputManager` | `playerInputManager` | – | – |

### UI Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Seats Available Icon List | `vehicleSeatsAvailableIconList` | `List<GameObject>` | new List<GameObject> () | – |
| Vehicle Driver Icon Panel | `vehicleDriverIconPanel` | `GameObject` | – | – |
| Vehicle Passenger Icon Panel | `vehiclePassengerIconPanel` | `GameObject` | – | – |
| Vehicle Driver Text | `vehicleDriverText` | `Text` | – | – |
| Vehicle Passenger Text | `vehiclePassengerText` | `Text` | – | – |
| Vehicle Full Panel | `vehicleFullPanel` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の更新コルーチンがあれば停止する。 |
| `setCurrentVehicleDetected(GameObject newVehicle)` | 検知車両を保持し、車両なら席数や運転/同乗/満車アイコンとキー表示を更新する。 |
| `inputEnterOnVehicleAsDriver()` | 満車・運転中・直後の再搭乗などのガードを通ったら、プレイヤーを運転席に乗せる。 |
| `inputEnterOnVehicleAsPassenger()` | 運転中なら現車両をデバイスとして使い直し、そうでなければガード確認後に同乗させる。 |
