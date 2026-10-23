# energyStationSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `craftingStationSystem`
- **ソース**: `Crafting System/energyStationSystem.cs:6`

**概要**: `craftingStationSystem`を継承したエネルギー供給ステーション。時間経過でエネルギーを消費・再充填し、出力接続先へ現在量と無限エネルギー状態を伝える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Energy Enabled | `energyEnabled` | `bool` | true | – |
| Energy Name | `energyName` | `string` | – | – |
| Max Energy Amount | `maxEnergyAmount` | `float` | – | – |
| Current Energy Amount | `currentEnergyAmount` | `float` | – | – |
| Use Energy Over Time | `useEnergyOverTime` | `bool` | – | – |
| Use Energy Rate | `useEnergyRate` | `float` | – | – |
| Energy Amount To Use Over Time | `energyAmountToUseOverTime` | `float` | – | – |
| Refill Energy After Time | `refillEnergyAfterTime` | `bool` | – | – |
| Time To Refill Energy | `timeToRefillEnergy` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Energy Active | `energyActive` | `bool` | – | – |
| Energy In Use | `energyInUse` | `bool` | – | – |
| Refilling Energy In Process | `refillingEnergyInProcess` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Events On Energy State Change Only If Output Socked Connected | `checkEventsOnEnergyStateChangeOnlyIfOutputSockedConnected` | `bool` | – | – |
| Use Events On Empty Energy | `useEventsOnEmptyEnergy` | `bool` | – | – |
| Events On Empty Energy | `eventsOnEmptyEnergy` | `UnityEvent` | – | – |
| Use Events On Refilled Energy | `useEventsOnRefilledEnergy` | `bool` | – | – |
| Events On Refilled Energy | `eventsOnRefilledEnergy` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の`updateCoroutine`を`StopCoroutine`で止めるだけ。 |
| `getCurrentEnergyAmount()` | `currentEnergyAmount`を返すだけ。 |
| `getEnergyName()` | `energyName`を返すだけ。 |
| `setEnergyActiveState(bool state)` | `energyActive`を設定し、trueで更新コルーチン停止、falseで開始して補充・使用中フラグを下ろす。 |
| `refillAllEnergy()` | `setCurrentEnergyAmount`で最大量まで補充するだけ。 |
| `removeAllEnergy()` | `setCurrentEnergyAmount`で0にするだけ。 |
| `setCurrentEnergyAmount(float newAmount)` | 現在量を設定し、`checkEnergyAmountState`で上限・下限をクランプして空/補充イベントを発火する。 |
| `addOrRemoveToCurrentEnergyAmount(float newAmount)` | 現在量に`newAmount`を加算し、上限・下限クランプと空/補充イベント判定を行う。 |
| `setEnergyInUseState(bool state)` | `energyInUse`を設定するだけ。 |
| `checkEventOnEmptyEnergy()` | 出力ソケット必須設定で未接続なら中断し、`useEventsOnEmptyEnergy`なら空イベントを発火する。 |
| `checkEventOnRefilledEnergy()` | 出力ソケット必須設定で未接続なら中断し、`useEventsOnRefilledEnergy`なら補充イベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventsOnEmptyEnergy` | `UnityEvent` | – |
| `eventsOnRefilledEnergy` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkStateOnRemoveOuput()`, `checkStateOnSetOuput()`

</details>
