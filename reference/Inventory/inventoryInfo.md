# inventoryInfo

- **種別**: class
- **ソース**: `Inventory/inventoryInfo.cs:7`
- **属性**: `System.Serializable`

**概要**: インベントリ 1 オブジェクト分のデータを保持するシリアライズ可能クラス。名前・アイコン・数量・使用可否・武器情報・重量などをまとめ、コピー用コンストラクタも持つ。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Name | `Name` | `string` | – | – |
| Inventory Game Object | `inventoryGameObject` | `GameObject` | – | – |
| Object Info | `objectInfo` | `string` | – | TextArea (3, 10) |
| Icon | `icon` | `Texture` | – | – |
| Amount | `amount` | `int` | – | – |
| Amount Per Unit | `amountPerUnit` | `int` | – | – |
| Infinite Amount | `infiniteAmount` | `bool` | – | – |
| Store Total Amount Per Unit | `storeTotalAmountPerUnit` | `bool` | – | – |
| Show Amount Per Unit In Amount Text | `showAmountPerUnitInAmountText` | `bool` | – | – |
| Can Be Used | `canBeUsed` | `bool` | – | – |
| Can Be Equiped | `canBeEquiped` | `bool` | – | – |
| Can Be Dropped | `canBeDropped` | `bool` | – | – |
| Can Be Combined | `canBeCombined` | `bool` | – | – |
| Can Be Examined | `canBeExamined` | `bool` | true | – |
| Can Be Discarded | `canBeDiscarded` | `bool` | – | – |
| Hide Slot On Menu | `hideSlotOnMenu` | `bool` | – | – |
| Use New Behavior On Use | `useNewBehaviorOnUse` | `bool` | – | – |
| New Behavior On Use Message | `newBehaviorOnUseMessage` | `string` | – | TextArea (3, 10) |
| New Behavior On Unable To Use Message | `newBehaviorOnUnableToUseMessage` | `string` | – | TextArea (3, 10) |
| Use New Behavior On Combine | `useNewBehaviorOnCombine` | `bool` | – | – |
| New Behavior On Combine Message | `newBehaviorOnCombineMessage` | `string` | – | TextArea (3, 10) |
| Use One Unit On New Behaviour Combine | `useOneUnitOnNewBehaviourCombine` | `bool` | true | – |
| Use Sound On Use Object | `useSoundOnUseObject` | `bool` | – | – |
| Sound On Use Object | `soundOnUseObject` | `AudioClip` | – | – |
| On Use Object Audio Element | `onUseObjectAudioElement` | `AudioElement` | – | – |
| Is Equipped | `isEquipped` | `bool` | – | – |
| Quick Access Slot Index | `quickAccessSlotIndex` | `int` | -1 | – |
| Use Durability | `useDurability` | `bool` | – | – |
| Durability Amount | `durabilityAmount` | `float` | 100 | – |
| Max Durability Amount | `maxDurabilityAmount` | `float` | 100 | – |
| Object Is Broken | `objectIsBroken` | `bool` | – | – |
| Sell Multiplier If Object Is Broken | `sellMultiplierIfObjectIsBroken` | `float` | 1 | – |
| Is Weapon | `isWeapon` | `bool` | – | – |
| Is Melee Weapon | `isMeleeWeapon` | `bool` | – | – |
| Is Melee Shield | `isMeleeShield` | `bool` | – | – |
| Is Armor Cloth Accessory | `isArmorClothAccessory` | `bool` | – | – |
| Projectiles In Magazine | `projectilesInMagazine` | `int` | -1 | – |
| Main Weapon Object Info | `mainWeaponObjectInfo` | `weaponObjectInfo` | – | – |
| Object To Combine | `objectToCombine` | `GameObject` | – | – |
| Combined Object | `combinedObject` | `GameObject` | – | – |
| Combined Object Message | `combinedObjectMessage` | `string` | – | TextArea (3, 10) |
| Can Be Sold | `canBeSold` | `bool` | true | – |
| Vendor Price | `vendorPrice` | `float` | – | – |
| Infinite Vendor Amount Available | `infiniteVendorAmountAvailable` | `bool` | – | – |
| Category Name | `categoryName` | `string` | – | – |
| Category Index | `categoryIndex` | `int` | – | – |
| Element Index | `elementIndex` | `int` | – | – |
| Sell Price | `sellPrice` | `float` | – | – |
| Use Min Level To Buy | `useMinLevelToBuy` | `bool` | – | – |
| Min Level To Buy | `minLevelToBuy` | `float` | – | – |
| Weight | `weight` | `float` | – | – |
| Spawn Object | `spawnObject` | `bool` | – | – |
| Use Custom Object To Drop | `useCustomObjectToDrop` | `bool` | – | – |
| Custom Object To Drop | `customObjectToDrop` | `GameObject` | – | – |
| Drop Object Offset | `dropObjectOffset` | `Vector3` | – | – |
| Cant Be Stored On Inventory | `cantBeStoredOnInventory` | `bool` | – | – |
| Can Be Held | `canBeHeld` | `bool` | – | – |
| Can Be Place On Quick Access Slot | `canBePlaceOnQuickAccessSlot` | `bool` | – | – |
| Can Be Set On Quick Slots | `canBeSetOnQuickSlots` | `bool` | – | – |
| Set Maximum Amount Per Slot | `setMaximumAmountPerSlot` | `bool` | – | – |
| Maximum Amount Per Slot | `maximumAmountPerSlot` | `int` | – | – |
| Set Maximum Object Amount | `setMaximumObjectAmount` | `bool` | – | – |
| Maximum Object Amount | `maximumObjectAmount` | `int` | – | – |
| Button | `button` | `Button` | – | – |
| Menu Icon Element | `menuIconElement` | `inventoryMenuIconElement` | – | – |
| Inventory Object Prefab | `inventoryObjectPrefab` | `GameObject` | – | – |
| Current Vendor Object Slot Panel Info | `currentVendorObjectSlotPanelInfo` | `vendorObjectSlotPanelInfo` | – | – |
| Empty Inventory Prefab | `emptyInventoryPrefab` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `InitializeAudioElements()` | `soundOnUseObject` が null でなければ `onUseObjectAudioElement.clip` に割り当てる。 |
| `setNewName(string newName)` | `Name` を `newName` に置き換えるだけ。 |
| `resetInventoryInfo()` | 全項目を空スロット用の既定値（`amount` 0、各種可否 false など）に戻し、`menuIconElement` の表示もクリアする。 |
| `copyInventoryObject(inventoryInfo objectToStore, inventoryInfo objectToCopy)` | `objectToCopy` の各設定値・状態・アイコンを `objectToStore` に複製し、`objectToStore` を返す。 |
