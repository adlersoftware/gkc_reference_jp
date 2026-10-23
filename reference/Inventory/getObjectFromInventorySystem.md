# getObjectFromInventorySystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/getObjectFromInventorySystem.cs:6`

**概要**: プレイヤーのインベントリに対象オブジェクトが何個あるかを確認し、使用（消費）やイベント発火を行うコンポーネント。判定には `extraInventoryObjectAmount` を加味した残量を使う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory Object Name | `inventoryObjectName` | `string` | – | – |
| Use Infinite Objects | `useInfiniteObjects` | `bool` | – | – |
| Check Inventory Manager | `checkInventoryManager` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Extra Inventory Object Amount | `extraInventoryObjectAmount` | `int` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Object Found On Inventory | `eventOnObjectFoundOnInventory` | `UnityEvent` | – | – |
| Event On Object Not Found On Inventory | `eventOnObjectNotFoundOnInventory` | `UnityEvent` | – | – |
| Event On Amount Available | `eventOnAmountAvailable` | `UnityEvent` | – | – |
| Event On Amount Not Available | `eventOnAmountNotAvailable` | `UnityEvent` | – | – |
| Main Inventory Manager | `mainInventoryManager` | `inventoryManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `addExtraInventoryObjectAmount(int extraAmount)` | `extraInventoryObjectAmount` に `extraAmount` を加算し、負値にならないよう 0 で下限を切る。 |
| `checkIfObjectFoundOnInventory()` | 残量（無限なら 1、追加分を加算）が 0 より大きいかで found／not found イベントを発火する。 |
| `useInventoryObject(int amountToUse)` | 残量が `amountToUse` 以上なら在庫からその分を削除して使用可能イベントを、不足なら不可イベントを発火する。 |
| `useInventoryObjectAndGetResult(int amountToUse)` | `useInventoryObject` と同じ判定と在庫消費を行い、成否を `bool` で返す。 |
| `setCurrentPlayer(GameObject newPlayer)` | プレイヤーの `playerComponentsManager` から `mainInventoryManager` を取得して保持する。 |
| `setNewInventoryObjectName(string newName)` | `inventoryObjectName` を `newName` に差し替えるだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnObjectFoundOnInventory` | `UnityEvent` | – |
| `eventOnObjectNotFoundOnInventory` | `UnityEvent` | – |
| `eventOnAmountAvailable` | `UnityEvent` | – |
| `eventOnAmountNotAvailable` | `UnityEvent` | – |
