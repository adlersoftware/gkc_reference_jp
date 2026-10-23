# AIHidePositionsManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/AIHidePositionsManager.cs:5`

**概要**: AIが隠れる位置のリスト`hidePositionList`を保持し、シーン上にギズモで隠れ場所を表示する管理コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hide Position List | `hidePositionList` | `List<Transform>` | new List<Transform> () | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Radius | `gizmoRadius` | `float` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `addNewWayPoint()` | 最後の隠れ位置の前方1m（空なら自身の位置）に子オブジェクトを作り、`hidePositionList`へ追加して更新する。 |
