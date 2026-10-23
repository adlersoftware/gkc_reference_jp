# inventoryBankManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/inventoryBankManager.cs:5`

**概要**: インベントリの「銀行（倉庫）」側の在庫リストを管理するコンポーネント。起動時に `inventoryListManager` から在庫を複製し、名前指定で追加・数量取得・削除とエディタ用ヘルパーを提供する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Inventory Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Game System Manager | `gameSystemManager` | `gameManager` | – | エディタからのバンク保存に使う`gameManager`。 |
| Main Inventory Manager | `mainInventoryManager` | `inventoryListManager` | – | アイテム定義を参照する`inventoryListManager`。 |
| Use Max Inventory Bank Slots Amount | `useMaxInventoryBankSlotsAmount` | `bool` | – | オンでバンクの最大スロット数を制限する。 |
| Max Inventory Bank Slots Amount | `maxInventoryBankSlotsAmount` | `int` | – | バンクに置ける最大スロット数。 / 表示条件: `useMaxInventoryBankSlotsAmount` がオンのとき |

### Save/Load Bank Inventory Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Load Current Bank Inventory From Save File | `loadCurrentBankInventoryFromSaveFile` | `bool` | – | オンで起動時にセーブからバンク在庫を読み込む。 |
| Save Current Bank Inventory To Save File | `saveCurrentBankInventoryToSaveFile` | `bool` | – | オンでバンク在庫をセーブデータに書き込む。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `inventoryListManagerList` | `List<inventoryListElement>` | new List<inventoryListElement> () | – |
| `bankInventoryList` | `List<inventoryInfo>` | new List<inventoryInfo> () | – |
| `inventoryManagerListString` | `string[]` | – | – |
| `inventoryManagerStringInfoList` | `List<inventoryManagerStringInfo>` | new List<inventoryManagerStringInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setNewInventoryListManagerList(List<inventoryListElement> newList)` | `inventoryListManagerList` を `newList` で置き換えるだけ。 |
| `setInventoryFromInventoryListManager()` | `mainInventoryManager` のカテゴリ／要素インデックスから `inventoryInfo` を複製し、在庫リストに追加する。 |
| `getBankInventoryList()` | `bankInventoryList` をそのまま返すだけ。 |
| `addInventoryObjectByName(string objectName, int amountToAdd)` | 同名要素があれば数量を加算し、無ければ `mainInventoryManager` から情報を複製して `amountToAdd` で新規追加する。 |
| `getInventoryObjectAmountByName(string inventoryObjectName)` | 同名オブジェクトの合計数量を返し、1 つも無ければ -1 を返す。 |
| `removeObjectAmountFromInventory(string objectName, int amountToRemove)` | 同名要素の数量を減算し、0 以下になった要素はリストから削除する。 |
| `getInventoryListManagerList()` | エディタ用にカテゴリ名と要素名の配列を作り直し、`updateComponent` を呼ぶ。 |
| `setInventoryObjectListNames()` | 各要素の `Name` を `inventoryObjectName` で上書きし、`updateComponent` を呼ぶ。 |
| `addNewInventoryObjectToInventoryListManagerList()` | 名前が「New Object」の `inventoryListElement` を追加して `updateComponent` を呼ぶ。 |
| `saveCurrentInventoryListToFile()` | `gameManager` を検索して「Inventory Bank」としてセーブし、`updateComponent` を呼ぶ。 |
| `updateComponent()` | `GKC_Utils.updateComponent` と `updateDirtyScene` でインスペクタとシーンを更新する。 |

## 内部型

- `inventoryManagerStringInfo`（class）
