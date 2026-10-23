# sharedActionContent

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Action System/Shared Action System/sharedActionContent.cs:6`

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| First Character Is Player | `firstCharacterIsPlayer` | `bool` | – | – |

### Match Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Adjust Position To First Character | `adjustPositionToFirstCharacter` | `bool` | – | – |
| Adjust Position To Second Character | `adjustPositionToSecondCharacter` | `bool` | – | – |
| Match Position Used On Action | `matchPositionUsedOnAction` | `bool` | – | – |
| Adjust Match Position On First Character | `adjustMatchPositionOnFirstCharacter` | `bool` | – | – |
| Adjust Match Position On Second Character | `adjustMatchPositionOnSecondCharacter` | `bool` | – | – |
| Align Main Shared Action Game Object To Both Characters | `alignMainSharedActionGameObjectToBothCharacters` | `bool` | – | – |
| Resume Any Character If Action Finished | `resumeAnyCharacterIfActionFinished` | `bool` | – | – |

### Probability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Probability To Use Action | `useProbabilityToUseAction` | `bool` | – | – |
| Probability To Use Action | `probabilityToUseAction` | `float` | – | Range (0, 100) |

### Distance Condition Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Min Distance To Activate Action | `useMinDistanceToActivateAction` | `bool` | – | – |
| Min Distance To Activate Action | `minDistanceToActivateAction` | `float` | – | – |
| Use Min Angle To Activate Action | `useMinAngleToActivateAction` | `bool` | – | – |
| Min Angle To Activate Action | `minAngleToActivateAction` | `float` | – | – |

### Stats Condition Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Character Stats | `checkCharacterStats` | `bool` | – | – |
| Shared Action Condition Stat Info List | `sharedActionConditionStatInfoList` | `List<sharedActionConditionStatInfo>` | new List<sharedActionConditionStatInf… | – |

### Weapon Condition Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Weapons On First Character | `checkWeaponsOnFirstCharacter` | `bool` | – | – |
| Use Melee Weapon On First Character | `useMeleeWeaponOnFirstCharacter` | `bool` | – | – |
| Use Fire Weapon On First Character | `useFireWeaponOnFirstCharacter` | `bool` | – | – |
| Check Weapon Name On First Character | `checkWeaponNameOnFirstCharacter` | `bool` | – | – |
| Weapon Name On First Character | `weaponNameOnFirstCharacter` | `string` | – | – |
| Check Weapons On Second Character | `checkWeaponsOnSecondCharacter` | `bool` | – | – |
| Use Melee Weapon On Second Character | `useMeleeWeaponOnSecondCharacter` | `bool` | – | – |
| Use Fire Weapon On Second Character | `useFireWeaponOnSecondCharacter` | `bool` | – | – |
| Check Weapon Name On Second Character | `checkWeaponNameOnSecondCharacter` | `bool` | – | – |
| Weapon Name On Second Character | `weaponNameOnSecondCharacter` | `string` | – | – |

### Character Dead Condition Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Stop Action If Any Character Is Dead | `stopActionIfAnyCharacterIsDead` | `bool` | true | – |
| Stop Action If First Character Is Dead | `stopActionIfFirstCharacterIsDead` | `bool` | – | – |
| Stop Action If Second Character Is Dead | `stopActionIfSecondCharacterIsDead` | `bool` | – | – |

### Conditions Failed Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Alternative Shared Action If Conditions Failed | `useAlternativeSharedActionIfConditionsFailed` | `bool` | – | – |
| Alternative Shared Action Name | `alternativeSharedActionName` | `string` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| First Character Action System | `firstCharacterActionSystem` | `actionSystem` | – | – |
| Second Character Action System | `secondCharacterActionSystem` | `actionSystem` | – | – |

## 内部型

- `sharedActionConditionStatInfo`（class）
