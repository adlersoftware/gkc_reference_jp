# spawnObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/spawnObject.cs:6`

**概要**: プレハブやオブジェクトを指定位置に生成するコンポーネントで、生成数・上限・プール利用・リモートイベント送信などを設定できる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Spawn Object Enabled | `spawnObjectEnabled` | `bool` | true | – |
| Object To Spawn | `objectToSpawn` | `GameObject` | – | – |
| Spawn Position | `spawnPosition` | `Transform` | – | – |
| Radius To Spawn | `radiusToSpawn` | `float` | – | – |
| Set Object Rotation | `setObjectRotation` | `bool` | true | – |
| Set Object Scale | `setObjectScale` | `bool` | – | – |
| New Object Scale | `newObjectScale` | `Vector3` | – | – |
| Spawn Amount Of Same Object | `spawnAmountOfSameObject` | `bool` | – | – |
| Amount Of Same Object To Spawn | `amountOfSameObjectToSpawn` | `int` | – | – |
| Spawn Objects On Start | `spawnObjectsOnStart` | `bool` | – | – |

### Pooling Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Spawn Object From Pooling System | `spawnObjectFromPoolingSystem` | `bool` | – | – |
| Check GKC Pooling Element On Spawned Object | `checkGKC_PoolingElementOnSpawnedObject` | `bool` | – | – |

### Spawn Local Position And Rotation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Spawn Reference Position | `useSpawnReferencePosition` | `bool` | – | – |
| Spawn Reference Position | `spawnReferencePosition` | `Transform` | – | – |
| Set Spawned Object Parent | `setSpawnedObjectParent` | `bool` | – | – |
| Spawned Object Parent | `spawnedObjectParent` | `Transform` | – | – |

### Spawn Raycast Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Raycast To Spawn Object | `useRaycastToSpawnObject` | `bool` | – | – |
| Layer To Spawn Object | `layerToSpawnObject` | `LayerMask` | – | – |
| Use Infinite Raycast Distance | `useInfiniteRaycastDistance` | `bool` | – | – |
| Raycast Distance | `raycastDistance` | `float` | – | – |
| Raycast Spawn Object Offset | `raycastSpawnObjectOffset` | `Vector3` | – | – |
| Launch Raycast To Down Direction | `launchRaycastToDownDirection` | `bool` | – | – |
| Adjust Spawned Object To Surface Normal | `adjustSpawnedObjectToSurfaceNormal` | `bool` | – | – |
| Ignore Rigidbodies On Raycast | `ignoreRigidbodiesOnRaycast` | `bool` | – | – |

### Spawn List Of Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Spawn Object List | `spawnObjectList` | `bool` | – | – |
| Object List To Spawn | `objectListToSpawn` | `List<GameObject>` | new List<GameObject> () | – |
| Use Custom Spawn Object List | `useCustomSpawnObjectList` | `bool` | – | – |
| Spawnable Object Info List | `spawnableObjectInfoList` | `List<spawnableObjectInfo>` | new List<spawnableObjectInfo> () | – |

### Store Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Store Spawned Objects | `storeSpawnedObjects` | `bool` | – | – |
| Spawned Object List | `spawnedObjectList` | `List<GameObject>` | new List<GameObject> () | – |

### Spawn Limit Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Spawn Limit Amount | `useSpawnLimitAmount` | `bool` | – | – |
| Spawn Limit Amount | `spawnLimitAmount` | `int` | – | – |
| Check If Objects Spawned Are Dead | `checkIfObjectsSpawnedAreDead` | `bool` | – | – |
| Event On Limit Reached | `eventOnLimitReached` | `UnityEvent` | – | – |
| Event On Limit Not Reached | `eventOnLimitNotReached` | `UnityEvent` | – | – |

### Spawn Possibility Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Random Possibility To Spawn | `useRandomPossibilityToSpawn` | `bool` | – | – |
| Possibility To Spawn | `possibilityToSpawn` | `float` | – | Range (0, 100) |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Send Spawned Object On Event | `sendSpawnedObjectOnEvent` | `bool` | – | – |
| Event To Send S Pawned Object | `eventToSendSPawnedObject` | `eventParameters.eventToCallWithGameObject` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Send Spawned Object On Remote Event | `sendSpawnedObjectOnRemoteEvent` | `bool` | – | – |
| Remote Event To Send Object | `remoteEventToSendObject` | `string` | – | – |
| Use Remove Event List | `useRemoveEventList` | `bool` | – | – |
| Remove Event Name List | `removeEventNameList` | `List<remoteEventInfo>` | new List<remoteEventInfo> () | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Number Of Spawn Objects | `currentNumberOfSpawnObjects` | `int` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCustomPositionToSpawn(Vector3 newPosition)` | `customPositionToSpawn` を設定するだけ。 |
| `setCustomPositionOffsetYToSpawn(float newOffset)` | `customPositionOffsetYToSpawn` を設定するだけ。 |
| `activateSpawnObject()` | 有効時、設定されたリストまたは単一オブジェクトを指定個数だけ `createObject` で生成する。 |
| `createObject(GameObject newObject)` | 発生確率と上限を確認してオブジェクトを生成し、位置・親・向きを整えてリスト登録とイベント送信を行う。 |
| `checkIfSpawnObjectsListNull()` | 生成リストから null や死亡した要素を取り除き、現在の生成数を更新する。 |
| `removeSpawnedObjectFromList(GameObject objectToCheck)` | 一致する生成オブジェクトをリストから削除し、生成数を更新する。 |
| `getLastObjectSpawned()` | 最後に生成したオブジェクトを返すだけ。 |
| `checkEventsOnSpawnLimits()` | 生成数が上限以上かどうかで到達/未到達イベントを発火する。 |
| `destroySpawnedObjects()` | `storeSpawnedObjects` が有効なら生成済みオブジェクトをすべて破棄してリストを空にする。 |
| `setAmountOfSameObjectToSpawn(int newValue)` | `amountOfSameObjectToSpawn` を設定するだけ。 |
| `setSpawnObjectEnabledState(bool state)` | `spawnObjectEnabled` を設定するだけ。 |
| `enableRemovetEventState(string remoteEventName)` | `enableRemoteEventState` にそのまま委譲する。 |
| `disableRemovetEventState(string remoteEventName)` | `disableRemoteEventState` にそのまま委譲する。 |
| `enableOrDisableAllRemovetEventStates(bool state)` | `enableOrDisableAllRemoteEventStates` にそのまま委譲する。 |
| `enableRemoteEventState(string remoteEventName)` | 指定名のリモートイベントの有効フラグを true にする。 |
| `disableRemoteEventState(string remoteEventName)` | 指定名のリモートイベントの有効フラグを false にする。 |
| `enableOrDisableAllRemoteEventStates(bool state)` | リスト内すべてのリモートイベントの有効状態をまとめて設定する。 |
| `setObjectToSpawn(GameObject newObject)` | `objectToSpawn` を設定するだけ。 |
| `setSpawnPosition(Transform newTransform)` | `spawnPosition` を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnLimitReached` | `UnityEvent` | – |
| `eventOnLimitNotReached` | `UnityEvent` | – |

## 内部型

- `remoteEventInfo`（class）
- `spawnableObjectInfo`（class）
