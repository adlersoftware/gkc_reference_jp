# objectToOverrideSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Override System/objectToOverrideSystem.cs:5`

**概要**: オーバーライド可能なオブジェクトに付ける設定コンポーネント。可否フラグと対象、開始・終了時のリモートイベント、外部からの制御開始・終了を提供する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Be Overriden | `canBeOverriden` | `bool` | true | – |
| Object To Override | `objectToOverride` | `GameObject` | – | – |

### Remote Events On Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Events On Object On Start | `useRemoteEventsOnObjectOnStart` | `bool` | – | – |
| Remote Event Name List On Object On Start | `remoteEventNameListOnObjectOnStart` | `List<string>` | new List<string> () | – |
| Use Remote Events On Object On End | `useRemoteEventsOnObjectOnEnd` | `bool` | – | – |
| Remote Event Name List On Object On End | `remoteEventNameListOnObjectOnEnd` | `List<string>` | new List<string> () | – |

### Remote Events On Player Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Events On Player On Start | `useRemoteEventsOnPlayerOnStart` | `bool` | – | – |
| Remote Event Name List On Player On Start | `remoteEventNameListOnPlayerOnStart` | `List<string>` | new List<string> () | – |
| Use Remote Events On Player On End | `useRemoteEventsOnPlayerOnEnd` | `bool` | – | – |
| Remote Event Name List On Player On End | `remoteEventNameListOnPlayerOnEnd` | `List<string>` | new List<string> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `canBeOverridenActive()` | `canBeOverriden`を返すだけ。 |
| `getObjectToOverride()` | `objectToOverride`が未設定なら自身を代入してから返す。 |
| `setCurrentPlayer(GameObject newPlayer)` | `currentPlayer`に`newPlayer`を設定するだけ。 |
| `setOverrideControlExternally(bool state)` | プレイヤーの制御系を取得し、`state`に応じて対象の操作を開始または停止し、停止入力の一時停止状態を設定する。 |
