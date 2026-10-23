# WaypointCircuit

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/AI/WaypointCircuit.cs:6`

**概要**: Transformのリストから周回コースを組み、距離に応じた位置と方向をCatmull-Rom補間で返すウェイポイント回路。経路の追加や名前整列、位置リセットなどのエディタ補助も持つ。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Smooth Route | `smoothRoute` | `bool` | true | ウェイポイント間をCatmull-Rom曲線で滑らかにつなぐかどうか。 |
| Editor Visualisation Substeps | `editorVisualisationSubsteps` | `float` | 100 | ギズモ表示で経路を分割するステップ数。大きいほど滑らか。 / Range (1, 100) |

### Gizmo Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | シーンビューに経路のギズモを表示するかどうか。 |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | – | ギズモのラベルと線に使う色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Radius | `gizmoRadius` | `float` | – | ギズモで表示する球の半径の大きさ。 / 表示条件: `showGizmo` がオンのとき |
| Use Handle For Vertex | `useHandleForVertex` | `bool` | – | 各ウェイポイントをフリーハンドルで移動できるようにするかどうか。 / 表示条件: `showGizmo` がオンのとき |
| Handle Radius | `handleRadius` | `float` | – | フリーハンドルとして表示する球の半径。 / 表示条件: `showGizmo.boolValue && useHandleForVertex.boolValue` |
| Handle Gizmo Color | `handleGizmoColor` | `Color` | – | フリーハンドルの表示に使う色。 / 表示条件: `showGizmo.boolValue && useHandleForVertex.boolValue` |
| Show Vertex Handles | `showVertexHandles` | `bool` | – | 各ウェイポイントに位置ハンドルを表示するかどうか。 / 表示条件: `showGizmo` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `waypointList` | `List<Transform>` | new List<Transform> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getClosestPosition(Vector3 position)` | 指定位置に最も近いウェイポイントの座標を返し、見つからなければ`Vector3.zero`を返す。 |
| `getProgressValue(Vector3 position)` | 最も近いウェイポイントを探し、先頭からそこまでの累積距離を返す（先頭なら直接距離、空なら-1）。 |
| `GetRoutePoint(float dist)` | `dist`位置の座標と、少し先との差分から求めた進行方向を`RoutePoint`として返す。 |
| `GetRoutePosition(float dist)` | `dist`を`Length`で折り返し、`smoothRoute`ならCatmull-Rom、違えば線形補間で座標を返す。 |
| `addNewWayPoint()` | 末尾点の前方1m（無ければ自身の位置）に子オブジェクトを作り`waypointList`に追加して更新する。 |
| `addNewWayPointAtIndex(int index)` | 新しいウェイポイントを作って指定インデックスの右3mに置き、その直後に挿入して名前を振り直す。 |
| `renameWaypoints()` | 各ウェイポイントを1始まりの連番に改名し、親を付け直したうえでシーンを更新する。 |
| `resetWaypointsPositions()` | 全ウェイポイントのローカル位置を原点から前方2mずつ並ぶようにリセットし、シーンを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とダーティシーン更新を呼び、インスペクタ表示を更新する。 |

## 内部型

- `RoutePoint`（struct）
