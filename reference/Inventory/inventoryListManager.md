# inventoryListManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/inventoryListManager.cs:13`

**概要**: インベントリのカテゴリと `inventoryInfo` の一覧を保持・編集するマネージャ。名前からの検索、カテゴリ/オブジェクトの追加・削除、プレハブ生成、一覧の保存/読み込みを提供する。

**公式ドキュメント抜粋**（[Inventory List Manager](../../docs/additional-managers/main-inventory-manager-inventory-bank-and-vendor/inventory-list-manager.md)）

> It is used to configure all the inventory objects that will be used on the game. Along with this, the vendor system and inventory bank system are used to configure the info that will be managed in the ingame vendor system and the inventory bank, to store objects in fixed places, similar to games like borderlands, resident evil series, and others.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Inventory Capture Tool Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Relative Path Captures | `relativePathCaptures` | `string` | "Assets/Game Kit Controller/Prefabs/I… | アイコン画像を保存するキャプチャ用フォルダのパス。 |
| Inventory Camera | `inventoryCamera` | `Camera` | – | アイコン撮影に使用するインベントリ用カメラ。 |
| Look Objects Position | `lookObjectsPosition` | `Transform` | – | 撮影時にアイテムを配置する基準トランスフォーム。 |
| Inventory Camera Parent Game Object | `inventoryCameraParentGameObject` | `GameObject` | – | 撮影時だけ有効化されるカメラの親オブジェクト。 |

### Prefabs Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Empty Inventory Prefab | `emptyInventoryPrefab` | `GameObject` | – | アイテム用プレハブを作る際の雛形になる空オブジェクト。 |
| Relative Inventory Path | `relativeInventoryPath` | `string` | "Assets/Game Kit Controller/Prefabs/I… | 生成したアイテムプレハブを保存するフォルダのパス。 |
| Remove Inventory Prefab When Deleting Inventory Object | `removeInventoryPrefabWhenDeletingInventoryObject` | `bool` | – | ONにするとアイテム削除時にプレハブファイルも消す。 |

### Inventory Bank Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Inventory Bank Manager | `mainInventoryBankManager` | `inventoryBankManager` | – | インベントリバンクの管理コンポーネントへの参照。 |

### Inventory List (DEBUG)

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory List Message | `inventoryListMessage` | `string` | "IMPORTANT: THIS IS A DEBUG LIST OF I… | デバッグ用リストの注意書きとして表示するテキスト。 / TextArea (3, 10) |

### Update Inventory List Info

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory List Update Message | `inventoryListUpdateMessage` | `string` | "Press the Update Inventory List Butt… | リスト更新ボタンの使い方を示す説明テキスト。 / TextArea (3, 10) |

### Save/Load Inventory List To File

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Inventory List Manager Data | `mainInventoryListManagerData` | `inventoryListManagerData` | – | リストの保存先になるデータアセットへの参照。 |
| Update Inventory List Scriptable Object On Create Edit Remove | `updateInventoryListScriptableObjectOnCreateEditRemove` | `bool` | true | ONにすると追加・編集・削除のたびに保存データも更新する。 |

### Add Inventory Object Info To Main List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add New Inventory Object To Add Through Editor List | `addNewInventoryObjectToAddThroughEditorList` | `bool` | – | ONにすると複数プレハブをまとめてリストへ追加する。 |
| New Inventory Object To Add Through Editor | `newInventoryObjectToAddThroughEditor` | `GameObject` | – | リストへ1件だけ追加するアイテムプレハブ。 |
| Use New Category To Add Object | `useNewCategoryToAddObject` | `bool` | – | ONにすると追加先カテゴリ名を手動で指定する。 |
| New Category To Add Object | `newCategoryToAddObject` | `string` | – | アイテム追加先として指定するカテゴリ名。 / 表示条件: `useNewCategoryToAddObject` がオンのとき |

### Full Crafting Blueprint Template Data List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Full Crafting Blueprint Info Template Data | `mainFullCraftingBlueprintInfoTemplateData` | `fullCraftingBlueprintInfoTemplateData` | – | クラフト設計図テンプレートのデータへの参照。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `inventoryList` | `List<inventoryInfo>` | new List<inventoryInfo> () | – |
| `inventoryCategoryInfoList` | `List<inventoryCategoryInfo>` | new List<inventoryCategoryInfo> () | – |
| `inventoryCaptureToolOpen` | `bool` | – | – |
| `newInventoryObjectToAddThroughEditorList` | `List<GameObject>` | new List<GameObject> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 未初期化なら自身を`_inventoryListManagerInstance`にし、別インスタンスがあれば自身を破棄する。 |
| `getFullCraftingBlueprintInfoTemplateData()` | `mainFullCraftingBlueprintInfoTemplateData`を返すだけ。 |
| `getDisassemblePiecesOfCraftingObjectByName(string objectName, ref List<int> amountList)` | 分解レシピから`objectName`を探し、分解素材プレハブのリストを返しつつ`amountList`に必要数を追加する。 |
| `existInventoryInfoFromName(string objectName)` | `inventoryList`を小文字比較で走査し、同名の要素があれば`true`を返す。 |
| `getInventoryInfoFromName(string objectName)` | `inventoryList`から完全一致する`inventoryInfo`を返し、無ければ`null`を返す。 |
| `getInventoryInfoFromInventoryGameObject(GameObject objectToFind)` | `inventoryGameObject`が一致する`inventoryInfo`を返し、無ければ`null`を返す。 |
| `getInventoryInfoFromCategoryListByName(string inventoryObjectName)` | 全カテゴリの`inventoryList`から名前一致の`inventoryInfo`を返し、無ければ`null`を返す。 |
| `getInventoryAmountPerUnitFromInventoryGameObject(GameObject objectToFind)` | `inventoryGameObject`一致要素の`amountPerUnit`を返し、無ければ`-1`を返す。 |
| `getInventoryCategoryIndexByName(string categoryName)` | `Name`が一致するカテゴリのインデックスを返し、無ければ`-1`を返す。 |
| `getInventoryInfoIndexByName(string inventoryObjectName)` | カテゴリ内の一致するオブジェクトのインデックスを返し、無ければ`-1`を返す。 |
| `getInventoryPrefab(GameObject inventoryGameObject)` | `inventoryGameObject`一致要素の`inventoryObjectPrefab`を返し、無ければ`null`を返す。 |
| `getInventoryPrefabByName(string objectName)` | 名前が一致する要素の`inventoryObjectPrefab`を返し、無ければ`null`を返す。 |
| `getInventoryMeshByName(string objectName)` | 名前が一致する要素の`inventoryGameObject`（メッシュ）を返し、無ければ`null`を返す。 |
| `getInventoryObjectComponentByInventoryGameObject(GameObject inventoryGameObjectToSearch)` | `inventoryGameObject`一致要素のプレハブから`inventoryObject`コンポーネントを返す。 |
| `getInventoryObjectAmountPerUnitByName(string inventoryObjectName)` | 名前が一致する要素の`amountPerUnit`を返し、無ければ0を返す。 |
| `getInventoryObjectIconByName(string inventoryObjectName)` | 名前が一致する要素の`icon`テクスチャを返し、無ければ`null`を返す。 |
| `getMaxDurabilityValueOnObjectByName(string objectName)` | `useDurability`有効で名前一致の要素の`maxDurabilityAmount`を返し、無ければ`-1`を返す。 |
| `setInventoryCaptureIcon(inventoryInfo info, Texture2D texture)` | カテゴリ内で`info`と同一の要素の`icon`を`texture`に差し替え、`updateComponent`を呼ぶ。 |
| `getDataPath()` | `relativePathCaptures`のフォルダが無ければ作成し、末尾スラッシュ付きのパスを返す。 |
| `addNewInventoryObject(int categoryIndex, inventoryInfo newInventoryInfo)` | カテゴリ/要素インデックスとカテゴリ名を設定して両リストへ追加し、撮影ツールを閉じて更新する。 |
| `addNewInventoryObject(int categoryIndex)` | 空の`inventoryInfo`を作ってカテゴリ/要素インデックスを設定し、両リストへ追加して更新する。 |
| `removeInventoryObjectByName(string objectToRemoveName)` | 全カテゴリから名前一致の要素を探し、見つかれば`removeInventoryObject`で削除する。 |
| `removeInventoryObject(int categoryIndex, int objectIndex)` | 指定要素をカテゴリと`inventoryList`から削除し、一覧更新と保存チェックを行う。 |
| `createInventoryPrafab(int categoryIndex, int index)` | エディタ専用で、メッシュから空プレハブを複製してコライダー等を移し、プレハブとして保存・登録する。 |
| `updateInventoryPrefab(int categoryIndex, int index)` | `inventoryList`を再構築し、対象プレハブの情報・名前・ピックアップ設定を定義へ更新する。 |
| `removeInventoryPrafab(int categoryIndex, int index)` | エディタ専用で、該当プレハブを探してリストから要素を外し、設定に応じてプレハブを削除する。 |
| `getMainInventoryBankManager()` | `mainInventoryBankManager`を返すだけ。 |
| `addNewCategory()` | 空の`inventoryCategoryInfo`を追加して`updateComponent`を呼ぶ。 |
| `removeCategory(int categoryIndex)` | カテゴリ内の各オブジェクトを`inventoryList`からも削除してからカテゴリを外し、一覧と保存を更新する。 |
| `removeAllCategories()` | `inventoryCategoryInfoList`と`inventoryList`を空にして、更新と保存チェックを行う。 |
| `updateSingleInventoryList()` | 全カテゴリを走査して`inventoryList`を作り直し、各要素のカテゴリ/要素インデックスを振り直す。 |
| `updateInventoryList()` | `updateSingleInventoryList`の後、各プレハブの情報や名前を定義に合わせて更新する。 |
| `updateCategory()` | 全カテゴリの各要素へカテゴリ名・カテゴリ/要素インデックスを設定し直し、`updateComponent`を呼ぶ。 |
| `addCopyOfInventoryObject(int categoryIndex, int index)` | 対象要素の複製を作り、名前とプレハブ参照を空にして直後の位置へ挿入する。 |
| `spawnInventoryObjectByName(string objectName, int amount, Vector3 newPosition, Quaternion newRotation)` | 名前一致のプレハブを指定位置・回転で生成し、数量と表示名を設定して返す（無ければ`null`）。 |
| `renameInventoryObject(string currentObjectName, string newObjectName)` | 名前一致の要素を`setNewName`で改名し、`updateInventoryPrefab`でプレハブ側も更新する。 |
| `renameCraftingObjectByName(string currentObjectName, string newObjectName)` | クラフト用テンプレートから旧名の項目を探して改名し、アセット名も変更してデータベースを更新する。 |
| `saveInventoryListToFile()` | `mainInventoryListManagerData.inventoryList`へカテゴリ一覧をコピーし、`updateComponent`を呼ぶ。 |
| `loadInventoryListFromFile()` | `mainInventoryListManagerData.inventoryList`からカテゴリ一覧を復元し、一覧を再構築して更新する。 |
| `checkIfUpdateInventoryListScriptableObjectOnCreateEditRemove()` | 設定が有効なら`saveInventoryListToFile`を呼ぶだけ。 |
| `setInventoryCaptureToolOpenState(bool state)` | `inventoryCaptureToolOpen`を設定し、ログ出力と`updateComponent`を行う。 |
| `addObjectInfoIntoInventoryList()` | 設定された新規オブジェクトを`inventoryObject`から読み取ってカテゴリへ登録し、参照をクリアする。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`で自身とシーンの更新を促す。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |
| `static GameObject spawnInventoryObject(GameObject currentInventoryObjectPrefab, Transform positionToInstantiate, int amount, inventoryInfo newInventoryInfo)` | – |
