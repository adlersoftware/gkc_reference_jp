# vehicleCameraController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `cameraControllerManager`
- **ソース**: `Camera/Vehicles/vehicleCameraController.cs:8`

**概要**: 車両運転中のカメラを、複数の`vehicleCameraStateInfo`状態の切り替えで管理するコンポーネント。注視方向・ズーム・揺れ・衝突距離・乗降時のリセットを扱い、状態変更は各マネージャへ通知される。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Third Person Vertical Rotation Speed | `thirdPersonVerticalRotationSpeed` | `float` | 5 | 三人称視点での上下方向のカメラ回転感度。 |
| Third Person Horizontal Rotation Speed | `thirdPersonHorizontalRotationSpeed` | `float` | 5 | 三人称視点での左右方向のカメラ回転感度。 |
| First Person Vertical Rotation Speed | `firstPersonVerticalRotationSpeed` | `float` | 5 | 一人称視点での上下方向のカメラ回転感度。 |
| First Person Horizontal Rotation Speed | `firstPersonHorizontalRotationSpeed` | `float` | 5 | 一人称視点での左右方向のカメラ回転感度。 |
| Clip Cast Radius | `clipCastRadius` | `float` | 0.16f | カメラ衝突判定に使う球キャストの半径。 |
| Back Clip Speed | `backClipSpeed` | `float` | – | 遮蔽物から元の距離へ戻るときの補間速度。 |
| Maximum Boost Distance | `maximumBoostDistance` | `float` | – | ブースト時にカメラを後方へ下げる最大距離。 |
| Camera Boost Speed | `cameraBoostSpeed` | `float` | – | ブースト時にカメラを前後へ動かす速さ。 |
| Camera Change Enabled | `cameraChangeEnabled` | `bool` | – | オンにすると入力でカメラステートを切り替えられる。 |
| Smooth Between State | `smoothBetweenState` | `float` | – | ステート切替時のカメラ移動を補間する速さ。 |
| Collision Layer | `layer` | `LayerMask` | – | カメラ衝突判定の球キャストに使うレイヤー。 |
| Smooth Transitions In New Camera Fov | `smoothTransitionsInNewCameraFov` | `bool` | – | オンにすると新しい画角への変更を滑らかに行う。 |
| Reset Camera Rotation On Get Off | `resetCameraRotationOnGetOff` | `bool` | – | オンにすると降車時にカメラの回転を初期化する。 |

### Smooth Camera Rotation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Smooth Camera Rotation | `useSmoothCameraRotation` | `bool` | – | オンにするとカメラの回転を補間して滑らかにする。 |
| Use Smooth Camera Rotation Third Person | `useSmoothCameraRotationThirdPerson` | `bool` | – | 三人称視点で回転の補間を個別に有効にする。 / 表示条件: `useSmoothCameraRotation` がオンのとき |
| Smooth Camera Rotation Speed Vertical Third Person | `smoothCameraRotationSpeedVerticalThirdPerson` | `float` | 10 | 三人称視点で上下回転を補間する速さ。 / 表示条件: `useSmoothCameraRotation.boolValue && useSmoothCameraRotationThirdPerson.boolValue` |
| Smooth Camera Rotation Speed Horizontal Third Person | `smoothCameraRotationSpeedHorizontalThirdPerson` | `float` | 10 | 三人称視点で左右回転を補間する速さ。 / 表示条件: `useSmoothCameraRotation.boolValue && useSmoothCameraRotationThirdPerson.boolValue` |
| Use Smooth Camera Rotation First Person | `useSmoothCameraRotationFirstPerson` | `bool` | – | 一人称視点で回転の補間を個別に有効にする。 / 表示条件: `useSmoothCameraRotation` がオンのとき |
| Smooth Camera Rotation Speed Vertical First Person | `smoothCameraRotationSpeedVerticalFirstPerson` | `float` | 10 | 一人称視点で上下回転を補間する速さ。 / 表示条件: `useSmoothCameraRotation.boolValue && useSmoothCameraRotationFirstPerson.boolValue` |
| Smooth Camera Rotation Speed Horizontal First Person | `smoothCameraRotationSpeedHorizontalFirstPerson` | `float` | 10 | 一人称視点で左右回転を補間する速さ。 / 表示条件: `useSmoothCameraRotation.boolValue && useSmoothCameraRotationFirstPerson.boolValue` |

### Follow Position Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Smooth Camera Follow | `useSmoothCameraFollow` | `bool` | – | オンにすると車両への追従位置を補間して滑らかにする。 |
| Smooth Camera Follow Speed | `smoothCameraFollowSpeed` | `float` | – | 車両への追従位置を補間する速さ。 / 表示条件: `useSmoothCameraFollow` がオンのとき |
| Smooth Camera Follow Max Distance | `smoothCameraFollowMaxDistance` | `float` | – | 追従速度を切り替える距離のしきい値。 / 表示条件: `useSmoothCameraFollow` がオンのとき |
| Smooth Camera Follow Max Distance Speed | `smoothCameraFollowMaxDistanceSpeed` | `float` | – | しきい値超過時に追従速度へ掛ける倍率。 / 表示条件: `useSmoothCameraFollow` がオンのとき |

### Zoom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Zoom Enabled | `zoomEnabled` | `bool` | – | オンにすると車両カメラのズーム入力を有効にする。 |

### Vehicle Camera States

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Default State Name | `defaultStateName` | `string` | "Third Person" | 初期カメラステート名を保持する文字列。 |
| Current State Name | `currentStateName` | `string` | – | 現在適用されているカメラステート名。 |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Send Current Camera Transform On Change State | `sendCurrentCameraTransformOnChangeState` | `bool` | – | オンにするとステート変更時にカメラ位置をイベントで送る。 |
| Event To Send Current Camera Transform On Change State | `eventToSendCurrentCameraTransformOnChangeState` | `eventParameters.eventToCallWithTransform` | – | ステート変更時に現在の`Transform`を通知するイベント。 / 表示条件: `sendCurrentCameraTransformOnChangeState` がオンのとき |

### Vehicle Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle | `vehicle` | `GameObject` | – | このカメラが追従する車両のオブジェクト。 / 表示条件: `showVehicleElements` がオンのとき |
| Vehicle Transform To Follow | `vehicleTransformToFollow` | `Transform` | – | カメラが位置を追従する車両側のトランスフォーム。 / 表示条件: `showVehicleElements` がオンのとき |
| IK Driving Manager | `IKDrivingManager` | `IKDrivingSystem` | – | 搭乗時の一人称状態を設定する運転システム。 / 表示条件: `showVehicleElements` がオンのとき |
| Weapon Manager | `weaponManager` | `vehicleWeaponSystem` | – | 現在のカメラ情報を受け取る車両武器システム。 / 表示条件: `showVehicleElements` がオンのとき |
| Hud Manager | `hudManager` | `vehicleHUDManager` | – | カメラ方向の基準を受け取る車両HUD管理。 / 表示条件: `showVehicleElements` がオンのとき |
| Action Manager | `actionManager` | `inputActionManager` | – | マウス軸とポーズ状態を取得する入力管理。 / 表示条件: `showVehicleElements` がオンのとき |
| Gravity Control | `gravityControl` | `vehicleGravityControl` | – | カメラのピボットを渡す車両重力制御。 / 表示条件: `showVehicleElements` がオンのとき |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | 車両速度の算出に使う`Rigidbody`。 / 表示条件: `showVehicleElements` がオンのとき |
| Shaking Manager | `shakingManager` | `vehicleCameraShake` | – | 揺れの開始と停止を指示するカメラシェイク管理。 / 表示条件: `showVehicleElements` がオンのとき |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | オンにすると各カメラステートのギズモを描画する。 |
| Gizmo Radius | `gizmoRadius` | `float` | – | ピボットとカメラ位置に描く球の半径。 / 表示条件: `showGizmo` がオンのとき |
| Label Gizmo Color | `labelGizmoColor` | `Color` | – | シーンビューに出すステート名ラベルの文字色。 / 表示条件: `showGizmo` がオンのとき |
| Show Camera Direction Gizmo | `showCameraDirectionGizmo` | `bool` | – | オンにするとカメラの向きを示す矢印を描画する。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Length | `gizmoArrowLength` | `float` | 1 | カメラ向き矢印の先端パーツの長さ。 / 表示条件: `showGizmo.boolValue && showCameraDirectionGizmo.boolValue` |
| Gizmo Arrow Line Length | `gizmoArrowLineLength` | `float` | 2.5f | カメラ向き矢印の線分として描く長さ。 / 表示条件: `showGizmo.boolValue && showCameraDirectionGizmo.boolValue` |
| Gizmo Arrow Angle | `gizmoArrowAngle` | `float` | 20 | カメラ向き矢印の先端を開く角度。 / 表示条件: `showGizmo.boolValue && showCameraDirectionGizmo.boolValue` |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `currentVerticalRotationSpeed` | `float` | – | – |
| `currentHorizontalRotationSpeed` | `float` | – | – |
| `cameraStateIndex` | `int` | – | – |
| `vehicleCameraStates` | `List<vehicleCameraStateInfo>` | new List<vehicleCameraStateInfo> () | – |
| `shakeSettings` | `shakeSettingsInfo` | – | – |
| `cameraPaused` | `bool` | – | – |
| `isFirstPerson` | `bool` | – | – |
| `usingZoomOn` | `bool` | – | – |
| `currentState` | `vehicleCameraStateInfo` | – | – |
| `drivingVehicle` | `bool` | – | – |
| `lookAngle` | `Vector2` | – | – |
| `showShakeSettings` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getLookDirection()` | 現在の注視方向を返し、一人称はピボットの前方、デッドゾーン内は`Vector3.forward`になる。 |
| `setZoom(bool state)` | ズーム可否を確認して`usingZoomOn`を切り替え、FOVと縦横の回転速度をズーム用または元の値へ設定する。 |
| `disableZoom()` | ズーム中なら`usingZoomOn`をfalseにして回転速度を元へ戻すだけで、FOVは変更しない。 |
| `changeRotationSpeedValue(float newVerticalRotationValue, float newHorizontalRotationValue)` | 一人称か三人称かに応じて、縦横の回転速度を引数の値へ差し替える。 |
| `setOriginalRotationSpeed()` | 一人称と三人称の縦横回転速度を、保存済みの初期値へ戻す。 |
| `checkCurrentRotationSpeed()` | 現在の視点に合わせて縦横の`current`回転速度を選択して設定する。 |
| `setCameraState(string stateName)` | 名前一致の状態を`currentState`へ複製し、ズーム解除・乗員の一人称設定・HUD設定・状態変更イベント送出を行う。 |
| `setCheckCameraShakeActiveState(bool state)` | 揺れ許可フラグを設定し、シェイク管理の車両用状態を切り替え、無効化時は後退フラグを解除して停止する。 |
| `usingBoost(bool state, string shakeName, bool useBoostCameraShake, bool moveCameraAwayOnBoost)` | 揺れ許可時のみ`boosting`を立て、ブースト開始/終了に合わせてカメラ後退フラグと指定名のシェイクを切り替える。 |
| `setFirstPersonCameraState()` | 有効かつ一人称の最初のカメラ状態を、名前指定の状態設定で適用する。 |
| `setCameraStateByName(string cameraStateName)` | カメラが自由な時のみ、名前一致の状態を探して状態変更処理を呼び、見つからなければ何もしない。 |
| `changeCameraPositionByIndex(int newIndex)` | 範囲外なら0に丸めて`cameraStateIndex`を設定し、状態変更処理を呼ぶ。 |
| `changeCameraPosition()` | 自由カメラ時のみ次の有効な状態へインデックスを進め、状態変更処理を呼ぶ。 |
| `resetCameraRotation()` | ピボットとカメラのローカル回転を`Quaternion.identity`へ戻す。 |
| `resetAxisCameraRotationToVehicleForwardDirection()` | 車両前方とのY角度差を求め、その分だけ自身をY回転して向きを車両正面へ合わせる。 |
| `setDamageCameraShake()` | 一人称か三人称かと設定に応じて、ダメージ用の外部シェイクを`shakingManager`へ渡す。 |
| `setCameraExternalShake(externalShakeInfo externalShake)` | シェイク管理がある場合に、受け取った外部シェイク情報をそのまま渡す。 |
| `moveAwayCamera()` | 本体が空で何もしない。 |
| `getPlayer(GameObject playerElement)` | プレイヤーから`playerController`とカメラ管理・メインカメラを取得し、2.5D/自由カメラ状態も保持する。 |
| `getVehicleMainCameraTransform()` | 現在の状態の`cameraTransform`を返す。 |
| `getVehicleCameraControllerTransform()` | 自分自身の`transform`を返す。 |
| `changeCameraDrivingState(bool state, bool resetCameraRotationWhenGetOn)` | 運転状態を設定し、降車時はブースト/ズーム/FOV/ポーズを解除、乗車時はカメラ回転やFOVをリセットする。 |
| `updateTo2_5dor3dWorld(bool state)` | 2.5Dかどうかの3つのフラグを設定し、`hudManager`側のカメラ種別チェックを呼ぶ。 |
| `resetCameraTransformRotation()` | 自身の回転を`Quaternion.identity`へ戻し、`resetCameraRotation`も呼ぶ。 |
| `setCameraPosition(bool state)` | 乗車時用の状態名があればそれを適用し、なければ一人称/三人称を設定して武器管理へカメラ情報を渡す。 |
| `setFirstOrThirdPerson(bool state)` | 一人称または三人称に一致する最初の状態を探して`setCameraState`を呼び、インデックスも更新する。 |
| `adjustCameraToCurrentCollisionDistance()` | 一人称でなければ、衝突判定の更新を呼んで現在の衝突距離に合わせてカメラを配置する。 |
| `checkCameraCollision()` | ピボットから`SphereCastAll`して最近の非トリガー衝突点までの距離を求め、`SmoothDamp`した値を返す。 |
| `startOrStopFollowVehiclePosition(bool state)` | `followVehiclePosition`を設定するだけ。 |
| `pauseOrPlayVehicleCamera(bool state)` | `cameraPaused`を設定するだけ。 |
| `isVehicleCameraPaused()` | `cameraPaused`の値を返す。 |
| `isCameraTypeFree()` | `cameraTypeFree`の値を返す。 |
| `isPlayerMovingOn3dWorld()` | `playerMovingOn3dWorld`の値を返す。 |
| `getCurrentCameraPivot()` | 現在の状態の`pivotTransform`を返す。 |
| `getCurrentCameraTransform()` | 現在の状態の`cameraTransform`を返す。 |
| `getVehicleLookAngle()` | 現在の`lookAngle`（縦横の視点角度）を返す。 |
| `gameIsPaused()` | `actionManager`にゲームが一時停止中か問い合わせて返す。 |
| `setVehicleAndCameraParent(Transform newParent)` | 車両と自身の両方の親を、指定した`Transform`へ付け替える。 |
| `inputChangeCamera()` | 運転中かつゲームもカメラも非ポーズの時だけ、`changeCameraPosition`を呼ぶ。 |
| `inputZoom()` | 運転中かつゲームもカメラも非ポーズの時だけ、`setZoom`を現在のズーム状態の逆で呼ぶ。 |
| `inputTakeCapture()` | 運転中かつゲームもカメラも非ポーズの時だけ、`playerCameraManager.takeCapture`を呼ぶ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`getLockedCameraTransform()`, `getOriginalLockedCameraPivotPosition()`, `isFirstPersonActive()`, `isMoveInXAxisOn2_5d()`

</details>

## 内部型

- `vehicleCameraStateInfo`（class）
- `shakeSettingsInfo`（class）
