# weaponOnInventory

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `objectOnInventory`
- **ソース**: `Inventory/Inventory Pickups Behaviour/weaponOnInventory.cs:5`

**概要**: `objectOnInventory` を継承した武器用の挙動。ピックアップ時に残弾を武器へ引き継ぎ、ドロップ時に弾倉数を保存する。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Weapon Pickup | `mainWeaponPickup` | `weaponPickup` | – | – |
| Check Events On Change Equip State | `checkEventsOnChangeEquipState` | `bool` | true | – |
| Remaining Ammo | `remainingAmmo` | `int` | -1 | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getRemainingAmmoValue()` | `remainingAmmo` を返すだけ。 |
| `getWeaponPickup()` | `mainWeaponPickup` を返すだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`eventOnDropObject(GameObject currentPlayer)`, `eventOnPickObject(GameObject currentPlayer)`, `setObjectEquippedStateOnInventory(GameObject currentPlayer, bool state)`

</details>
