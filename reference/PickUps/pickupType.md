# pickupType

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `PickUps/Pickups Behaviour/pickupType.cs:5`

**概要**: 拾えるオブジェクトの基底クラスで、取得可否の判定、取得確定、取得メッセージ表示、アビリティ解放や設計図追加といった共通処理を持つ。個々の取得挙動はサブクラスが上書きして実装する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Store Pickup On Inventory | `storePickupOnInventory` | `bool` | – | – |
| Use Inventory Object When Picked | `useInventoryObjectWhenPicked` | `bool` | – | – |

### Pickup Message Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Pickup Message | `useCustomPickupMessage` | `bool` | true | – |
| Object Taken As Pickup Message | `objectTakenAsPickupMessage` | `string` | – | TextArea (5, 15) |
| Object Taken As Inventory Message | `objectTakenAsInventoryMessage` | `string` | – | TextArea (5, 15) |
| Explanation | `explanation` | `string` | "Use -AMOUNT- in the position of the … | TextArea (2, 6) |

### Enable Abilities on Use Take Pickup Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Abilities List To Enable On Take Pickup | `useAbilitiesListToEnableOnTakePickup` | `bool` | – | – |
| Abilities List To Enable On Take Pickup | `abilitiesListToEnableOnTakePickup` | `List<string>` | new List<string> () | – |

### Activate Abilities on Take Pickup Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Ability On Take Pickup | `activateAbilityOnTakePickup` | `bool` | – | – |
| Ability Name To Active On Take Pickup | `abilityNameToActiveOnTakePickup` | `string` | – | – |
| Ability Is Temporally Activated | `abilityIsTemporallyActivated` | `bool` | – | – |

### Crafting Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Get Crafting Recipes | `getCraftingRecipes` | `bool` | – | – |
| Crafting Recipes List | `craftingRecipesList` | `List<string>` | new List<string> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Pickup Object | `mainPickupObject` | `pickUpObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `takePickupByButton()` | 状態を同期し、取得可能なら `confirmTakePickupByButton` を呼ぶ。 |
| `takePickupByTrigger()` | 状態を同期し、取得可能なら `confirmTakePickupByTrigger` を呼ぶ。 |
| `assignPickupObjectState()` | 取得者情報とトリガー取得フラグを `mainPickupObject` からコピーし、取得可否を false に戻す。 |
| `checkIfCanBePicked()` | `canPickCurrentObject` を返すだけ。 |
| `confirmTakePickup()` | 本体が空で何もしない。 |
| `showPickupTakenMessage(int amountToShow)` | `-AMOUNT-` を個数に置換した文言を `showRecieveInfo` で表示する（保存時は在庫用文言）。 |
| `showPickupTakenMessage(string messageToUse)` | 空でない文言をそのまま `mainPickupObject.showRecieveInfo` で表示する。 |
| `checkIfUseInventoryObjectWhenPicked()` | インベントリ保存かつ使用設定のとき、`useInventoryObjectByName` で対象オブジェクトを1個使用する。 |
| `checkIfEnableAbilitiesOnTakePickup(GameObject currentPlayer)` | 設定された能力リストの能力群を `currentPlayer` に対して有効化する。 |
| `checkIfActivateAbilitiesOnTakePickup(GameObject currentPlayer)` | 指定能力を `currentPlayer` で発動し、一時発動フラグも渡す。 |
| `checkIfaddNewBlueprintsUnlockedList(GameObject currentPlayer)` | `craftingRecipesList` の設計図を `currentPlayer` に追加する。 |
| `setObjectTakenAsPickupMessage(string newMessage)` | `objectTakenAsPickupMessage` を設定するだけ。 |
| `setObjectTakenAsInventoryMessage(string newMessage)` | `objectTakenAsInventoryMessage` を設定するだけ。 |
| `renameObject(string newName)` | 本体が空で何もしない（サブクラスで上書きするための仮想メソッド）。 |
