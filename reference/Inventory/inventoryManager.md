# inventoryManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `inventoryManagerInfo`
- **ソース**: `Inventory/inventoryManager.cs:13`

**概要**: プレイヤーの所持品`inventoryList`を保持し、拾得・使用・装備と解除・ドロップ・合成・耐久度・スロットUI・イベント通知を扱うインベントリの中核コンポーネントです。アイテム定義やプレハブは`mainInventoryListManager`から取得し、クイックアクセス枠やポーズメニューとも連携します。

**公式ドキュメント抜粋**（[Inventory Manager](../../docs/player-controller-components/player-controller/inventory-manager.md)）

> Used to manage the inventory that the player carries with it, including to configure the initial inventory that the player has at the beginning of the game, which can be empty or contain certain items or weapons, which can be configured as equipped at the start too. It also allows to combine, drop, use, examine and more actions with the objects, including showing the weapons slots equipped in-game.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory Enabled | `inventoryEnabled` | `bool` | – | ONにするとインベントリ機能全体を有効化する。 |
| Open Inventory Menu Enabled | `openInventoryMenuEnabled` | `bool` | true | ONにするとインベントリメニューを開く入力を受け付ける。 |

### Inventory Slots Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Infinite Slots | `infiniteSlots` | `bool` | – | ONにするとスロット数の上限がなくなる。 |
| Inventory Slot Amount | `inventorySlotAmount` | `int` | – | インベントリに用意するスロットの総数。 / 表示条件: `infiniteSlots` がオフのとき |
| Infinite Amount Per Slot | `infiniteAmountPerSlot` | `bool` | – | ONにすると1スロットの数量上限を撤廃する。 |
| Amount Per Slot | `amountPerSlot` | `int` | – | 1スロットあたりの既定の最大所持数。 / 表示条件: `infiniteAmountPerSlot` がオフのとき |
| Combine Elements At Drop | `combineElementsAtDrop` | `bool` | – | ONにするとドロップ時に同名の束を自動で詰め直す。 / 表示条件: `infiniteAmountPerSlot` がオフのとき |
| Ignore Maximum Object Amount | `ignoreMaximumObjectAmount` | `bool` | – | ONにするとアイテムごとの最大所持数チェックを省略する。 |

### Other Inventory Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Button Usable Color | `buttonUsable` | `Color` | – | 使用可能なボタンに適用する色。 |
| Button Not Usable Color | `buttonNotUsable` | `Color` | – | 使用不可のボタンに適用する色。 |
| Use Only When Needed Amount To Use Object | `useOnlyWhenNeededAmountToUseObject` | `bool` | – | ONにすると要求数ちょうどの個数だけ使用する。 |
| Active Number Of Objects To Use Menu | `activeNumberOfObjectsToUseMenu` | `bool` | – | ONにすると使用前に個数を選ぶメニューを出す。 |
| Set Total Amount When Drop Object | `setTotalAmountWhenDropObject` | `bool` | – | ONにするとドロップ数を1つのプレハブにまとめる。 |
| Configure Number Objects To Use Rate | `configureNumberObjectsToUseRate` | `float` | 0.4f | 個数選択の増減が1回進む間隔(秒)。 |
| Faster Number Objects To Use Rate | `fasterNumberObjectsToUseRate` | `float` | 0.1f | 押し続け時の高速な増減間隔(秒)。 |
| Wait Time To Use Faster Number Objects To Use Rate | `waitTimeToUseFasterNumberObjectsToUseRate` | `float` | 1 | 高速な増減へ切り替わるまでの秒数。 |
| Use Blur UI Panel | `useBlurUIPanel` | `bool` | true | ONにするとメニュー表示中に背景をぼかす。 |
| Show Inventory Objects Name | `showInventoryObjectsName` | `bool` | true | ONにするとスロットにアイテム名を表示する。 |
| Show Object Amount If Equal One | `showObjectAmountIfEqualOne` | `bool` | true | ONにすると所持数が1でも個数を表示する。 |
| Select First Inventory Object When Opening Menu | `selectFirstInventoryObjectWhenOpeningMenu` | `bool` | true | ONにすると開いた際に先頭スロットを選択する。 |
| Drop Single Object On Infinite Amount | `dropSingleObjectOnInfiniteAmount` | `bool` | true | ONにすると無限所持アイテムを落とした時に所持数が0になる。 |
| Menu Panel Name | `menuPanelName` | `string` | "Inventory Manager" | ポーズ管理に登録するメニューの識別名。 |

### Objects Durability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Durability On Object Enabled | `checkDurabilityOnObjectEnabled` | `bool` | true | ONにするとアイテムの耐久度を管理する。 |
| Destroy Objects On Empty Durability | `destroyObjectsOnEmptyDurability` | `bool` | – | ONにすると耐久度が尽きたアイテムを消す。 |
| Drop Objects On Empty Durability | `dropObjectsOnEmptyDurability` | `bool` | – | ONにすると耐久度が尽きたアイテムを地面に落とす。 |
| Set Objects As Broken On Empty Durability | `setObjectsAsBrokenOnEmptyDurability` | `bool` | – | ONにすると耐久度切れを故障状態にする。 |
| Unequip Object On Empty Durability | `unequipObjectOnEmptyDurability` | `bool` | – | ONにすると耐久度切れ時に装備を外す。 |
| Broken Objects Cant Be Used | `brokenObjectsCantBeUsed` | `bool` | – | ONにすると故障したアイテムの使用を禁止する。 |
| Broken Objects Cant Be Equipped | `brokenObjectsCantBeEquipped` | `bool` | – | ONにすると故障したアイテムの装備を禁止する。 |

### Weight Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Weight Limit To Pick Objects | `checkWeightLimitToPickObjects` | `bool` | – | ONにすると重量上限を超える取得を制限する。 / 表示条件: `showAllSettings.boolValue \|\| showWeightSettings.boolValue` |
| Main Inventory Weight Manager | `mainInventoryWeightManager` | `inventoryWeightManager` | – | 重量判定を行う管理コンポーネントへの参照。 / 表示条件: `showAllSettings.boolValue \|\| showWeightSettings.boolValue` |

### Inventory Weapons Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Store Picked Weapons On Inventory | `storePickedWeaponsOnInventory` | `bool` | – | ONにすると拾った武器を手に持たず収納する。 / 表示条件: `showAllSettings.boolValue \|\| showWeaponsSettings.boolValue` |
| Equip Weapons When Picked | `equipWeaponsWhenPicked` | `bool` | – | ONにすると拾った武器をその場で装備する。 / 表示条件: `showAllSettings.boolValue \|\| showWeaponsSettings.boolValue && storePickedWeaponsOnInventory.boolValue` |
| Equip Picked Weapon Only It Not Previous Weapon Equipped | `equipPickedWeaponOnlyItNotPreviousWeaponEquipped` | `bool` | – | ONにすると既に武器を装備中なら持ち替えない。 / 表示条件: `showAllSettings.boolValue \|\| showWeaponsSettings.boolValue && storePickedWeaponsOnInventory.boolValue` |
| Change To Fire Weapons Mode When Picking Fire Weapon | `changeToFireWeaponsModeWhenPickingFireWeapon` | `bool` | – | ONにすると射撃武器を拾うと射撃モードへ切替える。 / 表示条件: `showAllSettings.boolValue \|\| showWeaponsSettings.boolValue && storePickedWeaponsOnInventory.boolValue` |
| Change To Melee Weapons Mode When Picking Melee Weapon | `changeToMeleeWeaponsModeWhenPickingMeleeWeapon` | `bool` | – | ONにすると近接武器を拾うと近接モードへ切替える。 / 表示条件: `showAllSettings.boolValue \|\| showWeaponsSettings.boolValue && storePickedWeaponsOnInventory.boolValue` |
| Use Max Number Of Weapons To Equip | `useMaxNumberOfWeaponsToEquip` | `bool` | – | ONにすると同時に装備できる武器数の上限を適用する。 / 表示条件: `showAllSettings.boolValue \|\| showWeaponsSettings.boolValue && storePickedWeaponsOnInventory.boolValue` |
| Max Number Of Weapons To Equip | `maxNumberOfWeaponsToEquip` | `int` | – | 同時に装備できる武器の最大数。 / 表示条件: `storePickedWeaponsOnInventory.boolValue && useMaxNumberOfWeaponsToEquip.boolValue` |
| Max Number Of Weapons Equipped Message | `maxNumberOfWeaponsEquippedMessage` | `string` | – | 武器の装備上限に達した時に出す文言。 / 表示条件: `storePickedWeaponsOnInventory.boolValue && useMaxNumberOfWeaponsToEquip.boolValue` / TextArea (1, 10) |
| Take Ammo From Weapons Already Carried | `takeAmmoFromWeaponsAlreadyCarried` | `bool` | – | ONにすると所持済み武器の弾薬として拾得物を加算する。 / 表示条件: `showAllSettings.boolValue \|\| showWeaponsSettings.boolValue && storePickedWeaponsOnInventory.boolValue` |
| Draw Initial Weapon Equipped On Start Enabled | `drawInitialWeaponEquippedOnStartEnabled` | `bool` | – | ONにすると開始時に装備中の武器を手に持つ。 / 表示条件: `showAllSettings.boolValue \|\| showWeaponsSettings.boolValue && storePickedWeaponsOnInventory.boolValue` |
| Draw First Melee Weapon Available | `drawFirstMeleeWeaponAvailable` | `bool` | – | ONにすると開始時に所持する近接武器を選択する。 / 表示条件: `storePickedWeaponsOnInventory.boolValue && drawInitialWeaponEquippedOnStartEnabled.boolValue` |
| Draw First Fire Weapon Available | `drawFirstFireWeaponAvailable` | `bool` | – | ONにすると開始時に所持する射撃武器を選択する。 / 表示条件: `storePickedWeaponsOnInventory.boolValue && drawInitialWeaponEquippedOnStartEnabled.boolValue` |
| Draw Last Weapon Carried On Hands On Load Enabled | `drawLastWeaponCarriedOnHandsOnLoadEnabled` | `bool` | true | ONにするとロード時に前回持っていた武器を装備する。 / 表示条件: `showAllSettings.boolValue \|\| showWeaponsSettings.boolValue && storePickedWeaponsOnInventory.boolValue` |

### Examine Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Examine Object Before Store Enabled | `examineObjectBeforeStoreEnabled` | `bool` | – | ONにすると取得前にアイテムの観察を挟む。 / 表示条件: `showAllSettings.boolValue \|\| showExamineSettings.boolValue` |
| Distance To Place Object In Camera | `distanceToPlaceObjectInCamera` | `float` | 10 | 観察時にカメラからアイテムを離す距離。 / 表示条件: `showAllSettings.boolValue \|\| showExamineSettings.boolValue` |
| Place Object In Camera Speed | `placeObjectInCameraSpeed` | `float` | 10 | アイテムを観察位置まで移動させる速度。 / 表示条件: `showAllSettings.boolValue \|\| showExamineSettings.boolValue` |
| Number Of Rotations Object In Camera | `numberOfRotationsObjectInCamera` | `int` | 3 | 観察開始時にアイテムを回す周回数。 / 表示条件: `showAllSettings.boolValue \|\| showExamineSettings.boolValue` |
| Place Object In Camera Rotation Speed | `placeObjectInCameraRotationSpeed` | `float` | 0.02f | 観察開始時の回転補間に使う時間。 / 表示条件: `showAllSettings.boolValue \|\| showExamineSettings.boolValue` |
| Extra Camera Fov On Examine Objects | `extraCameraFovOnExamineObjects` | `float` | 20 | 観察時にカメラFOVへ加算する値。 / 表示条件: `showAllSettings.boolValue \|\| showExamineSettings.boolValue` |

### Inventory Show Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Inventory Camera Enabled | `useInventoryCameraEnabled` | `bool` | true | ONにすると表示用カメラとライトを切替える。 / 表示条件: `showAllSettings.boolValue \|\| showExamineSettings.boolValue` |
| Rotation Speed | `rotationSpeed` | `float` | – | メニュー内でアイテムを回転させる速度。 / 表示条件: `showAllSettings.boolValue \|\| showExamineSettings.boolValue` |
| Zoom Speed | `zoomSpeed` | `float` | – | メニュー内カメラのズーム速度。 / 表示条件: `showAllSettings.boolValue \|\| showExamineSettings.boolValue` |
| Max Zoom Value | `maxZoomValue` | `float` | – | ズームインした時のカメラFOVの下限値。 / 表示条件: `showAllSettings.boolValue \|\| showExamineSettings.boolValue` |
| Min Zoom Value | `minZoomValue` | `float` | – | ズームアウト時の到達FOV値。 / 表示条件: `showAllSettings.boolValue \|\| showExamineSettings.boolValue` |

### Inventory Messages Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Message When Object Used | `showMessageWhenObjectUsed` | `bool` | true | ONにするとアイテム使用時にメッセージを出す。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` |
| Used Object Message | `usedObjectMessage` | `GameObject` | – | 使用結果などを表示するメッセージパネル。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` |
| Full Inventory Message | `fullInventoryMessage` | `GameObject` | – | インベントリが満杯の時に表示するパネル。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` |
| Full Inventory Message Time | `fullInventoryMessageTime` | `float` | 2 | 満杯メッセージを表示しておく秒数。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` |
| Combined Object Message | `combinedObjectMessage` | `GameObject` | – | 合成結果を表示するメッセージパネル。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` |
| Combine Object Message Time | `combineObjectMessageTime` | `float` | – | 合成メッセージを表示しておく秒数。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` |
| Used Object Message Time | `usedObjectMessageTime` | `float` | – | 使用メッセージを表示しておく秒数。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` |
| Unable To Use Object Message | `unableToUseObjectMessage` | `string` | – | アイテムを使用できない時の文言。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` / TextArea (1, 10) |
| Non Needed Amount Avaliable | `nonNeededAmountAvaliable` | `string` | – | 必要な個数が足りない時の文言。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` / TextArea (1, 10) |
| Object Not Found Message | `objectNotFoundMessage` | `string` | – | 対象のアイテムが見つからない時の文言。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` / TextArea (1, 10) |
| Cant Use This Object Here Message | `cantUseThisObjectHereMessage` | `string` | – | この場所では使えない時の文言。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` / TextArea (1, 10) |
| Unable To Combine Message | `unableToCombineMessage` | `string` | – | アイテムを合成できなかった時の文言。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` / TextArea (1, 10) |
| Can Be Combined But Object Is Full Message | `canBeCombinedButObjectIsFullMessage` | `string` | "These objects can be combined, but -… | 合成可能だが合成先が満杯な時の文言。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` / TextArea (1, 10) |
| Not Enough Space To Combine Message | `notEnoughSpaceToCombineMessage` | `string` | – | 合成先の空きが足りない時の文言。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` / TextArea (1, 10) |
| Weight Limit Reached Message | `weightLimitReachedMessage` | `string` | – | 所持重量の上限に達した時の文言。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` / TextArea (1, 10) |
| Object Too Much Heavy To Carry Message | `objectTooMuchHeavyToCarryMessage` | `string` | – | 重すぎて持ち運べない時の文言。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` / TextArea (1, 10) |
| Max Object Amount Reached Message Time | `maxObjectAmountReachedMessageTime` | `float` | 2 | 最大所持数メッセージの表示秒数。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` |
| Max Object Amount Reached Message | `maxObjectAmountReachedMessage` | `string` | "Can't store more units of this object" | アイテムの最大所持数に達した時の文言。 / 表示条件: `showAllSettings.boolValue \|\| showMessagesSettings.boolValue` / TextArea (1, 10) |

### Sound Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Audio Sounds | `useAudioSounds` | `bool` | – | ONにするとインベントリ操作時の効果音を再生する。 / 表示条件: `showAllSettings.boolValue \|\| showSoundsSettings.boolValue` |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | インベントリの効果音を再生するAudioSource。 / 表示条件: `showAllSettings.boolValue \|\| showSoundsSettings.boolValue` |

### Inventory Options On Slot Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Inventory Options On Slot | `useInventoryOptionsOnSlot` | `bool` | – | ONにするとスロット選択時に操作メニューを出す。 / 表示条件: `showAllSettings.boolValue \|\| showOthersSettings.boolValue` |
| Inventory Options On Slot Panel | `inventoryOptionsOnSlotPanel` | `RectTransform` | – | スロット操作メニューのRectTransform。 / 表示条件: `showAllSettings.boolValue \|\| showOthersSettings.boolValue && useInventoryOptionsOnSlot.boolValue` |
| Main Inventory Slot Options Buttons | `mainInventorySlotOptionsButtons` | `inventorySlotOptionsButtons` | – | スロット操作ボタンをまとめた管理コンポーネント。 / 表示条件: `showAllSettings.boolValue \|\| showOthersSettings.boolValue && useInventoryOptionsOnSlot.boolValue` |

### AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Used By AI | `usedByAI` | `bool` | – | ONにするとAI用として扱いプレイヤー操作を無効化する。 / 表示条件: `showAllSettings.boolValue \|\| showOthersSettings.boolValue` |

### Grab Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Send Grabbed Object To Inventory If Grabbing New One | `sendGrabbedObjectToInventoryIfGrabbingNewOne` | `bool` | – | ONにすると掴み直す際に所持中の物を収納する。 / 表示条件: `showAllSettings.boolValue \|\| showOthersSettings.boolValue` |
| Take Only One Unit To Grab | `takeOnlyOneUnitToGrab` | `bool` | – | ONにすると掴み出し時に1個だけ取り出す。 / 表示条件: `showAllSettings.boolValue \|\| showOthersSettings.boolValue` |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Inventory Initialized | `eventOnInventoryInitialized` | `UnityEvent` | – | インベントリ初期化完了時に発火するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event On Click Inventory Change | `eventOnClickInventoryChange` | `UnityEvent` | – | インベントリ内容の変更時に発火するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event On Inventory Slot Selected | `eventOnInventorySlotSelected` | `UnityEvent` | – | スロットが選択された時に発火するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event On Inventory Slot Un Selected | `eventOnInventorySlotUnSelected` | `UnityEvent` | – | スロットの選択が外れた時に発火するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event On Inventory Closed | `eventOnInventoryClosed` | `UnityEvent` | – | インベントリを閉じた時に発火するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event On Inventory Opened | `eventOnInventoryOpened` | `UnityEvent` | – | インベントリを開いた時に発火するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event On Inventory List Change | `eventOnInventoryListChange` | `UnityEvent` | – | 所持品リストが変化した時に発火するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Use Event On Inventory Object Equipped | `useEventOnInventoryObjectEquipped` | `bool` | – | ONにすると装備時のイベントを有効化する。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event On Inventory Object Equipped | `eventOnInventoryObjectEquipped` | `eventParameters.eventToCallWithString` | – | アイテム装備時に名前を渡して呼ぶイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useEventOnInventoryObjectEquipped.boolValue` |
| Use Event On Inventory Object Un Equipped | `useEventOnInventoryObjectUnEquipped` | `bool` | – | ONにすると装備解除時のイベントを有効化する。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event On Inventory Object Un Equipped | `eventOnInventoryObjectUnEquipped` | `eventParameters.eventToCallWithString` | – | 装備解除時に名前を渡して呼ぶイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useEventOnInventoryObjectUnEquipped.boolValue` |
| Use Event On Repair Current Object | `useEventOnRepairCurrentObject` | `bool` | true | ONにすると修理時のイベントを有効化する。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event On Repair Current Object | `eventOnRepairCurrentObject` | `UnityEvent` | – | 修理に成功した時に発火するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useEventOnRepairCurrentObject.boolValue` |
| Event On Unable To Repair Current Object | `eventOnUnableToRepairCurrentObject` | `UnityEvent` | – | 修理できなかった時に発火するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useEventOnRepairCurrentObject.boolValue` |
| Use Event If System Disabled | `useEventIfSystemDisabled` | `bool` | – | ONにすると機能無効時にイベントを発火する。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event If System Disabled | `eventIfSystemDisabled` | `UnityEvent` | – | インベントリが無効な時に発火するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useEventIfSystemDisabled.boolValue` |

### Save/Load Inventory Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Load Current Player Inventory From Save File | `loadCurrentPlayerInventoryFromSaveFile` | `bool` | true | ONにするとセーブファイルから所持品を読み込む。 / 表示条件: `showAllSettings.boolValue \|\| showSaveLoadSettings.boolValue` |
| Save Current Player Inventory To Save File | `saveCurrentPlayerInventoryToSaveFile` | `bool` | true | ONにすると所持品をセーブファイルへ書き込む。 / 表示条件: `showAllSettings.boolValue \|\| showSaveLoadSettings.boolValue` |
| Set Infinite Slot Values On Save Load | `setInfiniteSlotValuesOnSaveLoad` | `bool` | true | ONにするとロード時に無限スロット設定も復元する。 / 表示条件: `showAllSettings.boolValue \|\| showSaveLoadSettings.boolValue` |

### Inventory Menu State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | ONにするとインベントリ処理のログを出力する。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue` |

### Inventory List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory Panel | `inventoryPanel` | `GameObject` | – | インベントリ画面全体のパネル。 / 表示条件: `showElementSettings` がオンのとき |
| Inventory List Content | `inventoryListContent` | `GameObject` | – | スロットを並べるリストの親オブジェクト。 / 表示条件: `showElementSettings` がオンのとき |
| Inventory List Scroll Rect | `inventoryListScrollRect` | `ScrollRect` | – | スロット一覧のスクロール制御。 / 表示条件: `showElementSettings` がオンのとき |
| Object Icon | `objectIcon` | `GameObject` | – | スロットを生成する元になるアイコンボタン。 / 表示条件: `showElementSettings` がオンのとき |
| Equip Button | `equipButton` | `GameObject` | – | 装備操作を行うボタンのオブジェクト。 / 表示条件: `showElementSettings` がオンのとき |
| Unequip Button | `unequipButton` | `GameObject` | – | 装備解除ボタンのオブジェクト。 / 表示条件: `showElementSettings` がオンのとき |
| Use Button Image | `useButtonImage` | `Image` | – | 使用ボタンに表示するアイコン画像。 / 表示条件: `showElementSettings` がオンのとき |
| Equip Button Image | `equipButtonImage` | `Image` | – | 装備ボタンに表示するアイコン画像。 / 表示条件: `showElementSettings` がオンのとき |
| Unequip Button Image | `unequipButtonImage` | `Image` | – | 装備解除ボタンに表示する画像。 / 表示条件: `showElementSettings` がオンのとき |
| Drop Button Image | `dropButtonImage` | `Image` | – | ドロップボタンに表示する画像。 / 表示条件: `showElementSettings` がオンのとき |
| Combine Button Image | `combineButtonImage` | `Image` | – | 合成ボタンに表示するアイコン画像。 / 表示条件: `showElementSettings` がオンのとき |
| Examine Button Image | `examineButtonImage` | `Image` | – | 観察ボタンに表示するアイコン画像。 / 表示条件: `showElementSettings` がオンのとき |
| Discard Button Image | `discardButtonImage` | `Image` | – | 破棄ボタンに表示するアイコン画像。 / 表示条件: `showElementSettings` がオンのとき |
| Drop All Units Object Button Image | `dropAllUnitsObjectButtonImage` | `Image` | – | 全数ドロップボタンに表示する画像。 / 表示条件: `showElementSettings` がオンのとき |
| Examine Object Panel | `examineObjectPanel` | `GameObject` | – | アイテムを拡大観察する画面のパネル。 / 表示条件: `showElementSettings` がオンのとき |
| Examine Object Name | `examineObjectName` | `Text` | – | 観察画面に表示するアイテム名テキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Examine Object Description | `examineObjectDescription` | `Text` | – | 観察画面に表示する説明テキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Take Object In Examine Panel Button | `takeObjectInExaminePanelButton` | `GameObject` | – | 観察画面からアイテムを取得するボタン。 / 表示条件: `showElementSettings` がオンのとき |
| Current Object Name | `currentObjectName` | `Text` | – | 選択中アイテムの名前を表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Current Object Info | `currentObjectInfo` | `Text` | – | 選択中アイテムの情報を表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Object Image | `objectImage` | `RawImage` | – | 選択中アイテムを表示するRawImage。 / 表示条件: `showElementSettings` がオンのとき |
| Inventory Camera | `inventoryCamera` | `Camera` | – | メニュー内でアイテムを映すカメラ。 / 表示条件: `showElementSettings` がオンのとき |
| Inventory Light | `inventoryLight` | `Light` | – | メニュー内のアイテムを照らすライト。 / 表示条件: `showElementSettings` がオンのとき |
| Look Objects Position | `lookObjectsPosition` | `Transform` | – | メニュー内でアイテムを表示する位置。 / 表示条件: `showElementSettings` がオンのとき |
| Empty Inventory Prefab | `emptyInventoryPrefab` | `GameObject` | – | 空スロットやドロップ時に使う雛形プレハブ。 / 表示条件: `showElementSettings` がオンのとき |
| Number Of Objects To Use Menu | `numberOfObjectsToUseMenu` | `GameObject` | – | 使用数を選ぶポップアップメニュー。 / 表示条件: `showElementSettings` がオンのとき |
| Number Of Objects To Use Menu Rect Transform | `numberOfObjectsToUseMenuRectTransform` | `RectTransform` | – | 使用数メニューのRectTransform。 / 表示条件: `showElementSettings` がオンのとき |
| Number Of Objects To Use Text | `numberOfObjectsToUseText` | `Text` | – | 選択中の使用数を表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Number Of Objects To Use Menu Position | `numberOfObjectsToUseMenuPosition` | `RectTransform` | – | 使用数メニューを表示する基準位置。 / 表示条件: `showElementSettings` がオンのとき |
| Number Of Objects To Drop Menu Position | `numberOfObjectsToDropMenuPosition` | `RectTransform` | – | ドロップ数メニューを表示する基準位置。 / 表示条件: `showElementSettings` がオンのとき |
| Inventory Slots Scrollbar | `inventorySlotsScrollbar` | `Scrollbar` | – | スロット一覧のスクロールバー。 / 表示条件: `showElementSettings` がオンのとき |
| Inventory Object Infor Scrollbar | `inventoryObjectInforScrollbar` | `Scrollbar` | – | アイテム情報欄のスクロールバー。 / 表示条件: `showElementSettings` がオンのとき |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | 武器管理コンポーネントへの参照。 / 表示条件: `showElementSettings` がオンのとき |
| Main Melee Weapons Grabbed Manager | `mainMeleeWeaponsGrabbedManager` | `meleeWeaponsGrabbedManager` | – | 近接武器の管理コンポーネントへの参照。 / 表示条件: `showElementSettings` がオンのとき |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | プレイヤー制御コンポーネントへの参照。 / 表示条件: `showElementSettings` がオンのとき |
| Pause Manager | `pauseManager` | `menuPause` | – | ポーズメニュー管理コンポーネントへの参照。 / 表示条件: `showElementSettings` がオンのとき |
| Player Input | `playerInput` | `playerInputManager` | – | プレイヤー入力管理コンポーネントへの参照。 / 表示条件: `showElementSettings` がオンのとき |
| Main Inventory List Manager | `mainInventoryListManager` | `inventoryListManager` | – | インベントリリスト管理コンポーネントへの参照。 / 表示条件: `showElementSettings` がオンのとき |
| Using Devices Manager | `usingDevicesManager` | `usingDevicesSystem` | – | デバイス使用管理コンポーネントへの参照。 / 表示条件: `showElementSettings` がオンのとき |
| Main Inventory Menu Panels System | `mainInventoryMenuPanelsSystem` | `inventoryMenuPanelsSystem` | – | インベントリのパネル切替システムへの参照。 / 表示条件: `showElementSettings` がオンのとき |
| Main Inventory Bank UI System | `mainInventoryBankUISystem` | `inventoryBankUISystem` | – | インベントリバンクUIへの参照。 / 表示条件: `showElementSettings` がオンのとき |
| Main Vendor UI System | `mainVendorUISystem` | `vendorUISystem` | – | ベンダー取引UIの管理コンポーネントへの参照。 / 表示条件: `showElementSettings` がオンのとき |
| Main Inventory Quick Access Slots System | `mainInventoryQuickAccessSlotsSystem` | `inventoryQuickAccessSlotsSystem` | – | クイックアクセススロット管理への参照。 / 表示条件: `showElementSettings` がオンのとき |
| Main Inventory Manager Prefab | `mainInventoryManagerPrefab` | `GameObject` | – | シーンに無い時に生成する管理用プレハブ。 / 表示条件: `showElementSettings` がオンのとき |
| Main Inventory Character Customization System | `mainInventoryCharacterCustomizationSystem` | `inventoryCharacterCustomizationSystem` | – | キャラクターカスタマイズ管理への参照。 / 表示条件: `showElementSettings` がオンのとき |

### Initial Inventory List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Scriptable Object For Initial Inventory List | `useScriptableObjectForInitialInventoryList` | `bool` | – | ONにすると初期所持品をデータアセットから設定する。 |
| Use Multiple Scriptable Object For Initial Inventory List | `useMultipleScriptableObjectForInitialInventoryList` | `bool` | – | ONにすると複数の初期所持品データを併用する。 / 表示条件: `useScriptableObjectForInitialInventoryList` がオンのとき |
| Main Initial Inventory List Data | `mainInitialInventoryListData` | `initialinventoryListData` | – | 初期所持品を定義したデータアセットへの参照。 / 表示条件: `useScriptableObjectForInitialInventoryList` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `examiningObject` | `bool` | – | – |
| `inventoryOpened` | `bool` | – | – |
| `currentInventoryObject` | `inventoryInfo` | – | – |
| `firstObjectToCombine` | `inventoryInfo` | – | – |
| `secondObjectToCombine` | `inventoryInfo` | – | – |
| `mainInventoryManagerName` | `string` | "Main Inventory Manager" | – |
| `inventoryListManagerList` | `List<inventoryListElement>` | new List<inventoryListElement> () | – |
| `menuIconElementList` | `List<inventoryMenuIconElement>` | new List<inventoryMenuIconElement> () | – |
| `mainMultipleInitialInventoryListData` | `List<initialinventoryListData>` | new List<initialinventoryListData> () | – |
| `inventoryManagerListString` | `string []` | – | – |
| `inventoryManagerStringInfoList` | `List<inventoryManagerStringInfo>` | new List<inventoryManagerStringInfo> () | – |
| `quickAccessSlotInfoList` | `List<inventoryQuickAccessSlotElement.quickAccessSlotInfo>` | new List<inventoryQuickAccessSlotElem… | – |
| `usableInventoryObjectInfoList` | `List<usableInventoryObjectInfo>` | new List<usableInventoryObjectInfo> () | – |
| `initializingInventory` | `bool` | – | – |
| `inventoryOptionsOnSlotPanelActive` | `bool` | – | – |
| `showElementSettings` | `bool` | – | – |
| `showAllSettings` | `bool` | – | – |
| `showWeightSettings` | `bool` | – | – |
| `showWeaponsSettings` | `bool` | – | – |
| `showExamineSettings` | `bool` | – | – |
| `showMessagesSettings` | `bool` | – | – |
| `showSoundsSettings` | `bool` | – | – |
| `showOthersSettings` | `bool` | – | – |
| `showEventSettings` | `bool` | – | – |
| `showSaveLoadSettings` | `bool` | – | – |
| `showDebugSettings` | `bool` | – | – |
| `currentNumberOfWeaponsEquipped` | `int` | 0 | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setExamineObjectBeforeStoreEnabledState(bool state)` | フラグ`examineObjectBeforeStoreEnabled`に`state`を代入するだけの単純な設定メソッド。 |
| `isExamineObjectBeforeStoreEnabled()` | フラグ`examineObjectBeforeStoreEnabled`の値をそのまま返すだけの取得メソッド。 |
| `setInventoryFromInventoryListManager()` | 初期インベントリ定義（ScriptableObject/リスト）から`inventoryList`を構築し、スロット上限でスタック分割、`addInventoryObject`がfalseの要素を除去する。 |
| `setInventory(bool creatingInventoryIcons)` | `checkInventoryAmountPerSpace`と`checkRemainigEmptyInventorySlots`を実行し、引数がtrueなら`createInventoryIcons`でUIアイコンも再生成する。 |
| `checkInventoryAmountPerSpace()` | 各要素の量がスロット上限を超える分を`reOrderInventoryList`で別スロットへ移し、`infiniteAmountPerSlot`時は何もしない。 |
| `reOrderInventoryList(inventoryInfo objectInfo, int amount, int index)` | 満杯なら空きスロットへ`amount`を移すか`inventoryAmountNotTaken`に計上し、空きがあれば`index`直後に複製を挿入して新インデックスを返す。 |
| `checkRemainigEmptyInventorySlots()` | `infiniteSlots`でなければ`inventoryList`が`inventorySlotAmount`に達するまで`addNewInventorySlot`で空きスロットを追加する。 |
| `isInitializingInventory()` | 初期化中かどうかを示す`initializingInventory`の値を返すだけ。 |
| `isInventoryEmpty()` | `inventoryList`が空、または全要素の`amount`が0の時にtrueを返す。 |
| `isAnyInventoryWeaponEquipped()` | `isEquipped`かつ`isWeapon`の要素が1つでもあればtrueを返す。 |
| `addNewInventorySlot()` | 名前が"Empty Slot"で量0の空`inventoryInfo`を`inventoryList`の末尾に追加する。 |
| `checkEmptySlots()` | `amount`が0の要素をリスト末尾へ移動し、`updateFullInventorySlots`を呼んで満杯状態を更新する。 |
| `createInventoryIcons()` | 既存アイコンの`Button`オブジェクトを破棄したうえで、`inventoryList`の全要素について`createInventoryIcon`を呼び直す。 |
| `createInventoryIcon(inventoryInfo currentInventoryInfo, int index)` | `objectIcon`を`inventoryListContent`下に生成し、名前・アイコン・数量・単位量・耐久度を設定して`button`と`menuIconElement`を要素に登録する。 |
| `existInventoryInfoFromName(string objectName)` | 名前が存在するかの判定を`mainInventoryListManager.existInventoryInfoFromName`に委譲するだけ。 |
| `existInPlayerInventoryFromName(string objectName)` | プレイヤーの`inventoryList`内に同名の要素があればtrueを返す。 |
| `selectFirstObjectAvailableOfCategoryType(List<string> categoryList)` | 量が1以上でカテゴリ名が`categoryList`に含まれる最初の要素のボタンを押下扱いにし、無ければ`disableCurrentObjectInfo`を呼ぶ。 |
| `getInventoryInfoByName(string objectName)` | マスター側`mainInventoryListManager`から名前で`inventoryInfo`を取得して返す。 |
| `getInventoryInfoByIndex(int objectIndex)` | `objectIndex`が範囲外ならnull、そうでなければ`inventoryList`の該当要素を返す。 |
| `getRandomInventoryInfo()` | 量が1以上の要素をランダムに選んで返し、100回失敗すると先頭要素、範囲外ならnullを返す。 |
| `getPlayerInventoryInfoByName(string objectName)` | `inventoryList`を名前で検索し、見つかればその要素、無ければnullを返す。 |
| `setCustomAmountToUse(float customAmount)` | `customAmount`をintにキャストして`customAmountToUse`に代入するだけの設定メソッド。 |
| `tryToPickUpObjectByName(string objectName)` | マスターから名前で要素を取得し`amount`に`customAmountToUse`を設定して`tryToPickUpObject`を呼び、その後`customAmountToUse`を1に戻す。 |
| `tryToPickUpObjectByName(string objectName, int objectAmount)` | 名前から要素を取得して`objectAmount`を量に設定し拾得を実行、拾えた数を返す（見つからなければ-1）。 |
| `tryToPickUpObject(inventoryInfo inventoryObjectToPickup)` | 重量・最大所持数・スロット上限を見て個数を調整し空きへ追加、UI・イベント・武器自動装備を更新して拾得数を返す。 |
| `getLastInventoryObjectPickedName()` | 最後に拾得したオブジェクト名`lastInventoryObjectPickedName`を返すだけ。 |
| `getArmorClothPieceCategoryByName(string pieceName)` | マスターからプレハブを取得して`armorClothPickup.categoryName`を返し、取得できなければ空文字を返す。 |
| `addObjectToInventory(inventoryInfo objectToAdd, int amountToTake, int index)` | `index`が-1なら量0の最初の空きスロット、0以上ならそのスロットへマスター情報を複製して`amountToTake`と耐久度を設定し、アイコン表示を更新する。 |
| `updateFullInventorySlots()` | `menuIconElementList`と`inventoryList`を対応付け直して各アイコンの名前・画像・数量・装備・耐久度を更新し、`infiniteSlots`時は量0のスロットを削除する。 |
| `addInventoryExtraSpace(int amount)` | `inventorySlotAmount`に`amount`を加えて空きスロットを補充し、ボタン未生成のスロットにアイコンを作る（`infiniteSlots`時は何もしない）。 |
| `getPressedButton(Button buttonObj)` | 対応する要素を探し、既に選択中ならオプション表示と合成キャンセル、未選択なら`setObjectInfo`とカメラFOV調整・スロット選択イベントを行う。 |
| `setCurrenObjectByPrefab(GameObject objectToSearch, string inventoryObjectName)` | まず名前一致、次に`inventoryGameObject`一致で要素を探して`currentInventoryObject`に設定し、見つからなければnullにする。 |
| `setCurrenInventoryInfoByPickup(inventoryInfo newObject)` | `setCurrentInventoryObject`に処理を委譲するだけのラッパー。 |
| `setExternalCharacterForInventoryUsage(GameObject externalCharacterForInventoryUsage)` | 外部キャラクター参照を保持し、nullでない場合に`currentExternalCharacterForInventoryUsageAssigned`をtrueにする。 |
| `inventoryContainsObject(GameObject objectToCheck)` | `inventoryGameObject`が一致し`amount`が1以上の要素があればtrueを返す。 |
| `searchForObjectNeed(GameObject obj)` | `setCurrentUseInventoryGameObject`で使用対象を設定してから`useCurrentObject`を呼ぶ。 |
| `useInventoryObjectByNameExternally(string objectName)` | 操作不能・行動中でなければ`usableInventoryObjectInfoList`から同名の`amountToUse`を取得して`useInventoryObjectByName`を呼ぶ。 |
| `useInventoryObjectByName(string objectName, int amountToUse)` | 量が1以上で同名の要素を`currentInventoryObject`にし、`numberOfObjectsToUse`に`amountToUse`を設定して`useCurrentObject`を実行する。 |
| `setCurrentUseInventoryGameObject(GameObject obj)` | `currentUseInventoryGameObject`を設定し、その`useInventoryObject`コンポーネントをキャッシュする（nullならnull）。 |
| `removeCurrentInventoryObject()` | `currentInventoryObject`をnullにするだけのクリア処理。 |
| `removeCurrentUseInventoryObject()` | `currentUseInventoryObject`をnullにするだけのクリア処理。 |
| `useCurrentObjectByButton(RectTransform menuPosition)` | 対象の量が2以上なら数量指定メニューを`menuPosition`に表示し、再度押すとメニューを閉じて`useCurrentObject`を実行する。 |
| `checkCurrentUseInventoryObject()` | `currentUseInventoryObject`があればその`selectObjectOnInventory`を呼び出す。 |
| `setUsingCurrentObjectFromQuickAccessSlotsInventoryState(bool state)` | フラグ`usingCurrentObjectFromQuickAccessSlotsInventory`に`state`を代入するだけの設定メソッド。 |
| `useCurrentObject()` | 新挙動なら`useObjectOnNewBehavior`へ委譲し、通常は必要数を消費して音・UI・イベントを更新し、失敗時はメッセージを出す。 |
| `wasLastObjectWasUsedSuccessfully()` | 直前の使用が成功したかを示す`lastObjectWasUsedSuccessfully`を返すだけ。 |
| `setCustomMessageOnConditionFailedOnUseObjectWithNewBehavior(string newMessage, bool state)` | 失敗時カスタムメッセージの有効フラグと文言を代入するだけの設定メソッド。 |
| `setUseObjectWithNewBehaviorResult(int amountPicked)` | 新挙動の使用結果として`amountPicked`を減算し、数量表示・メッセージ・音・イベントを更新して0個なら失敗表示する。 |
| `isIgnoreMaximumObjectAmountActive()` | 最大所持数無視フラグ`ignoreMaximumObjectAmount`の値を返すだけ。 |
| `isCurrentObjectNotNull()` | `currentInventoryObject`とその`inventoryGameObject`がともにnullでない場合のみtrueを返す。 |
| `useEquippedObjectAction(string objectName, inventoryInfo objectInfoToUse)` | 参照一致、次に名前一致で要素を探して`currentInventoryObject`にし、`useObjectOnNewBehavior`を個数1で実行する。 |
| `checkLimitOnEquipWeapon()` | 装備数上限が有効で装備数が上限以上ならメッセージを表示してtrueを返し、それ以外はfalse。 |
| `equipCurrentObject()` | 現在の要素を武器なら`weaponsManager`/近接管理、それ以外は`inventoryObject`経由で装備し、`isEquipped`・アイコン・クイックアクセス枠・耐久度・装備イベントを更新する。 |
| `unEquipCurrentObject()` | 現在の装備を武器・近接・防具の各管理から解除し、`isEquipped`とアイコンを戻し、クイックアクセス枠を`updateQuickAccessSlotInfo(-1,…)`で空にして解除イベントを送る。 |
| `setCurrentInventoryObjectAndUnequipByName(string objectToUnequipName)` | 名前からプレイヤー在庫の要素を取得して`setCurrentInventoryObject`したうえで`unEquipCurrentObject`を呼ぶ。 |
| `unEquipObjectByName(string objectToUnequipName)` | 同名の装備中要素の装備フラグ・アイコン・クイックアクセス枠を解除してイベントを送る（武器側解除は呼ばない）。 |
| `equipObjectByName(string objectName)` | 未装備（`ignoreIfObjectEquippedActive`時は装備中も可）で装備可能かつ同名の要素を`currentInventoryObject`にして`equipCurrentObject`を呼ぶ。 |
| `equipObjectByNameWithoutCheckIfEquipped(string objectName)` | `ignoreIfObjectEquippedActive`をtrueにして`equipObjectByName`を呼び、直後にfalseへ戻す。 |
| `dropAllUnitsObjectAtOnce()` | 現在の要素の全数量を`numberOfObjectsToUse`に入れて`dropCurrentObject(true)`で一括ドロップする。 |
| `setOnQuickSlotsCurrentObjectDirectly()` | 現在の要素を`setOnQuickSlotsCurrentObjectDirectly(…, -1)`で直接クイックアクセス枠へ割り当て、スロットオプションを閉じる。 |
| `discardCurrentObject()` | 現在の要素の全数量を`numberOfObjectsToUse`に入れ、プレハブを生成しない`dropCurrentObject(false)`で破棄する。 |
| `dropCurrentObject(RectTransform menuPosition)` | 数量指定メニューが有効なら`menuPosition`に表示し、再押下時にメニューを閉じて`dropCurrentObject(true)`を実行する。 |
| `dropCurrentObject(bool instantiateInventoryObjectPrefab)` | `numberOfObjectsToUse`分を在庫から減らしてプレハブを生成または破棄し、同一スタックの結合・装備解除・UIとイベント更新まで行う。 |
| `checkObjectDroppedEvent(GameObject currentObjectDropped)` | ドロップされたオブジェクトの`inventoryObject`を取得し、`eventOnDropObjectNewBehaviour`を呼ぶ。 |
| `dropObject(GameObject currentInventoryObjectPrefab, Vector3 positionToInstantiate, int amount)` | プレハブを指定位置に生成して拾得用の数量・単位量・耐久度を設定し、ドロップイベントを送る（`inventoryObject`が無ければRigidbodyを付与）。 |
| `dropObjectByName(string equipName, int amount, bool instantiateInventoryObjectPrefab, bool dropOnlyObjectMesh, bool avoidDropIfEquipped)` | ドロップ可能で同名の要素を探し、装備中なら`avoidDropIfEquipped`次第で除外しつつ、メッシュのみ設定と数量を入れて`dropCurrentObject`を呼ぶ。 |
| `dropEquipByName(string equipName, int amount, bool instantiateInventoryObjectPrefab, bool dropOnlyObjectMesh)` | 装備中で同名の要素を`currentInventoryObject`にし、`dropOnlyObjectMeshActive`と数量を設定して`dropCurrentObject`でドロップする。 |
| `dropEquipByIndex(int objectIndex, int amount, bool instantiateInventoryObjectPrefab, bool dropOnlyObjectMesh)` | `objectIndex`が範囲外なら中断し、装備中ならその要素を対象に、メッシュ限定フラグと数量を設定してドロップする。 |
| `carryPhysicalObjectFromInventory()` | 在庫から1個または全量をドロップしてインベントリを閉じ、生成物の`carryPhysicalObjectFromInventory`で実際に掴ませる。 |
| `isSendGrabbedObjectToInventoryIfGrabbingNewOneEnabled()` | フラグ`sendGrabbedObjectToInventoryIfGrabbingNewOne`の値を返すだけ。 |
| `getLastObjectDropped()` | 直近に生成したドロップ品`lastObjectDropped`を返すだけ。 |
| `dropAllInventory()` | 再生中のみ、`inventoryList`を末尾から順に全数量を`dropCurrentObject(true)`で地面にドロップする。 |
| `removeAllInventoryWithoutDrops()` | 再生中のみ、全要素を`dropCurrentObject(false)`で処理してプレハブを生成せず在庫だけ空にする。 |
| `disableObjectsToCombineIcon()` | 合成対象の`firstObjectToCombine`と`secondObjectToCombine`の合成アイコン表示を消す。 |
| `setCombineIcontPressedState(bool state, inventoryInfo inventoryObjectToCombine)` | 指定要素の`menuIconElement.combineIcon`の表示を`state`に合わせるだけ。 |
| `setCombiningObjectsState(bool state)` | 現在の要素が合成可能なら`combiningObjects`と合成アイコンを`state`にし、スロットオプションを閉じる。 |
| `combineCurrentObject()` | 2つの合成対象の組み合わせと空きを確認し、各1個を消費して結果を在庫へ加え、新挙動時は委譲してイベントを送る。 |
| `setCombineObjectsWithNewBehaviorResult(int amountPicked, bool combinedSuccessfully)` | 新挙動合成の結果を受け、`-OBJECT-`/`-AMOUNT-`を置換したメッセージ表示と合成元の数量減算・ボタン削除・イベント送信を行い、対象参照をクリアする。 |
| `getCurrentInventoryObjectInfo()` | `currentInventoryObject`をそのまま返すだけの取得メソッド。 |
| `getCurrentFirstObjectToCombine()` | 合成対象1つ目`firstObjectToCombine`を返すだけ。 |
| `getCurrentSecondObjectToCombine()` | 合成対象2つ目`secondObjectToCombine`を返すだけ。 |
| `setCurrentPickupObject(pickUpObject newPickupObject)` | `currentPickupObject`に`newPickupObject`を代入するだけの設定メソッド。 |
| `setCurrentPickupGameObject(GameObject newObject)` | `currentPickupGameObject`に`newObject`を代入するだけの設定メソッド。 |
| `setObjectInfo(inventoryInfo currentInventoryObjectInfo)` | 対象を選択状態にして名前・説明を表示し、使用/装備/ドロップ等ボタンの可否色を設定し、カメラ前にメッシュを生成する。 |
| `getInventoryPrefab(GameObject inventoryGameObject)` | `mainInventoryListManager.getInventoryPrefab`に委譲して対応プレハブを返すだけ。 |
| `getInventoryObjectComponentByInventoryGameObject(GameObject inventoryGameObjectToSearch)` | `mainInventoryListManager`の同名メソッドに委譲して`inventoryObject`を取得するだけ。 |
| `getInventoryPrefabByName(string objectName)` | `mainInventoryListManager`から名前でプレハブを取得して返すだけ。 |
| `getInventoryMeshByName(string objectName)` | `mainInventoryListManager`から名前でメッシュを取得して返すだけ。 |
| `isInventoryFull()` | `infiniteSlots`/`infiniteAmountPerSlot`ならfalse、それ以外は全スロットが上限に達している場合のみtrueを返す。 |
| `getNumberOfFreeSlots()` | `infiniteSlots`なら1を返し、それ以外は`amount`が0のスロット数を数えて返す。 |
| `getRealAmountOfFreeSlots()` | `amount`が0のスロット数を数えて返す（`infiniteSlots`の特別扱いをしない版）。 |
| `freeSpaceInSlot(GameObject inventoryObjectMesh)` | 同名メッシュの要素についてスロット上限から現在量を引いた空き数を返し、該当が無ければ-1を返す。 |
| `getAmountPerSlotFromInventoryObject(GameObject inventoryObjectMesh)` | 該当メッシュのスロット上限（個別設定があればそれ）を返し、見つからなければ既定の`amountPerSlot`を返す。 |
| `checkIfObjectCanBeStored(GameObject inventoryObjectMesh, int amountToStore)` | 空きスロット数と同一オブジェクトの残容量から`amountToStore`が収まるかを判定する（`infiniteSlots`は常にtrue）。 |
| `addAmountToInventorySlot(inventoryInfo objectInfo, int currentSlotAmount, int extraAmount)` | 同じメッシュで量が`currentSlotAmount`（または無限）のスロットに`extraAmount`を加えて表示更新し、無ければ`addObjectToInventory`で新規追加する。 |
| `getTimeTime()` | ポーズ管理が通常タイムスケールなら`Time.time`、そうでなければ`Time.unscaledTime`を返す。 |
| `getDeltaTime()` | ポーズ管理が通常タイムスケールなら`Time.deltaTime`、そうでなければ`Time.unscaledDeltaTime`を返す。 |
| `addObjectSingleUnitToInventoryByName(string objectName)` | `addObjectAmountToInventoryByName`を数量1で呼ぶだけのラッパー。 |
| `addObjectAmountToInventoryByName(string objectName, int amountToMove)` | マスターから名前で要素を複製して`amount`を`amountToMove`にし、`tryToPickUpObject`で在庫へ追加する。 |
| `removeAllObjectAmountFromInventoryByName(string objectName)` | 同名の全スロットを末尾から走査し、それぞれの全量を`removeObjectAmountFromInventory`で取り除く。 |
| `removeObjectAmountFromInventoryByName(string objectName, int amountToMove)` | 最初に見つかった同名スロットから`amountToMove`を`removeObjectAmountFromInventory`で減らす。 |
| `sellObjectOnVendorSystem(int objectToMoveIndex, int amountToMove)` | ベンダー売却用に`removeObjectAmountFromInventory`で在庫を減らし、弾薬表示と全クイックアクセス枠の数量を更新する。 |
| `removeObjectAmountFromInventory(int objectToMoveIndex, int amountToMove)` | 指定スロットから`amountToMove`を減らし、不足時は同名の他スロットから補充、0になれば装備解除とボタン削除、在庫再構築とUI更新を行う。 |
| `addOrRemoveDurabilityAmountToObjectByName(string objectName, int inventoryObjectIndex, float newAmount, bool setAmountAsCurrentValue)` | 指定インデックスの耐久度を`newAmount`で設定または加算し、0以下なら破壊・ドロップ等を適用して表示を更新する（-1は無効）。 |
| `getDurabilityValueOnObjectByName(string objectName)` | 耐久度機能が無効なら-1を返し、該当要素が耐久度を使う場合のみ`durabilityAmount`を返す。 |
| `getMaxDurabilityValueOnObjectByName(string objectName)` | 耐久度機能が無効なら-1を返し、それ以外は`mainInventoryListManager`から最大耐久度を取得して返す。 |
| `updateUIAfterRepairingCurrentObjectSelectedOnInventoryMenu(bool state)` | 修理後に現在の要素の耐久度表示を更新し、成功時は`eventOnRepairCurrentObject`、失敗時は`eventOnUnableToRepairCurrentObject`を発火する。 |
| `repairDurabilityObjectByIndex(int objectIndex)` | 指定要素が耐久度を使う武器・近接・防具・盾なら各マネージャーの`repairObjectFully`系を呼んでtrueを返し、対象外ならfalse。 |
| `isObjectBroken(int objectIndex)` | 指定要素が耐久度を使う場合に`objectIsBroken`を返し、それ以外や-1ならfalseを返す。 |
| `isObjectDurabilityComplete(int objectIndex)` | 指定要素の耐久度が最大未満ならfalse、耐久度を使わない要素や-1ならtrueを返す。 |
| `setCurrentInventoryObject(inventoryInfo newObject)` | `currentInventoryObject`に`newObject`を代入するだけの設定メソッド。 |
| `getCurrentInventoryObjectIndex()` | `currentInventoryObject`がnullなら-1、そうでなければ`inventoryList`内の位置を返す。 |
| `getInventoryObjectIndexByInventoryInfo(inventoryInfo currentObject)` | `currentObject`がnullなら-1、そうでなければ`inventoryList`内のインデックスを返す。 |
| `getInventoryObjectIndexByName(string inventoryObjectName)` | 同名の先頭要素のインデックスを返し、見つからなければ-1を返す。 |
| `getInventoryObjectAmountByName(string inventoryObjectName)` | 同名要素の`amount`を合計して返し、合計が0以下なら-1を返す。 |
| `getNumberOfWeaponsEquipped()` | 初期化中は保持値を返し、それ以外は`isWeapon`かつ`isEquipped`の要素を数え直してその数を返す。 |
| `getInventoryObjectIconByName(string inventoryObjectName)` | `mainInventoryListManager.getInventoryObjectIconByName`に委譲してアイコン`Texture`を返すだけ。 |
| `getInventoryObjectAmountPerUnitByName(string inventoryObjectName)` | `mainInventoryListManager`から名前で単位あたりの数量を取得して返すだけ。 |
| `checkIfInventoryObjectEquipped(string inventoryObjectName)` | 同名の要素が装備中ならtrueを返す。 |
| `setUsedByAIState(bool state)` | フラグ`usedByAI`に`state`を代入するだけの設定メソッド。 |
| `setInventoryEnabledState(bool state)` | フラグ`inventoryEnabled`に`state`を代入するだけの設定メソッド。 |
| `canUseInput()` | 近接攻撃処理中ならfalse、それ以外はtrueを返す。 |
| `playerIsBusy()` | デバイス使用中・移動不可・サブメニューやプレイヤーメニュー表示中ならtrueを返す（ターン制戦闘中はfalse）。 |
| `isGamePaused()` | `pauseManager.isGamePaused`の結果を返すだけの委譲メソッド。 |
| `isUsingGenericModelActive()` | `playerControllerManager.isUsingGenericModelActive`の結果を返すだけの委譲メソッド。 |
| `isFirstPersonActive()` | `playerControllerManager.isPlayerOnFirstPerson`の結果を返すだけの委譲メソッド。 |
| `setPausePlayerRotateToCameraDirectionOnFirstPersonActiveState(bool state)` | プレイヤーコントローラーの同名メソッドへ`state`を渡すだけの委譲メソッド。 |
| `setAnimatorState(bool state)` | `playerControllerManager.setAnimatorState`へ`state`を渡すだけの委譲メソッド。 |
| `examineCurrentPickupObject(inventoryInfo inventoryObjectToPickup)` | インベントリを開いて対象を複製・選択し、調べパネルを有効化して取得ボタンとカメラFOV、名前＋数量表示を設定する。 |
| `confirmToPickCurrentObjectInExaminingPanel()` | 調べパネルから`pickObjectByButton`で取得を実行し、調べ表示を終了して必要ならプレイヤーメニューを閉じる。 |
| `examineCurrentObject(bool state)` | 調べパネルの表示を切り替え、名前・説明・カメラ配置とFOV・プレイヤーメニューを設定し、終了時は移動を止めて対象参照をクリアする。 |
| `playerIsExaminingInventoryObject()` | 調べ表示中かどうかを示す`examiningObject`を返すだけ。 |
| `setNewInventoryList(List<inventoryInfo> newInventoryList)` | 受け取ったリストの各要素を複製して`inventoryList`へ上書きし、空きスロット整理と全アイコン更新を行う。 |
| `moveObjectToBank(int objectToMoveIndex, int amountToMove)` | `removeObjectAmountFromInventory`で在庫から移動分を減らし、弾薬表示と全クイックアクセス枠の数量を更新する。 |
| `setCurrentInventoryBankSystem(GameObject inventoryBankGameObject)` | `mainInventoryBankUISystem.setCurrentInventoryBankSystem`へ渡すだけの委譲メソッド。 |
| `setCurrentVendorSystem(GameObject inventoryBankGameObject)` | `mainVendorUISystem.setCurrentInventoryBankSystem`へ渡すだけの委譲メソッド。 |
| `setCurrentInventoryBankObject(GameObject inventoryBankGameObject)` | `mainInventoryBankUISystem.setCurrentInventoryBankObject`へ渡すだけの委譲メソッド。 |
| `setCurrentVendorObject(GameObject inventoryBankGameObject)` | `mainVendorUISystem.setCurrentInventoryBankObject`へ渡すだけの委譲メソッド。 |
| `openOrCloseInventoryBankMenu(bool state)` | `mainInventoryBankUISystem.openOrCloseInventoryBankMenu`へ`state`を渡すだけの委譲メソッド。 |
| `instantiateMainInventoryManagerPrefab()` | `mainInventoryListManager`が未設定ならシングルトン取得・シーン検索・プレハブ生成の順で探索して参照を確保し、既にあればメッセージを出す。 |
| `selectMainInventoryManagerOnScene()` | マスターが未設定なら生成を試み、取得できた場合にエディタ上でそのGameObjectを選択状態にする。 |
| `inputConfirmToPickCurrentObjectInExaminingPanel()` | 調べ表示中かつ拾得対象がある時に取得確定を実行し、デバイス使用ボタンの再入力を0.5秒抑止する。 |
| `inputOpenOrCloseInventory()` | メニュー開閉がポーズ中でなく、インベントリと開閉が有効な場合に`inventoryOpened`を反転して開閉する。 |
| `inputSetZoomInState(bool state)` | インベントリが有効かつ開いている時のみ、`state`に応じて`zoomInEnabled`/`zoomInDisabled`を呼ぶ。 |
| `inputSetZoomOutState(bool state)` | インベントリが有効かつ開いている時のみ、`state`に応じて`zoomOutEnabled`/`zoomOutDisabled`を呼ぶ。 |
| `useAmmoFromInventory(string weaponName, int amountToUse)` | 弾薬名で`removeObjectAmountFromInventoryByName`を呼び、スロット分割をまたいで`amountToUse`分を消費する。 |
| `checkIfWeaponUseAmmoFromInventory()` | `storePickedWeaponsOnInventory`時に、在庫弾薬を使う射撃武器へ在庫内の同名弾薬総数を残弾として設定する。 |
| `setActivatingDualWeaponSlotState(bool state)` | フラグ`activatingDualWeaponSlot`に`state`を代入するだけの設定メソッド。 |
| `setCurrentRighWeaponNameValue(string newValue)` | `currentRighWeaponName`に`newValue`を代入するだけの設定メソッド。 |
| `setCurrentLeftWeaponNameValue(string newValue)` | `currentLeftWeaponName`に`newValue`を代入するだけの設定メソッド。 |
| `adjustCameraFovToSeeInventoryObject()` | 対象が`useZoomRange`なら`initialZoom`、そうでなければ既定FOVを目標に`checkResetCameraFov`でカメラFOVを調整する。 |
| `disableCurrentObjectInfo()` | 名前・説明・各操作ボタンの色や表示を初期状態に戻し、オブジェクト画像を非表示にしてスロットオプションも閉じる。 |
| `checkInventoryOptionsOnSlot(bool state)` | スロットオプションパネルを`state`にし、使用・装備・ドロップ・合成・調べなどの可否を`setButtonsState`へ渡して表示位置を合わせる。 |
| `setInventoryOptionsOnSlotPanelActiveState(bool state)` | `inventoryOptionsOnSlotPanel`のGameObject表示を`state`に合わせるだけ。 |
| `setEquipButtonState(bool state)` | `state`がtrueなら装備ボタンを有効・解除ボタンを非表示、falseなら解除ボタンを有効・装備ボタンを非表示に切り替える。 |
| `setAllAmountObjectToUse()` | `numberOfObjectsToUse`に現在の要素の全数量を入れ、その数値をUIテキストへ反映する。 |
| `addObjectToUse()` | `numberOfObjectsToUse`を1増やし、現在の所持数を上限としてクランプしてUIテキストを更新する。 |
| `removeObjectToUse()` | `numberOfObjectsToUse`を1減らし、1未満にならないようクランプしてUIテキストを更新する。 |
| `startToAddObjectToUse()` | `addingObjectToUse`をtrueにし、数量増加の基準時刻`lastTimeConfigureNumberOfObjects`を現在時刻に設定する。 |
| `stopToAddObjectToUse()` | `addingObjectToUse`をfalseにし、時刻と高速増加フラグ`useFasterNumberObjectsToUseRateActive`をリセットする。 |
| `startToRemoveObjectToUse()` | `removinvObjectToUse`をtrueにし、数量減少の基準時刻`lastTimeConfigureNumberOfObjects`を現在時刻に設定する。 |
| `stopToRemoveObjectToUse()` | `removinvObjectToUse`をfalseにし、時刻と高速増加フラグ`useFasterNumberObjectsToUseRateActive`をリセットする。 |
| `setNumberOfObjectsToUseText(int amount)` | `numberOfObjectsToUseText`に`amount`の文字列を表示するだけ。 |
| `enableNumberOfObjectsToUseMenu(RectTransform menuPosition)` | 数量指定メニューが有効で対象が使用/ドロップ可能なら、指定位置にメニューを表示し数量を1に初期化する。 |
| `disableNumberOfObjectsToUseMenu()` | `numberOfObjectsToUse`を1に戻し、数量指定メニューを非表示にする。 |
| `resetNumberOfObjectsToUse()` | `numberOfObjectsToUse`を1に戻してUIテキストも更新するだけ。 |
| `resetAndDisableNumberOfObjectsToUseMenu()` | `disableNumberOfObjectsToUseMenu`と`resetNumberOfObjectsToUse`を順に呼ぶだけのラッパー。 |
| `playSound(AudioElement newClip)` | `useAudioSounds`が有効なら`AudioPlayer.PlayOneShot`で`newClip`を再生する。 |
| `setCustomObjectNotFoundMessage(bool state, string newMessage)` | 見つからない時のカスタム文言と有効フラグを代入するだけの設定メソッド。 |
| `showObjectMessage(string message, float messageDuration, GameObject messagePanel)` | 空文字でなければ既存のコルーチンを止め、指定パネルに`messageDuration`秒だけメッセージを表示するコルーチンを開始する。 |
| `showObjectMessage(string message, float messageDuration)` | `usedObjectMessage`パネルを指定して3引数版の`showObjectMessage`を呼ぶだけ。 |
| `enableOrDisableHUD(bool state)` | `mainInventoryQuickAccessSlotsSystem.enableOrDisableHUD`へ`state`を渡すだけの委譲メソッド。 |
| `enableOrDisableWeaponSlotsParentOutOfInventory(bool state)` | クイックアクセススロット親の表示を`enableOrDisableQuickAccessSlotsParentOutOfInventory`へ委譲して切り替える。 |
| `checkToEnableOrDisableWeaponSlotsParentOutOfInventory(bool state)` | クイックアクセススロット親の表示判定をクイックアクセス管理の同名メソッドへ委譲する。 |
| `checkToEnableOrDisableQuickAccessSlotsParentOutOfInventoryFromFireWeaponsMode(bool state)` | 射撃武器モード時のクイックアクセス親表示判定を管理側の同名メソッドへ委譲する。 |
| `checkToEnableOrDisableQuickAccessSlotsParentOutOfInventoryFromMeleeWeaponsMode(bool state)` | 近接武器モード時のクイックアクセス親表示判定を管理側の同名メソッドへ委譲する。 |
| `setShowWeaponSlotsPausedState(bool state)` | `mainInventoryQuickAccessSlotsSystem.setShowQuickAccessSlotsPausedState`へ`state`を渡すだけの委譲メソッド。 |
| `updateAmountsInventoryPanel()` | `inventoryList`の全要素について`updateAmount`を呼び、数量表示を一括更新する。 |
| `updateAmount(inventoryInfo inventoryInfoToUpdate, int amount)` | 指定要素のアイコンに`amount`（単位量設定時は積算値）や無限アイコンを反映し、耐久度表示も更新する。 |
| `breakFullDurabilityOnCurrentWeapon()` | 耐久度機能が有効なら、射撃武器モードと近接武器モードそれぞれの`breakFullDurabilityOnCurrentWeapon`を呼んで耐久度を0にする。 |
| `removeButton(inventoryInfo currentObj)` | 対象スロットを空表示に戻して`resetInventoryInfo`し、カメラ上のメッシュ削除・選択解除イベント・現在参照のクリアを行う。 |
| `setMenuIconElementPressedState(bool state)` | 現在の要素のアイコン`pressedIcon`の表示を`state`に合わせるだけ。 |
| `enableObjectRotation()` | カメラ前のオブジェクト`objectInCamera`が存在する場合のみ`enableRotation`をtrueにする。 |
| `disableObjectRotation()` | フラグ`enableRotation`をfalseにするだけの設定メソッド。 |
| `destroyObjectInCamera()` | `objectInCamera`がnullでなければ`Destroy`で削除する。 |
| `placeObjectInCameraPosition()` | 既存の移動コルーチンを止め、`placeObjectInCameraPositionCoroutine`を開始してオブジェクトをカメラ位置へ移動させる。 |
| `stopObjectInCameraPositionMovevement()` | `objectInCameraPositionCoroutine`がnullでなければ停止する。 |
| `placeObjectInCameraRotation()` | 既存の回転コルーチンを止め、`placeObjectInCameraRotationCoroutine`を開始して回転を合わせる。 |
| `stopObjectInCameraRotationMovevement()` | `objectInCameraRotationCoroutine`がnullでなければ停止する。 |
| `setInventoryPanelByName(string panelInfo)` | `mainInventoryMenuPanelsSystem.setInventoryPanelByName`へ`panelInfo`を渡すだけの委譲メソッド。 |
| `showMaxObjectAmountReachedMessage(string objectName)` | 最大所持数メッセージ内の`-OBJECT-`を`objectName`で置換し、所定時間メッセージを表示する。 |
| `showInventoryFullMessage()` | 既存のコルーチンを止めて`showInventoryFullMessageCoroutine`を開始し、インベントリ満杯メッセージを表示する。 |
| `zoomInEnabled()` | フラグ`zoomingIn`をtrueにするだけの設定メソッド。 |
| `zoomInDisabled()` | フラグ`zoomingIn`をfalseにするだけの設定メソッド。 |
| `zoomOutEnabled()` | フラグ`zoomingOut`をtrueにするだけの設定メソッド。 |
| `zoomOutDisabled()` | フラグ`zoomingOut`をfalseにするだけの設定メソッド。 |
| `checkResetCameraFov(float targetValue)` | 進行中のFOV変更コルーチンを止め、`resetCameraFovCorutine`を`targetValue`で開始する。 |
| `isInventoryMenuOpened()` | インベントリが開いているかを示す`inventoryOpened`を返すだけ。 |
| `resetScroll(Scrollbar scrollBarToReset)` | `resetScrollCoroutine`を開始して指定スクロールバーの位置をリセットする。 |
| `resetInventorySlotsRectTransform()` | `resetRectTransformCoroutine`を開始してインベントリスロットのRectTransformを初期化する。 |
| `enableOrDisableInventoryMenu(bool state)` | `inventoryPanel`のGameObject表示を`state`に合わせるだけ。 |
| `openOrClosePlayerMenuFromUseInventoryObject(bool state)` | `inventoryOpened`を更新してポーズメニューとパネル表示・メニュー名の状態を`state`に合わせ、開閉後処理を呼ぶ。 |
| `openOrCloseInventory(bool state)` | メニュー使用可否とプレイヤー状態を確認したうえで`inventoryOpened`を変更し、ポーズメニュー・パネル表示を切り替えて開閉後処理を実行する。 |
| `setOpenOrCloseInventoryMenuState()` | 開閉状態に応じてアイコン・調べパネル・カメラ・クイックアクセス枠を初期化し、開いた時は先頭を選択して開閉イベントを送る。 |
| `openOrCLoseInventoryFromTouch()` | `inventoryOpened`を反転して`openOrCloseInventory`を呼ぶだけのタッチ入力用ラッパー。 |
| `resetDragAndDropWeaponSlotState()` | クイックアクセス管理の`resetDragAndDropSlotState`へ委譲してドラッグ状態を戻すだけ。 |
| `updateSingleWeaponSlotInfo(string newRighWeaponName, string newLeftWeaponName)` | クイックアクセス管理の同名メソッドへ左右の武器名を渡すだけの委譲メソッド。 |
| `updateSingleWeaponSlotInfoWithoutAddingAnotherSlot(string newRighWeaponName)` | スロットを追加せずに右手武器名を更新する処理をクイックアクセス管理へ委譲する。 |
| `updateDualWeaponSlotInfo(string newRighWeaponName, string newLeftWeaponName)` | 二丁持ちスロット情報の更新をクイックアクセス管理の同名メソッドへ委譲する。 |
| `updateQuickAccessSlotInfo(int slotIndex, inventoryInfo currentSlotToMove, inventoryQuickAccessSlotElement.quickAccessSlotInfo slotToUnEquip, playerWeaponSystem secondaryWeaponToEquip)` | スロット番号・移動する要素・解除するスロット・副武器を渡してクイックアクセス枠の更新を委譲する。 |
| `updateQuickAccesSlotAmount(int weaponSlotIndex)` | 指定スロットの数量表示更新をクイックアクセス管理へ委譲するだけ。 |
| `updateAllQuickAccessSlotsAmount()` | 全クイックアクセス枠の数量更新をクイックアクセス管理へ委譲するだけ。 |
| `updateAllWeaponSlotAmmo()` | `updateAllQuickAccessSlotsAmount`を呼び、全スロットの弾薬表示を更新する。 |
| `getFirstSingleWeaponSlot(string weaponNameToAvoid)` | クイックアクセス管理から、指定名を避けた最初の単一武器スロット名を取得して返す。 |
| `showWeaponSlotsParentWhenWeaponSelectedByName(string objectName)` | 名前指定でスロット選択時の親表示処理をクイックアクセス管理へ委譲する。 |
| `showWeaponSlotsParentWhenWeaponSelected(int weaponSlotIndex)` | スロット番号指定で親表示処理をクイックアクセス管理へ委譲する。 |
| `stopShowWeaponSlotsParentWhenWeaponSelectedCoroutuine()` | スロット選択時の表示コルーチン停止をクイックアクセス管理へ委譲する。 |
| `isShowWeaponSlotsAlwaysActive()` | クイックアクセス枠を常時表示する設定かをクイックアクセス管理に問い合わせて返す。 |
| `updateWeaponCurrentlySelectedIcon(int weaponSlotIndex, bool activeCurrentWeaponSlot)` | 指定スロットの選択中アイコン表示の更新をクイックアクセス管理へ委譲する。 |
| `disableCurrentlySelectedIcon()` | 選択中アイコンの無効化をクイックアクセス管理へ委譲するだけ。 |
| `selectWeaponByPressingSlotWeapon(GameObject buttonToCheck)` | スロットのボタン押下による武器選択をクイックアクセス管理の`selectQuickAccessSlotByPressingSlot`へ委譲する。 |
| `moveWeaponSlotsOutOfInventory()` | クイックアクセス枠をインベントリ外へ移動する処理をクイックアクセス管理へ委譲する。 |
| `moveWeaponSlotsToInventory()` | クイックアクセス枠をインベントリ内へ移動する処理をクイックアクセス管理へ委譲する。 |
| `setWeaponSlotsBackgroundColorAlphaValue(float newAlphaValue)` | クイックアクセス枠の背景色アルファ値を`newAlphaValue`に設定する処理を委譲する。 |
| `changeToMeleeWeapons(string meleeWeaponName)` | 近接武器モードへの切り替えをクイックアクセス管理の`changeToMeleeWeapons`へ委譲する。 |
| `checkQuickAccessSlotToSelectByName(string objectOnSlotName)` | 指定名のオブジェクトが入ったクイックアクセス枠の選択判定を管理側へ委譲する。 |
| `selectCurrentSlotWeaponIfAvailable()` | 現在スロットの武器を選択できるか試み、その結果をクイックアクセス管理から受け取って返す。 |
| `selectFirstGeneralWeaponAvailable()` | 利用可能な最初の汎用武器を選択する処理をクイックアクセス管理へ委譲する。 |
| `checkEventOnSystemDisabled()` | `useEventIfSystemDisabled`が有効なら`eventIfSystemDisabled`を発火する。 |
| `checkEventOnInventoryInitialized()` | `eventOnInventoryInitialized`を無条件に発火するだけ。 |
| `checkEventOnClickInventoryChange()` | `eventOnClickInventoryChange`を無条件に発火するだけ。 |
| `checkEventOnInventorySlotSelected()` | `eventOnInventorySlotSelected`を無条件に発火するだけ。 |
| `checkEventOnInventorySlotUnSelected()` | `eventOnInventorySlotUnSelected`を無条件に発火するだけ。 |
| `checkEventOnInventoryClosed()` | `eventOnInventoryClosed`を無条件に発火するだけ。 |
| `checkEventOnInventoryOpened()` | `eventOnInventoryOpened`を無条件に発火するだけ。 |
| `checkEventOnInventoryListChange()` | `eventOnInventoryListChange`を無条件に発火するだけ。 |
| `setEquipWeaponsWhenPickedPausedState(bool state)` | フラグ`equipWeaponsWhenPickedPaused`に`state`を代入するだけの設定メソッド。 |
| `setOpenInventoryMenuEnabled(bool state)` | フラグ`openInventoryMenuEnabled`に`state`を代入するだけの設定メソッド。 |
| `addNewInventoryObjectToInventoryListManagerList()` | 名前"New Object"・数量1の`inventoryListElement`を初期リストへ追加し、`updateComponent`で反映する。 |
| `clearInitialInventoryListOnEditor()` | 初期インベントリリスト`inventoryListManagerList`を空にし、`updateComponent`で反映する。 |
| `addNewInventoryObject()` | 空の`inventoryInfo`を`inventoryList`へ追加し、`updateComponent`で反映する（エディタ用）。 |
| `getInventoryListManagerList()` | マスターのカテゴリ名と各カテゴリ内オブジェクト名を文字列配列へ展開して保持し、`updateComponent`で反映する。 |
| `setInventoryObjectListNames()` | 初期リスト各要素の`Name`を`inventoryObjectName`で上書きし、`updateComponent`で反映する。 |
| `saveCurrentInventoryListToFileFromEditor()` | `pauseManager.saveGameInfoFromEditor("Player Inventory")`で在庫を保存し、メッセージ表示と`updateComponent`を行う。 |
| `setAddAllObjectEnabledState(bool state)` | 初期リスト全要素の`addInventoryObject`を`state`にそろえ、`updateComponent`で反映する。 |
| `setEquipAllObjectEnabledState(bool state)` | 初期リスト全要素の`isEquipped`を`state`にそろえ、`updateComponent`で反映する。 |
| `removeAllWeaponsFromInitialInventoryList()` | マスターを確認しつつ初期リストを末尾から走査し、`isWeapon`がtrueの要素を削除して`updateComponent`で反映する。 |
| `removeAllObjectsFromInitialInventoryList()` | 初期インベントリリストを空にして`updateComponent`で反映するだけ。 |
| `setAddObjectEnabledState(int objectIndex)` | 指定要素の`addInventoryObject`を反転し、`updateComponent`で反映する。 |
| `setEquippedObjectState(int objectIndex, bool state)` | 指定要素の`isEquipped`を`state`にして`updateComponent`で反映する。 |
| `setEquippedObjectState(int objectIndex)` | 指定要素の`isEquipped`を反転し、`updateComponent`で反映する。 |
| `setDestroyObjectsOnEmptyDurabilityValueFromEditor(bool state)` | `destroyObjectsOnEmptyDurability`を`state`にして`updateComponent`で反映する（エディタ用）。 |
| `setCheckDurabilityOnObjectEnabledValueFromEditor(bool state)` | `checkDurabilityOnObjectEnabled`を`state`にして`updateComponent`で反映する（エディタ用）。 |
| `setSetObjectsAsBrokenOnEmptyDurabilityValueFromEditor(bool state)` | `setObjectsAsBrokenOnEmptyDurability`を`state`にして`updateComponent`で反映する（エディタ用）。 |
| `setOpenInventoryMenuEnabledFromEditor(bool state)` | `setOpenInventoryMenuEnabled`を呼んだうえで`updateComponent`で反映する（エディタ用）。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`でこのコンポーネントとシーンをダーティ更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnInventoryInitialized` | `UnityEvent` | – |
| `eventOnClickInventoryChange` | `UnityEvent` | – |
| `eventOnInventorySlotSelected` | `UnityEvent` | – |
| `eventOnInventorySlotUnSelected` | `UnityEvent` | – |
| `eventOnInventoryClosed` | `UnityEvent` | – |
| `eventOnInventoryOpened` | `UnityEvent` | – |
| `eventOnInventoryListChange` | `UnityEvent` | – |
| `eventIfSystemDisabled` | `UnityEvent` | – |
| `eventOnRepairCurrentObject` | `UnityEvent` | – |
| `eventOnUnableToRepairCurrentObject` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`InitializeAudioElements()`, `getCurrentInventoryListManagerList()`, `getInventoryList()`, `getInventorySlotAmount()`, `initializeInventoryValues()`, `isInfiniteSlotsActive()`, `isLoadCurrentPlayerInventoryFromSaveFileActive()`, `isSaveCurrentPlayerInventoryToSaveFileActive()`, `setInfiniteSlotsState(bool state)`, `setInventorySlotAmountValue(int newValue)`, `setNewInventoryListManagerList(List<inventoryListElement> newList)`, `updateDurabilityAmountStateOnAllInventoryObjects()`

</details>

## 内部型

- `inventoryManagerStringInfo`（class）
- `usableInventoryObjectInfo`（class）
