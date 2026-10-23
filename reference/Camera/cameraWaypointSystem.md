# cameraWaypointSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Cutscene/cameraWaypointSystem.cs:7`

**概要**: カットシーン用に、プレイヤーカメラを経由点またはベジェ曲線に沿って移動させ、終了時には元の位置と回転へ戻すコンポーネント。ウェイポイントの追加・削除・名前振り直しはエディタ用関数として提供される。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Waypoint Enabled | `cameraWaypointEnabled` | `bool` | true | OFFにするとウェイポイント移動を一切実行しない有効/無効スイッチ。 |
| Current Camera Transform | `currentCameraTransform` | `Transform` | – | 移動させるカメラのTransform。未設定ならプレイヤーから取得する。 |
| Wait Time Between Points | `waitTimeBetweenPoints` | `float` | – | 各ウェイポイント到達後、次へ動き出すまでの待ち時間（秒）。 |
| Movement Speed | `movementSpeed` | `float` | – | ウェイポイント間の移動速度。大きいほど速く移動する。 |
| Rotation Speed | `rotationSpeed` | `float` | – | 目標方向へカメラを回転させる速さ。 |
| Search Player On Scene If Not Assigned | `searchPlayerOnSceneIfNotAssigned` | `bool` | true | カメラ未設定時にシーンのプレイヤーを自動検索して設定する。 |
| Ignore Waypoint On Free Camera | `ignoreWaypointOnFreeCamera` | `bool` | – | ONにするとフリーカメラ使用中はウェイポイント移動を行わない。 |
| Ignore Waypoint On Locked Camera | `ignoreWaypointOnLockedCamera` | `bool` | – | ONにするとロックカメラ使用中はウェイポイント移動を行わない。 |
| Ignore Waypoint On FBA | `ignoreWaypointOnFBA` | `bool` | – | ONにするとFBA（フルボディアウェアネス）中は移動を行わない。 |

### Camera State Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pause Player Camera Enabled | `pausePlayerCameraEnabled` | `bool` | – | ONにするとカットシーン中プレイヤーカメラの更新を停止する。 |
| Reset Camera Position On End | `resetCameraPositionOnEnd` | `bool` | – | ONにすると終了時にカメラを元の位置と回転へ戻す。 |
| Reset Camera Position Speed | `resetCameraPositionSpeed` | `float` | 5 | 終了時に元の位置へ戻る時のカメラ移動速度。 |
| Use Main Camera Transform | `useMainCameraTransform` | `bool` | – | ONにすると現在のカメラ（フリー/ロック）のTransformを移動対象にする。 |
| Set This Transform As Camera Parent | `setThisTransformAsCameraParent` | `bool` | – | ONにすると移動中カメラをこのオブジェクトの子にする。 |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On End | `useEventOnEnd` | `bool` | – | ONにすると経路の移動完了時にイベントを呼ぶ。 |
| Event On End | `eventOnEnd` | `UnityEvent` | – | ウェイポイント移動の完了時に呼ばれるイベント。 / 表示条件: `useEventOnEnd` がオンのとき |
| Use Event To Stop Cut Scene | `useEventToStopCutScene` | `bool` | – | ONにするとカットシーン停止時にイベントを呼ぶ。 |
| Event To Stop Cutscene | `eventToStopCutscene` | `UnityEvent` | – | 移動中に停止要求があった時に呼ばれるイベント。 / 表示条件: `useEventToStopCutScene` がオンのとき |

### Bezier Path Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Bezier Curve | `useBezierCurve` | `bool` | – | ONにするとウェイポイントではなくBezierスプラインに沿って移動する。 |
| Spline | `spline` | `BezierSpline` | – | 移動経路として使う`BezierSpline`。 / 表示条件: `useBezierCurve` がオンのとき |
| Bezier Duration | `bezierDuration` | `float` | 10 | スプライン全体を移動するのにかかる時間（秒）。 / 表示条件: `useBezierCurve` がオンのとき |
| Snap Camera To First Spline Point | `snapCameraToFirstSplinePoint` | `bool` | – | ONにすると開始位置をスプラインの始点に合わせる。 / 表示条件: `useBezierCurve` がオンのとき |
| Use External Progress | `useExternalProgress` | `bool` | – | ONにすると進行度を外部関数`externalProgress`から取得する。 / 表示条件: `useBezierCurve` がオンのとき |

### Gizmo Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | ONにするとシーンビューにウェイポイントのギズモを表示する。 |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.black | ギズモに表示するウェイポイント番号の文字色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Radius | `gizmoRadius` | `float` | – | ウェイポイント位置に描く球ギズモの半径。 / 表示条件: `showGizmo` がオンのとき |
| Use Handle For Waypoints | `useHandleForWaypoints` | `bool` | – | ONにするとシーンビューでウェイポイントを移動できるハンドルを出す。 / 表示条件: `showGizmo` がオンのとき |
| Handle Radius | `handleRadius` | `float` | – | ウェイポイント移動ハンドルの表示半径。 / 表示条件: `showGizmo.boolValue && useHandleForWaypoints.boolValue` |
| Handle Gizmo Color | `handleGizmoColor` | `Color` | – | ウェイポイント移動ハンドルの色。 / 表示条件: `showGizmo.boolValue && useHandleForWaypoints.boolValue` |
| Show Waypoint Handles | `showWaypointHandles` | `bool` | – | ONにすると位置調整用の標準ハンドルを表示する。 / 表示条件: `showGizmo` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `waypointList` | `List<cameraWaypointInfo>` | new List<cameraWaypointInfo> () | – |
| `pointToLook` | `Transform` | – | – |
| `currentMovementSpeed` | `float` | – | – |
| `currentRotationSpeed` | `float` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentCameraTransform(GameObject cameraGameObject)` | nullでなければ対象の`Transform`を保持し、未保存なら元の親・ローカル位置・回転を記録する。 |
| `findPlayerOnScene()` | シーン検索設定が有効なら`GKC_Utils.findMainPlayerOnScene`でプレイヤーを探して設定する。 |
| `setCurrentPlayer(GameObject currentPlayer)` | プレイヤーのカメラ管理からピボットやカメラ種別を取得し、設定に応じて追従するカメラ`Transform`を決める。 |
| `checkMovementCoroutine(bool play)` | 有効時のみ既存の移動を止め、`play`なら経由点を用意してカメラをポーズ・親設定した上で移動コルーチンを開始する。 |
| `stopMoveThroughWayPointsCoroutine()` | 移動コルーチンを停止し、`waypointInProcess`をfalseにする。 |
| `stopWaypointsIfInProcess()` | `waypointInProcess`がtrueの時だけ、移動コルーチンの停止を呼ぶ。 |
| `stopWaypointsAndResetCameraPosition()` | 移動中ならコルーチンを止め、終了時リセット設定が有効ならカメラ位置を戻す。 |
| `resetCameraPosition()` | 現在の視点が除外対象なら何もせず、そうでなければカメラを元の位置と回転へ戻すコルーチンを開始する。 |
| `setCameraDirection()` | プレイヤーカメラの回転を自身の回転に合わせ、ピボットのローカル回転と`lookAngle`も同期させる。 |
| `setCameraWaypointEnabledState(bool state)` | `cameraWaypointEnabled`を設定するだけ。 |
| `setCustomGameObjectToLook(GameObject newGameObject)` | nullなら注視対象を解除し、そうでなければその`Transform`を注視対象に設定する。 |
| `setCustomTransformToLook(Transform newTransform)` | 注視対象を設定し、nullかどうかで`customTransformToLookActive`を更新する。 |
| `checkEventToStopCutscene()` | 経由点移動中かつ設定が有効なら`eventToStopCutscene`を発火する。 |
| `addNewWayPoint()` | 最後の経由点の前方に新しいウェイポイントを作成してリスト末尾へ追加し、`updateComponent`を呼ぶ。 |
| `addNewWayPoint(int insertAtIndex)` | 新しいウェイポイントを作成し、指定インデックスの次へ挿入して名前を振り直す。 |
| `renameAllWaypoints()` | 全ウェイポイントの名前を3桁の連番に振り直して`updateComponent`を呼ぶ。 |
| `removeWaypoint(int index)` | 指定インデックスのウェイポイントを`DestroyImmediate`で削除し、リストから除去する。 |
| `removeAllWaypoints()` | 全ウェイポイントを`DestroyImmediate`で削除し、リストを空にする。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とシーン更新を呼んでインスペクタ表示を更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnEnd` | `UnityEvent` | – |
| `eventToStopCutscene` | `UnityEvent` | – |

## 内部型

- `cameraWaypointInfo`（class）
