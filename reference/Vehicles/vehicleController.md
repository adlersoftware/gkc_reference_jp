# vehicleController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/Vehicle Controllers/vehicleController.cs:6`

**概要**: 車両操作の基底コントローラーで、搭乗中の入力を読み取り、ブースト・燃料・エンジンON/OFF・2.5D回転・ホバーボードのウェイポイント移動を扱う。派生コントローラー向けに多くのメソッドが空の仮想関数として用意されている。

**公式ドキュメント抜粋**（[NWH Vehicle Physics 2](../../docs/integrations/current-integrations/nwh-vehicle-physics-2.md)）

> This page covers the integration of NWH Vehicle Physics 2 and Game Kit Controller <figure<img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F0t4D1U4uEbMrfFcZQ7hQ%2Fimage.png?alt=media token=6e436931-55da-470d-9779-c45ced02c5ca" alt=""<figcaption</figcaption</figure NWH Vehicle Physics 2 is a complete vehicle simulation package for Unity. Realistic, easy to use, and heavily customizable. • Easy and fast to set up with all the defaults loaded automatically and a validation system that warns the developer about any setup issues. • Vehicle setup wizard that creates a functional vehicle from scratch in a few clicks. Multiple presets are available. • Modular vehicle architecture. Enable or disable parts of the vehicle as they are needed, either manually or through the built-in LOD system. • Powertrain solver that fea…

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Update Vehicle State Enabled | `updateVehicleStateEnabled` | `bool` | – | – |
| Call Vehicle Update Each Frame | `callVehicleUpdateEachFrame` | `bool` | true | – |
| Call Vehicle Fixed Update Each Frame | `callVehicleFixedUpdateEachFrame` | `bool` | true | – |
| Update Passengers Angular Direction | `updatePassengersAngularDirection` | `bool` | – | – |
| Use Horizontal Input Lerp | `useHorizontalInputLerp` | `bool` | true | – |

### Vehicle Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Controller Settings | `vehicleControllerSettings` | `vehicleControllerSettingsInfo` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Update2 5d Input Enabled | `update2_5dInputEnabled` | `bool` | true | – |
| Ignore Vertical Input On2 5d | `ignoreVerticalInputOn2_5d` | `bool` | – | – |
| Keep Velocity On Change Of Direction On2 5d View | `keepVelocityOnChangeOfDirectionOn2_5dView` | `bool` | – | – |
| Force Vehicle Rotation To2 5d View Direction | `forceVehicleRotationTo2_5dViewDirection` | `bool` | true | – |
| Update2 5d Rotation Left Or Right Enabled | `update2_5dRotationLeftOrRightEnabled` | `bool` | true | – |
| Update Only Right Axis Rotation On2 5d | `updateOnlyRightAxisRotationOn2_5d` | `bool` | – | – |
| Set3d Wolrd State On Getting Off | `set3dWolrdStateOnGettingOff` | `bool` | – | – |

### Hoverboard-Rail Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Hoverboard Waypoints Enabled | `useHoverboardWaypointsEnabled` | `bool` | – | – |
| Hoverboard Waypoints Extra Rotation | `hoverboardWaypointsExtraRotation` | `float` | – | – |
| Use Custom Hoverboard Center Point | `useCustomHoverboardCenterPoint` | `bool` | – | – |
| Custom Hoverboard Center Point | `customHoverboardCenterPoint` | `Vector3` | – | – |
| Use Hoverboard Jump Clamp | `useHoverboardJumpClamp` | `bool` | – | – |
| Hoverboard Jump Force | `hoverboardJumpForce` | `float` | 500 | – |
| Hoverboard Jump Clamp | `hoverboardJumpClamp` | `float` | 50 | – |
| Reset Vehicle Transform Rotation After Hoverboard | `resetVehicleTransformRotationAfterHoverboard` | `bool` | – | – |
| Reset Vehicle Transform Rotation Speed | `resetVehicleTransformRotationSpeed` | `float` | 10 | – |
| Reset Vehicle Transform Rotation To Identity | `resetVehicleTransformRotationToIdentity` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Driving | `driving` | `bool` | – | – |
| Is Turned On | `isTurnedOn` | `bool` | – | – |
| Vehicle Destroyed | `vehicleDestroyed` | `bool` | – | – |
| Using Gravity Control | `usingGravityControl` | `bool` | – | – |
| Braking | `braking` | `bool` | – | – |
| Using Impulse | `usingImpulse` | `bool` | – | – |
| Jump Input Pressed | `jumpInputPressed` | `bool` | – | – |
| Current Normal | `currentNormal` | `Vector3` | – | – |
| Last Time Jump | `lastTimeJump` | `float` | – | – |
| Current Speed | `currentSpeed` | `float` | – | – |
| Autobrake Active | `autobrakeActive` | `bool` | – | – |
| Using Hover Board Waypoint | `usingHoverBoardWaypoint` | `bool` | – | – |
| Last Time Released From Waypoint | `lastTimeReleasedFromWaypoint` | `float` | – | – |
| Way Points Manager | `wayPointsManager` | `hoverBoardWayPoints` | – | – |
| Camera Type Free | `cameraTypeFree` | `bool` | – | – |
| Player Moving On3d World | `playerMovingOn3dWorld` | `bool` | – | – |
| Move In X Axis On2 5d | `moveInXAxisOn2_5d` | `bool` | – | – |
| Pause Update2 5d Rotation To Left Or Right By Input Debug | `pauseUpdate2_5dRotationToLeftOrRightByInputDebug` | `bool` | – | – |
| Pause Update2 5d Rotation To Left Or Right Debug | `pauseUpdate2_5dRotationToLeftOrRightDebug` | `bool` | – | – |
| Ignore To Turn On Or Off Input Active | `ignoreToTurnOnOrOffInputActive` | `bool` | – | – |
| Moving Backwards | `movingBackwards` | `bool` | – | – |

### Debug Input

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Horizontal Axis | `horizontalAxis` | `float` | 0 | – |
| Vertical Axis | `verticalAxis` | `float` | 0 | – |
| Axis Values | `axisValues` | `Vector2` | – | – |
| Raw Axis Values | `rawAxisValues` | `Vector2` | – | – |
| Motor Input | `motorInput` | `float` | – | – |
| Moving | `moving` | `bool` | – | – |
| Using Boost | `usingBoost` | `bool` | – | – |
| Boost Input | `boostInput` | `float` | 1 | – |
| Touch Platform | `touchPlatform` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Vehicle HUD Manager | `mainVehicleHUDManager` | `vehicleHUDManager` | – | – |
| Main Vehicle Camera Controller | `mainVehicleCameraController` | `vehicleCameraController` | – | – |
| Main Vehicle Gravity Control | `mainVehicleGravityControl` | `vehicleGravityControl` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Main IK Driving System | `mainIKDrivingSystem` | `IKDrivingSystem` | – | – |
| Main Input Action Manager | `mainInputActionManager` | `inputActionManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `InitializeAudioElements()` | – |
| `checkCameraType()` | 車両カメラからカメラ種別・3D/2.5D・X軸移動の状態を取得し各フラグに保持する。 |
| `vehicleUpdate()` | 運転入力を読み取り、ブースト・燃料・2.5D回転・後退判定まで毎フレーム更新する。 |
| `update2_5DState()` | 2.5Dでカメラ軸方向へ位置を補正し、左右入力で車両の向きを切り替える。 |
| `updateCameraSteerState()` | カメラ視線方向から操舵値`steering`を求め`horizontalAxis`に反映する。 |
| `updateMovingState()` | `verticalAxis`が0以外なら`moving`をtrueにするだけ。 |
| `vehicleFixedUpdate()` | 本体が空で何もしない。 |
| `setCollisionDetected(Collision currentCollision)` | 本体が空で何もしない。 |
| `startBrakeVehicleToStopCompletely()` | 本体が空で何もしない。 |
| `endBrakeVehicleToStopCompletely()` | 本体が空で何もしない。 |
| `changeVehicleState()` | `driving`を反転し、自動エンジンON/OFFと重力制御の状態も切り替える。 |
| `passengerGettingOnOff()` | 本体が空で何もしない。 |
| `checkVehicleStateOnPassengerGettingOnOrOff(bool state)` | 本体が空で何もしない。 |
| `fixDestroyedVehicle()` | 破壊状態なら`vehicleDestroyed`をfalseにして自身を再度有効化する。 |
| `disableVehicle()` | `vehicleDestroyed`を立ててエンジンを切り、自身を無効化する。 |
| `getCurrentSpeed()` | 基底の既定値として常に100を返すだけ。 |
| `getMaxForwardSpeed()` | 設定`vehicleControllerSettings`の最高速度を返すだけ。 |
| `inputJump()` | 運転中かつジャンプ可能なら`jumpInputPressed`をtrueにする。 |
| `inputHoldOrReleaseJump(bool holdingButton)` | 前回ジャンプから0.2秒を超えた長押しで`usingImpulse`を有効化し、離すと解除する。 |
| `inputHoldOrReleaseTurbo(bool holdingButton)` | 押下でブーストとカメラ演出を有効化し、離すと停止して`boostInput`を1に戻す。 |
| `inputSetTurnOnState()` | 運転中でエンジン切替可能なら`setEngineOnOrOffState`を呼ぶ。 |
| `inputHorn()` | 運転中なら`pressHorn`でクラクションを鳴らす。 |
| `inputHoldOrReleaseBrake(bool holdingButton)` | 運転中に`braking`をボタン状態に合わせるだけ。 |
| `isBrakeActive()` | `braking`またはハンドブレーキ入力が有効ならtrueを返す。 |
| `pressHorn()` | `mainVehicleHUDManager`のクラクション再生を呼ぶだけ。 |
| `setAudioState(AudioElement source, float distance, float volume, bool loop, bool play, bool stop)` | 音源の距離・音量・ループ・空間ブレンドを設定し、指定に応じて再生・停止する。 |
| `setIgnoreToTurnOnOrOffInputActiveState(bool state)` | `ignoreToTurnOnOrOffInputActive`を設定するだけ。 |
| `setEngineOnOrOffState()` | 燃料があれば`turnOnOrOff`でエンジン状態を反転する。 |
| `turnOnOrOff(bool state, bool previouslyTurnedOn)` | `isTurnedOn`を設定してON/OFF処理を呼ぶが、破壊中はONにしない。 |
| `setTurnOnState()` | 本体が空で何もしない。 |
| `setTurnOffState(bool previouslyTurnedOn)` | 入力値とブーストを初期化し、カメラ演出の停止と`usingImpulse`解除を行う。 |
| `changeGravityControlUse(bool state)` | `usingGravityControl`を設定し`usingImpulse`を解除する。 |
| `setNormal(Vector3 normalValue)` | `currentNormal`を設定するだけ。 |
| `getNormal()` | `currentNormal`を返すだけ。 |
| `usingBoosting()` | 本体が空で何もしない。 |
| `isUseOfGravityActive()` | 重力制御コンポーネントの`useGravity`を返すだけ。 |
| `isDrivingActive()` | `driving`を返すだけ。 |
| `isPlayerUsingInput()` | 生入力軸が0以外ならtrueを返す。 |
| `isCameraTypeFree()` | `cameraTypeFree`を返すだけ。 |
| `isPlayerMovingOn3dWorld()` | `playerMovingOn3dWorld`を返すだけ。 |
| `isMovingBackwards()` | 速度方向が前方向と90度を超えると`movingBackwards`をtrueにして返す。 |
| `getLastLookingInRightDirectionOn2_5d()` | 2.5Dで最後に向いた右方向を返し、未設定なら軸方向を返す。 |
| `getCurrentNormal()` | 重力制御コンポーネントの現在の法線を返す。 |
| `setNewMainCameraTransform(Transform newTransform)` | 本体が空で何もしない。 |
| `setNewPlayerCameraTransform(Transform newTransform)` | 本体が空で何もしない。 |
| `setUseForwardDirectionForCameraDirectionState(bool state)` | 本体が空で何もしない。 |
| `setUseRightDirectionForCameraDirectionState(bool state)` | 本体が空で何もしない。 |
| `setAddExtraRotationPausedState(bool state)` | 本体が空で何もしない。 |
| `activateAutoBrakeOnGetOff()` | `braking`と`autobrakeActive`をtrueにして降車時の自動ブレーキを開始する。 |
| `checkAutoBrakeOnGetOffState()` | 自動ブレーキ中に速度が0.5未満なら`braking`とフラグを解除する。 |
| `isVehicleOnGround()` | 常にfalseを返すだけ。 |
| `canUseHoverboardWaypoints()` | `useHoverboardWaypointsEnabled`を返すだけ。 |
| `getLastTimeReleasedFromWaypoint()` | `lastTimeReleasedFromWaypoint`を返すだけ。 |
| `isUsingHoverBoardWaypoint()` | `usingHoverBoardWaypoint`を返すだけ。 |
| `enterOrExitFromWayPoint(bool state)` | ウェイポイント乗降で重力制御とRigidbodyのキネマティックを切り替え、解放時刻を記録する。 |
| `receiveWayPoints(hoverBoardWayPoints wayPoints)` | `wayPointsManager`にウェイポイントを設定するだけ。 |
| `getMotorInput()` | `motorInput`を返すだけ。 |
| `getHorizontalAxis()` | `horizontalAxis`を返すだけ。 |
| `getVerticalAxis()` | `verticalAxis`を返すだけ。 |
| `getPlayerMouseAxis()` | 入力管理コンポーネントのマウス軸をそのまま返す。 |
| `getPlayerMovementAxis()` | 入力管理コンポーネントの移動軸をそのまま返す。 |
| `resetVehicleTransformRotation()` | 既存の回転コルーチンを止め、回転リセット用コルーチンを開始する。 |
| `resetVehicleTransformRotationCoroutine()` | 法線に合わせた向き（またはidentity）へ`Slerp`で徐々に回転させる。 |
| `pickOrReleaseHoverboardVehicle(bool state, bool auto)` | ウェイポイント乗降を切り替え、カメラ追従の停止や終端での勢い付与を行う。 |
| `activeHoverboardMovement()` | 既存コルーチンを止めてウェイポイント移動コルーチンを開始する。 |
| `stopMoveThroughWayPointsCoroutine()` | 移動コルーチンがあれば停止するだけ。 |
| `getVehicleComponents(GameObject mainVehicleObject)` | 指定オブジェクトからHUD・カメラ・重力・Rigidbody・IK等の参照を取得し保持する。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`Awake()`, `Start()`

</details>

## 内部型

- `vehicleControllerSettingsInfo`（class）
