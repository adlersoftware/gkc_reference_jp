# dynamicSplitScreenSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Others/dynamicSplitScreenSystem.cs:5`

**概要**: 2人のプレイヤーが離れたときに画面を動的に分割するシステム。距離に応じてスプリッタ、2台目のカメラ、カリングマスクを制御する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dynamic Split Screen Active | `dynamicSplitScreenActive` | `bool` | true | – |
| Split Distance | `splitDistance` | `float` | 5 | – |
| Splitter Color | `splitterColor` | `Color` | – | – |
| Splitter Width | `splitterWidth` | `float` | – | – |
| Second Player Camera Culling Mask | `secondPlayerCameraCullingMask` | `LayerMask` | – | – |
| Regular Camera Culling Mask | `regularCameraCullingMask` | `LayerMask` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Extra Position Offset1 Top Down | `extraPositionOffset1TopDown` | `Vector3` | – | – |
| Extra Position Offset2 Top Down | `extraPositionOffset2TopDown` | `Vector3` | – | – |
| Using Top Down View | `usingTopDownView` | `bool` | – | – |
| Screen Rotation Speed | `screenRotationSpeed` | `float` | 20 | – |

### 2.5D Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using2 5d View | `using2_5dView` | `bool` | – | – |
| Moving On X Axis | `movingOnXAxis` | `bool` | – | – |
| Min Horizontal Axis Distance To Offset2 5d | `minHorizontalAxisDistanceToOffset2_5d` | `float` | – | – |
| Horizonta Axis Offset2 5d | `horizontaAxisOffset2_5d` | `float` | – | – |
| Max Horizontal Distance For Vertical Split | `maxHorizontalDistanceForVerticalSplit` | `float` | 20 | – |
| Reverse Movement Direction | `reverseMovementDirection` | `bool` | – | – |
| Far Screen Rotation Clamp Values | `farScreenRotationClampValues` | `Vector2` | – | – |
| Close Screen Rotation Clamp Values | `closeScreenRotationClampValues` | `Vector2` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Max Distance Reached | `maxDistanceReached` | `bool` | – | – |
| Player1 On Lower Position | `player1OnLowerPosition` | `bool` | – | – |
| Current Screen Rotation | `currentScreenRotation` | `float` | – | – |
| Player1 On Left Side | `player1OnLeftSide` | `bool` | – | – |
| Current Horizontal Distance | `currentHorizontalDistance` | `float` | – | – |
| Current Distance | `currentDistance` | `float` | – | – |
| Current Extra Position Offset1 | `currentExtraPositionOffset1` | `Vector3` | – | – |
| Current Extra Position Offset2 | `currentExtraPositionOffset2` | `Vector3` | – | – |
| Close Vertical Position | `closeVerticalPosition` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player1 | `player1` | `Transform` | – | – |
| Player2 | `player2` | `Transform` | – | – |
| Main Player Camera Manager1 | `mainPlayerCameraManager1` | `playerCamera` | – | – |
| Main Player Camera Manager2 | `mainPlayerCameraManager2` | `playerCamera` | – | – |
| Camera1 | `camera1` | `Camera` | – | – |
| Camera2 | `camera2` | `Camera` | – | – |
| Split | `split` | `GameObject` | – | – |
| Splitter | `splitter` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setDynamicSplitScreenActiveState(bool state, GameObject newPlayer1, GameObject newPlayer2, bool creatingCharactersOnEditor)` | 有効フラグと `enabled` を設定し両プレイヤーのカメラを取得、2台目カメラの `cullingMask` を状態で切り替え、エディタ生成時は更新する。 |
| `setDynamicSplitScreenActiveState(bool state)` | `dynamicSplitScreenActive` と `enabled` を設定するだけ。 |
