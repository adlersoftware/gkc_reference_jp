# vendorSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vendor System/vendorSystem.cs:5`

**概要**: ベンダーの在庫リストを保持するコンポーネントで、`inventoryListManager`のカテゴリ/要素インデックスから商品を複製し、価格・在庫数・最低購入レベルを設定します。在庫のセーブ/ロード用の処理も持ちます。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use General Buy Price Multiplier | `useGeneralBuyPriceMultiplier` | `bool` | – | 全商品の購入価格に共通の倍率を掛けるか。 |
| General Buy Price Multiplayer Percentage | `generalBuyPriceMultiplayerPercentage` | `float` | – | 購入価格に掛ける共通の倍率の値。 / 表示条件: `useGeneralBuyPriceMultiplier` がオンのとき |
| Use General Sell Price Multiplier | `useGeneralSellPriceMultiplier` | `bool` | – | 全商品の売却価格に共通の倍率を掛けるか。 |
| General Sell Price Multiplayer Percentage | `generalSellPriceMultiplayerPercentage` | `float` | – | 売却価格に掛ける共通の倍率の値。 / 表示条件: `useGeneralSellPriceMultiplier` がオンのとき |
| Infinite Vendor Amount Available | `infiniteVendorAmountAvailable` | `bool` | – | 全商品の在庫を無限扱いにするか。 |

### Main Inventory Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Game System Manager | `gameSystemManager` | `gameManager` | – | 在庫の保存に使う`gameManager`の参照。 |
| Main Inventory Manager | `mainInventoryManager` | `inventoryListManager` | – | 商品の元データを提供する`inventoryListManager`。 |

### Save/Load Vendor Inventory Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Load Current Vendor Inventory From Save File | `loadCurrentVendorInventoryFromSaveFile` | `bool` | – | セーブデータから在庫を読み込むか。 |
| Save Current Vendor Inventory To Save File | `saveCurrentVendorInventoryToSaveFile` | `bool` | – | 在庫をセーブデータへ保存するか。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `inventoryListManagerList` | `List<inventoryListElement>` | new List<inventoryListElement> () | – |
| `vendorInventoryList` | `List<inventoryInfo>` | new List<inventoryInfo> () | – |
| `inventoryManagerListString` | `string[]` | – | – |
| `inventoryManagerStringInfoList` | `List<inventoryManagerStringInfo>` | new List<inventoryManagerStringInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setNewInventoryListManagerList(List<inventoryListElement> newList)` | `inventoryListManagerList`を差し替えるだけ。 |
| `setInventoryFromInventoryListManager()` | 各要素の`inventoryInfo`を複製し、数量・価格・無限在庫・最低レベルを反映して`vendorInventoryList`に追加する。 |
| `getVendorInventoryList()` | `vendorInventoryList`を返すだけ。 |
| `setVendorInventoryList(List<inventoryInfo> newVendorInventoryList)` | 渡されたリストのコピーを`vendorInventoryList`に代入するだけ。 |
| `getInventoryListManagerList()` | カテゴリ名と商品名から`inventoryManagerStringInfoList`を再構築してコンポーネントを更新するエディタ用処理。 |
| `setInventoryObjectListNames()` | 各要素の`Name`を`inventoryObjectName`に揃えてコンポーネントを更新するだけ。 |
| `addNewInventoryObjectToInventoryListManagerList()` | 名前"New Object"の`inventoryListElement`を追加してコンポーネントを更新するだけ。 |
| `saveCurrentVendorListToFile()` | `gameManager`を探して`saveGameInfoFromEditor("Vendor")`を呼び、保存後にコンポーネントを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とシーンのダーティ更新を行うだけ。 |

## 内部型

- `inventoryManagerStringInfo`（class）
