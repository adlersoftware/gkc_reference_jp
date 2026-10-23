# saveMissionsInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `saveGameInfo`
- **ソース**: `Save System/Custom Class To Save/saveMissionsInfo.cs:8`

**概要**: `objectiveLogSystem`のミッション進行（ID・シーン・受注／進行／完了状態・サブ目標・報酬文言）を保存し、ロード時にミッション状態を再構築する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Objective Log System | `mainObjectiveLogSystem` | `objectiveLogSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveGameContent(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)` | `getPersistanceList`でミッション状態を集め、同一`saveNumber`・`playerID`の`missionsList`を置き換えて`BinaryFormatter`で保存する。 |
| `loadGameContent(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 保存スロットから`playerID`の`missionsList`を`persistanceInfoList`へ読み込み、`loadInfoOnMainComponent`でミッション状態を再構築する。 |
| `getPersistanceList(int playerID, bool showDebugInfo)` | `objectiveSlotInfoList`を走査し、`missionID`・`missionScene`・完了／進行フラグ・目標文言・`subObjectiveCompleteList`を写す。 |
| `debugMissionInfo(persistanceMissionInfo missinInfo)` | `persistanceMissionInfo`の主要フィールドを1行に連結して`print`するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`initializeValuesOnComponent()`, `loadGame(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `saveGame(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)`

</details>
