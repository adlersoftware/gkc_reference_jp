# healerWeapon

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/New Weapon Behaviors/healerWeapon.cs:6`

**概要**: 回復・ダメージ・燃料やエネルギーの補充を切り替えて使う多機能武器。レイキャストした対象へ効果を適用し、設定に応じて弾を消費または回収する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Can Heal | `canHeal` | `bool` | – | – |
| Heal Rate | `healRate` | `float` | – | – |
| Healt Amount | `healtAmount` | `float` | – | – |
| Can Damage | `canDamage` | `bool` | – | – |
| Damage Rate | `damageRate` | `float` | – | – |
| Damage Amount | `damageAmount` | `float` | – | – |
| Can Refill Energy | `canRefillEnergy` | `bool` | – | – |
| Energy Rate | `energyRate` | `float` | – | – |
| Energy Amount | `energyAmount` | `float` | – | – |
| Can Refill Fuel | `canRefillFuel` | `bool` | – | – |
| Fuel Rate | `fuelRate` | `float` | – | – |
| Fuel Amount | `fuelAmount` | `float` | – | – |
| Can Gather Health | `canGatherHealth` | `bool` | – | – |
| Can Gather Energy | `canGatherEnergy` | `bool` | – | – |
| Can Gather Fuel | `canGatherFuel` | `bool` | – | – |
| Use With Vehicles | `useWithVehicles` | `bool` | – | – |
| Use With Characters | `useWithCharacters` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |
| Can Activate Reaction System Temporally | `canActivateReactionSystemTemporally` | `bool` | – | – |
| Damage Reaction ID | `damageReactionID` | `int` | -1 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Current Object To Check | `currentObjectToCheck` | `GameObject` | – | – |
| Current Health Element | `currentHealthElement` | `GameObject` | – | – |
| Target Found | `targetFound` | `bool` | – | – |
| Searching Targets | `searchingTargets` | `bool` | – | – |
| Heal Mode Active | `healModeActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Weapon Manager | `weaponManager` | `playerWeaponSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`があれば停止するだけ。 |
| `changeMode()` | 初期化後に`healModeActive`を反転し、回復と攻撃のモードを切り替える。 |
| `checkTarget(GameObject target)` | 対象が乗物かキャラで対応が有効なら、`changeTriggerState`で対象と計測開始時刻を登録する。 |
| `downButtonAction()` | `searchingTargets`を真にして更新コルーチンを開始し、対象探索と効果適用を始める。 |
| `upButtonAction()` | `searchingTargets`を偽にし、対象登録を解除して更新コルーチンを止める。 |
| `setCanHealState(bool state)` | `canHeal`を設定し、真ならダメージと燃料・エネルギー補充を偽にして回復専用にする。 |
| `setCanDamageState(bool state)` | `canDamage`を設定し、真なら回復と燃料・エネルギー補充を偽にして攻撃専用にする。 |
| `setCanRefillEnergyState(bool state)` | `canRefillEnergy`を設定し、真なら回復・ダメージ・燃料補充を偽にする。 |
| `setCanRefillFuelState(bool state)` | `canRefillFuel`を設定し、真なら回復・ダメージ・エネルギー補充を偽にする。 |
| `setCanGatherHealthState(bool state)` | `canGatherHealth`を`state`にするだけ。 |
| `setCanGatherEnergyState(bool state)` | `canGatherEnergy`を`state`にするだけ。 |
| `setCanGatherFuelState(bool state)` | `canGatherFuel`を`state`にするだけ。 |
| `setHealModeActiveState(bool state)` | `healModeActive`を`state`にするだけ。 |
