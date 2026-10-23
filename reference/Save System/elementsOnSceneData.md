# elementsOnSceneData

- **種別**: ScriptableObject（データアセット）
- **継承 / 実装**: `ScriptableObject`
- **ソース**: `Save System/Elements On Scene/elementsOnSceneData.cs:5`
- **属性**: `CreateAssetMenu (fileName = "Element On Scene Data", menuName = "GKC/Create Element On Scene Data", order = 51)`

**概要**: `elementsOnSceneInfo`のリストを保持するScriptableObjectで、プレハブIDとプレハブ名から要素プレハブを検索する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Elements On Scene Info List | `elementsOnSceneInfoList` | `List<elementsOnSceneInfo>` | new List<elementsOnSceneInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getElementScenePrefabById(int prefabID)` | `prefabID`が-1以下なら`null`を返し、それ以外は二重走査で一致する`elementPrefab`を返す。 |
| `getElementScenePrefabIDByName(string prefabName)` | 二重走査でプレハブ名が`prefabName`と一致または含まれるものを探し、その`elementPrefabID`を返す。 |
