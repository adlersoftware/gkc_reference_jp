# blackHoleProjectile

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `projectileSystem`
- **ソース**: `Powers/blackHoleProjectile.cs:6`

**概要**: 黒穴として機能する特殊弾。範囲内の`Rigidbody`を引き込み、終了時に爆発させて放出する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Get Objects Radius | `getObjectsRadius` | `float` | 40 | – |
| Black Hole Attraction Force | `blackHoleAttractionForce` | `float` | 150 | – |
| Opening Black Hole Particles | `openingBlackHoleParticles` | `GameObject` | – | – |
| Closing Black Hole Particles | `closingBlackHoleParticles` | `GameObject` | – | – |
| Tag To Locate | `tagToLocate` | `List<string>` | new List<string> () | – |
| Elements To Absorve | `elementsToAbsorve` | `List<GameObject>` | new List<GameObject> () | – |
| Rigidbodies To Absorve | `rigidbodiesToAbsorve` | `List<Rigidbody>` | new List<Rigidbody> () | – |
| Min Distance To Stop Attraction | `minDistanceToStopAttraction` | `float` | 4 | – |
| Damage Rate | `damageRate` | `float` | 0.5f | – |

### Black Hole Duration Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Stop Bullet Timer | `stopBulletTimer` | `float` | 1 | – |
| Black Hole Duration | `blackHoleDuration` | `float` | 10 | – |
| Time To Open Black Hole After Shoot | `timeToOpenBlackHoleAfterShoot` | `float` | 0.5f | – |
| Time To Activate Open Particles | `timeToActivateOpenParticles` | `float` | 3.5f | – |
| Time To Activate Close Particles | `timeToActivateCloseParticles` | `float` | 4 | – |
| Time To Close Black Hole | `timeToCloseBlackHole` | `float` | 0.5f | – |
| Time To Destroy Particles | `timeToDestroyParticles` | `float` | 10 | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `dropBlackHoleObjects()` | 吸い込んだ`Rigidbody`の重力を戻して爆発力を加え、黒穴のパーティクルを消す。 |
| `stopBlackHole()` | 弾を停止させるフラグを立てるだけ。 |
| `activateProjectileAbility()` | 他の黒穴を破棄し、重力の有効化・コライダー拡大・トレイル変更を行う。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetProjectile()`

</details>
