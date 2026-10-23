# playerSphereModeSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/playerSphereModeSystem.cs:6`

**概要**: プレイヤーが球体になって転がる「スフィアモード」への切替を扱う。車両情報を選択し、状態変更コルーチンを起動する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sphere Mode Enabled | `sphereModeEnabled` | `bool` | – | – |
| Default Vehicle State Name | `defaultVehicleStateName` | `string` | "Sphere" | – |

### Vehicle Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Info List | `vehicleInfoList` | `List<vehicleInfo>` | new List<vehicleInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Using Sphere Mode | `usingSphereMode` | `bool` | – | – |
| Is External Vehicle Controller | `isExternalVehicleController` | `bool` | – | – |
| Current Rider System | `currentRiderSystem` | `mainRiderSystem` | – | – |
| Current Rider System Transform | `currentRiderSystemTransform` | `Transform` | – | – |
| Current Object To Control Transform | `currentObjectToControlTransform` | `Transform` | – | – |
| Current Object To Control | `currentObjectToControl` | `GameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Manager | `playerManager` | `playerController` | – | – |
| Gravity Manager | `gravityManager` | `gravitySystem` | – | – |
| Using Devices Manager | `usingDevicesManager` | `usingDevicesSystem` | – | – |
| Player Collider | `playerCollider` | `Collider` | – | – |
| Main Override Element Control System | `mainOverrideElementControlSystem` | `overrideElementControlSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentVehicleInfo(string newVehicleInfoName)` | 名前一致の車両情報を現在に設定し、他の項目を解除して必要なら球体モードを終了、選択イベントを送出する。 |
| `toggleSphereModeActiveState()` | `usingSphereMode` を反転して `setSphereModeActiveState` に渡すだけ。 |
| `setSphereModeActiveState(bool state)` | 有効かつ使用可能なら、車両状態変更コルーチンを開始する。 |

## 内部型

- `vehicleInfo`（class）
