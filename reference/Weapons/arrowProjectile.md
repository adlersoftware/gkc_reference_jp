# arrowProjectile

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/Projectiles/arrowProjectile.cs:6`

**概要**: 矢用の投射物で、着弾面への刺さり・跳ね返り・拾い直しを面の種類ごとに処理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Rotate Arrow With Gravity | `rotateArrowWithGravity` | `bool` | true | – |
| Gravity Force Rotation Speed | `gravityForceRotationSpeed` | `float` | 5 | – |
| Extra Rotation Amount | `extraRotationAmount` | `float` | – | – |
| Moving Objects Tag | `movingObjectsTag` | `string` | "moving" | – |
| Use Gravity On Arrow | `useGravityOnArrow` | `bool` | true | – |
| Gravity Force Down Amount | `gravityForceDownAmount` | `float` | 5 | – |

### Adjust On Surface Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Adjust To Surface Speed | `adjustToSurfaceSpeed` | `float` | 4 | – |
| Offset On Character Body Parent | `offsetOnCharacterBodyParent` | `float` | 0.15f | – |
| Attach Projectile To Surface Offset | `attachProjectileToSurfaceOffset` | `float` | 0.5f | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Arrow Impact | `useEventOnArrowImpact` | `bool` | – | – |
| Event On Arrow Impact | `eventOnArrowImpact` | `UnityEvent` | – | – |
| Event To Drop Arrow Pickup On Bounce | `eventToDropArrowPickupOnBounce` | `UnityEvent` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Projectile System | `mainProjectileSystem` | `projectileSystem` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Main Spawn Object | `mainSpawnObject` | `spawnObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkObjectDetected(GameObject objectToDamage)` | 着弾時に矢を停止させて対象へ親子付けし、面の種類別の跳ね返りや胴体への刺さり登録を行う。 |
| `resetProjectile()` | `applyArrowForces`を戻し、調整コルーチンを止め、親を解除して落下力を1に戻す。 |
| `setNewArrowDownForce(float newValue)` | `currentArrowDownForce`を`newValue`に設定するだけ。 |
| `setArrowSurfaceTypeInfoList(List<bowSystem.arrowSurfaceTypeInfo> newArrowSurfaceTypeInfoList)` | 面の種類リストを差し替え、`checkSurfaceTypeDetected`を真にして判定を有効にする。 |
| `disableCheckSurfaceTypeDetected()` | `checkSurfaceTypeDetected`を偽にして面の種類判定を止めるだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnArrowImpact` | `UnityEvent` | – |
| `eventToDropArrowPickupOnBounce` | `UnityEvent` | – |
