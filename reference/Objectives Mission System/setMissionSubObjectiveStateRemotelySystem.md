# setMissionSubObjectiveStateRemotelySystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Objectives Mission System/setMissionSubObjectiveStateRemotelySystem.cs:6`

**概要**: 遠隔イベントなどからミッションのサブ目標完了やキャンセルを`objectiveManager`へ指示するコンポーネント。カウンター方式やリモートイベントにも対応する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Mission Info Enabled | `setMissionInfoEnabled` | `bool` | true | – |
| Mission ID | `missionID` | `int` | – | – |
| Mission Scene | `missionScene` | `int` | -1 | – |
| Sub Objective Name | `subObjectiveName` | `string` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Objective Counter Instead Of List | `useObjectiveCounterInsteadOfList` | `bool` | – | – |
| Increaset Counter To Current Mission Active | `increasetCounterToCurrentMissionActive` | `bool` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Events | `useRemoteEvents` | `bool` | – | – |
| Remove Event Name List | `removeEventNameList` | `List<string>` | new List<string> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Sub Objective Complete | `useEventOnSubObjectiveComplete` | `bool` | – | – |
| Event On Sub Objective Complete | `eventOnSubObjectiveComplete` | `UnityEvent` | – | – |
| Use Event On Sub Objective Cancelled | `useEventOnSubObjectiveCancelled` | `bool` | – | – |
| Event On Sub Objective Complete Cancelled | `eventOnSubObjectiveCompleteCancelled` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `addSubObjectiveCompleteRemotely(string customSubObjectiveName)` | 引数のサブ目標名をそのまま`sendMissionInfo`へ渡すだけ。 |
| `addSubObjectiveCompleteRemotely()` | 保持している`subObjectiveName`を`sendMissionInfo`へ渡すだけ。 |
| `sendMissionInfo(string newSubObjectiveName)` | 有効時のみ`objectiveManager`を取得し、カウンター加算かサブ目標完了を指示し、リモートイベント処理と完了イベントを行う。 |
| `cancelCurrentMissionRemotely()` | 有効時のみ`objectiveManager`に`missionScene`と`missionID`で現ミッションのキャンセルを指示し、必要ならイベントを発火する。 |
| `setMissionID(int newValue)` | `missionID`を指定値に設定するだけ。 |
| `increaseMissionID()` | `missionID`を1増やすだけ。 |
| `decreaseMissionID()` | `missionID`を1減らし、負にならないよう0で止める。 |
| `setSubObjectiveName(string newValue)` | `subObjectiveName`を指定文字列に設定するだけ。 |
| `setMissionInfoEnabledState(bool state)` | `setMissionInfoEnabled`を指定状態に設定するだけ。 |
| `setMissionInfoEnabledStateFromEditor(bool state)` | `setMissionInfoEnabledState`を呼んだ後、コンポーネントとシーンを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnSubObjectiveComplete` | `UnityEvent` | – |
| `eventOnSubObjectiveCompleteCancelled` | `UnityEvent` | – |
