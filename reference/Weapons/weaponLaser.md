# weaponLaser

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `laser`
- **ソース**: `Weapons/New Weapon Behaviors/weaponLaser.cs:6`

**概要**: 武器から照射するレーザーで、ヒット判定・継続ダメージ・レーザーレシーバーや反射キューブへの接続を扱う挙動。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Laser Enabled | `weaponLaserEnabled` | `bool` | – | – |
| Laser Damage | `laserDamage` | `float` | 0.3f | – |
| Layer | `layer` | `LayerMask` | – | – |
| Lasertype | `lasertype` | `laserDevice.laserType` | – | – |
| Reflaction Limit | `reflactionLimit` | `int` | 10 | – |
| Use Energy Rate | `useEnergyRate` | `float` | – | – |
| Amount Energy Used | `amountEnergyUsed` | `int` | – | – |
| Use Min Time To Use Laser Damage Rate | `useMinTimeToUseLaserDamageRate` | `bool` | – | – |
| Min Time To Use Laser Damage Rate | `minTimeToUseLaserDamageRate` | `float` | – | – |
| Laser Damage Rate | `laserDamageRate` | `float` | – | – |

### Sound Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Laser Effect | `laserEffect` | `AudioClip` | – | – |
| Laser Effect Audio Element | `laserEffectAudioElement` | `AudioElement` | – | – |
| Play Sound Rate | `playSoundRate` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Reloading | `reloading` | `bool` | – | – |
| Current Laser | `currentLaser` | `GameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Manager | `weaponManager` | `playerWeaponSystem` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |
| Hit Smoke | `hitSmoke` | `GameObject` | – | – |
| Hit Sparks | `hitSparks` | `GameObject` | – | – |
| Laser Light | `laserLight` | `GameObject` | – | – |
| Player | `player` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `damageTarget(GameObject objectToDamage, Vector3 laserDirection, Vector3 hitPoint)` | レート制限を確認して可否を決め、可能なら`applyDamage.checkHealth`で対象へダメージを与える。 |
| `setLaserInfo(laserDevice.laserType type, GameObject laser, Vector3 pos)` | 当たったレーザーと位置を保存して色を複写し、種類に応じてラインポイント数を設定する。 |
| `removeLaserInfo()` | `currentLaserRenderer`をnullにするだけ。 |
| `enableWeaponLaser()` | `setWeaponLaserState(true)`を呼ぶだけ。 |
| `disableWeaponLaser()` | `setWeaponLaserState(false)`を呼ぶだけ。 |
| `setWeaponLaserState(bool state)` | リロード中は無効のまま、それ以外はレーザー有効状態とライト・軌跡・ヒットエフェクトを切り替える。 |
