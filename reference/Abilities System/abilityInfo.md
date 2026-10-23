# abilityInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/abilityInfo.cs:6`

**概要**: 1つのアビリティの設定と状態（有効可否、クールダウン、時間制限、エネルギー、押下状態、イベント、コルーチン）を保持する基底クラス。効果本体は派生クラス側が実装する。

## インスペクター設定

### Ability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Name | `Name` | `string` | – | – |
| Ability Enabled | `abilityEnabled` | `bool` | – | – |
| Ability Texture | `abilityTexture` | `Texture` | – | – |
| Ability Sprite | `abilitySprite` | `Sprite` | – | – |
| Add Ability To UI Wheel Active | `addAbilityToUIWheelActive` | `bool` | true | – |
| Update Ability Active | `updateAbilityActive` | `bool` | – | – |
| Deactivate Ability When Change To Another | `deactivateAbilityWhenChangeToAnother` | `bool` | – | – |
| Disable Ability Input In Use State On Press Down | `disableAbilityInputInUseStateOnPressDown` | `bool` | – | – |
| Can Be Used Only On Ground | `canBeUsedOnlyOnGround` | `bool` | – | – |
| Show Ability Description | `showAbilityDescription` | `bool` | – | – |
| Ability Description | `abilityDescription` | `string` | – | TextArea (3, 10) |

### Ability UI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ability Visible On Wheel Selection | `abilityVisibleOnWheelSelection` | `bool` | true | – |
| Ability Can Be Shown On Wheel Selection | `abilityCanBeShownOnWheelSelection` | `bool` | true | – |

### Ability Limit/Duration Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Time Limit | `useTimeLimit` | `bool` | – | – |
| Time Limit | `timeLimit` | `float` | – | – |
| Use Limit When Ability Current Active From Press | `useLimitWhenAbilityCurrentActiveFromPress` | `bool` | – | – |
| Call Input To Deactivate Ability On Time Limit | `callInputToDeactivateAbilityOnTimeLimit` | `bool` | – | – |
| Event On Time Limit Before | `eventOnTimeLimitBefore` | `UnityEvent` | – | – |
| Event On Time Limit After | `eventOnTimeLimitAfter` | `UnityEvent` | – | – |
| Use Time Limit On Press Down | `useTimeLimitOnPressDown` | `bool` | – | – |
| Use Time Limit On Press Up | `useTimeLimitOnPressUp` | `bool` | – | – |
| Avoid Ability Input While Limit Active | `avoidAbilityInputWhileLimitActive` | `bool` | – | – |
| Reset Ability Currently Active From Press State On Time Limit | `resetAbilityCurrentlyActiveFromPressStateOnTimeLimit` | `bool` | – | – |
| Avoid To Use Other Abilities While Limit Active | `avoidToUseOtherAbilitiesWhileLimitActive` | `bool` | – | – |

### Ability Cool Down Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Cool Down | `useCoolDown` | `bool` | – | – |
| Cool Down Duration | `coolDownDuration` | `float` | – | – |
| Use Cool Down When Ability Currently Active From Press | `useCoolDownWhenAbilityCurrentlyActiveFromPress` | `bool` | – | – |
| Event On Cool Down Activate | `eventOnCoolDownActivate` | `UnityEvent` | – | – |
| Use Cool Down On Press Down | `useCoolDownOnPressDown` | `bool` | – | – |
| Use Cool Down On Press Up | `useCoolDownOnPressUp` | `bool` | – | – |
| Activate Cool Down After Time Limit | `activateCoolDownAfterTimeLimit` | `bool` | – | – |
| Cool Down Multiplier | `coolDownMultiplier` | `float` | 1 | – |

### Ability Input Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Input On Press Down | `useInputOnPressDown` | `bool` | – | – |
| Use Input On Press Hold | `useInputOnPressHold` | `bool` | – | – |
| Use Input On Press Up | `useInputOnPressUp` | `bool` | – | – |
| Check If Input Press Down Before Activate Up | `checkIfInputPressDownBeforeActivateUp` | `bool` | – | – |
| Can Use Press Down Input If Player Busy | `canUsePressDownInputIfPlayerBusy` | `bool` | – | – |
| Can Stop Ability If Action Active | `canStopAbilityIfActionActive` | `bool` | – | – |
| Ignore Set Ability Currently Active From Press Down | `ignoreSetAbilityCurrentlyActiveFromPressDown` | `bool` | – | – |

### Ability Energy Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Energy On Ability | `useEnergyOnAbility` | `bool` | – | – |
| Use Energy With Rate | `useEnergyWithRate` | `bool` | – | – |
| Energy Amount Used | `energyAmountUsed` | `float` | – | – |
| Use Energy On Press Down | `useEnergyOnPressDown` | `bool` | – | – |
| Use Energy On Press Hold | `useEnergyOnPressHold` | `bool` | – | – |
| Use Energy On Press Up | `useEnergyOnPressUp` | `bool` | – | – |
| Use Energy Once On Press Down | `useEnergyOnceOnPressDown` | `bool` | – | – |
| Use Energy Once On Press Up | `useEnergyOnceOnPressUp` | `bool` | – | – |

### Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Animation With Action System | `useAnimationWithActionSystem` | `bool` | – | – |
| Animation Action System Name | `animationActionSystemName` | `string` | – | – |
| Use Animation On Press Down | `useAnimationOnPressDown` | `bool` | – | – |
| Use Animation On Press Up | `useAnimationOnPressUp` | `bool` | – | – |

### Ability Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Abilities System | `mainPlayerAbilitiesSystem` | `playerAbilitiesSystem` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Set Current Ability | `useEventsOnSetCurrentAbility` | `bool` | – | – |
| Event On Set Current Ability | `eventOnSetCurrentAbility` | `UnityEvent` | – | – |
| Use Event On Use Ability | `useEventOnUseAbility` | `bool` | – | – |
| Event On Use Ability | `eventOnUseAbility` | `UnityEvent` | – | – |
| Event To Deactivate Ability | `eventToDeactivateAbility` | `UnityEvent` | – | – |
| Use Condition Check To Activate Ability On Press Down | `useConditionCheckToActivateAbilityOnPressDown` | `bool` | – | – |
| Event To Call To Check Condition On Press Down | `eventToCallToCheckConditionOnPressDown` | `UnityEvent` | – | – |
| Use Condition Check To Activate Ability On Press Up | `useConditionCheckToActivateAbilityOnPressUp` | `bool` | – | – |
| Event To Call To Check Condition On Press Up | `eventToCallToCheckConditionOnPressUp` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ability Currently Active From Press Down | `abilityCurrentlyActiveFromPressDown` | `bool` | – | – |
| Ability Currently Active From Press Up | `abilityCurrentlyActiveFromPressUp` | `bool` | – | – |
| Is Current Ability | `isCurrentAbility` | `bool` | – | – |
| Cool Down In Process | `coolDownInProcess` | `bool` | – | – |
| Time Limit In Process | `timeLimitInProcess` | `bool` | – | – |
| Current Cool Down Duration | `currentCoolDownDuration` | `float` | – | – |
| Update Ability In Process | `updateAbilityInProcess` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `disableAbilityCurrentActiveFromPressState()` | 押下/押上由来のアクティブ状態を両方falseにするだけ。 |
| `enableOrDisableAbilityExternally(bool state)` | `state`に応じ外部向けの有効化/無効化を呼び分ける。 |
| `setAbilityEnabledState(bool state)` | `abilityEnabled`を設定するだけ。 |
| `isAbilityEnabled()` | `abilityEnabled`をそのまま返す。 |
| `enableAbilityExternally()` | 有効状態にして`enableAbility`を呼ぶ。 |
| `disableAbilityExternally()` | 無効化し、現在状態・更新・押下状態をすべて解除する。 |
| `setAbilityVisibleOnWheelSelectionState(bool state)` | `abilityVisibleOnWheelSelection`を設定するだけ。 |
| `setAbilityCanBeShownOnWheelSelectionState(bool state)` | `abilityCanBeShownOnWheelSelection`を設定するだけ。 |
| `updateAbilityState()` | 本体が空の`virtual`メソッドで何もしない。 |
| `enableAbility()` | 派生クラスが実装する空の`virtual`メソッド。 |
| `disableAbility()` | 本体が空の`virtual`メソッドで何もしない。 |
| `deactivateAbility()` | 本体が空の`virtual`メソッドで何もしない。 |
| `activateSecondaryActionOnAbility()` | 本体が空の`virtual`メソッドで何もしない。 |
| `checkIfUseAnimationWithActionSystemOnPressDown()` | アニメと押下の設定が真なら、アクション名でカスタムアクションを起動する。 |
| `checkIfUseAnimationWithActionSystemOnPressUp()` | 押上用の設定が真なら、同様にカスタムアクションを起動する。 |
| `checkEventOnSetCurrentAbility()` | 設定時のみ`eventOnSetCurrentAbility`を発火する。 |
| `checkUseEventOnUseAbility()` | 設定時のみ`eventOnUseAbility`を発火する。 |
| `checkEventToDeactivateAbility()` | `eventToDeactivateAbility`を無条件で発火する。 |
| `useAbilityPressDown()` | 本体が空の`virtual`メソッドで何もしない。 |
| `useAbilityPressHold()` | 本体が空の`virtual`メソッドで何もしない。 |
| `useAbilityPressUp()` | 本体が空の`virtual`メソッドで何もしない。 |
| `activateCoolDown()` | `useCoolDown`時のみ既存CD/制限を止め、CDコルーチンを開始する。 |
| `stopActivateCoolDown()` | CDコルーチンがあれば停止するだけ。 |
| `activateTimeLimit()` | `useTimeLimit`時のみ既存を止め、時間制限コルーチンを開始する。 |
| `stopActivateTimeLimit()` | 制限コルーチンを止め、`timeLimitInProcess`をfalseにする。 |
| `activateUpdateAbility()` | `updateAbilityActive`時のみ更新コルーチンを開始し、処理中フラグを立てる。 |
| `stopActivateUpdateAbility()` | 更新コルーチンを止め、`updateAbilityInProcess`をfalseにする。 |
| `setCoolDownDurationValue(float newValue)` | `coolDownDuration`を設定するだけ。 |
| `getCoolDownDurationValue()` | `coolDownDuration`を返すだけ。 |
| `setTimeLimitValue(float newValue)` | `timeLimit`を設定するだけ。 |
| `getTimeLimitValue()` | `timeLimit`を返すだけ。 |
| `setUseCoolDownValue(bool state)` | `useCoolDown`を設定するだけ。 |
| `setUseTimeLimitValue(bool state)` | `useTimeLimit`を設定するだけ。 |
| `setUseEnergyOnAbilityValue(bool state)` | `useEnergyOnAbility`を設定するだけ。 |
| `setEnergyAmountUsedValue(float newValue)` | `energyAmountUsed`を設定するだけ。 |
| `setUseInputOnPressDownState(bool state)` | `useInputOnPressDown`を設定するだけ。 |
| `setUseInputOnPressHoldState(bool state)` | `useInputOnPressHold`を設定するだけ。 |
| `setUseInputOnPressUpState(bool state)` | `useInputOnPressUp`を設定するだけ。 |
| `isCoolDownInProcess()` | `coolDownInProcess`をそのまま返す。 |
| `isTimeLimitInProcess()` | `timeLimitInProcess`をそのまま返す。 |
| `enableOrDisableAbilityFromEditor(bool state)` | 有効状態を設定し`updateComponent`でシーンを更新する。 |
| `enableOrDisableAllAbilitiesCanBeShownOnWheelFromEditor(bool state)` | ホイール表示可否を設定し`updateComponent`でシーンを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnTimeLimitBefore` | `UnityEvent` | – |
| `eventOnTimeLimitAfter` | `UnityEvent` | – |
| `eventOnCoolDownActivate` | `UnityEvent` | – |
| `eventOnSetCurrentAbility` | `UnityEvent` | – |
| `eventOnUseAbility` | `UnityEvent` | – |
| `eventToDeactivateAbility` | `UnityEvent` | – |
| `eventToCallToCheckConditionOnPressDown` | `UnityEvent` | – |
| `eventToCallToCheckConditionOnPressUp` | `UnityEvent` | – |
