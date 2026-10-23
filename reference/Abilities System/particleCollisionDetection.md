# particleCollisionDetection

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/particleCollisionDetection.cs:6`

**概要**: パーティクル衝突を検出し、位置や相手オブジェクトをイベントで通知するコンポーネント。レイヤーと最大検出回数の制限を持つ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Detection Enabled | `detectionEnabled` | `bool` | true | – |
| Use Layermask On Objects Detected | `useLayermaskOnObjectsDetected` | `bool` | – | – |
| Layermask To Check | `layermaskToCheck` | `LayerMask` | – | – |

### Collision Max Amount Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Collision Max Amount | `useCollisionMaxAmount` | `bool` | – | – |
| Collision Max Amount | `collisionMaxAmount` | `int` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Particle System | `mainParticleSystem` | `ParticleSystem` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Debug Collision Print Active | `debugCollisionPrintActive` | `bool` | – | – |
| Current Collision Counter | `currentCollisionCounter` | `int` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Collision | `useEventOnCollision` | `bool` | true | – |
| Event On Collision | `eventOnCollision` | `eventParameters.eventToCallWithVector3` | – | – |
| Use Event On Collision With Game Object | `useEventOnCollisionWithGameObject` | `bool` | – | – |
| Event On Collision With Game Object | `eventOnCollisionWithGameObject` | `eventParameters.eventToCallWithGameObject` | – | – |
| Collision Events | `collisionEvents` | `List<ParticleCollisionEvent>` | new List<ParticleCollisionEvent> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setDetectionEnabledState(bool state)` | `detectionEnabled` を設定するだけ。 |
