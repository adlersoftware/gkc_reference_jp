# basicAnimatorController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `customCharacterControllerBase`
- **ソース**: `Player/Generic Model Controller/basicAnimatorController.cs:5`

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Horizontal Animator Name | `horizontalAnimatorName` | `string` | "Horizontal" | – |
| Vertical Animator Name | `verticalAnimatorName` | `string` | "Vertical" | – |
| State Animator Name | `stateAnimatorName` | `string` | "State" | – |
| Grounded State Animator Name | `groundedStateAnimatorName` | `string` | "Grounded" | – |
| Movement Animator Name | `movementAnimatorName` | `string` | "Movement" | – |
| Speed Multiplier Animator Name | `speedMultiplierAnimatorName` | `string` | "SpeedMultiplier" | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Jump State | `jumpState` | `int` | 2 | – |
| Movement State | `movementState` | `int` | 1 | – |
| Fall State | `fallState` | `int` | 3 | – |
| Death State | `deathState` | `int` | 10 | – |
| Current State | `currentState` | `int` | – | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`activateJumpAnimatorState()`, `setCharacterControllerActiveState(bool state)`, `updateCharacterControllerAnimator()`, `updateCharacterControllerState()`, `updateHorizontalVerticalInputValues(Vector2 newValues)`, `updateMovementInputValues(Vector3 newValues)`, `updateOnGroundValue(bool state)`

</details>
