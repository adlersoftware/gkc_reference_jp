# GKCMeleeConditionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `GKCConditionInfo`
- **ソース**: `Condition System/GKCMeleeConditionSystem.cs:5`

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check If Carryin Weapon | `checkIfCarryinWeapon` | `bool` | – | – |
| Weapon Carried Name | `weaponCarriedName` | `string` | – | – |
| Check If Weapon On Hand | `checkIfWeaponOnHand` | `bool` | – | – |
| Check If Weapon Secondary Ability Active | `checkIfWeaponSecondaryAbilityActive` | `bool` | – | – |
| Check Both Conditions On Coroutine Update | `checkBothConditionsOnCoroutineUpdate` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Condition Complete Checked | `currentConditionCompleteChecked` | `bool` | – | – |
| Current Condition Not Complete Checked | `currentConditionNotCompleteChecked` | `bool` | – | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkConditionOnUpdateState()`, `checkFunctionOnTriggerExit()`, `checkIfConditionComplete()`, `checkIfConditionCompleteAndReturnResult()`

</details>
