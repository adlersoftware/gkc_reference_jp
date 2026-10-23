# savePlayerOptionsInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `saveGameInfo`
- **ソース**: `Save System/Custom Class To Save/savePlayerOptionsInfo.cs:8`

**概要**: `playerOptionsEditorSystem`の各オプション現在値（スクロールバー／スライダー／トグル／ドロップダウン）を保存・復元する。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Options Editor System | `mainPlayerOptionsEditorSystem` | `playerOptionsEditorSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveGameContent(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)` | `getPersistanceList`で取得した`optionsList`を同一スロットへ上書きし、`saveInfoOnRegularTxtFile`ならテキストにも出力する。 |
| `loadGameContent(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 保存スロットから`playerID`の`optionsList`を`persistanceInfoList`へ読み込み、`loadInfoOnMainComponent`で各オプションへ適用する。 |
| `getPersistanceList(int playerID, bool showDebugInfo)` | `optionInfoList`を走査し、`optionName`とスクロールバー／スライダー／トグル／ドロップダウンの現在値を写す。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkSaveInfoToLoadOnStartOnAllScenes(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `loadGame(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `saveGame(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)`

</details>
