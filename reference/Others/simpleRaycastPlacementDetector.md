# simpleRaycastPlacementDetector

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/simpleRaycastPlacementDetector.cs:5`

**概要**: レイキャストの当たった面に合わせてオブジェクトを配置する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Raycast Layermask | `raycastLayermask` | `LayerMask` | – | – |
| Placement Enabled | `placementEnabled` | `bool` | true | – |
| Raycast Distance | `raycastDistance` | `float` | 2 | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Raycast Direction | `raycastDirection` | `Transform` | – | – |
| Main Transform | `mainTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activePlacement()` | 有効時、`raycastDirection`からレイを飛ばし、当たった面の法線向きと位置に`mainTransform`を合わせる。 |
