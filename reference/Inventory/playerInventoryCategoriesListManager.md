# playerInventoryCategoriesListManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/playerInventoryCategoriesListManager.cs:9`

**概要**: インベントリのカテゴリ一覧パネルと、カテゴリ選択によるスロット表示の絞り込みを管理する UI コンポーネント。複数カテゴリの同時選択にも対応する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Category Selected Icon Color | `categorySelectedIconColor` | `Color` | – | – |
| Categor Un Selected Icon Color | `categorUnSelectedIconColor` | `Color` | – | – |

### Category Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Category Info List | `categoryInfoList` | `List<categoryInfo>` | new List<categoryInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Category List Panel Active | `categoryListPanelActive` | `bool` | – | – |
| Selecting Multiple Categories | `selectingMultipleCategories` | `bool` | – | – |
| Categories String List | `categoriesStringList` | `List<string>` | new List<string> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Categories Panel Opened | `eventOnCategoriesPanelOpened` | `UnityEvent` | – | – |
| Event On Categories Panel Closed | `eventOnCategoriesPanelClosed` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Category List Panel | `categoryListPanel` | `GameObject` | – | – |
| Inventory List Panel | `inventoryListPanel` | `RectTransform` | – | – |
| Inventory List Panel Scale On Category Opened | `inventoryListPanelScaleOnCategoryOpened` | `RectTransform` | – | – |
| Inventory List Panel Scale On Category Closed | `inventoryListPanelScaleOnCategoryClosed` | `RectTransform` | – | – |
| Main Inventory Manager | `mainInventoryManager` | `inventoryManager` | – | – |
| Inventory Slots Scrollbar | `inventorySlotsScrollbar` | `Scrollbar` | – | – |
| Combine Categories Icon | `combineCategoriesIcon` | `RawImage` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `selectInventoryCategoryList(List<string> categoryNameList)` | 複数選択が無効なら有効化し、`categoryNameList` の各カテゴリを `selectInventoryCategory` で順に選択する。 |
| `selectInventoryCategory(string categoryName)` | カテゴリの選択状態・アイコン色・表示スロットを更新し、スクロールをリセットしてスロットオプションを閉じる。 |
| `enableOrDisableCategoryListPanel()` | `categoryListPanelActive` を反転して `updateInventoryListPanelPosition` を呼ぶだけ。 |
| `enableCategoryListPanel()` | フラグを true にしてパネル位置を更新するだけ。 |
| `disableCategoryListPanel()` | フラグを false にしてパネル位置を更新するだけ。 |
| `updateInventoryListPanelPosition()` | 開閉イベントを発火し、パネルの active と `inventoryListPanel` の位置・サイズを開閉状態に合わせる。 |
| `enableAllCategories()` | `hideSlotOnMenu` でない全スロットのボタンを有効化し、スロットオプションを閉じる。 |
| `enableSelectingMultipleCategories()` | フラグを false にしてから反転メソッドを呼び、結果として複数選択を有効にする。 |
| `disableSelectingMultipleCategories()` | フラグを true にしてから反転メソッドを呼び、結果として複数選択を無効にする。 |
| `enableOrDisableSelectingMultipleCategories()` | `selectingMultipleCategories` を反転し、結合アイコンの色とカテゴリ名リストを更新する。 |
| `disableAllCategoriesIcons()` | 全カテゴリの `categorySelected` を false にし、下線アイコンとアイコン色を未選択状態へ戻す。 |
| `resetScroll()` | `inventorySlotsScrollbar.value` を 0 から 1 にするコルーチンを開始してスクロール位置をリセットする。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCategoriesPanelOpened` | `UnityEvent` | – |
| `eventOnCategoriesPanelClosed` | `UnityEvent` | – |

## 内部型

- `categoryInfo`（class）
