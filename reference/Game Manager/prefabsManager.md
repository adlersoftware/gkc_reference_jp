# prefabsManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Game Manager/prefabsManager.cs:6`

**概要**: カテゴリ別にプレハブを登録・検索し、エディタでカメラ前方のレイキャスト位置へ配置するための管理コンポーネント。

**公式ドキュメント抜粋**（[Prefabs Manager](../../docs/additional-managers/prefabs-manager.md)）

> There is a system called Prefabs Manager, which allows to manage, instantiate and add prefabs to the scene easily, avoiding the need to search between folders. For this follow these steps: Go to the upper part of unity, in the options of the top, Game Kit Controller-Create Prefabs Manager. If there was a Prefabs Manager previously in the scene, it will select in the editor, else a new one will be placed on the scene and selected in the editor. Inside the Prefab Type Info List, you can find the current prefab categories configured and the different prefabs configured in each one along an explanation of what each category does. This list is mostly used to configure the prefabs of the project, where you can add your own, so you can use this system as well to place your new prefabs into the scene. Once you have your prefabs configured here (using the buttons to configure a path for the prefa…

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Prefabs Url | `prefabsUrl` | `string` | "Assets/Game Kit Controller/Prefabs/" | プレハブの取得元となるフォルダのパス。 |
| Layer To Place Objects | `layerToPlaceObjects` | `LayerMask` | – | 配置位置を決めるレイキャストの対象レイヤー。 |
| Place Objects Offset | `placeObjectsOffset` | `float` | 0.5f | 衝突点から上へずらして配置する高さ。 |
| See Prefab Types Explanation | `seePrefabTypesExplanation` | `bool` | – | プレハブ種別の説明文を表示するかどうか。 |

### Prefabs Searcher Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Prefab Name To Search | `prefabNameToSearch` | `string` | – | 名前の部分一致でプレハブを絞り込む文字列。 / 表示条件: `showPrefabsSearcher` がオンのとき |
| Prefab Category To Search | `prefabCategoryNameToSearch` | `string` | – | カテゴリ名でプレハブを絞り込む検索文字列。 / 表示条件: `showPrefabsSearcher` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `prefabTypeInfoList` | `List<prefabTypeInfo>` | new List<prefabTypeInfo> () | – |
| `prefabTypeInfoListToPlaceOnScene` | `List<prefabTypeInfo>` | new List<prefabTypeInfo> () | – |
| `prefabSearchResultList` | `List<prefabTypeInfo>` | new List<prefabTypeInfo> () | – |
| `searchComplete` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `placePrefabInScene(int typeIndex, int prefabIndex)` | エディタカメラ前方のレイのヒット位置に、指定プレハブをオフセット付きで生成して記録する。 |
| `addPrefab(int prefabTypeIndex)` | 指定カテゴリに「New Prefab」という名前の空`prefabInfo`を追加して更新する。 |
| `addPrefabType()` | 「New Type」という空カテゴリを`prefabTypeInfoList`の末尾に追加する。 |
| `addPrefabType(int prefabTypeIndex)` | 「New Type」カテゴリを指定インデックスの直後に挿入する。 |
| `getPrefabPath(string prefabType, string prefabName)` | カテゴリ名とプレハブ名から`prefabsUrl`以下のパス文字列を組み立てて返す。 |
| `updatePrefabsListToPlaceOnScene()` | `prefabTypeInfoList`を元に配置用リストを作り直し（プレハブ参照のみ複製）、エディタ状態を更新する。 |
| `makePrefabsSearchByName()` | `prefabNameToSearch`で名前を部分一致検索して結果リストを作り、`searchComplete`をtrueにする。 |
| `makePrefabsSearchByCategory()` | `prefabCategoryNameToSearch`でカテゴリ名を部分一致検索し、該当カテゴリの全プレハブを結果に格納する。 |
| `placePrefabInSceneByGameObject(GameObject objectToSearch)` | カテゴリ内で一致するプレハブGameObjectを探し、`placePrefabInScene`で配置する。 |
| `cleanSearchResults()` | 検索結果と検索語をクリアし、`searchComplete`をfalseにする。 |
| `getPrefabGameObject(string prefabName)` | 名前が小文字で一致するプレハブGameObjectを返し、無ければnullを返す。 |
| `spawnPrefabByName(string prefabName)` | 名前一致のプレハブを`placePrefabInScene`で配置し、無ければ警告を出す。 |
| `getPrefabSpawnOffset(string prefabName)` | 名前一致のプレハブの`positionToSpawnOffset`を返し、無ければ0を返す。 |
| `setURLWithNames(int prefabTypeIndex)` | 指定カテゴリ内プレハブの`Name`と`urlName`をGameObject名から設定し、未割当なら警告する。 |
| `getAndSetAllPrefabsInFolder(int prefabTypeIndex, bool searchOnSubFolders)` | エディタ限定で、カテゴリのフォルダから`.prefab`を読み込んで`prefabInfoList`を作り直す。 |
| `selectLastPrefabSpawned()` | 直前に生成したプレハブをエディタで選択し、参照をnullにする。 |
| `updateComponent()` | 自身の変更をエディタへ反映し、シーンをダーティにする。 |

## 内部型

- `prefabTypeInfo`（class）
- `prefabInfo`（class）
