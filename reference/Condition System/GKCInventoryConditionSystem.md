# GKCInventoryConditionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `GKCConditionInfo`
- **ソース**: `Condition System/GKCInventoryConditionSystem.cs:5`

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory Condition Info List | `inventoryConditionInfoList` | `List<inventoryConditionInfo>` | new List<inventoryConditionInfo> () | – |
| Check If Inventory Is Empty | `checkIfInventoryIsEmpty` | `bool` | – | – |
| Check If Any Weapon Is Equipped | `checkIfAnyWeaponIsEquipped` | `bool` | – | – |
| Any Weapon Must Be Equipped | `anyWeaponMustBeEquipped` | `bool` | – | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkIfConditionComplete()`, `checkIfConditionCompleteAndReturnResult()`

</details>

## 内部型

- `inventoryConditionInfo`（class）
