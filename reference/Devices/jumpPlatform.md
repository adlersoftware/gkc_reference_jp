# jumpPlatform

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/jumpPlatform.cs:5`

**概要**: 触れたプレイヤー・乗り物・任意の剛体を打ち上げるジャンプ台。対象種別や設定に応じ力を加える方法を変える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Platform Enabled | `platformEnabled` | `bool` | true | – |
| Jump Force | `jumpForce` | `float` | – | – |

### Condition Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use With Player | `useWithPlayer` | `bool` | – | – |
| Use With NPC | `useWithNPC` | `bool` | – | – |
| Use With Vehicles | `useWithVehicles` | `bool` | – | – |
| Use With Any Rigidbody | `useWithAnyRigidbody` | `bool` | – | – |
| Use Key To Jump With Player | `useKeyToJumpWithPlayer` | `bool` | – | – |
| Use Key To Jump With Vehicles | `useKeyToJumpWithVehicles` | `bool` | – | – |
| Player Tag | `playerTag` | `string` | "Player" | – |
| Friend Tag | `friendTag` | `string` | "friend" | – |
| Enemy Tag | `enemyTag` | `string` | "enemy" | – |
| Vehicle Tag | `vehicleTag` | `string` | "vehicle" | – |

### Parable Launch Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Parable Launch | `useParableLaunch` | `bool` | – | – |
| Target Position | `targetPosition` | `Transform` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Play Jump Platform Animation | `playJumpPlatformAnimation` | `bool` | true | – |
| Platform Animation | `platformAnimation` | `string` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Impulse | `objectToImpulse` | `GameObject` | – | – |
| Object To Impulse List | `objectToImpulseList` | `List<GameObject>` | new List<GameObject> () | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remove Event Name List | `removeEventNameList` | `List<string>` | new List<string> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Animation | `mainAnimation` | `Animation` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPlatformEnabledState(bool state)` | `platformEnabled`を設定するだけ。 |
