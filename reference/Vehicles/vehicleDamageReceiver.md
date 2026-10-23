# vehicleDamageReceiver

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `healthManagement`
- **ソース**: `Vehicles/vehicleDamageReceiver.cs:4`

**概要**: 車両の各コライダーに付いて被弾を受け、`vehicleHUDManager`へ体力・燃料・エネルギー処理を中継する受信コンポーネント。`healthManagement`の抽象メソッドも上書き実装する。

## インスペクター設定

### Main Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Damage Multiplier | `damageMultiplier` | `float` | 1 | Range (1, 10) |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle | `vehicle` | `GameObject` | – | – |
| Hud Manager | `hudManager` | `vehicleHUDManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setDamage(float amount, Vector3 fromDirection, Vector3 damagePos, GameObject bulletOwner, GameObject projectile, bool damageConstant, bool searchClosestWeakSpot, bool damageCanBeBlocked)` | `damageMultiplier`を掛けた量を`hudManager.setDamage`へ渡し、部位体力設定なら部位も減らす。 |
| `setHeal(float amount)` | `hudManager.getHealth`に回復量をそのまま渡すだけ。 |
| `getMaxHealthAmount()` | `hudManager`の最大体力を返すだけ。 |
| `getAuxHealthAmount()` | `hudManager`の予備体力を返すだけ。 |
| `addAuxHealthAmount(float amount)` | `hudManager.addAuxHealthAmount`に委譲するだけ。 |
| `getCurrentFuelAmount()` | `hudManager`の現在燃料を返すだけ。 |
| `getMaxFuelAmount()` | `hudManager`の最大燃料を返すだけ。 |
| `getFuel(float amount)` | `hudManager.getFuel`に補充量を渡すだけ。 |
| `removeFuel(float amount)` | `hudManager.removeFuel`に消費量を渡すだけ。 |
| `destroyVehicle()` | `hudManager.destroyVehicle`を呼んで車両を破壊するだけ。 |
| `getDecalImpactIndex()` | `hudManager.getDecalImpactIndex`の値を返すだけ。 |
| `getEnergy(float amount)` | `hudManager.getEnergy`に補充量を渡すだけ。 |
| `removeEnergy(float amount)` | `hudManager.removeEnergy`に消費量を渡すだけ。 |
| `getCurrentEnergyAmount()` | `hudManager`の現在エネルギーを返すだけ。 |
| `getMaxEnergyAmount()` | `hudManager`の最大エネルギーを返すだけ。 |
| `getAuxEnergyAmount()` | `hudManager`の予備エネルギーを返すだけ。 |
| `addAuxEnergyAmount(float amount)` | `hudManager.addAuxEnergyAmount`に委譲するだけ。 |
| `isVehicleDestroyed()` | `hudManager.destroyed`を返すだけ。 |
| `ignoreCollisionWithSolidVehicleColliderList(Collider colliderToIgnore, bool state)` | `hudManager`の同名メソッドにコライダーと状態を渡すだけ。 |
| `setVehicle(GameObject vehicleGameObject, vehicleHUDManager currentVehicleHUDManager)` | `vehicle`と`hudManager`を差し替えてシーンを更新する。 |
| `setDamageTargetOverTimeState(float damageOverTimeDelay, float damageOverTimeDuration, float damageOverTimeAmount, float damageOverTimeRate, bool damageOverTimeToDeath, int damageTypeID)` | 継続ダメージの遅延・時間・量・間隔・致死可否・種類を`hudManager`へ渡すだけ。 |
| `removeDamagetTargetOverTimeState()` | `hudManager.stopDamageOverTime`を呼ぶだけ。 |
| `getHUDManager()` | 保持している`hudManager`を返すだけ。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とダーティシーン更新を呼ぶだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`addAuxHealthAmountWithHealthManagement(float amount)`, `checkIfDeadWithHealthManagement()`, `checkIfMaxEnergyWithHealthManagement()`, `checkIfMaxFuelWithHealthManagement()`, `checkIfMaxHealthWithHealthManagement()`, `getAuxHealthAmountWithHealthManagement()`, `getCharacterOrVehicleWithHealthManagement()`, `getCurrentEnergyAmountWithHealthManagement()`, `getCurrentFuelAmountWithHealthManagement()`, `getCurrentHealthAmount()`, `getCurrentHealthAmountWithHealthManagement()`, `getDecalImpactIndexWithHealthManagement()`, `getHealthAmountToPickWithHealthManagement(float amount)`, `getMaxHealthAmountWithHealthManagement()`, `getPlaceToShootGameObjectWithHealthManagement()`, `getPlaceToShootWithHealthManagement()`, `getVehicleDriverWithHealthManagement()`, `getVehicleHUDManagerWithHealthManagement()`, `getVehicleWithHealthManagement()`, `isUseImpactSurfaceActiveWithHealthManagement()`, `isVehicleWithHealthManagement()`, `killCharacterWithHealthManagement()`, `killCharacterWithHealthManagement(GameObject projectile, Vector3 direction, Vector3 position, GameObject attacker, bool damageConstant)`, `removeDamagetTargetOverTimeStateWithHealthManagement()`, `removeEnergyWithHealthManagement(float amount)`, `removeFuelWithHealthManagement(float fuelAmount)`, `setDamageOrHealthTargetWithDelayWithHealthManagement(float waitAmount, float valueAmount, int damageTypeID)`, `setDamageTargetOverTimeStateWithHealthManagement(float damageOverTimeDelay, float damageOverTimeDuration, float damageOverTimeAmount, float damageOverTimeRate, bool damageOverTimeToDeath, int damageTypeID)`, `setDamageWithHealthManagement(float damageAmount, Vector3 fromDirection, Vector3 damagePos, GameObject attacker, GameObject projectile, bool damageConstant, bool searchClosestWeakSpot, bool ignoreShield, bool ignoreDamageInScreen, bool damageCanBeBlocked, bool canActivateReactionSystemTemporally, int damageReactionID, int damageTypeID)`, `setEnergyWithHealthManagement(float amount)`, `setFuelWithHealthManagement(float fuelAmount)`, `setHealWithHealthManagement(float healAmount)`

</details>
