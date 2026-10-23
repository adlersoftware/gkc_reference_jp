# applyDamageOnArea

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `applyEffectOnArea`
- **ソース**: `Health/applyDamageOnArea.cs:5`

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Can Activate Reaction System Temporally | `canActivateReactionSystemTemporally` | `bool` | – | – |
| Damage Reaction ID | `damageReactionID` | `int` | -1 | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |
| Damage Object Over Time On Exit | `damageObjectOverTimeOnExit` | `bool` | – | – |
| Damage Over Time On Exit Amount | `damageOverTimeOnExitAmount` | `float` | – | – |
| Damage Over Time On Exit Duration | `damageOverTimeOnExitDuration` | `float` | – | – |
| Damage Over Time On Exit Rate | `damageOverTimeOnExitRate` | `float` | – | – |
| Damage Over Time On Exit Until Death | `damageOverTimeOnExitUntilDeath` | `bool` | – | – |
| Attacker Game Object | `attackerGameObject` | `GameObject` | – | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`applyEffect(GameObject objectToAffect)`, `checkApplyEffectOnExit(GameObject objectToAffect)`

</details>
