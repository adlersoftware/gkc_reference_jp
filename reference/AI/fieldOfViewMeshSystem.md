# fieldOfViewMeshSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/fieldOfViewMeshSystem.cs:5`

**概要**: AIの視界範囲を扇形メッシュとして可視化するコンポーネント。レイキャストで視界形状を生成し、状態に応じて表示の有無やメッシュ色を切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Field Of View Active | `fieldOfViewActive` | `bool` | – | – |
| Original Color | `originalColor` | `Color` | Color.white | – |
| Alert Color | `alertColor` | `Color` | Color.red | – |
| View Radius | `viewRadius` | `float` | – | – |
| View Angle | `viewAngle` | `float` | – | Range (0, 360) |
| Obstacle Mask | `obstacleMask` | `LayerMask` | – | – |
| Mesh Resolution | `meshResolution` | `float` | – | – |
| Edge Resolve Iterations | `edgeResolveIterations` | `int` | – | – |
| Edge Dst Threshold | `edgeDstThreshold` | `float` | – | – |
| Mask Cutaway Dst | `maskCutawayDst` | `float` | .1f | – |
| Use Obstacle Raycast | `useObstacleRaycast` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| View Mesh Filter | `viewMeshFilter` | `MeshFilter` | – | – |
| Main Mesh Renderer | `mainMeshRenderer` | `MeshRenderer` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setActiveState(bool state)` | `fieldOfViewActive`のときだけ、表示状態が異なればGameObjectのアクティブを切り替える。 |
| `setMaterialColor(Color newColor)` | `mainMeshRenderer.material.color`を指定色にするだけ。 |
| `setRegularColor()` | `originalColor`を指定して`setMaterialColor`を呼ぶだけ。 |
| `setAlertColor()` | `alertColor`を指定して`setMaterialColor`を呼ぶだけ。 |

## 内部型

- `viewCastInfo`（struct）
- `edgeInfo`（struct）
