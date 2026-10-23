# taserProjectile

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `projectileSystem`
- **ソース**: `Weapons/Projectiles/taserProjectile.cs:6`

**概要**: テーザー用の投射物で、命中したキャラを指定時間だけ気絶させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Use Layer Mask To Ignore | `useLayerMaskToIgnore` | `bool` | – | – |
| Layer Mask To Ignore | `layerMaskToIgnore` | `LayerMask` | – | – |

### Ragdoll Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sedate Delay | `sedateDelay` | `float` | – | – |
| Use Weak Spot To Reduce Delay | `useWeakSpotToReduceDelay` | `bool` | – | – |
| Sedate Until Receive Damage | `sedateUntilReceiveDamage` | `bool` | – | – |
| Sedate Duration | `sedateDuration` | `float` | – | – |
| Use Action System On Impact | `useActionSystemOnImpact` | `bool` | – | – |
| Action System On Impact Name | `actionSystemOnImpactName` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkObjectDetected(Collider col)` | 着弾音と停止処理の後、対象がキャラなら`sedateCharacter`で気絶させ、必要ならアクションを起動する。 |
| `destroyObject()` | `destroyProjectile()`を呼ぶだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetProjectile()`

</details>
