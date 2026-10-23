# healthManagement

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/healthManagement.cs:6`

**概要**: `health`などの各コンポーネントが継承する体力処理の基底クラス。ほぼ全てのメソッドが空実装か固定値の返却で、実際の処理は派生クラスが担当する。`checkHealthAmountOnSpot`だけが部位体力の減算とイベント発火を実装している。

**公式ドキュメント抜粋**（[Emerald AI](../../docs/integrations/current-integrations/emerald-ai.md)）

> This page covers the integration of Emerald AI and Game Kit Controller. Emerald AI allows developers to quickly create engaging dynamic AI with 100's of AAA quality features, all without having to write a single line of code! Emerald's editor is designed to make creating AI easy, yet incredibly customizable.\ \ Emerald caters to all kinds of developers and offers everything users would expect from an all-in-one AI system. You can find more information about Emerald AI, and its documentation and also purchase it over on the Unity Asset Store. Black Horizon Studios (The maker of Emerald AI) has a tutorial video showing the inspector changes needed to integration Emerald AI and Game Kit Controller. If you'd rather just get a step by step instructions for the inspector changes you can view these in the tab below labelled "Step by Step Instructions". While the video also covers the code chang…

## インスペクター設定

### Main Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Health Amount On Spot | `useHealthAmountOnSpot` | `bool` | – | – |
| Healht Amount On Spot | `healhtAmountOnSpot` | `float` | – | – |
| Kill Character On Emtpy Health Amount On Spot | `killCharacterOnEmtpyHealthAmountOnSpot` | `bool` | – | – |
| Remove Component On Empty Health | `removeComponentOnEmptyHealth` | `bool` | – | – |
| Ignore Use Health Amount On Spot | `ignoreUseHealthAmountOnSpot` | `bool` | – | – |
| Use Custom Character Radius | `useCustomCharacterRadius` | `bool` | – | – |
| Custom Character Radius | `customCharacterRadius` | `float` | – | – |

### Events Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Emtpy Health Amount On Spot | `eventOnEmtpyHealthAmountOnSpot` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Health Amount On Spot Empty | `healthAmountOnSpotEmpty` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setDamageWithHealthManagement(float damageAmount, Vector3 fromDirection, Vector3 damagePos, GameObject attacker, GameObject projectile, bool damageConstant, bool searchClosestWeakSpot, bool ignoreShield, bool ignoreDamageInScreen, bool damageCanBeBlocked, bool canActivateReactionSystemTemporally, int damageReactionID, int damageTypeID)` | ダメージ適用の基底メソッドで、本体が空のため何もせず引数も使わない。 |
| `getCurrentHealthAmount()` | 常に`-1`を返すだけで、実際の現在体力は参照しない。 |
| `isUseShieldActive()` | 常に`false`を返すだけで、シールドの有効状態は判定しない。 |
| `getCurrentShieldAmount()` | 常に`0`を返すだけで、実際のシールド量は参照しない。 |
| `checkIfDeadWithHealthManagement()` | 常に`false`を返すだけで、死亡判定は行わない。 |
| `checkIfMaxHealthWithHealthManagement()` | 常に`false`を返すだけで、体力が最大かどうかは判定しない。 |
| `setDamageTargetOverTimeStateWithHealthManagement(float damageOverTimeDelay, float damageOverTimeDuration, float damageOverTimeAmount, float damageOverTimeRate, bool damageOverTimeToDeath, int damageTypeID)` | 継続ダメージ設定の基底メソッドで、本体が空のため何もしない。 |
| `setDamageOrHealthTargetWithDelayWithHealthManagement(float waitAmount, float valueAmount, int damageTypeID)` | 遅延ダメージ／回復設定の基底メソッドで、本体が空のため何もしない。 |
| `removeDamagetTargetOverTimeStateWithHealthManagement()` | 継続ダメージ状態の解除用の基底で、本体が空で何もしない。 |
| `sedateCharacterithHealthManagement(Vector3 position, float sedateDelay, bool useWeakSpotToReduceDelay, bool sedateUntilReceiveDamage, float sedateDuration)` | 鎮静化処理の基底メソッドで、本体が空のため`position`などの引数を使わない。 |
| `setHealWithHealthManagement(float healAmount)` | 回復処理の基底メソッドで、本体が空のため`healAmount`を使わない。 |
| `setShieldWithHealthManagement(float shieldAmount)` | シールド付与の基底メソッドで、本体が空のため`shieldAmount`を使わない。 |
| `getCurrentHealthAmountWithHealthManagement()` | 常に`0`を返すだけで、現在体力は参照しない。 |
| `getMaxHealthAmountWithHealthManagement()` | 常に`0`を返すだけで、最大体力は参照しない。 |
| `getAuxHealthAmountWithHealthManagement()` | 常に`0`を返すだけで、補助体力値は保持しない。 |
| `addAuxHealthAmountWithHealthManagement(float amount)` | 補助体力値の加算用の基底で、本体が空のため`amount`を使わない。 |
| `getHealthAmountToPickWithHealthManagement(float amount)` | 常に`0`を返すだけで、`amount`から取得可能量は計算しない。 |
| `killCharacterWithHealthManagement(GameObject projectile, Vector3 direction, Vector3 position, GameObject attacker, bool damageConstant)` | 死亡処理の基底メソッドで、本体が空のため何もせず引数も使わない。 |
| `killCharacterWithHealthManagement()` | 引数なしの死亡処理の基底で、本体が空のため何もしない。 |
| `getPlaceToShootWithHealthManagement()` | 常に`null`を返すだけで、狙い位置の`Transform`は返さない。 |
| `getPlaceToShootGameObjectWithHealthManagement()` | 常に`null`を返すだけで、狙い位置のオブジェクトは返さない。 |
| `isCharacterWithHealthManagement()` | 常に`false`を返すだけで、キャラクターかどうかは判定しない。 |
| `isVehicleWithHealthManagement()` | 常に`false`を返すだけで、乗り物かどうかは判定しない。 |
| `getCharacterWeakSpotListWithHealthManagement()` | 常に`null`を返すだけで、弱点リストは返さない。 |
| `isCharacterInRagdollState()` | 常に`false`を返すだけで、ラグドール状態かは判定しない。 |
| `getCharacterRootMotionTransform()` | 常に`null`を返すだけで、ルートモーションの`Transform`は返さない。 |
| `getCharacterOrVehicleWithHealthManagement()` | 常に`null`を返すだけで、キャラクター／乗り物のオブジェクトは返さない。 |
| `setFuelWithHealthManagement(float fuelAmount)` | 燃料設定の基底メソッドで、本体が空のため`fuelAmount`を使わない。 |
| `removeFuelWithHealthManagement(float fuelAmount)` | 燃料減少の基底メソッドで、本体が空のため`fuelAmount`を使わない。 |
| `getCurrentFuelAmountWithHealthManagement()` | 常に`0`を返すだけで、現在の燃料量は参照しない。 |
| `checkIfMaxFuelWithHealthManagement()` | 常に`false`を返すだけで、燃料が満タンかは判定しない。 |
| `getCharacterWithHealthManagement()` | 常に`null`を返すだけで、キャラクターのオブジェクトは返さない。 |
| `getVehicleWithHealthManagement()` | 常に`null`を返すだけで、乗り物のオブジェクトは返さない。 |
| `getVehicleHUDManagerWithHealthManagement()` | 常に`null`を返すだけで、`vehicleHUDManager`は返さない。 |
| `getVehicleDriverWithHealthManagement()` | 常に`null`を返すだけで、運転手のオブジェクトは返さない。 |
| `isVehicleBeingDrivenWithHealthManagement()` | 常に`false`を返すだけで、乗り物が運転中かは判定しない。 |
| `checkIfDetectSurfaceBelongToVehicleWithHealthManagement(Collider surfaceFound)` | 常に`false`を返すだけで、`surfaceFound`が乗り物のものかは判定しない。 |
| `checkIfWeakSpotListContainsTransformWithHealthManagement(Transform transformToCheck)` | 常に`false`を返すだけで、`transformToCheck`が弱点リストにあるかは判定しない。 |
| `setEnergyWithHealthManagement(float energyAmount)` | エネルギー設定の基底メソッドで、本体が空のため`energyAmount`を使わない。 |
| `removeEnergyWithHealthManagement(float energyAmount)` | エネルギー減少の基底メソッドで、本体が空のため`energyAmount`を使わない。 |
| `getCurrentEnergyAmountWithHealthManagement()` | 常に`0`を返すだけで、現在のエネルギー量は参照しない。 |
| `checkIfMaxEnergyWithHealthManagement()` | 常に`false`を返すだけで、エネルギーが最大かは判定しない。 |
| `isUseImpactSurfaceActiveWithHealthManagement()` | 常に`false`を返すだけで、着弾面の使用設定は参照しない。 |
| `getDecalImpactIndexWithHealthManagement()` | 常に`-1`を返すだけで、デカールのインデックスは参照しない。 |
| `changePlaceToShootPosition(bool state)` | 狙い位置の切り替え用の基底で、本体が空のため`state`を使わない。 |
| `setPlaceToShootPositionOffset(float newValue)` | 狙い位置のオフセット設定の基底で、本体が空のため`newValue`を使わない。 |
| `setPlaceToShootLocalPosition(Vector3 newValue)` | 狙い位置のローカル座標設定の基底で、本体が空のため`newValue`を使わない。 |
| `isDead()` | 常に`false`を返すだけで、死亡状態は参照しない。 |
| `setBlockDamageActiveState(bool state)` | ダメージブロック有効化の基底で、本体が空のため`state`を使わない。 |
| `isBlockDamageActiveState()` | 常に`false`を返すだけで、ダメージブロック状態は参照しない。 |
| `setBlockDamageProtectionAmount(float newValue)` | ブロック時の軽減量設定の基底で、本体が空のため`newValue`を使わない。 |
| `setBlockDamageRangleAngleState(bool useMaxBlockRangeAngleValue, float maxBlockRangeAngleValue)` | ブロック可能角度の設定用の基底で、本体が空のため引数を使わない。 |
| `setHitReactionBlockIDValue(int newBlockID)` | ヒットリアクションのブロックID設定の基底で、本体が空で何もしない。 |
| `updateSliderOffset(float value)` | スライダーのオフセット更新用の基底で、本体が空のため`value`を使わない。 |
| `updateOriginalSliderOffset()` | スライダーの元オフセット復元用の基底で、本体が空で何もしない。 |
| `setIgnoreParryActiveState(bool state)` | パリィ無視状態の設定用の基底で、本体が空のため`state`を使わない。 |
| `characterHasWeakSpotListWithHealthManagement()` | 常に`false`を返すだけで、弱点リストの有無は判定しない。 |
| `checkIfDamagePositionIsCloseEnoughToWeakSpotByNameWithHealthManagement(Vector3 collisionPosition, List<string> weakSpotNameList, float maxDistanceToWeakSpot)` | 常に`false`を返すだけで、弱点との距離判定は行わない。 |
| `getClosestWeakSpotPositionToPositionWithHealthManagement(Vector3 positionToCheck, List<string> weakListNameToCheck, bool checkWeakListName, float maxDistanceToBodyPart)` | 常に`-Vector3.one`を返すだけで、最寄り弱点の位置は計算しない。 |
| `checkHealthAmountOnSpot(float damageAmount)` | 部位体力`healhtAmountOnSpot`から`damageAmount`を減算し、0以下でイベント発火と任意の死亡・`Destroy`を行う。 |
| `setUseHealthAmountOnSpotState(bool state)` | `useHealthAmountOnSpot`を`state`に設定するだけ。 |
| `setIgnoreUseHealthAmountOnSpot(bool state)` | `ignoreUseHealthAmountOnSpot`を`state`に設定するだけ。 |
| `killCharacterIfCurrentlyDrivingVehicle()` | 運転中の死亡処理用の基底で、本体が空のため何もしない。 |
| `explodeVehicleIfCharacterCurrentlyDriving()` | 運転中の乗り物爆発用の基底で、本体が空のため何もしない。 |
| `setPlayerMenuActiveState(bool state)` | プレイヤーメニューの状態設定用の基底で、本体が空のため`state`を使わない。 |
| `setDamageReactionPausedState(bool state)` | ダメージリアクション停止設定の基底で、本体が空のため`state`を使わない。 |
| `getDamageReceiverColliderList()` | 常に`null`を返すだけで、ダメージ受信コライダー一覧は返さない。 |
| `setIgnoreWeakSpotsActiveState(bool state)` | 弱点無視状態の設定用の基底で、本体が空のため`state`を使わない。 |
| `checkIfDamageReceiverBelongsToThisCharacter(GameObject objectToCheck)` | 常に`false`を返すだけで、`objectToCheck`の所属判定は行わない。 |
| `getUseCustomCharacterRadiusValue()` | `useCustomCharacterRadius`が真なら`customCharacterRadius`を、偽なら`-1`を返す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnEmtpyHealthAmountOnSpot` | `UnityEvent` | – |
