# vendorUISystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vendor System/vendorUISystem.cs:8`

**概要**: ベンダー（売買）メニューのUIを制御するコンポーネントで、カテゴリと商品スロットの生成・選択・個数指定、購入/売却の確定処理を行います。`inventoryBankSystem`または`vendorSystem`の在庫リストを表示し、通貨の増減と在庫更新を反映します。

**公式ドキュメント抜粋**（[Vendor UI System](../../docs/character-level-components/character/vendor-ui-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Objects With Higher Level Than Player | `showObjectsWithHigherLevelThanPlayer` | `bool` | true | – |
| Add Sold Objects To Shop | `addSoldObjectsToShop` | `bool` | true | – |
| Current Object Selected Price Extra Text | `currentObjectSelectedPriceExtraText` | `string` | – | – |
| Price Extra Text | `priceExtraText` | `string` | "Available: " | – |
| Out Of Stock Text | `outOfStockText` | `string` | "OUT OF STOCK" | – |
| Zoom Speed | `zoomSpeed` | `float` | – | – |
| Max Zoom Value | `maxZoomValue` | `float` | – | – |
| Min Zoom Value | `minZoomValue` | `float` | – | – |
| Rotation Speed | `rotationSpeed` | `float` | – | – |
| Use Blur UI Panel | `useBlurUIPanel` | `bool` | true | – |
| Configure Number Objects To Use Rate | `configureNumberObjectsToUseRate` | `float` | 0.4f | – |
| Faster Number Objects To Use Rate | `fasterNumberObjectsToUseRate` | `float` | 0.1f | – |
| Wait Time To Use Faster Number Objects To Use Rate | `waitTimeToUseFasterNumberObjectsToUseRate` | `float` | 1 | – |
| Main Inventory Manager Name | `mainInventoryManagerName` | `string` | "Main Inventory Manager" | – |
| Show Buy Object Amount Sign | `showBuyObjectAmountSign` | `bool` | – | – |
| Show Sell Object Amount Sign | `showSellObjectAmountSign` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Menu Opened | `menuOpened` | `bool` | – | – |
| Adding Object To Use | `addingObjectToUse` | `bool` | – | – |
| Removinv Object To Use | `removinvObjectToUse` | `bool` | – | – |
| Number Of Objects To Use | `numberOfObjectsToUse` | `int` | – | – |
| Buying Objects | `buyingObjects` | `bool` | true | – |
| Selling Objects | `sellingObjects` | `bool` | – | – |

### Inventory Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Vendor Inventory List | `vendorInventoryList` | `List<inventoryInfo>` | new List<inventoryInfo> () | – |
| Vendor Object Slot Panel Info List | `vendorObjectSlotPanelInfoList` | `List<vendorObjectSlotPanelInfo>` | new List<vendorObjectSlotPanelInfo> () | – |
| Vendor Category Slot Panel Info List | `vendorCategorySlotPanelInfoList` | `List<vendorCategorySlotPanelInfo>` | new List<vendorCategorySlotPanelInfo> () | – |
| Sold Object List | `soldObjectList` | `List<inventoryInfo>` | new List<inventoryInfo> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Set Buy Mode | `eventOnSetBuyMode` | `UnityEvent` | – | – |
| Event On Set Sell Mode | `eventOnSetSellMode` | `UnityEvent` | – | – |
| Event On Purchase | `eventOnPurchase` | `UnityEvent` | – | – |
| Event On Sale | `eventOnSale` | `UnityEvent` | – | – |
| Event On Object Out Of Stock | `eventOnObjectOutOfStock` | `UnityEvent` | – | – |
| Event On Not Enough Money | `eventOnNotEnoughMoney` | `UnityEvent` | – | – |
| Event On Not Enough Level | `eventOnNotEnoughLevel` | `UnityEvent` | – | – |
| Event On Max Object Amount Reached | `eventOnMaxObjectAmountReached` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vendor Menu | `vendorMenu` | `GameObject` | – | – |
| Category Scroll Rect | `categoryScrollRect` | `ScrollRect` | – | – |
| Object Scroll Rect | `objectScrollRect` | `ScrollRect` | – | – |
| Category Slots Parent | `categorySlotsParent` | `GameObject` | – | – |
| Category Slot Prefab | `categorySlotPrefab` | `GameObject` | – | – |
| Object Slots Parent | `objectSlotsParent` | `GameObject` | – | – |
| Object Slot Prefab | `objectSlotPrefab` | `GameObject` | – | – |
| Vendor Object List Scrollbar | `vendorObjectListScrollbar` | `Scrollbar` | – | – |
| Number Of Objects To Use Text | `numberOfObjectsToUseText` | `Text` | – | – |
| Current Object Selected Price Text | `currentObjectSelectedPriceText` | `Text` | – | – |
| Total Price Text | `totalPriceText` | `Text` | – | – |
| Total Money Amount Available | `totalMoneyAmountAvailable` | `Text` | – | – |
| Current Category Name Text | `currentCategoryNameText` | `Text` | – | – |
| Current Object Name Text | `currentObjectNameText` | `Text` | – | – |
| Current Object Information Text | `currentObjectInformationText` | `Text` | – | – |
| Inventory Camera | `inventoryCamera` | `Camera` | – | – |
| Inventory Menu Render Texture | `inventoryMenuRenderTexture` | `RawImage` | – | – |
| Look Objects Position | `lookObjectsPosition` | `Transform` | – | – |
| Player Inventory Manager | `playerInventoryManager` | `inventoryManager` | – | – |
| Using Devices Manager | `usingDevicesManager` | `usingDevicesSystem` | – | – |
| Main Inventory List Manager | `mainInventoryListManager` | `inventoryListManager` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Player Input | `playerInput` | `playerInputManager` | – | – |
| Main Currency System | `mainCurrencySystem` | `currencySystem` | – | – |
| Main Player Experience System | `mainPlayerExperienceSystem` | `playerExperienceSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`がnullでなければ停止するだけ。 |
| `setCurrentInventoryBankObject(GameObject inventoryBankGameObject)` | `currentInventoryBankObject`を代入するだけ。 |
| `setCurrentInventoryBankSystem(GameObject inventoryBankGameObject)` | インベントリバンクとそのシステムを設定し、オブジェクト生成位置を取得、バンク在庫か`vendorSystem`の在庫を`vendorInventoryList`へ読み込む。 |
| `updateInventoryListOnVendorSystem()` | バンクが自前の在庫を使っていない場合、`mainVendorSystem`に現在の`vendorInventoryList`を書き戻す。 |
| `openOrCloseVendorMenuByButton()` | `devicesManager`でデバイスを使用/解除し、バンクの使用状態を`menuOpened`に合わせ、一時登録を外す。 |
| `openOrCloseVendorMenu(bool state)` | `menuOpened`とポーズメニューを切り替え、ベンダーメニュー表示、UIリセット、購入モード設定、カメラ有効化、更新コルーチン開始を行う。 |
| `updateAllInventoryVendorUI()` | カテゴリ名・商品名・選択中オブジェクト名と説明のテキストを、ローカライズを反映して更新するだけ。 |
| `resetVendorUIState()` | 選択状態やプレビュー、価格表示を初期化し、メニュー開放時は売却分の在庫反映とスロット生成、閉鎖時は全リスト破棄を行う。 |
| `createCategorySlots()` | 商品が存在するインベントリカテゴリごとにカテゴリスロットを生成し、名前・アイコン・表示テキストを設定してリストに追加する。 |
| `createInventoryIcons()` | `vendorInventoryList`の各アイテムについて`createVendorObjectIcon`で商品アイコンを生成するだけ。 |
| `resetScrollRectAndScrollBarPositions()` | カテゴリ側スクロールを先頭に戻してレイアウトを再構築し、商品側のスクロール位置リセットも呼ぶ。 |
| `resetObjectScrollRectAndScrollBarPositions()` | `AutoScroll`コルーチンを開始して商品リストのスクロールバー位置を先頭へ戻すだけ。 |
| `createVendorObjectIcon(inventoryInfo currentInventoryInfo, int index)` | 商品スロットを生成し、名前・レベル・在庫数・買値/売値を設定して`button`を`inventoryInfo`に紐づけ、リストへ追加する。 |
| `destroyVendorObjectSlotPanelInfoList()` | `vendorInventoryList`の各要素が持つ`button`のGameObjectを破棄するだけ。 |
| `destroyVendorCategorySlotPanelInfoList()` | `vendorCategorySlotPanelInfoList`の各要素が持つ`button`のGameObjectを破棄するだけ。 |
| `getCategoryPressedButton(Button buttonObj)` | 押されたカテゴリを特定し、そのカテゴリの商品だけを表示（レベル・在庫で絞り込み）して先頭を選択、見出しとスクロールを更新する。 |
| `getObjectPressedButton(Button buttonObj)` | `buttonObj`に一致する商品スロットのインデックスを探し、`setObjectInfo`に渡す。無ければ-1を渡す。 |
| `setObjectInfo(int index)` | 指定インデックスの商品を選択してスロットを強調し、プレビュー用オブジェクトを生成してカメラFOV・名前・説明・個数を更新する。無効時は選択を解除する。 |
| `setVendorObjectSlotPanelInfoPressedState(bool state)` | 選択中の商品スロットの`pressedIcon`表示を`state`に合わせるだけ。 |
| `setVendorCategorySlotPanelInfoPressedState(bool state)` | 選択中のカテゴリスロットの`pressedIcon`表示を`state`に合わせるだけ。 |
| `enableObjectRotation()` | `objectInCamera`があれば`enableRotation`をtrueにするだけ。 |
| `disableObjectRotation()` | `enableRotation`をfalseにするだけ。 |
| `destroyObjectInCamera()` | `objectInCamera`があれば`Destroy`するだけ。 |
| `zoomInEnabled()` | `zoomingIn`をtrueにするだけ。 |
| `zoomInDisabled()` | `zoomingIn`をfalseにするだけ。 |
| `zoomOutEnabled()` | `zoomingOut`をtrueにするだけ。 |
| `zoomOutDisabled()` | `zoomingOut`をfalseにするだけ。 |
| `checkResetCameraFov(float targetValue)` | `inventoryCamera.fieldOfView`を`targetValue`に設定するだけ。 |
| `addObjectToUse()` | 選択中商品の数量を1増やし、無限在庫なら99、通常は在庫数を上限として`setNumberOfObjectsToUseText`で表示を更新する。 |
| `removeObjectToUse()` | 選択中商品の数量を1減らし、下限を1（在庫0なら0）に保って`setNumberOfObjectsToUseText`で表示を更新する。 |
| `startToAddObjectToUse()` | `addingObjectToUse`をtrueにし、数量加算の基準時刻`lastTimeConfigureNumberOfObjects`を記録するだけ。 |
| `stopToAddObjectToUse()` | `addingObjectToUse`をfalseにし、加算時刻と高速加算フラグをリセットするだけ。 |
| `startToRemoveObjectToUse()` | `removinvObjectToUse`をtrueにし、数量減算の基準時刻`lastTimeConfigureNumberOfObjects`を記録するだけ。 |
| `stopToRemoveObjectToUse()` | `removinvObjectToUse`をfalseにし、減算時刻と高速加算フラグをリセットするだけ。 |
| `resetAndDisableNumberOfObjectsToUseMenu()` | `resetNumberOfObjectsToUse`を呼ぶだけ。 |
| `resetNumberOfObjectsToUse()` | 選択中商品の数量を1（在庫0なら0、未選択なら1）に戻し、テキスト表示を更新する。 |
| `setNumberOfObjectsToUseText(int amount)` | 数量テキストを設定し、選択中商品の単価と`amount`倍の合計金額を買値/売値と符号付きで表示する。 |
| `setBuyMode()` | `buyingObjects`をtrueにしてリストを破棄し、バンク在庫を読み直してUIを初期化、購入モードイベントを呼ぶ。 |
| `setSellMode()` | インベントリが空なら何もせず、売却可能な所持品を`vendorInventoryList`へ複製して数量をまとめ、売却モードイベントを呼ぶ。 |
| `joinSameInventoryObjectsAmount()` | `vendorInventoryList`内で同名アイテムの数量を1件に合算し、重複要素を削除する。 |
| `destroyAndClearAllList()` | 商品とカテゴリのスロットを破棄し、`vendorInventoryList`・カテゴリ・商品の各リストをクリアするだけ。 |
| `callEventOnSetBuyMode()` | `eventOnSetBuyMode`を呼び出すだけ。 |
| `callEventOnSetSellMode()` | `eventOnSetSellMode`を呼び出すだけ。 |
| `confirmBuyObject()` | 在庫・レベル・所持金を確認して合計金額を計算し、インベントリ追加かオブジェクト生成を行い、成功時に在庫減算・支払い・購入イベント・表示更新を行う。 |
| `confirmSellObject()` | 売却額を計算してプレイヤーのインベントリから数量分を削除し、在庫数を減らして売却リストへ追加、代金加算と売却イベント・表示更新を行う。 |
| `removeButton()` | 選択中商品のボタンとリスト要素を削除し、同カテゴリの別商品か先頭カテゴリを選択、無ければ購入モードに戻す。 |
| `updateCurrentInventoryObjectSlot()` | 選択中商品の在庫表示を、無限在庫なら"Inf"、在庫ありなら数量、0なら在庫切れ表示に更新するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnSetBuyMode` | `UnityEvent` | – |
| `eventOnSetSellMode` | `UnityEvent` | – |
| `eventOnPurchase` | `UnityEvent` | – |
| `eventOnSale` | `UnityEvent` | – |
| `eventOnObjectOutOfStock` | `UnityEvent` | – |
| `eventOnNotEnoughMoney` | `UnityEvent` | – |
| `eventOnNotEnoughLevel` | `UnityEvent` | – |
| `eventOnMaxObjectAmountReached` | `UnityEvent` | – |
