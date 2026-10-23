# craftingSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Crafting System/craftingSystem.cs:6`

**概要**: クラフト機能の窓口となるコンポーネントで、在庫・設計図・作業台・設置モードの各システムへ処理を委譲する。材料消費やブループリント解禁、時間制クラフトの進行情報の取得も公開APIとして提供する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Crafting System Enabled | `craftingSystemEnabled` | `bool` | – | – |
| Crafting System Menu Name | `craftingSystemMenuName` | `string` | "Crafting System Menu" | – |
| Ignore Check Materials Needed To Craft Enabled | `ignoreCheckMaterialsNeededToCraftEnabled` | `bool` | – | – |
| Spawn All Inventory Objects | `spawnAllInventoryObjects` | `bool` | – | – |

### Blueprints/recipes unlocked

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Only Blueprints Unlocked | `useOnlyBlueprintsUnlocked` | `bool` | – | – |
| Blueprints Unlocked List | `blueprintsUnlockedList` | `List<string>` | new List<string> () | – |
| Use Event On Unlock Blueprint | `useEventOnUnlockBlueprint` | `bool` | – | – |
| Extra Message On Unlock Blueprint | `extraMessageOnUnlockBlueprint` | `string` | – | – |
| Event On Unlock Blueprint | `eventOnUnlockBlueprint` | `eventParameters.eventToCallWithString` | – | – |

### Categories To Craft Available

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Allow All Object Categories To Craft At Any Moment Enabled | `allowAllObjectCategoriesToCraftAtAnyMomentEnabled` | `bool` | true | – |
| Object Categories To Craft Available At Any Moment | `objectCategoriesToCraftAvailableAtAnyMoment` | `List<string>` | new List<string> () | – |

### Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Animation On Craft Object Anywhere | `useAnimationOnCraftObjectAnywhere` | `bool` | – | – |
| Animation Name On Craft Anywhere | `animationNameOnCraftAnywhere` | `string` | "Craft Simple Object" | – |
| Use Animation On Craft Object On Workbench | `useAnimationOnCraftObjectOnWorkbench` | `bool` | – | – |
| Animation Name On Craft On Workbench | `animationNameOnCraftOnWorkbench` | `string` | "Craft On Workbench" | – |

### Placement Mode Active Externally Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Placement Active State Externally Enabled | `setPlacementActiveStateExternallyEnabled` | `bool` | true | – |
| Event On Set Placement Active State Externally Not Enabled | `eventOnSetPlacementActiveStateExternallyNotEnabled` | `UnityEvent` | – | – |
| Event On No Object Found To Use Placement Externally | `eventOnNoObjectFoundToUsePlacementExternally` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Menu Opened | `menuOpened` | `bool` | – | – |
| Menu Opened From Workbench | `menuOpenedFromWorkbench` | `bool` | – | – |
| Current Inventory Object Selected Index | `currentInventoryObjectSelectedIndex` | `int` | -1 | – |
| Placement Active Stat Externally Active | `placementActiveStatExternallyActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Open Menu | `eventOnOpenMenu` | `UnityEvent` | – | – |
| Event On Close Menu | `eventOnCloseMenu` | `UnityEvent` | – | – |
| Event To Stop Using Workbench On Damage Received | `eventToStopUsingWorkbenchOnDamageReceived` | `UnityEvent` | – | – |
| Event On Open Workbench | `eventOnOpenWorkbench` | `UnityEvent` | – | – |
| Event On Close Workbench | `eventOnCloseWorkbench` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Crafting UI System | `mainCraftingUISystem` | `craftingUISystem` | – | – |
| Main Inventorymanager | `mainInventorymanager` | `inventoryManager` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Player Game Object | `playerGameObject` | `GameObject` | – | – |
| Position To Spawn Objects If Not Space On Inventory | `positionToSpawnObjectsIfNotSpaceOnInventory` | `Transform` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Crafting Placement System | `mainCraftingPlacementSystem` | `craftingPlacementSystem` | – | – |
| Main Objects Stats System | `mainObjectsStatsSystem` | `objectsStatsSystem` | – | – |
| Main Player Stats System | `mainPlayerStatsSystem` | `playerStatsSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `openOrCloseCraftingMenu(bool state)` | `menuOpened`を`state`に切り替え、開く際にUI未割り当てなら取得し、開閉イベントを発火する。 |
| `checkStateOnCraftObject()` | クラフト用アニメ設定が有効なら、作業台か否かで選んだアニメをプレイヤーに再生させる。 |
| `getCurrentInventoryObjectIndex()` | `mainInventorymanager`から現在選択中のインベントリオブジェクトのインデックスを返すだけ。 |
| `getInventoryObjectAmountByName(string inventoryObjectName)` | 指定名オブジェクトの所持数を`mainInventorymanager`に問い合わせて返すだけ。 |
| `getInventoryObjectIconByName(string inventoryObjectName)` | 指定名オブジェクトのアイコンテクスチャを`mainInventorymanager`から取得して返すだけ。 |
| `removeObjectAmountFromInventoryByName(string objectName, int amountToMove)` | 指定名オブジェクトを`amountToMove`個減らすよう`mainInventorymanager`に委譲するだけ。 |
| `removeObjectAmountFromInventoryByIndex(int objectIndex, int amountToMove)` | 指定インデックスのオブジェクトを`amountToMove`個減らすよう在庫管理側へ委譲するだけ。 |
| `checkIfPlayerInventoryIsFull(string inventoryObjectName, int inventoryObjectAmount)` | 在庫が満杯ならtrueを返し、そうでなければ指定オブジェクトを指定数収納できるかを返す。 |
| `giveInventoryObjectToCharacter(string objectName, int objectAmount)` | `applyDamage`の付与処理で指定名オブジェクトを指定数プレイヤーに渡す。 |
| `getInventoryList()` | `mainInventorymanager`のインベントリリストをそのまま返すだけ。 |
| `getInventoryInfoByName(string objectName)` | 指定名の`inventoryInfo`を`mainInventorymanager`から取得して返すだけ。 |
| `getInventoryInfoByIndex(int objectIndex)` | 指定インデックスの`inventoryInfo`を`mainInventorymanager`から取得して返すだけ。 |
| `repairDurabilityObjectByIndex(int objectIndex)` | 指定インデックスのオブジェクトの耐久度修理を在庫管理側に委譲し、その結果を返す。 |
| `isObjectBroken(int objectIndex)` | 指定インデックスのオブジェクトが破損しているかを在庫管理側に問い合わせて返すだけ。 |
| `isObjectDurabilityComplete(int objectIndex)` | 指定インデックスのオブジェクトの耐久度が満タンかを在庫管理側に問い合わせて返す。 |
| `getInventoryMeshByName(string objectName)` | 指定名オブジェクトのメッシュ`GameObject`を`mainInventorymanager`から取得して返す。 |
| `getCurrentObjectToPlace()` | `mainCraftingUISystem`から現在選択中オブジェクトの設置用プレハブを取得して返すだけ。 |
| `getCurrentObjectToPlaceByName(string objectName)` | 指定名オブジェクトの設置用プレハブを`mainCraftingUISystem`経由で取得して返すだけ。 |
| `updateObjectSelectedName(string newCurrentObjectCategorySelectedName, string newCurrentObjectSelectedName)` | 選択中のカテゴリ名とオブジェクト名を`mainCraftingUISystem`へ渡して更新するだけ。 |
| `getCurrentObjectLayerMaskToAttachObjectByName(string objectName)` | 指定名オブジェクトを設置時にアタッチする`LayerMask`をUIシステムから取得して返す。 |
| `getCurrentObjectToPlacePositionOffsetByName(string objectName)` | 指定名オブジェクトの設置位置オフセット`Vector3`をUIシステムから取得して返すだけ。 |
| `checkIfCurrentObjectToPlaceUseCustomLayerMaskByName(string objectName)` | 指定名オブジェクトが設置用カスタム`LayerMask`を使う設定かをUIシステムに問い合わせて返す。 |
| `getCurrentObjectCustomLayerMaskToPlaceObjectByName(string objectName)` | 指定名オブジェクトの設置用カスタム`LayerMask`をUIシステムから取得して返すだけ。 |
| `getCurrentObjectCanBeRotatedValuesByName(string objectName, ref bool objectCanBeRotatedOnYAxis, ref bool objectCanBeRotatedOnXAxis)` | 指定名オブジェクトのY軸/X軸回転可否を`ref`引数へ書き込むだけで、無ければ両方false。 |
| `getCurrentObjectSelectedName()` | `mainCraftingUISystem`が保持する現在選択中オブジェクト名を返すだけ。 |
| `isIgnoreCheckMaterialsNeededToCraftEnabled()` | 材料チェックを無視する設定値を返すだけ。 |
| `setPlacementActiveState(bool state)` | 設置ポーズ中は何もせず、設置可能ならメッシュを設定し、メニューを閉じて配置モードを切り替える。 |
| `setPlacementActiveStateExternally(bool state)` | 無効設定ならイベントを出して中断し、有効なら設置可能オブジェクトを選んで配置モードを開始/終了する。 |
| `setCurrentInventoryObjectSelectedIndex(int newValue)` | 現在選択中インベントリオブジェクトのインデックスを`newValue`に設定するだけ。 |
| `selectNextOrPreviousObjectForPlacement(bool state)` | インデックスを前後に動かし、設置可能なオブジェクトを探して選択名をUIに反映し、結果を返す。 |
| `setPlacementActivePausedState(bool state)` | `mainCraftingPlacementSystem`の設置一時停止状態を`state`に設定するだけ。 |
| `setOriginalPlacementActivePausedState()` | 設置の一時停止状態を元の値へ戻すよう`mainCraftingPlacementSystem`に委譲するだけ。 |
| `checkIfStatValueAvailable(string statName, int statAmount)` | 指定ステータスが`statAmount`分あるかを`mainPlayerStatsSystem`に問い合わせて返す。 |
| `addOrRemovePlayerStatAmount(string statName, int statAmount)` | 指定ステータスを`statAmount`だけ増減するよう`mainPlayerStatsSystem`に委譲するだけ。 |
| `setUseOnlyBlueprintsUnlockedState(bool state)` | 解禁ブループリントのみ表示する設定を`state`にし、UI側にも同じ設定を渡す。 |
| `isUseOnlyBlueprintsUnlockedActive()` | `useOnlyBlueprintsUnlocked`の現在値を返すだけ。 |
| `setBlueprintsUnlockedListValue(List<string> newBlueprintsUnlockedList)` | 解禁ブループリントのリストを新しいリストの複製で置き換え、UIにも同じリストを渡す。 |
| `getBlueprintsUnlockedListValue()` | 解禁ブループリント名のリスト`blueprintsUnlockedList`をそのまま返すだけ。 |
| `addNewBlueprintsUnlockedElement(string newBlueprintsUnlockedElement)` | 未登録なら解禁リストに追加し、解禁イベントを発火してUI側にも追加を伝える。 |
| `setObjectCategoriesToCraftAvailableAtAnyMomentValue(List<string> newList)` | 常時クラフト可能なカテゴリのリストを`newList`で置き換えるだけ。 |
| `getObjectCategoriesToCraftAvailableAtAnyMomentValue()` | 常時クラフト可能なカテゴリのリストをそのまま返すだけ。 |
| `addObjectCategoriesToCraftAvailableAtAnyMomentElement(string newElement)` | 未含まれていれば常時クラフト可能カテゴリのリストに`newElement`を追加するだけ。 |
| `getCraftObjectInTimeInfoList()` | 時間のかかるクラフトの進行情報リストを`mainCraftingUISystem`から取得して返すだけ。 |
| `anyObjectToCraftInTimeActive()` | UIが割り当て済みなら時間制クラフトの進行有無を問い合わせ、未割り当てならfalseを返す。 |
| `setCraftObjectInTimeInfoList(List<craftObjectInTimeSimpleInfo> newCraftObjectInTimeSimpleInfoList)` | 時間制クラフトの進行情報リストをUIへ渡して復元させるだけ。 |
| `setOpenFromWorkbenchState(bool state, List<string> newObjectCategoriesToCraftAvailableOnCurrentBench, bool allowToCraftAllObjectsOnCurrentBenchValue)` | 作業台経由の開閉状態・対象カテゴリ・全クラフト可否をUIへ渡し、作業台フラグを更新する。 |
| `setCurrentcurrentCraftingWorkbenchSystem(craftingWorkbenchSystem newCraftingWorkbenchSystem)` | 現在使用中の`craftingWorkbenchSystem`をUIへ設定するだけで、UI未割り当てなら何もしない。 |
| `stopUsingWorkbenchOnDamageReceived()` | メニューが作業台から開かれている場合のみ、使用中断イベントを発火しUI側にも通知する。 |
| `closeMenuOnWorkbenchWithActionSystem()` | 作業台メニュー表示中かつプレイヤーがアクション中なら、そのアクション用アニメを再生する。 |
| `repairCurrentObjectSelectedOnInventoryMenu()` | 耐久度機能が有効なときだけ、選択中オブジェクトの修理をUI側に依頼する。 |
| `updateUIAfterRepairingCurrentObjectSelectedOnInventoryMenu(bool state)` | 修理結果`state`をインベントリマネージャへ渡してUI更新を委譲するだけ。 |
| `getStatsFromObjectByName(string objectName)` | 指定名オブジェクトのステータス情報リストを`mainObjectsStatsSystem`から取得して返す。 |
| `objectCanBeUpgraded(string objectName)` | 指定名オブジェクトがアップグレード可能かを`mainObjectsStatsSystem`に問い合わせて返す。 |
| `setCraftingSystemEnabledStateFromEditor(bool state)` | エディタ用に`craftingSystemEnabled`を`state`へ設定し、コンポーネントを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とシーンのダーティ更新でコンポーネント状態を反映するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnSetPlacementActiveStateExternallyNotEnabled` | `UnityEvent` | – |
| `eventOnNoObjectFoundToUsePlacementExternally` | `UnityEvent` | – |
| `eventOnOpenMenu` | `UnityEvent` | – |
| `eventOnCloseMenu` | `UnityEvent` | – |
| `eventToStopUsingWorkbenchOnDamageReceived` | `UnityEvent` | – |
| `eventOnOpenWorkbench` | `UnityEvent` | – |
| `eventOnCloseWorkbench` | `UnityEvent` | – |
