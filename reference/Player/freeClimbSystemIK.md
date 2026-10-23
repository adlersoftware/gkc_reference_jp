# freeClimbSystemIK

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `OnAnimatorIKComponent`
- **ソース**: `Player/Extra Movements/freeClimbSystemIK.cs:5`

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Climb System IK Active | `climbSystemIKActive` | `bool` | – | – |
| Layer Mask | `layerMask` | `LayerMask` | – | – |
| IK Weight Enabled Speed | `IKWeightEnabledSpeed` | `float` | 10 | – |
| IK Weight Disabled Speed | `IKWeightDisabledSpeed` | `float` | 2 | – |
| Raycast Distance | `raycastDistance` | `float` | 1.3f | – |
| Body Part IK Info List | `bodyPartIKInfoList` | `List<bodyPartIKInfo>` | new List<bodyPartIKInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Is Moving | `playerIsMoving` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Free Climb System | `mainFreeClimbSystem` | `freeClimbSystem` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`setActiveState(bool state)`, `updateOnAnimatorIKState()`

</details>

## 内部型

- `bodyPartIKInfo`（class）
