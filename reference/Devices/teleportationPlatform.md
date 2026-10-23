# teleportationPlatform

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/teleportationPlatform.cs:5`

**概要**: 触れたオブジェクトを対向する転送先プラットフォームへ送る。位置・回転・重力方向の調整とイベント発火を行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Teleport Enabled | `teleportEnabled` | `bool` | true | – |
| Platform To Move | `platformToMove` | `Transform` | – | – |
| Layermask | `layermask` | `LayerMask` | – | – |
| Use Button To Activate | `useButtonToActivate` | `bool` | – | – |

### Check Layer Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Object Layer To Teleport | `checkObjectLayerToTeleport` | `bool` | – | – |
| Object Layer To Teleport | `objectLayerToTeleport` | `LayerMask` | – | – |
| Ignore Vehicles To Teleport | `ignoreVehiclesToTeleport` | `bool` | – | – |
| Vehicle Radius Multiplier | `vehicleRadiusMultiplier` | `float` | 0.5f | – |

### Rotation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Object Rotation | `setObjectRotation` | `bool` | – | – |
| Set Full Object Rotation | `setFullObjectRotation` | `bool` | – | – |
| Adjust Player Camera Rotation If Player Teleported | `adjustPlayerCameraRotationIfPlayerTeleported` | `bool` | – | – |
| Object Rotation Transform | `objectRotationTransform` | `Transform` | – | – |

### Gravity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Gravity Direction | `setGravityDirection` | `bool` | – | – |
| Set Gravity Manager | `setGravityManager` | `setGravity` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Inside | `objectInside` | `GameObject` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Call Event On Teleport | `callEventOnTeleport` | `bool` | – | – |
| Event On Teleport | `eventOnTeleport` | `UnityEvent` | – | – |
| Call Event On Every Teleport | `callEventOnEveryTeleport` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Platform To Move Manager | `platformToMoveManager` | `teleportationPlatform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `removeObjectInside()` | `objectInside`を`null`にするだけ。 |
| `activateTeleport()` | 転送先プラットフォームを取得して`sendObject`で送り、内部参照を解除し、設定に応じイベントを発火する。 |
| `sendObject(GameObject objectToMove)` | レイキャストで着地点を求め、乗り物は半径分浮かせ、任意で回転・カメラ・重力方向を調整して移動する。 |
| `setTeleportEnabledState(bool state)` | `teleportEnabled`を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnTeleport` | `UnityEvent` | – |
