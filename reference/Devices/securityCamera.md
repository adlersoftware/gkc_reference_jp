# securityCamera

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/securityCamera.cs:4`

**概要**: 監視カメラの首振りとズームを制御する。通常入力と`overrideInputManager`による強制操作の両方に対応する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sensitivity | `sensitivity` | `float` | – | – |
| Clamp Tilt Y | `clampTiltY` | `Vector2` | – | – |
| Clamp Tilt X | `clampTiltX` | `Vector2` | – | – |
| Zoom Limit | `zoomLimit` | `Vector2` | – | – |
| Activated | `activated` | `bool` | – | – |
| Zoom Speed | `zoomSpeed` | `float` | – | – |
| Control Overriden | `controlOverriden` | `bool` | – | – |
| Input Rotation Speed | `inputRotationSpeed` | `float` | 5 | – |
| Override Rotation Speed | `overrideRotationSpeed` | `float` | 10 | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Base X | `baseX` | `GameObject` | – | – |
| Base Y | `baseY` | `GameObject` | – | – |
| Override Input | `overrideInput` | `overrideInputManager` | – | – |
| Cam | `cam` | `Camera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getLookValue(Vector2 currentAxisValues)` | 受け取った軸値を保持し、次フレームの回転計算に使わせる。 |
| `setZoom(int mult)` | `mult`の方向へFOVを変化させ、`zoomLimit`の範囲内にクランプする。 |
| `changeCameraState(bool state)` | `activated`を設定し、カメラの有効化と、終了時のFOV復元を行う。 |
| `startOverride()` | `overrideControlState(true)`を呼ぶだけ。 |
| `stopOverride()` | `overrideControlState(false)`を呼ぶだけ。 |
| `overrideControlState(bool state)` | 開始時は現在の首振り角を引き継ぎ、終了時は角度と軸値をリセットして上書き操作状態を設定する。 |
