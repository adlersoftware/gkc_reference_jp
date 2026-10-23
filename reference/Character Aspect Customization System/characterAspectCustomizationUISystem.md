# characterAspectCustomizationUISystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `ingameMenuPanel`
- **ソース**: `Character Aspect Customization System/characterAspectCustomizationUISystem.cs:7`

**概要**: キャラクター作成メニューのUI制御コンポーネントで、ボタン/トグル/スライダーの入力を`characterCustomizationManager`のカスタマイズ処理へ中継します。パネル開閉やカメラ位置、キャラクター回転、マルチキャラクターの切り替えも扱います。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Animator Idle | `setNewAnimatorIdle` | `bool` | – | – |
| Animator Idle | `animatorIdle` | `int` | – | – |
| Set Unscaled Time On Animator | `setUnscaledTimeOnAnimator` | `bool` | – | – |

### Template Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Character Aspect Customization Template Data | `mainCharacterAspectCustomizationTemplateData` | `characterAspectCustomizationTemplateData` | – | – |

### Customization Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Customization Type Button Info List | `characterCustomizationTypeButtonInfoList` | `List<characterCustomizationTypeButtonInfo>` | new List<characterCustomizationTypeBu… | – |
| Use Multiple Character Customization | `useMultipleCharacterCustomization` | `bool` | – | – |
| Multiple Character Customization Type Button Info List | `multipleCharacterCustomizationTypeButtonInfoList` | `List<multipleCharacterCustomizationTypeButtonInfo>` | new List<multipleCharacterCustomizati… | – |

### UI Panel Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Panel Category Info List | `panelCategoryInfoList` | `List<panelCategoryInfo>` | new List<panelCategoryInfo> () | – |

### Rotate Character Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Rotate Character Enabled | `rotateCharacterEnabled` | `bool` | true | – |
| Character Rotation Speed | `characterRotationSpeed` | `float` | 10 | – |

### Initial Armor/Cloth Set Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Initial Class | `setInitialClass` | `bool` | – | – |
| Initial Class Name | `initialClassName` | `string` | – | – |
| Initial Armor Cloth Name | `initialArmorClothName` | `string` | – | – |
| Set Initial Class Just First Time Menu Opened | `setInitialClassJustFirstTimeMenuOpened` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Character Customization Manager Assigned | `characterCustomizationManagerAssigned` | `bool` | – | – |
| Menu Opened | `menuOpened` | `bool` | – | – |
| Keep All Character Meshes Disabled Active | `keepAllCharacterMeshesDisabledActive` | `bool` | – | – |
| Current Full Character Name | `currentFullCharacterName` | `string` | "" | – |

### Events

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Set Next Character Model | `eventToSetNextCharacterModel` | `UnityEvent` | – | – |
| Event To Set Previous Character Model | `eventToSetPreviousCharacterModel` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Character Customization Manager | `currentCharacterCustomizationManager` | `characterCustomizationManager` | – | – |
| Main Mouse Cursor Controller | `mainMouseCursorController` | `mouseCursorController` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Main Character Transform | `mainCharacterTransform` | `Transform` | – | – |
| Main Player Controller Transform | `mainPlayerControllerTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `copy()` | 現在の型別ボタン情報を複製し、名前を"Alice"にしたマルチキャラクター項目として追加してコンポーネントを更新するエディタ用処理。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とシーンのダーティ更新を行うだけ。 |
| `setMultipleCharacterCustomizationTypeButtonInfoByName(string characterName)` | 名前が一致する項目を検索して現在の名前とボタン情報リストを設定し、複数キャラ時は他キャラのボタンを非表示にする。 |
| `stopMenuCoroutineUpdate()` | `menuCoroutine`がnullでなければ停止するだけ。 |
| `inputSetRotationInputActive(bool state)` | メニューが開いているときだけ`rotationInputActive`を設定する。 |
| `inputToggleRotationInputActive()` | `rotationInputActive`を反転するだけ。 |
| `checkButtonPressedWithoutCheckIfPreviouslyPressed(GameObject buttonObject)` | 前回押下かのチェックを省いて直接`checkButton`を呼ぶだけ。 |
| `checkButtonPressed(GameObject buttonObject)` | 前回と同じボタンなら無視し、違えば`checkButton`で対応するカスタマイズ処理を実行する。 |
| `openPanelInfo(GameObject buttonObject)` | ボタンに対応するパネルを探して全パネルを閉じた後に開き、イベント・カメラ位置・スライダー値を適用して現在パネルにする。 |
| `closeAllPanelInfo()` | 全パネルを非表示にして`isCurrentPanel`をfalseにするだけ。 |
| `setMainCharacterCustomizationManager(characterCustomizationManager newCharacterCustomizationManager)` | 参照を代入し、nullでないかを`characterCustomizationManagerAssigned`に反映するだけ。 |
| `setMainCharacterAspectCustomizationTemplateData(characterAspectCustomizationTemplateData newCharacterAspectCustomizationTemplateData)` | `mainCharacterAspectCustomizationTemplateData`を代入するだけ。 |
| `setMainCharacterTransform(Transform newTransform)` | `mainCharacterTransform`を代入するだけ。 |
| `setMainPlayerControllerTransform(Transform newTransform)` | `mainPlayerControllerTransform`を代入するだけ。 |
| `setNewCharacterModel(GameObject newObject)` | 新モデルからマネージャーとテンプレートデータを取得し、キャラクターとプレイヤーのTransformを差し替える。 |
| `setNextOrPreviousCharacterModel(bool state)` | `state`に応じて次/前のキャラクターモデル設定イベントを呼び、インベントリ側のカスタマイズシステムにも転送する。 |
| `enableOrDisableHeadTemporaly(bool state)` | `currentCharacterCustomizationManager`があれば、その頭メッシュの一時表示切り替えを呼ぶだけ。 |
| `equipOrUnequipObject(bool state, string objectName, string categoryName)` | `setObjectState`で装備を切り替え、`checkEquippedStateOnObject`でベースメッシュを調整して成否を返す。 |
| `checkCameraViewToFirstOrThirdPerson(bool state)` | マネージャーがいれば`keepAllCharacterMeshesDisabledActive`を設定し、一人称/三人称の切り替えを転送する。 |
| `checkCameraViewToFirstOrThirdPersonOnEditor(bool state)` | エディタ用に`keepAllCharacterMeshesDisabledActive`を設定し、マネージャーの同処理を呼ぶ。 |
| `checkIfObjectAlreadyOnCurrentPiecesList(string pieceName)` | マネージャーに問い合わせ、参照が無ければfalseを返す。 |
| `getArmorClothPieceByName(string categoryName)` | マネージャーの結果をそのまま返し、参照が無ければ空文字を返す。 |
| `getArmorClothCategoryByName(string categoryName)` | マネージャーの結果をそのまま返し、参照が無ければ空文字を返す。 |
| `setMainInventoryCharacterCustomizationSystem(inventoryCharacterCustomizationSystem newInventoryCharacterCustomizationSystem)` | 参照を代入し、nullでないかを`mainInventoryCharacterCustomizationSystemAssigned`に反映するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToSetNextCharacterModel` | `UnityEvent` | – |
| `eventToSetPreviousCharacterModel` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`initializeMenuPanel()`, `openOrCloseMenuPanel(bool state)`

</details>

## 内部型

- `characterCustomizationButtonInfo`（class）
- `multipleCharacterCustomizationTypeButtonInfo`（class）
- `characterCustomizationTypeButtonInfo`（class）
- `panelCategoryInfo`（class）
- `panelInfo`（class）
