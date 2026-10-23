# objectExperienceSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Experience System/objectExperienceSystem.cs:6`

**概要**: オブジェクトから攻撃したキャラクターへ経験値・金額・インベントリアイテム・レシピなどの報酬を渡し、一度だけ付与する設定も持つコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Give Reward Only Once Enabled | `giveRewardOnlyOnceEnabled` | `bool` | – | – |

### Experience Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Experience Random Range | `useExperienceRandomRange` | `bool` | – | – |
| Experience Random Range | `experienceRandomRange` | `Vector2` | – | – |
| Experience Amount | `experienceAmount` | `int` | – | – |
| Use Transform As Exp Text Position | `useTransformAsExpTextPosition` | `bool` | true | – |
| Object Transform | `objectTransform` | `Transform` | – | – |
| Extra Experience Text | `extraExperienceText` | `string` | – | – |

### Money Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Money Random Range | `useMoneyRandomRange` | `bool` | – | – |
| Money Random Range | `moneyRandomRange` | `Vector2` | – | – |
| Money Amount | `moneyAmount` | `int` | – | – |

### Inventory Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Give Inventory Object | `giveInventoryObject` | `bool` | – | – |
| Inventory Object Name | `inventoryObjectName` | `string` | – | – |
| Inventory Object Amount | `inventoryObjectAmount` | `int` | – | – |
| Only Refill Certain Amount Of Inventory Object Amount | `onlyRefillCertainAmountOfInventoryObjectAmount` | `bool` | – | – |
| Position To Instantiate Inventory Object Pickup | `positionToInstantiateInventoryObjectPickup` | `Transform` | – | – |
| Max Radius To Instantiate | `maxRadiusToInstantiate` | `float` | – | – |
| Force Amount | `forceAmount` | `float` | – | – |
| Force Radius | `forceRadius` | `float` | – | – |
| Inventory Object Force Mode | `inventoryObjectForceMode` | `ForceMode` | – | – |
| Spawn All Inventory Objects | `spawnAllInventoryObjects` | `bool` | – | – |
| Spawn Object If Not Enough Space On Inventory | `spawnObjectIfNotEnoughSpaceOnInventory` | `bool` | true | – |
| Give Random Single Object From List | `giveRandomSingleObjectFromList` | `bool` | – | – |
| Give Inventory Object List | `giveInventoryObjectList` | `bool` | – | – |
| Inventory Element Info List | `inventoryElementInfoList` | `List<inventoryElementInfo>` | new List<inventoryElementInfo> () | – |
| Get Inventory Objects From Inventory Bank | `getInventoryObjectsFromInventoryBank` | `bool` | – | – |
| Main Inventory Bank System | `mainInventoryBankSystem` | `inventoryBankSystem` | – | – |

### Stamina Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Refill Stamina | `refillStamina` | `bool` | – | – |
| Refill Full Stamina | `refillFullStamina` | `bool` | – | – |
| Stamina Amount To Refill | `staminaAmountToRefill` | `float` | – | – |

### Inventory Extra Slots Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Increase Inventory Slots Amount | `increaseInventorySlotsAmount` | `bool` | – | – |
| Extra Inventory Slots Amount | `extraInventorySlotsAmount` | `int` | – | – |

### Inventory Extra Weight Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Increase Inventory Weight Limit | `increaseInventoryWeightLimit` | `bool` | – | – |
| Extra Weight Limit | `extraWeightLimit` | `float` | – | – |

### Stats To Increase Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Increase Stats Values | `increaseStatsValues` | `bool` | – | – |
| Stat Info List | `statInfoList` | `List<statInfo>` | new List<statInfo> () | – |

### Skill Points Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Get Skill Points | `getSkillPoints` | `bool` | – | – |
| Use Skill Points Random Range | `useSkillPointsRandomRange` | `bool` | – | – |
| Skill Points Random Range | `skillPointsRandomRange` | `Vector2` | – | – |
| Skill Points Amount | `skillPointsAmount` | `int` | – | – |

### Skill Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Get Skill | `getSkill` | `bool` | – | – |
| Skill To Get Name | `skillToGetName` | `string` | – | – |
| Get Skill List | `getSkillList` | `bool` | – | – |
| Skill To Get Name List | `skillToGetNameList` | `List<string>` | new List<string> () | – |
| Show Message On Get Skill | `showMessageOnGetSkill` | `bool` | – | – |
| Message On Get Skill | `messageOnGetSkill` | `string` | – | Write -SKILLNAME- in the string to replace that part of the message with the name of the skill. |

### Abilities Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Get Ability | `getAbility` | `bool` | – | – |
| Ability To Get Name | `abilityToGetName` | `string` | – | – |
| Get Ability List | `getAbilityList` | `bool` | – | – |
| Ability To Get Name List | `abilityToGetNameList` | `List<string>` | new List<string> () | – |
| Show Message On Get Ability | `showMessageOnGetAbility` | `bool` | – | – |
| Message On Get Ability | `messageOnGetAbility` | `string` | – | Write -ABILITYNAME- in the string to replace that part of the message with the name of the skill. |

### Crafting Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Get Crafting Recipes | `getCraftingRecipes` | `bool` | – | – |
| Crafting Recipes List | `craftingRecipesList` | `List<string>` | new List<string> () | – |

### Player Manual Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Player Manually | `setPlayerManually` | `bool` | – | – |
| Send Always To Main Player | `sendAlwaysToMainPlayer` | `bool` | – | – |
| Search Player By Tag If Not Assigned | `searchPlayerByTagIfNotAssigned` | `bool` | true | – |
| Player To Configure | `playerToConfigure` | `GameObject` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Events | `useRemoteEvents` | `bool` | – | – |
| Remove Event Name List | `removeEventNameList` | `List<string>` | new List<string> () | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Reward | `useEventOnReward` | `bool` | – | – |
| Eventt On Reward | `eventtOnReward` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Reward Obtained | `rewardObtained` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `sendExperienceToPlayerManually()` | `setPlayerManually`が有効な時、設定済みプレイヤー`playerToConfigure`へ報酬処理を呼ぶだけ。 |
| `sendExperienceToPlayer(GameObject playerToUse)` | `setPlayerManually`なら`playerToConfigure`を、そうでなければ引数のプレイヤーを報酬処理へ渡す。 |
| `sendExperienceToAttacker(GameObject attackerGameObject)` | 一度だけ設定を尊重し、乗り物なら運転手を対象に経験値・金額・アイテム等の報酬を与え、`rewardObtained`を立てる。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventtOnReward` | `UnityEvent` | – |

## 内部型

- `inventoryElementInfo`（class）
- `statInfo`（class）
