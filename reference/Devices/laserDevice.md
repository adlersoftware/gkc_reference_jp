# laserDevice

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `laser`
- **ソース**: `Devices/laserDevice.cs:5`

**概要**: レーザーの発射側。レイキャストでヒットを判定し、シールドやダメージ処理、コネクタへの受け渡しを行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Enable Player Shield | `enablePlayerShield` | `bool` | true | – |
| Assigned | `assigned` | `bool` | – | – |
| Laser Connector | `laserConnector` | `GameObject` | – | – |
| Lasertype | `lasertype` | `laserType` | – | – |
| Damage Amount | `damageAmount` | `float` | – | – |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Damage Player | `canDamagePlayer` | `bool` | – | – |
| Can Damage Characters | `canDamageCharacters` | `bool` | – | – |
| Can Damage Vehicles | `canDamageVehicles` | `bool` | – | – |
| Can Damage Everything | `canDamageEverything` | `bool` | – | – |
| Can Kill With One Hit | `canKillWithOneHit` | `bool` | – | – |
| Send Message On Contact | `sendMessageOnContact` | `bool` | – | – |
| Shield Ability Name | `shieldAbilityName` | `string` | "Shield" | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Contant Functions | `contantFunctions` | `UnityEvent` | new UnityEvent () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setAssignLaserState(bool state)` | `assigned`を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `contantFunctions` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`disableLaser()`

</details>

## 内部型

- `laserType`（enum）
