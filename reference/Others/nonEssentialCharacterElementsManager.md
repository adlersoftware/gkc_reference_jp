# nonEssentialCharacterElementsManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/nonEssentialCharacterElementsManager.cs:7`

**概要**: キャラクターの装飾用オブジェクトをリスト管理するエディタ向けコンポーネントで、名前検索・選択・削除・一括の有効化/無効化を提供する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Information

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Explanation | `explanation` | `string` | "You can remove any of the elements o… | このリストの使い方と操作ボタンの説明文。 / TextArea (3, 15) |

### Object Searcher

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Name To Search | `objectSearcherName` | `string` | "" | 名前で要素を絞り込むための検索文字列。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `objectToSelectInfoList` | `List<objectToSelectInfo>` | new List<objectToSelectInfo> () | – |
| `objectSearchResultList` | `List<string>` | new List<string> () | – |
| `searchObjectsActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `clearObjectsSearcResultList()` | 検索結果・検索文字列・検索中フラグをすべて初期化する。 |
| `showObjectsBySearchName()` | 検索文字列に部分一致するオブジェクト名を重複なく検索結果リストへ追加する。 |
| `selectObjectByName(string objectName)` | 名前が一致する要素を探し、`selectObjectByIndex` で選択する。 |
| `selectObjectByIndex(int index)` | 指定インデックスのオブジェクトをエディタ上でアクティブにする。 |
| `removeObjectByName(string objectName)` | 名前が一致する要素を探し、単体破棄として削除する。 |
| `destroyAllObjects()` | プレハブを展開してから全要素を破棄し、リストを空にして更新する。 |
| `removeObjectByIndex(int index, bool destroyingSingleObject)` | 指定要素のオブジェクトを即時破棄してリストから外し、設定された破棄イベントを発火する。 |
| `updateObjectNames()` | 各要素の `Name` を実際のオブジェクト名で更新してシーンを更新する。 |
| `enableOrDisableObjectByName(string objectName, bool state)` | 名前一致の要素を探して有効/無効を切り替え、シーンを更新する。 |
| `enableOrDisableObjectByIndex(int index, bool state)` | 指定要素の `SetActive` を切り替え、設定に応じて有効/無効イベントを発火する。 |
| `enableOrDisableAllObjects(bool state)` | 全要素の `SetActive` を切り替え、それぞれの有効/無効イベントを発火して更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent` と `updateDirtyScene` で表示とシーンを更新する。 |

## 内部型

- `objectToSelectInfo`（class）
