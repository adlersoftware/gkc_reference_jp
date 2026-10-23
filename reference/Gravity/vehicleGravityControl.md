# vehicleGravityControl

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `gravityObjectManager`
- **ソース**: `Gravity/vehicleGravityControl.cs:5`

**概要**: 車両用の重力制御で、カメラ方向へのサーフェス探索・法線への回転・親設定・重力値の一時変更を扱う。`gravityObjectManager`を継承する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Gravity | `useGravity` | `bool` | true | – |
| Gravity Force | `gravityForce` | `float` | 9.8f | – |
| Search New Surface On High Fall Speed | `searchNewSurfaceOnHighFallSpeed` | `bool` | true | – |
| Check Surface Below On Regular State | `checkSurfaceBelowOnRegularState` | `bool` | – | – |
| Time To Set Null Parent On Air | `timeToSetNullParentOnAir` | `float` | 0.5f | – |
| Change Driver Gravity When Gets Off | `changeDriverGravityWhenGetsOff` | `bool` | true | – |
| Set Vehicle Regular Gravity On Driver Get Off | `setVehicleRegularGravityOnDriverGetOff` | `bool` | – | – |

### Circumnavigation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Circumnavigate Rotation Speed | `circumnavigateRotationSpeed` | `float` | 10 | – |
| Circumnavigate Current Surface Active | `circumnavigateCurrentSurfaceActive` | `bool` | – | – |
| Use Lerp Rotation | `useLerpRotation` | `bool` | – | – |
| Check Surface Below Ledge | `checkSurfaceBelowLedge` | `bool` | – | – |
| Surface Below Ledge Raycast Distance | `surfaceBelowLedgeRaycastDistance` | `float` | 3 | – |
| Below Ledge Rotation Speed | `belowLedgeRotationSpeed` | `float` | 10 | – |
| Min Angle Difference To Adhere To Surface | `minAngleDifferenceToAdhereToSurface` | `float` | 4 | – |

### Current Normal/Gravity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Regular Gravity | `regularGravity` | `Vector3` | new Vector3 (0, 1, 0) | – |
| Current Normal | `currentNormal` | `Vector3` | new Vector3 (0, 1, 0) | – |

### Gravity At Start Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Start With New Gravity | `startWithNewGravity` | `bool` | – | – |
| Use Vehicle Rotation | `useVehicleRotation` | `bool` | – | – |
| Adjust Rotation To Surface Found | `adjustRotationToSurfaceFound` | `bool` | – | – |
| New Gravity To Start | `newGravityToStart` | `Vector3` | – | – |

### Shake Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shake Camera On High Fall Speed | `shakeCameraOnHighFallSpeed` | `bool` | true | – |
| Min Speed To Shake Camera | `minSpeedToShakeCamera` | `float` | 10 | – |
| Camera Shake Can Be Used | `cameraShakeCanBeUsed` | `bool` | true | – |

### Others Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Settings | `settings` | `otherSettings` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Gravity Control Enabled | `gravityControlEnabled` | `bool` | – | – |
| On Ground | `OnGround` | `bool` | – | – |
| Gravity Power Active | `gravityPowerActive` | `bool` | – | – |
| Power Activated | `powerActivated` | `bool` | – | – |
| Recalculating Surface | `recalculatingSurface` | `bool` | – | – |
| Searching Surface | `searchingSurface` | `bool` | – | – |
| Searching New Surface Below | `searchingNewSurfaceBelow` | `bool` | – | – |
| Search Around | `searchAround` | `bool` | – | – |
| Rotating | `rotating` | `bool` | – | – |
| Circumnavigable Surface Found | `circumnavigableSurfaceFound` | `bool` | – | – |
| Use Center Point Active | `useCenterPointActive` | `bool` | – | – |
| Current Center Point | `currentCenterPoint` | `Transform` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Gravity Adherence Raycast Parent | `gravityAdherenceRaycastParent` | `Transform` | – | – |
| Surface Below Raycast Transform | `surfaceBelowRaycastTransform` | `Transform` | – | – |
| Main Vehicle Controller | `mainVehicleController` | `vehicleController` | – | – |
| Gravity Center Collider | `gravityCenterCollider` | `Collider` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Vehicle Camera Manager | `vehicleCameraManager` | `vehicleCameraController` | – | – |
| HUD Manager | `HUDManager` | `vehicleHUDManager` | – | – |
| Action Manager | `actionManager` | `inputActionManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCollisionDetected(Collision currentCollision)` | サーフェス探索中に衝突点から進行方向を求め、周囲の探索を停止する。 |
| `setFatherDetectedAsParent()` | `fatherDetected`を車両とカメラの親に設定する。 |
| `setNullParent()` | 車両とカメラの親を`null`にする。 |
| `activateGravityPower(Vector3 dir, Vector3 right)` | `dir`方向へサーフェス探索を開始し、親解除・コライダー有効化・カメラ揺れ・車両側の重力制御を有効にする。 |
| `deactivateGravityPower()` | 探索中か法線が通常と異なる場合に解除し、通常法線へ回転して速度とカメラ揺れを戻す。 |
| `changeGravityControlState(bool state)` | 重力制御の有効フラグを設定し、無効かつ空中なら重力パワーを解除する。 |
| `rotateToSurface(Vector3 normal, int rotSpeed)` | 車両とカメラを法線方向へ補間回転し、通常時は元の速度を復元するコルーチン。 |
| `setUseCenterPointActiveState(bool state, Transform newCenterPoint)` | 中心点の使用フラグとTransformを設定するだけ。 |
| `rotateVehicleToRaycastDirection(Vector3 raycastDirection)` | レイキャストで新サーフェスを探し、見つかれば速度を止めて接地回転や親設定を行う。 |
| `rotateVehicleToLandSurface(Vector3 hitNormal)` | 既存の回転コルーチンを止め、着地法線への回転コルーチンを開始する。 |
| `rotateVehicleToLandSurfaceCoroutine(Vector3 hitNormal)` | 車両とカメラを法線へ補間回転し、下向き速度を加えて着地させる。 |
| `getCurrentCameraPivot(Transform newPivot)` | カメラピボットを設定するだけ。 |
| `pauseDownForce(bool state)` | 下向き力(`useGravity`)を`state`の否定に設定するだけ。 |
| `setCustomNormal(Vector3 normal)` | 補間なしで車両とカメラを指定法線の向きへ即座に回転させる。 |
| `getGravityForce()` | 現在の重力値を返す。 |
| `setNewGravityForce(float newValue)` | 重力値を設定するだけ。 |
| `setOriginalGravityForce()` | 重力値を保存しておいた元の値へ戻す。 |
| `getRegularGravity()` | 通常重力の法線`regularGravity`を返す。 |
| `updateCurrentNormalExternally(Vector3 newValue)` | 現在の法線を外部から設定するだけ。 |
| `changeDriverGravityWhenGetsOffActive()` | 降車時にドライバーの重力を変更する設定値を返す。 |
| `isSetVehicleRegularGravityOnDriverGetOffActive()` | 降車時に車両を通常重力へ戻す設定値を返す。 |
| `setGravityForcePausedState(bool state)` | 重力値の一時停止フラグを設定するだけ。 |
| `isGravityPowerActive()` | 重力パワーが有効か返す。 |
| `isGravityControlEnabled()` | 重力制御が有効か返す。 |
| `inputEnableOrDisableGravityControl(bool enableGravityControl)` | 破壊済みや3D移動でない場合は無視し、可能ならピボット方向で重力制御を開始/解除する。 |
| `inputIncreasOrDecreaseGravitySpeed(bool increaseGravitySpeed)` | 探索中のみ加速フラグを切替え、カメラ揺れを加速用か通常用に切替える。 |
| `setCheckDownSpeedActiveState(bool state)` | 下向き速度チェックのフラグを設定するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`getCurrentNormal()`, `isUsingRegularGravity()`

</details>

## 内部型

- `otherSettings`（class）
