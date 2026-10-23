# GKCUIManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/GKCUIManager.cs:7`

**概要**: 名前付きUI要素のリストをまとめて、または個別に有効/無効化し、名前検索やエディタ上での選択も行うUI管理コンポーネント。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Manager Enabled | `managerEnabled` | `bool` | true | OFFにするとUI要素の有効/無効切替を一切行わない。 |

### UI Object Searcher

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Name To Search | `objectSearcherName` | `string` | – | UI要素名を部分一致で検索するための入力文字列。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `UIElementInfoList` | `List<UIElementInfo>` | new List<UIElementInfo> () | – |
| `objectSearchResultList` | `List<string>` | new List<string> () | – |
| `searchObjectsActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableAllUIElement()` | `UIElementInfoList`の全UI要素を有効化する。 |
| `disableAllUIElement()` | `UIElementInfoList`の全UI要素を無効化する。 |
| `enableOrDisableAllUIElement(bool state)` | 各要素名を指定して`enableOrDisableUIElement`を`state`で呼び出す。 |
| `enableUIElement(string objectName)` | `objectName`のUI要素を有効化する。 |
| `disableUIElement(string objectName)` | `objectName`のUI要素を無効化する。 |
| `enableOrDisableUIElement(string objectName, bool state)` | `objectName`の要素を`state`にしてGameObjectを切り替え、対応イベントを発火して保存する。 |
| `clearObjectsSearcResultList()` | 検索結果リストを空にし、検索名と`searchObjectsActive`をリセットする。 |
| `showObjectsBySearchName()` | 検索名を小文字化し、名前と追加タグの部分一致を`objectSearchResultList`に詰める。 |
| `selectObjectByName(string objectName)` | `objectName`に一致する要素のインデックスを`selectObjectByIndex`に渡す。 |
| `selectObjectByIndex(int index)` | `index`番の要素の`UIGameObject`をエディタ上で選択状態にする。 |

## 内部型

- `UIElementInfo`（class）
