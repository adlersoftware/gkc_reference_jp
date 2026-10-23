# laserPlayer

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `laser`
- **ソース**: `Abilities System/Custom Abilities/laserPlayer.cs:5`

**概要**: プレイヤーに当たったレーザーを反射・描画する `laser` 派生クラス。ヒット位置、レーザーの色、屈折回数を保持する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Laser Damage | `laserDamage` | `float` | 0.3f | – |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Hit Smoke | `hitSmoke` | `GameObject` | – | – |
| Hit Sparks | `hitSparks` | `GameObject` | – | – |
| Lasertype | `lasertype` | `laserDevice.laserType` | – | – |
| Reflaction Limit | `reflactionLimit` | `int` | 10 | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Player | `player` | `GameObject` | – | – |
| Current Laser | `currentLaser` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setLaserInfo(laserDevice.laserType type, GameObject laser, Vector3 pos)` | 当たっているレーザーとヒット位置・種類を保持し、色を合わせて `LineRenderer` の頂点を初期化する。 |
| `removeLaserInfo()` | `currentLaserRenderer` を null にするだけ。 |
