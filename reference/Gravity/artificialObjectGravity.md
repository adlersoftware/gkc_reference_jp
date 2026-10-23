# artificialObjectGravity

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Gravity/artificialObjectGravity.cs:5`

**概要**: Rigidbodyを持つオブジェクトに`useGravity`を使わず独自方向の重力力を与え、接地判定と摩擦材を管理するコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Ray Distance | `rayDistance` | `float` | – | – |
| High Friction Material | `highFrictionMaterial` | `PhysicsMaterial` | – | – |
| Gravity Force | `gravityForce` | `float` | 9.8f | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| On Ground | `onGround` | `bool` | – | – |
| Active | `active` | `bool` | true | – |
| Normal | `normal` | `Vector3` | – | – |
| Hit Point | `hitPoint` | `Vector3` | – | – |
| Aux Normal | `auxNormal` | `Vector3` | – | – |
| Normal Assigned | `normalAssigned` | `bool` | – | – |
| Zero Gravity Active | `zeroGravityActive` | `bool` | – | – |

### Center Point Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Center Point Active | `useCenterPointActive` | `bool` | – | – |
| Current Center Point | `currentCenterPoint` | `Transform` | – | – |
| Use Inverse Direction To Center Point | `useInverseDirectionToCenterPoint` | `bool` | – | – |
| Use Center Point List For Rigidbodies | `useCenterPointListForRigidbodies` | `bool` | – | – |
| Center Point List | `centerPointList` | `List<Transform>` | new List<Transform> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponents()` | 未初期化ならRigidbodyとColliderを取得し、元の重力値を保存する。 |
| `enableGravity(LayerMask layer, PhysicsMaterial frictionMaterial, Vector3 normalDirection)` | 指定レイヤーと摩擦材を設定し、`useGravity`を切り法線方向を初期重力として登録する。 |
| `setActiveState(bool state)` | `active`フラグを設定するだけ。 |
| `removeGravity()` | レイヤーをDefaultへ戻し`useGravity`を有効にしてからコンポーネントを破棄する。 |
| `removeGravityComponent()` | レイヤーをDefaultへ戻してコンポーネントを破棄する。 |
| `removeJustGravityComponent()` | レイヤーは変えずにコンポーネントを破棄する。 |
| `setZeroGravityActiveState(bool state)` | 無重力フラグを設定し、有効なら`useGravity`を切る。 |
| `setCurrentGravity(Vector3 newNormal)` | `useGravity`を切り、法線を直接設定して確定状態にする。 |
| `setUseCenterPointActiveState(bool state, Transform newCenterPoint)` | 中心点使用フラグとTransformを設定するだけ。 |
| `setUseInverseDirectionToCenterPointState(bool state)` | 中心点と逆方向へ引くかどうかのフラグを設定するだけ。 |
| `setGravityForceValue(bool setOriginal, float newValue)` | 元の重力値か指定値を`gravityForce`へ設定する。 |
| `setUseCenterPointListForRigidbodiesState(bool state, List<Transform> newCenterPointList)` | 中心点リストの使用フラグとリストを設定するだけ。 |
| `getCurrentNormalDirection()` | 直前のフレームで使った重力方向を返す。 |
