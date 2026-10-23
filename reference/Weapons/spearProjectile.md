# spearProjectile

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `projectileSystem`
- **ソース**: `Weapons/Projectiles/spearProjectile.cs:6`

**概要**: 槍の投射物で、着弾時の刺さりや一撃必殺、ラグドールを貫いて運ぶ処理を持つ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Ray Distance | `rayDistance` | `float` | 1 | – |
| Carrying Ragdoll Speed Multiplier | `carryingRagdollSpeedMultiplier` | `float` | 3 | – |
| Max Projectile Speed Clamp | `maxProjectileSpeedClamp` | `float` | 30 | – |
| Capsule Cast Radius | `capsuleCastRadius` | `float` | 2 | – |
| Delay To Drop Spear If Not Surface Found | `delayToDropSpearIfNotSurfaceFound` | `float` | 10 | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use General Probability To Kill Targets | `useGeneralProbabilityToKillTargets` | `bool` | – | – |
| General Probability To Kill Targets | `generalProbabilityToKillTargets` | `float` | – | Range (0, 100) |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Surface Found | `surfaceFound` | `bool` | – | – |
| Carrying Ragdoll | `carryingRagdoll` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Raycast Position Transform | `raycastPositionTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`があれば停止するだけ。 |
| `checkObjectDetected(Collider col)` | 着弾で停止して対象やラグドールへ親子付けし、一撃必殺判定なら`killCharacter`と運搬を、そうでなければダメージと力を与える。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetProjectile()`

</details>
