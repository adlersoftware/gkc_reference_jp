# playerAbilitiesUISystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/playerAbilitiesUISystem.cs:11`

**概要**: アビリティのホイールメニューとDpadクイックアクセスUIを構築・更新し、スロット選択、アイコン割当、クールダウン/制限表示、タッチ入力を担当する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Open Menu Enabled | `openMenuEnabled` | `bool` | true | – |
| Ability List Manager Enabled | `abilityListManagerEnabled` | `bool` | – | – |
| Number Of Ability Slots | `numberOfAbilitySlots` | `int` | 8 | – |
| Select Ability On Menu Close | `selectAbilityOnMenuClose` | `bool` | – | – |
| Use Dpad Panel | `useDpadPanel` | `bool` | true | – |
| Time To Show Ability Slots Wheel | `timeToShowAbilitySlotsWheel` | `float` | 1 | – |
| Use Blur UI Panel | `useBlurUIPanel` | `bool` | true | – |
| Slow Down Time When Menu Active | `slowDownTimeWhenMenuActive` | `bool` | – | – |
| Time Scale When Menu Active | `timeScaleWhenMenuActive` | `float` | – | – |
| Ability Wheel Menu Rotation Range | `abilityWheelMenuRotationRange` | `Vector2` | new Vector2 (5f, 3f) | – |
| Rotation HUD Speed | `rotationHUDSpeed` | `float` | 20 | – |
| Show Only Enabled Ability Slots | `showOnlyEnabledAbilitySlots` | `bool` | – | – |

### Ability Slot Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Current Slot Size | `changeCurrentSlotSize` | `bool` | – | – |
| Change Current Slot Speed | `changeCurrentSlotSpeed` | `float` | – | – |
| Change Current Slot Multiplier | `changeCurrentSlotMultiplier` | `float` | – | – |
| Distance From Center To Select Ability | `distanceFromCenterToSelectAbility` | `float` | 10 | – |

### Slot Position And Size Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Slots Change Scale | `useSlotsChangeScale` | `bool` | – | – |
| Number Of Slots To Change Scale | `numberOfSlotsToChangeScale` | `int` | – | – |
| Slot Scale | `slotScale` | `float` | – | – |
| Min Slot Scale | `minSlotScale` | `float` | 0.3f | – |
| Slot Height Offset | `slotHeightOffset` | `float` | – | – |
| Wheel Radius | `wheelRadius` | `float` | 880 | – |

### Wheel And Scroll Rect Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Wheel Menu | `useWheelMenu` | `bool` | true | – |

### Sound Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Sound On Slot | `useSoundOnSlot` | `bool` | – | – |
| Sound Effect | `soundEffect` | `AudioClip` | – | – |
| Sound Effect Audio Element | `soundEffectAudioElement` | `AudioElement` | – | – |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |

### Dpad Icon Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dpad Icon Info List | `dpadIconInfoList` | `List<dpadIconInfo>` | new List<dpadIconInfo> () | – |
| Use Current Ability Icon | `useCurrentAbilityIcon` | `bool` | – | – |
| Current Ability Icon | `currentAbilityIcon` | `dpadIconInfo` | – | – |
| Current Ability Input Text | `currentAbilityInputText` | `Text` | – | – |
| Ability Input Name | `abilityInputName` | `string` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Selecting Ability | `selectingAbility` | `bool` | – | – |
| Current Ability Pressed Index | `currentAbilityPressedIndex` | `int` | -1 | – |
| Pause Check Using Device On Ability Input | `pauseCheckUsingDeviceOnAbilityInput` | `bool` | – | – |
| Input Paused | `inputPaused` | `bool` | – | – |
| Ability Slot Info List | `abilitySlotInfoList` | `List<abilitySlotInfo>` | new List<abilitySlotInfo> () | – |
| Closest Slot | `closestSlot` | `abilitySlotInfo` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Can Move State Paused On Menu Opened | `playerCanMoveStatePausedOnMenuOpened` | `bool` | true | – |
| Used By AI | `usedByAI` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Abilities Assigned On Dpad | `eventOnAbilitiesAssignedOnDpad` | `UnityEvent` | – | – |
| Event On Abilities Not Assigned On Dpad | `eventOnAbilitiesNotAssignedOnDpad` | `UnityEvent` | – | – |
| Event On Open Abilities Wheel | `eventOnOpenAbilitiesWheel` | `UnityEvent` | – | – |
| Event On Close Abilities Wheel | `eventOnCloseAbilitiesWheel` | `UnityEvent` | – | – |

### UI Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ability Slots Menu | `abilitySlotsMenu` | `GameObject` | – | – |
| Wheel Ability List Element | `wheelAbilityListElement` | `GameObject` | – | – |
| Dpad Panel | `dpadPanel` | `GameObject` | – | – |
| Main Enery Slider | `mainEnerySlider` | `Slider` | – | – |
| Abilities Energy Slider | `abilitiesEnergySlider` | `Slider` | – | – |
| Ability Slots Wheel | `abilitySlotsWheel` | `Transform` | – | – |
| Current Ability Name Text | `currentAbilityNameText` | `Text` | – | – |
| Complete Ability Wheel | `completeAbilityWheel` | `GameObject` | – | – |
| Complete Ability Wheel Rect Transform | `completeAbilityWheelRectTransform` | `RectTransform` | – | – |
| Slot Arrow | `slotArrow` | `Transform` | – | – |
| Slot Arrow Icon | `slotArrowIcon` | `Transform` | – | – |
| Slot Arrow Rect Transform | `slotArrowRectTransform` | `RectTransform` | – | – |
| Wheel Background | `wheelBackground` | `GameObject` | – | – |
| Slots Grid Transform Parent | `slotsGridTransformParent` | `Transform` | – | – |
| Slots Grid Panel Game Object | `slotsGridPanelGameObject` | `GameObject` | – | – |
| Grid Ability List Element | `gridAbilityListElement` | `GameObject` | – | – |
| Slots Grid Background | `slotsGridBackground` | `GameObject` | – | – |
| Ability Description Text Game Object | `abilityDescriptionTextGameObject` | `GameObject` | – | – |
| Ability Description Text | `abilityDescriptionText` | `Text` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Main Player Abilities System | `mainPlayerAbilitiesSystem` | `playerAbilitiesSystem` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Time Bullet Manager | `timeBulletManager` | `timeBullet` | – | – |
| Player Input | `playerInput` | `playerInputManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableDpadPanel(bool state)` | `useDpadPanel`が偽なら強制非表示とし、Dpadパネルの表示を切替える。 |
| `enableOrDisableExtraElementsOnAbilitiesUI(bool state)` | ホイール時は矢印、非ホイール時は背景を、加えて現在名テキストを表示切替する。 |
| `isUseWheelMenuActive()` | `useWheelMenu`をそのまま返す。 |
| `updateCurrentAbilityInputText()` | 現在アイコン使用時、`abilityInputName`のキー名をテキストへ入れる。 |
| `setTouchingMenuPanelState(bool state)` | `fingerPressingTouchPanel`を設定し、タッチゾーン除外状態をPauseManagerへ伝える。 |
| `updateCurrentSelectedAbilityUIByName(string abilityName)` | 一覧管理とDpad有効時のみ、再入防止フラグを立てて`selectAbilityByName`を呼ぶ。 |
| `selectAbilityByName(string abilityName)` | スロット一覧から同名を探して`selectAbility`を呼ぶだけ。 |
| `selectAbility(abilitySlotInfo slotInfo)` | 必要なら現在アビリティを設定し、選択アイコンとDpadアイコン・テキストを更新する。 |
| `changeSlotSize(abilitySlotInfo slotInfo, bool setRegularSize, float sizeMultiplier, bool smoothSizeChange)` | 既存の拡縮コルーチンを止め、スロット拡縮コルーチンを起動する。 |
| `selectAbilitySlots(bool state)` | 各種チェック後ホイールを開閉し、ポーズメニュー・時間・回転・イベントを更新する。 |
| `setPauseCheckUsingDeviceOnAbilityInputState(bool state)` | `pauseCheckUsingDeviceOnAbilityInput`を設定するだけ。 |
| `togglePauseCheckUsingDeviceOnAbilityInputState()` | デバイス使用チェックの一時停止フラグを反転する。 |
| `canBeOpened()` | ゲーム停止・デバイス使用・モード無効・メニュー中などを確認し開けるか返す。 |
| `udpateSlotsInfo()` | `updateSlotsInfo`を呼ぶだけの綴り違いラッパー。 |
| `updateSlotsInfo()` | 有効アビリティからスロットを配置・表示し、拡縮調整とDpadアイコン更新を行う。 |
| `checkIfAssignActivatedAbilitiesToFreeDpadSlots(string currentAbilityName, int abilityIndexToCheck, bool addingAbilityToWheel)` | Dpad割当の有無に応じ空きへ割当/解除し、現在アイコンとイベントを更新する。 |
| `updateDpadIconsOnWheelMenu()` | 有効スロットごとにDpad方向アイコンの表示と向きを割当情報に合わせ更新する。 |
| `getDpadIconInfoListIndexByAbilityIndex(int abilityIndex)` | アビリティ番号が一致するDpad情報の位置を返し、無ければ-1を返す。 |
| `getDpadIconInfoListIndexByAbilityName(string abilityName)` | アビリティ名が一致するDpad情報の位置を返し、無ければ-1を返す。 |
| `setDpadIconsInfo()` | 未割当時のみ有効アビリティをDpad各方向へ順に割当て、イベントと未使用アイコンを処理する。 |
| `checkEventsOnAbilitiesAssignedOnDpad(bool state)` | 状態が変化した時だけ割当/未割当イベントを発火する。 |
| `getAbilitySlotInfoList()` | `abilitySlotInfoList`をそのまま返す。 |
| `getAbilityIndexByName(string abilityName)` | アビリティ名から`abilityInfoList`の番号を返し、無ければ-1を返す。 |
| `setCurrentAbilityIconAssignedByName(string abilityName)` | 現在アイコン使用時、名前から番号を引いて`currentAbilityIcon`へ割当てる。 |
| `setDpadIconInfo(dpadIconInfo newDpadIconInfo, int currentAbilityIndex)` | 番号が有効なら名前・画像・表示を設定し、無効なら解除して未割当アイコンを隠す。 |
| `updateDpadIconsOnAbilitiesDeactivated()` | Dpad有効時、無効化されたアビリティの割当を解除する。 |
| `playSound(AudioElement sound)` | `sound`がnullでなければ`AudioPlayer`で1回再生する。 |
| `setUsedByAIState(bool state)` | `usedByAI`を設定するだけ。 |
| `setUseDpadPanelState(bool state)` | `useDpadPanel`を設定するだけ。 |
| `updateEnergySlider()` | 再生中かつDpad有効時、元スライダーの値を能力スライダーへ複製する。 |
| `activateAbilityCoolDown(string abilityName)` | 該当アイコンの制限表示を消し、クールダウン表示コルーチンを開始する。 |
| `activateAbilityLimit(string abilityName)` | 該当アイコンの制限表示コルーチンを開始し、残り時間を表示する。 |
| `stopActivateAbilityLimit(dpadIconInfo currentDpadIconInfo)` | 制限コルーチンを止め、制限テキストを非表示にする。 |
| `setInputPausedState(bool state)` | `inputPaused`を設定するだけ。 |
| `toggleInputPausedState()` | `inputPaused`を反転する。 |
| `setNumberOfAbilitySlotsValue(int newAmount)` | `numberOfAbilitySlots`を設定するだけ。 |
| `updateNumberOfAbilitySlotsWithAbilitiesAmount()` | 有効アビリティ数でスロット数を設定し直す。 |
| `inputOpenOrCloseAbilityWheel(bool openAbilityWheel)` | 各種チェック後、引数に応じ`selectAbilitySlots`でホイールを開閉する。 |
| `inputStartToPressAbilityWheelPanel()` | 旧チェックをコメントで残したまま`inputOpenOrCloseAbilityWheel(true)`を呼ぶ。 |
| `inputStopToPressAbilityWheelPanel()` | 同様に旧チェックを残し`inputOpenOrCloseAbilityWheel(false)`を呼ぶ。 |
| `inputUseDpadDirectionPressDown(int dpadIndex)` | 選択中はスロットをDpadへ割当、通常時はその方向のアビリティを押下使用する。 |
| `inputUseDpadDirectionPressHold()` | 押下中のDpad番号があれば、現在アビリティの押し続け使用を呼ぶ。 |
| `inputUseDpadDirectionPressUp()` | 押下中の番号があれば押上使用を呼び、番号を-1へ戻す。 |
| `resetCurrentAbilityPressedIndexByName(string abilityName)` | 押下中番号のアビリティ名が一致すれば-1へ戻す。 |
| `inputTouchPressDown(int dpadIndex)` | タッチ環境時のみDpad押下処理を呼び、押し続けフラグを立てる。 |
| `inputTouchPressUp()` | タッチ環境時のみ押し続けフラグを下ろし、Dpad押上処理を呼ぶ。 |
| `isSelectingAbilityActive()` | `selectingAbility`をそのまま返す。 |
| `setOpenMenuEnabled(bool state)` | `openMenuEnabled`を設定するだけ。 |
| `setUseDpadPanelStateFromEditor(bool state)` | Dpad有効状態を設定し`updateComponent`でシーンを更新する。 |
| `setOpenMenuEnabledFromEditor(bool state)` | メニュー開閉可否を設定し`updateComponent`でシーンを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnAbilitiesAssignedOnDpad` | `UnityEvent` | – |
| `eventOnAbilitiesNotAssignedOnDpad` | `UnityEvent` | – |
| `eventOnOpenAbilitiesWheel` | `UnityEvent` | – |
| `eventOnCloseAbilitiesWheel` | `UnityEvent` | – |

## 内部型

- `dpadDirection`（enum）
- `abilitySlotInfo`（class）
- `dpadIconInfo`（class）
