# WaypointProgressTracker

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/AI/WaypointProgressTracker.cs:4`

**概要**: `WaypointCircuit`上の進捗距離を進めながら、注視点`target`を先読み位置へ動かす追従トラッカー。スムーズとポイント間の2モードを切り替えられる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Waypoint Active | `waypointActive` | `bool` | – | – |
| Look Ahead For Target Offset | `lookAheadForTargetOffset` | `float` | 5 | – |
| Look Ahead For Target Factor | `lookAheadForTargetFactor` | `float` | .1f | – |
| Look Ahead For Speed Offset | `lookAheadForSpeedOffset` | `float` | 10 | – |
| Look Ahead For Speed Factor | `lookAheadForSpeedFactor` | `float` | .2f | – |
| Progress Style | `progressStyle` | `ProgressStyle` | ProgressStyle.SmoothAlongRoute | – |
| Point To Point Threshold | `pointToPointThreshold` | `float` | 4 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Progress Distance | `progressDistance` | `float` | – | – |
| Progress Num | `progressNum` | `int` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle AI | `vehicleAI` | `vehicleAINavMesh` | – | – |
| Target | `target` | `Transform` | – | – |
| Circuit | `circuit` | `WaypointCircuit` | – | – |
| Vehicle Transform | `vehicleTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setWaypointActiveState(bool state)` | `waypointActive`を設定し、回路追従とAIの走行状態を有効/無効に切り替える。 |
| `activateTrackState()` | `waypointActive`がfalseのときだけ追従を有効にして再開する。 |
| `stopTrackState()` | `waypointActive`がtrueのときだけ追従を無効にして止める。 |
| `resetTrackerState()` | 回路が無ければ戻り、あれば`target`をモードに応じた位置に合わせ`progressDistance`を再計算する。 |

## 内部型

- `ProgressStyle`（enum）
