# overrideCameraController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Override System/overrideCameraController.cs:5`

**概要**: オーバーライド対象を追従する三人称カメラ。マウス入力による回転、カメラ衝突の回避、親子付けや再出現位置を管理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Controller Enabled | `cameraControllerEnabled` | `bool` | true | – |
| Target To Follow | `targetToFollow` | `Transform` | – | – |
| Pivot Transform | `pivotTransform` | `Transform` | – | – |
| Camera Transform | `cameraTransform` | `Transform` | – | – |
| Camera Active | `cameraActive` | `bool` | – | – |
| X Limits | `xLimits` | `Vector2` | – | – |
| Rotation Speed | `rotationSpeed` | `float` | 10 | – |
| Camera Rotation Speed Vertical | `cameraRotationSpeedVertical` | `float` | 5 | – |
| Camera Rotation Speed Horizontal | `cameraRotationSpeedHorizontal` | `float` | 5 | – |
| Layer | `layer` | `LayerMask` | – | – |
| Clip Cast Radius | `clipCastRadius` | `float` | – | – |
| Back Clip Speed | `backClipSpeed` | `float` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Controller Radius | `controllerRadius` | `float` | 2 | – |
| Reapear In Certain Position | `reapearInCertainPosition` | `bool` | – | – |
| Position To Reapear | `positionToReapear` | `Transform` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.yellow | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Override Input | `overrideInput` | `overrideInputManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`を停止するだけ。 |
| `getCameraTransform()` | `cameraTransform`を返すだけ。 |
| `setCameraActiveState(bool state)` | カメラ制御が有効な場合のみ状態を設定し、停止時は角度をリセット、開始時は更新コルーチンを起動する。 |
| `isCameraControllerEnabled()` | `cameraControllerEnabled`を返すだけ。 |
| `setParentState(bool state)` | `state`なら追従対象から切り離してその位置へ移動し、そうでなければ追従対象の子にする。 |
| `resetLocalRotationPosition()` | 自身のローカル回転と位置を初期値に戻すだけ。 |
| `resetRotation(Quaternion newRotation)` | Y軸のみ`newRotation`の向きに合わせた回転を設定するだけ。 |
| `checkCameraCollision()` | ピボットから後方へスフィアキャストし、最も近い非トリガーの衝突点までの距離を滑らかに補間して返す。 |
| `getControllerRadius()` | `controllerRadius`を返すだけ。 |
| `reapearInCertainPositionActive()` | `reapearInCertainPosition`を返すだけ。 |
| `getPositionToReapear()` | `positionToReapear`があればその位置を、なければ`Vector3.zero`を返す。 |
