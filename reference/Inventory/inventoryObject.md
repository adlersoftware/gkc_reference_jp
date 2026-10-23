# inventoryObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/inventoryObject.cs:4`

**概要**: シーン上のインベントリアイテム（`inventoryInfo` を保持）から、`objectOnInventory` の新挙動系メソッドを呼び出すラッパー。実処理はすべて `mainObjectOnInventory` に委譲する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory Object Info | `inventoryObjectInfo` | `inventoryInfo` | – | – |

### Main Inventory Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Object On Inventory | `mainObjectOnInventory` | `objectOnInventory` | – | – |

### Inventory Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Zoom Range | `useZoomRange` | `bool` | true | – |
| Max Zoom | `maxZoom` | `float` | 30 | – |
| Min Zoom | `minZoom` | `float` | 100 | – |
| Initial Zoom | `initialZoom` | `float` | 46 | – |
| Mesh Position Offset | `meshPositionOffset` | `Vector3` | – | – |
| Mesh Rotation Offset | `meshRotationOffset` | `Vector3` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `useObjectOnNewBehavior(GameObject currentPlayer, int amountToUse)` | `mainObjectOnInventory` の使用処理に `currentPlayer` と `amountToUse` を渡す。 |
| `useObjectOnNewBehaviorWithExternalCharacter(GameObject currentPlayer, GameObject currentExternalCharacterForInventoryUsage, int amountToUse)` | 使用処理を外部キャラクター対応版に 3 引数でそのまま委譲する。 |
| `combineObjectsOnNewBehavior(GameObject currentPlayer, inventoryInfo inventoryInfoToUse)` | `mainObjectOnInventory` の結合処理に `currentPlayer` と `inventoryInfoToUse` を渡す。 |
| `carryPhysicalObjectFromInventory(GameObject currentPlayer)` | `mainObjectOnInventory` の物理保持処理に `currentPlayer` を渡すだけ。 |
| `eventOnPickObjectNewBehaviour(GameObject currentPlayer)` | `mainObjectOnInventory.eventOnPickObject` を呼ぶだけ。 |
| `eventOnDropObjectNewBehaviour(GameObject currentPlayer)` | `mainObjectOnInventory.eventOnDropObject` を呼ぶだけ。 |
| `setObjectEquippedStateOnInventoryOnNewBehavior(GameObject currentPlayer, bool state)` | 装備状態の設定を `mainObjectOnInventory` に委譲し、その戻り値を返す（null 時は false）。 |
| `getCustomMessageOnNotAbleToEquip()` | `mainObjectOnInventory` から装備不可メッセージを取得して返し、null 時は空文字を返す。 |
