# animatorTriggerEnterExitEvent

- **種別**: class
- **継承 / 実装**: `StateMachineBehaviour`
- **ソース**: `Others/animatorTriggerEnterExitEvent.cs:5`

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event Enabled | `eventEnabled` | `bool` | true | – |
| Event Enter Enabled | `eventEnterEnabled` | `bool` | true | – |
| Event Exit Enabled | `eventExitEnabled` | `bool` | true | – |
| Enter Event Message | `enterEventMessage` | `string` | – | – |
| Enter Event Message Parameter | `enterEventMessageParameter` | `string` | – | – |
| Exit Event Message | `exitEventMessage` | `string` | – | – |
| Exit Event Message Parameter | `exitEventMessageParameter` | `string` | – | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnStateEnter(Animator animator, AnimatorStateInfo stateInfo, int layerIndex)`, `OnStateExit(Animator animator, AnimatorStateInfo stateInfo, int layerIndex)`

</details>
