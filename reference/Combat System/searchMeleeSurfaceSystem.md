# searchMeleeSurfaceSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/searchMeleeSurfaceSystem.cs:5`

**概要**: 近接攻撃時に足元や隠しサーフェスを探索し、サーフェス情報を攻撃システムへ渡す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Search Surface Enabled | `searchSurfaceEnabled` | `bool` | true | – |
| Layer To Check | `layerToCheck` | `LayerMask` | – | – |
| Raycast Distance | `raycastDistance` | `float` | 2 | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Surface Info On Melee Attack Name For Swing On Air | `surfaceInfoOnMeleeAttackNameForSwingOnAir` | `string` | "Swing On Air" | – |
| Max Distance To Hidden Surfaces | `maxDistanceToHiddenSurfaces` | `float` | 3 | – |

### Extraction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check For Materials Zone To Extract | `checkForMaterialsZoneToExtract` | `bool` | – | – |
| Max Detection Distance To Extract | `maxDetectionDistanceToExtract` | `float` | 10 | – |
| Use Max Material Zones To Extract At Same Time | `useMaxMaterialZonesToExtractAtSameTime` | `bool` | – | – |
| Max Material Zones To Extract At Same Time | `maxMaterialZonesToExtractAtSameTime` | `int` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Last Surface Detected | `lastSurfaceDetected` | `GameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Grabbed Object Melee Attack System | `mainGrabbedObjectMeleeAttackSystem` | `grabbedObjectMeleeAttackSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkSurfaceDown()` | 下方向のレイキャストでサーフェスを探す`checkSurfaceType(true)`を呼ぶだけ。 |
| `checkHiddenSurfacesDown()` | レイキャストを使わず近距離の`hiddenMeleeSurface`を探す`checkSurfaceType(false)`を呼ぶ。 |
| `checkSurface()` | サーフェス名・リモートイベント・検出イベントを処理し、`checkSurfaceFoundOnAttackToProcess`で攻撃側へ渡す。 |
