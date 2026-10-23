# vehicleLaser

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `laser`
- **ソース**: `Vehicles/vehicleLaser.cs:5`

**概要**: 車両搭載レーザーの照射判定と描画を行うコンポーネント。ヒット位置に火花やパーティクルを出し、継続的にダメージを与える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Laser Damage | `laserDamage` | `float` | 0.3f | – |
| Laser Damage Rate | `laserDamageRate` | `float` | 0.5f | – |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |
| Using Custom Ray Position | `usingCustomRayPosition` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Hit Particles | `hitParticles` | `GameObject` | – | – |
| Hit Sparks | `hitSparks` | `GameObject` | – | – |
| Vehicle | `vehicle` | `GameObject` | – | – |
| Vehicle Camera | `vehicleCamera` | `GameObject` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Vehicle Camera Manager | `vehicleCameraManager` | `vehicleCameraController` | – | – |
| Vehicle HUD | `vehicleHUD` | `vehicleHUDManager` | – | – |
| Current Driver | `currentDriver` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `changeLaserState(bool state)` | 描画と`laserActive`を設定し、有効化時は演出開始とドライバー取得、無効化時は火花とパーティクルを消す。 |
| `updateCustomRayPosition(Vector3 newPosition, Vector3 newDirection)` | `usingCustomRayPosition`を立て、カスタムの照射開始位置と方向を保存する。 |
