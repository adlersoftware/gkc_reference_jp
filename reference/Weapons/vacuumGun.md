# vacuumGun

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/New Weapon Behaviors/vacuumGun.cs:5`

**概要**: カメラ前方のオブジェクトを吸い寄せて保持し、射出もできる吸引銃の挙動。掴んだ物のレイヤーを退避して復元する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vacuum Enabled | `vacuumEnabled` | `bool` | true | – |
| Layer To Detect | `layerToDetect` | `LayerMask` | – | – |
| Ignore Objects Tag | `ignoreObjectsTag` | `bool` | – | – |
| Tags To Ignore | `tagsToIgnore` | `List<string>` | new List<string> () | – |
| Layer To Set On Objects Found | `layerToSetOnObjectsFound` | `string` | "Ignore Raycast" | – |
| Max Distance Grab | `maxDistanceGrab` | `float` | – | – |
| Store Objects On Inventory | `storeObjectsOnInventory` | `bool` | – | – |
| Min Distance To Store Objects | `minDistanceToStoreObjects` | `float` | – | – |
| Vacuum Speed | `vacuumSpeed` | `float` | 10 | – |
| Hold Distance | `holdDistance` | `float` | 3 | – |
| Destroy All Objects On Reach Position | `destroyAllObjectsOnReachPosition` | `bool` | true | – |

### Expel Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Expel Enabled | `expelEnabled` | `bool` | – | – |
| Expel Transform Position | `expelTransformPosition` | `Transform` | – | – |
| Expel Rate | `expelRate` | `float` | 0.5f | – |
| Expel Force | `expelForce` | `float` | 20 | – |
| Expel Objects One By One | `expelObjectsOneByOne` | `bool` | – | – |

### Ignore Expel Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Inventory Object List To Expel | `ignoreInventoryObjectListToExpel` | `bool` | – | – |
| Ignore Inventory Object List To Expel List | `ignoreInventoryObjectListToExpelList` | `List<string>` | new List<string> () | – |
| Ignore Inventory Object Category List To Expel | `ignoreInventoryObjectCategoryListToExpel` | `bool` | – | – |
| Ignore Inventory Object Category List To Expel List | `ignoreInventoryObjectCategoryListToExpelList` | `List<string>` | new List<string> () | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Rotor | `useRotor` | `bool` | true | – |
| Rotor | `rotor` | `Transform` | – | – |
| Rotor Rotation Speed | `rotorRotationSpeed` | `float` | 10 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Expel Active | `expelActive` | `bool` | – | – |
| Vacuum Active | `vacuumActive` | `bool` | – | – |
| Rigidbody List | `rigidbodyList` | `List<Rigidbody>` | new List<Rigidbody> () | – |
| Rigidbody Info List | `rigidbodyInfoList` | `List<rigidbodyInfo>` | new List<rigidbodyInfo> () | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Events | `useRemoteEvents` | `bool` | – | – |
| Remove Event Name List | `removeEventNameList` | `List<string>` | new List<string> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Inventory Manager | `mainInventoryManager` | `inventoryManager` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | – |
| Main Player Weapon System | `mainPlayerWeaponSystem` | `playerWeaponSystem` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`があれば停止するだけ。 |
| `setVacuumEnabledState(bool state)` | 吸引中なら止めてから`vacuumEnabled`を設定する。 |
| `enableVacuum()` | `enableOrDisableVacuum(true)`を呼ぶだけ。 |
| `disableVacuum()` | `enableOrDisableVacuum(false)`を呼ぶだけ。 |
| `enableOrDisableVacuum(bool state)` | 有効時は保持距離を戻して更新を開始し、無効時はコルーチンを止めて掴みリストとレイヤーを復元する。 |
| `setExpelEnabledState(bool state)` | 射出中なら止めてから`expelEnabled`を設定する。 |
| `enableOrDisableExpel(bool state)` | 射出状態を設定し、開始時は更新を回して吸引を解除し、終了時はコルーチンを止める。 |

## 内部型

- `rigidbodyInfo`（class）
