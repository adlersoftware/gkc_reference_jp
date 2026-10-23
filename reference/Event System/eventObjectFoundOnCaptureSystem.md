# eventObjectFoundOnCaptureSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Event System/eventObjectFoundOnCaptureSystem.cs:6`

**概要**: オブジェクトを捕獲・発見した時に`UnityEvent`を1回（設定次第で複数回）呼ぶ小規模コンポーネント。検出オブジェクトを引数で渡すイベントも選べる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event Enabled | `eventEnabled` | `bool` | true | – |
| Call Event Multiple Times | `callEventMultipleTimes` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Event Triggered | `eventTriggered` | `bool` | – | – |
| Event Triggered With Game Object | `eventTriggeredWithGameObject` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Call On Capture | `eventToCallOnCapture` | `UnityEvent` | – | – |
| Use Event To Send Object | `useEventToSendObject` | `bool` | – | – |
| Event To Send Object | `eventToSendObject` | `eventParameters.eventToCallWithGameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `callEventOnCapture()` | 有効かつ未発動なら`eventToCallOnCapture`を呼び、`callEventMultipleTimes`でなければ発動済みフラグを立てる。 |
| `callEventOnCaptureWithGameObject(GameObject newObject)` | `useEventToSendObject`時、オブジェクトが非nullで未発動なら`eventToSendObject`に渡して呼び、必要なら発動済みにする。 |
| `setEventEnabledState(bool state)` | `eventEnabled`を設定するだけの薄いセッター。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToCallOnCapture` | `UnityEvent` | – |
