# useAbilitySimpleAIAction

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `simpleAIAction`
- **ソース**: `AI/Custom AI Behavior/useAbilitySimpleAIAction.cs:5`

**概要**: `AIAbilitiesSystemBrain`から指定名のアビリティを発動し、終了後にカメラと注視状態を戻すAIアクション。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Ability Name | `currentAbilityName` | `string` | – | – |
| Min Wait Time To Finish Ability | `minWaitTimeToFinishAbility` | `float` | 0.4f | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ability In Process | `abilityInProcess` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main AI Abilities System Brain | `mainAIAbilitiesSystemBrain` | `AIAbilitiesSystemBrain` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentAbilityName(string abilityName)` | `currentAbilityName`を`abilityName`に設定するだけ。 |
| `setCurrentAbilityNameAndStartAIAction(string abilityName)` | アビリティ名を設定してから`startAIAction`でアクションを開始する。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetStatesOnActionEnd()`, `startAIAction()`, `updateSystem()`

</details>
