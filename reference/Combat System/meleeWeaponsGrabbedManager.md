# meleeWeaponsGrabbedManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/meleeWeaponsGrabbedManager.cs:6`

**概要**: 近接武器の所持リストと盾を管理する中核コンポーネントで、武器の装備/納刀、体へのメッシュ表示、インベントリ・クイックアクセス連携、耐久値、IK、武器抽選や入力処理をまとめて扱う。実際の攻撃やアニメーションは`grabbedObjectMeleeAttackSystem`へ委譲する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Melee Weapons Grabbed Manager Enabled | `meleeWeaponsGrabbedManagerEnabled` | `bool` | true | – |
| Store Each Grabbed Weapon | `storeEachGrabbedWeapon` | `bool` | – | – |
| Store Only One Weapon | `storeOnlyOneWeapon` | `bool` | – | – |
| Can Spawn Any Weapon Stored Infinite Times | `canSpawnAnyWeaponStoredInfiniteTimes` | `bool` | – | – |
| Store Picked Weapons On Inventory | `storePickedWeaponsOnInventory` | `bool` | – | – |
| Draw Weapon At Start If Found On Initializing Inventory | `drawWeaponAtStartIfFoundOnInitializingInventory` | `bool` | – | – |
| Number Keys To Change Between Melee Weapons Enabled | `numberKeysToChangeBetweenMeleeWeaponsEnabled` | `bool` | true | – |
| Drop Thrown Weapon If Changing To Another Weapon Enabled | `dropThrownWeaponIfChangingToAnotherWeaponEnabled` | `bool` | – | – |
| Drop Thrown Weapon When Using Device Enabled | `dropThrownWeaponWhenUsingDeviceEnabled` | `bool` | – | – |

### Hide Weapon Meshes Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Override Option To Hide Weapon Mesh When Not Used | `overrideOptionToHideWeaponMeshWhenNotUsed` | `bool` | – | – |
| Hide Weapon Mesh When Not Used | `hideWeaponMeshWhenNotUsed` | `bool` | – | – |

### Start Game With Melee Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Start Game With Weapon | `startGameWithWeapon` | `bool` | – | – |
| Draw Weapon On Start Enabled | `drawWeaponOnStartEnabled` | `bool` | true | – |
| Weapon Name To Start Game | `weaponNameToStartGame` | `string` | – | – |
| Start Game With List Of Weapons | `startGameWithListOfWeapons` | `bool` | – | – |
| List Of Weapons To Start | `listOfWeaponsToStart` | `List<string>` | new List<string> () | – |
| Start With Random Weapon | `startWithRandomWeapon` | `bool` | – | – |
| Start With Random Weapon From List Of Weapons To Start | `startWithRandomWeaponFromListOfWeaponsToStart` | `bool` | – | – |
| Start With Weapon Only If Already Available | `startWithWeaponOnlyIfAlreadyAvailable` | `bool` | – | – |
| Draw Weapon At Start If Configured Externally | `drawWeaponAtStartIfConfiguredExternally` | `bool` | – | – |

### Start Game With Melee Shield Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Start Game With Shield | `startGameWithShield` | `bool` | – | – |
| Shield Name To Start Game | `shieldNameToStartGame` | `string` | – | – |

### Weapon List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Melee Weapon Grabbed Info List | `meleeWeaponGrabbedInfoList` | `List<meleeWeaponGrabbedInfo>` | new List<meleeWeaponGrabbedInfo> () | – |
| Melee Weapon Prefab Info List | `meleeWeaponPrefabInfoList` | `List<meleeWeaponPrefabInfo>` | new List<meleeWeaponPrefabInfo> () | – |

### Shield List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shield Prefab Info List | `shieldPrefabInfoList` | `List<shieldPrefabInfo>` | new List<shieldPrefabInfo> () | – |
| Shield Grabbed Info List | `shieldGrabbedInfoList` | `List<shieldGrabbedInfo>` | new List<shieldGrabbedInfo> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On State Change | `useEventsOnStateChange` | `bool` | – | – |
| Event On State Active | `eventOnStateActive` | `UnityEvent` | – | – |
| Event On State Deactivate | `eventOnStateDeactivate` | `UnityEvent` | – | – |
| Use Events On Melee Weapon Equipped | `useEventsOnMeleeWeaponEquipped` | `bool` | – | – |
| Event On Melee Weapon Equipped | `eventOnMeleeWeaponEquipped` | `UnityEvent` | – | – |
| Use Event On Grab Drop Weapon | `useEventOnGrabDropWeapon` | `bool` | – | – |
| Event On Grab Weapon | `eventOnGrabWeapon` | `UnityEvent` | – | – |
| Event On Drop Weapon | `eventOnDropWeapon` | `UnityEvent` | – | – |

### Stolen Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Weapon Stolen | `useEventOnWeaponStolen` | `bool` | – | – |
| Event On Weapon Stolen | `eventOnWeaponStolen` | `UnityEvent` | – | – |

### Save Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Save Current Melee Weapon List To Save File | `saveCurrentMeleeWeaponListToSaveFile` | `bool` | true | – |

### IK Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use IK On Hands | `useIKOnHands` | `bool` | – | – |
| Use IK On Hands Only On Fba | `useIKOnHandsOnlyOnFba` | `bool` | – | – |
| Main IK System | `mainIKSystem` | `IKSystem` | – | – |
| Hands On Melee Weapon IK System | `handsOnMeleeWeaponIKSystem` | `OnAnimatorIKComponent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Melee Weapons Grabbed Manager Active | `meleeWeaponsGrabbedManagerActive` | `bool` | – | – |
| Current Number Of Weapons Available | `currentNumberOfWeaponsAvailable` | `int` | – | – |
| Current Weapon Index | `currentWeaponIndex` | `int` | 0 | – |
| Equip Melee Weapon Paused | `equipMeleeWeaponPaused` | `bool` | – | – |
| Current Melee Weapon Sheathed Or Carried | `currentMeleeWeaponSheathedOrCarried` | `bool` | – | – |
| Is Loading Game | `isLoadingGame` | `bool` | – | – |
| Carrying Object | `carryingObject` | `bool` | – | – |
| Full Body Awareness Active | `fullBodyAwarenessActive` | `bool` | – | – |
| Custom Melee Weapon Mesh Scale Active | `customMeleeWeaponMeshScaleActive` | `bool` | – | – |
| Custom Melee Weapon Mesh Scale | `customMeleeWeaponMeshScale` | `float` | 0 | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Game Object | `playerGameObject` | `GameObject` | – | – |
| Player Input | `playerInput` | `playerInputManager` | – | – |
| Main Grab Objects | `mainGrabObjects` | `grabObjects` | – | – |
| Main Grabbed Object Melee Attack System | `mainGrabbedObjectMeleeAttackSystem` | `grabbedObjectMeleeAttackSystem` | – | – |
| Main Inventory Manager | `mainInventoryManager` | `inventoryManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `initializeMeleeManagerValues()` | 本体が空で何もしない。 |
| `drawNextWeaponAvailable()` | 所持数を数え直し、1本以上あれば先頭の武器を`checkMeleeWeaponToUse`で装備する。 |
| `drawRandomWeaponFromPrefabList(string previousWeaponName)` | 直前と違う武器をプリファブ一覧から抽選し、その武器を装備する。 |
| `inputSetWeaponByIndex(int currentNumberInput)` | 入力番号を所持リストのインデックスへ変換し、所持数とグラブ可否を確認して`checkWeaponByNumber`を呼ぶ。 |
| `resetStartWithWeaponCheckedOnCharacterSpawn()` | 開始時武器チェック済みフラグ`startWithWeaponChecked`をfalseに戻すだけ。 |
| `checkMeleeWeaponToUse(string weaponNameToSearch, bool checkIfWeaponNotFound)` | 指定名の所持武器があれば装備し、無ければプリファブから生成してグラブさせ、成否を返す。 |
| `setCheckDrawKeepWeaponAnimationPauseState(bool state)` | 攻撃システムの描画/納刀アニメーション一時停止フラグを設定するだけ。 |
| `checkIfDrawWeapon()` | マネージャ有効時に`currentWeaponIndex`の武器を装備し、描画/納刀イベントを発火する。 |
| `stopActivateDrawkeepMeleeWeaponAnimationCoroutine()` | 実行中の武器描画アニメーション用コルーチンを停止する。 |
| `enableOrDisableMeleeWeaponsGrabbedManager(bool state)` | 有効時は現在武器を装備、無効時は納刀・投擲中ならドロップし、UI・イベント・クイックアクセスを更新する。 |
| `setDrawMeleeWeaponsPausedState(bool state)` | 武器を抜く処理を止めるフラグ`drawMeleeWeaponsPaused`を設定するだけ。 |
| `disableCurrentMeleeWeapon(string weaponName)` | 指定武器が現在武器なら所持状態を解除し、武器オブジェクトを非表示にして体のメッシュを表示する。 |
| `checkObjectMeshToEnableOrDisable(bool enableWeaponMesh, meleeWeaponGrabbedInfo currentMeleeWeaponGrabbedInfo)` | 武器メッシュを必要なら生成し、表示切替と親・位置・回転・スケールの設定を行う。 |
| `getWeaponPrefabByName(string weaponName)` | 名前一致の`meleeWeaponPrefabInfo`を返し、無ければnullを返す。 |
| `checkIfCanUseMeleeWeaponPrefabByName(string weaponName)` | その名前の武器プリファブが登録されているかを返す。 |
| `getWeaponGrabbedByName(string weaponName)` | 所持リストから名前一致の武器の`grabPhysicalObjectMeleeAttackSystem`を返す。 |
| `checkWeaponToStore(string weaponName, GameObject weaponGameObject)` | `storeEachGrabbedWeapon`有効時のみ、拾った武器を所持リストへ追加/選択してインベントリ登録する。 |
| `checkToDropWeaponFromList(string weaponName)` | 所持リストから武器を外し、投擲状態に応じてインベントリからも削除し、ドロップ力を加える。 |
| `disableIsCurrentWeaponStateOnAllWeapons()` | 全武器の`isCurrentWeapon`をfalseにするだけ。 |
| `isCurrentMeleeWeaponSheathedOrCarried()` | 現在武器を所持または納刀中かを返す。 |
| `isGrabObjectsEnabled()` | グラブシステムが有効かを返す。 |
| `isCarryingRegularPhysicalObject()` | 通常の物理オブジェクトを運んでいるかを返す。 |
| `enableOrDisableMeleeWeaponMeshesOnCharacterBody(bool state)` | 所持中で非投擲の武器メッシュを一括表示/非表示し、現在武器と非表示設定は除外する。 |
| `enableOrDisableMeleeWeaponMeshOnCharacterBodyByNameAndInstantiateMesh(bool state, string weaponName)` | 指定武器のメッシュを生成しつつ、非表示設定を考慮して表示状態を切り替える。 |
| `checkIfHideWeaponMeshWhenNotUsedByName(string weaponNameToSearch)` | 指定武器が所持中なら「未使用時にメッシュを隠す」設定を返す。 |
| `checkIfHideShieldMeshWhenNotUsedByName(string shieldNameToSearch)` | 指定盾が所持中なら「未使用時にメッシュを隠す」設定を返す。 |
| `enableOrDisableMeleeWeaponMeshOnCharacterBodyByName(bool state, string weaponNameToSearch)` | 指定武器のメッシュ表示を、状態が異なる場合のみ切り替える。 |
| `enableOrDisableAllMeleeWeaponMeshesOnCharacterBody(bool state)` | 全武器メッシュを一括切替し、表示時は現在武器を除外する。 |
| `enableOrDisableAllMeleeWeaponMeshesOnCharacterBodyCheckingIfHiddingMeshes(bool state)` | 同上だが、表示時に各武器の「隠す」設定も加味する。 |
| `enableOrDisableAllMeleeWeaponShieldMeshesOnCharacterBody(bool state)` | 所持中の全盾オブジェクトを一括表示/非表示し、表示時は現在盾を除外する。 |
| `enableOrDisableAllMeleeWeaponShieldMeshesOnCharacterBodyCheckingIfHiddingMeshes(bool state)` | 同上だが、表示時に盾の「隠す」設定も加味する。 |
| `characterIsCarryingWeapon()` | マネージャ有効かつ攻撃システムが武器を所持しているかを返す。 |
| `getLastTimeDrawMeleeWeapon()` | 最後に武器を抜いた時刻を攻撃システムから返す。 |
| `equipMeleeWeapon(string weaponNameToSearch, bool checkIfWeaponNotFound, bool ignoreDrawMeleeWeapon)` | 武器を所持リストへ追加または選択し、必要なら描画してクイックアクセスを更新、装備成否を返す。 |
| `unEquipMeleeWeapon(string weaponNameToSearch, bool dropWeaponObject)` | 武器の所持/選択を解除し、メッシュを隠して`dropWeaponObject`で表示を切替、次のインデックスを再計算する。 |
| `checkWeaponToSelectOnQuickAccessSlots(string weaponName)` | 指定武器を装備して描画/納刀イベントを発火し、現在武器になったかを返す。 |
| `getCurrentGrabbedObjectTransform()` | 武器所持中のみ現在の武器Transformを返す。 |
| `isMeleeWeaponsGrabbedManagerActive()` | マネージャが有効かを返す。 |
| `getCurrentWeaponName()` | `isCurrentWeapon`な武器名を返し、無ければ空文字を返す。 |
| `getCurrentShieldName()` | `isCurrentShield`な盾名を返し、無ければ空文字を返す。 |
| `getEmptyWeaponToUseOnlyShield()` | 盾だけを使うための空武器名を攻撃システムから返す。 |
| `getCurrentWeaponMeshByName(string weaponName)` | 指定武器のメッシュGameObjectを返す。 |
| `isWeaponInGrabbedInfoList(string weaponName)` | 指定名の武器が所持リストにあるかを返す。 |
| `getCurrentWeaponActiveName()` | `currentWeaponIndex`にある武器名を返す。 |
| `isUseEquipShieldCheckWhenActivatingShieldActive()` | 盾有効化時の装備チェックフラグを返す。 |
| `setUseEquipShieldCheckWhenActivatingShieldState(bool state)` | 盾有効化時の装備チェックフラグを設定するだけ。 |
| `equipShield(string shieldName)` | `setShieldActiveState(true, ...)`で盾を装備し、その成否を返す。 |
| `unequipeShield(string shieldName)` | 盾を非装備にして盾と空武器を非表示にし、成否を返す。 |
| `setShieldActiveState(bool state, string shieldName)` | 盾を生成・選択して表示と装備/解除イベントを切り替え、攻撃システムへ盾情報と防御値を渡す。 |
| `checkEquipShieldIfNotCarryingPreviously()` | 盾未所持かつ条件を満たす時、最後に拾った盾が自動装備対象ならインベントリで装備する。 |
| `toggleDrawOrSheatheShield(string shieldName)` | 盾の現在状態から抜くか納めるかを決めて`drawOrSheatheShield`を呼ぶ。 |
| `drawOrSheatheShield(bool state, string shieldName, bool ignoreSetShieldActiveState)` | 必要なら盾を有効化し、攻撃システムに盾の抜刀/納刀を指示して親状態を補正する。 |
| `checkToKeepWeapon()` | 入力有効チェック付きで現在武器を納刀する。 |
| `checkToKeepWeaponWithoutCheckingInputActive()` | 入力状態を無視して現在武器を納刀する。 |
| `setStartGameWithWeaponState(bool state)` | 開始時武器装備フラグ`startGameWithWeapon`を設定するだけ。 |
| `setStartGameWithWeaponStateFromEditor(bool state)` | 開始時武器装備フラグを設定し、エディタ用に`updateComponent`を呼ぶ。 |
| `setWeaponNameToStartGame(string newName)` | 開始時武器名`weaponNameToStartGame`を設定するだけ。 |
| `updateDurabilityAmountStateOnAllObjects()` | 攻撃/ブロックの耐久設定が有効なら、所持武器と盾の耐久表示を更新する。 |
| `updateDurabilityAmountStateOnObjectByName(string weaponName)` | 指定武器の耐久表示だけを更新する。 |
| `getDurabilityAmountStateOnObjectByName(string weaponName)` | 指定武器の耐久値を返し、直前のドロップ値が残っていればそれを使い、無効時は-1を返す。 |
| `getDurabilityAmountStateOnObjectShieldByName(string weaponName)` | 指定盾の耐久値を返し、見つからないか無効時は-1を返す。 |
| `initializeDurabilityValue(float newAmount, string weaponName, int currentObjectIndex)` | 指定武器の耐久値を初期化し、インベントリ番号`currentObjectIndex`も渡す。 |
| `setInventoryObjectIndex(string weaponName, int currentObjectIndex)` | 指定武器のインベントリオブジェクト番号を設定する。 |
| `initializeDurabilityValueOnShield(float newAmount, string shieldName, int currentObjectIndex)` | 指定盾の耐久値とインベントリ番号を初期化する。 |
| `setInventoryObjectIndexOnShield(string shieldName, int currentObjectIndex)` | 指定盾のインベントリオブジェクト番号を設定する。 |
| `repairObjectFully(string weaponName)` | 指定武器の耐久値を全回復する。 |
| `repairObjectShieldFully(string weaponName)` | 指定盾の耐久値を全回復する。 |
| `breakFullDurabilityOnCurrentWeapon()` | 武器所持中かつ耐久設定有効なら、現在武器の耐久を0にする。 |
| `breakFullDurabilityOnCurrentShield()` | 武器所持中かつ耐久設定有効なら、現在盾の耐久を0にする。 |
| `checkDurabilityOnBlockWithShield(float extraMultiplier)` | 現在盾のブロック時耐久処理を`extraMultiplier`付きで行い、その結果を返す。 |
| `checkIfReturnThrowWeaponOrDropItExternally()` | 武器投擲中なら、設定に応じて外部ドロップ(false)か手元へ戻す(true)を選ぶ。 |
| `checkIfDropThrownWeaponWhenUsingDevice()` | デバイス使用時に投擲中の武器を落とす設定なら、外部ドロップする。 |
| `isCurrentWeaponThrown()` | 現在武器が投擲中かを返す。 |
| `isAimingBowActive()` | 弓のエイム中かを返す。 |
| `isCuttingModeActive()` | 切断モード中かを返す。 |
| `isBlockActive()` | ブロック中かを返す。 |
| `isDrawWeaponAtStartIfFoundOnInitializingInventoryActive()` | インベントリ初期化時に武器を抜く設定かを返す。 |
| `setWeaponNameToStartGameFromEditor(string newName)` | 開始武器名を設定し、エディタ用に`updateComponent`を呼ぶ。 |
| `addNewMeleeWeaponPrefab(GameObject newWeaponPrefab, string newWeaponName, bool useBowWeaponType)` | 武器プリファブを一覧へ追加し、既存項目なら空欄を補完して`updateComponent`を呼ぶ。 |
| `removeMeleeWeaponPrefab(string newWeaponName)` | 指定武器プリファブを削除し、残りの`weaponPrefabIndex`を振り直して更新する。 |
| `checkIfMeleeShieldExists(string shieldName)` | 指定盾が未登録の場合にtrueを返す。 |
| `removeMeleeShieldPrefab(string shieldName)` | 指定盾プリファブを削除し、残りの`shieldPrefabIndex`を振り直して更新する。 |
| `addNewMeleeShieldPrefab(GameObject newShieldPrefab, string newShieldName)` | 盾プリファブを一覧へ追加し、既存のマウント設定を引き継いで`updateComponent`を呼ぶ。 |
| `inputDrawOrKeepMeleeWeapon()` | 投擲中なら投擲/戻し、武器が無ければ何もせず、それ以外は入力チェック付きで抜刀/納刀する。 |
| `drawOrKeepMeleeWeaponWithoutCheckingInputActive()` | 入力状態を無視して武器の抜刀/納刀を行う。 |
| `drawMeleeWeaponGrabbedCheckingAnimationDelay()` | 現在武器が描画アニメを使う場合のみ0.2秒遅延コルーチンで抜刀/納刀し、他は即実行する。 |
| `resetCurrentAttackByIndex()` | 攻撃システムの現在攻撃インデックスをリセットする。 |
| `activateGrabbedObjectMeleeAttackByIndex()` | 攻撃システムの現在インデックスの攻撃を発動する。 |
| `activateOrDeactivateBlockGrabbedObjectMeleee(bool state)` | `state`に応じてブロック入力の有効/解除を攻撃システムへ送る。 |
| `activateOrDeactivateBlockGrabbedObjectMeleeeCheckingCurrentState(bool state)` | 現在のブロック状態と異なる場合のみブロック入力の有効/解除を行う。 |
| `setIgnoreUseDrawKeepWeaponAnimationState(bool state)` | 描画/納刀アニメを無視するフラグを攻撃システムに設定する。 |
| `setOriginalIgnoreUseDrawKeepWeaponAnimationState()` | 描画/納刀アニメ無視フラグを元の値に戻す。 |
| `setIsCarryingObjectState(bool state)` | 武器所持状態を反映し、IK・グラブ/ドロップイベント・最後の所持武器名を更新する。 |
| `setFullBodyAwarenessActiveState(bool state)` | FBA状態を保持し、武器所持中ならIKの手設定を更新する。 |
| `getCurrentNumberOfWeaponsAvailable()` | 所持中武器を数え直し、その件数を返す。 |
| `checkIfCarryingWeaponByName(string weaponName)` | 指定武器を所持しているかを返す。 |
| `getFirstRegularMeleeWeaponTypeAvailableName()` | 所持中の非ボウ武器の先頭名を返し、無ければ空文字を返す。 |
| `getFirstBowMeleeWeaponTypeAvailableName()` | 所持中のボウ武器の先頭名を返し、無ければ空文字を返す。 |
| `isThereAnyBowMeleeWeaponTypeAvailable()` | 所持リストにボウ武器が1つでもあるかを返す。 |
| `renameWeapon(string currentWeaponName, string newWeaponName)` | 武器プリファブ名を変更し、プリファブ側の名前も更新して`updateComponent`を呼ぶ。 |
| `selectAndDrawFirstBowMeleeWeaponTypeAvailable()` | 有効時、所持中の最初のボウ武器をクイックアクセス経由で選択・装備する。 |
| `checkEventOnWeaponStolen()` | 武器奪取イベントが有効なら`eventOnWeaponStolen`を発火する。 |
| `setCustomMeleeWeaponMeshScaleActive(float newValue)` | メッシュ倍率を設定し、0以外ならカスタム倍率を有効にする。 |
| `setWeaponMeshScaleOnAllWeapons(float newValue)` | 倍率を設定し、所持武器とメッシュのlocalScaleを一括変更する。 |
| `setPlaceTriggerInFrontOfCharacterOnAllAttacksState(bool state)` | 全攻撃のトリガーをキャラ前方に置く設定を攻撃システムへ渡す。 |
| `setExtraTriggerMultiplierScaleOnAllMeleeAttacksActiveState(bool state, float value)` | 全近接攻撃の追加トリガー倍率設定を攻撃システムへ渡す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStateActive` | `UnityEvent` | – |
| `eventOnStateDeactivate` | `UnityEvent` | – |
| `eventOnMeleeWeaponEquipped` | `UnityEvent` | – |
| `eventOnGrabWeapon` | `UnityEvent` | – |
| `eventOnDropWeapon` | `UnityEvent` | – |
| `eventOnWeaponStolen` | `UnityEvent` | – |

## 内部型

- `meleeWeaponGrabbedInfo`（class）
- `meleeWeaponPrefabInfo`（class）
- `shieldPrefabInfo`（class）
- `shieldGrabbedInfo`（class）
