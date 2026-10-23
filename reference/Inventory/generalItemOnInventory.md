# generalItemOnInventory

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `objectOnInventory`
- **ソース**: `Inventory/generalItemOnInventory.cs:5`

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Stat Info List | `statInfoList` | `List<statInfo>` | new List<statInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`activateUseObjectActionOnInventory(GameObject currentPlayer, int amountToUse)`, `activateUseObjectActionOnInventoryWithExternalCharacter(GameObject currentPlayer, GameObject currentExternalCharacterForInventoryUsage, int amountToUse)`, `setObjectEquippedStateOnInventory(GameObject currentPlayer, bool state)`

</details>

## 内部型

- `statInfo`（class）
