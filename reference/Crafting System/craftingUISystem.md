# craftingUISystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `ingameMenuPanel`
- **ソース**: `Crafting System/craftingUISystem.cs:8`

**概要**: クラフトメニューのUI本体で、設計図・在庫・修理・分解・配置・アップグレードの各パネルを制御する。材料消費と生成、作業台カテゴリの絞り込み、時間制クラフトのコルーチン開始までを担う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Spawn Object Buttons Enabled | `spawnObjectButtonsEnabled` | `bool` | true | – |
| Amount Of Object Buttons To Spawn | `amountOfObjectButtonsToSpawn` | `int` | 50 | – |
| Amount Of Ingredients Buttons To Spawn | `amountOfIngredientsButtonsToSpawn` | `int` | 50 | – |
| Amount Of Inventory Buttons To Spawn | `amountOfInventoryButtonsToSpawn` | `int` | 100 | – |
| Amount On Repare Ingredients Buttons To Spawn | `amountOnRepareIngredientsButtonsToSpawn` | `int` | 30 | – |
| Amount Of Object Stats Button To Spawn | `amountOfObjectStatsButtonToSpawn` | `int` | 0 | – |
| Amount Of Object To Craft In Time Button To Spawn | `amountOfObjectToCraftInTimeButtonToSpawn` | `int` | 20 | – |
| Amount Of Disassemble Ingredients To Spawn | `amountOfDisassembleIngredientsToSpawn` | `int` | 20 | – |

### Workbench Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Crafting Menu Only Usable On Workbenches Enabled | `craftingMenuOnlyUsableOnWorkbenchesEnabled` | `bool` | – | – |
| Repair Objects Only On Workbench Enabled | `repairObjectsOnlyOnWorkbenchEnabled` | `bool` | – | – |
| Disassemble Objects Only On Workbench Enabled | `disassembleObjectsOnlyOnWorkbenchEnabled` | `bool` | – | – |
| Upgrade Objects Only On Workbenche Enabled | `upgradeObjectsOnlyOnWorkbencheEnabled` | `bool` | – | – |

### Crafting Template Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Crafting Blueprint Info Template Data List | `craftingBlueprintInfoTemplateDataList` | `List<craftingBlueprintInfoTemplateData>` | new List<craftingBlueprintInfoTemplat… | – |

### UI Panel Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Panel Category Info List | `panelCategoryInfoList` | `List<panelCategoryInfo>` | new List<panelCategoryInfo> () | – |

### Message Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Message On Object Created | `messageOnObjectCreated` | `string` | – | TextArea (3, 5) |
| Message On Unable To Create Object | `messageOnUnableToCreateObject` | `string` | – | TextArea (3, 5) |
| Message On Object Repaired | `messageOnObjectRepaired` | `string` | – | TextArea (3, 5) |
| Message On Unable To Repair Object | `messageOnUnableToRepairObject` | `string` | – | TextArea (3, 5) |
| Message On Object Disassembled | `messageOnObjectDisassembled` | `string` | – | TextArea (3, 5) |
| Message On Object In Process | `messageOnObjectInProcess` | `string` | "-OBJECT- creation in process." | TextArea (3, 5) |
| Message On Unable To Create Object From Stats | `messageOnUnableToCreateObjectFromStats` | `string` | – | TextArea (3, 5) |
| Message To Show Object Stats | `messageToShowObjectStats` | `string` | – | TextArea (3, 5) |
| Object Name Field | `objectNameField` | `string` | "-OBJECT-" | – |
| Object Amount Field | `objectAmountField` | `string` | "-AMOUNT-" | – |
| Object Stats Field | `objectStatsField` | `string` | "-STATS-" | – |

### Blueprints/recipes unlocked

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Only Blueprints Unlocked | `useOnlyBlueprintsUnlocked` | `bool` | – | – |
| Blueprints Unlocked List | `blueprintsUnlockedList` | `List<string>` | new List<string> () | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Repair Objects Only If Fully Broken | `repairObjectsOnlyIfFullyBroken` | `bool` | true | – |
| Use Upgrade Panel Enabled | `useUpgradePanelEnabled` | `bool` | true | – |
| Ignore Stats On Craft Objects Enabled | `ignoreStatsOnCraftObjectsEnabled` | `bool` | – | – |
| Show Object Stats On Select Object | `showObjectStatsOnSelectObject` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Showing Inventory List | `showingInventoryList` | `bool` | – | – |
| Show All Categories Active | `showAllCategoriesActive` | `bool` | true | – |
| Main Crafting System Assigned | `mainCraftingSystemAssigned` | `bool` | – | – |
| Components Assigned | `componentsAssigned` | `bool` | – | – |
| Menu Opened | `menuOpened` | `bool` | – | – |
| Current Amount To Create | `currentAmountToCreate` | `int` | 1 | – |
| Current Object Selected Name | `currentObjectSelectedName` | `string` | – | – |
| Current Object Category Selected Name | `currentObjectCategorySelectedName` | `string` | – | – |
| Current Object Selected Index | `currentObjectSelectedIndex` | `int` | – | – |
| Object Filter Active | `objectFilterActive` | `bool` | – | – |
| Current Object Is Broken | `currentObjectIsBroken` | `bool` | – | – |
| Current Object Canbe Disassembled | `currentObjectCanbeDisassembled` | `bool` | – | – |
| Current Object Can Be Placed | `currentObjectCanBePlaced` | `bool` | – | – |
| Upgrade Panel Active | `upgradePanelActive` | `bool` | – | – |

### Current Workbench Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Menu Opened From Workbench | `menuOpenedFromWorkbench` | `bool` | – | – |
| Allow To Craft All Objects On Current Bench | `allowToCraftAllObjectsOnCurrentBench` | `bool` | – | – |
| Object Categories To Craft Available On Current Bench | `objectCategoriesToCraftAvailableOnCurrentBench` | `List<string>` | new List<string> () | – |
| Current Crafting Workbench System | `currentCraftingWorkbenchSystem` | `craftingWorkbenchSystem` | – | – |

### Object List Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Crafting Object Button Info List | `craftingObjectButtonInfoList` | `List<craftingObjectButtonInfo>` | new List<craftingObjectButtonInfo> () | – |
| Current Object Ingredients Info List | `currentObjectIngredientsInfoList` | `List<craftingObjectButtonInfo>` | new List<craftingObjectButtonInfo> () | – |
| Current Inventory Info List | `currentInventoryInfoList` | `List<craftingObjectButtonInfo>` | new List<craftingObjectButtonInfo> () | – |
| Current Repair Ingredients Info List | `currentRepairIngredientsInfoList` | `List<craftingObjectButtonInfo>` | new List<craftingObjectButtonInfo> () | – |
| Current Craft Object In Time Info List | `currentCraftObjectInTimeInfoList` | `List<craftingObjectButtonInfo>` | new List<craftingObjectButtonInfo> () | – |
| Object Stat Button Info List | `objectStatButtonInfoList` | `List<objectStatButtonInfo>` | new List<objectStatButtonInfo> () | – |
| Current Disassemble Ingredients Info List | `currentDisassembleIngredientsInfoList` | `List<craftingObjectButtonInfo>` | new List<craftingObjectButtonInfo> () | – |
| Craft Object In Time Info List | `craftObjectInTimeInfoList` | `List<craftObjectInTimeInfo>` | new List<craftObjectInTimeInfo> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Show Inventory List | `eventOnShowInventoryList` | `UnityEvent` | – | – |
| Event On Show Blueprint List | `eventOnShowBlueprintList` | `UnityEvent` | – | – |
| Use Event On Show Object Panel Info | `useEventOnShowObjectPanelInfo` | `bool` | – | – |
| Event On Show Object Panel Info | `eventOnShowObjectPanelInfo` | `UnityEvent` | – | – |
| Use Event On Show Pressed Object Info | `useEventOnShowPressedObjectInfo` | `bool` | – | – |
| Event On Show Pressed Object Info | `eventOnShowPressedObjectInfo` | `UnityEvent` | – | – |
| Event On Open Upgrade Object Panel | `eventOnOpenUpgradeObjectPanel` | `UnityEvent` | – | – |
| Event On Close Upgrade Object Panel | `eventOnCloseUpgradeObjectPanel` | `UnityEvent` | – | – |
| Event On Object Created | `eventOnObjectCreated` | `eventParameters.eventToCallWithString` | – | – |
| Event On Object Not Created | `eventOnObjectNotCreated` | `eventParameters.eventToCallWithString` | – | – |
| Event On Object Repaired | `eventOnObjectRepaired` | `eventParameters.eventToCallWithString` | – | – |
| Event On Object Disassembled | `eventOnObjectDisassembled` | `eventParameters.eventToCallWithString` | – | – |
| Event On Show Object Stats | `eventOnShowObjectStats` | `eventParameters.eventToCallWithString` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Crafting System | `mainCraftingSystem` | `craftingSystem` | – | – |

### UI Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Crafting Button Info Prefab | `craftingButtonInfoPrefab` | `GameObject` | – | – |
| Current Object Name Text | `currentObjectNameText` | `Text` | – | – |
| Current Object Description Text | `currentObjectDescriptionText` | `Text` | – | – |
| Current Amount Of Objects Selected Text | `currentAmountOfObjectsSelectedText` | `Text` | – | – |
| Searcher Input Field | `searcherInputField` | `InputField` | – | – |
| Current Object Category Name Text | `currentObjectCategoryNameText` | `Text` | – | – |
| Crafting Button Info Panel List | `craftingButtonInfoPanelList` | `RectTransform` | – | – |
| Current Object Selected Image | `currentObjectSelectedImage` | `RawImage` | – | – |
| Craft Object Panel | `craftObjectPanel` | `GameObject` | – | – |
| Disassemble Button | `disassembleButton` | `GameObject` | – | – |
| Repair Button | `repairButton` | `GameObject` | – | – |
| Repair Ingredients Panel | `repairIngredientsPanel` | `GameObject` | – | – |
| Disassemble Ingredients Panel | `disassembleIngredientsPanel` | `GameObject` | – | – |

### UI Repair Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Repair Panel List | `repairPanelList` | `RectTransform` | – | – |
| Repair Panel List Element Prefab | `repairPanelListElementPrefab` | `GameObject` | – | – |

### UI Place Object Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Place Object Button | `placeObjectButton` | `GameObject` | – | – |

### UI Hover Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hover Blueprint Panel | `hoverBlueprintPanel` | `RectTransform` | – | – |
| Hover Blueprint Panel List | `hoverBlueprintPanelList` | `RectTransform` | – | – |
| Hover Blueprint Panel List Element Prefab | `hoverBlueprintPanelListElementPrefab` | `GameObject` | – | – |

### UI Upgrade Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Upgrade Button | `upgradeButton` | `GameObject` | – | – |
| Upgrade Panel | `upgradePanel` | `GameObject` | – | – |
| Object Stats Panel List | `objectStatsPanelList` | `RectTransform` | – | – |
| Object Stat Panel List Element Prefab | `objectStatPanelListElementPrefab` | `GameObject` | – | – |

### UI Craft Objects In Time Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Craft Objects In Time Panel List | `craftObjectsInTimePanelList` | `RectTransform` | – | – |
| Craft Objects In Time Panel List Element Prefab | `craftObjectsInTimePanelListElementPrefab` | `GameObject` | – | – |

### Inventory Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory Panel List | `inventoryPanelList` | `RectTransform` | – | – |
| Inventory Panel List Element Prefab | `inventoryPanelListElementPrefab` | `GameObject` | – | – |

### Disassemble Ingredients Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disassemble Ingredients Panel List | `disassembleIngredientsPanelList` | `RectTransform` | – | – |
| Isassemble Ingredients Panel List Element Prefab | `isassembleIngredientsPanelListElementPrefab` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `showInventoryList()` | 在庫表示フラグを立ててイベントを発火し、カテゴリを更新して修理・分解ボタンを出す。 |
| `showBlueprintList()` | 在庫表示を閉じて設計図表示に切り替え、カテゴリを再構築して修理・分解・設置ボタンを隠す。 |
| `showUpgradePanel()` | アップグレードが有効な場合のみフラグを立て、イベントを発火してアップグレードパネルを表示する。 |
| `closeUpgradePanel()` | アップグレードが有効な場合のみフラグを下ろし、イベントを発火してアップグレードパネルを閉じる。 |
| `setShowAllObjectsOrOnlyAvailableToCreate(bool state)` | 本体が空で何もしない。 |
| `repairCurrentObjectSelectedOnInventoryMenu()` | インベントリの現在選択インデックスを取得し、-1でなければそのオブジェクトの修理を実行する。 |
| `repairObjectExternallyByIndex(int objectIndex)` | 指定インデックスのオブジェクトが破損なら選択状態を合わせて修理を試み、結果でUIを更新する。 |
| `repairObject()` | 選択中オブジェクトが破損なら`currentButtonInfo`のカテゴリ名と名前で修理処理を呼び出すだけ。 |
| `disassembleObject()` | 分解可能ならオブジェクトを1個消費し、破損有無に応じた材料を付与してイベント発火と再表示を行う。 |
| `checkShowAllObjectsByFilter()` | 検索文字で在庫/設計図ボタンを名前一致のみ表示に絞り、フィルタ有効フラグを立てる。 |
| `removeObjectsFilter()` | フィルタ中なら検索欄を空にし、全カテゴリ表示へ戻してカテゴリパネル表示を更新する。 |
| `confirmToCreate()` | メニュー表示中に、材料を消費して即時作成または時間制の`craftObjectInTime`を開始する。 |
| `increaseOrDecreaseAmountToCreate(bool state)` | 作成数を増減し、増やす場合は作成可能数を超えないよう戻し、1未満にせず表示を更新する。 |
| `resetAmountToCreate()` | 作成数を1に戻し、その数値表示テキストを更新するだけ。 |
| `selectFirstObjectAvailableButton()` | 全カテゴリ表示なら先頭、絞り込み中なら作成可能な最初のボタンを押した扱いにする。 |
| `checkButtonPressedWithoutCheckIfPreviouslyPressed(GameObject buttonObject)` | 前回押下チェックを行わず、`checkButton`で対象ボタンの選択処理を実行するだけ。 |
| `checkButtonPressed(GameObject buttonObject)` | デバッグ出力の後、`checkButton`で対象ボタンのオブジェクト情報を選択状態に反映する。 |
| `updateObjectSelectedName(string newCurrentObjectCategorySelectedName, string newCurrentObjectSelectedName)` | 選択中オブジェクト名とカテゴリ名を引数の値に置き換えるだけ。 |
| `canObjectBePlaced(string objectCategoryName, string objectName)` | 指定カテゴリ/名前の設計図を探し、設置可能か`useObjectToPlace`を返す（無ければfalse）。 |
| `openPanelInfo(GameObject buttonObject)` | パネルボタンのカテゴリを選択し、名称表示・作成数リセット・先頭オブジェクト選択を行い、任意でイベントを発火する。 |
| `setOpenFromWorkbenchState(bool state, List<string> newObjectCategoriesToCraftAvailableOnCurrentBench, bool allowToCraftAllObjectsOnCurrentBenchValue)` | 作業台からの開閉状態が変わったときだけ、フラグ・全クラフト可否・対象カテゴリリストを更新する。 |
| `setCurrentcurrentCraftingWorkbenchSystem(craftingWorkbenchSystem newCraftingWorkbenchSystem)` | 現在の作業台システム参照を引数の`craftingWorkbenchSystem`に置き換えるだけ。 |
| `checkEventToStopUsingWorkbenchOnDamageReceived()` | 作業台から開いている場合のみ、現在の作業台へ被ダメージ時の使用中断チェックを委譲する。 |
| `getCurrentObjectToPlace()` | 選択中カテゴリ/オブジェクトの設計図から設置用プレハブを返す（見つからなければnull）。 |
| `getCurrentObjectToPlaceByName(string objectName)` | 全設計図を走査して指定名オブジェクトの設置用プレハブを返す（見つからなければnull）。 |
| `getCurrentObjectLayerMaskToAttachObjectByName(string objectName)` | 指定名オブジェクトのアタッチ用`LayerMask`を走査して返す（無ければ空の`LayerMask`）。 |
| `getCurrentObjectToPlacePositionOffsetByName(string objectName)` | 指定名オブジェクトの設置位置オフセットを返し、見つからなければ`Vector3.zero`を返す。 |
| `checkIfCurrentObjectToPlaceUseCustomLayerMaskByName(string objectName)` | 指定名オブジェクトが設置時にカスタム`LayerMask`を使うかを返し、無ければfalseを返す。 |
| `getCurrentObjectCustomLayerMaskToPlaceObjectByName(string objectName)` | 指定名オブジェクトの設置用カスタム`LayerMask`を返し、無ければ空の`LayerMask`を返す。 |
| `getCurrentObjectCanBeRotatedValuesByName(string objectName, ref bool objectCanBeRotatedOnYAxis, ref bool objectCanBeRotatedOnXAxis)` | 指定名オブジェクトのY軸/X軸回転可否を`ref`引数へ設定し、無ければ両方falseにする。 |
| `getCraftingBlueprintInfoTemplateDataList()` | 設計図テンプレートデータのリストをそのまま返すだけ。 |
| `getCurrentObjectSelectedName()` | `currentObjectSelectedName`を返すだけ。 |
| `setPlacementActiveState(bool state)` | 作業台経由なら何もせず、在庫リスト選択中はインデックスを同期してから配置モードを設定する。 |
| `setUseOnlyBlueprintsUnlockedState(bool state)` | `useOnlyBlueprintsUnlocked`を`state`に設定するだけ。 |
| `isUseOnlyBlueprintsUnlockedActive()` | `useOnlyBlueprintsUnlocked`の現在値を返すだけ。 |
| `setBlueprintsUnlockedListValue(List<string> newBlueprintsUnlockedList)` | 解禁ブループリントのリストを新しいリストの複製で置き換えるだけ。 |
| `getBlueprintsUnlockedListValue()` | 解禁ブループリントのリストをそのまま返すだけ。 |
| `addNewBlueprintsUnlockedElement(string newBlueprintsUnlockedElement)` | 未登録なら解禁リストに追加し、メニュー表示中なら設計図リストを再表示する。 |
| `isCurrentObjectCategoryAvailable(string categoryName)` | 全カテゴリ許可か作業台・常時許可リストに基づき、指定カテゴリがクラフト可能かを判定して返す。 |
| `anyObjectToCraftInTimeActive()` | 時間制クラフトの進行リストが1件以上あるかどうかを返すだけ。 |
| `getCraftObjectInTimeInfoList()` | 進行中の時間制クラフト情報を簡易情報クラスの新しいリストに詰め替えて返す。 |
| `setCraftObjectInTimeInfoList(List<craftObjectInTimeSimpleInfo> newCraftObjectInTimeSimpleInfoList)` | 渡された簡易情報から進行情報を作ってリストへ追加し、0.5秒後に各クラフトのコルーチンを開始する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnShowInventoryList` | `UnityEvent` | – |
| `eventOnShowBlueprintList` | `UnityEvent` | – |
| `eventOnShowObjectPanelInfo` | `UnityEvent` | – |
| `eventOnShowPressedObjectInfo` | `UnityEvent` | – |
| `eventOnOpenUpgradeObjectPanel` | `UnityEvent` | – |
| `eventOnCloseUpgradeObjectPanel` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`initializeMenuPanel()`, `openOrCloseMenuFromTouchExternally()`, `openOrCloseMenuPanel(bool state)`

</details>

## 内部型

- `panelCategoryInfo`（class）
- `panelInfo`（class）
- `craftObjectInTimeInfo`（class）
