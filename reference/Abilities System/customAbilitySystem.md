# customAbilitySystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `abilityInfo`
- **ソース**: `Abilities System/Custom Abilities/customAbilitySystem.cs:6`

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Press Down | `useEventOnPressDown` | `bool` | – | – |
| Event On Press Down | `eventOnPressDown` | `UnityEvent` | – | – |
| Use Event On Press Hold | `useEventOnPressHold` | `bool` | – | – |
| Event On Press Hold | `eventOnPressHold` | `UnityEvent` | – | – |
| Use Event On Press Up | `useEventOnPressUp` | `bool` | – | – |
| Event On Press Up | `eventOnPressUp` | `UnityEvent` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Press Delay Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Delay Time To Use Event On Press Up | `useDelayTimeToUseEventOnPressUp` | `bool` | – | – |
| Delay Time To Use Event On Press Up | `delayTimeToUseEventOnPressUp` | `float` | – | – |
| Use Event On Press Up Before And After | `useEventOnPressUpBeforeAndAfter` | `bool` | – | – |
| Event On Press Up Before | `eventOnPressUpBefore` | `UnityEvent` | – | – |
| Event On Press Up After | `eventOnPressUpAfter` | `UnityEvent` | – | – |
| Delay Time To Use Event On Press Up Before | `delayTimeToUseEventOnPressUpBefore` | `float` | – | – |
| Delay Time To Use Event On Press Up After | `delayTimeToUseEventOnPressUpAfter` | `float` | – | – |
| Use Delay Time To Use Event On Press Hold | `useDelayTimeToUseEventOnPressHold` | `bool` | – | – |
| Delay Time To Use Event On Press Hold | `delayTimeToUseEventOnPressHold` | `float` | – | – |
| Use Event On Press Hold Just Once | `useEventOnPressHoldJustOnce` | `bool` | – | – |

### Other Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Update Ability State | `useEventOnUpdateAbilityState` | `bool` | – | – |
| Event On Update Ability State | `eventOnUpdateAbilityState` | `UnityEvent` | – | – |
| Use Event On Enable Ability | `useEventOnEnableAbility` | `bool` | – | – |
| Event On Enable Ability | `eventOnEnableAbility` | `UnityEvent` | – | – |
| Use Event On Disable Ability | `useEventOnDisableAbility` | `bool` | – | – |
| Event On Disable Ability | `eventOnDisableAbility` | `UnityEvent` | – | – |
| Use Event On Deactivate Ability | `useEventOnDeactivateAbility` | `bool` | – | – |
| Event On Deactivate Ability | `eventOnDeactivateAbility` | `UnityEvent` | – | – |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnPressDown` | `UnityEvent` | – |
| `eventOnPressHold` | `UnityEvent` | – |
| `eventOnPressUp` | `UnityEvent` | – |
| `eventOnPressUpBefore` | `UnityEvent` | – |
| `eventOnPressUpAfter` | `UnityEvent` | – |
| `eventOnUpdateAbilityState` | `UnityEvent` | – |
| `eventOnEnableAbility` | `UnityEvent` | – |
| `eventOnDisableAbility` | `UnityEvent` | – |
| `eventOnDeactivateAbility` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`activateSecondaryActionOnAbility()`, `deactivateAbility()`, `disableAbility()`, `enableAbility()`, `updateAbilityState()`, `useAbilityPressDown()`, `useAbilityPressHold()`, `useAbilityPressUp()`

</details>
