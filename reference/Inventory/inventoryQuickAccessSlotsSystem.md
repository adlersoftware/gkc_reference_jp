# inventoryQuickAccessSlotsSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/Inventory Quick Access System/inventoryQuickAccessSlotsSystem.cs:8`

**概要**: クイックアクセススロットの生成・表示・選択を管理するコンポーネント。番号キーやマウスホイールからのスロット選択、武器の装備/解除、HUD 上のスロット表示の切り替えを扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Number Quick Access Slots | `numberQuickAccessSlots` | `int` | 10 | – |
| Use Inventory Quick Access Slots | `useInventoryQuickAccessSlots` | `bool` | true | – |
| Time To Drag | `timeToDrag` | `float` | 0.5f | – |
| Use Drag Drop Inventory Slots | `useDragDropInventorySlots` | `bool` | – | – |
| Hide Empty Slots | `hideEmptySlots` | `bool` | – | – |

### Show Slots Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Quick Access Slots Always | `showQuickAccessSlotsAlways` | `bool` | true | – |
| Keep Quick Access Slots Hidden On Main Screen | `keepQuickAccessSlotsHiddenOnMainScreen` | `bool` | – | – |
| Show Quick Access Slots Parent Duration | `showQuickAccessSlotsParentDuration` | `float` | 1 | – |
| Quick Access Slots Parent Scale | `quickAccessSlotsParentScale` | `float` | 0.7f | – |
| Set Quick Access Slots Alpha Value Out Of Inventory | `setQuickAccessSlotsAlphaValueOutOfInventory` | `bool` | – | – |
| Quick Access Slots Alpha Value Out Of Inventory | `quickAccessSlotsAlphaValueOutOfInventory` | `float` | – | – |
| Show Quick Access Slots When Changing Slot | `showQuickAccessSlotsWhenChangingSlot` | `bool` | true | – |
| Show Quick Access Slot Selected Icon | `showQuickAccessSlotSelectedIcon` | `bool` | true | – |
| Swap Inventory Object Slots On Grid Enabled | `swapInventoryObjectSlotsOnGridEnabled` | `bool` | true | – |
| Min Time To Select Quick Access Slot | `minTimeToSelectQuickAccessSlot` | `float` | 0.4f | – |
| Show Slot Amount Enabled | `showSlotAmountEnabled` | `bool` | true | – |
| Show Slot Ammo Amount Enabled | `showSlotAmmoAmountEnabled` | `bool` | true | – |
| Assign Quick Accesss Slots On Number Keys On Inventory Opened Enabled | `assignQuickAccesssSlotsOnNumberKeysOnInventoryOpenedEnabled` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disable Quick Access Slots When Changing From Fire Weapons Mode | `disableQuickAccessSlotsWhenChangingFromFireWeaponsMode` | `bool` | false | – |
| Disable Quick Access Slots When Changing From Melee Weapons Mode | `disableQuickAccessSlotsWhenChangingFromMeleeWeaponsMode` | `bool` | false | – |
| Holster Fire Weapon If Slot Already Selected | `holsterFireWeaponIfSlotAlreadySelected` | `bool` | true | – |
| Sheathe Melee Weapons If Slot Already Selected | `sheatheMeleeWeaponsIfSlotAlreadySelected` | `bool` | true | – |
| Change Always To Weapon Without Double Selection | `changeAlwaysToWeaponWithoutDoubleSelection` | `bool` | – | – |

### Input Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Quick Access Input Number Keys Enabled | `quickAccessInputNumberKeysEnabled` | `bool` | true | – |
| Quick Access Input Mouse Wheel Active | `quickAccessInputMouseWheelActive` | `bool` | – | – |
| Change Weapons With Keys Active | `changeWeaponsWithKeysActive` | `bool` | – | – |
| Use Events On Change Weapons With Keys Active | `useEventsOnChangeWeaponsWithKeysActive` | `bool` | – | – |
| Events On Change Weapons With Keys Active | `eventsOnChangeWeaponsWithKeysActive` | `eventParameters.eventToCallWithBool` | – | – |

### Character Customization Slots Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Customization Slot Game Object List | `characterCustomizationSlotGameObjectList` | `List<GameObject>` | new List<GameObject> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Current Object Can Be Equipped | `currentObjectCanBeEquipped` | `bool` | – | – |
| Current Object Can Be Used | `currentObjectCanBeUsed` | `bool` | – | – |
| Current Slot Index | `currentSlotIndex` | `int` | – | – |
| Pressed Objec Without Equip Or Use Property | `pressedObjecWithoutEquipOrUseProperty` | `bool` | – | – |
| Dragged From Inventory List | `draggedFromInventoryList` | `bool` | – | – |
| Dragged From Quick Access Slots | `draggedFromQuickAccessSlots` | `bool` | – | – |
| Inventory Opened | `inventoryOpened` | `bool` | – | – |
| Customizing Character Active | `customizingCharacterActive` | `bool` | – | – |
| Check Object Categories To Use Active | `checkObjectCategoriesToUseActive` | `bool` | – | – |
| Current Category List To Use Active | `currentCategoryListToUseActive` | `List<string>` | new List<string> () | – |
| Check Slots Category Name To Drop | `checkSlotsCategoryNameToDrop` | `bool` | – | – |
| Quick Access Input Number Keys Paused | `quickAccessInputNumberKeysPaused` | `bool` | – | – |
| Change Of Weapons In Proccess | `changeOfWeaponsInProccess` | `bool` | – | – |

### Quick Access Slots Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Customization Slot List | `characterCustomizationSlotList` | `List<inventoryQuickAccessSlotElement.quickAccessSlotInfo>` | new List<inventoryQuickAccessSlotElem… | – |
| Quick Access Slot Info List | `quickAccessSlotInfoList` | `List<inventoryQuickAccessSlotElement.quickAccessSlotInfo>` | new List<inventoryQuickAccessSlotElem… | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Set Fire Weapons Mode | `eventToSetFireWeaponsMode` | `UnityEvent` | – | – |
| Event To Set Melee Weapons Mode | `eventToSetMeleeWeaponsMode` | `UnityEvent` | – | – |

### UI Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slot Prefab | `slotPrefab` | `GameObject` | – | – |
| Instantiate Quick Slot Prefab Enabled | `instantiateQuickSlotPrefabEnabled` | `bool` | true | – |
| Quick Access Slots List | `quickAccessSlotsList` | `List<GameObject>` | new List<GameObject> () | – |
| Inventory Quick Access Slots | `inventoryQuickAccessSlots` | `GameObject` | – | – |
| Quick Access Slot To Move | `quickAccessSlotToMove` | `GameObject` | – | – |
| Quick Access Slot Selected Icon | `quickAccessSlotSelectedIcon` | `GameObject` | – | – |
| Quick Access Slots Parent On Inventory | `quickAccessSlotsParentOnInventory` | `Transform` | – | – |
| Quick Access Slots Parent Out Of Inventory | `quickAccessSlotsParentOutOfInventory` | `Transform` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Inventory Manager | `mainInventoryManager` | `inventoryManager` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Melee Weapons Grabbed Manager | `mainMeleeWeaponsGrabbedManager` | `meleeWeaponsGrabbedManager` | – | – |
| Player Input | `playerInput` | `playerInputManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `initializeQuickAccessSlots()` | スロットを所定数生成して番号表示と`quickAccessSlotInfoList`を構築し、武器のキー切り替えを止める。 |
| `enableOrDisableAllQuickAccessSlots(bool state)` | `hideEmptySlots`有効時は全スロット表示を`state`に合わせ、無効化時は空きスロットだけ隠す。 |
| `setOnQuickSlotsCurrentObjectDirectly(inventoryInfo currentInventoryInfo, int quickAccessSlotIndex)` | 指定スロット、または`-1`なら空きスロットに`inventoryInfo`を割り当て、`checkDroppedSlot`で装備する。 |
| `updateInventoryOpenedState()` | インベントリ表示中の入力をレイキャストしてドラッグ状態を進め、最後に`resetDragAndDropSlotState`を呼ぶ。 |
| `checkDroppedSlot()` | 離した位置に応じ、スロットへの割り当てや武器の入れ替え・二丁化・装備解除を行い、最後にドラッグ状態をリセットする。 |
| `updateQuickAccessInputKeysState(bool inventoryMenuOpened)` | 番号キーを読み、インベントリ表示中は現在のオブジェクトをスロットへ割り当て、非表示中はスロットを選択する。 |
| `inputSetSlotByIndex(int currentNumberInput)` | 番号キーを0始まりのインデックスに変換し、入力可否を確認して`checkQuickAccessSlotToSelect`を呼ぶ。 |
| `setQuickAccessInputNumberKeysPausedState(bool state)` | `quickAccessInputNumberKeysPaused`を設定するだけ。 |
| `selectFirstMeleeWeaponAvailable()` | 有効なスロットを先頭から探し、最初の近接武器スロットを`checkQuickAccessSlotToSelect`で選択する。 |
| `selectFirstFireWeaponAvailable()` | 有効なスロットを先頭から探し、最初の射撃武器（非近接）のスロットを選択する。 |
| `selectFirstGeneralWeaponAvailable()` | 先頭から有効な武器スロットを探し、`checkQuickAccessSlotToSelect`で選択する。 |
| `selectCurrentSlotWeaponIfAvailable()` | `currentSlotIndex`のスロットが有効かつ武器なら選択して`true`を返し、それ以外は`false`を返す。 |
| `checkQuickAccessSlotToSelectByName(string objectOnSlotName)` | 有効なスロットから`Name`が`objectOnSlotName`と一致するものを探し、見つかればそのスロットを選択する。 |
| `setOverrideChangeToWeaponWithoutDoubleSelectionState(bool state)` | `changeToWeaponWithoutDoubleSelection`を設定するだけ。 |
| `changeFromMeleeToFireWeapons(string weaponName, int quickAccessSlotIndex)` | 実行中の武器切り替えコルーチンを止め、近接から射撃への`changeOfWeaponsCoroutine`を開始する。 |
| `changeFromFireToMeleeWeapons(string weaponName, int quickAccessSlotIndex)` | 実行中の武器切り替えコルーチンを止め、射撃から近接への`changeOfWeaponsCoroutine`を開始する。 |
| `stopChangeOfWeaponsCoroutine()` | `changeBetweenWeaponsCoroutine`を止め、`changeOfWeaponsInProccess`を`false`にする。 |
| `changeToMeleeWeapons(string meleeWeaponName)` | スロット一覧から`meleeWeaponName`の位置を探し、見つかれば近接武器切り替えコルーチンを開始する。 |
| `inputSelectNextOrPreviousQuickAccessSlot(bool state)` | `state`の向きに次の有効なスロットを循環探索して選択する（イベント使用時はイベントのみ呼ぶ）。 |
| `inputNextOrPreviousQuickAccessSlotByMouseWheel(bool state)` | `quickAccessInputMouseWheelActive`が有効なときだけ前後スロット選択の入力処理へ渡す。 |
| `checkIfWeaponSharesPocketInWeaponSlots(string weaponName)` | 有効な単発射撃武器スロットを走査し、`weaponName`と同一ポケットかを判定して返す。 |
| `updateSingleWeaponSlotInfo(string currentRighWeaponName, string currentLeftWeaponName)` | 右武器の番号キーのスロットを更新し、左武器を空きスロットへ移すか、空きが無ければ解除する。 |
| `updateSingleWeaponSlotInfoWithoutAddingAnotherSlot(string currentRighWeaponName)` | 右武器のスロットだけを単発武器として更新し、`activatingDualWeaponSlot`を再設定する。 |
| `updateDualWeaponSlotInfo(string currentRighWeaponName, string currentLeftWeaponName)` | 右/左武器の既存スロットを調べ、二丁持ち化や退避を行って`updateQuickAccessSlotInfo`で反映する。 |
| `updateQuickAccessSlotInfo(int slotIndex, inventoryInfo currentSlotToMove, inventoryQuickAccessSlotElement.quickAccessSlotInfo slotToUnEquip, playerWeaponSystem secondaryWeaponToEquip)` | `slotIndex`へ`currentSlotToMove`のアイコン等を設定し、`slotToUnEquip`指定時はそのスロットを空にする。 |
| `updateQuickAccessSlotAmountByName(string objectName)` | `objectName`のスロットを探し、数量0以下なら空に、それ以外は`updateQuickAccesSlotAmount`で更新する。 |
| `updateQuickAccesSlotAmount(int slotIndex)` | 指定スロットの数量テキストを、武器なら弾薬、その他は個数（無限なら`Inf`）に更新する。番号`-1`は末尾。 |
| `updateAllQuickAccessSlotsAmount()` | 全スロットに対して`updateQuickAccesSlotAmount`を呼び、数量表示をまとめて更新する。 |
| `getFirstSingleWeaponSlot(string weaponNameToAvoid)` | 有効かつ非近接・非二丁のスロットから`weaponNameToAvoid`以外の名前を返し、無ければ空文字を返す。 |
| `showQuickAccessSlotsParentWhenSlotSelectedByName(string objectName)` | 設定有効時、`objectName`のスロットを探して表示コルーチンを開始する。 |
| `showQuickAccessSlotsParentWhenSlotSelected(int slotIndex)` | インベントリ非表示中かつ設定有効なとき、`slotIndex`の表示コルーチンを開始し直す。 |
| `stopShowQuickAccessSlotsParentWhenSlotSelectedCoroutuine()` | `slotsParentCouroutine`があれば停止するだけ。 |
| `setShowQuickAccessSlotsAlwaysState(bool state)` | `showQuickAccessSlotsAlways`を設定するだけ。 |
| `isShowQuickAccessSlotsAlwaysActive()` | `showQuickAccessSlotsAlways`の値を返すだけ。 |
| `updateCurrentlySelectedSlotIcon(int slotIndex, bool activeCurrentQuickAccessSlot)` | `slotIndex`のスロットだけ`currentlySelectedIcon`を点灯し、`currentSlotIndex`も更新する。 |
| `checkModeToUpdateWeaponCurrentlySelectedIcon()` | 現在のモードに応じた対象スロットを求め、`updateCurrentlySelectedSlotIcon`でアイコンを更新する。 |
| `disableCurrentlySelectedIcon()` | 全スロットの`currentlySelectedIcon`を非表示にする。 |
| `selectQuickAccessSlotByPressingSlot(GameObject buttonToCheck)` | 入力可能かつインベントリ非表示のとき、`buttonToCheck`に対応するスロットを選択する。 |
| `moveQuickAccessSlotsOutOfInventory()` | スロット群をインベントリ外の親へ移し、背景アルファを`quickAccessSlotsAlphaValueOutOfInventory`にする。 |
| `moveQuickAccessSlotsToInventory()` | スロット群をインベントリ内の親へ戻して等倍にし、選択アイコンを消して背景アルファを1にする。 |
| `setQuickAccessSlotsBackgroundColorAlphaValue(float newAlphaValue)` | 設定有効時、全スロットの背景色アルファを`newAlphaValue`にする。 |
| `enableOrDisableHUD(bool state)` | `enableOrDisableQuickAccessSlotsParentOutOfInventory`へそのまま渡すだけ。 |
| `enableOrDisableQuickAccessSlotsParentOutOfInventory(bool state)` | ポーズ中でなければ、インベントリ外のスロット親の表示を`state`に切り替える。 |
| `checkToEnableOrDisableQuickAccessSlotsParentOutOfInventory(bool state)` | ポーズ中でなく`showQuickAccessSlotsAlways`有効なときだけ、スロット親表示を`state`に切り替える。 |
| `checkToEnableOrDisableQuickAccessSlotsParentOutOfInventoryFromFireWeaponsMode(bool state)` | 射撃モード離脱時の無効化設定を確認し、`showQuickAccessSlotsAlways`有効時に表示を`state`へ切り替える。 |
| `checkToEnableOrDisableQuickAccessSlotsParentOutOfInventoryFromMeleeWeaponsMode(bool state)` | 近接モード離脱時の無効化設定を確認し、`showQuickAccessSlotsAlways`有効時に表示を`state`へ切り替える。 |
| `setInventoryQuickAccessSlotsActiveState(bool state)` | `inventoryQuickAccessSlots`のアクティブ状態を`state`に合わせるだけ。 |
| `setShowQuickAccessSlotsPausedState(bool state)` | `showQuickAccessSlotsPaused`を設定するだけ。 |
| `resetDragAndDropSlotState()` | `activatingDualWeaponSlot`を解除し、ドラッグ用オブジェクトと各判定フラグを初期化する。 |
| `setOpenOrCloseInventoryMenuState(bool state)` | `inventoryOpened`を更新し、ドラッグ/タッチ状態を戻して全スロット表示を`state`に合わせる。 |
| `setCustomizingCharacterActiveState(bool state)` | `customizingCharacterActive`を設定し、`currentQuickAccessList`をカスタマイズ用リストへ切り替える。 |
| `isCustomizingCharacterActive()` | `customizingCharacterActive`の値を返すだけ。 |
| `getCurrentQuickAccessList()` | `currentQuickAccessList`を返すだけ。 |
| `setCheckObjectCategoriesToUseActiveState(bool state)` | `checkObjectCategoriesToUseActive`を設定するだけ。 |
| `setCurrentCategoryListToUseActive(List<string> newList)` | `currentCategoryListToUseActive`に`newList`を設定するだけ。 |
| `setCheckSlotsCategoryNameToDropActive(bool state)` | `checkSlotsCategoryNameToDrop`を設定するだけ。 |
| `setKeepQuickAccessSlotsHiddenOnMainScreenState(bool state)` | `keepQuickAccessSlotsHiddenOnMainScreen`を設定するだけ。 |
| `setShowQuickAccessSlotsAlwaysStateFromEditor(bool state)` | `setShowQuickAccessSlotsAlwaysState`を呼び、`updateComponent`でシーンを更新する。 |
| `setKeepQuickAccessSlotsHiddenOnMainScreenStateFromEditor(bool state)` | `setKeepQuickAccessSlotsHiddenOnMainScreenState`を呼び、`updateComponent`でシーンを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToSetFireWeaponsMode` | `UnityEvent` | – |
| `eventToSetMeleeWeaponsMode` | `UnityEvent` | – |
