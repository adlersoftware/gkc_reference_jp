# meleeWeaponOnInventory

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `objectOnInventory`
- **ソース**: `Inventory/Inventory Pickups Behaviour/meleeWeaponOnInventory.cs:5`

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Melee Weapon Pickup | `mainMeleeWeaponPickup` | `meleeWeaponPickup` | – | – |
| Check Events On Change Equip State | `checkEventsOnChangeEquipState` | `bool` | true | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`eventOnDropObject(GameObject currentPlayer)`, `eventOnPickObject(GameObject currentPlayer)`, `setObjectEquippedStateOnInventory(GameObject currentPlayer, bool state)`

</details>
