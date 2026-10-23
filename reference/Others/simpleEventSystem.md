# simpleEventSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/simpleEventSystem.cs:6`

**概要**: 有効/無効の2種類（または通常1種類）のUnityEventを持ち、遅延付きの発火と状態保持を行う汎用イベントコンポーネント。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event Enabled | `eventEnabled` | `bool` | true | – |
| Use Events On Activate And Disabled | `useEventsOnActivateAndDisabled` | `bool` | true | – |
| Use Delay To Event | `useDelayToEvent` | `bool` | – | – |
| Delay To Event | `delayToEvent` | `float` | – | – |
| Activated | `activated` | `bool` | – | – |
| Call On Start | `callOnStart` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Event Coroutine Active | `eventCoroutineActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Call On Activate | `eventToCallOnActivate` | `UnityEvent` | new UnityEvent () | – |
| Event To Call On Disable | `eventToCallOnDisable` | `UnityEvent` | new UnityEvent () | – |
| Regular Event To Call | `regularEventToCall` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateDevice()` | `eventEnabled`なら、遅延設定に応じて`callEvent`を遅延実行または即時実行する。 |
| `callEvent()` | 有効/無効イベント使用時は`activated`を反転して対応イベントを、そうでなければ通常イベントを発火する。 |
| `setActivatedStateAndCallEvents(bool state)` | `activated`を`state`にして、その状態に対応するイベントを発火する。 |
| `setActivatedState(bool state)` | `activated`を`state`にするだけ。 |
| `callEventsForCurrentActivatedState()` | 現在の`activated`に応じた有効/無効イベントを発火する。 |
| `setEventEnabledState(bool state)` | `eventEnabled`を`state`にするだけ。 |
| `setDelayToEventValue(float newValue)` | `delayToEvent`を`newValue`にするだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToCallOnActivate` | `UnityEvent` | – |
| `eventToCallOnDisable` | `UnityEvent` | – |
| `regularEventToCall` | `UnityEvent` | – |
