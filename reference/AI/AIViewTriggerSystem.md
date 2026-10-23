# AIViewTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/AIViewTriggerSystem.cs:5`

**概要**: トリガーの進入・退出時に、UnityEventの呼び出しと`findObjectivesSystem`への容疑者登録/解除を行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Trigger Enabled | `checkTriggerEnabled` | `bool` | true | – |
| On Trigger Enter | `onTriggerEnter` | `bool` | – | – |
| On Trigger Exit | `onTriggerExit` | `bool` | – | – |
| Send Detected Object As Suspect On Enter | `sendDetectedObjectAsSuspectOnEnter` | `bool` | true | – |
| Remove Detected Object As Suspect On Exit | `removeDetectedObjectAsSuspectOnExit` | `bool` | true | – |
| Send Detected Object As Target To Check On Enter | `sendDetectedObjectAsTargetToCheckOnEnter` | `bool` | – | – |
| Remove Detected Object As Target To Check On Exit | `removeDetectedObjectAsTargetToCheckOnExit` | `bool` | – | – |

### Regular Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events | `useEvents` | `bool` | – | – |
| On Trigger Enter Event | `onTriggerEnterEvent` | `UnityEvent` | new UnityEvent () | – |
| On Trigger Exit Event | `onTriggerExitEvent` | `UnityEvent` | new UnityEvent () | – |

### Events With Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use On Trigger Enter Event With Object | `useOnTriggerEnterEventWithObject` | `bool` | – | – |
| On Trigger Enter Event With Object | `onTriggerEnterEventWithObject` | `eventParameters.eventToCallWithGameObject` | – | – |
| Use On Trigger Exit Event With Object | `useOnTriggerExitEventWithObject` | `bool` | – | – |
| On Trigger Exit Event With Object | `onTriggerExitEventWithObject` | `eventParameters.eventToCallWithGameObject` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTrigger(Collider col, bool isEnter)` | `isEnter`で進入/退出を分け、設定に応じイベント呼び出しと容疑者・確認対象の登録/解除を行う。 |
| `callEvent(UnityEvent eventToCall)` | 受け取った`UnityEvent`を`Invoke`するだけ。 |
| `callEventWithObject(eventParameters.eventToCallWithGameObject eventToCall, GameObject objectToSend)` | `GameObject`を引数に取るイベントを、渡されたオブジェクトで`Invoke`するだけ。 |
| `setCheckTriggerEnabledState(bool state)` | `checkTriggerEnabled`を`state`に設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `onTriggerEnterEvent` | `UnityEvent` | – |
| `onTriggerExitEvent` | `UnityEvent` | – |
