# sharedActionButtonActivator

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Action System/Shared Action System/sharedActionButtonActivator.cs:6`

**概要**: プレイヤー側の共有アクション起動を扱うコンポーネント。アクション名と有効状態を保持し、ランダム指定や一定時間だけの有効化に対応する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Button Activator Enabled | `buttonActivatorEnabled` | `bool` | true | – |
| Button Active | `buttonActive` | `bool` | – | – |
| Set Active State On Start | `setActiveStateOnStart` | `bool` | – | – |
| Shared Action Name On Start | `sharedActionNameOnStart` | `string` | – | – |
| Use Random Shared Action Name | `useRandomSharedActionName` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Shared Action Name | `sharedActionName` | `string` | – | – |
| Current Time To Disable Activator | `currentTimeToDisableActivator` | `float` | – | – |
| Current External Character | `currentExternalCharacter` | `GameObject` | – | – |
| Check To Disable Activator In Process | `checkToDisableActivatorInProcess` | `bool` | – | – |

### Event Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shared Action Event Info List | `sharedActionEventInfoList` | `List<sharedActionEventInfo>` | new List<sharedActionEventInfo> () | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events It Target Detected | `useEventsItTargetDetected` | `bool` | – | – |
| Events It Target Detected | `eventsItTargetDetected` | `UnityEvent` | – | – |
| Use Events It Target Not Detected | `useEventsItTargetNotDetected` | `bool` | – | – |
| Events It Target Not Detected | `eventsItTargetNotDetected` | `UnityEvent` | – | – |
| Event On Assigning New Info | `eventOnAssigningNewInfo` | `UnityEvent` | – | – |
| Event To Send New Action Name | `eventToSendNewActionName` | `eventParameters.eventToCallWithString` | – | – |
| Event On Enable Activator | `eventOnEnableActivator` | `UnityEvent` | – | – |
| Event On Disable Activator | `eventOnDisableActivator` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Shared Action System | `mainSharedActionSystem` | `sharedActionSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setuseRandomSharedActionNameState(bool state)` | `useRandomSharedActionName`に`state`を設定するだけ。 |
| `enableActivatorAndSetSharedActioName(string newName)` | アクティベータを有効化したうえで`setSharedActionName`に`newName`を渡す。 |
| `setSharedActionName(string newName)` | 有効時のみ`sharedActionName`を更新し、名前設定イベントと一致リストのイベントを発火する。 |
| `setSharedActionNameAndEnableWithDuration(string newName)` | `newName`を`;`で名前と秒数に分割し、名前設定と`enableActivatorWithDuration`を行う。 |
| `setExternalCharacter(GameObject newCharacter)` | `currentExternalCharacter`に`newCharacter`を設定するだけ。 |
| `activateRandomSharedActionByName()` | `useRandomSharedActionName`を一時的に有効にして起動し、元の値に戻す。 |
| `activateSharedActionByName()` | 有効状態と外部キャラを確認して共有アクションを起動し、成否に応じたイベントを発火する。 |
| `enableActivator()` | `enableOrDisableaActivator(true)`を呼ぶだけ。 |
| `disableActivator()` | `enableOrDisableaActivator(false)`を呼ぶだけ。 |
| `enableOrDisableaActivator(bool state)` | 有効時のみ`buttonActive`を`state`にしてアクティブ状態変更イベントを発火する。 |
| `enableActivatorWithDuration(float newDuration)` | `enableOrDisableActivatorWithDuration(true, newDuration)`を呼ぶだけ。 |
| `disableActivatorWithDuration()` | 実行中または待機中なら`enableOrDisableActivatorWithDuration(false, 0)`を呼ぶ。 |
| `enableOrDisableActivatorWithDuration(bool state, float newDuration)` | コルーチンを止めて時間を設定し、有効時は指定秒後に自動で無効化する処理を開始、無効時は即イベントを発火する。 |
| `stopUpdateCoroutine()` | `updateCoroutine`が実行中なら停止するだけ。 |
| `setButtonActivatorEnabledState(bool state)` | `buttonActivatorEnabled`に`state`を設定するだけ。 |
| `setButtonActivatorEnabledStateFromEditor(bool state)` | 状態を設定した後、`updateComponent`でシーンを更新するエディタ用関数。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventsItTargetDetected` | `UnityEvent` | – |
| `eventsItTargetNotDetected` | `UnityEvent` | – |
| `eventOnAssigningNewInfo` | `UnityEvent` | – |
| `eventOnEnableActivator` | `UnityEvent` | – |
| `eventOnDisableActivator` | `UnityEvent` | – |

## 内部型

- `sharedActionEventInfo`（class）
