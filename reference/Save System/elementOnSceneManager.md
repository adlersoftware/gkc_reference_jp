# elementOnSceneManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Save System/Elements On Scene/elementOnSceneManager.cs:5`

**概要**: シーン内の`elementOnScene`をID付きで一覧管理するシングルトン。保存時の未登録要素の収集、IDの採番、一時状態の保持、エディタ用の一括設定を担当する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Save Current Player Elements On Scene To Save File | `saveCurrentPlayerElementsOnSceneToSaveFile` | `bool` | true | – |
| Elements Scene | `elementsScene` | `int` | – | – |
| Find Disabled Elements On Scene Game Objects | `findDisabledElementsOnSceneGameObjects` | `bool` | – | – |

### Elements On Scene Prefabs Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Elements On Scene Data | `useElementsOnSceneData` | `bool` | – | – |
| Main Elements On Scene Data | `mainElementsOnSceneData` | `elementsOnSceneData` | – | – |

### Elements On Scene Prefabs Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Load Stats On Object ID List | `ignoreLoadStatsOnObjectIDList` | `bool` | – | – |
| Ignore Load Stats On Object ID List Info | `ignoreLoadStatsOnObjectIDListInfo` | `List<int>` | new List<int> () | – |
| Ignore Load Stats On Object Prefab ID List | `ignoreLoadStatsOnObjectPrefabIDList` | `bool` | – | – |
| Ignore Load Stats On Object Prefab ID List Info | `ignoreLoadStatsOnObjectPrefabIDListInfo` | `List<int>` | new List<int> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Element ID | `currentElementID` | `int` | 0 | – |
| Element On Scene List | `elementOnSceneList` | `List<elementOnScene>` | new List<elementOnScene> () | – |
| Temporal Element On Scene Info List | `temporalElementOnSceneInfoList` | `List<temporalElementOnSceneInfo>` | new List<temporalElementOnSceneInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 初期化済みなら戻り、重複インスタンスなら自身を破棄し、そうでなければ静的`Instance`に自身を設定する。 |
| `initializeValues()` | 本体が空で何もしない。 |
| `checkForInstantiatedElementsOnSceneOnSave()` | null要素を除去してIDの重複を解消し、未登録の`elementOnScene`を情報付きで一覧へ追加する。 |
| `setNewInstantiatedElementOnSceneManagerIngame(elementOnScene newElementOnScene)` | IDを進めて保存有効とプリファブID使用を設定し、要素を一覧へ追加する。 |
| `setNewInstantiatedElementOnSceneManagerIngameWithInfo(elementOnScene newElementOnScene)` | IDを採番してアクティブにし、データがあれば名前からプリファブIDも設定して一覧へ追加する。 |
| `setTemporalElementActiveState(int elementID, int elementScene, bool elementActiveState)` | ID・シーン・状態を`temporalElementOnSceneInfo`として一時リストへ追加する。 |
| `removeElementFromSceneList(elementOnScene newElementOnScene)` | 一覧に含まれていれば取り除くだけ。 |
| `getElementOnSceneInfo(int elementID, int elementScene)` | 一覧が空なら収集し、シーン番号とIDが一致する有効な要素を返す。見つからなければnull。 |
| `addNewElementOnScene(elementOnScene newElementOnScene)` | IDを進めてシーン番号とIDを設定し、要素を一覧へ追加する。 |
| `getAllElementsOnSceneOnLevel()` | 一覧をクリアし、無効オブジェクトも含める設定に応じてシーン上の全`elementOnScene`を集める。 |
| `setStatsSearchingByInfo(int currentElementScene, int currentElementID, elementOnScene currentElementOnScene)` | `saveElementsOnSceneInfo`を探し、シーン番号・ID・要素を渡して統計検索を依頼する。 |
| `isSaveCurrentPlayerElementsOnSceneToSaveFile()` | `saveCurrentPlayerElementsOnSceneToSaveFile`を返すだけ。 |
| `setSaveCurrentPlayerElementsOnSceneToSaveFileState(bool state)` | `saveCurrentPlayerElementsOnSceneToSaveFile`を設定するだけ。 |
| `getAllElementsOnSceneOnLevelAndAssignInfoToAllElements()` | 全要素を集めてIDを0から振り直し、状態・シーン番号・元配置フラグを設定して更新する。 |
| `setEnableStateOnAllElementsOnScene(bool state)` | 全要素の`saveElementEnabled`を指定状態にしてコンポーネントを更新する。 |
| `setIDOnElementsOnScenePrefabs()` | `elementsOnSceneData`の各プリファブへ0から順に`elementPrefabID`を割り当て、アセットを更新する。 |
| `setIDOnElementsOnScenePrefabsLocatedOnScene()` | シーン上の要素へ、名前から引いたプリファブIDを設定して更新する。 |
| `getAllElementsOnSceneOnLevelByEditor()` | エディタ用に全要素を集め直し、コンポーネントを更新する。 |
| `clearElementsOnSceneList()` | `elementOnSceneList`を空にして更新する。 |
| `addSingleElementOnSceneToManager(elementOnScene newElementOnScene)` | 未登録なら状態・ID・シーン番号を設定し、元配置要素として一覧へ追加して更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`で自身とシーンをダーティにする。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |

## 内部型

- `temporalElementOnSceneInfo`（class）
