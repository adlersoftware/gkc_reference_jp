# objectiveStationSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Objectives Mission System/objectiveStationSystem.cs:6`

**概要**: ステーションのミッション一覧と進行インデックスを保持する。プレイヤーUIへの受け渡し、ミッション状態の確認、レベル内ミッションの収集を行う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Character Objective Panel | `useCharacterObjectivePanel` | `bool` | – | – |
| Current Character Objective Index | `currentCharacterObjectiveIndex` | `int` | – | – |
| Start Mission After Pressing Closing Station | `startMissionAfterPressingClosingStation` | `bool` | – | – |
| Use Delay To Start Mission | `useDelayToStartMission` | `bool` | – | – |
| Delay To Start Mission | `delayToStartMission` | `float` | – | – |

### Objective Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Objective Info List | `objectiveInfoList` | `List<objectiveInfo>` | new List<objectiveInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Objective Station | `usingObjectiveStation` | `bool` | – | – |
| First Time Missions State Checked | `firstTimeMissionsStateChecked` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Mission Availables | `eventOnMissionAvailables` | `UnityEvent` | – | – |
| Event On All Missions Complete | `eventOnAllMissionsComplete` | `UnityEvent` | – | – |

### Explanation

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Explanation | `explanation` | `string` | "This is a station system which " + … | TextArea (5, 20) |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkMissionsState()` | 各ミッションの完了/報酬状態を調べ、未達があれば`eventOnMissionAvailables`を、全達成なら`eventOnAllMissionsComplete`を発火する。 |
| `setCurrentPlayer(GameObject player)` | プレイヤーを保持し、その`playerComponentsManager`から目標ステーションUIを取得して参照を更新する。 |
| `activateObjectiveStation()` | 使用中フラグを反転し、開く時は自ステーションをUIに渡し、閉じる時は状態確認を行ってからメニューを開閉する。 |
| `setUsingObjectiveStationState(bool state)` | `usingObjectiveStation`を使用中かどうかの状態に設定するだけ。 |
| `getObjectiveInfoList()` | このステーションに設定されたミッション情報リストを返すだけ。 |
| `increaseCurrentCharacterObjectiveIndex()` | 現在のミッションインデックスを1増やし、一覧数を超えないよう末尾で止める。 |
| `setCurrentCharacterObjectiveIndex(int newIndex)` | ミッションインデックスを指定値にし、一覧数を超える場合は末尾に補正する。 |
| `getCurrentCharacterObjectiveIndex()` | 現在のミッションインデックスを返すだけ。 |
| `isThereMissionsAvailableOnStation(int indexMissionToCheck)` | 指定インデックス以前のミッションを調べ、未完了または再挑戦可能なものがあればtrueを返す。 |
| `getAllMissionsSystemOnLevel()` | 一覧をクリアしてレベル内の全`objectiveEventSystem`を集め、それぞれの情報を追加してシーンを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`でこのコンポーネントとシーンを更新するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnMissionAvailables` | `UnityEvent` | – |
| `eventOnAllMissionsComplete` | `UnityEvent` | – |

## 内部型

- `objectiveInfo`（class）
