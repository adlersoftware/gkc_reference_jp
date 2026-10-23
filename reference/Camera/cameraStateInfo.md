# cameraStateInfo

- **種別**: class
- **ソース**: `Camera/Player Camera/cameraStateInfo.cs:5`
- **属性**: `System.Serializable`

**概要**: カメラ状態1つ分の設定値（位置オフセット、FOV、リーン、頭部追従など）を保持するシリアライズ可能クラス。別の状態から値をコピーまたは補間代入する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Name | `Name` | `string` | – | – |
| Cam Position Offset | `camPositionOffset` | `Vector3` | – | – |
| Pivot Position Offset | `pivotPositionOffset` | `Vector3` | – | – |
| Pivot Parent Position Offset | `pivotParentPositionOffset` | `Vector3` | – | – |
| Y Limits | `yLimits` | `Vector2` | – | – |
| Initial Fov Value | `initialFovValue` | `float` | – | – |
| Fov Transition Speed | `fovTransitionSpeed` | `float` | 10 | – |
| Max Fov Value | `maxFovValue` | `float` | – | – |
| Min Fov Value | `minFovValue` | `float` | 17 | – |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | – | – |
| Original Cam Position Offset | `originalCamPositionOffset` | `Vector3` | – | – |
| Lean Enabled | `leanEnabled` | `bool` | – | – |
| Max Lean Angle | `maxLeanAngle` | `float` | – | – |
| Lean Speed | `leanSpeed` | `float` | – | – |
| Lean Reset Speed | `leanResetSpeed` | `float` | – | – |
| Lean Raycast Distance | `leanRaycastDistance` | `float` | – | – |
| Lean Angle On Surface Found | `leanAngleOnSurfaceFound` | `float` | – | – |
| Lean Height | `leanHeight` | `float` | – | – |
| Is Lean On FBA | `isLeanOnFBA` | `bool` | – | – |
| FBA Lean Position Offset X | `FBALeanPositionOffsetX` | `float` | – | – |
| FBA Lean Position Offset Y | `FBALeanPositionOffsetY` | `float` | – | – |
| Head Track Active | `headTrackActive` | `bool` | true | – |
| Look In Player Direction | `lookInPlayerDirection` | `bool` | – | – |
| Look In Player Direction Speed | `lookInPlayerDirectionSpeed` | `float` | – | – |
| Allow Rotation With Input | `allowRotationWithInput` | `bool` | – | – |
| Time To Reset Rotation After Input | `timeToResetRotationAfterInput` | `float` | – | – |
| Use Y Limits On Look At Target Active | `useYLimitsOnLookAtTargetActive` | `bool` | – | – |
| Y Limits On Look At Target Active | `YLimitsOnLookAtTargetActive` | `Vector2` | new Vector2 (-20, 30) | – |
| Camera Collision Active | `cameraCollisionActive` | `bool` | true | – |
| Pivot Rotation Offset | `pivotRotationOffset` | `float` | – | – |
| Ignore Camera Shake On Run State | `ignoreCameraShakeOnRunState` | `bool` | – | – |
| Follow Transform Position | `followTransformPosition` | `bool` | – | – |
| Transform To Follow | `transformToFollow` | `Transform` | – | – |
| Use Follow Transform Position Offset | `useFollowTransformPositionOffset` | `bool` | – | – |
| Follow Transform Position Offset | `followTransformPositionOffset` | `Vector3` | – | – |
| Set Near Clip Plane Value | `setNearClipPlaneValue` | `bool` | – | – |
| Near Clip Plane Value | `nearClipPlaneValue` | `float` | – | – |
| Use Custom Movement Lerp Speed | `useCustomMovementLerpSpeed` | `bool` | – | – |
| Movement Lerp Speed | `movementLerpSpeed` | `float` | 5 | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `assignCameraStateValues(cameraStateInfo from, float lerpSpeed)` | `from` の値を取り込み、`lerpSpeed` が0より大きければ位置オフセットと `yLimits` を補間、0なら即時コピーする。 |
