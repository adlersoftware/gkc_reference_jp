# setMapOrientationSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Map/setMapOrientationSystem.cs:5`

**概要**: プレイヤーの`mapSystem`に対し、マップの向き(カメラ軸と基準`Transform`)を設定する小さな橋渡しコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Map Camera Movement Type | `mapCameraMovementType` | `mapCameraMovement` | – | – |
| Map Orientation Transform | `mapOrientationTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setMapOrientation()` | 現在プレイヤーの`mapSystem`へ`mapCameraMovementType`と向き用`Transform`を渡し、地図の向きを設定する。 |
| `setCurrentPlayer(GameObject newPlayer)` | `currentPlayer`に`newPlayer`を保持するだけ。 |

## 内部型

- `mapCameraMovement`（enum）
