# saveInventoryBankInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `saveGameInfo`
- **ソース**: `Save System/Custom Class To Save/saveInventoryBankInfo.cs:8`

**概要**: インベントリバンクの在庫（名前・数量・カテゴリ／要素インデックス）を保存し、ロード時に`inventoryListElement`の新しいリストとして復元する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Inventory Bank Manager | `mainInventoryBankManager` | `inventoryBankManager` | – | – |
| Main Inventory Manager Name | `mainInventoryManagerName` | `string` | "Main Inventory Manager" | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveGameContent(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)` | `bankInventoryList`を`inventoryObjectList`へ変換し、同一`saveNumber`の先頭エントリを上書きして保存する。 |
| `loadGameContent(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 保存された`inventoryObjectList`を`inventoryListElement`へ変換して`persistanceInfoList`を作り、バンクの在庫として適用する。 |
| `getPersistanceList(int playerID, bool showDebugInfo)` | `bankInventoryList`を走査し、`Name`・`amount`・`infiniteAmount`・`categoryIndex`・`elementIndex`を`persistanceInventoryObjectInfo`へ写す。 |
| `saveGameContentFromEditor(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo)` | エディタ用に`getPersistanceVendorListElement`で`inventoryListManagerList`を取得し、`File.Create`で保存ファイルを上書きする。 |
| `getPersistanceVendorListElement(int playerID, bool showDebugInfo)` | `mainInventoryBankManager.inventoryListManagerList`を走査し、`inventoryObjectName`などを`persistanceInventoryObjectInfo`へ変換して返す。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`loadGame(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `saveGame(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)`, `saveGameFromEditor(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo)`

</details>
