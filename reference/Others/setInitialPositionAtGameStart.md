# setInitialPositionAtGameStart

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/setInitialPositionAtGameStart.cs:5`

**概要**: ゲーム開始時に登録オブジェクトを指定位置・回転へ移動させる。

**公式ドキュメント抜粋**（[Set Initial Position At Game Start](../../docs/toplevelcomponents/player-and-game-management/set-initial-position-at-game-start.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Initial Position Enabled | `setInitialPositionEnabled` | `bool` | – | – |
| Position Offset | `positionOffset` | `Vector3` | – | – |
| Rotation Offset | `rotationOffset` | `Vector3` | – | – |
| Use Custom Transform | `useCustomTransform` | `bool` | – | – |
| Custom Transform | `customTransform` | `Transform` | – | – |
| Adjust Object To Surface | `adjustObjectToSurface` | `bool` | – | – |
| Layer To Place Elements | `layerToPlaceElements` | `LayerMask` | – | – |

### Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Objects To Move List | `objectsToMoveList` | `List<Transform>` | new List<Transform> () | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.green | – |
| Gizmo Arrow Length | `gizmoArrowLength` | `float` | 1 | – |
| Gizmo Arrow Angle | `gizmoArrowAngle` | `float` | 20 | – |
| Gizmo Arrow Color | `gizmoArrowColor` | `Color` | Color.white | – |
| Arrow Length | `arrowLength` | `float` | 3 | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setInitialPosition()` | `useCustomTransform`や`positionOffset`から目標位置・回転を決め、必要なら地面へレイキャストで合わせて全対象へ適用する。 |
