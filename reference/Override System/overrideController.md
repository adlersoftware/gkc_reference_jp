# overrideController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Override System/overrideController.cs:5`

**概要**: Rigidbodyを操作するためのオーバーライド用コントローラ。カメラ方向の入力で移動・ジャンプ・ブレーキ・ダッシュを行い、対象メッシュの親子付けも扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Move Speed Multiplier | `moveSpeedMultiplier` | `float` | – | – |
| Air Control Amount | `airControlAmount` | `float` | – | – |
| Jump Power | `jumpPower` | `float` | – | – |
| Can Jump | `canJump` | `bool` | – | – |
| Brake Force | `brakeForce` | `float` | 5 | – |
| Time To Jump On Colliding Exit | `timeToJumpOnCollidingExit` | `float` | 0.4f | – |
| Layer Mask | `layerMask` | `LayerMask` | – | – |
| Raycast Distance | `raycastDistance` | `float` | – | – |

### Angular Velocity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Angular Velocity | `useAngularVelocity` | `bool` | – | – |
| Angular Velocity Rotation Speed | `angularVelocityRotationSpeed` | `float` | 100 | – |
| Angular Velocity Rotation Lerp Speed | `angularVelocityRotationLerpSpeed` | `float` | 5 | – |
| Apply Force On Angular Velocity | `applyForceOnAngularVelocity` | `bool` | – | – |
| Force Multiplier On Angular Velocity | `forceMultiplierOnAngularVelocity` | `float` | – | – |

### Run Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Run | `canRun` | `bool` | – | – |
| Run Speed | `runSpeed` | `float` | – | – |

### Impulse Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Impulse | `canImpulse` | `bool` | – | – |
| Impulse Force | `impulseForce` | `float` | – | – |
| Impulse Cool Down | `impulseCoolDown` | `float` | 0.5f | – |

### Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Damage Objects Enabled | `damageObjectsEnabled` | `bool` | – | – |
| Damage Objects Multiplier | `damageObjectsMultiplier` | `float` | – | – |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Collision Force Limit | `collisionForceLimit` | `float` | – | – |
| Can Activate Reaction System Temporally | `canActivateReactionSystemTemporally` | `bool` | – | – |
| Damage Reaction ID | `damageReactionID` | `int` | -1 | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Controller Enabled | `controllerEnabled` | `bool` | – | – |
| On Ground | `onGround` | `bool` | – | – |
| Current Speed | `currentSpeed` | `float` | – | – |
| Run Active | `runActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Override Input | `overrideInput` | `overrideInputManager` | – | – |
| Override Camera Transform | `overrideCameraTransform` | `Transform` | – | – |
| Override Camera Parent Transform | `overrideCameraParentTransform` | `Transform` | – | – |
| Controller Mesh Parent | `controllerMeshParent` | `Transform` | – | – |
| Controller Mesh | `controllerMesh` | `GameObject` | – | – |
| Raycast Position | `raycastPosition` | `Transform` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`を停止するだけ。 |
| `changeControllerState(bool state)` | 制御状態を設定して入力を初期化し、Rigidbodyを停止・kinematic切替したうえで、有効時のみ更新コルーチンを開始する。 |
| `setControllerMesh(GameObject newControllerMesh)` | 操作対象メッシュを設定して指定親の下へ移動し、`parentAssignedSystem`を追加して親を割り当てる。 |
| `getControllerMesh()` | `controllerMesh`を返すだけ。 |
| `removeControllerMesh()` | メッシュを親から切り離し、`parentAssignedSystem`があれば削除する。 |
| `inputJump()` | ジャンプ可能で接地中かつ猶予時間内なら、上方向の力を外部力として設定し、次の更新で適用させる。 |
| `inputSetBrakeState(bool state)` | `state`がtrueなら接地中のみブレーキを有効にし、falseなら解除するだけ。 |
| `inputImpulse()` | クールダウン中でなければ移動方向、なければカメラ前方へのダッシュ力を設定し、次の更新で適用させる。 |
| `inputRunState(bool state)` | `canRun`が有効なら走行状態を`state`に設定するだけ。 |
