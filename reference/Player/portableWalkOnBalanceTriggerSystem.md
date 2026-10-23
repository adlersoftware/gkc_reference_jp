# portableWalkOnBalanceTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/portableWalkOnBalanceTriggerSystem.cs:5`

**概要**: 設置型のバランス足場。表面の傾斜や位置に合わせて自身の向きを調整し、レイキャストで足場の長さをスケールさせる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Raycast Layermask | `raycastLayermask` | `LayerMask` | – | – |
| Max Raycast Distance | `maxRaycastDistance` | `float` | – | – |
| Adjust End To Any Distance | `adjustEndToAnyDistance` | `bool` | – | – |
| Activate On Start | `activateOnStart` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Surface Layer | `checkSurfaceLayer` | `bool` | – | – |
| Layer Surface | `layerSurface` | `LayerMask` | – | – |
| Raycast Radius | `raycastRadius` | `float` | – | – |
| Destroy Object If Surface Not Found | `destroyObjectIfSurfaceNotFound` | `bool` | – | – |
| Check Surface Inclination | `checkSurfaceInclination` | `bool` | – | – |
| Min Surface Inclination | `minSurfaceInclination` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pivot Transform | `pivotTransform` | `Transform` | – | – |
| Start Transform | `startTransform` | `Transform` | – | – |
| End Transform | `endTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateWalkOnBalanceTrigger()` | 表面に合わせて姿勢を決め、前方レイキャストの距離で足場を伸縮させる。 |
