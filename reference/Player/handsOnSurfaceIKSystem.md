# handsOnSurfaceIKSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `OnAnimatorIKComponent`
- **ソース**: `Player/Animator IK/handsOnSurfaceIKSystem.cs:6`

**概要**: 手を壁や床などの表面に合わせるIKコンポーネント。表面レイキャストで手の目標を決め、手ごとの重みを補間して適用する。

**公式ドキュメント抜粋**（[Hands On Surface IK System](../../docs/player-controller-components/non-essential-components/hands-on-surface-ik-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Adjust Hands To Surfaces Enabled | `adjustHandsToSurfacesEnabled` | `bool` | true | – |
| Layer To Adjust Hands To Surfaces | `layerToAdjustHandsToSurfaces` | `LayerMask` | – | – |
| Movement Speed Lerp Speed | `movementSpeedLerpSpeed` | `float` | 2 | – |
| Wait Time After Ground To Check Surface | `waitTimeAfterGroundToCheckSurface` | `float` | 1.5f | – |
| Wait Time After Crouch To Check Surface | `waitTimeAfterCrouchToCheckSurface` | `float` | 1.5f | – |
| Weight Lerp Speed | `weightLerpSpeed` | `float` | 6 | – |
| Max Hands Distance | `maxHandsDistance` | `float` | 3 | – |
| Min Moving Input To Use Walk Speed | `minMovingInputToUseWalkSpeed` | `float` | 0.5f | – |
| Min IK Weight To Use Walk Speed | `minIKWeightToUseWalkSpeed` | `float` | 0.4f | – |
| Pause Hands On Surface If Close Combat Active | `pauseHandsOnSurfaceIfCloseCombatActive` | `bool` | – | – |

### Hands Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hands To Surface Info List | `handsToSurfaceInfoList` | `List<handsToSurfaceInfo>` | new List<handsToSurfaceInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Hands | `usingHands` | `bool` | – | – |
| Adjust Hands Paused | `adjustHandsPaused` | `bool` | – | – |
| Smooth Busy Disable Active | `smoothBusyDisableActive` | `bool` | – | – |
| Hands Check Paused With Delay Active | `handsCheckPausedWithDelayActive` | `bool` | – | – |
| Is Busy | `isBusy` | `bool` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.white | – |
| Gizmo Radius | `gizmoRadius` | `float` | – | – |

### Component Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Animator | `animator` | `Animator` | – | – |
| IK Manager | `IKManager` | `IKSystem` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `currentWeightInBothHandsEqualTo(float weightValue)` | 両手の `currentHandWeight` が指定値と一致していれば true を返す。 |
| `playerIsBusy()` | 手使用中・非一人称・FF/無重力・近接/アクション中・停止中・飛行/水泳・物所持なら true を返す。 |
| `setWeightLerpSpeedValue(float newValue)` | `weightLerpSpeed` を設定するだけ。 |
| `setOriginalWeightLerpSpeed()` | 保存値 `originalWeightLerpSpeed` で `setWeightLerpSpeedValue` を呼ぶだけ。 |
| `setAdjustHandsPausedState(bool state)` | `adjustHandsPaused` を設定するだけ。 |
| `setSmoothBusyDisableActiveState(bool state)` | `smoothBusyDisableActive` を設定するだけ。 |
| `setAdjustHandsToSurfacesEnabledState(bool state)` | `adjustHandsToSurfacesEnabled` を設定するだけ。 |
| `enableHandsCheckPausedWithDelayActive(float duration)` | 既存の遅延コルーチンを止め、指定時間後に再開するコルーチンを開始する。 |
| `stopUpdateDelayToResumeStateCoroutine()` | 遅延コルーチンを停止し、`handsCheckPausedWithDelayActive` を false にする。 |
| `setAdjustHandsToSurfacesEnabledStateFromEditor(bool state)` | 値を設定してから `updateComponent` を呼ぶ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`updateOnAnimatorIKState()`

</details>

## 内部型

- `handsToSurfaceInfo`（class）
- `multipleRayInfo`（class）
