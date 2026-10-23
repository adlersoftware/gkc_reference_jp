# simpleScannerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/Scanner System/simpleScannerSystem.cs:6`

**概要**: スキャナーカメラの有効状態を切り替え、`cullingMask`とイベントを更新する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Simple Scanner Camera Enabled | `simpleScannerCameraEnabled` | `bool` | true | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Regular Layer Mask | `regularLayerMask` | `LayerMask` | – | – |
| Scanner Layer Mask | `scannerLayerMask` | `LayerMask` | – | – |
| Camera Active | `cameraActive` | `bool` | – | – |
| Use Events On Camera State Change | `useEventsOnCameraStateChange` | `bool` | – | – |
| Event On Camera Active | `eventOnCameraActive` | `UnityEvent` | – | – |
| Event On Camera Deactivate | `eventOnCameraDeactivate` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableCamera(bool state)` | 設定有効かつ状態変化時のみ、`cameraActive`を更新してイベント発火と`cullingMask`の切り替えを行う。 |
| `toggleCameraEnabledState()` | `cameraActive`を反転して`enableOrDisableCamera`を呼ぶ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCameraActive` | `UnityEvent` | – |
| `eventOnCameraDeactivate` | `UnityEvent` | – |
