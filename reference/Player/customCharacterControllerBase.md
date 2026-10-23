# customCharacterControllerBase

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Generic Model Controller/customCharacterControllerBase.cs:6`

**概要**: キャラクターモデルのコントローラ設定（Animatorパラメータ、カプセルコライダー、移動速度、カメラ状態、AI値など）を保持し、派生クラスが上書きできる仮想メソッド群を提供する基底クラス。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Controller Enabled | `characterControllerEnabled` | `bool` | true | – |
| Animator Forward Input Lerp Speed | `animatorForwardInputLerpSpeed` | `float` | 0.1f | – |
| Animator Turn Input Lerp Speed | `animatorTurnInputLerpSpeed` | `float` | 0.1f | – |
| Forward Amount Multiplier | `forwardAmountMultiplier` | `float` | 1 | – |
| Update Forward Amount Input Value From Player Controller | `updateForwardAmountInputValueFromPlayerController` | `bool` | – | – |
| Update Turn Amount Input Value From Player Controller | `updateTurnAmountInputValueFromPlayerController` | `bool` | – | – |
| Update Using Input Value From Player Controller | `updateUsingInputValueFromPlayerController` | `bool` | – | – |
| Place To Shoot Offset | `placeToShootOffset` | `float` | – | – |
| Use Place To Shoot Local Position | `usePlaceToShootLocalPosition` | `bool` | – | – |
| Place To Shoot Local Position | `placeToShootLocalPosition` | `Vector3` | – | – |

### Collider Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Capsule Collider Values | `setCapsuleColliderValues` | `bool` | – | – |
| Capsule Collider Center | `capsuleColliderCenter` | `Vector3` | – | – |
| Capsule Collider Radius | `capsuleColliderRadius` | `float` | – | – |
| Capsule Collider Height | `capsuleColliderHeight` | `float` | – | – |
| Capsule Collider Direction | `capsuleColliderDirection` | `int` | 0 | – |
| Use Extra Colliders | `useExtraColliders` | `bool` | – | – |
| Extra Colliders List | `extraCollidersList` | `List<Collider>` | new List<Collider> () | – |
| Set Layer On Extra Collider | `setLayerOnExtraCollider` | `bool` | true | – |

### Animator Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Animator | `mainAnimator` | `Animator` | – | – |
| Original Animator Controller | `originalAnimatorController` | `RuntimeAnimatorController` | – | – |
| Original Avatar | `originalAvatar` | `Avatar` | – | – |
| Charactet Position Offset | `charactetPositionOffset` | `Vector3` | – | – |
| Character Rotation Offset | `characterRotationOffset` | `Vector3` | – | – |

### Root Motion Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Root Motion | `useRootMotion` | `bool` | true | – |
| No Root Walk Movement Speed | `noRootWalkMovementSpeed` | `float` | – | – |
| No Root Run Movement Speed | `noRootRunMovementSpeed` | `float` | – | – |
| No Root Sprint Movement Speed | `noRootSprintMovementSpeed` | `float` | – | – |
| No Root Crouch Movement Speed | `noRootCrouchMovementSpeed` | `float` | – | – |
| No Root Crouch Run Movement Speed | `noRootCrouchRunMovementSpeed` | `float` | 4 | – |
| No Root Walk Strafe Movement Speed | `noRootWalkStrafeMovementSpeed` | `float` | – | – |
| No Root Run Strafe Movement Speed | `noRootRunStrafeMovementSpeed` | `float` | – | – |

### Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Camera States | `setNewCameraStates` | `bool` | – | – |
| New Camera State Third Person | `newCameraStateThirdPerson` | `string` | – | – |
| New Camera State First Person | `newCameraStateFirstPerson` | `string` | – | – |

### Combat Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Combat Type ID | `combatTypeID` | `int` | – | – |
| Player Mode Name | `playerModeName` | `string` | "Combat" | – |
| Move Damage Triggers To Main Parents Enabled | `moveDamageTriggersToMainParentsEnabled` | `bool` | true | – |
| Parent For Combat Damage Triggers | `parentForCombatDamageTriggers` | `Transform` | – | – |
| Other Powers Shoot Zone Parent | `otherPowersShootZoneParent` | `Transform` | – | – |

### Abilities Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Ability Brain Attack Enabled State | `setAbilityBrainAttackEnabledState` | `bool` | – | – |
| Ability Brain Attack Enabled State | `abilityBrainAttackEnabledState` | `bool` | – | – |
| Set Custom Abilities List | `setCustomAbilitiesList` | `bool` | – | – |
| Custom Abilities List | `customAbilitiesList` | `List<string>` | new List<string> () | – |
| Set Change Ability After Time Enabled State | `setChangeAbilityAfterTimeEnabledState` | `bool` | – | – |
| Change Ability After Time Enabled State | `changeAbilityAfterTimeEnabledState` | `bool` | – | – |
| Set Ability By Default | `setAbilityByDefault` | `bool` | – | – |
| Ability By Default Name | `abilityByDefaultName` | `string` | – | – |

### AI Visibility

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hidden From AI Attacks | `hiddenFromAIAttacks` | `bool` | – | – |

### AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set AI Values | `setAIValues` | `bool` | – | – |
| Min Random Time Between Attacks | `minRandomTimeBetweenAttacks` | `float` | – | – |
| Max Random Time Between Attacks | `maxRandomTimeBetweenAttacks` | `float` | – | – |
| Min Time Between Attacks | `minTimeBetweenAttacks` | `float` | – | – |
| New Min Distance To Enemy Using Close Combat | `newMinDistanceToEnemyUsingCloseCombat` | `float` | – | – |
| New Min Distance To Close Combat | `newMinDistanceToCloseCombat` | `float` | – | – |
| Raycast Position Offset | `raycastPositionOffset` | `float` | 1 | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Custom Action Category ID | `customActionCategoryID` | `int` | – | – |
| Character Radius | `characterRadius` | `float` | – | – |
| Custom Ragdoll Info Name | `customRagdollInfoName` | `string` | – | – |
| Health Bar Offset | `healthBarOffset` | `float` | – | – |

### Ground Adherence Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Height Diff Raycast Radius | `heightDiffRaycastRadius` | `float` | – | – |
| Max Step Height | `maxStepHeight` | `float` | – | – |
| New Ray Distance | `newRayDistance` | `float` | 0 | – |

### Other Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Meshes List | `characterMeshesList` | `List<GameObject>` | new List<GameObject> () | – |
| Character Game Object | `characterGameObject` | `GameObject` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Controller Active | `characterControllerActive` | `bool` | – | – |
| Horizontal Input | `horizontalInput` | `float` | – | – |
| Vertical Input | `verticalInput` | `float` | – | – |
| Player Using Input | `playerUsingInput` | `bool` | – | – |
| Movement Input | `movementInput` | `Vector3` | – | – |
| Forward Amount | `forwardAmount` | `float` | – | – |
| Turn Amount | `turnAmount` | `float` | – | – |
| On Ground | `onGround` | `bool` | – | – |
| Character Transform | `characterTransform` | `Transform` | – | – |
| Extra Colliders Info Initialized | `extraCollidersInfoInitialized` | `bool` | – | – |
| Original Character Pivot Transform Position | `originalCharacterPivotTransformPosition` | `Vector3` | – | – |
| Player Controller Transform | `playerControllerTransform` | `Transform` | – | – |
| Can Move | `canMove` | `bool` | – | – |
| Ragdoll Currently Active | `ragdollCurrentlyActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On State Change | `useEventsOnStateChange` | `bool` | – | – |
| Event On Character Controller Activated | `eventOnCharacterControllerActivated` | `UnityEvent` | – | – |
| Event On Character Controller Deactivated | `eventOnCharacterControllerDeactivated` | `UnityEvent` | – | – |
| Use Event To Send Character Object On Start | `useEventToSendCharacterObjectOnStart` | `bool` | – | – |
| Event To Send Character Object On Start | `eventToSendCharacterObjectOnStart` | `eventParameters.eventToCallWithGameObject` | – | – |
| Event To Send Character Object On End | `eventToSendCharacterObjectOnEnd` | `eventParameters.eventToCallWithGameObject` | – | – |
| Event On Instantiate Custom Character Object | `eventOnInstantiateCustomCharacterObject` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateCharacterControllerState()` | 中身が空の仮想メソッドで、派生クラスがコントローラ状態の更新処理を実装するためのフック。 |
| `updateCanMoveState(bool state)` | `canMove` フラグを設定するだけ。 |
| `setRagdollCurrentlyActiveState(bool state)` | `ragdollCurrentlyActive` フラグを設定するだけ。 |
| `updateCharacterControllerAnimator()` | 中身が空の仮想メソッドで、派生クラスがAnimator更新処理を実装するためのフック。 |
| `updateMovementInputValues(Vector3 newValues)` | `movementInput` に受け取った値をそのまま代入するだけ。 |
| `updateHorizontalVerticalInputValues(Vector2 newValues)` | `horizontalInput` と `verticalInput` にx成分とy成分を代入するだけ。 |
| `activateJumpAnimatorState()` | 中身が空の仮想メソッドで、ジャンプ時のAnimator処理を派生クラスに委ねる。 |
| `updateForwardAmountInputValue(float newValue)` | 受け取った値に `forwardAmountMultiplier` を掛けて `forwardAmount` に代入する。 |
| `updateTurnAmountInputValue(float newValue)` | `turnAmount` に受け取った値をそのまま代入するだけ。 |
| `updateOnGroundValue(bool state)` | `onGround` フラグを設定するだけ。 |
| `updatePlayerUsingInputValue(bool state)` | `playerUsingInput` フラグを設定するだけ。 |
| `setForwardAmountMultiplierValue(float newValue)` | `forwardAmountMultiplier` を設定するだけ。 |
| `resetAnimatorState()` | 中身が空の仮想メソッドで、Animatorのリセット処理を派生クラスに委ねる。 |
| `setCharacterControllerActiveState(bool state)` | 有効時のみ `characterControllerActive` を更新し、状態変更イベントの発火とメッシュ表示の切り替えを行う。 |
| `enableOrDisableCharacterMeshesList(bool state)` | `characterMeshesList` 内の各オブジェクトの有効状態をまとめて `state` に切り替える。 |
| `setOriginalCharacterGameObjectTransformPosition(Vector3 newValue)` | `originalCharacterPivotTransformPosition` を設定するだけ。 |
| `setPlayerControllerTransform(Transform newTransform)` | `playerControllerTransform` を設定するだけ。 |
| `setCharacterTransform(Transform newTransform)` | `characterTransform` を設定するだけ。 |
| `checkEventsOnStateChange(bool state)` | 設定に応じて状態変更イベントと `characterGameObject` を渡す開始/終了イベントを発火する。 |
| `updateAnimatorFloatValue(int animatorIDValue, float floatValue)` | `mainAnimator` のfloatパラメータをID指定で設定するだけ。 |
| `updateAnimatorIntegerValue(int animatorIDValue, int intValue)` | `mainAnimator` のintパラメータをID指定で設定するだけ。 |
| `updateAnimatorBoolValue(int animatorIDValue, bool boolValue)` | `mainAnimator` のboolパラメータをID指定で設定するだけ。 |
| `updateAnimatorFloatValueLerping(int animatorIDValue, float floatValue, float animatorLerpSpeed, float currentFixedUpdateDeltaTime)` | `mainAnimator` のfloatパラメータを補間速度とデルタタイム付きで設定するだけ。 |
| `setCapsuleColliderDirectionValue(float newValue)` | floatをintにキャストして `capsuleColliderDirection` に設定するだけ。 |
| `setCapsuleColliderCenterValue(Vector3 newValue)` | `capsuleColliderCenter` を設定するだけ。 |
| `setCapsuleColliderRadiusValue(float newValue)` | `capsuleColliderRadius` を設定するだけ。 |
| `setCapsuleColliderHeightValue(float newValue)` | `capsuleColliderHeight` を設定するだけ。 |
| `setPlaceToShootOffsetValue(float newValue)` | `placeToShootOffset` を設定するだけ。 |
| `setCharactetPositionOffsetValue(Vector3 newValue)` | `charactetPositionOffset` を設定するだけ。 |
| `setCharacterRotationOffsetValue(Vector3 newValue)` | `characterRotationOffset` を設定するだけ。 |
| `setUseRootMotionValue(bool state)` | `useRootMotion` を設定するだけ。 |
| `setNoRootWalkMovementSpeedValue(float newValue)` | `noRootWalkMovementSpeed` を設定するだけ。 |
| `setNoRootRunMovementSpeedValue(float newValue)` | `noRootRunMovementSpeed` を設定するだけ。 |
| `setNoRootSprintMovementSpeedValue(float newValue)` | `noRootSprintMovementSpeed` を設定するだけ。 |
| `setNoRootCrouchMovementSpeedValue(float newValue)` | `noRootCrouchMovementSpeed` を設定するだけ。 |
| `setNoRootWalkStrafeMovementSpeedValue(float newValue)` | `noRootWalkStrafeMovementSpeed` を設定するだけ。 |
| `setNoRootRunStrafeMovementSpeedValue(float newValue)` | `noRootRunStrafeMovementSpeed` を設定するだけ。 |
| `setSetNewCameraStatesValue(bool state)` | `setNewCameraStates` を設定するだけ。 |
| `setNewCameraStateThirdPersonValue(string newValue)` | `newCameraStateThirdPerson` を設定するだけ。 |
| `setNewCameraStateFirstPersonValue(string newValue)` | `newCameraStateFirstPerson` を設定するだけ。 |
| `setCustomActionCategoryIDValue(float newValue)` | floatをintにキャストして `customActionCategoryID` に設定するだけ。 |
| `setCharacterRadiusValue(float newValue)` | `characterRadius` を設定するだけ。 |
| `setCombatTypeIDValue(float newValue)` | floatをintにキャストして `combatTypeID` に設定するだけ。 |
| `setCustomRagdollInfoNameValue(string newValue)` | `customRagdollInfoName` を設定するだけ。 |
| `setPlayerModeNameValue(string newValue)` | `playerModeName` を設定するだけ。 |
| `setHealthBarOffsetValue(float newValue)` | `healthBarOffset` を設定するだけ。 |
| `setHiddenFromAIAttacksValue(bool state)` | `hiddenFromAIAttacks` を設定するだけ。 |
| `setSetAIValuesValue(bool state)` | `setAIValues` を設定するだけ。 |
| `setMaxRandomTimeBetweenAttacksValue(float newValue)` | `maxRandomTimeBetweenAttacks` を設定するだけ。 |
| `setMinRandomTimeBetweenAttacksValue(float newValue)` | `minRandomTimeBetweenAttacks` を設定するだけ。 |
| `setNewMinDistanceToEnemyUsingCloseCombatValue(float newValue)` | `newMinDistanceToEnemyUsingCloseCombat` を設定するだけ。 |
| `setNewMinDistanceToCloseCombatValue(float newValue)` | `newMinDistanceToCloseCombat` を設定するだけ。 |
| `setRaycastPositionOffsetValue(float newValue)` | `raycastPositionOffset` を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCharacterControllerActivated` | `UnityEvent` | – |
| `eventOnCharacterControllerDeactivated` | `UnityEvent` | – |
| `eventOnInstantiateCustomCharacterObject` | `UnityEvent` | – |
