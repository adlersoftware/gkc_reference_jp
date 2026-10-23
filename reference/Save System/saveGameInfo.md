# saveGameInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Save System/Custom Class To Save/saveGameInfo.cs:5`

**概要**: 各コンポーネント固有のデータをセーブ/ロードするための基底クラス。全メソッドが空の`virtual`で、派生クラスによる上書きを前提とする。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Game Saved On Home Menu | `gameSavedOnHomeMenu` | `bool` | – | – |
| Ignore Player ID On Save Load Info | `ignorePlayerIDOnSaveLoadInfo` | `bool` | – | – |
| Ignore Save Number On Save Load Info | `ignoreSaveNumberOnSaveLoadInfo` | `bool` | – | – |
| Save Number To Ignore Save Load Info | `saveNumberToIgnoreSaveLoadInfo` | `int` | -1 | – |
| Save Info On Regular Txt File | `saveInfoOnRegularTxtFile` | `bool` | – | – |
| Save Info On Regula File Name | `saveInfoOnRegulaFileName` | `string` | – | – |
| Load Info On Regula File Name | `loadInfoOnRegulaFileName` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveGame(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)` | 本体が空で何もしない。派生クラスで上書きする`virtual`メソッド。 |
| `loadGame(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 本体が空で何もしない。派生クラスで上書きする`virtual`メソッド。 |
| `saveGameFromEditor(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 本体が空で何もしない。派生クラスで上書きする`virtual`メソッド。 |
| `initializeValuesOnComponent()` | 本体が空で何もしない。派生クラスで上書きする`virtual`メソッド。 |
| `deleteGameInfo(int saveNumberToDelete, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 本体が空で何もしない。派生クラスで上書きする`virtual`メソッド。 |
| `copyGameInfo(int saveNumberToStoreDuplicate, int saveNumberToDuplicate, int playerID, string currentSaveDataPath, bool copyAllInfoWithoutChecks, bool showDebugInfo)` | 本体が空で何もしない。派生クラスで上書きする`virtual`メソッド。 |
| `showSaveInfoDebug(int saveNumberToShow, int playerID, string currentSaveDataPath, bool showAllGameInfoDebug, bool showDebugInfo)` | 本体が空で何もしない。派生クラスで上書きする`virtual`メソッド。 |
| `checkSaveInfoToLoadOnStartOnAllScenes(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 本体が空で何もしない。派生クラスで上書きする`virtual`メソッド。 |
