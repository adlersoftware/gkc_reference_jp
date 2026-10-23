# animatorTriggerEvent

- **種別**: class
- **継承 / 実装**: `StateMachineBehaviour`
- **ソース**: `Others/animatorTriggerEvent.cs:5`

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event Enabled | `eventEnabled` | `bool` | true | – |
| Event On Enter Enabled | `eventOnEnterEnabled` | `bool` | true | – |
| Event On Exit Enabled | `eventOnExitEnabled` | `bool` | – | – |
| Event Message | `eventMessage` | `string` | – | – |
| Use Message Parameter | `useMessageParameter` | `bool` | true | – |
| Event Message Parameter | `eventMessageParameter` | `string` | – | – |

### Remote Animator Trigger Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Animator Trigger Event System | `useRemoteAnimatorTriggerEventSystem` | `bool` | – | – |
| Remote Animator Trigger Event Name | `RemoteAnimatorTriggerEventName` | `string` | – | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnStateEnter(Animator animator, AnimatorStateInfo stateInfo, int layerIndex)`, `OnStateExit(Animator animator, AnimatorStateInfo stateInfo, int layerIndex)`

</details>
