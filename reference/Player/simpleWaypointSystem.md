# simpleWaypointSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/simpleWaypointSystem.cs:5`

**概要**: ウェイポイントの Transform リストを保持して公開するだけのコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Way Points | `wayPoints` | `List<Transform>` | new List<Transform> () | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.black | – |
| Gizmo Radius | `gizmoRadius` | `float` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getWayPoints()` | `wayPoints` リストをそのまま返すだけ。 |
