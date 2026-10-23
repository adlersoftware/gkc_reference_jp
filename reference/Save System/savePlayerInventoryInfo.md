# savePlayerInventoryInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `saveGameInfo`
- **ソース**: `Save System/Custom Class To Save/savePlayerInventoryInfo.cs:8`

**概要**: プレイヤーインベントリの全アイテム情報（数量・装備・耐久度・弾数）とスロット数・クラフト情報を保存し、ロード時に復元する。

## インスペクター設定

### Other Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Assign Loaded Inventory If Empty | `ignoreAssignLoadedInventoryIfEmpty` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Persistance Info List | `persistanceInfoList` | `List<inventoryListElement>` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Inventory Manager | `mainInventoryManager` | `inventoryManagerInfo` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveGameContent(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)` | `getPersistanceList`の結果で同一`saveNumber`・`playerID`のエントリを丸ごと置換し、`gameSavedOnHomeMenu`も記録して保存する。 |
| `loadGameContent(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 保存データを`inventoryListElement`へ変換し、スロット数・ブループリント・クラフト情報も`mainInventoryManager`へ反映して復元する。 |
| `getPersistanceList(int playerID, bool showDebugInfo)` | 数量が正のアイテムだけを写し、装備・耐久度・弾数に加えてスロット数・クラフト情報・最後に持った武器名も収集する。 |
| `saveGameContentFromEditor(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo)` | エディタ用に`getPersistanceInventoryListElement`で現在の管理リストを取得し、`File.Create`で保存ファイルを上書きする。 |
| `getPersistanceInventoryListElement(int playerID, bool showDebugInfo)` | `getCurrentInventoryListManagerList`を走査し、`Name`・`amount`・`categoryIndex`・`elementIndex`だけを`persistanceInventoryObjectInfo`へ写す。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`initializeValuesOnComponent()`, `loadGame(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `saveGame(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)`, `saveGameFromEditor(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo)`

</details>
