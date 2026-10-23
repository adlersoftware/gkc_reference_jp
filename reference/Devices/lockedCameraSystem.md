# lockedCameraSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/lockedCameraSystem.cs:6`

**概要**: 固定カメラ（locked camera）のゾーン・カメラ軸・トリガー・ウェイポイントを保持し、`playerCamera` にカメラ切替を指示するコンポーネント。メソッドの大半はエディタ用の要素生成/削除と、全カメラ共通フラグの一括設定。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer To Place New Camera | `layerToPlaceNewCamera` | `LayerMask` | – | 新しいカメラを配置する時のレイキャスト対象レイヤー。 |
| Use Raycast To Place Cameras | `useRaycastToPlaceCameras` | `bool` | – | ONにすると追加時にレイキャスト位置へカメラを置く。 |
| Event Trigger Scale | `eventTriggerScale` | `Vector3` | – | 生成するカメラトリガーのBoxColliderの大きさ。 |

### Prefab Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Transform Prefab | `cameraTransformPrefab` | `GameObject` | – | カメラ軸を生成するためのプレハブ。 |
| Camera Trigger Prefab | `cameraTriggerPrefab` | `GameObject` | – | カメラ切替トリガーを生成するためのプレハブ。 |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | ONにするとシーンビューにギズモを表示する。 |
| Show Gizmo On Playing | `showGizmoOnPlaying` | `bool` | – | ONにすると再生中もギズモを表示する。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Color | `gizmoColor` | `Color` | – | 軸や球などのギズモを描画する時の色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | – | シーンビューに出すギズモのラベル色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Radius | `gizmoRadius` | `float` | 0.3f | 軸位置に描く球ギズモの表示半径。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Length | `gizmoArrowLength` | `float` | 1.4f | カメラ向きを示す矢印の頭の長さ。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Line Length | `gizmoArrowLineLength` | `float` | 3.4f | カメラ向きを示す矢印の線の長さ。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Angle | `gizmoArrowAngle` | `float` | 20 | カメラ向きを示す矢印の開き角度。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Color | `gizmoArrowColor` | `Color` | – | カメラ向きを示す矢印ギズモの色。 / 表示条件: `showGizmo` がオンのとき |
| Bound Color | `boundColor` | `Color` | Color.red | 追従範囲を示すギズモの枠線の色。 / 表示条件: `showGizmo` がオンのとき |

### Free Handles Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Free Handle | `useFreeHandle` | `bool` | – | ONにすると位置をフリーハンドルで編集できる。 / 表示条件: `showGizmo` がオンのとき |
| Handle Radius | `handleRadius` | `float` | 0.1f | フリーハンドルの当たり判定の半径。 / 表示条件: `showGizmo.boolValue && useFreeHandle.boolValue` |
| Handle Gizmo Color | `handleGizmoColor` | `Color` | – | 位置調整ハンドルに使うギズモの色。 / 表示条件: `showGizmo.boolValue && useFreeHandle.boolValue` |
| Show Do Position Handles | `showDoPositionHandles` | `bool` | – | ONにすると位置調整用のハンドルを表示する。 / 表示条件: `showGizmo` がオンのとき |
| Show Buttons | `showButtons` | `bool` | true | ONにするとギズモ上の操作ボタンを表示する。 / 表示条件: `showGizmo` がオンのとき |
| Buttons Size | `buttonsSize` | `float` | 0.1f | ギズモ上に出す操作ボタンの表示サイズ。 / 表示条件: `showGizmo.boolValue && showButtons.boolValue` |

### Floors Triggers Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Floor Triggers Cubes | `showFloorTriggersCubes` | `bool` | – | ONにするとトリガー範囲を立方体で表示する。 / 表示条件: `showGizmo` がオンのとき |
| Floor Triggers Cubes Color | `floorTriggersCubesColor` | `Color` | – | トリガー範囲を示す立方体の色。 / 表示条件: `showGizmo.boolValue && showFloorTriggersCubes.boolValue` |

### Waypoint List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Waypoint List | `showWaypointList` | `bool` | – | ONにするとウェイポイントを球で表示する。 / 表示条件: `showGizmo` がオンのとき |
| Waypoint List Color | `waypointListColor` | `Color` | – | ウェイポイントを示す球ギズモの色。 / 表示条件: `showGizmo.boolValue && showWaypointListProp.boolValue` |

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera View Explanation | `cameraViewExplanation` | `string` | "" +         "Camera Axis is the piv… | カメラ軸と位置の調整方法を説明する文章。 / TextArea (5, 10) |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `lockedCameraList` | `List<cameraElement>` | new List<cameraElement> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCameraTransform(GameObject cameraTransform)` | 指定した `cameraPosition` のカメラを `locked`/`free` で切替え、2.5D制限を適用して選択状態を更新する。 |
| `findPlayerOnScene()` | `GKC_Utils.findMainPlayerOnScene` で見つけたプレイヤーを `getPlayerGameObject` に渡すだけ。 |
| `getPlayerGameObject(GameObject objectToCheck)` | `currentPlayer` と `playerCameraManager` を設定し、乗り物なら運転中のドライバーに置換える。 |
| `setLockedCameraToEditorCameraPosition(int lockedCameraListIndex, int cameraTransformListIndex)` | エディタカメラの位置・角度を対象カメラの `axis`/`cameraPosition` とピボットへコピーして更新する。 |
| `setEditorCameraPositionToLockedCamera(int lockedCameraListIndex, int cameraTransformListIndex)` | 指定カメラの `cameraPosition` へ `GKC_Utils.alignViewToObject` でエディタ視点を合わせるだけ。 |
| `duplicateLockedCamera(int lockedCameraListIndex, int cameraTransformListIndex)` | 新しいカメラ要素を追加し、指定要素の全設定値・位置・トリガーを複製して更新する。 |
| `assignPlayerToStartOnLockedCamera(GameObject newPlayer)` | 先頭カメラ要素の `startGameWithThisView` を有効にし `playerForView` に指定プレイヤーを設定する。 |
| `addLookAtCustomMultipleTargetsList(Transform newTransform)` | 先頭カメラの注視対象リストへ、重複しないよう `newTransform` を追加する。 |
| `removeLookAtCustomMultipleTargetsList(Transform newTransform)` | 先頭カメラの注視対象リストから `newTransform` を削除する。 |
| `addOrRemoveLookAtCustomMultipleTargetsList(Transform newTransform, bool state)` | 先頭カメラの注視対象リストへ `state` に応じて追加または削除する。 |
| `addNewCameraTransformElememnt(int index)` | 指定ゾーンへ `cameraTransformPrefab` を複製し、`cameraAxis` とイベントトリガーを登録する。 |
| `removeNewCameraTransformElememnt(int lockedCameraListIndex, int cameraTransformListIndex, bool updateInspector)` | 対象カメラ要素のオブジェクトを削除し、`updateInspector` 時のみリストからも除去する。 |
| `removeAllCameraTransformElements(int index)` | 指定ゾーンの全カメラ要素を削除してリストを空にし、更新する。 |
| `removeAllCameraZones()` | 全ゾーンのカメラ要素とゾーンを削除し、`lockedCameraList` を空にする。 |
| `addNewCameraZone()` | `New Camera Zone` オブジェクトと `cameraElement` を生成して一覧に追加する。 |
| `removeCameraZone(int index, bool updateInspector)` | 指定ゾーンのカメラ要素と親オブジェクトを削除し、必要なら一覧から除去する。 |
| `addCameraTrigger(int lockedCameraListIndex, int cameraTransformListIndex)` | カメラトリガーのプレハブを複製して親に付け、送信対象にカメラ位置を設定する。 |
| `removeCameraTrigger(int lockedCameraListIndex, int cameraTransformListIndex, int cameraTriggerIndex, bool updateInspector)` | 指定トリガーのゲームオブジェクトを削除し、必要ならリストからも除去する。 |
| `removeAllCameraTriggers(int lockedCameraListIndex, int cameraTransformListIndex)` | 対象カメラの全トリガーを削除してリストを空にする。 |
| `selectCurrentTrigger(int lockedCameraListIndex, int cameraTransformListIndex, int cameraTriggerIndex)` | 指定トリガーを `GKC_Utils.setActiveGameObjectInEditor` でエディタ上で選択するだけ。 |
| `addWaypoint(int lockedCameraListIndex, int cameraTransformListIndex)` | `Waypoint` オブジェクトを生成して親の下に置き、`waypointList` に追加する。 |
| `removeWaypoint(int lockedCameraListIndex, int cameraTransformListIndex, int waypointIndex, bool updateInspector)` | 指定ウェイポイントのオブジェクトを削除し、必要ならリストからも除去する。 |
| `removeAllWaypoints(int lockedCameraListIndex, int cameraTransformListIndex)` | 対象カメラの全ウェイポイントを削除してリストを空にする。 |
| `setGizmosState(bool state)` | 全カメラ要素の `showGizmo` を `state` に設定するだけ。 |
| `setCameraParentListName(string name, int index)` | 指定ゾーンの `parentList` の名前を `name` に変更するだけ。 |
| `addLockedCameraPivot(int lockedCameraListIndex, int cameraTransformListIndex)` | ピボット未設定時のみ `Camera Pivot` を生成して `axis` をその子に移す。 |
| `addLockedCameraPivot2_5d(int lockedCameraListIndex, int cameraTransformListIndex)` | ピボットがある場合に `2.5d Pivot` と注視方向オブジェクトを生成して設定する。 |
| `addLockedCameraPivotTopDown(int lockedCameraListIndex, int cameraTransformListIndex)` | ピボットがある場合に `Top Down Pivot` と注視方向オブジェクトを生成して設定する。 |
| `setAllCamerasAsPointAndClickOrFree(bool state)` | 全カメラの `usePointAndClickSystem` を `state` に揃えて更新する。 |
| `setCanChangeCameraToFreeViewByInputInAllCameras(bool state)` | 全カメラの `canChangeCameraToFreeViewByInput` を `state` に揃えて更新する。 |
| `setAllCamerasAsTankControlsOrRegular(bool state)` | 全カメラの `useTankControls` を `state` に揃えて更新する。 |
| `setAllCamerasAsRelativeMovementsOrRegular(bool state)` | 全カメラの `useRelativeMovementToLockedCamera` を `state` に揃えて更新する。 |
| `setAllCamerasAsChangeRootMotionEnabledOrDisabled(bool state)` | 全カメラの `changeRootMotionActive` を `state` に揃えて更新する。 |
| `setAllCamerasAsUseRootMotionEnabledOrDisabled(bool state)` | 全カメラの `useRootMotionActive` を `state` に揃えて更新する。 |
| `setAllCamerasAsUseClampAimDirectionEnabledOrDisabled(bool state)` | 全カメラの `clampAimDirections` を `state` に揃えて更新する。 |
| `updateTriggers()` | 全カメラの各トリガーの `eventTriggerSystem.dontUseDelay` を有効にして更新する。 |
| `changeViewToCameraInEditor(int lockedCameraListIndex, int cameraTransformListIndex)` | プレイヤーがいるとき指定カメラへ切替え、必要ならスムーズ遷移を一時的に無効化する。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static void setEditorCameraPosition(Transform transformToUse)` | – |
| `static void drawBoundGizmo(Vector3 currentPosition, cameraAxis currentCameraAxis, Color newBoundColor)` | – |

## 内部型

- `cameraElement`（class）
- `cameraAxis`（class）
