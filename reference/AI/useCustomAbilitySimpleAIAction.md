# useCustomAbilitySimpleAIAction

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `simpleAIAction`
- **ソース**: `AI/Custom AI Behavior/useCustomAbilitySimpleAIAction.cs:5`

**概要**: 指定名のアビリティを待ち時間後に発動し、対象の注視とNavMeshの一時停止を制御するAIアクション。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Ability Name | `currentAbilityName` | `string` | – | – |
| Min Wait Time To Finish Ability | `minWaitTimeToFinishAbility` | `float` | 0.4f | – |
| Wait Time To Use Ability | `waitTimeToUseAbility` | `float` | 0.5f | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Move Nav Mesh Paused | `setMoveNavMeshPaused` | `bool` | – | – |
| Move Namvesh Paused Duration | `moveNamveshPausedDuration` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ability In Process | `abilityInProcess` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main AI Abilities System Brain | `mainAIAbilitiesSystemBrain` | `AIAbilitiesSystemBrain` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main AI Navmesh | `mainAINavmesh` | `AINavMesh` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentAbilityName(string abilityName)` | `currentAbilityName`を`abilityName`に設定するだけ。 |
| `setCurrentAbilityNameAndStartAIAction(string abilityName)` | アビリティ名を設定してから`startAIAction`でアクションを開始する。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetStatesOnActionEnd()`, `startAIAction()`, `updateSystem()`

</details>
