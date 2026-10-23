# dialogManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Dialog System/dialogManager.cs:5`

**概要**: レベル内の `dialogContentSystem` を一覧管理し、ID とシーン番号で検索・生成するマネージャ。シングルトン `Instance` として初期化される。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dialog System Enabled | `dialogSystemEnabled` | `bool` | true | – |
| Dialog Scene | `dialogScene` | `int` | – | – |
| Save Current Dialog Content To Save File | `saveCurrentDialogContentToSaveFile` | `bool` | true | – |
| Layer To Place Objects | `layerToPlaceObjects` | `LayerMask` | – | – |

### Dialog Content System List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dialog Content System List | `dialogContentSystemList` | `List<dialogContentSystem>` | new List<dialogContentSystem> () | – |

### Prefabs List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dialog Content Prefab | `dialogContentPrefab` | `GameObject` | – | – |
| External Dialog Prefab | `externalDialogPrefab` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 既に初期化済みなら何もせず、重複インスタンスなら自身を破棄し、それ以外は静的 `Instance` に登録する。 |
| `getAllDialogContentSystemOnLevel()` | シーン上の `dialogContentSystem` を検索して一覧を作り直す。 |
| `getAllDialogContentOnLevelAndAssignInfo()` | 一覧を再取得し、各要素へ連番 ID と `dialogScene` を割り当てて更新する。 |
| `clearDialogContentList()` | `dialogContentSystemList` を空にして `updateComponent` を呼ぶ。 |
| `getDialogContentSystem(int dialogContentID, int dialogContentScene)` | シーン番号と ID の両方が一致する要素を返し、無ければ `null` を返す。 |
| `instantiateDialogContentSystem()` | `dialogContentPrefab` を `instantateObjectOnLevel` でシーンに生成する。 |
| `instantiateExternalDialogSystem()` | `externalDialogPrefab` を `instantateObjectOnLevel` でシーンに生成する。 |
| `instantateObjectOnLevel(GameObject objectToInstantiate)` | エディタカメラのレイキャスト位置にプレハブを生成し、`lastObjectInstantiated` に保持する。 |
| `getLastObjectInstantiated()` | `lastObjectInstantiated` を返すだけ。 |
| `addDialogContentToCharacter(Transform newDialogContentParent, GameObject newDialogContentOwner)` | ダイアログ内容を生成し、その所有者を指定オブジェクトに設定する（親引数は未使用）。 |
| `updateComponent()` | `GKC_Utils` 経由でコンポーネントとシーンのダーティ更新を行う。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |
