# hoverBoardWayPoints

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/hoverBoardWayPoints.cs:5`

**概要**: ホバーボード用レールのウェイポイント群を保持し、トリガーに進入した車両へレール移動を開始させるコンポーネント。エディタで点の追加・削除・改名も行う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Way Point Element | `wayPointElement` | `GameObject` | – | ウェイポイント追加時に複製するプレハブ。 |
| Movement Speed | `movementSpeed` | `float` | – | ウェイポイント移動の基本速度。 |
| Move In One Direction | `moveInOneDirection` | `bool` | – | 一方向のみの移動にする切替（移動処理では未参照）。 |
| Trigger Radius | `triggerRadius` | `float` | – | 各ウェイポイントのトリガー半径。 |
| Force At End | `forceAtEnd` | `float` | – | 終点で車両へ加える力の大きさ。 |
| Rails Offset | `railsOffset` | `float` | – | レールメッシュの高さ方向オフセット。 |
| Extra Scale | `extraScale` | `float` | – | レール方向のメッシュを伸ばす追加倍率。 |
| Vehicle Tag | `vehicleTag` | `string` | "vehicle" | 接近を検知する車両のタグ名を指定。 |
| Allow Movement On Both Directions | `allowMovementOnBothDirections` | `bool` | – | 逆方向への移動も許可するかの切替。 |

### Modify Speed Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Modify Movement Speed Enabled | `modifyMovementSpeedEnabled` | `bool` | true | 縦入力で速度を変えられるようにする切替。 |
| Max Movement Speed | `maxMovementSpeed` | `float` | 2 | 加速時に掛ける速度倍率の上限。 / 表示条件: `modifyMovementSpeedEnabled` がオンのとき |
| Min Movement Speed | `minMovementSpeed` | `float` | 0.1f | 減速時に掛ける速度倍率の下限。 / 表示条件: `modifyMovementSpeedEnabled` がオンのとき |
| Modify Movement Speed | `modifyMovementSpeed` | `float` | 5 | 速度倍率を変える際の補間速度。 / 表示条件: `modifyMovementSpeedEnabled` がオンのとき |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | シーンにウェイポイントのギズモを表示する切替。 |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.black | ウェイポイント番号ラベルの表示色。 |
| Gizmo Radius | `gizmoRadius` | `float` | – | ウェイポイント位置に描く球の半径。 |
| Use Handle For Vertex | `useHandleForVertex` | `bool` | – | シーンビューで自由移動ハンドルを使う切替。 |
| Handle Radius | `handleRadius` | `float` | – | 自由移動ハンドルの表示サイズ。 |
| Handle Gizmo Color | `handleGizmoColor` | `Color` | – | 自由移動ハンドルの描画に使う色。 |
| Show Vertex Handles | `showVertexHandles` | `bool` | – | 位置ハンドルギズモを表示するかの切替。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `wayPoints` | `List<wayPointsInfo>` | new List<wayPointsInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `addNewWayPoint()` | `wayPointElement`を末尾点の前方に複製して子にし、方向・トリガー・メッシュ情報を`wayPoints`に追加する。 |
| `removeWaypoint(int index)` | 指定インデックスのウェイポイントオブジェクトを即時削除して`wayPoints`から外し、シーンを更新する。 |
| `addNewWayPointAtIndex(int index)` | 指定点の前方に新しい点を複製して`index`位置に挿入し、全点の名前を振り直す。 |
| `selectObjectByIndex(int index)` | 指定インデックスのウェイポイントをエディタ上で選択するだけ。 |
| `renameAllWaypoints()` | 各ウェイポイント名を1始まりの連番に直し、兄弟順もインデックスに合わせる。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とダーティシーン更新を呼ぶだけ。 |

## 内部型

- `wayPointsInfo`（class）
