# camera2_5dSplineZoneOptions

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Player Camera/camera2_5dSplineZoneOptions.cs:5`

**概要**: 2.5D スプラインマップのゾーン用オプションで、ゾーン進入時にプレイヤーの `playerCamera` を取得してロックカメラの回転追従を制御する小規模コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera2 5d Spline Zone Enabled | `camera2_5dSplineZoneEnabled` | `bool` | true | – |
| Set Follow Player Rotation Direction Paused State | `setFollowPlayerRotationDirectionPausedState` | `bool` | – | – |
| Set Follow Player Rotation Direction Paused Value | `setFollowPlayerRotationDirectionPausedValue` | `bool` | – | – |
| Adjust Locked Camera Rotation To Transform | `adjustLockedCameraRotationToTransform` | `bool` | – | – |
| Adjust Locked Camera Rotation Speed | `adjustLockedCameraRotationSpeed` | `float` | 10 | – |
| Transform To Adjust Locked Camera Rotation | `transformToAdjustLockedCameraRotation` | `Transform` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentPlayerAndActivateCameraState(GameObject newPlayer)` | プレイヤーを設定したうえで、ゾーン用のカメラ状態設定を適用するだけ。 |
| `setCurrentPlayer(GameObject newPlayer)` | `currentPlayer` を更新して `playerCamera` を取得する。null なら警告を出して中断。 |
| `setCameraStateOnPlayer()` | ゾーン機能有効時、回転追従の一時停止と指定 Transform への回転補間を `playerCamera` に指示する。 |
