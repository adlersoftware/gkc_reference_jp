# objectOnInventory

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/Inventory Pickups Behaviour/objectOnInventory.cs:5`

**概要**: インベントリ上のオブジェクト挙動を派生クラス向けに定義する基底コンポーネント。使用・結合・装備の空実装と、リモートイベント/アビリティ/ステータス/レシピ/条件判定の共通処理を提供する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Inventory Object | `mainInventoryObject` | `inventoryObject` | – | – |
| Use Only Amount Needed | `useOnlyAmountNeeded` | `bool` | – | – |
| Close Inventory On Object Used | `closeInventoryOnObjectUsed` | `bool` | – | – |

### Condition Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Conditions To Use Object Enabled | `checkConditionsToUseObjectEnabled` | `bool` | – | – |
| Player On Ground To Use Object | `playerOnGroundToUseObject` | `bool` | – | – |
| Action System Not Playing Animations | `actionSystemNotPlayingAnimations` | `bool` | – | – |
| Use Custom Message On Condition Failed | `useCustomMessageOnConditionFailed` | `bool` | – | – |
| Custom Message On Condition Failed | `customMessageOnConditionFailed` | `string` | – | TextArea (3, 10) |
| Custom Message On Not Able To Equip | `customMessageOnNotAbleToEquip` | `string` | "-OBJECT- can't be equipped" | TextArea (3, 10) |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event | `useRemoteEvent` | `bool` | – | – |
| Remote Event List | `remoteEventList` | `List<string>` | new List<string> () | – |

### Remote Events On Use Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Use Object | `useRemoteEventOnUseObject` | `bool` | – | – |
| Remote Event List On Use Object | `remoteEventListOnUseObject` | `List<string>` | new List<string> () | – |

### Remote Events On Equip Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Equip Object | `useRemoteEventOnEquipObject` | `bool` | – | – |
| Remote Event List On Equip Object | `remoteEventListOnEquipObject` | `List<string>` | new List<string> () | – |
| Use Remote Event On Unequip Object | `useRemoteEventOnUnequipObject` | `bool` | – | – |
| Remote Event List On Unquip Object | `remoteEventListOnUnquipObject` | `List<string>` | new List<string> () | – |

### Enable Abilities on Equip Inventory Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Abilities List To Enable On Equip Inventory Object | `useAbilitiesListToEnableOnEquipInventoryObject` | `bool` | – | – |
| Abilities List To Enable On Equip Inventory Object | `abilitiesListToEnableOnEquipInventoryObject` | `List<string>` | new List<string> () | – |

### Enable Abilities on Use Inventory Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Abilities List To Enable On Use Inventory Object | `useAbilitiesListToEnableOnUseInventoryObject` | `bool` | – | – |
| Abilities List To Enable On Use Inventory Object | `abilitiesListToEnableOnUseInventoryObject` | `List<string>` | new List<string> () | – |

### Activate Abilities on Use Inventory Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Ability On Use Inventory Object | `activateAbilityOnUseInventoryObject` | `bool` | – | – |
| Ability Name To Active On Use Inventory Object | `abilityNameToActiveOnUseInventoryObject` | `string` | – | – |
| Ability Is Temporally Activated | `abilityIsTemporallyActivated` | `bool` | – | – |
| Check If Ability Is Not Active Or On Cool Down | `checkIfAbilityIsNotActiveOrOnCoolDown` | `bool` | – | – |

### Stats To Increase Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Increase Stats Values | `increaseStatsValues` | `bool` | – | – |
| Stats To Increase Info List | `statsToIncreaseInfoList` | `List<objectExperienceSystem.statInfo>` | new List<objectExperienceSystem.statI… | – |

### Crafting Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Get Crafting Recipes | `getCraftingRecipes` | `bool` | – | – |
| Crafting Recipes List | `craftingRecipesList` | `List<string>` | new List<string> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateUseObjectActionOnInventory(GameObject currentPlayer, int amountToUse)` | 本体が空で何もしない。派生クラスで上書きする仮想メソッド。 |
| `activateUseObjectActionOnInventoryWithExternalCharacter(GameObject currentPlayer, GameObject currentExternalCharacterForInventoryUsage, int amountToUse)` | 本体が空で何もしない。外部キャラクター用に派生クラスで上書きする。 |
| `activateCombineObjectActionOnInventory(GameObject currentPlayer, inventoryInfo inventoryInfoToUse)` | 本体が空で何もしない。合成処理を派生クラスで実装する仮想メソッド。 |
| `carryPhysicalObjectFromInventory(GameObject currentPlayer)` | 本体が空で何もしない。物理オブジェクト所持を派生クラスで実装する。 |
| `eventOnPickObject(GameObject currentPlayer)` | 本体が空で何もしない。取得時処理を派生クラスで実装する。 |
| `eventOnDropObject(GameObject currentPlayer)` | 本体が空で何もしない。ドロップ時処理を派生クラスで実装する。 |
| `checkRemoteEvents(GameObject currentPlayer)` | `useRemoteEvent`有効時、プレイヤーの`remoteEventSystem`へ`remoteEventList`の各イベントを送る。 |
| `checkRemoteEventsOnUseObject(GameObject currentPlayer)` | 使用時用の設定が有効なら`remoteEventListOnUseObject`の各イベントをプレイヤーへ送る。 |
| `checkRemoteEventsOnSetObjectEquipState(GameObject currentPlayer, bool state)` | 装備/解除の設定に応じ、対応するリストのリモートイベントをプレイヤーへ送る。 |
| `setObjectEquippedStateOnInventory(GameObject currentPlayer, bool state)` | 本体が空で常にfalseを返す。装備状態処理を派生クラスで実装する。 |
| `checkIfEnableAbilitiesOnEquipInventoryObject(GameObject currentPlayer, bool state)` | 設定有効ならプレイヤーのアビリティ群を`state`に合わせて一括有効/無効化する。 |
| `checkIfEnableAbilitiesOnUseInventoryObject(GameObject currentPlayer)` | 使用時用リストのアビリティ群をプレイヤーで有効化する。 |
| `checkIfActivateAbilitiesOnUseInventoryObject(GameObject currentPlayer)` | 指定アビリティをプレイヤーで発動し、一時発動フラグも渡す。 |
| `checkIfAbilitiesOnUseOrCooldown(GameObject currentPlayer)` | 対象アビリティが発動中かクールダウン中かを問い合わせて返す。 |
| `checkIfIncreaseStatsOnUseInventoryObject(GameObject currentPlayer)` | 設定有効なら`statsToIncreaseInfoList`のステータスをプレイヤーに加算する。 |
| `checkIfaddNewBlueprintsUnlockedList(GameObject currentPlayer)` | 設定有効なら`craftingRecipesList`をプレイヤーの解禁ブループリントに追加する。 |
| `checkConditions(GameObject currentPlayer)` | 接地・行動アニメーション停止の条件を満たさなければfalseを返す判定。 |
| `checkExternalElementsOnUseInventoryObject(GameObject currentPlayer)` | 使用時のアビリティ・ステータス・レシピ・リモートイベントをまとめて実行する。 |
| `getCustomMessageOnNotAbleToEquip()` | `customMessageOnNotAbleToEquip`を返すだけ。 |
