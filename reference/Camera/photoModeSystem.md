# photoModeSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Camera Effect/photoModeSystem.cs:6`

**概要**: フォトモード用のフリーカメラ。プレイヤーカメラをピボットに付け替えて自由移動・回転させ、タイムスケール停止や撮影イベントを扱う。

**公式ドキュメント抜粋**（[Photo Mode System](../../docs/player-controller-components/non-essential-components/photo-mode-system.md)）

> 

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Photo Mode Enabled | `photoModeEnabled` | `bool` | true | – |
| Rotation Speed | `rotationSpeed` | `float` | – | – |
| Smooth Camera Rotation Speed Vertical | `smoothCameraRotationSpeedVertical` | `float` | – | – |
| Smooth Camera Rotation Speed Horizontal | `smoothCameraRotationSpeedHorizontal` | `float` | – | – |
| Clamp Tilt X | `clampTiltX` | `Vector2` | – | – |
| Movement Speed | `movementSpeed` | `float` | – | – |
| Sides Rotation Speed | `sidesRotationSpeed` | `float` | 1 | – |
| Clamp Camera Distance | `clampCameraDistance` | `bool` | – | – |
| Max Camera Radius | `maxCameraRadius` | `float` | – | – |
| Set Custom Time Scale | `setCustomTimeScale` | `bool` | – | – |
| Custom Time Scale | `customTimeScale` | `float` | – | – |
| Freeze All Characters On Scene | `freezeAllCharactersOnScene` | `bool` | – | – |
| Can Use Turbo Enabled | `canUseTurboEnabled` | `bool` | true | – |
| Turbo Speed Multiplier | `turboSpeedMultiplier` | `float` | 2 | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Photo Mode Active | `eventOnPhotoModeActive` | `UnityEvent` | – | – |
| Event On Photo Mode Deactive | `eventOnPhotoModeDeactive` | `UnityEvent` | – | – |
| Event On Take Photo | `eventOnTakePhoto` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Movement Axis Values | `movementAxisValues` | `Vector2` | – | – |
| Mouse Axis Values | `mouseAxisValues` | `Vector2` | – | – |
| Current Look Angle | `currentLookAngle` | `Vector2` | – | – |
| Photo Mode Input Active | `photoModeInputActive` | `bool` | – | – |
| Photo Mode Active | `photoModeActive` | `bool` | – | – |
| Turbo Active | `turboActive` | `bool` | – | – |

### Component Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Transform | `mainTransform` | `Transform` | – | – |
| Pivot Transform | `pivotTransform` | `Transform` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Player Input | `playerInput` | `playerInputManager` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Time Bullet | `mainTimeBullet` | `timeBullet` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `mainUpdateCoroutine` を停止するだけ。 |
| `setPhotoModeActiveState(bool state)` | フォトモードを切り替え、タイムスケールやキャラクター停止、カメラの親と位置の保存復元、イベント発火を行う。 |
| `enableOrDisablePhotoMode()` | 現在の状態を反転して `setPhotoModeActiveState` を呼ぶだけ。 |
| `takePhoto()` | `eventOnTakePhoto` を発火するだけ。 |
| `resetCameraPosition()` | 既存のリセット処理を止め、カメラ位置を戻すコルーチンを開始する。 |
| `setCameraDirection()` | プレイヤーカメラの向きをピボットの回転に合わせ、`lookAngleValue` を更新する。 |
| `inputTakePhoto()` | フォトモード中のみ `takePhoto` を呼ぶ。 |
| `inputToogleCameraRotation()` | フォトモード中のみ `cameraRotationActive` を反転させる。 |
| `inputEnableOrDisablePhotoMode()` | `enableOrDisablePhotoMode` を呼ぶだけ。 |
| `inputSetTurboMode(bool state)` | フォトモード中かつターボ許可時のみ `turboActive` を設定する。 |
| `inputMoveCameraUp()` | `movingCameraUp` を true にするだけ。 |
| `inputMoveCameraDown()` | `movingCameraDown` を true にするだけ。 |
| `inputRotategCameraToRight()` | `rotatingCameraToRight` を true にするだけ。 |
| `inputRotateCameraToLeft()` | `rotatingCameraToLeft` を true にするだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnPhotoModeActive` | `UnityEvent` | – |
| `eventOnPhotoModeDeactive` | `UnityEvent` | – |
| `eventOnTakePhoto` | `UnityEvent` | – |
