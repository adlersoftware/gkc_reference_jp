# checkCollisionType

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/checkCollisionType.cs:5`

**概要**: 衝突・トリガーの開始/終了/滞在を設定フラグで振り分け、UnityEventやSendMessageで外部へ通知する検出コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Collisions Enabled | `checkCollisionsEnabled` | `bool` | true | – |
| On Collision Enter | `onCollisionEnter` | `bool` | – | – |
| On Collision Exit | `onCollisionExit` | `bool` | – | – |
| On Trigger Enter | `onTriggerEnter` | `bool` | – | – |
| On Trigger Exit | `onTriggerExit` | `bool` | – | – |
| On Trigger Stay | `onTriggerStay` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Parent | `parent` | `GameObject` | – | – |
| Object To Collide | `objectToCollide` | `GameObject` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Active | `active` | `bool` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Send Message Functions Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| On Collision Enter Function Name | `onCollisionEnterFunctionName` | `string` | – | – |
| On Collision Exit Function Name | `onCollisionExitFunctionName` | `string` | – | – |
| On Trigger Enter Function Name | `onTriggerEnterFunctionName` | `string` | – | – |
| On Trigger Exit Function Name | `onTriggerExitFunctionName` | `string` | – | – |
| On Trigger Stay Function Name | `onTriggerStayFunctionName` | `string` | – | – |

### Regular Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events | `useEvents` | `bool` | – | – |
| On Collision Enter Event | `onCollisionEnterEvent` | `UnityEvent` | new UnityEvent () | – |
| On Collision Exit Event | `onCollisionExitEvent` | `UnityEvent` | new UnityEvent () | – |
| On Trigger Enter Event | `onTriggerEnterEvent` | `UnityEvent` | new UnityEvent () | – |
| On Trigger Exit Event | `onTriggerExitEvent` | `UnityEvent` | new UnityEvent () | – |
| On Trigger Stay Event | `onTriggerStayEvent` | `UnityEvent` | new UnityEvent () | – |

### Events With Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use On Collision Enter Event With Object | `useOnCollisionEnterEventWithObject` | `bool` | – | – |
| On Collision Enter Event With Object | `onCollisionEnterEventWithObject` | `eventParameters.eventToCallWithGameObject` | – | – |
| Use On Collision Exit Event With Object | `useOnCollisionExitEventWithObject` | `bool` | – | – |
| On Collision Exit Event With Object | `onCollisionExitEventWithObject` | `eventParameters.eventToCallWithGameObject` | – | – |
| Use On Trigger Enter Event With Object | `useOnTriggerEnterEventWithObject` | `bool` | – | – |
| On Trigger Enter Event With Object | `onTriggerEnterEventWithObject` | `eventParameters.eventToCallWithGameObject` | – | – |
| Use On Trigger Exit Event With Object | `useOnTriggerExitEventWithObject` | `bool` | – | – |
| On Trigger Exit Event With Object | `onTriggerExitEventWithObject` | `eventParameters.eventToCallWithGameObject` | – | – |
| Use On Trigger Stay Event With Object | `useOnTriggerStayEventWithObject` | `bool` | – | – |
| On Trigger Stay Event With Object | `onTriggerStayEventWithObject` | `eventParameters.eventToCallWithGameObject` | – | – |

### Events With Collision Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Send On Collision Enter Info Event | `sendOnCollisionEnterInfoEvent` | `bool` | – | – |
| On Collision Enter Info Event | `onCollisionEnterInfoEvent` | `eventParameters.eventToCallWithCollision` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkOnCollision(Collision col, bool isEnter)` | `isEnter`で衝突開始/終了を選び、条件が揃えばイベント送信と`active`の更新を行う。 |
| `checkTrigger(Collider col, bool isEnter)` | `isEnter`に応じてトリガー開始/終了のイベントとSendMessageを実行し、`active`をtrueにする。 |
| `checkTriggerOnState(Collider col)` | `OnTriggerStay`用に滞在中のイベントとSendMessageを実行し、`active`をtrueにする。 |
| `checkTriggerWithGameObject(GameObject obj, bool isEnter)` | `Collider`の代わりにGameObjectを受け取ってトリガーの開始/終了処理を行う。 |
| `callEvent(UnityEvent eventToCall)` | `eventToCall.Invoke()`を呼ぶだけ。 |
| `callEventWithObject(eventParameters.eventToCallWithGameObject eventToCall, GameObject objectToSend)` | `objectToSend`を引数に`eventToCall.Invoke`を呼ぶだけ。 |
| `setCheckCollisionsEnabledState(bool state)` | `checkCollisionsEnabled`を`state`にするだけ。 |
| `checkSendOnCollisionEnterInfoEvent(Collision collision)` | `sendOnCollisionEnterInfoEvent`が有効なら衝突情報イベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `onCollisionEnterEvent` | `UnityEvent` | – |
| `onCollisionExitEvent` | `UnityEvent` | – |
| `onTriggerEnterEvent` | `UnityEvent` | – |
| `onTriggerExitEvent` | `UnityEvent` | – |
| `onTriggerStayEvent` | `UnityEvent` | – |
