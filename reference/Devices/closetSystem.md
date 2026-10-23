# closetSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/closetSystem.cs:6`

**概要**: 複数のドア付き収納を管理し、ドア開閉のアニメーション、内部オブジェクトの生成・表示切替、プレイヤーのデバイス一覧更新を行う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Open Type | `openType` | `doorOpenType` | – | ドアの開き方。平行移動か回転かを選ぶ。 |
| Use Sounds | `useSounds` | `bool` | – | ドア開閉時に効果音を再生するか。 |

### Gizmo Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | ドア位置などのギズモを表示するか。 |
| Gizmo Radius | `gizmoRadius` | `float` | – | ドア位置に描く球ギズモの半径。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Length | `gizmoArrowLength` | `float` | 1 | 回転方向を示す矢印の羽根の長さ。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Line Length | `gizmoArrowLineLength` | `float` | 2.5f | 回転方向を示す矢印の線の長さ。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Angle | `gizmoArrowAngle` | `float` | 20 | 矢印の羽根が開く角度（度）。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Color | `gizmoArrowColor` | `Color` | Color.white | 回転方向を示す矢印ギズモの表示色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.black | シーンビューでギズモに添えるラベルの文字色。 / 表示条件: `showGizmo` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `closetDoorList` | `List<closetDoorInfo>` | new List<closetDoorInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `changeDoorOpenCloseState(Transform currentDoor)` | 指定ドアの開閉コルーチンを再開始し、`openType`に応じ移動か回転で開閉する。 |
| `setCurrentPlayer(GameObject player)` | プレイヤーを保持し、`usingDevicesSystem`を取得して次回以降の一覧操作に備える。 |
| `removeDeviceFromList(GameObject objecToRemove)` | プレイヤーの`usingDevicesSystem`から対象オブジェクトをデバイス一覧より除外する。 |
| `setObjectToAddToCloset(GameObject objectToAdd)` | 収納へ追加するオブジェクトを保持するだけ。 |
| `setObjectToRemoveFromCloset(GameObject objectToRemove)` | 収納から取り出すオブジェクトを保持するだけ。 |
| `addObjectToCloset(Transform doorToAdd)` | `objectToAddToCloset`の`objectToActive`を、開いている指定ドアの内部リストへ追加し親子付けする。 |
| `removeObjectFromCloset(Transform doorToAdd)` | 指定ドアの内部リストから、`objectToRemoveFromCloset`に対応するオブジェクトを外す。 |
| `addNewDoor()` | 新規ドア情報を一覧へ追加し、`updateComponent`でInspectorへ反映する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`でコンポーネント更新を要求するだけ。 |

## 内部型

- `doorOpenType`（enum）
- `closetDoorInfo`（class）
- `objectToSpawInfo`（class）
