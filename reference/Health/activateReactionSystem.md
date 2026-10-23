# activateReactionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `applyEffectOnArea`
- **ソース**: `Health/activateReactionSystem.cs:5`

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Custom Action | `activateCustomAction` | `bool` | – | – |
| Custom Action Name | `customActionName` | `string` | – | – |
| Activate Reaction | `activateReaction` | `bool` | – | – |
| Reaction Name | `reactionName` | `string` | – | – |
| Damage To Send On Reaction | `damageToSendOnReaction` | `float` | – | – |
| Check To Activate Reaction System Temporally | `checkToActivateReactionSystemTemporally` | `bool` | – | – |
| Use Custom Damage Reaction ID | `useCustomDamageReactionID` | `bool` | – | – |
| Damage Reaction ID | `damageReactionID` | `int` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Reaction Transform | `mainReactionTransform` | `Transform` | – | – |
| Object Blocked | `objectBlocked` | `GameObject` | – | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`applyEffect(GameObject objectToAffect)`

</details>
