# selectObjectManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/selectObjectManager.cs:6`

**概要**: エディタ用のオブジェクト選択支援で、名前検索した結果から階層上の対象を選択する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Select Info List | `objectToSelectInfoList` | `List<objectToSelectInfo>` | new List<objectToSelectInfo> () | – |
| Explanation | `explanation` | `string` | "Press the o button on any of the bel… | TextArea (3, 10) |
| Object Search Result List | `objectSearchResultList` | `List<string>` | new List<string> () | – |
| Object Searcher Name | `objectSearcherName` | `string` | "" | – |
| Search Objects Active | `searchObjectsActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `clearObjectsSearcResultList()` | `objectSearchResultList`を空にし、検索語と`searchObjectsActive`も初期化する。 |
| `showObjectsBySearchName()` | `objectSearcherName`を小文字化し、名前や追加タグに一致する項目を`objectSearchResultList`へ重複なく追加する。 |
| `selectObjectByName(string objectName)` | `objectName`と一致する項目を探して`selectObjectByIndex`を呼ぶ。 |
| `selectObjectByIndex(int index)` | 指定項目がコンポーネント選択ならメニューコマンドを実行し、そうでなければ対象`GameObject`をエディタでアクティブにする。 |

## 内部型

- `objectToSelectInfo`（class）
