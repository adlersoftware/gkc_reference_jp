# playerCamera

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `cameraControllerManager`
- **ソース**: `Camera/Player Camera/playerCamera.cs:9`

**概要**: プレイヤーのカメラ全体を管理するコンポーネントで、三人称/一人称/フルボディアウェアネス(FBA)の視点切替、フリー/ロックオンカメラの状態、ピボットとメインカメラの位置・回転、頭ボブ、リーン、マウスホイールでの距離変更、シェイクやノイズなどを制御する。入力用ラッパーとエディタ用ヘルパーも多数持つ。

**公式ドキュメント抜粋**（[Player Camera](../../docs/player-controller-components/player-camera.md)）

> It contains the main camera used for the controller, including:

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Camera Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Camera Transform | `playerCameraTransform` | `Transform` | – | プレイヤー位置に追従するカメラ親`Transform`。 |
| Main Camera | `mainCamera` | `Camera` | – | 画角やクリップ面を制御する`Camera`本体。 |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | ピボットからの距離で位置が決まるカメラ`Transform`。 |
| Pivot Camera Transform | `pivotCameraTransform` | `Transform` | – | 上下回転を担うピボット`Transform`。 |
| Pivot Lean Transform | `pivotLeanTransform` | `Transform` | – | リーン時の傾きを加える親`Transform`。 |
| Pivot Lean Child Transform | `pivotLeanChildTransform` | `Transform` | – | リーン時にピボットをぶら下げる子`Transform`。 |
| Main Camera Parent | `mainCameraParent` | `Transform` | – | `mainCamera`を戻す際の親`Transform`。 |

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Rotation Input Enabled | `cameraRotationInputEnabled` | `bool` | true | 入力によるカメラ回転を許可するかの切替。 |
| Third Person Vertical Rotation Speed | `thirdPersonVerticalRotationSpeed` | `float` | 5 | 三人称視点での上下回転の感度。 |
| Third Person Horizontal Rotation Speed | `thirdPersonHorizontalRotationSpeed` | `float` | 5 | 三人称視点での左右回転の感度。 |
| First Person Vertical Rotation Speed | `firstPersonVerticalRotationSpeed` | `float` | 5 | 一人称視点での上下回転の感度。 |
| First Person Horizontal Rotation Speed | `firstPersonHorizontalRotationSpeed` | `float` | 5 | 一人称視点での左右回転の感度。 |
| Max Check Dist | `maxCheckDist` | `float` | 0.1f | カメラ衝突判定に使う`SphereCast`の半径。 |
| Smooth Between State | `smoothBetweenState` | `float` | – | カメラステート間を補間する速さ。 |
| Movement Lerp Speed | `movementLerpSpeed` | `float` | 5 | 非衝突時にカメラ位置を寄せる補間速度。 |
| Pivot Camera Movement Lerp Speed | `pivotCameraMovementLerpSpeed` | `float` | 5 | ピボットを目標位置へ寄せる補間速度。 |
| Extra Camera Collision Distance | `extraCameraCollisionDistance` | `float` | – | カメラ衝突判定に上乗せする距離。 |
| Camera Collision Always Active | `cameraCollisionAlwaysActive` | `bool` | true | 全ステートでカメラ衝突判定を常に行う切替。 |
| Use Pivot Camera Collision Enabled | `usePivotCameraCollisionEnabled` | `bool` | – | ピボット位置でも衝突判定するかの切替。 |
| Pivot Camera Collision Height Offset | `pivotCameraCollisionHeightOffset` | `float` | 0.7f | ピボット衝突判定を上へずらす高さ。 / 表示条件: `usePivotCameraCollisionEnabled` がオンのとき |
| Default Near Clip Plane | `defaultNearClipPlane` | `float` | 0.02f | 既定値として復帰させる`nearClipPlane`。 |
| Ignore External Fov Changes Enabled | `ignoreExternalFovChangesEnabled` | `bool` | – | 外部からのFOV変更を無視するかの切替。 |

### Full Body Awareness Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Full Body Awareness Enabled | `fullBodyAwarenessEnabled` | `bool` | – | 全身表示（FBA）カメラを有効にする切替。 |

### Change View Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Camera View Enabled | `changeCameraViewEnabled` | `bool` | true | 視点切替の入力を受け付けるかの切替。 |
| Aim Side | `aimSide` | `sideToAim` | – | 三人称で構えるときの左右の構え側。 |
| Change Camera Side Active | `changeCameraSideActive` | `bool` | true | 視点切替時に構え側も入れ替えるかの切替。 |
| Toogle Camera View To Third First And Locked Enabled | `toogleCameraViewToThirdFirstAndLockedEnabled` | `bool` | true | 固定カメラも含めて視点を巡回させるかの切替。 |

### Camera Bullet Time Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Regular Movement On Bullet Time | `regularMovementOnBulletTime` | `bool` | – | バレットタイム中も通常速度で動かすかの切替。 |
| Use Unscaled Time On Bullet Time | `useUnscaledTimeOnBulletTime` | `bool` | – | バレットタイム中に非スケール時間を使う切替。 |

### Follow Position Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Smooth Camera Follow | `useSmoothCameraFollow` | `bool` | – | `SmoothDamp`で位置を滑らかに追従させる切替。 |
| Smooth Camera Follow Speed | `smoothCameraFollowSpeed` | `float` | – | 追従の滑らかさ。小さいほど機敏に動く。 / 表示条件: `useSmoothCameraFollow` がオンのとき |
| Smooth Camera Follow Speed On Aim | `smoothCameraFollowSpeedOnAim` | `float` | – | エイム中の追従の滑らかさ（SmoothDamp）。 / 表示条件: `useSmoothCameraFollow` がオンのとき |
| Smooth Camera Follow Max Distance | `smoothCameraFollowMaxDistance` | `float` | – | この距離を超えると追従速度を変える閾値。 / 表示条件: `useSmoothCameraFollow` がオンのとき |
| Smooth Camera Follow Max Distance Speed | `smoothCameraFollowMaxDistanceSpeed` | `float` | – | 閾値超過時に速度へ掛ける倍率。 / 表示条件: `useSmoothCameraFollow` がオンのとき |
| Smooth Return Speed | `smoothReturnSpeed` | `float` | 1 | 元の追従位置へ戻るときの速さ。 |
| Check Camera Distance On Smooth Return Enabled | `checkCameraDistanceOnSmoothReturnEnabled` | `bool` | true | 復帰時に距離に応じて速度を上げるかの切替。 |
| Smooth Go Speed | `smoothGoSpeed` | `float` | 1 | 死亡時にラグドールへ寄る速さ。 |
| Check Camera Distance On Smooth Go Enabled | `checkCameraDistanceOnSmoothGoEnabled` | `bool` | true | ラグドール追従で距離に応じ加速するかの切替。 |

### Smooth Camera Rotation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Smooth Camera Rotation | `useSmoothCameraRotation` | `bool` | – | カメラ回転を補間して滑らかにするかの切替。 |
| Use Smooth Camera Rotation Third Person | `useSmoothCameraRotationThirdPerson` | `bool` | – | 三人称で回転補間を適用するかの切替。 / 表示条件: `useSmoothCameraRotation` がオンのとき |
| Smooth Camera Rotation Speed Vertical Third Person | `smoothCameraRotationSpeedVerticalThirdPerson` | `float` | 10 | 三人称での上下回転補間の速さ。 / 表示条件: `useSmoothCameraRotation.boolValue && useSmoothCameraRotationThirdPerson.boolValue` |
| Smooth Camera Rotation Speed Horizontal Third Person | `smoothCameraRotationSpeedHorizontalThirdPerson` | `float` | 10 | 三人称での左右回転補間の速さ。 / 表示条件: `useSmoothCameraRotation.boolValue && useSmoothCameraRotationThirdPerson.boolValue` |
| Use Smooth Camera Rotation First Person | `useSmoothCameraRotationFirstPerson` | `bool` | – | 一人称で回転補間を適用するかの切替。 / 表示条件: `useSmoothCameraRotation` がオンのとき |
| Smooth Camera Rotation Speed Vertical First Person | `smoothCameraRotationSpeedVerticalFirstPerson` | `float` | 10 | 一人称での上下回転補間の速さ。 / 表示条件: `useSmoothCameraRotation.boolValue && useSmoothCameraRotationFirstPerson.boolValue` |
| Smooth Camera Rotation Speed Horizontal First Person | `smoothCameraRotationSpeedHorizontalFirstPerson` | `float` | 10 | 一人称での左右回転補間の速さ。 / 表示条件: `useSmoothCameraRotation.boolValue && useSmoothCameraRotationFirstPerson.boolValue` |

### Zoom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Zoom Speed | `zoomSpeed` | `float` | 120 | ズーム時にFOVを変更する速さ。 |
| Fov Change Speed | `fovChangeSpeed` | `float` | – | 通常時や着地時のFOV変更の速さ。 |
| Third Person Vertical Rotation Speed Zoom In | `thirdPersonVerticalRotationSpeedZoomIn` | `float` | 2.5f | ズーム中の三人称の上下回転感度。 |
| Third Person Horizontal Rotation Speed Zoom In | `thirdPersonHorizontalRotationSpeedZoomIn` | `float` | 2.5f | ズーム中の三人称の左右回転感度。 |
| First Person Vertical Rotation Speed Zoom In | `firstPersonVerticalRotationSpeedZoomIn` | `float` | 2.5f | ズーム中の一人称の上下回転感度。 |
| First Person Horizontal Rotation Speed Zoom In | `firstPersonHorizontalRotationSpeedZoomIn` | `float` | 2.5f | ズーム中の一人称の左右回転感度。 |

### Mouse Wheel Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Move Camera Position With Mouse Wheel Active | `moveCameraPositionWithMouseWheelActive` | `bool` | – | ホイールでカメラ距離を変えられるようにする切替。 |
| Move Camera Position Forward With Mouse Wheel Speed | `moveCameraPositionForwardWithMouseWheelSpeed` | `float` | 0.3f | ホイール1回で手前へ寄せる量。 / 表示条件: `moveCameraPositionWithMouseWheelActive` がオンのとき |
| Move Camera Position Backward With Mouse Wheel Speed | `moveCameraPositionBackwardWithMouseWheelSpeed` | `float` | 0.3f | ホイール1回でカメラを奥へ離す量。 / 表示条件: `moveCameraPositionWithMouseWheelActive` がオンのとき |
| Reverse Mouse Wheel Direction Enabled | `reverseMouseWheelDirectionEnabled` | `bool` | – | ホイールの寄る・離れる方向を反転する切替。 / 表示条件: `moveCameraPositionWithMouseWheelActive` がオンのとき |
| Max Extra Distance On Third Person | `maxExtraDistanceOnThirdPerson` | `float` | 1 | 三人称で基準位置から離せる最大距離。 / 表示条件: `moveCameraPositionWithMouseWheelActive` がオンのとき |
| Use Camera Mouse Wheel States | `useCameraMouseWheelStates` | `bool` | – | 距離に応じてカメラステートを自動切替するか。 / 表示条件: `moveCameraPositionWithMouseWheelActive` がオンのとき |

### Mouse Wheel Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Min Distance To Change To First Person | `minDistanceToChangeToFirstPerson` | `float` | 0.1f | 一人称へ切り替わる距離の閾値。 / 表示条件: `moveCameraPositionWithMouseWheelActive` がオンのとき |

### 2.5d Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Camera Limit | `useCameraLimit` | `bool` | – | 固定カメラの移動を上下左右の範囲内に制限する切替。 / 表示条件: `using2_5ViewActive.boolValue \|\| cameraType.enumValueIndex == 1` |
| Use Width Limit | `useWidthLimit` | `bool` | – | 幅方向の制限を適用するかの切替。 / 表示条件: `using2_5ViewActive.boolValue \|\| cameraType.enumValueIndex == 1 && useCameraLimit.boolValue` |
| Width Limit Right | `widthLimitRight` | `float` | – | 制限基準位置から右へ許す幅の広さ。 / 表示条件: `useCameraLimit.boolValue && useWidthLimit.boolValue` |
| Width Limit Left | `widthLimitLeft` | `float` | – | 制限基準位置から左へ許す幅の広さ。 / 表示条件: `useCameraLimit.boolValue && useWidthLimit.boolValue` |
| Use Height Limit | `useHeightLimit` | `bool` | – | 高さ方向の制限を適用するかの切替。 / 表示条件: `using2_5ViewActive.boolValue \|\| cameraType.enumValueIndex == 1 && useCameraLimit.boolValue` |
| Height Limit Upper | `heightLimitUpper` | `float` | – | 制限基準位置から上へ許す高さ。 / 表示条件: `useCameraLimit.boolValue && useHeightLimit.boolValue` |
| Height Limit Lower | `heightLimitLower` | `float` | – | 制限基準位置から下へ許す高さ。 / 表示条件: `useCameraLimit.boolValue && useHeightLimit.boolValue` |
| Use Depth Limit | `useDepthLimit` | `bool` | – | 奥行き方向の制限を適用するかの切替。 / 表示条件: `using2_5ViewActive.boolValue \|\| cameraType.enumValueIndex == 1 && useCameraLimit.boolValue` |
| Depth Limit Front | `depthLimitFront` | `float` | – | 制限基準位置から前へ許す距離。 / 表示条件: `useCameraLimit.boolValue && useDepthLimit.boolValue` |
| Depth Limit Backward | `depthLimitBackward` | `float` | – | 制限基準位置から後ろへ許す距離。 / 表示条件: `useCameraLimit.boolValue && useDepthLimit.boolValue` |
| Current Camera Limit Position | `currentCameraLimitPosition` | `Vector3` | – | 各制限を測る基準となる中心位置。 / 表示条件: `using2_5ViewActive.boolValue \|\| cameraType.enumValueIndex == 1 && useCameraLimit.boolValue` |
| Clamp Aim Directions | `clampAimDirections` | `bool` | – | 2.5Dで狙い方向を決められた向きに制限する切替。 / 表示条件: `using2_5ViewActive.boolValue \|\| cameraType.enumValueIndex == 1` |
| Number Of Aim Directions | `numberOfAimDirections` | `int` | 8 | 狙い方向を制限するときの方向数（8/4/2）。 / 表示条件: `using2_5ViewActive.boolValue \|\| cameraType.enumValueIndex == 1` |
| Min Distance To Center Clamp Aim | `minDistanceToCenterClampAim` | `float` | 1.2f | 中央付近では制限を緩める距離の閾値。 / 表示条件: `using2_5ViewActive.boolValue \|\| cameraType.enumValueIndex == 1` |

### Zero Gravity Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Rotate Forward On Zero Gravity Mode On | `canRotateForwardOnZeroGravityModeOn` | `bool` | – | 無重力中にカメラを前方へ回せるようにする切替。 |
| Rotate Forward On Zero Gravity Speed | `rotateForwardOnZeroGravitySpeed` | `float` | – | 無重力時に前方回転させる速さ。 |

### Reset Camera Rotation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Reset Camera Rotation After Time | `resetCameraRotationAfterTime` | `bool` | – | 無操作時間後に視点を戻すかの切替。 |
| Time To Reset Camera Rotation | `timeToResetCameraRotation` | `float` | – | 視点を戻し始めるまでの待ち秒数。 / 表示条件: `resetCameraRotationAfterTime` がオンのとき |
| Reset Camera Rotation Speed | `resetCameraRotationSpeed` | `float` | – | 視点をプレイヤー方向へ戻す速さ。 |

### Set Extra Camera Rotation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Extra Camera Rotation Enabled | `setExtraCameraRotationEnabled` | `bool` | true | 追加のカメラ回転アクションを有効にする切替。 |
| Extra Camera Rotation Amount | `extraCameraRotationAmount` | `float` | 180 | 追加回転アクションで回す角度（度）。 / 表示条件: `setExtraCameraRotationEnabled` がオンのとき |
| Extra Camera Rotation Speed | `extraCameraRotationSpeed` | `float` | 3 | 追加回転を完了させるまでの速さ。 / 表示条件: `setExtraCameraRotationEnabled` がオンのとき |
| Use Camera Forward Direction | `useCameraForwardDirection` | `bool` | true | 追加回転の基準をカメラ前方にするかの切替。 / 表示条件: `setExtraCameraRotationEnabled` がオンのとき |

### Player Camera States

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current State Name | `currentStateName` | `string` | – | 現在適用中のカメラステート名。 |
| Default Third Person State Name | `defaultThirdPersonStateName` | `string` | "Third Person" | 三人称へ切り替えるときに使うステート名。 |
| Default First Person State Name | `defaultFirstPersonStateName` | `string` | "First Person" | 一人称へ切り替えるときに使うステート名。 |
| Default Full Body Awareness State Name | `defaultFullBodyAwarenessStateName` | `string` | "Full Body Awareness" | FBAを有効にしたときに使うステート名。 |
| Default Full Body Awareness Crouch State Name | `defaultFullBodyAwarenessCrouchStateName` | `string` | "Full Body Awareness Crouch" | FBAでしゃがみ時に使うステート名。 |
| Default Full Body Awareness Aim State Name | `defaultFullBodyAwarenessAimStateName` | `string` | "Full Body Awareness Aim" | FBAでエイム時に使うステート名。 |
| Default Full Body Awareness Crouch Aim State Name | `defaultFullBodyAwarenessCrouchAimStateName` | `string` | "Full Body Awareness Crouch Aim" | FBAでしゃがみエイム時のステート名。 |
| Default Full Body Awareness Dual Aim State Name | `defaultFullBodyAwarenessDualAimStateName` | `string` | "Full Body Awareness Dual Aim" | FBAで二丁持ちエイム時のステート名。 |
| Default Full Body Awareness Crouch Dual Aim State Name | `defaultFullBodyAwarenessCrouchDualAimStateName` | `string` | "Full Body Awareness Crouch Dual Aim" | FBAでしゃがみ二丁エイム時のステート名。 |
| Default Third Person Aim Right State Name | `defaultThirdPersonAimRightStateName` | `string` | "Aim Right" | 三人称で右構えエイム時のステート名。 |
| Default Third Person Aim Left State Name | `defaultThirdPersonAimLeftStateName` | `string` | "Aim Left" | 三人称で左構えエイム時のステート名。 |
| Default Third Person Aim Right Crouch State Name | `defaultThirdPersonAimRightCrouchStateName` | `string` | "Aim Right Crouch" | 三人称の右構えしゃがみエイム時のステート名。 |
| Default Third Person Aim Left Crouch State Name | `defaultThirdPersonAimLeftCrouchStateName` | `string` | "Aim Left Crouch" | 三人称の左構えしゃがみエイム時のステート名。 |
| Default Third Person Crouch State Name | `defaultThirdPersonCrouchStateName` | `string` | "Third Person Crouch" | 三人称でしゃがみ時に使うステート名。 |
| Default First Person Crouch State Name | `defaultFirstPersonCrouchStateName` | `string` | "First Person Crouch" | 一人称でしゃがみ時に使うステート名。 |
| Default Move Camera Away State Name | `defaultMoveCameraAwayStateName` | `string` | "Move Away" | カメラを引くアクション時のステート名。 |
| Default Locked Camera State Name | `defaultLockedCameraStateName` | `string` | "Locked Camera" | 固定カメラにしたときに使うステート名。 |
| Default AI Camera State Name | `defaultAICameraStateName` | `string` | "AI Camera" | AI用カメラで使うステート名。 |
| Default Vehicle Passenger State Name | `defaultVehiclePassengerStateName` | `string` | "Vehicle Passenger" | 乗り物の同乗者時に使うステート名。 |

### Player Camera States Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Camera State Change | `useEventsOnCameraStateChange` | `bool` | – | ステート変更時に登録イベントを発火するかの切替。 |

### Locked Camera Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Locked Camera System Prefab | `lockedCameraSystemPrefab` | `GameObject` | – | 新規固定カメラを配置するときに複製するプレハブ。 |
| Locked Camera Limit System Prefab | `lockedCameraLimitSystemPrefab` | `GameObject` | – | 固定カメラの制限システム用プレハブ。 |

### AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Used By AI | `usedByAI` | `bool` | – | AI操作時にプレイヤー向け処理を止めるフラグ。 |

### 2.5d Locked Settings On AI

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Custom Original Locked Camera Pivot Position | `customOriginalLockedCameraPivotPosition` | `Vector3` | – | AI時の2.5D固定カメラの基準ピボット位置。 / 表示条件: `usedByAI` がオンのとき |
| Use Custom Original Locked Camera Pivot Position Transform | `useCustomOriginalLockedCameraPivotPositionTransform` | `bool` | – | 基準ピボット位置を`Transform`から取るかの切替。 / 表示条件: `usedByAI` がオンのとき |
| Custom Original Locked Camera Pivot Position Transform | `customOriginalLockedCameraPivotPositionTransform` | `Transform` | – | 基準ピボット位置として使う`Transform`参照。 / 表示条件: `usedByAI.boolValue && useCustomOriginalLockedCameraPivotPositionTransform.boolValue` |

### Locked Camera Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Locked Camera Elements Parent | `lockedCameraElementsParent` | `Transform` | – | 固定カメラ用オブジェクト群の親`Transform`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Locked Main Camera Transform | `lockedMainCameraTransform` | `Transform` | – | 固定カメラの回転基準となる`Transform`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Locked Camera Axis | `lockedCameraAxis` | `Transform` | – | 固定カメラの向きの基準となる軸`Transform`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Locked Camera Position | `lockedCameraPosition` | `Transform` | – | 固定カメラの注視位置を表す`Transform`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Locked Camera Pivot | `lockedCameraPivot` | `Transform` | – | 固定カメラのピボット`Transform`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Look Camera Parent | `lookCameraParent` | `Transform` | – | 狙い方向の計算に使う親`Transform`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Look Camera Pivot | `lookCameraPivot` | `Transform` | – | 狙い方向の計算に使うピボット`Transform`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Look Camera Direction | `lookCameraDirection` | `Transform` | – | 狙い方向の基準位置を持つ`Transform`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Clamp Aim Direction Transform | `clampAimDirectionTransform` | `Transform` | – | 狙い方向を制限するときに使う`Transform`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Look Direction Transform | `lookDirectionTransform` | `Transform` | – | 実際の視線方向を表す`Transform`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Aux Locked Camera Axis | `auxLockedCameraAxis` | `Transform` | – | 固定カメラ軸の位置保持に使う補助`Transform`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Set Transparent Surfaces Manager | `setTransparentSurfacesManager` | `setTransparentSurfaces` | – | 固定カメラ時に透明化する`setTransparentSurfaces`参照。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |

### Player Camera Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Game Object | `playerControllerGameObject` | `GameObject` | – | プレイヤー本体のGameObject参照。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Player Input | `playerInput` | `playerInputManager` | – | 入力状態を参照する`playerInputManager`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | 移動状態を参照する`playerController`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Powers Manager | `powersManager` | `otherPowers` | – | 構え側の切替などで参照する`otherPowers`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Gravity Manager | `gravityManager` | `gravitySystem` | – | 重力状態を参照する`gravitySystem`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Head Bob Manager | `headBobManager` | `headBob` | – | カメラ揺れを委ねる`headBob`参照。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Grab Objects Manager | `grabObjectsManager` | `grabObjects` | – | 物を持つ動作を参照する`grabObjects`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Scanner Manager | `scannerManager` | `scannerSystem` | – | スキャナ状態を参照する`scannerSystem`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | 武器のFOVやエイムを参照する`playerWeaponsManager`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Player Nav Mesh Manager | `playerNavMeshManager` | `playerNavMeshSystem` | – | AI移動を参照する`playerNavMeshSystem`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Character State Icon Manager | `characterStateIconManager` | `characterStateIconSystem` | – | 状態アイコンを参照する`characterStateIconSystem`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Main Collider | `mainCollider` | `Collider` | – | 追従範囲の計算に使うプレイヤーの`Collider`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Main Camera Capture System | `mainCameraCaptureSystem` | `cameraCaptureSystem` | – | カメラ撮影を行う`cameraCaptureSystem`参照。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Target To Follow | `targetToFollow` | `Transform` | – | カメラが位置を追う対象`Transform`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Hips Transform | `hipsTransform` | `Transform` | – | 死亡時などに追う腰の`Transform`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |

### Use Camera Reticle Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Update Reticle Active State | `updateReticleActiveState` | `bool` | – | 視点に応じてレティクル表示を更新するかの切替。 / 表示条件: `showSettings` がオンのとき |
| Use Camera Reticle Third Person | `useCameraReticleThirdPerson` | `bool` | – | 三人称でもレティクルを出すかの切替。 / 表示条件: `showSettings.boolValue && updateReticleActiveState.boolValue` |
| Use Camera Reticle First Person | `useCameraReticleFirstPerson` | `bool` | – | 一人称でレティクルを出すかの切替。 / 表示条件: `showSettings.boolValue && updateReticleActiveState.boolValue` |
| Camera Reticle Game Object | `cameraReticleGameObject` | `GameObject` | – | 表示を切り替えるレティクルのGameObject。 / 表示条件: `showSettings.boolValue && updateReticleActiveState.boolValue` |
| Main Camera Reticle Game Object | `mainCameraReticleGameObject` | `GameObject` | – | 常時表示側のメインレティクル。 / 表示条件: `showSettings.boolValue && updateReticleActiveState.boolValue` |

### Use Camera Reticle Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Custom Reticle Parent | `mainCustomReticleParent` | `RectTransform` | – | カスタムレティクルを配置する親`RectTransform`。 / 表示条件: `showSettings` がオンのとき |

### Adjust Camera To Previous Character View Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Adjust Camera To Previous Character Direction Active | `adjustCameraToPreviousCharacterDirectionActive` | `bool` | – | キャラ切替時に前キャラの向きへ合わせるかの切替。 / 表示条件: `showSettings` がオンのとき |
| Use Smooth Camera Transition Between Characters | `useSmoothCameraTransitionBetweenCharacters` | `bool` | – | キャラ切替時のカメラ移動を補間するかの切替。 / 表示条件: `showSettings` がオンのとき |
| Smooth Camera Transition Between Characters Speed | `smoothCameraTransitionBetweenCharactersSpeed` | `float` | – | キャラ切替時のカメラ移動速度。 / 表示条件: `showSettings` がオンのとき |
| Set New Character Always In Previous Character View | `setNewCharacterAlwaysInPreviousCharacterView` | `bool` | – | 新キャラを前キャラと同じ視点で始めるかの切替。 / 表示条件: `showSettings` がオンのとき |
| Set New Character Always In Third Person | `setNewCharacterAlwaysInThirdPerson` | `bool` | – | 新キャラを常に三人称で始めるかの切替。 / 表示条件: `showSettings.boolValue && !setNewCharacterAlwaysInPreviousCharacterView.boolValue` |
| Set New Character Always In First Person | `setNewCharacterAlwaysInFirstPerson` | `bool` | – | 新キャラを常に一人称で始めるかの切替。 / 表示条件: `showSettings.boolValue && !setNewCharacterAlwaysInPreviousCharacterView.boolValue` |

### Local Multiplayer Single Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Multiple Target Fov | `useMultipleTargetFov` | `bool` | – | 複数ターゲットを収めるためFOVを自動調整するかの切替。 / 表示条件: `showSettings` がオンのとき |
| Multiple Targets Min Fov | `multipleTargetsMinFov` | `float` | 20 | 自動調整するときのFOVの下限値。 / 表示条件: `showSettings.boolValue && useMultipleTargetFov.boolValue` |
| Multiple Targets Max Fov | `multipleTargetsMaxFov` | `float` | 70 | 自動調整するときのFOVの上限値。 / 表示条件: `showSettings.boolValue && useMultipleTargetFov.boolValue` |
| Multiple Targets Fov Speed | `multipleTargetsFovSpeed` | `float` | 40 | FOV自動調整の反応の速さの目安。 / 表示条件: `showSettings.boolValue && useMultipleTargetFov.boolValue` |
| Use Multiple Targets Y Position | `useMultipleTargetsYPosition` | `bool` | – | 複数ターゲット時にカメラ高さも自動調整するかの切替。 / 表示条件: `showSettings` がオンのとき |
| Multiple Targets Y Position Speed | `multipleTargetsYPositionSpeed` | `float` | – | 複数ターゲット時の高さ補間速度。 / 表示条件: `showSettings.boolValue && useMultipleTargetsYPosition.boolValue` |
| Multiple Targets Max Height | `multipleTargetsMaxHeight` | `float` | 30 | 高さ自動調整で加える最大の高さ。 / 表示条件: `showSettings.boolValue && useMultipleTargetsYPosition.boolValue` |
| Multiple Targets Height Multiplier | `multipleTargetsHeightMultiplier` | `float` | 0.5f | ターゲット範囲の広がりに掛ける高さ倍率。 / 表示条件: `showSettings.boolValue && useMultipleTargetsYPosition.boolValue` |
| Max Multiple Target Height | `maxMultipleTargetHeight` | `float` | 30 | 自動調整するカメラ高さの上限。 / 表示条件: `showSettings.boolValue && useMultipleTargetsYPosition.boolValue` |
| Min Multiple Target Height | `minMultipleTargetHeight` | `float` | -1 | 自動調整するカメラ高さの下限。 / 表示条件: `showSettings.boolValue && useMultipleTargetsYPosition.boolValue` |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | デバッグ用ログを出力するかの切替。 / 表示条件: `showSettings` がオンのとき |

### Look At Target Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Look At Target Enabled | `lookAtTargetEnabled` | `bool` | – | 対象を自動で見る（ロックオン）機能の有効切替。 / 表示条件: `showLookTargetSettings` がオンのとき |

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Activate Look At Target Enabled | `canActivateLookAtTargetEnabled` | `bool` | true | オンでプレイヤー入力による対象の注視を許可する。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Can Active Look At Target On Locked Camera | `canActiveLookAtTargetOnLockedCamera` | `bool` | – | ロックオンカメラ中でも手動で対象を注視できるようにする。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Look At Target Transform | `lookAtTargetTransform` | `Transform` | – | 注視方向の計算に使う補助`Transform`（通常は自動生成）。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Target To Look | `targetToLook` | `Transform` | – | 現在注視中の対象。通常はスクリプトが自動設定する。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Max Distance To Find Target | `maxDistanceToFindTarget` | `float` | – | カメラからこの距離内のオブジェクトを注視候補として検索する。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Use Layer To Search Targets | `useLayerToSearchTargets` | `bool` | – | 候補検索をタグではなく`layerToLook`のレイヤーで行う。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Layer To Look | `layerToLook` | `LayerMask` | – | 注視候補の検索と障害物判定に使うレイヤー。 / 表示条件: `lookAtTargetEnabled.boolValue && useLayerToSearchTargets.boolValue` |
| Look Only If Target On Screen | `lookOnlyIfTargetOnScreen` | `bool` | – | 画面内に映っている対象だけを注視候補にする。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Check Obstacles To Target | `checkObstaclesToTarget` | `bool` | – | 注視対象までの間に障害物がある候補を除外する。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Get Closest To Camera Center | `getClosestToCameraCenter` | `bool` | – | 画面中心に近い対象を選ぶか、プレイヤーに近い対象を選ぶか。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Use Max Distance To Camera Center | `useMaxDistanceToCameraCenter` | `bool` | – | 画面中心からの距離が上限を超える対象を除外する。 / 表示条件: `lookAtTargetEnabled.boolValue && getClosestToCameraCenter.boolValue` |
| Max Distance To Camera Center | `maxDistanceToCameraCenter` | `float` | – | 画面中心からこの距離（ピクセル）以内の対象だけを候補にする。 / 表示条件: `getClosestToCameraCenter.boolValue && useMaxDistanceToCameraCenter.boolValue` |
| Activate Strafe Mode If No Targets To Look Found | `activateStrafeModeIfNoTargetsToLookFound` | `bool` | – | 対象が見つからない時にストレイフモードへ切り替える。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Layer To Check Possible Targets Below Cursor | `layerToCheckPossibleTargetsBelowCursor` | `LayerMask` | – | ロックオンカメラでカーソル下の対象を探すレイヤー。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |

### Search Point To Look Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Search Point To Look Components | `searchPointToLookComponents` | `bool` | – | `pointToLook`コンポーネントのポイントも注視候補に含める。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Point To Look Components Layer | `pointToLookComponentsLayer` | `LayerMask` | – | `pointToLook`を検索するレイヤー。 / 表示条件: `lookAtTargetEnabled.boolValue && searchPointToLookComponents.boolValue` |

### Stop Look At Target Aim Assist Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Time To Stop Aim Assist | `useTimeToStopAimAssist` | `bool` | – | 自動エイムアシストを一定時間で解除する機能を有効にする。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Time To Stop Aim Assist | `timeToStopAimAssist` | `float` | – | エイムアシストが自動で解除されるまでの秒数。 / 表示条件: `lookAtTargetEnabled.boolValue && useTimeToStopAimAssist.boolValue` |
| Use Time To Stop Aim Assist Locked Camera | `useTimeToStopAimAssistLockedCamera` | `bool` | – | ロックオンカメラの注視を一定時間で解除する機能を有効にする。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Time To Stop Aim Assist Locked Camera | `timeToStopAimAssistLockedCamera` | `float` | – | ロックオンカメラで注視が解除されるまでの秒数。 / 表示条件: `lookAtTargetEnabled.boolValue && useTimeToStopAimAssistLockedCamera.boolValue` |

### Change Between Target Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Change Target To Look With Camera Axis | `canChangeTargetToLookWithCameraAxis` | `bool` | – | カメラ操作で注視対象を切り替えられるようにする。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Minimum Camera Drag To Change Target To Look | `minimumCameraDragToChangeTargetToLook` | `float` | 1 | 対象切り替えと判定するカメラ入力の最小値。 / 表示条件: `lookAtTargetEnabled.boolValue && canChangeTargetToLookWithCameraAxis.boolValue` |
| Wait Time To Next Change Target To Look | `waitTimeToNextChangeTargetToLook` | `float` | 0.5f | 続けて対象を切り替えないための待ち時間（秒）。 / 表示条件: `lookAtTargetEnabled.boolValue && canChangeTargetToLookWithCameraAxis.boolValue` |
| Use Only Horizontal Camera Drag Value | `useOnlyHorizontalCameraDragValue` | `bool` | – | 切り替え時にカメラの横方向の入力だけを考慮する。 / 表示条件: `lookAtTargetEnabled.boolValue && canChangeTargetToLookWithCameraAxis.boolValue` |

### Look At Target Speed Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Look At Target Speed | `lookAtTargetSpeed` | `float` | – | 注視対象へカメラを向ける速度の倍率。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Look Closer At Target Speed | `lookCloserAtTargetSpeed` | `float` | 3 | 対象の方向とほぼ一致した後の微調整用の速度。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Look At Target Speed2 5d View | `lookAtTargetSpeed2_5dView` | `float` | 5 | 2.5Dビューで注視対象へ向く速度。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Look At Target Speed Others Locked Views | `lookAtTargetSpeedOthersLockedViews` | `float` | 5 | 固定カメラ視点で注視対象へ向く速度。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |

### Icon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Look Target Icon | `useLookTargetIcon` | `bool` | – | 注視中に画面上へアイコンを表示する。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Look At Target Icon | `lookAtTargetIcon` | `GameObject` | – | 注視中に画面へ表示するアイコンの`GameObject`。 / 表示条件: `lookAtTargetEnabled.boolValue && useLookTargetIcon.boolValue` |
| Look At Target Regular Icon Game Object | `lookAtTargetRegularIconGameObject` | `GameObject` | – | 通常の照準アイコン。非エイム用アイコン表示時は非表示になる。 / 表示条件: `lookAtTargetEnabled.boolValue && useLookTargetIcon.boolValue` |
| Look At Target Icon When Not Aiming | `lookAtTargetIconWhenNotAiming` | `GameObject` | – | 非エイム時のカーソル表示に切り替えるアイコン。 / 表示条件: `lookAtTargetEnabled.boolValue && useLookTargetIcon.boolValue` |

### Look At Characters Body Parts Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Look At Body Parts On Characters | `lookAtBodyPartsOnCharacters` | `bool` | – | キャラクターの弱点部位を狙って注視する。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |

### Look At Characters Body Parts Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Object To Grab Found Shader | `useObjectToGrabFoundShader` | `bool` | – | 注視対象にアウトラインシェーダーを適用する。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Object To Grab Found Shader | `objectToGrabFoundShader` | `Shader` | – | 注視対象の輪郭表示に使うシェーダー。 / 表示条件: `lookAtTargetEnabled.boolValue && useObjectToGrabFoundShader.boolValue` |
| Shader Outline Width | `shaderOutlineWidth` | `float` | – | 輪郭シェーダーで描く線の太さ。 / 表示条件: `lookAtTargetEnabled.boolValue && useObjectToGrabFoundShader.boolValue` |
| Shader Outline Color | `shaderOutlineColor` | `Color` | – | 輪郭シェーダーで描く線の色を指定する。 / 表示条件: `lookAtTargetEnabled.boolValue && useObjectToGrabFoundShader.boolValue` |

### Remote Events On Lock On Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Events On Lock On | `useRemoteEventsOnLockOn` | `bool` | – | 対象の`remoteEventSystem`へロックオン開始と終了を通知する。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |

### Events On Lock On Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Lock On | `useEventsOnLockOn` | `bool` | – | ロックオン開始・終了時にイベントを実行する。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Event On Lock On Start | `eventOnLockOnStart` | `UnityEvent` | – | ロックオン開始時に実行する処理。 / 表示条件: `lookAtTargetEnabled.boolValue && useEventsOnLockOn.boolValue` |
| Event On Lock On End | `eventOnLockOnEnd` | `UnityEvent` | – | ロックオン終了時に実行する処理。 / 表示条件: `lookAtTargetEnabled.boolValue && useEventsOnLockOn.boolValue` |
| Use Events On Lock At Target | `useEventsOnLockAtTarget` | `bool` | – | 対象を注視している間の開始・終了イベントを有効にする。 / 表示条件: `showLookTargetSettings.boolValue && lookAtTargetEnabled.boolValue` |
| Event On Lock At Target Start | `eventOnLockAtTargetStart` | `UnityEvent` | – | 対象の注視を開始した時に実行する処理。 / 表示条件: `lookAtTargetEnabled.boolValue && useEventsOnLockAtTarget.boolValue` |
| Event On Lock At Target End | `eventOnLockAtTargetEnd` | `UnityEvent` | – | 対象の注視を終了した時に実行する処理。 / 表示条件: `lookAtTargetEnabled.boolValue && useEventsOnLockAtTarget.boolValue` |

### Event On Moving Locked Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Moving Locked Camera | `useEventOnMovingLockedCamera` | `bool` | – | ロックオンカメラの移動に関するイベントを有効にする。 / 表示条件: `showEventSettings` がオンのとき |
| Use Event On Free Camere Too | `useEventOnFreeCamereToo` | `bool` | – | フリーカメラの移動時にも同じイベントを実行する。 / 表示条件: `showEventSettings` がオンのとき |
| Event On Start Moving Locked Camera | `eventOnStartMovingLockedCamera` | `UnityEvent` | – | カメラ移動を開始した時に実行する処理。 / 表示条件: `showEventSettings.boolValue && useEventOnMovingLockedCamera.boolValue \|\| useEventOnFreeCamera.boolValue` |
| Event On Keep Moving Locked Camera | `eventOnKeepMovingLockedCamera` | `UnityEvent` | – | カメラ移動中に毎回実行する処理。 / 表示条件: `showEventSettings.boolValue && useEventOnMovingLockedCamera.boolValue \|\| useEventOnFreeCamera.boolValue` |
| Event On Stop Moving Locked Camera | `eventOnStopMovingLockedCamera` | `UnityEvent` | – | カメラ移動を停止した時に実行する処理。 / 表示条件: `showEventSettings.boolValue && useEventOnMovingLockedCamera.boolValue \|\| useEventOnFreeCamera.boolValue` |

### Event On Third/First Person View Change Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Third First Person View Change | `useEventOnThirdFirstPersonViewChange` | `bool` | – | 三人称と一人称の切り替え時のイベントを有効にする。 / 表示条件: `showEventSettings` がオンのとき |
| Set First Person Event | `setFirstPersonEvent` | `UnityEvent` | – | 一人称視点に切り替えた時に実行する処理。 / 表示条件: `showEventSettings.boolValue && useEventOnThirdFirstPersonViewChange.boolValue` |
| Set Third Person Event | `setThirdPersonEvent` | `UnityEvent` | – | 三人称視点に切り替えた時に実行する処理。 / 表示条件: `showEventSettings.boolValue && useEventOnThirdFirstPersonViewChange.boolValue` |

### Event On FBA Person View Change Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On FBA View Change | `useEventOnFBAViewChange` | `bool` | – | FBAの有効・無効切り替え時のイベントを有効にする。 / 表示条件: `showEventSettings` がオンのとき |
| Event On Enable FBA | `eventOnEnableFBA` | `UnityEvent` | – | 実行中にFBAを有効にした時に実行する処理。 / 表示条件: `showEventSettings.boolValue && useEventOnFBAViewChange.boolValue` |
| Event On Disable FBA | `eventOnDisableFBA` | `UnityEvent` | – | 実行中にFBAを無効にした時に実行する処理。 / 表示条件: `showEventSettings.boolValue && useEventOnFBAViewChange.boolValue` |
| Event On Enable FBA In Editor | `eventOnEnableFBAInEditor` | `UnityEvent` | – | エディタ上でFBAを有効にした時に実行する処理。 / 表示条件: `showEventSettings.boolValue && useEventOnFBAViewChange.boolValue` |
| Event On Disable FBA In Editor | `eventOnDisableFBAInEditor` | `UnityEvent` | – | エディタ上でFBAを無効にした時に実行する処理。 / 表示条件: `showEventSettings.boolValue && useEventOnFBAViewChange.boolValue` |

### Other FBA Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Head Collider On FBA | `useHeadColliderOnFBA` | `bool` | – | FBA中に`headColliderOnFBA`を有効にする。 / 表示条件: `showEventSettings` がオンのとき |
| Use Head Collider On Third Person | `useHeadColliderOnThirdPerson` | `bool` | – | 三人称視点でもFBA用ヘッドコライダーを有効にする。 / 表示条件: `showEventSettings` がオンのとき |
| Head Collider On FBA | `headColliderOnFBA` | `Collider` | – | FBA時に切り替える頭部のコライダー。 / 表示条件: `showEventSettings.boolValue && useHeadColliderOnFBA.boolValue \|\| useHeadColliderOnThirdPerson.boolValue` |
| Event To Activate Head Collider On FBA | `eventToActivateHeadColliderOnFBA` | `UnityEvent` | – | ヘッドコライダーが有効になった時に実行する処理。 / 表示条件: `showEventSettings.boolValue && useHeadColliderOnFBA.boolValue \|\| useHeadColliderOnThirdPerson.boolValue` |
| Event To Deactivate Head Collider On FBA | `eventToDeactivateHeadColliderOnFBA` | `UnityEvent` | – | ヘッドコライダーが無効になった時に実行する処理。 / 表示条件: `showEventSettings.boolValue && useHeadColliderOnFBA.boolValue \|\| useHeadColliderOnThirdPerson.boolValue` |
| Event To Activate Head Collider On FBA On Editor | `eventToActivateHeadColliderOnFBAOnEditor` | `UnityEvent` | – | エディタ上でヘッドコライダーを有効にした時の処理。 / 表示条件: `showEventSettings.boolValue && useHeadColliderOnFBA.boolValue \|\| useHeadColliderOnThirdPerson.boolValue` |
| Event To Deactivate Head Collider On FBA On Editor | `eventToDeactivateHeadColliderOnFBAOnEditor` | `UnityEvent` | – | エディタ上でヘッドコライダーを無効にした時の処理。 / 表示条件: `showEventSettings.boolValue && useHeadColliderOnFBA.boolValue \|\| useHeadColliderOnThirdPerson.boolValue` |

### Change Third/First Person View In Editor Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Third Person In Editor Event | `setThirdPersonInEditorEvent` | `UnityEvent` | – | エディタで三人称表示に切り替えた時に実行する処理。 / 表示条件: `showEventSettings` がオンのとき |
| Set First Person In Editor Event | `setFirstPersonInEditorEvent` | `UnityEvent` | – | エディタで一人称表示に切り替えた時に実行する処理。 / 表示条件: `showEventSettings` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `cameraCanBeUsed` | `bool` | – | – |
| `FBAPivotCameraTransform` | `Transform` | – | – |
| `fullBodyAwarenessActive` | `bool` | – | – |
| `defaultStateName` | `string` | – | – |
| `useCustomThirdPersonAimActive` | `bool` | – | – |
| `useCustomThirdPersonAimCrouchActive` | `bool` | – | – |
| `currentVerticalRotationSpeed` | `float` | – | – |
| `currentHorizontalRotationSpeed` | `float` | – | – |
| `cameraStateEventInfoList` | `List<cameraStateEventInfo>` | new List<cameraStateEventInfo> () | – |
| `playerCameraStates` | `List<cameraStateInfo>` | new List<cameraStateInfo> () | – |
| `settings` | `cameraSettings` | new cameraSettings () | – |
| `onGround` | `bool` | – | – |
| `aimingInThirdPerson` | `bool` | – | – |
| `crouching` | `bool` | – | – |
| `firstPersonActive` | `bool` | – | – |
| `usingZoomOn` | `bool` | – | – |
| `usingZoomOff` | `bool` | – | – |
| `cameraCanRotate` | `bool` | true | – |
| `cameraType` | `typeOfCamera` | – | – |
| `cameraCurrentlyLocked` | `bool` | – | – |
| `lookAngle` | `Vector2` | – | – |
| `currentState` | `cameraStateInfo` | – | – |
| `lerpState` | `cameraStateInfo` | – | – |
| `lastTimeInputUsedWhenLookInPlayerDirectionActive` | `float` | – | – |
| `horizontalInput` | `float` | – | – |
| `verticalInput` | `float` | – | – |
| `playerNavMeshEnabled` | `bool` | – | – |
| `lookingAtTarget` | `bool` | – | – |
| `lookAtTargetIconRectTransform` | `RectTransform` | – | – |
| `tagToLookList` | `List<string>` | new List<string> () | – |
| `lookingAtPoint` | `bool` | – | – |
| `pointTargetPosition` | `Vector3` | – | – |
| `bodyPartsToLook` | `List<string>` | new List<string> () | – |
| `pauseOutlineShaderChecking` | `bool` | – | – |
| `cameraList` | `List<Camera>` | new List<Camera> () | – |
| `showSettings` | `bool` | – | – |
| `showEventSettings` | `bool` | – | – |
| `showLookTargetSettings` | `bool` | – | – |
| `showElements` | `bool` | – | – |
| `showCameraDebugState` | `bool` | – | – |
| `using2_5ViewActive` | `bool` | – | – |
| `useTopDownView` | `bool` | – | – |
| `setLookDirection` | `bool` | – | – |
| `targetToFollowForward` | `Vector3` | – | – |
| `currentLockedCameraCursor` | `RectTransform` | – | – |
| `currentLockedCameraCursorSize` | `Vector2` | – | – |
| `cameraRotationMode` | `cameraRotationType` | – | – |
| `zeroGravityModeOn` | `bool` | – | – |
| `freeFloatingModeOn` | `bool` | – | – |
| `focusArea` | `FocusArea` | – | – |
| `focusTargetPosition` | `Vector3` | – | – |
| `cameraMouseWheelStatesList` | `List<cameraMouseWheelStates>` | new List<cameraMouseWheelStates> () | – |
| `lockedCameraPrefabsTypesList` | `List<lockedCameraPrefabsTypes>` | new List<lockedCameraPrefabsTypes> () | – |
| `cameraNoiseStateList` | `List<cameraNoiseState>` | new List<cameraNoiseState> () | – |
| `leanActive` | `bool` | – | – |
| `leanToRightActive` | `bool` | – | – |
| `leanToLeftActive` | `bool` | – | – |
| `leanInputEnabled` | `bool` | true | – |
| `remoteEventOnLockOnStart` | `List<string>` | new List<string> () | – |
| `remoteEventOnLockOnEnd` | `List<string>` | new List<string> () | – |
| `mainCanvasSizeDelta` | `Vector2` | – | – |
| `halfMainCanvasSizeDelta` | `Vector2` | – | – |
| `usingScreenSpaceCamera` | `bool` | – | – |
| `cameraActionsInputEnabled` | `bool` | true | – |
| `externalReticleCurrentlyActive` | `bool` | – | – |
| `cameraReticleCurrentlyActive` | `bool` | – | – |
| `customReticleInfoList` | `List<customReticleInfo>` | new List<customReticleInfo> () | – |
| `temporaLockedCameraPrefabNmeToPlaceOnScene` | `string` | – | – |
| `followingMultipleTargets` | `bool` | – | – |
| `extraPositionOffset` | `Vector3` | – | – |
| `multipleTargetsToFollowList` | `List<Transform>` | new List<Transform> () | – |
| `lookingAtFixedTarget` | `bool` | – | – |
| `headColliderOnFBAActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPauseUpdateRegularPlayerCameraPositionState(bool state)` | `pauseUpdateRegularPlayerCameraPositionState` を設定するだけ。 |
| `setPlayerCameraTransformFollowsPlayerTransformRotationOnFBAState(bool state)` | FBA時にカメラの回転をプレイヤーに合わせるかを切り替えるフラグを設定するだけ。 |
| `setIgnoreHorizontalCameraRotationOnFBAState(bool state)` | FBA時の水平回転を無視するフラグを設定するだけ。 |
| `setIgnoreVerticalCameraRotationOnFBAState(bool state)` | FBA時の垂直回転を無視するフラグを設定するだけ。 |
| `setIgnorePlayerRotationToCameraOnFBAState(bool state)` | FBA時にプレイヤーの回転をカメラへ反映しないフラグを設定するだけ。 |
| `getLookDirectionTransformRotationValue(Vector3 forwardDirection)` | 前方方向と `lookCameraDirection` の内積から、2.5Dは±90度、通常は180度のY回転量を返す。 |
| `checkEventOnMoveCamera(Vector2 currentAxisValues)` | 入力の大きさで `movingCameraState` を更新し、移動の開始・継続・停止イベントを発火する。 |
| `getCurrentLookDirection2_5d()` | `lookCameraDirection` をそのまま返す。 |
| `getCurrentLookDirectionTopDown()` | `lookCameraDirection` をそのまま返す。 |
| `getDefaultThirdPersonStateName()` | `defaultThirdPersonStateName` を返す。 |
| `getDefaultFirstPersonStateName()` | `defaultFirstPersonStateName` を返す。 |
| `getDefaultVehiclePassengerStateName()` | `defaultVehiclePassengerStateName` を返す。 |
| `getDefaultFullBodyAwarenessStateName()` | `defaultFullBodyAwarenessStateName` を返す。 |
| `checkUpdateReticleActiveState(bool state)` | 外部レティクルの有無を反転して保持し、`updateReticleActive` で表示を更新する。 |
| `updateReticleActive()` | カメラ種別と一人称/三人称の設定に応じて中央レティクルの表示を切り替える。 |
| `enableOrDisableMainCameraReticle(bool state)` | `mainCameraReticleGameObject` の表示を状態に合わせて切り替える。 |
| `enableCustomReticle(string reticleName)` | `enableOrDisableCustomReticle` をtrueで呼び出すだけ。 |
| `disableCustomReticle(string reticleName)` | `enableOrDisableCustomReticle` をfalseで呼び出すだけ。 |
| `disableAllCustomReticle()` | 名前を空にして全カスタムレティクルを非表示にする。 |
| `enableOrDisableCustomReticle(bool state, string reticleName)` | 指定名のレティクルを表示して他を隠し、有効時は親をカーソル位置へ付け替える。 |
| `setCurrentLockedCameraCursor(RectTransform currentCursor)` | カーソルを設定して画面サイズから移動限界を計算し、nullなら位置を戻して解除する。 |
| `sortTargetsListToLookTransformByDistance(Transform a, Transform b)` | 画面上の中心からの距離で2つの対象を比較する並び替え用デリゲート。 |
| `checkChangeCurrentTargetToLook()` | マウス入力の角度と距離から注視対象を選び直し、`setLookAtTargetState` で切り替える。 |
| `setReverseVerticalAccelerometerState(bool state)` | `settings.reverseVerticalAccelerometer` を設定するだけ。 |
| `setReverseHorizontalAccelerometerState(bool state)` | `settings.reverseHorizontalAccelerometer` を設定するだけ。 |
| `clampLookAngle(float deltaTimeToUse)` | 入力を `lookAngle` に反映し、地上/空中や状態の上下限でクランプして視点を補正する。 |
| `checkCurrentRotationSpeed()` | 一人称か三人称かに応じて現在の垂直・水平回転速度を設定する。 |
| `sethorizontalCameraLimitActiveOnAirState(bool state)` | `horizontalCameraLimitActiveOnAir` を設定するだけ。 |
| `setShotCameraNoise(Vector2 noiseAmount)` | ノイズ量を設定して `addNoiseToCamera` を有効にし、継続時間は無効にする。 |
| `setShotCameraNoiseWithDuration(Vector2 noiseAmount, float duration)` | ノイズ量と継続時間を設定して開始時刻を記録し、一定時間だけカメラを揺らす。 |
| `isCurrentCameraLookInPlayerDirection()` | `currentState.lookInPlayerDirection` を返す。 |
| `lookInPlayerDirection(float rotationSpeedToUse, bool rotatePlayerCameraTransform, bool rotatePivotCameraTransform)` | ピボットとカメラの回転をプレイヤー方向へLerpし、角度が揃うとリセットを終了する。 |
| `projectOnSegment(Vector3 v1, Vector3 v2, Vector3 playerPosition)` | 線分v1-v2上で `playerPosition` に最も近い点を返す。 |
| `followPlayerPositionOnLockedCamera(float deltaTimeToUse)` | 固定カメラのピボットを、プレイヤーやウェイポイント・スプラインの目標へ速度設定に従い追従させる。 |
| `getHorizontalInput()` | `horizontalInput` を返す。 |
| `getVerticalInput()` | `verticalInput` を返す。 |
| `setCanvasInfo(Vector2 newMainCanvasSizeDelta, bool newUsingScreenSpaceCamera, bool creatingCharactersOnEditor)` | キャンバスのサイズとスクリーンスペースカメラ設定を保持し、必要ならエディタ更新を行う。 |
| `setFollowingMultipleTargetsState(bool state, bool activatingFunctionFromEditor)` | `followingMultipleTargets` を設定し、必要ならエディタ更新を行う。 |
| `setMultipleTargetsToFollowList(List<Transform> newMultipleTargetsToFollowList, bool activatingFunctionFromEditor)` | 複数追従対象リストを置き換え、空ならクリアして必要ならエディタ更新を行う。 |
| `setextraPositionOffsetValue(Vector3 newOffset)` | `extraPositionOffset` を設定するだけ。 |
| `getPositionToLimit(bool calculateOnRunTime)` | 複数対象やオフセット、2.5D/トップダウンの計算を経て、制限を適用した追従位置を返す。 |
| `calculateBoundPosition(bool calculateOnRunTime)` | `mainCollider` の境界から `FocusArea` を更新し、`boundOffset` 加算位置を返す。 |
| `setIgnorePivotCameraCollisionActiveState(bool state)` | `ignorePivotCameraCollisionActive` を設定するだけ。 |
| `setPivotCameraTransformParent(Transform newParent)` | ピボットの親を変更し、FBA時は頭部ピボットの親も設定に合わせて付け替える。 |
| `setPivotCameraTransformParentCurrentTransformToFollowWithDuration(float duration)` | FBA時にピボットを現在の追従先へ一定時間だけ親子付けし、その後元の親へ戻す。 |
| `setExtraFollowTransformPositionOffsetFBA(Vector3 newValue)` | FBA用の追従位置オフセットを設定し、非ゼロなら使用フラグを立てる。 |
| `stopUpdateCoroutine()` | `updateCoroutine` を停止するだけ。 |
| `setUpdatePivotTransformPositionOnFBAIfCameraCantBeUsedActiveState(bool state)` | FBAでカメラ使用不可でもピボットを更新するかのフラグを設定するだけ。 |
| `setUpdateFBAPivotCameraTransformInsideHeadPositionActiveState(bool state)` | フラグを設定し、FBA時は頭部ピボットの親と位置・回転を設定に合わせて切り替える。 |
| `isUpdateFBAPivotCameraTransformInsideHeadPositionActive()` | `updateFBAPivotCameraTransformInsideHeadPositionActive` を返す。 |
| `setCheckCameraCollisionEvenOnFullBodyAwarenessActiveState(bool state)` | `checkCameraCollisionEvenOnFullBodyAwarenessActive` を設定するだけ。 |
| `checkCameraPosition()` | ピボットからカメラへ球体キャストし、衝突時は手前へ、非衝突時は設定位置へLerpする。 |
| `setTurnBasedCombatActionActiveState(bool state)` | `turnBasedCombatActionActive` を設定するだけ。 |
| `setCameraToFreeOrLocked(typeOfCamera state, lockedCameraSystem.cameraAxis lockedCameraInfo)` | フリー/固定カメラを切り替え、状態名・FOV・カーソル・イベント・各マネージャの設定を更新する。 |
| `setClampAimDirectionsState(bool state)` | `clampAimDirections` を設定するだけ。 |
| `calculateLockedCameraLookAtPlayerPosition()` | 固定カメラ軸から注視対象への角度を求め、制限内にクランプして保存する。 |
| `setCameraLimit(bool useCameraLimitValue, bool useWidthLimitValue, float newWidthLimitRight, float newWidthLimitLeft, bool useHeightLimitValue, float newHeightLimitUpper, float newHeightLimitLower, Vector3 newCameraLimitPosition, bool depthLimitEnabled, float newDepthLimitFront, float newDepthLimitBackward)` | 幅・高さ・奥行きのカメラ制限の使用有無と値、基準位置をまとめて設定する。 |
| `setNewCameraForwardPosition(float newCameraForwardPosition)` | 固定カメラ軸の前後位置を変更し、メインカメラを付け替えて `lockedCameraMovement` を呼ぶ。 |
| `isTopdownViewEnabled()` | `useTopDownView` を返す。 |
| `callLockedCameraEventOnEnter(lockedCameraSystem.cameraAxis cameraAxisToCheck)` | 設定されていれば固定カメラの入場用UnityEventを発火する。 |
| `callLockedCameraEventOnExit(lockedCameraSystem.cameraAxis cameraAxisToCheck)` | 設定されていれば固定カメラの退場用UnityEventを発火する。 |
| `setUsing2_5ViewActiveState(bool state)` | `using2_5ViewActive` を設定するだけ。 |
| `setUseCustomOriginalLockedCameraPivotPositionTransformState(bool state)` | カスタムの元ピボット位置Transformを使うフラグを設定するだけ。 |
| `setCustomOriginalLockedCameraPivotPosition(Vector3 newValue)` | `customOriginalLockedCameraPivotPosition` を設定するだけ。 |
| `setNewOriginalLockedCameraPivotPosition(Vector3 newValue)` | `originalLockedCameraPivotPosition` を設定するだけ。 |
| `getCameraRaycastDirection()` | 固定カメラでカーソルがあればカーソル位置、なければカメラ前方のRayを返す。 |
| `setManualAimStateOnLockedCamera(bool state)` | 固定カメラの時のみ `setManualAimState` を呼ぶ。 |
| `setManualAimState(bool state)` | カーソルと注視対象を設定し、プレイヤーのエイム状態を切り替える。 |
| `movePlayerToDefaultHorizontalValue2_5d()` | 2.5Dの固定軸からずれていれば、プレイヤーを既定位置へ戻すコルーチンを開始する。 |
| `stopLockedCameraMovementCoroutine()` | `lockedCameraMoving` をfalseにし、移動コルーチンを停止する。 |
| `lockedCameraMovement(bool isBeingSetToLocked)` | 固定カメラへの移行コルーチンを開始し、既存の移行は停止する。 |
| `setCurrentAxisTransformValues(Transform newValues)` | 固定メインカメラの位置とY回転を指定Transformに合わせる。 |
| `setLockedMainCameraTransformRotation(Vector3 normal)` | 法線に合わせて固定カメラのピボットとカメラの回転を設定し、軸位置を補正する。 |
| `setLockedCameraAxisPositionOnGravityChange(Vector3 newPosition)` | 固定カメラ軸の位置を目標へLerpするコルーチンを開始する。 |
| `setCharacterRotatingToSurfaceState(bool state)` | `characterRotatingToSurface` を設定するだけ。 |
| `getCurrentLockedCameraTransform()` | `lockedCameraPosition` を返す。 |
| `getCurrentLockedCameraAxis()` | `lockedCameraAxis` を返す。 |
| `getCameraTransform()` | `mainCameraTransform` を返す。 |
| `getMainCamera()` | `mainCamera` が未設定なら `Camera.main` を取得して親を設定し、返す。 |
| `setNewMainCameraOnMainParent()` | メインカメラを `mainCameraParent` の子にして位置と回転をリセットする。 |
| `setMainCameraParent(Transform newParent)` | メインカメラの親を指定Transformに変更する。 |
| `resetMainCameraLocalPositionRotation()` | メインカメラのローカル位置と回転をゼロに戻す。 |
| `setLookAtBodyPartsOnCharactersState(bool state)` | `lookAtBodyPartsOnCharacters` を設定するだけ。 |
| `setOriginalLookAtBodyPartsOnCharactersState()` | 保存しておいた元の値で `setLookAtBodyPartsOnCharactersState` を呼ぶ。 |
| `getClosestTargetToLook()` | 範囲内の対象から画面中心に近いものを選び、シェーダや狙う部位を設定して成否を返す。 |
| `setLookAtTargetStateInput(bool state)` | 固定カメラでは対象リストを巡回して次を注視し、それ以外は手動の注視切替を呼ぶ。 |
| `checkIfPlayerIsLookingAtDeadTarget(bool state)` | フリーなら手動注視を設定し、固定ではカーソル表示か注視解除に振り分ける。 |
| `setTemporalObjectToLookAtTarget(Transform newObject)` | `temporalObjectToLookAtTarget` を設定するだけ。 |
| `lookAtTemporalObjectToLookAtTarget()` | 一時対象が設定されていれば、それを手動注視の対象にして注視を開始する。 |
| `setLookAtTargetStateManual(bool state, Transform objectToLook)` | `setLookAtTargetState` を呼び、入力による注視フラグも合わせて設定する。 |
| `setLookAtTargetState(bool state, Transform objectToLook)` | 注視状態と対象・シェーダ・アイコン・イベントを更新し、対象が無ければ解除する。 |
| `setUseLookTargetIconState(bool state)` | `useLookTargetIcon` を設定するだけ。 |
| `setOriginalUseLookTargetIconValue()` | 保存した元の値で `useLookTargetIcon` を戻す。 |
| `setLookAtTargetOnLockedCameraState()` | `searchingToTargetOnLockedCamera` をtrueにするだけ。 |
| `getClosestTargetToLookOnLockedCamera()` | 固定カメラ用に障害物と画面内を判定しつつ最近傍の対象を探して成否を返す。 |
| `checkRemoveEventOnLockedOnStart(Transform objectToCheck)` | 対象が変わった時だけ、そのオブジェクトへロックオン開始のリモートイベントを送る。 |
| `checkRemoveEventOnLockOnEnd()` | 前回の対象へロックオン終了のリモートイベントを送り、記録を消す。 |
| `checkEventOnLockAtTargetState(bool state)` | 有効なら注視開始/終了のUnityEventを状態に応じて発火する。 |
| `checkEventOnLockedOnStart()` | 有効なら `eventOnLockOnStart` を発火する。 |
| `checkEventOnLockOnEnd()` | 有効なら `eventOnLockOnEnd` を発火する。 |
| `setTargetToLook(Transform newTarget)` | `targetToLook` を設定するだけ。 |
| `getLastCharacterToLook()` | `lastCharacterToLook` を返す。 |
| `getPlayerControllerGameObject()` | `playerControllerGameObject` を返す。 |
| `setHipsTransform(Transform newHips)` | `hipsTransform` を設定してエディタ更新を行う。 |
| `updateHipsTransformInGame(Transform newHips)` | `hipsTransform` を設定するだけ。 |
| `checkTargetToLookShader(Transform newObjectFound)` | 前の対象の輪郭を解除し、新しい対象があれば輪郭シェーダを付ける。 |
| `checkIfSetNewShaderToObjectToGrabFound(GameObject objectToCheck)` | 対象の `outlineObjectSystem` に輪郭シェーダを設定する。 |
| `checkIfSetOriginalShaderToPreviousObjectToGrabFound()` | 直前の対象の輪郭シェーダを解除して参照を消す。 |
| `setLookAtTargetEnabledState(bool state)` | `lookAtTargetEnabled` を設定するだけ。 |
| `setLookAtTargetEnabledStateDuration(bool currentState, float duration, bool nextState)` | 指定時間だけ注視を無効化し、その後 `nextState` に戻すコルーチンを開始する。 |
| `setLookAtTargetSpeedValue(float newValue)` | `lookAtTargetSpeed` を設定するだけ。 |
| `setOriginallookAtTargetSpeedValue()` | 元の値で `lookAtTargetSpeed` を戻す。 |
| `setMaxDistanceToFindTargetValue(float newValue)` | `maxDistanceToFindTarget` を設定するだけ。 |
| `setOriginalmaxDistanceToFindTargetValue()` | 元の値で `maxDistanceToFindTarget` を戻す。 |
| `setMaxDistanceToCameraCenter(bool useMaxDistance, float maxDistance)` | 画面中心からの距離制限の使用有無と値を設定するだけ。 |
| `setHeadColliderRadiusOnFBA(float newValue)` | 頭部のSphereColliderを取得して半径を変更し、元の半径を保持する。 |
| `getHeadColliderOnFBA()` | `headColliderOnFBA` を返す。 |
| `setOriginalHeadColliderRadiusOnFBA()` | 保存した元の半径で `setHeadColliderRadiusOnFBA` を呼ぶ。 |
| `setUseHeadColliderOnFBAState(bool state)` | `useHeadColliderOnFBA` を設定するだけ。 |
| `setUseHeadColliderOnThirdPersonState(bool state)` | `useHeadColliderOnThirdPerson` を設定するだけ。 |
| `checkGetUpStateFromDeathOnFBA()` | FBA時のみピボットを元の親に戻し、回転をリセットする。 |
| `death(bool state, bool followHips)` | 死亡状態とヘッドボブを更新し、FBAや三人称でピボットや追従先を死亡/復帰に合わせる。 |
| `setCustomSmoothReturnSpeed(float newValue)` | `smoothReturnSpeed` を設定するだけ。 |
| `setOriginalSmoothReturnSpeed()` | 元の値で `smoothReturnSpeed` を戻す。 |
| `slerpCameraState(cameraStateInfo to, cameraStateInfo from, float lerpSpeed)` | `to` に `from` の値を `lerpSpeed` で補間して割り当てる。 |
| `slerpCameraStateAtOnce(cameraStateInfo to, cameraStateInfo from)` | `to` に `from` の値を補間なしで割り当てる。 |
| `setTargetToFollow(Transform newTargetToFollow)` | 追従対象を設定し、カメラ位置をその位置へ即座に移動する。 |
| `setOriginalTargetToFollow()` | プレイヤー本体を追従対象に戻す。 |
| `setCameraStateOnlyOnThirdPerson(string stateName)` | FBAでなく三人称かつフリーカメラの時だけ状態を切り替える。 |
| `setDefaultCameraStateOnlyOnThirdPerson()` | 三人称の既定状態名で `setCameraStateOnlyOnThirdPerson` を呼ぶ。 |
| `setCameraStateExternally(string stateName)` | FBA中でなければ外部から状態を切り替える。 |
| `setCameraState(string stateName)` | 名前一致の状態を探して適用し、リーン・イベント・FOV・クリップ面を更新する。 |
| `setNewNearClipPlaneValue(float nearClipPlaneValue)` | `mainCamera.nearClipPlane` を設定するだけ。 |
| `setDefaultNearClipPlaneValue()` | 既定値で `setNewNearClipPlaneValue` を呼ぶ。 |
| `setIgnoreMainCameraFovOnSetCameraState(bool state)` | `ignoreMainCameraFovOnSetCameraState` を設定するだけ。 |
| `setDefaultThirdPersonStateName(string newName)` | `defaultThirdPersonStateName` を設定するだけ。 |
| `setDefaultFirstPersonStateName(string newName)` | `defaultFirstPersonStateName` を設定するだけ。 |
| `getCurrentStateName()` | `currentStateName` を返す。 |
| `setCameraPositionMouseWheelEnabledState(bool state)` | `cameraPositionMouseWheelEnabled` を設定するだけ。 |
| `moveAwayCamera()` | 可能なら立ち上がらせた上で、カメラを離す状態と三人称状態の間で切り替える。 |
| `isCurrentCameraStateHeadTrackActive()` | `currentState.headTrackActive` を返す。 |
| `setMainCameraFov(float targetValue, float speed)` | 既存のFOVコルーチンを止め、目標値への変更コルーチンを開始する。 |
| `stopFovChangeCoroutine()` | `changeFovCoroutine` を停止するだけ。 |
| `changeFovValue(float targetValue, float speed)` | FOVを `speed` で目標値へ近づけるコルーチンで、実行中フラグも管理する。 |
| `setFieldOfViewValueWithoutCheckIgnoreExternalFovChange(float newValue)` | 外部FOV無視の判定を一時的に外してFOVを直接設定する。 |
| `stopCameraFovStartAndEndCoroutine()` | `cameraFovStartAndEndCoroutine` を停止するだけ。 |
| `changeFovValueStartAndEnd(float startTargetValue, float endTargetValue, float speed)` | FOVを開始値へ動かした後、終了値へ動かすコルーチン。 |
| `isFOVChanging()` | `fieldOfViewChanging` を返す。 |
| `quickChangeFovValue(float targetValue)` | FOVを目標値へ補間なしで設定する。 |
| `setOriginalCameraFov()` | 現在の状態の初期FOVへ `zoomSpeed` で戻す。 |
| `getMainCameraCurrentFov()` | `mainCamera.fieldOfView` を返す。 |
| `setZoom(bool state)` | ズーム状態に応じてFOV・回転速度・スキャナー・武器のFOVを切り替える。 |
| `setZoomStateDuration(bool currentState, float duration, bool nextState)` | ズーム有効状態を一定時間だけ変更するコルーチンを開始する。 |
| `setZoomEnabledState(bool state)` | `settings.zoomEnabled` を設定するだけ。 |
| `disableZoom()` | ズーム中なら解除し、回転速度とスキャナーを元に戻す。 |
| `isUsingZoom()` | `usingZoomOn` を返す。 |
| `setUsingZoomOnValue(bool value)` | `usingZoomOn` を設定し、スキャナーのズーム状態も更新する。 |
| `setScannerManagerState(bool state)` | スキャナーが見つかっていれば、そのズーム状態を有効/無効にする。 |
| `changeRotationSpeedValue(float newVerticalRotationValue, float newHorizontalRotationValue)` | 一人称/三人称それぞれの回転速度を設定し、AI使用時は即時反映する。 |
| `setOriginalRotationSpeed()` | 一人称・三人称の回転速度を保存値へ戻す。 |
| `updateOriginalRotationSpeedValues()` | 現在の回転速度を保存用の元値へコピーする。 |
| `setPauseChangeCameraFovActiveState(bool state)` | `pauseChangeCameraFovActive` を設定するだけ。 |
| `activateAiming()` | エイム状態にし、側・しゃがみ・FBAに応じた照準用カメラ状態へ切り替える。 |
| `deactivateAiming()` | エイムを解除し、カメラ種別としゃがみに応じた通常状態へ戻す。 |
| `changeAimSide(int value)` | 1なら右、それ以外は左の照準カメラ状態に切り替える。FBA時は何もしない。 |
| `setUseCustomThirdPersonAimActivePausedState(bool state)` | `useCustomThirdPersonAimActivePaused` を設定するだけ。 |
| `isUseCustomThirdPersonAimActivePaused()` | `useCustomThirdPersonAimActivePaused` を返す。 |
| `setUseCustomThirdPersonAimActiveState(bool state, string newCustomDefaultThirdPersonAimRightStateName, string newCustomDefaultThirdPersonAimLeftStateName)` | フラグと左右のカスタム照準状態名を設定し、空なら既定名を使う。 |
| `setUseCustomThirdPersonAimCrouchActiveState(bool state, string newCustomDefaultThirdPersonAimRightCrouchStateName, string newCustomDefaultThirdPersonAimLeftCrouchStateName)` | しゃがみ用のカスタム照準フラグと左右の状態名を設定し、空なら既定名を使う。 |
| `setCheckUseCustomFBAAimActiveState(bool state)` | `checkUseCustomFBAAimActive` を設定するだけ。 |
| `onGroundOrOnAir(bool state)` | `onGround` を設定し、空中ならピボット角度の補正を有効にする。 |
| `startShakeCamera()` | カメラ揺れを有効にし、`currentCameraShakeStateName` をShakingに設定する。 |
| `isCameraShaking()` | `settings.shakingCameraActive` を返すだけ。 |
| `accelerateShake(bool value)` | カメラシェイクの加速フラグ `settings.accelerateShaking` を設定するだけ。 |
| `changeCameraToThirdOrFirstView(bool state)` | `firstPersonActive` が `state` と異なる場合のみ `changeCameraToThirdOrFirstView` を呼ぶ。 |
| `setCameraOnThirdPersonOrFBAView(bool state)` | `fullBodyAwarenessActive` が `state` と異なるときのみ `changeCameraView` を呼ぶ。 |
| `changeCameraToThirdOrFirstView()` | 三人称エイム中やスキャナー使用中でなければ `changeCameraView` で一人称/三人称を切替える。 |
| `changeCameraView()` | 一人称状態を反転してFBAを切替え、カメラ状態・頭ボブ・武器・重力・掴み管理へ通知する視点変更の本体。 |
| `checkIfDropObjectIfNotPhysical(bool disableAimState)` | `grabObjectsManager` があれば `checkIfDropObjectIfNotPhysical` に委譲する。 |
| `changeTypeView()` | `changeAimSide` でエイム側を調整した後、`changeCameraToThirdOrFirstView` で視点を切替える。 |
| `setAimModeSide(bool state)` | `aimSide` を左右反転して `powersManager` に通知する。`state` は反転するかを指定。 |
| `activateFirstPersonCamera()` | `firstPersonActive` を true にし、伏せ状態に応じた一人称カメラステートを設定して表示を更新する。 |
| `deactivateFirstPersonCamera()` | `firstPersonActive` を false にし、FBA/伏せに応じた三人称ステートを設定して表示を更新する。 |
| `activateFirstPersonCameraEditor()` | 編集中フラグを立てて `activateFirstPersonCamera` を呼び、最後に戻す。 |
| `deactivateFirstPersonCameraEditor()` | 編集中フラグを立てて `deactivateFirstPersonCamera` を呼び、最後に戻す。 |
| `activeFullBodyAwarenessEditor()` | FBAを有効化して三人称へ戻し、武器のFBA状態とカメラ/ピボット位置をリセットする。 |
| `deactiveFullBodyAwarenessEditor()` | FBAを無効化して三人称へ戻し、武器のFBA状態とカメラ/ピボット位置をリセットする。 |
| `updatePlayerStatesToView()` | 視点に合わせてアニメーター、メッシュ表示、接地判定、頭ボブ、武器、FBAイベントをまとめて更新する。 |
| `isChangeCameraViewEnabled()` | `changeCameraViewEnabled` かつ視点変更が一時停止中でないかを返す。 |
| `isPausePlayerCameraViewChangeActive()` | `pausePlayerCameraViewChange` を返すだけ。 |
| `enableOrDisableAllChangeCameraEnabledView(bool state)` | 視点変更とマウスホイールでのカメラ距離変更の有効状態をまとめて設定する。 |
| `setOriginalAllChangeCameraViewEnabledState()` | 視点変更とマウスホイール距離変更の有効状態を、保存された初期値へ戻す。 |
| `enableOrDisableChangeCameraView(bool state)` | `changeCameraViewEnabled` フラグを設定するだけ。 |
| `setOriginalchangeCameraViewEnabledValue()` | `originalChangeCameraViewEnabled` の値で視点変更の有効状態を設定する。 |
| `setPausePlayerCameraViewChangeState(bool state)` | `pausePlayerCameraViewChange` フラグを設定するだけ。 |
| `checkCharacterStateIconForViewChange()` | `characterStateIconManager` があれば視点変更用のアイコン更新に委譲する。 |
| `changeCameraRotationState(bool state)` | カメラ回転の可否フラグ `cameraCanRotate` を設定するだけ。 |
| `pauseOrPlayCamera(bool state)` | `cameraCanBeUsed` を設定し、有効化時には最終回転時刻も更新する。 |
| `cameraCanBeUsedActive()` | `cameraCanBeUsed` を返すだけ。 |
| `setCameraRotationInputEnabled(bool state)` | `cameraRotationInputEnabled` を設定するだけ。 |
| `enableCameraRotationInput()` | `cameraRotationInputEnabled` を true にするだけ。 |
| `disableCameraRotationInput()` | `cameraRotationInputEnabled` を false にするだけ。 |
| `setCameraActionsInputEnabledState(bool state)` | `cameraActionsInputEnabled` を設定するだけ。 |
| `enableCameraActionsInput()` | `cameraActionsInputEnabled` を true にするだけ。 |
| `disableCameraActionsInput()` | `cameraActionsInputEnabled` を false にするだけ。 |
| `calibrateAccelerometer()` | AI使用中でなくタッチ操作なら、現在の加速度から `calibrationMatrix` を再計算して端末の持ち方を補正する。 |
| `setUseAcelerometerState(bool state)` | `settings.useAcelerometer` を設定するだけ。 |
| `isCameraRotating()` | `isMoving` を返すだけ。 |
| `checkIfCameraRotatingWithTolerance(float movingTolerance)` | 水平/垂直入力の絶対値が `movingTolerance` を超えていれば true を返す。 |
| `isPlayerAiming()` | `playerAiming` を返すだけ。 |
| `setLastTimeMoved()` | `lastTimeMoved` に現在時刻を記録するだけ。 |
| `setLastTimeCameraRotated()` | `lastTimeCameraRotated` に現在時刻を記録するだけ。 |
| `playOrPauseHeadBob(bool state)` | 頭ボブ管理 `headBobManager` の再生/停止に委譲する。 |
| `stopAllHeadbobMovements()` | 頭ボブの全動作停止を `headBobManager` に委譲する。 |
| `pauseHeadBodWithDelay(float delayAmount)` | `delayAmount` 秒後の頭ボブ停止を `headBobManager` に依頼する。 |
| `getHeadBobManager()` | `headBobManager` を返すだけ。 |
| `setFirstOrThirdHeadBobView(bool state)` | 頭ボブの一人称/三人称設定を `headBobManager` に委譲する。 |
| `setHeadbobState(string headBobStateName)` | `headBobStateName` の頭ボブ状態設定を `headBobManager` に委譲する。 |
| `setDefaultHeadbobState()` | 頭ボブの既定状態への復帰を `headBobManager` に委譲する。 |
| `isCameraPlacedInFirstPerson()` | メインカメラとピボットの距離が0.01未満なら一人称とみなし true を返す。 |
| `isFullBodyAwarenessActive()` | `fullBodyAwarenessActive` を返すだけ。 |
| `setFullBodyAwarenessActiveState(bool state)` | `fullBodyAwarenessActive` フラグを設定するだけ。 |
| `updateFBAPivotCameraTransformValuesToMainPivotCameraTransform()` | FBAピボット生成済みなら、その位置と回転をピボットカメラに合わせる。 |
| `removeLeanRotationFromPivotCameraTransform()` | ピボットカメラのローカルオイラー角のYとZを0にしてリーン回転を除去する。 |
| `updateFBAPivotCameraTransformToPivotCameraTransform()` | FBA中かつFBAピボット生成済みなら `updatePivotTransformPosition` を呼ぶ。 |
| `setFBAPivotCameraTransformParent(Transform newParent)` | FBA中かつFBAピボット生成済みなら、その親を `newParent` に変更する。 |
| `isCameraTypeFree()` | `cameraType` が `free` かどうかを返すだけ。 |
| `setLookAngleValue(Vector2 newValue)` | `lookAngle` を `newValue` に設定するだけ。 |
| `resetMainCameraTransformLocalPosition()` | メインカメラのローカル位置を `lerpState` のカメラオフセットへ戻す。 |
| `resetPivotCameraTransformLocalPosition()` | ピボットカメラのローカル位置を `lerpState` のピボットオフセットへ戻す。 |
| `setPlayerCameraTransformRotation(Quaternion newRotation)` | `playerCameraTransform.rotation` を `newRotation` にするだけ。 |
| `resetCurrentCameraStateAtOnce()` | `currentState` の値を `lerpState` へ補間なしで即座に反映する。 |
| `configureCurrentLerpState(Vector3 pivotOffset, Vector3 cameraOffset)` | `lerpState` のピボット/カメラオフセットを引数の値に設定する。 |
| `configureCameraAndPivotPositionAtOnce()` | ピボットとメインカメラのローカル位置を `currentState` のオフセットへ即座に移動する。 |
| `setCurrentCameraUpRotationValue(float newRotation)` | `currentCameraUpRotation` を設定するだけ。 |
| `Rotate(Vector3 currentLookPost)` | AIからの視線目標 `navMeshCurrentLookPos` を設定するだけ。 |
| `setResetVerticalCameraRotationActiveState(bool state)` | `resetVerticalCameraRotationActive` を設定するだけ。 |
| `setPlayerNavMeshEnabledState(bool state)` | `playerNavMeshEnabled` を設定するだけ。 |
| `startOverride()` | `overrideTurretControlState(true)` を呼び、AI使用状態とカメラ位置を切替える。 |
| `stopOverride()` | `overrideTurretControlState(false)` を呼び、AIによる上書き状態を解除する。 |
| `overrideTurretControlState(bool state)` | `usedByAI` を `state` の反転値にし、AI使用時は `setOverrideCameraPosition` も呼ぶ。 |
| `setUsedByAIState(bool state)` | `usedByAI` を設定するだけ。 |
| `enableOrDisablePlayerCameraGameObject(bool state)` | `SetActive` がコメントアウトされており、実質何もしない。 |
| `enableOrDisableMainCamera(bool state)` | `mainCamera.enabled` を設定するだけ。 |
| `enableAICamera()` | `enableOrDisableAICamera(true)` を呼ぶだけ。 |
| `disableAICamera()` | `enableOrDisableAICamera(false)` を呼ぶだけ。 |
| `enableOrDisableAICamera(bool state)` | AIカメラの切替。有効化時は一人称から三人称へ戻してAIステートを設定し、無効化時は元の視点や前キャラ位置へ復帰させる。 |
| `setUseSmoothCameraTransitionBetweenCharactersState(bool state)` | `useSmoothCameraTransitionBetweenCharacters` を設定するだけ。 |
| `enableOrDisableCameraAudioListener(bool state)` | メインカメラに `AudioListener` があれば、その有効状態を設定する。 |
| `getScreenCenter()` | スクリーン中央座標を返し、`usingScreenSpaceCamera` 時はカメラの `rect` を考慮する。 |
| `adjustCameraToPreviousCharacter()` | カメラを一時停止し、前キャラの向きと見上げ角をコピーしてから再開する。 |
| `setPreviousCharacterControl(GameObject newPpreviousCharacterControl, Vector3 cameraPosition, Quaternion cameraRotation, bool previousCharacterControlInFirstPersonViewValue)` | 前キャラの参照、カメラ位置・回転、一人称だったかをまとめて記録する。 |
| `adjustCameraToPreviousCharacterSmoothly()` | 既存コルーチンを止め、前キャラのカメラ位置へ滑らかに移動するコルーチンを開始する。 |
| `setOverrideCameraPosition(bool state)` | 既定ステートのカメラオフセットをAI用/通常用に切替え、状態を再設定して即時反映する。 |
| `setExtraRotationToCamera()` | カメラへ追加回転を与えるコルーチンを開始し、完了まで回転入力とカメラ利用を止める。 |
| `setZeroGravityModeOnState(bool state)` | `zeroGravityModeOn` を設定するだけ。 |
| `setfreeFloatingModeOnState(bool state)` | `freeFloatingModeOn` を設定するだけ。 |
| `setForwardRotationValue(float value)` | `targetForwardRotationAngle` を設定するだけ。 |
| `getIconPosition(Vector3 worldObjectPosition)` | ワールド座標をビューポート経由でキャンバス座標へ変換し、アイコン位置を返す。 |
| `setLockedCameraRotationActiveToLeft(bool holdingButton)` | 固定回転量設定なら左回転コルーチン、そうでなければ左回転フラグを `holdingButton` で設定する。 |
| `setLockedCameraRotationActiveToRight(bool holdingButton)` | 固定回転量設定なら右回転コルーチン、そうでなければ右回転フラグを `holdingButton` で設定する。 |
| `stopRotateLockedCameraFixedRotationAmount()` | 固定量回転の実行フラグを false にし、回転コルーチンを停止する。 |
| `setLockedMainCameraTransformRotationSmoothly(Vector3 targetRotationEuler, float rotationSpeed)` | 実行中なら停止し、`targetRotationEuler` へ `rotationSpeed` で回すコルーチンを開始する。 |
| `setLockedMainCameraTransformRotationSmoothlyToCurrentLockedCameraView(float rotationSpeed)` | フリーカメラなら何もせず、ロック時は現在の軸の向きへ滑らかに回す。 |
| `setFollowPlayerRotationDirectionEnabledOnLockedCameraPausedState(bool state)` | `followPlayerRotationDirectionEnabledOnLockedCameraPaused` を設定するだけ。 |
| `setCanActivateLookAtTargetEnabledState(bool state)` | `canActivateLookAtTargetEnabled` を設定するだけ。 |
| `setMoveCameraPositionWithMouseWheelActiveState(bool state)` | `moveCameraPositionWithMouseWheelActive` を設定するだけ。 |
| `setOriginalMoveCameraPositionWithMouseWheelActiveState()` | マウスホイールでの距離変更を保存された初期値へ戻す。 |
| `moveCameraCloserOrFartherFromPlayer(bool movingDirection)` | ホイールでカメラ距離を前後させ、必要ならホイール状態の切替や一人称への移行まで行う。`movingDirection` で方向を指定。 |
| `disableStrafeModeActivateFromNoTargetsFoundActive()` | `strafeModeActivateFromNoTargetsFoundActive` を false にするだけ。 |
| `playerIsBusy()` | デバイス/サブメニュー/プレイヤーメニューのいずれかが使用中なら true を返す。 |
| `isUsingRegularGravity()` | `playerControllerManager.isUsingRegularGravity` に委譲する。 |
| `setCheckToKeepAfterAimingFromShootingState(bool state)` | `checkToKeepAfterAimingFromShooting` を設定するだけ。 |
| `setAimingFromShootingState(bool state)` | `aimingFromShooting` を設定するだけ。 |
| `isTemporalCameraViewToLockedCameraActive()` | `temporalCameraViewToLockedCameraActive` を返すだけ。 |
| `inputChangeCameraView()` | 入力による視点変更。フリー/ロックカメラの一時切替やFBA・一人称の切替を条件に応じて行う。 |
| `inputToogleCameraRotationInputState()` | カメラ操作入力が有効なら `cameraRotationInputEnabled` を反転する。 |
| `inputMoveCamerAway()` | フリーカメラで使用可かつ設定が有効なら `moveAwayCamera` でカメラを引く。 |
| `inputLookAtTarget()` | フリー時はロックオンを切替え、ロックカメラ時は手動ロックオンやカーソル表示を切替える。 |
| `activateShowCameraCursorWhenNotAimingState()` | 非エイム時のカーソル表示を有効にし、ロックカメラのカーソルと注視先を設定する。 |
| `inputCheckActivateStrafeModeIfNoTargetsToLookFound()` | フリー三人称で注視対象がない場合にストレイフモードの有効/無効を切替える。 |
| `inputZoom()` | フリー時は `setZoom` でFOVズーム、ロックカメラ時は `zoomValue` へFOVを変更する。 |
| `inputMoveSetRotateToLeftState(bool keyDown)` | 無重力モードのフリーカメラで、押下に応じ前方回転値を1または0にする。 |
| `inputMoveSetRotateToRightState(bool keyDown)` | 無重力モードのフリーカメラで、押下に応じ前方回転値を-1または0にする。 |
| `inputResetCameraRotation()` | カメラ操作入力が有効なら `resetCameraRotation` を呼ぶ。 |
| `inputRotateLockedCameraToRight(bool holdingButton)` | ロックカメラ時に左右回転入力が無視されていなければ、右回転を設定する。 |
| `inputRotateLockedCameraToLeft(bool holdingButton)` | ロックカメラ時に左右回転入力が無視されていなければ、左回転を設定する。 |
| `inputToggleLockedCameraRotation()` | ロックカメラの回転トグル設定が有効なら `lockedCameraRotationInputToggleActive` を反転する。 |
| `inputMoveCameraCloserOrFartherFromPlayer(bool movingDirection)` | カメラ操作入力が有効なとき `moveCameraCloserOrFartherFromPlayer` に委譲する。 |
| `inputEnableOrDisableRightLean(bool state)` | カメラ操作入力とリーン入力が有効なとき `enableOrDisableRightLean` に委譲する。 |
| `inputToggleRightLean()` | 左リーン中なら解除し、`leanActive` の反転値で右リーンを切替える。 |
| `inputEnableOrDisableLeftLean(bool state)` | カメラ操作入力とリーン入力が有効なとき `enableOrDisableLeftLean` に委譲する。 |
| `inputToggleLeftLean()` | 右リーン中なら解除し、`leanActive` の反転値で左リーンを切替える。 |
| `inputSetExtraCameraRotation()` | 設定が有効でフリーカメラ使用可なら `setExtraRotationToCamera` を呼ぶ。 |
| `inputMoveLockedCameraZoomOn()` | `inputMoveLockedCameraZoom(true)` を呼ぶだけ。 |
| `inputMoveLockedCameraZoomOff()` | `inputMoveLockedCameraZoom(false)` を呼ぶだけ。 |
| `inputMoveLockedCameraZoom(bool moveForward)` | フリー以外のとき、移動ズーム値を `zoomByMovingCameraAmount` 分だけ加減算する。 |
| `enableOrDisableRightLean(bool state)` | 右リーンの状態を設定し、有効時は `setLeanState` でカメラの親を切替える。 |
| `enableOrDisableLeftLean(bool state)` | 左リーンの状態を設定し、有効時は `setLeanState` でカメラの親を切替える。 |
| `isLeanActive()` | `leanActive` かリーン解除待ちフラグが true なら true を返す。 |
| `enableOrDisableLeanInput(bool state)` | `leanInputEnabled` を設定するだけ。 |
| `disableLean()` | `leanActive` と障害物検知を false にし、ピボット復帰フラグを立てる。 |
| `setLeanState()` | FBA中は何もせず、リーン用ピボットの高さを設定してピボットカメラをその子へ移す。 |
| `removeMainCameraPivotFromLeanPivot()` | FBA中は何もせず、ピボットカメラを `playerCameraTransform` の子へ戻す。 |
| `updateCurrentMousWheelCameraState(int newIndex)` | 指定インデックスのホイール状態へ移行し、イベント発火とカメラステート設定を行う。 |
| `updateCurrentMouseWheelCameraStateByDistance()` | 現在のカメラ距離が範囲内に入るホイール状態をカレントに設定する。 |
| `resetCameraRotation()` | フリー三人称で使用可なら `resetingCameraActive` を立て、回転リセットを要求する。 |
| `setFullBodyAwarenessEnabled(bool state)` | `fullBodyAwarenessEnabled` を設定するだけ。 |
| `setVehicleCameraMovementCoroutine(Coroutine cameraMovement)` | `vehicleCameraMovementCoroutine` を保持するだけ。 |
| `getVehicleCameraMovementCoroutine()` | `vehicleCameraMovementCoroutine` を返すだけ。 |
| `getCameraList()` | `cameraList` を返すだけ。 |
| `updateCameraList()` | 有効な各カメラを一度無効化して再度有効化し、描画の更新を促す。 |
| `getMainCanvasSizeDelta()` | `mainCanvasSizeDelta` を返すだけ。 |
| `isUsingScreenSpaceCamera()` | `usingScreenSpaceCamera` を返すだけ。 |
| `setFirstOrThirdPersonInEditor(bool state)` | `state` に応じて一人称/三人称のエディタ用イベントを発火する。 |
| `setThirdPersonInEditor()` | `setThirdPersonInEditorEvent` を発火するだけ。 |
| `setFirstPersonInEditor()` | `setFirstPersonInEditorEvent` を発火するだけ。 |
| `toggleViewOnEditor()` | `firstPersonActive` の反転値を `setFirstOrThirdPersonInEditor` に渡す。 |
| `setCameraPositionOffsetActiveState(bool state, Vector3 newOffset, float newSpeed)` | カメラ位置オフセットの有効/無効と、オフセット値・補間速度を設定する。 |
| `setCameraNoiseState(string cameraNoiseName)` | 名前が一致するノイズ状態を選び、`tick` を乱数化してノイズを有効化する。 |
| `disableCameraNoiseState()` | `cameraNoiseActive` を false にするだけ。 |
| `setResetCameraRotationAfterTimeState(bool state)` | `resetCameraRotationAfterTime` を設定するだけ。 |
| `setUseSmoothCameraFollowState(bool state)` | `useSmoothCameraFollow` を設定するだけ。 |
| `setOriginalUseSmoothCameraFollowState()` | `originalUseSmoothCameraFollowValue` でスムーズフォロー設定を戻す。 |
| `activateUseSmoothCameraFollowStateDuration(float duration)` | スムーズフォローを有効化し、`duration` 後に速度を減衰させて元の設定へ戻す。 |
| `setMovingInsideVehicleState(bool state)` | 車内移動フラグを設定し、降車時は床法線に合わせた回転リセットを開始する。 |
| `setUsingGenericModelActiveState(bool state)` | `usingGenericModelActive` を設定するだけ。 |
| `isMovingInsideVehicle()` | `movingInsideVehicle` を返すだけ。 |
| `takeCapture()` | `mainCameraCaptureSystem` があれば `mainCamera` でキャプチャを実行する。 |
| `addNewLockedCameraSystemToLevel()` | ロックカメラシステムのプレハブを原点に生成し、エディタで選択状態にする。 |
| `addNewLockedCameraLimitSystemToLevel()` | ロックカメラの範囲制限プレハブを原点に生成し、エディタで選択状態にする。 |
| `addNewLockedCameraPrefabTypeLevel(int cameraIndex)` | 指定インデックスのロックカメラプレハブを生成し、未設定なら警告を出力する。 |
| `setTemporalLockedCameraPrefabNameToPlaceOnSceneFromEditor(string newLockedCameraPrefabName)` | 配置用に保持するロックカメラ名を更新し、`updateComponent` を呼ぶ。 |
| `setTemporalLockedCameraPrefabToPlaceOnSceneFromEditor()` | 保持した名前のプレハブを生成し、そのロックカメラにプレイヤーを開始位置として割当てる。 |
| `setFullBodyAwarenessEnabledFromEditor(bool state)` | FBA有効フラグを設定して `updateComponent` を呼ぶ。 |
| `setReverseVerticalAccelerometerStateFromEditor(bool state)` | 縦アクセラレータ反転を設定して `updateComponent` を呼ぶ。 |
| `setReverseHorizontalAccelerometerStateFromEditor(bool state)` | 横アクセラレータ反転を設定するだけで、`updateComponent` は呼ばない。 |
| `updateCameraStateValuesOnEditor(int stateIndex)` | 指定ステートのコピーを作成し、`lerpState` として保持する。 |
| `setMoveCameraPositionWithMouseWheelActiveStateFromEditor(bool state)` | ホイール距離変更の設定を反映して `updateComponent` を呼ぶ。 |
| `enableOrDisableChangeCameraViewFromEditor(bool state)` | 視点変更の有効状態を設定して `updateComponent` を呼ぶ。 |
| `setCanActivateLookAtTargetEnabledStateFromEditor(bool state)` | ロックオン有効フラグを設定して `updateComponent` を呼ぶ。 |
| `setResetCameraRotationAfterTimeStateFromEditor(bool state)` | 時間経過リセット設定を反映して `updateComponent` を呼ぶ。 |
| `setZoomEnabledStateFromEditor(bool state)` | ズーム有効状態を設定して `updateComponent` を呼ぶ。 |
| `updateComponent()` | `GKC_Utils.updateComponent` と `updateDirtyScene` でコンポーネントとシーンを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartMovingLockedCamera` | `UnityEvent` | – |
| `eventOnKeepMovingLockedCamera` | `UnityEvent` | – |
| `eventOnStopMovingLockedCamera` | `UnityEvent` | – |
| `setThirdPersonInEditorEvent` | `UnityEvent` | – |
| `setFirstPersonInEditorEvent` | `UnityEvent` | – |
| `setThirdPersonEvent` | `UnityEvent` | – |
| `setFirstPersonEvent` | `UnityEvent` | – |
| `eventOnEnableFBA` | `UnityEvent` | – |
| `eventOnDisableFBA` | `UnityEvent` | – |
| `eventOnEnableFBAInEditor` | `UnityEvent` | – |
| `eventOnDisableFBAInEditor` | `UnityEvent` | – |
| `eventToActivateHeadColliderOnFBA` | `UnityEvent` | – |
| `eventToDeactivateHeadColliderOnFBA` | `UnityEvent` | – |
| `eventToActivateHeadColliderOnFBAOnEditor` | `UnityEvent` | – |
| `eventToDeactivateHeadColliderOnFBAOnEditor` | `UnityEvent` | – |
| `eventOnLockOnStart` | `UnityEvent` | – |
| `eventOnLockOnEnd` | `UnityEvent` | – |
| `eventOnLockAtTargetStart` | `UnityEvent` | – |
| `eventOnLockAtTargetEnd` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`changeCameraFov(bool state)`, `checkActivateOrDeactivateHeadColliderOnFBA(bool state)`, `checkResetLeanState(bool resetPivotCameraTransform)`, `crouch(bool isCrouching)`, `getCurrentTargetToLook()`, `getLastTimeMoved()`, `getLockedCameraTransform()`, `getOriginalCameraFov()`, `getOriginalLockedCameraPivotPosition()`, `getPivotCameraTransform()`, `getSplineForPlayerPosition(Vector3 playerPosition)`, `getSplineForwardDirection(Vector3 playerPosition)`, `is2_5ViewActive()`, `isFirstPersonActive()`, `isFullBodyAwarenessEnabled()`, `isLookintAtTargetByInput()`, `isMoveInXAxisOn2_5d()`, `isPlayerLookingAtTarget()`, `isShowCameraCursorWhenNotAimingActive()`, `istargetToLookLocated()`, `resetPivotCameraTransformLocalRotation()`, `setDrivingState(bool state)`, `setFBAPivotCameraTransformActiveState(bool state)`, `setFBAPivotTransformParentFromPlayer(Transform newParent)`, `setHeadColliderStateOnFBA(bool state)`, `setMainCameraFovStartAndEnd(float startTargetValue, float endTargetValue, float speed)`, `setMoveInXAxisOn2_5dState(bool state)`, `setPivotCameraTransformOriginalParent()`, `setPivotCameraTransformParentCurrentTransformToFollow()`, `setPlayerAndCameraParent(Transform newParent)`, `setShakeCameraState(bool state, string stateName)`, `setUpdatePlayerCameraPositionOnFixedUpdateActiveState(bool state)`, `setUpdatePlayerCameraPositionOnLateUpdateActiveState(bool state)`, `startOrStopUpdatePivotPositionOnFBA(bool state)`, `stopShakeCamera()`

</details>

## 内部型

- `typeOfCamera`（enum）
- `sideToAim`（enum）
- `cameraRotationType`（enum）
- `cameraSettings`（class）
- `FocusArea`（struct）
- `cameraMouseWheelStates`（class）
- `lockedCameraPrefabsTypes`（class）
- `cameraNoiseState`（class）
- `cameraStateEventInfo`（class）
- `customReticleInfo`（class）
