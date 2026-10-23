# characterDamageReceiver

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `healthManagement`
- **ソース**: `Health/characterDamageReceiver.cs:5`

**概要**: コライダーごとに付与される中継コンポーネント。受け取ったダメージに`damageMultiplier`を掛けて`health`へ転送し、回復・シールド・弱点・即死などのAPIも`healthManagement`として仲介する。

## インスペクター設定

### Main Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Damage Multiplier | `damageMultiplier` | `float` | 1 | Range (1, 20) |
| Apply Force On This Object If Detected | `applyForceOnThisObjectIfDetected` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character | `character` | `GameObject` | – | – |
| Health Manager | `healthManager` | `health` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Assigned | `characterAssigned` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setDamage(float amount, Vector3 fromDirection, Vector3 damagePos, GameObject bulletOwner, GameObject projectile, bool damageConstant, bool searchClosestWeakSpot, bool ignoreDamageInScreen, bool damageCanBeBlocked, bool canActivateReactionSystemTemporally, int damageReactionID, int damageTypeID)` | `amount`に`damageMultiplier`を掛けて`healthManager.setDamage`へ渡し、部位HP使用時は`checkHealthAmountOnSpot`も呼ぶ。 |
| `setHeal(float amount)` | `healthManager.getHealth(amount)`を呼んで回復するだけ。 |
| `getMaxHealthAmount()` | `healthManager.getMaxHealthAmount()`の値を返すだけ。 |
| `getAuxHealthAmount()` | `healthManager.getAuxHealthAmount()`の値を返すだけ。 |
| `addAuxHealthAmount(float amount)` | `healthManager.addAuxHealthAmount(amount)`に委譲するだけ。 |
| `getHealthAmountToLimit()` | `healthManager.getHealthAmountToLimit()`の値を返すだけ。 |
| `isApplyForceOnThisObjectIfDetectedActive()` | `applyForceOnThisObjectIfDetected`の真偽を返すだけ。 |
| `compareObjectTag(string tagToCompare)` | `characterAssigned`なら`character`、未設定なら自身のタグを`tagToCompare`と比較する。 |
| `killCharacter(GameObject projectile, Vector3 direction, Vector3 position, GameObject attacker, bool damageConstant)` | `healthManager.killCharacter`へ方向・位置・攻撃者・飛翔物を渡して即死させる。 |
| `getDecalImpactIndex()` | `healthManager.getDecalImpactIndex()`の値を返すだけ。 |
| `isCharacterDead()` | `healthManager.dead`を返すだけ。 |
| `setCharacter(GameObject characterGameObject, health currentHealth)` | `character`と`healthManager`を差し替えて`characterAssigned`を立て、非再生時は`updateComponent`も呼ぶ。 |
| `setDamageMultiplierValue(float newValue)` | `damageMultiplier`を`newValue`にし、非再生時はコンポーネントを更新する。 |
| `setDamageTargetOverTimeState(float damageOverTimeDelay, float damageOverTimeDuration, float damageOverTimeAmount, float damageOverTimeRate, bool damageOverTimeToDeath, int damageTypeID)` | 継続ダメージの遅延・時間・量・間隔・死亡設定を`healthManager.setDamageTargetOverTimeState`へ渡す。 |
| `removeDamagetTargetOverTimeState()` | `healthManager.stopDamageOverTime()`で継続ダメージを止めるだけ。 |
| `sedateCharacter(Vector3 position, float sedateDelay, bool useWeakSpotToReduceDelay, bool sedateUntilReceiveDamage, float sedateDuration)` | `healthManager.sedateCharacter`へ鎮静の遅延・継続時間・弱点多用設定を渡す。 |
| `getHealthManager()` | `healthManager`参照を返すだけ。 |
| `getShieldAmountToLimit()` | `healthManager.getShieldAmountToLimit()`の値を返すだけ。 |
| `addAuxShieldAmount(float amount)` | `healthManager.addAuxShieldAmount(amount)`に委譲するだけ。 |
| `setShield(float amount)` | `healthManager.setShield(amount)`に委譲するだけ。 |
| `characterIsOnRagdollState()` | `healthManager.characterIsOnRagdollState()`の値を返すだけ。 |
| `getTransformToAttachWeaponsByClosestPosition(Vector3 positionToCheck)` | `positionToCheck`に最も近い武器装着用`Transform`を`healthManager`から取得する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`でシーンをダーティ更新するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`addAuxHealthAmountWithHealthManagement(float amount)`, `characterHasWeakSpotListWithHealthManagement()`, `checkIfDamagePositionIsCloseEnoughToWeakSpotByNameWithHealthManagement(Vector3 collisionPosition, List<string> weakSpotNameList, float maxDistanceToWeakSpot)`, `checkIfDeadWithHealthManagement()`, `checkIfMaxHealthWithHealthManagement()`, `checkIfWeakSpotListContainsTransformWithHealthManagement(Transform transformToCheck)`, `explodeVehicleIfCharacterCurrentlyDriving()`, `getAuxHealthAmountWithHealthManagement()`, `getCharacterOrVehicleWithHealthManagement()`, `getCharacterRootMotionTransform()`, `getCharacterWeakSpotListWithHealthManagement()`, `getCharacterWithHealthManagement()`, `getClosestWeakSpotPositionToPositionWithHealthManagement(Vector3 positionToCheck, List<string> weakListNameToCheck, bool checkWeakListName, float maxDistanceToBodyPart)`, `getCurrentHealthAmount()`, `getCurrentHealthAmountWithHealthManagement()`, `getDecalImpactIndexWithHealthManagement()`, `getHealthAmountToPickWithHealthManagement(float amount)`, `getMaxHealthAmountWithHealthManagement()`, `getPlaceToShootGameObjectWithHealthManagement()`, `getPlaceToShootWithHealthManagement()`, `isCharacterInRagdollState()`, `isCharacterWithHealthManagement()`, `isUseImpactSurfaceActiveWithHealthManagement()`, `killCharacterIfCurrentlyDrivingVehicle()`, `killCharacterWithHealthManagement()`, `killCharacterWithHealthManagement(GameObject projectile, Vector3 direction, Vector3 position, GameObject attacker, bool damageConstant)`, `removeDamagetTargetOverTimeStateWithHealthManagement()`, `sedateCharacterithHealthManagement(Vector3 position, float sedateDelay, bool useWeakSpotToReduceDelay, bool sedateUntilReceiveDamage, float sedateDuration)`, `setDamageOrHealthTargetWithDelayWithHealthManagement(float waitAmount, float valueAmount, int damageTypeID)`, `setDamageTargetOverTimeStateWithHealthManagement(float damageOverTimeDelay, float damageOverTimeDuration, float damageOverTimeAmount, float damageOverTimeRate, bool damageOverTimeToDeath, int damageTypeID)`, `setDamageWithHealthManagement(float damageAmount, Vector3 fromDirection, Vector3 damagePos, GameObject attacker, GameObject projectile, bool damageConstant, bool searchClosestWeakSpot, bool ignoreShield, bool ignoreDamageInScreen, bool damageCanBeBlocked, bool canActivateReactionSystemTemporally, int damageReactionID, int damageTypeID)`, `setHealWithHealthManagement(float healAmount)`, `setShieldWithHealthManagement(float shieldAmount)`

</details>
