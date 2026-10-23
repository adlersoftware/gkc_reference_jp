# customCharacterControllerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `customCharacterControllerBase`
- **ソース**: `Player/Generic Model Controller/customCharacterControllerSystem.cs:5`

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

### Rotation To Surface Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Rotate Character Model To Surface Enabled | `rotateCharacterModelToSurfaceEnabled` | `bool` | – | – |
| Max Character X Rotation To Surface | `maxCharacterXRotationToSurface` | `float` | 40 | – |
| Max Character Z Rotation To Surface | `maxCharacterZRotationToSurface` | `float` | 40 | – |
| Character Rotation To Surface Speed | `characterRotationToSurfaceSpeed` | `float` | 10 | – |
| Character Position Adjustment To Surface Speed | `characterPositionAdjustmentToSurfaceSpeed` | `float` | 10 | – |
| Character Rotation To Surface Raycast Distance | `characterRotationToSurfaceRaycastDistance` | `float` | 2.5f | – |
| Min Surface Rotation | `minSurfaceRotation` | `float` | 5 | – |
| Use Reverse Rotation | `useReverseRotation` | `bool` | – | – |
| Ignore Local Z Axis Rotation Enabled | `ignoreLocalZAxisRotationEnabled` | `bool` | – | – |
| Adjust Model Position To Surface Enabled | `adjustModelPositionToSurfaceEnabled` | `bool` | true | – |
| Character Pivot Transform | `characterPivotTransform` | `Transform` | – | – |
| Surface Rotation Layermask | `surfaceRotationLayermask` | `LayerMask` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current State | `currentState` | `int` | – | – |
| Target Position | `targetPosition` | `Vector3` | – | – |
| Surface Found | `surfaceFound` | `bool` | – | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`activateJumpAnimatorState()`, `setCharacterControllerActiveState(bool state)`, `updateCharacterControllerAnimator()`, `updateCharacterControllerState()`, `updateHorizontalVerticalInputValues(Vector2 newValues)`, `updateMovementInputValues(Vector3 newValues)`, `updateOnGroundValue(bool state)`

</details>
