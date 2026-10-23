# BezierSpline

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/BezierSpline.cs:6`

**概要**: 3次ベジェスプラインを制御点・モード・ループ設定で管理するコンポーネントで、位置/速度/方向の取得や最近点探索、エディタでのカーブ追加削除を提供する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Direction Scale | `directionScale` | `float` | 0.5f | 進行方向を示す緑の矢印の長さ倍率。 |
| New Point Offset | `newPointOffset` | `float` | 0.2f | カーブ追加時に新しい点をずらす距離。 |
| New Point Bezier Offset | `newPointBezierOffset` | `float` | 0.2f | ベジェ点追加時に制御点をずらす量（現在は未参照）。 |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Handle Size | `handleSize` | `float` | 0.04f | スプライン点ハンドルの表示サイズ倍率。 |
| Pick Size | `pickSize` | `float` | 0.06f | スプライン点をクリック選択できる判定サイズ倍率。 |
| Show Gizmo | `showGizmo` | `bool` | – | シーンビューにスプラインの線とハンドルを表示する。 |
| Show Look Direction Gizmo | `showLookDirectionGizmo` | `bool` | – | 注視方向リストの球と矢印ギズモを表示する。 |
| Look Direction Gizmo Radius | `lookDirectionGizmoRadius` | `float` | 0.05f | 注視方向ギズモの球の半径。 |
| Look Direction Arrow Length | `lookDirectionArrowLength` | `float` | 1 | 注視方向ギズモの矢印の長さ。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `splinePointList` | `List<splinePointInfo>` | new List<splinePointInfo> () | – |
| `lookDirectionList` | `List<Transform>` | new List<Transform> () | – |
| `selectedIndex` | `int` | -1 | – |
| `points` | `List<Vector3>` | new List<Vector3> () | – |
| `modes` | `List<BezierControlPointMode>` | new List<BezierControlPointMode> () | – |
| `loop` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `GetControlPoint(int index)` | `points` から指定インデックスの制御点を返すだけ。 |
| `SetControlPoint(int index, Vector3 point)` | 制御点を移動し、ループ設定に応じて隣接するハンドル点を同じ差分だけ動かしてモードを適用する。 |
| `GetControlPointMode(int index)` | `modes` から該当する制御点モードを返すだけ。 |
| `SetControlPointMode(int index, BezierControlPointMode mode)` | 制御点モードを設定し、ループ時は端のモードも揃えてから `EnforceMode` を適用する。 |
| `GetPoint(float t)` | `t` をカーブ区間に変換し、3次ベジェ点をワールド座標で返す。 |
| `GetLookDirection(float t)` | `lookDirectionList` から該当区間のローカル角度を返す。 |
| `GetLookTransform(float t)` | `lookDirectionList` から該当区間の Transform を返す。 |
| `getPointIndex(float t)` | `t` に対応するカーブ区間のインデックスを返す。 |
| `GetVelocity(float t)` | 3次ベジェの一次微分からワールド空間の速度ベクトルを返す。 |
| `GetDirection(float t)` | `GetVelocity` を正規化した方向ベクトルを返す。 |
| `setInitialSplinePoint(Vector3 position)` | ワールド位置をローカルに変換して始点 `points[0]` に設定する。 |
| `setFinalSplinePoint(Vector3 position)` | ワールド位置をローカルに変換して終点 `points[points.Count - 1]` に設定する。 |
| `AccuracyToStepSize(float accuracy)` | `accuracy` を探索用ステップ幅へ変換し、0.001〜0.2 にクランプして返す。 |
| `FindNearestPointTo(Vector3 worldPos, float accuracy = 100f, int secondPassIterations = 7, float secondPassExtents = 0.025f)` | 正規化 t を受け取らない版で、もう一方の `FindNearestPointTo` の結果のみを返す。 |
| `FindNearestPointTo(Vector3 worldPos, out float normalizedT, float accuracy = 100f, int secondPassIterations = 7, float secondPassExtents = 0.025f)` | 粗いステップ探索と2段目の二分探索で、スプライン上の最近点とその正規化 `t` を求める。 |
| `setSelectedIndex(int index)` | 選択インデックスを設定し、コンポーネントを更新する。 |
| `AddCurve(int index, bool addingAtTheEnd)` | 指定位置に3つの制御点とモードを挿入してカーブを追加し、選択インデックスを更新する。 |
| `removeCurve(int index)` | 3の倍数インデックスのカーブを制御点ごと削除し、残りが4点ならループを解除して更新する。 |
| `alignLookDirection(bool adjustPositionAndRotation)` | `lookDirectionList` の各要素を3点おきの制御点位置へ移動し、必要なら回転も初期化する。 |
| `updateComponent()` | `GKC_Utils.updateComponent` を呼ぶだけ。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static Vector3 GetPoint(Vector3 p0, Vector3 p1, Vector3 p2, float t)` | – |
| `static Vector3 GetFirstDerivative(Vector3 p0, Vector3 p1, Vector3 p2, float t)` | – |
| `static Vector3 GetPoint(Vector3 p0, Vector3 p1, Vector3 p2, Vector3 p3, float t)` | – |
| `static Vector3 GetFirstDerivative(Vector3 p0, Vector3 p1, Vector3 p2, Vector3 p3, float t)` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`Reset()`

</details>

## 内部型

- `BezierControlPointMode`（enum）
- `splinePointInfo`（class）
