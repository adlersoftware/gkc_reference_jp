# objectDistributorSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Grab Objects/objectDistributorSystem.cs:6`

**概要**: `objectToSpawn` を配置位置から生成して放出する自販機型のコンポーネント。残数制限、開閉アニメーション、生成／空／開閉イベントを扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Distributor Enabled | `distributorEnabled` | `bool` | true | – |
| Object To Spawn | `objectToSpawn` | `GameObject` | – | – |
| Use Spawn Limit | `useSpawnLimit` | `bool` | – | – |
| Spawn Limit | `spawnLimit` | `int` | – | – |
| Current Units Amount | `currentUnitsAmount` | `int` | – | – |
| Use Units Text | `useUnitsText` | `bool` | – | – |
| Units Text | `unitsText` | `TextMesh` | – | – |
| Position To Spawn | `positionToSpawn` | `Transform` | – | – |
| Animation Name | `animationName` | `string` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Open Distributor | `eventOnOpenDistributor` | `UnityEvent` | – | – |
| Event On Close Distributor | `eventOnCloseDistributor` | `UnityEvent` | – | – |
| Event On Empty Units | `eventOnEmptyUnits` | `UnityEvent` | – | – |
| Use Event On Object Instatiated | `useEventOnObjectInstatiated` | `bool` | – | – |
| Even On Object Instantiated | `evenOnObjectInstantiated` | `eventParameters.eventToCallWithGameObject` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Object Spawned | `currentObjectSpawned` | `GameObject` | – | – |
| Object Spawned | `objectSpawned` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Animation | `mainAnimation` | `Animation` | – | – |
| Main Collider | `mainCollider` | `Collider` | – | – |
| Electronic Device Manager | `electronicDeviceManager` | `electronicDevice` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `spawnObject()` | 無効時は何もせず、残数を減らして表示を更新し、生成コルーチンを開始してオブジェクトを出す。 |
| `stopDistributorCoroutine()` | `playAnimationCoroutine` があれば `StopCoroutine` するだけ。 |
| `removeDeviceFromList()` | `electronicDeviceManager` から現在のプレイヤーを得て、その `usingDevicesSystem` の操作対象一覧から自身を外す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnOpenDistributor` | `UnityEvent` | – |
| `eventOnCloseDistributor` | `UnityEvent` | – |
| `eventOnEmptyUnits` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnTriggerExit(Collider col)`

</details>
