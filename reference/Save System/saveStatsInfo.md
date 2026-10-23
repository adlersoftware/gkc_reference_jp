# saveStatsInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `saveGameInfo`
- **ソース**: `Save System/Custom Class To Save/saveStatsInfo.cs:8`

**概要**: `playerStatsSystem`の各ステータスの現在値とbool状態を保存し、ロード時に`ignoreStatInitializationOnLoadGame`を除いて復元する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Stats System | `mainPlayerStatsSystem` | `playerStatsSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveGameContent(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)` | `getPersistanceList`の統計リストを同一スロット・`playerID`へ上書きし、`BinaryFormatter`で保存する。 |
| `loadGameContent(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 保存スロットから`playerID`の`statsList`を`persistanceInfoList`へ読み込み、`loadInfoOnMainComponent`で現在値を復元する。 |
| `getPersistanceList(int playerID, bool showDebugInfo)` | `statInfoList`の`currentValue`と`currentBoolState`を写し、`extraCurrentValue`の分を差し引いて0以上へ`Clamp`する。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`initializeValuesOnComponent()`, `loadGame(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `saveGame(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)`

</details>
