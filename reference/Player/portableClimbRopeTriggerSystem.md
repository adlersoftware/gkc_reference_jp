# portableClimbRopeTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/portableClimbRopeTriggerSystem.cs:5`

**概要**: 設置型の縄の長さと向きを自動調整するコンポーネント。表面の有無や傾斜を確認し、レイキャスト結果に合わせてロープを伸縮させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Down Raycast Direction | `useDownRaycastDirection` | `bool` | – | – |
| Raycast Layermask | `raycastLayermask` | `LayerMask` | – | – |
| Max Raycast Distance | `maxRaycastDistance` | `float` | – | – |
| Adjust Rope End To Any Distance | `adjustRopeEndToAnyDistance` | `bool` | – | – |
| Activate On Start | `activateOnStart` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Surface Layer | `checkSurfaceLayer` | `bool` | – | – |
| Layer Surface | `layerSurface` | `LayerMask` | – | – |
| Raycast Radius | `raycastRadius` | `float` | – | – |
| Destroy Object If Surface Not Found | `destroyObjectIfSurfaceNotFound` | `bool` | – | – |
| Check Surface Inclination | `checkSurfaceInclination` | `bool` | – | – |
| Max Surface Inclination | `maxSurfaceInclination` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Climb Rope Trigger System | `mainClimbRopeTriggerSystem` | `climbRopeTriggerSystem` | – | – |
| Rope Pivot Transform | `ropePivotTransform` | `Transform` | – | – |
| Custom Raycast Direction | `customRaycastDirection` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateClimbRopeTrigger()` | 表面確認後にレイキャストで上下端を決め、距離に応じたスケールと向きを設定する。 |
