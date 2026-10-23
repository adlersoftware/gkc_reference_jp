# setCameraFOVValue

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Player Camera/setCameraFOVValue.cs:5`

**概要**: メインカメラの FOV を増減・設定し、クランプ範囲内に収める小規模コンポーネント。カメラ未設定時はプレイヤーカメラやシーンから取得する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera FOV Change Enabled | `cameraFOVChangeEnabled` | `bool` | true | – |
| Change FOV Amount | `changeFOVAmount` | `float` | 0.4f | – |
| FOV Clamp Value | `FOVClampValue` | `Vector2` | – | – |
| Get Main Player Camera On Scene | `getMainPlayerCameraOnScene` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Camera Located | `mainCameraLocated` | `bool` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Camera | `mainCamera` | `Camera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableCameraFOVChange(bool state)` | `cameraFOVChangeEnabled` を設定するだけ。 |
| `increaseFov()` | FOV 変更が有効なら、FOV を `changeFOVAmount` だけ増やしてからクランプする。 |
| `decreaseFOV()` | FOV 変更が有効なら、FOV を `changeFOVAmount` だけ減らしてからクランプする。 |
| `setCameraFOV(float newValue)` | カメラの有無を確認して FOV を `newValue` に設定し、`FOVClampValue` でクランプする。 |
| `setFOVClampValueX(float newValue)` | `FOVClampValue.x` を設定するだけ。 |
| `setFOVClampValueY(float newValue)` | `FOVClampValue.y` を設定するだけ。 |
