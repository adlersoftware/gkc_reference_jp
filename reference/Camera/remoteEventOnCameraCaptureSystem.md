# remoteEventOnCameraCaptureSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Captures/remoteEventOnCameraCaptureSystem.cs:5`

**概要**: 撮影時のレイキャストで見つかったオブジェクトの `eventObjectFoundOnCaptureSystem` を呼び出す中継コンポーネント。カプセルキャストにも対応する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Object Found On Capture Enabled | `checkObjectFoundOnCaptureEnabled` | `bool` | true | – |
| Layermask To Use | `layermaskToUse` | `LayerMask` | – | – |
| Max Raycast Distance | `maxRaycastDistance` | `float` | 20 | – |
| Send Object On Surface Detected | `sendObjectOnSurfaceDetected` | `bool` | – | – |
| Object To Send On Surface Detected | `objectToSendOnSurfaceDetected` | `GameObject` | – | – |

### Raycast Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Capsule Raycast | `useCapsuleRaycast` | `bool` | – | – |
| Capsule Cast Radius | `capsuleCastRadius` | `float` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Transform | `cameraTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkCapture()` | 有効ならカメラ前方へレイキャスト（カプセル時は複数）し、当たった各オブジェクトの撮影イベントを呼ぶ。 |
| `setNewCameraTransform(Transform newCamera)` | `cameraTransform` を差し替えるだけ。 |
