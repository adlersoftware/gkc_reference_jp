# oxygenSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/oxygenSystem.cs:8`

**概要**: 酸素残量・消費レート・回復レートを管理し、`oxygenStateInfo`単位で使用中の消費や音・イベントを切り替える。残量が尽きると死亡イベントを発火し、スライダーとテキストのUIも更新する。

**公式ドキュメント抜粋**（[Oxygen System](../../docs/player-controller-components/non-essential-components/oxygen-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Oxygen System Enabled | `oxygenSystemEnabled` | `bool` | true | – |
| Oxygen Use Rate | `oxygenUseRate` | `float` | – | – |
| Close To Empty Oxygen Amount | `closeToEmptyOxygenAmount` | `float` | – | – |
| Oxygen Amount | `oxygenAmount` | `float` | – | – |
| Refill Oxygen Rate | `refillOxygenRate` | `float` | 18 | – |
| Refill Oxygen Delay After Use | `refillOxygenDelayAfterUse` | `float` | – | – |
| Oxygen Object Always Active | `oxygenObjectAlwaysActive` | `bool` | – | – |
| Time To Disable Oxygen Object | `timeToDisableOxygenObject` | `float` | – | – |
| Wait To Oxygen Filled To Use Again | `waitToOxygenFilledToUseAgain` | `bool` | – | – |
| Event On Oxygen Depleted Rate | `eventOnOxygenDepletedRate` | `float` | – | – |
| Use Oxygen UI On Screen On Any View | `useOxygenUIOnScreenOnAnyView` | `bool` | – | – |

### UI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Regular Oxygen Color | `regularOxygenColor` | `Color` | – | – |
| Close To Empty Oxygen Color | `closeToEmptyOxygenColor` | `Color` | – | – |
| Regular Oxygen Text Color | `regularOxygenTextColor` | `Color` | – | – |
| Close To Empty Oxygen Text Color | `closeToEmptyOxygenTextColor` | `Color` | – | – |

### Oxygen States Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Oxygen State Info List | `oxygenStateInfoList` | `List<oxygenStateInfo>` | new List<oxygenStateInfo> () | – |
| Oxygen State Name By Default | `oxygenStateNameByDefault` | `string` | "Oxygen On Space" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Oxygen Empty | `oxygenEmpty` | `bool` | – | – |
| Refilling Oxygen | `refillingOxygen` | `bool` | – | – |
| Using Oxygen | `usingOxygen` | `bool` | – | – |
| Oxygen Refilled | `oxygenRefilled` | `bool` | true | – |
| First Person Active | `firstPersonActive` | `bool` | – | – |
| Current Oxygen State Info | `currentOxygenStateInfo` | `oxygenStateInfo` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Oxygen Refilled | `eventOnOxygenRefilled` | `UnityEvent` | – | – |
| Event On Oxygen Empty | `eventOnOxygenEmpty` | `UnityEvent` | – | – |
| Event On Oxygen Depleted | `eventOnOxygenDepleted` | `UnityEvent` | – | – |
| Event On Oxygen Active | `eventOnOxygenActive` | `UnityEvent` | – | – |
| Event On Oxygen Deactivate | `eventOnOxygenDeactivate` | `UnityEvent` | – | – |
| Event On Oxygen Empty Death | `eventOnOxygenEmptyDeath` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Oxygen Slider | `oxygenSlider` | `Image` | – | – |
| Oxygen Amount Text | `oxygenAmountText` | `Text` | – | – |
| Oxygen Object | `oxygenObject` | `GameObject` | – | – |
| First Person Oxygen Panel | `firstPersonOxygenPanel` | `GameObject` | – | – |
| First Person Oxygen Amount Text | `firstPersonOxygenAmountText` | `Text` | – | – |
| Main Health | `mainHealth` | `health` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateOxygenState(string oxygenStateName)` | `setOxygenStateByName`で状態を選んでから`activeOxygenState`を呼ぶだけ。 |
| `disableOxygenState(string oxygenStateName)` | 名前で状態を選んでから`disableOxygenState`を呼ぶだけ。 |
| `activeOxygenState()` | 未使用で残量があれば、回復を止めて`usingOxygen`を立て、酸素関連のイベントを発火する。 |
| `disableOxygenState()` | 使用を終了して`refillOxygen`で回復を開始し、パネルを閉じて停止イベントを発火する。 |
| `refillOxygen(float refillDelay)` | 既存の回復コルーチンを止め、`refillDelay`秒後から回復するコルーチンを開始する。 |
| `stopRefillCoroutine()` | 実行中の`refillCoroutine`があれば停止するだけ。 |
| `refillOxygenDirectly()` | 酸素が空か使用中なら即座に最大値まで戻し、UI更新と回復済みフラグの設定を行う。 |
| `increaseTotalOxygenAmount(float extraValue)` | 現在値と最大値を`originalOxygenAmount + extraValue`に更新し、`auxOxygenAmount`も合わせる。 |
| `initializeOxygenAmount(float newValue)` | `oxygenAmount`に`newValue`を代入するだけ。 |
| `initializeOxygenUseRate(float newValue)` | `oxygenUseRate`に`newValue`を代入するだけ。 |
| `increaseOxygenUseRate(float newValue)` | `oxygenUseRate`に`newValue`を加算するだけ。 |
| `updateOxygenAmountWithoutUpdatingStatManager(int statId, float amount)` | 現在値と最大値・補助値を`amount`に揃えるだけで、`statId`は使わない。 |
| `updateOxygenUseRateAmountWithoutUpdatingStatManager(int statId, float amount)` | `oxygenUseRate`を`amount`にするだけで、`statId`は使わない。 |
| `getOxygen(float amount)` | `oxygenAmount`に`amount`を加えてUIと上限を更新し、回復イベントを発火して空状態を解除する。 |
| `getOxygenAmountToLimit()` | `originalOxygenAmount - auxOxygenAmount`を返すだけ。 |
| `addAuxOxygenAmount(float amount)` | `auxOxygenAmount`に`amount`を加算するだけ。 |
| `disableOxygenOnDeath()` | 使用を止めて停止イベントと`eventOnOxygenEmptyDeath`を発火し、時間の記録をリセットする。 |
| `setFirstPersonActiveState(bool state)` | `firstPersonActive`に`state`を代入するだけ。 |
| `setOxygenSystemEnabledState(bool state)` | `oxygenSystemEnabled`に`state`を代入するだけ。 |
| `setOxygenSystemEnabledStateFromEditor(bool state)` | 有効フラグを変更してから`updateComponent`でエディタへ反映する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnOxygenRefilled` | `UnityEvent` | – |
| `eventOnOxygenEmpty` | `UnityEvent` | – |
| `eventOnOxygenDepleted` | `UnityEvent` | – |
| `eventOnOxygenActive` | `UnityEvent` | – |
| `eventOnOxygenDeactivate` | `UnityEvent` | – |
| `eventOnOxygenEmptyDeath` | `UnityEvent` | – |

## 内部型

- `oxygenStateInfo`（class）
