# getInventoryObjectSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/getInventoryObjectSystem.cs:6`

**概要**: シーン上に置かれ、プレイヤーへ指定のインベントリオブジェクト（または複数リスト）を付与する取得ポイント。付与は `applyDamage.giveInventoryObjectToCharacter` に委譲する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory Object Name | `inventoryObjectName` | `string` | – | – |
| Object Amount | `objectAmount` | `int` | – | – |
| Only Refill Certain Amount Of Inventory Object Amount | `onlyRefillCertainAmountOfInventoryObjectAmount` | `bool` | – | – |
| Give Inventory Object List | `giveInventoryObjectList` | `bool` | – | – |
| Inventory Element Info List | `inventoryElementInfoList` | `List<inventoryElementInfo>` | new List<inventoryElementInfo> () | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Spawn Object If Not Enough Space On Inventory | `spawnObjectIfNotEnoughSpaceOnInventory` | `bool` | true | – |
| Max Radius To Instantiate | `maxRadiusToInstantiate` | `float` | – | – |
| Force Amount | `forceAmount` | `float` | – | – |
| Force Radius | `forceRadius` | `float` | – | – |
| Inventory Object Force Mode | `inventoryObjectForceMode` | `ForceMode` | – | – |
| Spawn All Inventory Objects | `spawnAllInventoryObjects` | `bool` | – | – |
| Disable Get Object After Obtained | `disableGetObjectAfterObtained` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Obtained | `objectObtained` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event If Object Stored | `useEventIfObjectStored` | `bool` | – | – |
| Event If Object Stored | `eventIfObjectStored` | `UnityEvent` | – | – |

### Player Manual Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Player Manually | `setPlayerManually` | `bool` | – | – |
| Send Always To Main Player | `sendAlwaysToMainPlayer` | `bool` | – | – |
| Search Player By Tag If Not Assigned | `searchPlayerByTagIfNotAssigned` | `bool` | true | – |
| Player To Configure | `playerToConfigure` | `GameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Player | `currentPlayer` | `GameObject` | – | – |
| Position To Place Inventory Object | `positionToPlaceInventoryObject` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `removeCurrentPlayer(GameObject player)` | `currentPlayer` が `player` と一致する場合のみ `null` に戻す。 |
| `getCurrentPlayer(GameObject player)` | `currentPlayer` に `player` を代入するだけ（名前と違い設定用）。 |
| `giveObjectToPlayer()` | 設定名の品（または `inventoryElementInfoList` の各品）をプレイヤーに付与し、`objectObtained` を true にする。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventIfObjectStored` | `UnityEvent` | – |

## 内部型

- `inventoryElementInfo`（class）
