# climbDetectionCollisionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/climbDetectionCollisionSystem.cs:5`

**概要**: フリークライム用の衝突判定オブジェクト。プレイヤーのコライダーの代わりに物理判定を行い、クライム面への接触状態を検出して公開する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Max Speed | `maxSpeed` | `float` | 10f | Range (0f, 100f) |
| Max Vertical Climb Speed | `maxVerticalClimbSpeed` | `float` | 4f | Range (0f, 100f) |
| Max Horizontal Climb Speed | `maxHorizontalClimbSpeed` | `float` | 4 | Range (0f, 100f) |
| Max Diagonal Up Climb Speed | `maxDiagonalUpClimbSpeed` | `float` | 4 | Range (0f, 100f) |
| Max Diagonal Down Climb Speed | `maxDiagonalDownClimbSpeed` | `float` | 4 | Range (0f, 100f) |
| Max Slide Down Climb Speed | `maxSlideDownClimbSpeed` | `float` | 6 | Range (0f, 100f) |
| Max Boost Climb Speed Multiplier | `maxBoostClimbSpeedMultiplier` | `float` | 1.5f | Range (0f, 100f) |
| Max Acceleration | `maxAcceleration` | `float` | 10f | Range (0f, 100f) |
| Max Air Acceleration | `maxAirAcceleration` | `float` | 1f | Range (0f, 100f) |
| Max Climb Acceleration | `maxClimbAcceleration` | `float` | 40f | Range (0f, 100f) |
| Max Ground Angle | `maxGroundAngle` | `float` | 25f | Range (0, 90) |
| Max Stairs Angle | `maxStairsAngle` | `float` | 50f | Range (0, 90) |
| Max Climb Angle | `maxClimbAngle` | `float` | 140f | Range (90, 170) |
| Max Snap Speed | `maxSnapSpeed` | `float` | 100f | Range (0f, 100f) |
| Probe Distance | `probeDistance` | `float` | 1f | – |
| Probe Mask | `probeMask` | `LayerMask` | -1 | – |
| Stairs Mask | `stairsMask` | `LayerMask` | -1 | – |
| Climb Mask | `climbMask` | `LayerMask` | -1 | – |
| Sphere Radius | `sphereRadius` | `float` | 0.5f | – |
| Sphere Align Speed | `sphereAlignSpeed` | `float` | 45 | – |
| Sphere Air Rotation | `sphereAirRotation` | `float` | 0.5f | – |

### Curve Speed Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Curve Speed Enabled | `useCurveSpeedEnabled` | `bool` | true | – |
| Horizontal Curve Speed | `horizontalCurveSpeed` | `float` | 0.1f | – |
| Vertical Curve Speed | `verticalCurveSpeed` | `float` | 0.1f | – |
| Diagonal Up Curve Speed | `diagonalUpCurveSpeed` | `float` | 0.1f | – |
| Diagonal Down Curve Speed | `diagonalDownCurveSpeed` | `float` | 0.1f | – |
| Climb Speed Curve | `climbSpeedCurve` | `AnimationCurve` | – | – |
| Climb Boost Speed Curve | `climbBoostSpeedCurve` | `AnimationCurve` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Any On Ground | `anyOnGround` | `bool` | – | – |
| Climb Contact Count | `climbContactCount` | `int` | – | – |
| Ground Contact Count | `groundContactCount` | `int` | – | – |
| Steep Contact Count | `steepContactCount` | `int` | – | – |
| Steps Since Last Grounded | `stepsSinceLastGrounded` | `int` | – | – |
| Climb Detection Active | `climbDetectionActive` | `bool` | – | – |
| Velocity | `velocity` | `Vector3` | – | – |
| Contact Normal | `contactNormal` | `Vector3` | – | – |
| Climb Normal | `climbNormal` | `Vector3` | – | – |
| Steep Normal | `steepNormal` | `Vector3` | – | – |
| Last Climb Normal | `lastClimbNormal` | `Vector3` | – | – |
| Current Curve Value | `currentCurveValue` | `float` | 0 | – |

### Movement Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Moving Horizontal | `movingHorizontal` | `bool` | – | – |
| Moving Vertical | `movingVertical` | `bool` | – | – |
| Moving Diagonal Up | `movingDiagonalUp` | `bool` | – | – |
| Moving Diagonal Down | `movingDiagonalDown` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Free Climb System | `mainFreeClimbSystem` | `freeClimbSystem` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Main Collider | `mainCollider` | `Collider` | – | – |
| Main Player Collider | `mainPlayerCollider` | `Collider` | – | – |
| Sphere Transform | `sphereTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateObjectPosition(Vector3 newPosition)` | `transform.position` を指定位置に設定するだけ。 |
| `enableOrDisableClimbDetection(bool state)` | 検出を切り替え、物理/コライダー、角度閾値、衝突無視、位置合わせ、更新コルーチンを設定する。 |
| `stopUpdateCoroutine()` | `updateCoroutine` が null でなければ停止するだけ。 |
| `climbSurfaceDetected()` | `climbContactCount` が 0 より大きいかを返す。 |
| `getMainRigidbodyVelocity()` | `mainRigidbody.linearVelocity` を返すだけ。 |
| `getMainRigidbodyPosition()` | `mainRigidbody.position` を返すだけ。 |
| `getLastClimbNormal()` | `lastClimbNormal` を返すだけ。 |
| `getContactNormal()` | `contactNormal` を返すだけ。 |
| `setNewParent(Transform newParent)` | `transform.SetParent(newParent)` を呼ぶだけ。 |
