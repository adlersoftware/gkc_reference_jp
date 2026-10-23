# saveVendorInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `saveGameInfo`
- **ソース**: `Save System/Custom Class To Save/saveVendorInfo.cs:8`

**概要**: ベンダー在庫の数量・価格・売値・購入最小レベル・スポーン設定を保存し、ロード時にベンダー在庫として復元する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Vendor System | `mainVendorSystem` | `vendorSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveGameContent(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)` | `vendorInventoryList`を変換して同一`saveNumber`の`playerInventoryList[0]`へ上書きし、在庫を保存する。 |
| `loadGameContent(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 保存された`playerInventoryList[0]`を`inventoryListElement`へ変換し、`vendorPrice`・`sellPrice`なども含めて`persistanceInfoList`に詰める。 |
| `getPersistanceList(int playerID, bool showDebugInfo)` | `vendorInventoryList`を走査し、`vendorPrice`・`sellPrice`・`minLevelToBuy`・`spawnObject`などを`persistanceInventoryObjectInfo`へ写す。 |
| `saveGameContentFromEditor(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo)` | エディタ用に`getPersistanceVendorListElement`の在庫を取得し、`File.Create`で保存ファイルを丸ごと上書きする。 |
| `getPersistanceVendorListElement(int playerID, bool showDebugInfo)` | `mainVendorSystem.inventoryListManagerList`を走査し、価格や購入条件を含む在庫情報を`persistanceInventoryObjectInfo`へ変換する。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`loadGame(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `saveGame(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)`, `saveGameFromEditor(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo)`

</details>
