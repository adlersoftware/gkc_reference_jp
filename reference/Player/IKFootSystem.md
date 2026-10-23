# IKFootSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `OnAnimatorIKComponent`
- **ソース**: `Player/Animator IK/IKFootSystem.cs:5`

**概要**: 足のIKコンポーネント。脚の長さと足のオフセット初期値を算出し、接地レイキャストに合わせて足と腰の位置を補正する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| IK Foot System Enabled | `IKFootSystemEnabled` | `bool` | true | – |
| Layer Mask | `layerMask` | `LayerMask` | – | – |
| IK Weight Enabled Speed | `IKWeightEnabledSpeed` | `float` | 10 | – |
| IK Weight Disabled Speed | `IKWeightDisabledSpeed` | `float` | 2 | – |
| Extra Foot Offset | `extraFootOffset` | `float` | 0.005f | – |
| Min Surface Angle To Use IK Foot | `minSurfaceAngleToUseIKFoot` | `float` | 0.1f | – |
| Max Surface Angle To Use IK Foot | `maxSurfaceAngleToUseIKFoot` | `float` | 0 | – |

### Hips Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hips Movement Speed | `hipsMovementSpeed` | `float` | 1.2f | – |
| Hips Position Up Clamp Amount | `hipsPositionUpClampAmount` | `float` | 0.2f | – |
| Hips Position Down Clamp Amount | `hipsPositionDownClampAmount` | `float` | -0.2f | – |
| Hips Position Up Moving Clamp Amount | `hipsPositionUpMovingClampAmount` | `float` | 0.2f | – |
| Hips Position Down Moving Clamp Amount | `hipsPositionDownMovingClampAmount` | `float` | -0.2f | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disable Component If IK System Not Enabled On Start | `disableComponentIfIKSystemNotEnabledOnStart` | `bool` | true | – |

### Leg Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Leg Info List | `legInfoList` | `List<legInfo>` | new List<legInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Use Ik Foot | `canUseIkFoot` | `bool` | – | – |
| IK Foot Paused | `IKFootPaused` | `bool` | – | – |
| Remove IK Value | `removeIKValue` | `bool` | – | – |
| Current Surface Angle | `currentSurfaceAngle` | `float` | – | – |
| Full Body Awareness Active | `fullBodyAwarenessActive` | `bool` | – | – |
| Can Adjust Hips Position | `canAdjustHipsPosition` | `bool` | true | – |
| Hips Position | `hipsPosition` | `Vector3` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Hips | `hips` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `calculateInitialFootValues()` | 左右の脚のオフセットと最大長を求め、腰位置を保存し、開始時に無効ならコンポーネントを無効化する。 |
| `getNewRaycastPosition(Vector3 targetTransformPosition, Vector3 lowerLegPosition, out float newDistance)` | 対象位置とすね位置をローカル化し、高さ差を `newDistance` で返し、すねの高さに合わせたワールド位置を返す。 |
| `setIKFootPausedState(bool state)` | `IKFootPaused` を設定するだけ。 |
| `setLegsInfo(Transform newHips, Transform rightLowerLeg, Transform leftLowerLeg, Transform rightFoot, Transform leftFoot, Transform rightToes, Transform leftToes)` | 腰と左右のすね・足・つま先を該当する `legInfo` に振り分けて設定し、`updateComponent` を呼ぶ。 |
| `setIKFootSystemEnabledState(bool state)` | 有効フラグを設定し、必要なら再生中にコンポーネントを有効化する。 |
| `setIKFootSystemEnabledStateFromEditor(bool state)` | 値を設定してから `updateComponent` を呼ぶ。 |
| `updateComponent()` | `GKC_Utils.updateComponent(this)` を呼ぶだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`updateOnAnimatorIKState()`

</details>

## 内部型

- `legInfo`（class）
