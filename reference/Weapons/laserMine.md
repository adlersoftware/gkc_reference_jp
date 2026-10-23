# laserMine

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `projectileSystem`
- **ソース**: `Weapons/Projectiles/laserMine.cs:6`

**概要**: レーザービーム式の地雷で、接触回数や時間経過で無効化される投射物の派生クラス。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Laser Beam | `laserBeam` | `GameObject` | – | – |
| Disable By Time | `disableByTime` | `bool` | – | – |
| Time To Disable | `timeToDisable` | `float` | – | – |
| Infinite Energy | `infiniteEnergy` | `bool` | – | – |
| Number Of Contacts To Disable | `numberOfContactsToDisable` | `int` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `increaseNumberOfContacts()` | 無限でなければ接触回数を増やし、規定回数に達したら`disableBullet(0)`で無効化する。 |
| `checkObjectDetected(Collider col)` | 着弾音と停止処理を行い、必要なら面へ密着させ、時間制か停止状態で無効化を待つ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetProjectile()`

</details>
