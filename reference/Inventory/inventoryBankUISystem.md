# inventoryBankUISystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/inventoryBankUISystem.cs:13`

**概要**: プレイヤー在庫とインベントリバンクの間でアイテムを移す UI を管理するコンポーネント。メニューの開閉、アイコン生成、ドラッグ&ドロップや数量指定、カメラの回転/ズームを扱う。

**公式ドキュメント抜粋**（[Inventory Bank UI System](../../docs/character-level-components/character/inventory-bank-ui-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Number Of Elements On Press Up | `useNumberOfElementsOnPressUp` | `bool` | – | – |
| Use Number Of Elements When Icon Not Moved | `useNumberOfElementsWhenIconNotMoved` | `bool` | – | – |
| Drop Full Objects Amount | `dropFullObjectsAmount` | `bool` | true | – |
| Drag And Drop Icons | `dragAndDropIcons` | `bool` | true | – |
| Time To Drag | `timeToDrag` | `float` | 0.5f | – |
| Configure Number Objects To Use Rate | `configureNumberObjectsToUseRate` | `float` | 0.4f | – |
| Faster Number Objects To Use Rate | `fasterNumberObjectsToUseRate` | `float` | 0.1f | – |
| Wait Time To Use Faster Number Objects To Use Rate | `waitTimeToUseFasterNumberObjectsToUseRate` | `float` | 1 | – |
| Main Inventory Manager Name | `mainInventoryManagerName` | `string` | "Main Inventory Manager" | – |
| Allow To Drop Player Inventory Into Custom Inventory Banks | `allowToDropPlayerInventoryIntoCustomInventoryBanks` | `bool` | – | – |
| Close Menu If Inventory Bank Object Destroyed | `closeMenuIfInventoryBankObjectDestroyed` | `bool` | – | – |
| Allow To Select New Slot Object If Setting Amount On Previous Enabled | `allowToSelectNewSlotObjectIfSettingAmountOnPreviousEnabled` | `bool` | true | – |
| Inventory Bank Full Message | `inventoryBankFullMessage` | `string` | "Inventory Bank is full" | – |
| Use Custom Max Inventory Bank Slots Amount | `useCustomMaxInventoryBankSlotsAmount` | `bool` | – | – |
| Show Empty Slots On Use Max Inventory Bank Slots Amount | `showEmptySlotsOnUseMaxInventoryBankSlotsAmount` | `bool` | – | – |
| Use Max Inventory Bank Slots Amount | `useMaxInventoryBankSlotsAmount` | `bool` | – | – |
| Max Inventory Bank Slots Amount | `maxInventoryBankSlotsAmount` | `int` | – | – |

### Zoom/Rotation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Zoom Speed | `zoomSpeed` | `float` | – | – |
| Max Zoom Value | `maxZoomValue` | `float` | – | – |
| Min Zoom Value | `minZoomValue` | `float` | – | – |
| Rotation Speed | `rotationSpeed` | `float` | – | – |
| Use Blur UI Panel | `useBlurUIPanel` | `bool` | true | – |

### Debug State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Menu Opened | `menuOpened` | `bool` | – | – |
| Slot To Move Found | `slotToMoveFound` | `bool` | – | – |
| Slot Found | `slotFound` | `GameObject` | – | – |
| Dragged From Player Inventory List | `draggedFromPlayerInventoryList` | `bool` | – | – |
| Dragged From Bank Inventory List | `draggedFromBankInventoryList` | `bool` | – | – |
| Dropped In Player Inventory List | `droppedInPlayerInventoryList` | `bool` | – | – |
| Dropped In Bank Inventory List | `droppedInBankInventoryList` | `bool` | – | – |
| Can Drop Objects To Inventory Bank | `canDropObjectsToInventoryBank` | `bool` | true | – |
| Touching | `touching` | `bool` | – | – |
| Dragging Slot Active | `draggingSlotActive` | `bool` | – | – |
| Reset Drag Drop Elements Enabled | `resetDragDropElementsEnabled` | `bool` | true | – |
| Current Slot To Move Inventory Object | `currentSlotToMoveInventoryObject` | `inventoryInfo` | – | – |
| Current Slot Found Inventory Object | `currentSlotFoundInventoryObject` | `inventoryInfo` | – | – |

### Debug List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Inventory List | `playerInventoryList` | `List<inventoryInfo>` | new List<inventoryInfo> () | – |
| Current Bank Inventory List | `currentBankInventoryList` | `List<inventoryInfo>` | new List<inventoryInfo> () | – |
| Player Icon Element List | `playerIconElementList` | `List<inventoryMenuIconElement>` | new List<inventoryMenuIconElement> () | – |
| Bank Icon Element List | `bankIconElementList` | `List<inventoryMenuIconElement>` | new List<inventoryMenuIconElement> () | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Open Close Inventory Bank | `useEventsOnOpenCloseInventoryBank` | `bool` | – | – |
| Event On Open Inventory Bank | `eventOnOpenInventoryBank` | `UnityEvent` | – | – |
| Event On Close Inventory Bank | `eventOnCloseInventoryBank` | `UnityEvent` | – | – |

### UI Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory Menu Render Texture | `inventoryMenuRenderTexture` | `RawImage` | – | – |
| Look Objects Position | `lookObjectsPosition` | `Transform` | – | – |
| Slot To Move | `slotToMove` | `GameObject` | – | – |
| Menu Background | `menuBackground` | `GameObject` | – | – |
| Inventory Object Render Panel | `inventoryObjectRenderPanel` | `GameObject` | – | – |
| Inventory Camera | `inventoryCamera` | `Camera` | – | – |
| Inventory Menu | `inventoryMenu` | `GameObject` | – | – |
| Player Inventory Slots | `playerInventorySlots` | `GameObject` | – | – |
| Player Inventory Slots Content | `playerInventorySlotsContent` | `GameObject` | – | – |
| Player Inventory Slot | `playerInventorySlot` | `GameObject` | – | – |
| Player Inventory Scrollbar | `playerInventoryScrollbar` | `Scrollbar` | – | – |
| Bank Inventory Slots | `bankInventorySlots` | `GameObject` | – | – |
| Bank Inventory Slots Content | `bankInventorySlotsContent` | `GameObject` | – | – |
| Bank Inventory Slot | `bankInventorySlot` | `GameObject` | – | – |
| Bank Inventory Scrollbar | `bankInventoryScrollbar` | `Scrollbar` | – | – |
| Number Of Elements Window | `numberOfElementsWindow` | `GameObject` | – | – |
| Number Of Objects To Use Text | `numberOfObjectsToUseText` | `Text` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Inventory Manager | `playerInventoryManager` | `inventoryManager` | – | – |
| Using Devices Manager | `usingDevicesManager` | `usingDevicesSystem` | – | – |
| Main Inventory List Manager | `mainInventoryListManager` | `inventoryListManager` | – | – |
| Main Inventory Bank Manager | `mainInventoryBankManager` | `inventoryBankManager` | – | – |
| Player Input | `playerInput` | `playerInputManager` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`があれば停止するだけ。 |
| `setCurrentInventoryBankObject(GameObject inventoryBankGameObject)` | `currentInventoryBankObject`を設定するだけ。 |
| `setCurrentInventoryBankSystem(GameObject inventoryBankGameObject)` | 対象の`inventoryBankSystem`から在庫と最大スロット数を設定し、専用バンクかで表示パネルを切り替える。 |
| `openOrCloseInventoryBankMenuByButton()` | `usingDevicesManager`経由でデバイス使用を要求し、未登録ならリストから除去する。 |
| `closeInventoryBankIfDestroyed()` | メニュー表示中に`currentInventoryBankSystem`がnullなら、デバイス使用状態を解除して閉じる。 |
| `openOrCloseInventoryBankMenu(bool state)` | `menuOpened`を更新してUIとポーズを切り替え、開く際は両在庫のアイコンを再生成し更新コルーチンを開始する。 |
| `createInventoryIcons(List<inventoryInfo> currentInventoryListToCreate, GameObject currentInventorySlot, GameObject currentInventorySlotsContent, List<inventoryMenuIconElement> currentIconElementList)` | 指定リストの既存ボタンを非表示にした後、各要素について`createInventoryIcon`を呼び直す。 |
| `createInventoryIcon(inventoryInfo currentInventoryInfo, int index, GameObject currentInventorySlot, GameObject currentInventorySlotsContent, List<inventoryMenuIconElement> currentIconElementList)` | 空きのアイコン要素を再利用または生成し、名前・アイコン・数量・ボタン参照を`inventoryInfo`へ設定する。 |
| `enableNumberOfElementsOnPressUp()` | ドラッグ設定に応じて数量指定メニューを開き、移動元と移動先の判定フラグを設定する。 |
| `enableObjectRotation()` | `objectInCamera`があれば`enableRotation`を`true`にする。 |
| `disableObjectRotation()` | `enableRotation`を`false`にするだけ。 |
| `destroyObjectInCamera()` | `objectInCamera`があれば`Destroy`するだけ。 |
| `zoomInEnabled()` | `zoomingIn`を`true`にするだけ。 |
| `zoomInDisabled()` | `zoomingIn`を`false`にするだけ。 |
| `zoomOutEnabled()` | `zoomingOut`を`true`にするだけ。 |
| `zoomOutDisabled()` | `zoomingOut`を`false`にするだけ。 |
| `checkResetCameraFov(float targetValue)` | 既存のFOVリセットコルーチンを止め、`targetValue`へ向かう`resetCameraFovCorutine`を開始する。 |
| `getCurrentPlayerInventoryList()` | プレイヤー在庫のコピーで`playerInventoryList`を作り直し、スロット上限で分割する。 |
| `addObjectToUse()` | `numberOfObjectsToUse`を1増やし、所持数を上限に`currentAmountToMove`と表示を更新する。 |
| `removeObjectToUse()` | `numberOfObjectsToUse`を1減らし、下限1で`currentAmountToMove`と数量表示を更新する。 |
| `startToAddObjectToUse()` | `addingObjectToUse`を`true`にし、連続加算の開始時刻を記録する。 |
| `stopToAddObjectToUse()` | `addingObjectToUse`を`false`にし、加算時刻と高速化フラグをリセットする。 |
| `startToRemoveObjectToUse()` | `removinvObjectToUse`を`true`にし、連続減算の開始時刻を記録する。 |
| `stopToRemoveObjectToUse()` | `removinvObjectToUse`を`false`にし、減算時刻と高速化フラグをリセットする。 |
| `enableNumberOfObjectsToUseMenu(RectTransform menuPosition)` | `numberOfElementsWindow`を表示して数量を1に戻し、`settingAmountObjectsToMove`を立てる。 |
| `resetAndDisableNumberOfObjectsToUseMenu()` | `disableNumberOfObjectsToUseMenu`の後、`resetNumberOfObjectsToUse`を呼ぶだけ。 |
| `disableNumberOfObjectsToUseMenu()` | 数量を1に戻し、`numberOfElementsWindow`を非表示にする。 |
| `resetNumberOfObjectsToUse()` | `numberOfObjectsToUse`を1に戻して数量表示を更新するだけ。 |
| `setNumberOfObjectsToUseText(int amount)` | `numberOfObjectsToUseText`に`amount`を文字列で表示するだけ。 |
| `resetScroll(Scrollbar scrollBarToReset)` | 2フレーム待ってから`scrollBarToReset.value`を1にするコルーチンを開始する。 |
| `resetBankInventoryRectTransform()` | バンク側のレイアウト再構築を数フレーム待って2回行うコルーチンを開始する。 |
| `updateFullInventorySlots(List<inventoryInfo> currentInventoryList, List<inventoryMenuIconElement> currentIconElementList, bool checkInventorySlotAmount)` | 既存アイコンを一旦非表示にし、在庫リストの内容をアイコン名・アイコン・数量へ順に反映する。 |
| `setMenuIconElementPressedState(bool state)` | `currentInventoryObject`の`pressedIcon`表示を`state`に切り替える。 |
| `removeButton(List<inventoryInfo> currentInventoryList, List<inventoryMenuIconElement> currentIconElementList, bool removeElementFromInventoryList)` | 数量0の要素をリストから削除し、空きスロット表示設定なら空要素を補充してカメラ表示を片付ける。 |
| `resetDragDropElements()` | 有効時、ドラッグ関連フラグと選択中オブジェクト・数量メニューを初期化する。 |
| `checkIfObjecToMoveAlreadyInBankList()` | 移動対象と同名のバンク内要素を探し、`currentObjectAlreadyInBankList`と該当インデックスを更新する。 |
| `confirmMoveObjects()` | ドラッグ元/先に応じ、バンクかプレイヤー在庫への移動処理を呼ぶ。 |
| `confirmMoveAllObjects()` | `currentAmountToMove`を対象オブジェクトの全数量にして`confirmMoveObjects`を呼ぶ。 |
| `confirmMoveFullInventoryBankToPlayerInventory()` | バンク内の全要素を順にプレイヤー在庫へ移し、UI更新と`cancelMoveObjects`で終了する。 |
| `confirmMoveFullPlayerInventoryToBankInventory()` | `canDropObjectsToInventoryBank`なら全要素をバンクへ移し、UI更新後に`cancelMoveObjects`を呼ぶ。 |
| `cancelMoveObjects()` | `resetDragDropElements`と`resetAndDisableNumberOfObjectsToUseMenu`を呼ぶ。 |
| `getPressedButton(Button buttonObj)` | 押されたボタンから対象インデックスを求め、`setObjectInfo`で選択しカメラのFOVを初期値へ戻す。 |
| `setObjectInfo(int index, bool isPlayerInventoryList)` | 指定リストの要素を選択中にし、`pressedIcon`を点け、プレハブを`lookObjectsPosition`に生成する。 |
| `checkInventoryObjectSlotsInput()` | タッチ/マウス入力をレイキャストし、アイコンのドラッグ開始・追従・離した位置の判定を行う。 |
| `checkDroppedObject()` | ドロップ先や重なったアイコンに応じて在庫間の移動・入れ替えを行い、失敗時はドラッグ状態をリセットする。 |
| `dragToPlayerInventory()` | 移動量を全数量に設定し、`dropFullObjectsAmount`なら即移動、そうでなければ数量メニューを開く。 |
| `dragToBankInventory()` | 同名要素をバンク内で探してから移動量を全数量にし、全量移動か数量メニュー表示かを選ぶ。 |
| `moveObjectsToBankInventory()` | 同名要素があれば数量を加算、無ければバンクへ追加してアイコンを生成し、プレイヤー在庫から移動する。 |
| `moveObjectsToPlayerInventory()` | 選択オブジェクトを`tryToPickUpObject`でプレイヤー在庫へ移し、失敗時は在庫満杯や上限のメッセージを出す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnOpenInventoryBank` | `UnityEvent` | – |
| `eventOnCloseInventoryBank` | `UnityEvent` | – |
