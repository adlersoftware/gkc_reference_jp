# simpleIKHand

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `OnAnimatorIKComponent`
- **ソース**: `Player/Animator IK/simpleIKHand.cs:5`

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Simple IK Hand Active | `simpleIKHandActive` | `bool` | – | – |
| IK Weight | `IKWeight` | `float` | – | – |
| Hand IK Goal | `handIKGoal` | `AvatarIKGoal` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Animator | `mainAnimator` | `Animator` | – | – |
| IK Position Transform | `IKPositionTransform` | `Transform` | – | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`setActiveState(bool state)`, `setCharacterElements(GameObject newCharacter)`, `updateOnAnimatorIKState()`

</details>
