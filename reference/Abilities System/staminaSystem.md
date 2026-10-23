# staminaSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/staminaSystem.cs:7`

**概要**: スタミナ値・最大値・消費レート・回復コルーチンを管理するコンポーネント。名前付きのスタミナ状態ごとに使用中フラグや空/回復イベントを持ち、円形/通常スライダーや残量テキストのUIも更新する。

**公式ドキュメント抜粋**（[Stamina System](../../docs/player-controller-components/elements-used-by-other-components/stamina-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Stamina Enabled | `useStaminaEnabled` | `bool` | true | – |
| Show Stamina UI Enabled | `showStaminaUIEnabled` | `bool` | true | – |
| Regular Stamina Color | `regularStaminaColor` | `Color` | – | – |
| Close To Empty Stamina Color | `closeToEmptyStaminaColor` | `Color` | – | – |
| Close To Empty Stamina Amount | `closeToEmptyStaminaAmount` | `float` | – | – |
| Stamina Amount | `staminaAmount` | `float` | – | – |

### Refill Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Auto Refill Stamina Enabled | `autoRefillStaminaEnabled` | `bool` | true | – |
| Hide Stamina UI After Delay If No Auto Refill Enabled | `hideStaminaUIAfterDelayIfNoAutoRefillEnabled` | `bool` | – | – |
| Refill Stamina Rate | `refillStaminaRate` | `float` | 18 | – |
| Refill Stamina Delay After Use | `refillStaminaDelayAfterUse` | `float` | – | – |
| Refill Stamina Delay After Empty | `refillStaminaDelayAfterEmpty` | `float` | – | – |
| Wait To Stamina Filled To Use Again | `waitToStaminaFilledToUseAgain` | `bool` | – | – |

### Stamina UI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Stamina Object Always Active | `staminaObjectAlwaysActive` | `bool` | – | – |
| Time To Disable Stamina Object | `timeToDisableStaminaObject` | `float` | – | – |
| Use Fade | `useFade` | `bool` | – | – |
| Fade Speed | `fadeSpeed` | `float` | – | – |
| Enabled Alpha Value | `enabledAlphaValue` | `float` | – | – |
| Use Slider Circle | `useSliderCircle` | `bool` | true | – |

### Stamina States Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Stamina State Info List | `staminaStateInfoList` | `List<staminaStateInfo>` | new List<staminaStateInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Stamina Empty | `staminaEmpty` | `bool` | – | – |
| Refilling Stamina | `refillingStamina` | `bool` | – | – |
| Using Stamina | `usingStamina` | `bool` | – | – |
| Stamina Refilled | `staminaRefilled` | `bool` | true | – |
| Stamina Use Paused | `staminaUsePaused` | `bool` | – | – |
| Total Stamina Rate Amount | `totalStaminaRateAmount` | `float` | – | – |
| Custom Refill Stamina Delay After Use | `customRefillStaminaDelayAfterUse` | `float` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| UI Elements Assigned | `UIElementsAssigned` | `bool` | true | – |
| Circle Stamina Slider | `circleStaminaSlider` | `Image` | – | – |
| Stamina Amount Text | `staminaAmountText` | `Text` | – | – |
| Stamina Panel | `staminaPanel` | `GameObject` | – | – |
| Regular Stamina Slider | `regularStaminaSlider` | `Slider` | – | – |
| Stamina Canvas Group | `staminaCanvasGroup` | `CanvasGroup` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `anyStaminaStateInUse()` | スタミナ状態リストを走査し、`staminaStateInUse`が立っている状態が1つでもあるかを返す。 |
| `activeStaminaStateWithCustomAmount(string staminaName, float customAmountToUse, float newDelayAfterUse)` | 指定名の状態を確認して`customAmountToUse`分を一度に消費し、大きい`newDelayAfterUse`は再回復待ちに反映する。 |
| `activeStaminaState(string staminaName)` | 指定状態の消費レートを加算して`usingStamina`を立て回復を止め、空なら`eventOnStaminaEmpty`を発火する。 |
| `useStaminaStateByName(string staminaName)` | `useStaminaStateOnce`を一時的に立てて`activeStaminaState`を呼び、状態を一度だけ消費させる。 |
| `setStaminaStateAsPaused(string staminaName)` | 指定名の状態を`setStaminaPausedState`で停止状態にするだけ。 |
| `setStaminaStateAsNotPaused(string staminaName)` | 指定名の状態の一時停止を`setStaminaPausedState`で解除するだけ。 |
| `setStaminaPausedState(bool state, string staminaName)` | 状態の`stateInPause`を設定し、停止時は設定に応じ`disableStaminaState`も呼ぶ。 |
| `useAllRemainStamina()` | 残りの`staminaAmount`を`useStaminaAmountExternally`で全消費する。0なら何もしない。 |
| `useStaminaAmountExternally(float amount)` | 回復を止めて`customRefillStaminaDelayAfterUse`を1にしてから、`amount`分を外部消費する。 |
| `setCustomRefillStaminaDelayAfterUseValue(float newValue)` | `customRefillStaminaDelayAfterUse`に`newValue`を代入するだけ。 |
| `disableStaminaState(string staminaName)` | 状態の使用フラグを下ろして消費レートを減算し、合計が0以下なら`usingStamina`を解除する。 |
| `disableCurrentStaminaState()` | 使用中のスタミナ状態のうち最初に見つかった1つを`disableStaminaState`で停止する。 |
| `refillStamina(float refillDelay)` | 既存の回復コルーチンを止め、`refillDelay`秒待ってから回復するコルーチンを開始する。 |
| `stopRefillCoroutine()` | 実行中の`refillCoroutine`があれば停止するだけ。 |
| `getStamina(float amount)` | `staminaAmount`に`amount`を加算してUIと上限を更新し、`staminaEmpty`を解除して回復イベントを発火する。 |
| `refillFullStamina()` | `getStamina`に`originalStaminaAmount`を渡し、満タンまで回復させるだけ。 |
| `setStaminaSliderAlphaValue(float value)` | UIがある場合に`staminaCanvasGroup.alpha`へ`value`を設定するだけ。 |
| `increaseTotalStaminaAmount(float extraValue)` | 現在値と最大値を最大値+`extraValue`に更新し、通常スライダーの`maxValue`も変更する。 |
| `getCurrentStaminaAmount()` | `staminaAmount`を返すだけ。 |
| `getOriginalStaminaAmount()` | `originalStaminaAmount`を返すだけ。 |
| `initializeStaminaAmount(float newValue)` | `staminaAmount`に`newValue`を代入するだけ。 |
| `updateStaminaAmountWithoutUpdatingStatManager(int statId, float amount)` | `staminaAmount`を`amount`にするだけで、`statId`は使わない。 |
| `updateRefillStaminaRateAmountWithoutUpdatingStatManager(int statId, float amount)` | `refillStaminaRate`を`amount`にするだけで、`statId`は使わない。 |
| `increaseTotalRefillStaminaRate(float extraValue)` | `refillStaminaRate`に`extraValue`を加算するだけ。 |
| `initializeRefillStaminaRate(float newValue)` | `refillStaminaRate`に`newValue`を代入するだけ。 |
| `setStaminaUsePausedState(bool state)` | `staminaUsePaused`に`state`を代入するだけ。 |
| `setStaminaRefilledOrEmptyOnStateList(bool state)` | 有効な全状態に対し、`state`に応じ回復/空のイベントを発火する。 |
| `getStaminaAmountToLimit()` | `originalStaminaAmount - auxStaminaAmount`を返すだけ。 |
| `addAuxStaminaAmount(float amount)` | `auxStaminaAmount`に`amount`を加算するだけ。 |
| `setUseStaminaEnabledState(bool state)` | `useStaminaEnabled`に`state`を代入するだけ。 |
| `setShowStaminaUIEnabledState(bool state)` | `showStaminaUIEnabled`を設定し、オフ時はプレイ中ならスタミナパネルを非表示にする。 |
| `setShowStaminaUIEnabledStateOnEditor(bool state)` | 上のUI表示設定を呼び出した後、`updateComponent`でコンポーネントとシーンを更新する。 |
| `setUseStaminaEnabledStateFromEditor(bool state)` | `useStaminaEnabled`を設定してから`updateComponent`でエディタ上の反映を行う。 |

## 内部型

- `staminaStateInfo`（class）
