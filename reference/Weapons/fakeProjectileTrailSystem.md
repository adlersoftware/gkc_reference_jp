# fakeProjectileTrailSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/fakeProjectileTrailSystem.cs:5`

**概要**: 実弾を使わず軌跡だけを目標点まで動かして見せるダミー投射物。時間切れや軌跡の消滅で破棄または非アクティブ化する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Trail Enabled | `trailEnabled` | `bool` | true | – |
| Reduce Trail Time Speed | `reduceTrailTimeSpeed` | `float` | 4 | – |
| Movement Active | `movementActive` | `bool` | true | – |
| Disable Instead Of Destroy Active | `disableInsteadOfDestroyActive` | `bool` | – | – |
| Speed Multiplier | `speedMultiplier` | `float` | – | – |
| Max Spawn Time | `maxSpawnTime` | `float` | 5 | – |
| Destroy Trail After Time | `destroyTrailAfterTime` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Trail Active | `trailActive` | `bool` | – | – |
| Target Position | `targetPosition` | `Vector3` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Trail | `mainTrail` | `TrailRenderer` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `instantiateFakeProjectileTrail(Vector3 newTargetPosition)` | `trailEnabled`なら自身を有効化して親を外し、軌跡を初期化して目標点方向を向き、移動を開始する。 |
| `setSpeedMultiplier(float newValue)` | `speedMultiplier`を`newValue`にするだけ。 |
| `stopTrailMovement()` | `movementActive`を偽にして移動を止めるだけ。 |
| `setDestroyTrailAfterTimeState(bool state)` | `destroyTrailAfterTime`を`state`にするだけ。 |
| `changeDestroyForSetActiveFunction(bool state)` | `disableInsteadOfDestroyActive`を`state`にするだけ。 |
| `resetFakeProjectileTrail()` | 軌跡中なら`trailActive`を下ろし、軌跡の時間・タイマー・移動設定を初期化して消去する。 |
