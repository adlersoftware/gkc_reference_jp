# joinObjectsPower

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/New Powers Behaviors/joinObjectsPower.cs:5`

**概要**: 2つのオブジェクトを互いに引き寄せるパワー。距離に応じた力を加え、衝突すると解除する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Power Enabled | `powerEnabled` | `bool` | true | – |
| Join Objects Force | `joinObjectsForce` | `float` | 40 | – |
| Time To Remove Join | `timeToRemoveJoin` | `float` | 5 | – |
| Extra Force On Vehicles | `extraForceOnVehicles` | `float` | 1 | – |
| Use Force Mode | `useForceMode` | `bool` | – | – |
| Force Mode Object1 | `forceModeObject1` | `ForceMode` | – | – |
| Force Mode Object2 | `forceModeObject2` | `ForceMode` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Join Objects | `joinObjects` | `bool` | – | – |
| Join Object1 | `joinObject1` | `Transform` | – | – |
| Join Object2 | `joinObject2` | `Transform` | – | – |
| Join Kinematic1 | `joinKinematic1` | `bool` | – | – |
| Join Kinematic2 | `joinKinematic2` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Powers Manager | `powersManager` | `otherPowers` | – | – |
| Layer | `layer` | `LayerMask` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Impact Particles | `impactParticles` | `GameObject` | – | – |
| Player Game Object | `playerGameObject` | `GameObject` | – | – |
| Current Rigidbody1 | `currentRigidbody1` | `Rigidbody` | – | – |
| Current Rigidbody2 | `currentRigidbody2` | `Rigidbody` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の更新コルーチンを停止するだけ。 |
| `addForce(Vector3 direction, Rigidbody rigidbodyAffected, ForceMode forceModeToUsse, bool isVehicle)` | 乗り物なら倍率を掛け、設定に応じた`ForceMode`で`Rigidbody`に力を加える。 |
| `activatePower()` | レイキャストで2つの対象を取得し、衝突監視と重力停止を設定して引き寄せを開始する。 |
| `removeObjectsjoin()` | 追加した衝突監視と発射物コンポーネントを破棄し、重力やパーティクルを元に戻す。 |
