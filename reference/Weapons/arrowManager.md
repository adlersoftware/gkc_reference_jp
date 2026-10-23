# arrowManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/arrowManager.cs:7`

**概要**: 弓の矢をインベントリの個数と連動させ、HUDの矢パネル・個数・種類アイコンを更新する管理クラス。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Arrows Enabled | `useArrowsEnabled` | `bool` | true | – |
| Current Arrow Inventory Object Name | `currentArrowInventoryObjectName` | `string` | "Regular Arrow" | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Arrows Found On Inventory | `eventOnArrowsFoundOnInventory` | `UnityEvent` | – | – |
| Event On Arrows Not Found On Inventory | `eventOnArrowsNotFoundOnInventory` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Arrow Info Panel | `arrowInfoPanel` | `GameObject` | – | – |
| Arrow Amount Text | `arrowAmountText` | `Text` | – | – |
| Arrow Type Icon | `arrowTypeIcon` | `RawImage` | – | – |
| Infinite Arrows Icon | `infiniteArrowsIcon` | `GameObject` | – | – |
| Main Inventory Manager | `mainInventoryManager` | `inventoryManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableArrowInfoPanel(bool state)` | 矢機能が有効なときだけ、`arrowInfoPanel`のアクティブ状態を`state`に合わせる。 |
| `checkIfArrowsFoundOnInventory()` | 矢の個数を取得し、0より多ければ発見イベント、そうでなければ未発見イベントを呼ぶ。 |
| `useArrowFromInventory(int amountToUse)` | 在庫を確認して矢があれば`amountToUse`個をインベントリから減らし、表示を更新する。 |
| `updateArrowAmountText()` | インベントリから矢の個数を取り直し、負値を0に補正して`arrowAmountText`へ表示する。 |
| `setCurrentArrowInventoryObjectName(string newName)` | `currentArrowInventoryObjectName`を`newName`に変更するだけ。 |
| `setArrowTypeIcon(Texture newIcon, bool useInfiniteArrows)` | アイコンにテクスチャを設定し、無限矢なら専用アイコンを出して個数表示を隠す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnArrowsFoundOnInventory` | `UnityEvent` | – |
| `eventOnArrowsNotFoundOnInventory` | `UnityEvent` | – |
