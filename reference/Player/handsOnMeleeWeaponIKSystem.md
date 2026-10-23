# handsOnMeleeWeaponIKSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `OnAnimatorIKComponent`
- **ソース**: `Player/Animator IK/handsOnMeleeWeaponIKSystem.cs:7`

**概要**: 近接武器を持っているときに両手を武器へ合わせるIKコンポーネント。`handInfoList` の手ごとの目標と重みを使い、多忙状態では重みを滑らかに落とす。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Adjust Hands Enabled | `adjustHandsEnabled` | `bool` | true | – |
| Weight Lerp Speed | `weightLerpSpeed` | `float` | 6 | – |
| Busy Body Part Weight Lerp Speed | `busyBodyPartWeightLerpSpeed` | `float` | 3 | – |
| Min Wait Time To Active Hands | `minWaitTimeToActiveHands` | `float` | 0.3f | – |

### Hands Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hand Info List | `handInfoList` | `List<handInfo>` | new List<handInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Hands On Melee Active | `handsOnMeleeActive` | `bool` | – | – |
| Using Hands | `usingHands` | `bool` | – | – |
| Is Busy | `isBusy` | `bool` | – | – |
| Adjust Hands Paused | `adjustHandsPaused` | `bool` | – | – |
| Smooth Busy Disable Active | `smoothBusyDisableActive` | `bool` | – | – |
| Hands Check Paused With Delay Active | `handsCheckPausedWithDelayActive` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Active State Change | `useEventsOnActiveStateChange` | `bool` | – | – |
| Event On Active | `eventOnActive` | `UnityEvent` | – | – |
| Event On Deactivate | `eventOnDeactivate` | `UnityEvent` | – | – |

### Component Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Animator | `animator` | `Animator` | – | – |
| IK Manager | `IKManager` | `IKSystem` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Main Melee Weapons Grabbed Manager | `mainMeleeWeaponsGrabbedManager` | `meleeWeaponsGrabbedManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `playerIsBusy()` | 手使用中・非一人称・FF/無重力・近接/死亡/停止中・ジェットパック等なら true を返す。 |
| `setWeightLerpSpeedValue(float newValue)` | `weightLerpSpeed` を設定するだけ。 |
| `setOriginalWeightLerpSpeed()` | 保存値 `originalWeightLerpSpeed` で `setWeightLerpSpeedValue` を呼ぶだけ。 |
| `setAdjustHandsPausedState(bool state)` | `adjustHandsPaused` を設定するだけ。 |
| `setSmoothBusyDisableActiveState(bool state)` | `smoothBusyDisableActive` を設定するだけ。 |
| `setAdjustHandsEnabledState(bool state)` | `adjustHandsEnabled` を設定するだけ。 |
| `enableHandsCheckPausedWithDelayActive(float duration)` | 既存の遅延コルーチンを止め、指定時間後に再開するコルーチンを開始する。 |
| `stopUpdateDelayToResumeStateCoroutine()` | 遅延コルーチンを停止し、`handsCheckPausedWithDelayActive` を false にする。 |
| `disableStateIfNotCurrentlyActiveOnIKSystem()` | IKManager 上で現在のコンポーネントでなければ `setActiveState(false)` を呼ぶ。 |
| `setAdjustHandsEnabledStateFromEditor(bool state)` | 値を設定してから `updateComponent` を呼ぶ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnActive` | `UnityEvent` | – |
| `eventOnDeactivate` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`enableBothHands()`, `enableOnlyLeftHand()`, `enableOnlyRightHand()`, `enableOrDisableRightOrLeftHand(bool state, bool isRightHand, bool setStateOnBothHands)`, `setActiveState(bool state)`, `updateOnAnimatorIKState()`

</details>

## 内部型

- `handInfo`（class）
