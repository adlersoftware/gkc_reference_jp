# grapplingHookEffect

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/Custom Abilities/Grappling Hook System/grapplingHookEffect.cs:5`

**概要**: グラップリングフックのロープを `LineRenderer` で螺旋状に描画するエフェクト。`DoGrapple` で対象点を決め、更新時に頂点を毎フレーム再計算する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Speed | `Speed` | `float` | 3f | The speed of the entire effect. |
| Spiral Speed | `SpiralSpeed` | `float` | 4f | The speed of the spiral offset (relative to 'Speed'). |
| Distance Speed | `DistanceSpeed` | `float` | 2f | The speed that the end of the line moves to the target point (relative to 'Speed') |
| Gravity | `Gravity` | `float` | 0.5f | A multiplier for the pull of gravity. |
| Segments | `Segments` | `int` | 100 | The number of points to be drawn by the line renderer. \nUpdates every time the effect is triggered. |
| Layer Mask | `layerMask` | `LayerMask` | – | – |

### Spiral Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Magnitude | `Magnitude` | `Vector2` | Vector2.one | The strength of the spiral. |
| Frequency | `Frequency` | `float` | 0.5f | The number of 'Curve' repetitions per world-unit. |
| Horizontal Offset | `HorizontalOffset` | `float` | 0.25f | The amount the horizontal part of the spiral is offset along 'Curve.' \nIf 'Curve' is a sine wave, 0.25 will result in a perfect spiral. |

### Noise Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Strength | `Strength` | `float` | 0.5f | The strength of the noise. |
| Scale | `Scale` | `float` | 0.25f | The scale of the noise samples. \nHigher = smoother. |

### Curves Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Curve | `Curve` | `AnimationCurve` | new AnimationCurve () | The base curve that the points will be offset along. \nA sine wave will make it look like a grapple spiral. |
| Magnitude Over Time | `MagnitudeOverTime` | `AnimationCurve` | new AnimationCurve () | The strength of the spiral and noise over time. |
| Magnitude Over Distance | `MagnitudeOverDistance` | `AnimationCurve` | new AnimationCurve () | The strength of the spiral and noise from the start to current end point within a 0 to 1 range. |
| Gravity Over Distance | `GravityOverDistance` | `AnimationCurve` | new AnimationCurve () | The vertical offset applied in world space to the line from the start to current end point within a 0 to 1 range. |
| Gravity Over Time | `GravityOverTime` | `AnimationCurve` | new AnimationCurve () | The strength of the gravity over time. |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Grappling Hook Effect Active | `grapplingHookEffectActive` | `bool` | – | – |
| Fixed Update Active | `fixedUpdateActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Line Renderer | `lineRenderer` | `LineRenderer` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Line Renderer Origin Position Transform | `lineRendererOriginPositionTransform` | `Transform` | – | – |
| Line Renderer Target Position Transform | `lineRendererTargetPositionTransform` | `Transform` | – | – |
| Player Controller Transform | `playerControllerTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateGrapplingHookEffect(Vector3 raycastDirection)` | 指定方向へカメラからレイを飛ばし、当たれば線を有効化して `DoGrapple` を呼びエフェクトを開始する。 |
| `activateGrapplingHookEffect()` | カメラ前方へレイを飛ばし、当たれば線を有効化して `DoGrapple` を呼びエフェクトを開始する。 |
| `deactivateGrapplingHookEffect()` | `grapplingHookEffectActive` を下げ、線を無効化して全頂点を原点位置へ戻す。 |
| `DoGrapple(Vector3 newWrapplePoint)` | 対象点を設定し、時間オフセットをリセットして頂点数を `Segments` に合わせる。 |
| `setFixedUpdateActiveState(bool state)` | `fixedUpdateActive` を設定するだけ（更新を `FixedUpdate` 側で行うかの切り替え）。 |
| `changeLineRendererOriginPositionParent(Transform newParent)` | 線の原点を `newParent` の子にしてローカル座標をゼロに合わせる。 |
| `setNewlineRendererTargetPositionTransform(Transform newObject)` | `lineRendererTargetPositionTransform` を新しい対象に差し替えるだけ。 |
