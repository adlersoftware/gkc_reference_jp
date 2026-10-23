# simpleMoveCameraToPosition

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Others/simpleMoveCameraToPosition.cs:4`

**概要**: メインカメラを指定オブジェクトの子にして、位置と回転を補間移動させるコンポーネント。移動終了で元の親へ戻す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Movement Active | `cameraMovementActive` | `bool` | true | – |
| Smooth Camera Movement | `smoothCameraMovement` | `bool` | true | – |
| Use Fixed Lerp Movement | `useFixedLerpMovement` | `bool` | true | – |
| Fixed Lerp Movement Speed | `fixedLerpMovementSpeed` | `float` | 2 | – |
| Camera Movement Speed Third Person | `cameraMovementSpeedThirdPerson` | `float` | 1 | – |
| Camera Movement Speed First Person | `cameraMovementSpeedFirstPerson` | `float` | 0.2f | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Moving Camera | `movingCamera` | `bool` | – | – |
| Move Camera Active | `moveCameraActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Position | `cameraPosition` | `GameObject` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Current Player | `currentPlayer` | `GameObject` | – | – |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `moveCamera(bool state)` | 有効ならカメラを `cameraPosition` の子にして補間移動を開始し、無効なら元の親へ戻す。 |
| `setCurrentPlayer(GameObject player)` | プレイヤーから `playerCamera` を取得し、そのメインカメラを保持する。 |
| `stopMovement()` | 移動用コルーチンを停止するだけ。 |
