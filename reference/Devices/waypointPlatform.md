# waypointPlatform

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/waypointPlatform.cs:6`

**概要**: ウェイポイント間を往復・周回する移動プラットフォームで、乗客や車両の親子付け、トリガー検出、ミラー移動、到達イベントを扱う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Platform Active | `platformActive` | `bool` | true | プラットフォームの移動を有効にするか。 |
| Player Tag | `playerTag` | `string` | "Player" | 乗客として扱うプレイヤーのタグ。 |
| Vehicle Tag | `vehicleTag` | `string` | "vehicle" | 車両として扱い親子付けするタグ。 |
| Repeat Waypoints | `repeatWaypoints` | `bool` | – | 終点まで移動した後に先頭から繰り返すか。 |
| Move In Circles | `moveInCircles` | `bool` | – | 最後のポイントから最初へ戻る周回移動にするか。 |
| Stop If Player Outside | `stopIfPlayerOutside` | `bool` | – | プレイヤーが降りると停止し、乗ると再開するか。 |
| Wait Time Between Points | `waitTimeBetweenPoints` | `float` | – | 各ポイントに到着した後に待つ秒数。 |
| Movement Speed | `movementSpeed` | `float` | – | ポイント間を移動する時の速さ。 |
| Moving Forward | `movingForward` | `bool` | true | 最初に進む向きを順方向にするか逆順にするか。 |
| Use Just To Move Platform | `useJustToMovePlatform` | `bool` | – | 乗降と自動移動を無効にし、外部から動かす専用にするか。 |

### Mirror Platform Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Mirror Platform Movement | `mirrorPlatformMovement` | `bool` | – | 別のプラットフォームの移動量を複製するか。 |
| Mirror Movement Direction | `mirrorMovementDirection` | `Vector3` | Vector3.one | 複製した移動量を各軸へ振り分ける方向。 |
| Platform To Mirror | `platformToMirror` | `waypointPlatform` | – | 移動量を複製する元のプラットフォーム。 |

### Return To Transform Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Return To Transform When Player Exits | `returnToTransformWhenPlayerExits` | `bool` | – | 全員降りたら指定した位置へ戻すか。 |
| Transform To Return When Player Exits | `transformToReturnWhenPlayerExits` | `Transform` | – | 戻り先として使うTransform。 / 表示条件: `returnToTransformWhenPlayerExits` がオンのとき |
| Delay To Return When Player Exits | `delayToReturnWhenPlayerExits` | `float` | – | 降車してから戻り始めるまでの秒数。 / 表示条件: `returnToTransformWhenPlayerExits` がオンのとき |
| Return Movement Speed | `returnMovementSpeed` | `float` | – | 戻る時の速さ。0以下なら通常の速度を使う。 / 表示条件: `returnToTransformWhenPlayerExits` がオンのとき |
| Reset Waypoint Index On Return | `resetWaypointIndexOnReturn` | `bool` | true | 戻り完了後に経路を先頭からやり直すか。 / 表示条件: `returnToTransformWhenPlayerExits` がオンのとき |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Waypoint Reached | `useEventOnWaypointReached` | `bool` | – | 指定したポイントへの到達時にイベントを呼ぶか。 |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Platform Transform | `platformTransform` | `Transform` | – | 実際に移動させるTransform。未設定なら自身を使う。 |
| Device String Action Manager | `deviceStringActionManager` | `deviceStringAction` | – | ボタン操作時のアクション名を表示するコンポーネント。 |
| Waypoints Parent | `waypointsParent` | `Transform` | – | 追加したポイントを格納する親Transform。 |

### Gizmo Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | シーンビューに経路のギズモを表示するか。 |
| Show Vertex Handles | `showVertexHandles` | `bool` | – | 各ポイントに位置ハンドルを表示するか。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.black | ポイント番号ラベルに使う文字色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Radius | `gizmoRadius` | `float` | – | ポイントを示す球ギズモの半径。 / 表示条件: `showGizmo` がオンのとき |
| Use Handle For Vertex | `useHandleForVertex` | `bool` | – | ポイントを移動させるハンドルを表示するか。 / 表示条件: `showGizmo` がオンのとき |
| Handle Radius | `handleRadius` | `float` | – | ポイント移動ハンドルの大きさ。 / 表示条件: `showGizmo.boolValue && useHandleForVertex.boolValue` |
| Handle Gizmo Color | `handleGizmoColor` | `Color` | – | ポイント移動ハンドルを描く色。 / 表示条件: `showGizmo.boolValue && useHandleForVertex.boolValue` |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `wayPoints` | `List<Transform>` | new List<Transform> () | – |
| `tagToCheckToMove` | `List<string>` | new List<string> () | – |
| `tagToCheckBelow` | `List<string>` | new List<string> () | – |
| `objectsDetectedBelowList` | `List<GameObject>` | new List<GameObject> () | – |
| `eventOnWaypointReachedList` | `List<eventOnWaypointInfo>` | new List<eventOnWaypointInfo> () | – |
| `passengersInfoList` | `List<passengersInfo>` | new List<passengersInfo> () | – |
| `vehiclesInfoList` | `List<vehiclesInfo>` | new List<vehiclesInfo> () | – |
| `distanceToMirror` | `float` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setMirroringPlatformActiveState(bool state)` | ミラー無効なら何もせず、有効ならフラグを設定し基準位置を現在位置で更新する。 |
| `addPassenger(Transform newPassenger)` | 未登録なら `passengersInfoList` に乗客と `playerController` を追加する。 |
| `addVehicle(Transform newVehicle)` | 未登録なら `vehiclesInfoList` に車両と `vehicleHUDManager` を追加する。 |
| `disablePlatform()` | 移動停止と `platformActive` 解除、乗客・車両の親解除、コライダーと自身の無効化を行う。 |
| `activatePlatformMovement()` | 経路が空なら現在位置以降のウェイポイントを詰め直し、移動コルーチンを開始する。 |
| `deactivatePlatformMovement()` | `checkMovementCoroutine(false)` を呼び移動を止めるだけ。 |
| `checkMovementCoroutine(bool play)` | 移動を止め、`platformActive` ならミラーを同期、`play` のときだけ移動コルーチンを開始する。 |
| `stopPlatformMovement()` | 実行中の `movement` コルーチンを停止し、その場で移動を止める。 |
| `activetMovementByButton()` | 移動方向を反転して経路を組み直し、デバイス表示名を更新して移動を開始する。 |
| `setDeviceStringActionState(bool state)` | `deviceStringActionManager` があれば `changeActionName` を呼ぶだけ。 |
| `addObjectDetectedBelow(GameObject objectToCheck)` | タグ一致か Rigidbody 持ちなら検出リストへ加え、経路番号を先頭に戻して移動を再開する。 |
| `removeObjectDetectedBelow(GameObject objectToCheck)` | 検出リストに含まれていれば取り除くだけ。 |
| `addNewWayPoint()` | 最後のウェイポイント前方に新しい点を作成してリストへ追加し、シーンを更新する。 |

## 内部型

- `eventOnWaypointInfo`（class）
- `passengersInfo`（class）
- `vehiclesInfo`（class）
