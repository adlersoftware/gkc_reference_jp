# cameraControllerManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Player Camera/cameraControllerManager.cs:5`

**概要**: プレイヤーのカメラ系コンポーネント用の基底クラスで、全メソッドが`virtual`の空実装か既定値の返却になっている。実際の挙動は派生クラスがオーバーライドして実装する。

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `isFirstPersonActive()` | 基底クラスの仮想メソッドで、常に`false`を返す。 |
| `isMoveInXAxisOn2_5d()` | 基底クラスの仮想メソッドで、常に`false`を返す。 |
| `setMoveInXAxisOn2_5dState(bool state)` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `getOriginalLockedCameraPivotPosition()` | 基底クラスの仮想メソッドで、常に`Vector3.zero`を返す。 |
| `getSplineForPlayerPosition(Vector3 playerPosition)` | 基底クラスの仮想メソッドで、引数は使わず`Vector3.zero`を返す。 |
| `getSplineForwardDirection(Vector3 playerPosition)` | 基底クラスの仮想メソッドで、引数は使わず`Vector3.zero`を返す。 |
| `changeCameraFov(bool state)` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `getPivotCameraTransform()` | 基底クラスの仮想メソッドで、常に`null`を返す。 |
| `getLockedCameraTransform()` | 基底クラスの仮想メソッドで、常に`null`を返す。 |
| `crouch(bool isCrouching)` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `setMainCameraFovStartAndEnd(float startTargetValue, float endTargetValue, float speed)` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `getOriginalCameraFov()` | 基底クラスの仮想メソッドで、常に`-1`を返す。 |
| `isPlayerLookingAtTarget()` | 基底クラスの仮想メソッドで、常に`false`を返す。 |
| `isLookintAtTargetByInput()` | 基底クラスの仮想メソッドで、常に`false`を返す。 |
| `setShakeCameraState(bool state, string stateName)` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `getLastTimeMoved()` | 基底クラスの仮想メソッドで、常に`-1`を返す。 |
| `setDrivingState(bool state)` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `is2_5ViewActive()` | 基底クラスの仮想メソッドで、常に`false`を返す。 |
| `istargetToLookLocated()` | 基底クラスの仮想メソッドで、常に`false`を返す。 |
| `setPlayerAndCameraParent(Transform newParent)` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `stopShakeCamera()` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `getCurrentTargetToLook()` | 基底クラスの仮想メソッドで、常に`null`を返す。 |
| `setUpdatePlayerCameraPositionOnLateUpdateActiveState(bool state)` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `setUpdatePlayerCameraPositionOnFixedUpdateActiveState(bool state)` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `isFullBodyAwarenessEnabled()` | 基底クラスの仮想メソッドで、常に`false`を返す。 |
| `setPivotCameraTransformParentCurrentTransformToFollow()` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `setPivotCameraTransformOriginalParent()` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `resetPivotCameraTransformLocalRotation()` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `setHeadColliderStateOnFBA(bool state)` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `setFBAPivotCameraTransformActiveState(bool state)` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `startOrStopUpdatePivotPositionOnFBA(bool state)` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `checkActivateOrDeactivateHeadColliderOnFBA(bool state)` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `checkResetLeanState(bool resetPivotCameraTransform)` | 基底クラスの空の仮想メソッドで、何もしない。 |
| `isShowCameraCursorWhenNotAimingActive()` | 基底クラスの仮想メソッドで、常に`false`を返す。 |
| `setFBAPivotTransformParentFromPlayer(Transform newParent)` | 基底クラスの空の仮想メソッドで、何もしない。 |
