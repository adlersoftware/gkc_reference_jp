# remoteAnimatorEventTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Event System/remoteAnimatorEventTriggerSystem.cs:5`

**概要**: `remoteEventSystem.eventInfo`と同じ形式のリストを自前で持ち、名前一致で`UnityEvent`を呼ぶ簡易版。イベント名ごとの有効/無効の切り替えもできる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remote Events Enabled | `remoteEventsEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event Info List | `eventInfoList` | `List<remoteEventSystem.eventInfo>` | new List<remoteEventSystem.eventInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `callRemoteEvent(string eventName)` | 無効時は何もせず、名前一致の有効要素で`useRegularEvent`なら`UnityEvent`を呼び、必要なら無効化して抜ける。 |
| `setEnabledEventState(string eventName)` | `setEnabledOrDisabledEventState(true, eventName)`を呼ぶだけのラッパー。 |
| `setDisabledEventState(string eventName)` | `setEnabledOrDisabledEventState(false, eventName)`を呼ぶだけのラッパー。 |
| `setEnabledOrDisabledEventState(bool state, string eventName)` | 名前が一致する最初の要素の`eventEnabled`を設定して抜ける。 |
