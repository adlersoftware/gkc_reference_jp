# AIWayPointPatrol

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/AIWayPointPatrol.cs:5`

**概要**: 巡回経路（パトロールとウェイポイント）のTransform階層を編集するための補助コンポーネント。`patrolList`を保持し、地点の追加・削除、地面への吸着、シーンへの反映を行う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Wait Time Between Points | `waitTimeBetweenPoints` | `float` | – | 各ウェイポイント到達後、次へ進むまで待つ秒数。 |
| Layer Mask | `layerMask` | `LayerMask` | – | `Adjust To Surface`で地面を検出するレイキャストの対象レイヤー。 |
| New Waypoint Offset | `newWaypointOffset` | `Vector3` | – | 新しい地点を追加するときの、前回地点からの相対距離。 |
| Surface Adjusment Offset | `surfaceAdjusmentOffset` | `float` | 0.1f | 地表に合わせた地点をサーフェスから浮かせる高さ。 |

### Gizmo Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | シーンビューに巡回地点の球とラベルを表示する。 |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | – | シーンビューに表示する地点ラベルの文字色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Radius | `gizmoRadius` | `float` | – | 巡回地点とウェイポイントを描く球ギズモの半径。 / 表示条件: `showGizmo` がオンのとき |
| Use Handle For Vertex | `useHandleForVertex` | `bool` | – | 各地点にドラッグ移動用の`FreeMoveHandle`を表示する。 / 表示条件: `showGizmo` がオンのとき |
| Use Free Handle | `useFreeHandle` | `bool` | – | 各地点にUnity標準の移動・回転ハンドルを表示する。 / 表示条件: `showGizmo` がオンのとき |
| Handle Radius | `handleRadius` | `float` | – | 上記ハンドルの表示サイズと当たり判定の半径。 / 表示条件: `showGizmo.boolValue && useHandleForVertex.boolValue \|\| useFreeHandle.boolValue` |
| Handle Gizmo Color | `handleGizmoColor` | `Color` | – | ハンドルを描画するときの色。 / 表示条件: `showGizmo.boolValue && useHandleForVertex.boolValue \|\| useFreeHandle.boolValue` |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `patrolList` | `List<patrolElementInfo>` | new List<patrolElementInfo> () | – |
| `currentPatrol` | `patrolElementInfo` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `addNewPatrol()` | `newWaypointOffset`を加えた位置に`Patrol_N`オブジェクトを生成して`patrolList`に追加し、シーンを更新する。 |
| `clearPatrolList()` | 各パトロールに`clearWayPoint`を呼び、残ったパトロールTransformを破棄してリストを空にする。 |
| `addNewWayPoint(int index)` | 指定パトロールの最後の地点からオフセットした位置にウェイポイントを生成して追加する。 |
| `removeWaypoint(int patrolIndex, int waypointIndex)` | 指定ウェイポイントを即時破棄してリストから削除し、シーンを更新する。 |
| `clearWayPoint(int index)` | 指定パトロールの全ウェイポイントとパトロール本体を破棄し、リストから削除する。 |
| `adjustWayPoints()` | 各ウェイポイントから下方向にレイキャストし、`layerMask`の地面へ`surfaceAdjusmentOffset`分浮かせて配置する。 |
| `invertPath()` | 空の実装で何もしない。 |

## 内部型

- `patrolElementInfo`（class）
