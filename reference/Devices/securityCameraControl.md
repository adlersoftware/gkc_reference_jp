# securityCameraControl

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/securityCameraControl.cs:4`

**概要**: 監視カメラ用の操作UI。ジョイスティックとズームボタンへのタッチ/マウス入力、プレイヤー入力をカメラ回転へ変換する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Drag Distance | `dragDistance` | `float` | 1 | – |
| Control Enabled | `controlEnabled` | `bool` | – | – |
| Clamp Tilt X | `clampTiltX` | `Vector2` | – | – |
| Clamp Tilt Z | `clampTiltZ` | `Vector2` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Security Camera Game Object | `securityCameraGameObject` | `GameObject` | – | – |
| Joystick | `joystick` | `GameObject` | – | – |
| Joystick Axis X | `joystickAxisX` | `Transform` | – | – |
| Joystick Axis Z | `joystickAxisZ` | `Transform` | – | – |
| Zoom Out Button | `zoomOutButton` | `GameObject` | – | – |
| Zoom In Button | `zoomInButton` | `GameObject` | – | – |
| Device Manager | `deviceManager` | `electronicDevice` | – | – |
| Security Camera Manager | `securityCameraManager` | `securityCamera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `rotateCamera(Vector2 values)` | 軸値に感度を掛けて`clampTiltX`/`clampTiltZ`内にクランプし、ジョイスティックのX/Z軸を回転させる。 |
| `activateSecurityControl()` | `setSecurityCameraControlState(true)`を呼ぶだけ。 |
| `deactivateSecurityCameraControl()` | `setSecurityCameraControlState(false)`を呼ぶだけ。 |
| `setSecurityCameraControlState(bool state)` | 有効化時にプレイヤーの各コンポーネントを取得し、`controlEnabled`と監視カメラの状態を設定、無効時はジョイスティックを戻す。 |
