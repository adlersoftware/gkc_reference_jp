# objectiveManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Objectives Mission System/objectiveManager.cs:5`

**概要**: シーン内の全ステーションとミッションを束ねるシングルトンマネージャ。IDとシーンでミッションを検索し、遠隔からの達成・中断処理を取り次ぐ。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Mission Scene | `missionScene` | `int` | – | – |

### Objective Station System List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Objective Station System List | `objectiveStationSystemList` | `List<objectiveStationSystem>` | new List<objectiveStationSystem> () | – |

### Prefabs List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer To Place Objects | `layerToPlaceObjects` | `LayerMask` | – | – |
| Mission Station Prefab | `missionStationPrefab` | `GameObject` | – | – |
| Mission System Prefab | `missionSystemPrefab` | `GameObject` | – | – |
| Empty Mission Station Prefab | `emptyMissionStationPrefab` | `GameObject` | – | – |
| Character Mission System Prefab | `characterMissionSystemPrefab` | `GameObject` | – | – |

### Other Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Explanation | `explanation` | `string` | "This is the main mission manager, an… | TextArea (5, 20) |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 初期化済みなら何もせず、重複インスタンスなら自身を破棄し、そうでなければ静的`Instance`に自身を登録する。 |
| `getObjectiveEventSystem(int missionID, int missionSceneToSearch)` | リストが空なら`getAllStationSystemOnLevel`で収集し、IDとシーン一致のミッションを返す。 |
| `getAllStationSystemOnLevel()` | `objectiveStationSystem`を全検索して重複なくリストへ格納し、`updateComponent`でシーンを更新する。 |
| `getAllStationSystemOnLevelAndAssignInfoToAllMissions()` | 全ステーションを収集した後、各ミッションへ0から連番のIDと`missionScene`を割り当ててシーンを更新する。 |
| `getAllStationSystemOnLevelByEditor()` | エディタ用に全ステーションを収集し直し、`updateComponent`でシーンを更新する。 |
| `clearStationSystemList()` | `objectiveStationSystemList`を空にしてシーンを更新するだけ。 |
| `instantiateMissionStation()` | `missionStationPrefab`を`instantateObjectOnLevel`に渡してシーン上に生成する。 |
| `instantiateMissionSystem()` | `missionSystemPrefab`を`instantateObjectOnLevel`に渡してシーン上に生成する。 |
| `instantiateEmptyMissionSystem()` | `emptyMissionStationPrefab`を`instantateObjectOnLevel`に渡してシーン上に生成する。 |
| `instantiateCharacterMissionSystem()` | `characterMissionSystemPrefab`を`instantateObjectOnLevel`に渡してシーン上に生成する。 |
| `instantateObjectOnLevel(GameObject objectToInstantiate)` | エディタカメラから`layerToPlaceObjects`へレイを飛ばし、命中点の少し上にプレハブを生成する。 |
| `addSubObjectiveCompleteRemotely(string subObjectiveName, int missionScene, int missionID)` | ID一致（`missionScene`が-1なら任意）のミッションを探して`addSubObjectiveComplete`を呼び、最初の一致で終了する。 |
| `increaseObjectiveCounterRemotely(int missionScene, int missionID)` | ID一致（`missionScene`が-1なら任意）のミッションへ`increaseObjectiveCounter`を遠隔から呼び出して終了する。 |
| `increaseObjectiveCounterRemotelyToCurrentMissionActive(int missionScene)` | 実行中で`missionScene`条件に合うミッションへ`increaseObjectiveCounter`を呼び出す。 |
| `checkRemoteEventsOnSubObjectiveCompleteRemotely(List<string> removeEventNameList, int missionScene, int missionID)` | ID一致（`missionScene`が-1なら任意）のミッションへイベント名リストを渡し、遠隔イベントを実行させる。 |
| `checkRemoteEventsOnSubObjectiveCompleteRemotelyToCurrentMissionActive(List<string> removeEventNameList, int missionScene)` | 実行中で`missionScene`条件に合うミッションへイベント名リストを渡し、遠隔イベントを実行させる。 |
| `cancelCurrentMissionRemotely(int missionScene, int missionID)` | IDとシーンでミッションを取得し、存在すれば`cancelCurrentMissionRemotely`で中断させる。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`を呼び、エディタ上の変更をシーンへ反映する。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |
