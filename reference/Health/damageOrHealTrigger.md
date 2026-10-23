# damageOrHealTrigger

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/damageOrHealTrigger.cs:5`

**概要**: トリガー内のオブジェクトへ継続的にダメージ・回復・エネルギー/燃料補給を行う。対象判定はタグ一覧とプレイヤー/車両/キャラクタの種別フラグで行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use With Player | `useWithPlayer` | `bool` | – | – |
| Use With Vehicles | `useWithVehicles` | `bool` | – | – |
| Use With Characters | `useWithCharacters` | `bool` | – | – |
| Tag To Affect List | `tagToAffectList` | `List<string>` | new List<string> () | – |

### Damage-Health Settinga

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Amount Enabled | `addAmountEnabled` | `bool` | – | – |
| Remove Amount Enabled | `removeAmountEnabled` | `bool` | – | – |
| Can Heal | `canHeal` | `bool` | – | – |
| Heal Rate | `healRate` | `float` | – | – |
| Healt Amount | `healtAmount` | `float` | – | – |
| Can Refill Energy | `canRefillEnergy` | `bool` | – | – |
| Energy Rate | `energyRate` | `float` | – | – |
| Energy Amount | `energyAmount` | `float` | – | – |
| Can Refill Fuel | `canRefillFuel` | `bool` | – | – |
| Fuel Rate | `fuelRate` | `float` | – | – |
| Fuel Amount | `fuelAmount` | `float` | – | – |

### Other Settinga

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Can Activate Reaction System Temporally | `canActivateReactionSystemTemporally` | `bool` | – | – |
| Damage Reaction ID | `damageReactionID` | `int` | -1 | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |
| Apply Value At Once | `applyValueAtOnce` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player | `player` | `GameObject` | – | – |
| Object With Health | `objectWithHealth` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `isInTagToAffectList(GameObject objectToCheck)` | `tagToAffectList`に対象のタグが含まれるかを返すだけ。 |
