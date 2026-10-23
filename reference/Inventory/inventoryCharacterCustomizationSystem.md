# inventoryCharacterCustomizationSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/inventoryCharacterCustomizationSystem.cs:6`

**概要**: 防具・服ピースの装備/解除と外見カスタマイズメニューを制御するコンポーネント。装備時のステータス/スキル/耐性/アビリティ適用、フルセット判定、ピースのドロップと耐久値の保存を担う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Customization Enabled | `characterCustomizationEnabled` | `bool` | true | – |
| Current Category List To Use Active | `currentCategoryListToUseActive` | `List<string>` | new List<string> () | – |
| Character Customization Menu Name | `characterCustomizationMenuName` | `string` | "Character Aspect Customization Menu" | – |
| Regular Inventory Panel Name | `regularInventoryPanelName` | `string` | "Default" | – |
| Customization Inventory Panel Name | `customizationInventoryPanelName` | `string` | "Armor-Cloth Customization" | – |
| Check Available Armor Cloth Quick Access Slots When Equipping Objects Enabled | `checkAvailableArmorClothQuickAccessSlotsWhenEquippingObjectsEnabled` | `bool` | true | – |

### Character Menu View Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Position Offset | `cameraPositionOffset` | `Vector3` | – | – |
| Camera Euler Offset | `cameraEulerOffset` | `Vector3` | – | – |
| Rotate Character Enabled | `rotateCharacterEnabled` | `bool` | true | – |
| Character Rotation Speed | `characterRotationSpeed` | `float` | 10 | – |

### Character Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Unscaled Time On Animator | `setUnscaledTimeOnAnimator` | `bool` | – | – |
| Set New Animator Idle | `setNewAnimatorIdle` | `bool` | – | – |
| Animator Idle | `animatorIdle` | `int` | – | – |

### Initial Armor/Cloth Pieces Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Initial Armor Cloth Piece List | `setInitialArmorClothPieceList` | `bool` | – | – |
| Initial Armor Cloth Piece List Name | `initialArmorClothPieceListName` | `string` | – | – |
| Initial Armor Cloth Info List | `initialArmorClothInfoList` | `List<initialArmorClothInfo>` | new List<initialArmorClothInfo> () | – |
| Use Character Aspect Customization Template | `useCharacterAspectCustomizationTemplate` | `bool` | – | – |
| Initial Character Aspect Customization Template | `initialCharacterAspectCustomizationTemplate` | `characterAspectCustomizationTemplate` | – | – |
| Use Random Character Aspect Customization Template | `useRandomCharacterAspectCustomizationTemplate` | `bool` | – | – |
| Character Aspect Customization Template List | `characterAspectCustomizationTemplateList` | `List<characterAspectCustomizationTemplate>` | new List<characterAspectCustomization… | – |

### Drop Pieces Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Inventory Manager | `useInventoryManager` | `bool` | true | – |
| Drop Armor Cloth Pieces Externally Enabled | `dropArmorClothPiecesExternallyEnabled` | `bool` | true | – |
| Instantiate Pieces Dropped Externally Enabled | `instantiatePiecesDroppedExternallyEnabled` | `bool` | true | – |
| Add Force To Dropped Object | `addForceToDroppedObject` | `bool` | – | – |
| Force Mode For Dropped Object | `forceModeForDroppedObject` | `ForceMode` | – | – |
| Force Amount To Dropped Object | `forceAmountToDroppedObject` | `float` | – | – |

### Character Values Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Upgrade Abilities Enabled | `upgradeAbilitiesEnabled` | `bool` | true | – |
| Upgrade Stats Enabled | `upgradeStatsEnabled` | `bool` | true | – |
| Upgrade Skills Enabled | `upgradeSkillsEnabled` | `bool` | true | – |
| Upgrade Damage Resistance Values Enabled | `upgradeDamageResistanceValuesEnabled` | `bool` | true | – |
| Use Event On Durability Affected Enabled | `useEventOnDurabilityAffectedEnabled` | `bool` | – | – |

### Durability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Store Durability Values Of Pieces Enabled | `storeDurabilityValuesOfPiecesEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Menu Opened | `menuOpened` | `bool` | – | – |
| Full Armor Cloth Active | `fullArmorClothActive` | `bool` | – | – |
| Current Full Armor Cloth Active Name | `currentFullArmorClothActiveName` | `string` | – | – |
| Main Character Aspect Customization UI System Assigned | `mainCharacterAspectCustomizationUISystemAssigned` | `bool` | – | – |
| Main Character Customization Manager Assigned | `mainCharacterCustomizationManagerAssigned` | `bool` | – | – |
| Rotation Input Active | `rotationInputActive` | `bool` | – | – |
| Keep All Character Meshes Disabled Active | `keepAllCharacterMeshesDisabledActive` | `bool` | – | – |

### Pieces and Stats Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Pieces List | `currentPiecesList` | `List<string>` | new List<string> () | – |
| Current Pieces Info List | `currentPiecesInfoList` | `List<pieceInfo>` | new List<pieceInfo> () | – |
| Temporal Stat Value List | `temporalStatValueList` | `List<temporalStatValue>` | new List<temporalStatValue> () | – |

### Armor Cloth Data Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Armor Cloth Piece Template Data | `mainArmorClothPieceTemplateData` | `armorClothPieceTemplateData` | – | – |
| Main Full Armor Cloth Template Data | `mainFullArmorClothTemplateData` | `fullArmorClothTemplateData` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Open Menu | `eventOnOpenMenu` | `UnityEvent` | – | – |
| Event On Close Menu | `eventOnCloseMenu` | `UnityEvent` | – | – |
| Event To Set Next Character Model | `eventToSetNextCharacterModel` | `UnityEvent` | – | – |
| Event To Set Previous Character Model | `eventToSetPreviousCharacterModel` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Inventory Manager | `mainInventoryManager` | `inventoryManager` | – | – |
| Main Inventory Quick Access Slots System | `mainInventoryQuickAccessSlotsSystem` | `inventoryQuickAccessSlotsSystem` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Main Camera Parent | `mainCameraParent` | `Transform` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |
| Main Character Aspect Customization UI System | `mainCharacterAspectCustomizationUISystem` | `characterAspectCustomizationUISystem` | – | – |
| Main Character Customization Manager | `mainCharacterCustomizationManager` | `characterCustomizationManager` | – | – |
| Main Player Inventory Categories List Manager | `mainPlayerInventoryCategoriesListManager` | `playerInventoryCategoriesListManager` | – | – |
| Main Remote Event System | `mainRemoteEventSystem` | `remoteEventSystem` | – | – |
| Main Player Stats System | `mainPlayerStatsSystem` | `playerStatsSystem` | – | – |
| Main Player Skills System | `mainPlayerSkillsSystem` | `playerSkillsSystem` | – | – |
| Main Player Abilities System | `mainPlayerAbilitiesSystem` | `playerAbilitiesSystem` | – | – |
| Main Health | `mainHealth` | `health` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkSetInitialArmorClothList()` | `setInitialArmorClothPieceList`が有効なら初期装備設定コルーチンを開始するだけ。 |
| `stopMenuCoroutineUpdate()` | 実行中の`menuCoroutine`があれば停止するだけ。 |
| `inputSetRotationInputActive(bool state)` | メニュー表示中のみ`rotationInputActive`を更新する。 |
| `setMultipleCharacterCustomizationTypeButtonInfoByName(string characterName)` | UIシステム割当済みなら同名メソッドへ処理を委譲するだけ。 |
| `openOrCloseCustomizationMenu(bool state)` | 開閉状態を反転し、カメラ位置・回転コルーチン・一人称メッシュ・開閉イベントを切り替える。 |
| `equipObject(string objectName, string categoryName)` | `equipOrUnequipObject(true, …)`で装備し、成功可否を返す。 |
| `unequipObject(string objectName, string categoryName)` | `equipOrUnequipObject(false, …)`で解除し、成功可否を返す。 |
| `unequipAllCurrentArmorCloth()` | 現在の防具/服を走査し、カテゴリ名が取れたものを在庫側の解除処理で外す。 |
| `setNewArmorClothPieceTemplateData(armorClothPieceTemplateData newArmorClothPieceTemplateData)` | `mainArmorClothPieceTemplateData`を差し替えるだけ。 |
| `setNewFullArmorClothTemplateData(fullArmorClothTemplateData newFullArmorClothTemplateData)` | `mainFullArmorClothTemplateData`を差し替えるだけ。 |
| `setInitialArmorClothPieceListState(bool state)` | `setInitialArmorClothPieceList`を設定するだけ。 |
| `setUseCharacterAspectCustomizationTemplateState(bool state)` | `useCharacterAspectCustomizationTemplate`を設定するだけ。 |
| `setUseRandomCharacterAspectCustomizationTemplateState(bool state)` | `useRandomCharacterAspectCustomizationTemplate`を設定するだけ。 |
| `setCharacterAspectCustomizationTemplateList(List<characterAspectCustomizationTemplate> newList)` | テンプレート一覧`characterAspectCustomizationTemplateList`を差し替えるだけ。 |
| `setInitialCharacterAspectCustomizationTemplate(characterAspectCustomizationTemplate newCharacterAspectCustomizationTemplate)` | `initialCharacterAspectCustomizationTemplate`を設定するだけ。 |
| `checkCameraViewToFirstOrThirdPerson(bool state)` | 機能有効かつUI割当済みなら、UI側の視点切替処理へ委譲するだけ。 |
| `checkCameraViewToFirstOrThirdPersonOnEditor(bool state)` | エディタ用にUI側の視点切替処理を呼ぶだけ。 |
| `setInitialArmorClothList()` | テンプレートまたは初期リストから初期防具を装備し、各ピースのステータスを適用する。 |
| `dropArmorClothPieceByCategoryName(string categoryName)` | カテゴリ名からピース名を引き、`dropArmorClothPieceByName`へ渡すだけ。 |
| `dropArmorClothPieceByName(string pieceName)` | 装備中のピースを在庫から1個ドロップし、設定に応じて解除処理と飛散力を与える。 |
| `addOrRemoveDurabilityAmountToObjectByCategoryName(string categoryName, float newAmount, bool setAmountAsCurrentValue)` | `categoryName`をピース名として耐久値を置換/加算し、必要なら耐久イベント通知と0以下時の在庫更新を行う。 |
| `updateDurabilityAmountStateOnAllObjects()` | 保持中の全ピースの耐久値を`-1`指定で在庫側へ反映する。 |
| `updateDurabilityAmountStateOnObjectByName(string objectName)` | 指定名のピース耐久値を在庫側へ反映して終了する。 |
| `getDurabilityAmountStateOnObjectByName(string objectName)` | 指定名のピース耐久値を返し、無ければ-1を返す。 |
| `initializeDurabilityValue(float newAmount, string objectName, int currentObjectIndex)` | 指定ピースの耐久値を`newAmount`に置き換える（`-1`の無限耐久は除外）。 |
| `repairObjectFully(string objectName)` | 指定ピースの耐久を在庫側の最大値まで回復させて反映する。 |
| `isCheckAvailableArmorClothQuickAccessSlotsWhenEquippingObjectsEnabled()` | `checkAvailableArmorClothQuickAccessSlotsWhenEquippingObjectsEnabled`を返すだけ。 |
| `checkIfArmorPartCanBeEquippedOnSameBodyPart(string objectName)` | `characterCustomizationManager`に同部位装備可否の判定を委譲し、未割当ならnullを返す。 |
| `getCharacterCustomizationManager()` | `mainCharacterCustomizationManager`を返すだけ。 |
| `updateCharacterTransform()` | `characterCustomizationManager`へ`playerTransform`を再設定するだけ。 |
| `setNewCharacterModel(GameObject newObject)` | UIシステム割当済みならキャラクターモデル差し替えを委譲するだけ。 |
| `updateCheckAssignCharacterAspectCustomizationUISystem()` | 機能有効かつ未割当のときUIシステムの参照取得を再試行する。 |
| `setNextOrPreviousCharacterModel(bool state)` | `state`に応じて次/前モデル用の`UnityEvent`を発火するだけ。 |
| `renameArmorClothObjectByName(string currentObjectName, string newObjectName)` | ピーステンプレートとフルセット内の名前を書き換え、必要ならアセット名変更と再更新を行う。 |
| `setNewCharacterCustomizationManager(characterCustomizationManager newCharacterCustomizationManager)` | `characterCustomizationManager`を差し替えてエディタ更新するだけ。 |
| `setKeepAllCharacterMeshesDisabledActiveStateOnEditor(bool state)` | `keepAllCharacterMeshesDisabledActive`を設定し更新するだけ。 |
| `setStoreDurabilityValuesOfPiecesEnabledValueOnEditor(bool state)` | `storeDurabilityValuesOfPiecesEnabled`を設定し更新するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnOpenMenu` | `UnityEvent` | – |
| `eventOnCloseMenu` | `UnityEvent` | – |
| `eventToSetNextCharacterModel` | `UnityEvent` | – |
| `eventToSetPreviousCharacterModel` | `UnityEvent` | – |

## 内部型

- `pieceInfo`（class）
- `elementSlotInfo`（class）
- `temporalStatValue`（class）
- `initialArmorClothInfo`（class）
