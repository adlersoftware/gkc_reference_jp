# enemyLaser

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `laser`
- **ソース**: `AI/Turret/enemyLaser.cs:4`

**概要**: タレットなどが放つレーザーの描画とダメージ処理を行うコンポーネント。レイキャストの命中点にスパークと煙を出し、設定された所有者名義でダメージを与える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Laser Damage | `laserDamage` | `float` | 0.2f | – |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |
| Use Damage Rate | `useDamageRate` | `bool` | – | – |
| Damage Rate | `damageRate` | `float` | 0.3f | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hit Particles | `hitParticles` | `GameObject` | – | – |
| Hit Sparks | `hitSparks` | `GameObject` | – | – |
| Use Custom Laser Position | `useCustomLaserPosition` | `bool` | – | – |
| Custom Laser Position | `customLaserPosition` | `Transform` | – | – |
| Owner | `owner` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setOwner(GameObject laserOwner)` | `owner`を設定するだけ。 |
