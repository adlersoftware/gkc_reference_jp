# powersListManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/powersListManager.cs:11`

**概要**: パワーのホイール選択とスロット編集を行うUI管理コンポーネント。割当・アイコン表示・ポーズメニュー連携を担当する。

**公式ドキュメント抜粋**（[Powers List Manager](../../docs/character-level-components/character/powers-list-manager.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Power List Manager Enabled | `powerListManagerEnabled` | `bool` | – | – |
| Range | `range` | `Vector2` | new Vector2 (5f, 3f) | – |
| Rotation HUD Speed | `rotationHUDSpeed` | `float` | 20 | – |
| Double Tap Time | `doubleTapTime` | `float` | 0.5f | – |
| Hold Tap Time | `holdTapTime` | `float` | 0.7f | – |
| Number Of Power Slots | `numberOfPowerSlots` | `int` | 8 | – |
| Number Of Enabled Powers | `numberOfEnabledPowers` | `int` | – | – |
| Adjust Slot Number To Amount Of Powers | `adjustSlotNumberToAmountOfPowers` | `bool` | – | – |
| Use Blur UI Panel | `useBlurUIPanel` | `bool` | true | – |
| Slow Down Time When Menu Active | `slowDownTimeWhenMenuActive` | `bool` | – | – |
| Time Scale When Menu Active | `timeScaleWhenMenuActive` | `float` | – | – |
| Select Power On Menu Close | `selectPowerOnMenuClose` | `bool` | – | – |
| Use Sound On Slot | `useSoundOnSlot` | `bool` | – | – |
| Sound Effect | `soundEffect` | `AudioClip` | – | – |
| Sound Effect Audio Element | `soundEffectAudioElement` | `AudioElement` | – | – |
| Change Current Slot Size | `changeCurrentSlotSize` | `bool` | – | – |
| Change Current Slot Speed | `changeCurrentSlotSpeed` | `float` | – | – |
| Change Current Slot Multiplier | `changeCurrentSlotMultiplier` | `float` | – | – |
| Distance From Center To Select Power | `distanceFromCenterToSelectPower` | `float` | 10 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Editing Powers | `editingPowers` | `bool` | – | – |
| Selecting Power | `selectingPower` | `bool` | – | – |
| Touching | `touching` | `bool` | – | – |
| Power Slot Info List | `powerSlotInfoList` | `List<powerSlotInfo>` | new List<powerSlotInfo> () | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Can Move State Paused On Menu Opened | `playerCanMoveStatePausedOnMenuOpened` | `bool` | true | – |
| Used By AI | `usedByAI` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Powers Slots Menu | `powersSlotsMenu` | `GameObject` | – | – |
| Powers List Content | `powersListContent` | `GameObject` | – | – |
| Powers List Element | `powersListElement` | `GameObject` | – | – |
| Powers Slots Wheel | `powersSlotsWheel` | `Transform` | – | – |
| Complete Powers Wheel | `completePowersWheel` | `GameObject` | – | – |
| Complete Powers List | `completePowersList` | `GameObject` | – | – |
| Current Power Name Text | `currentPowerNameText` | `Text` | – | – |
| Slot Arrow | `slotArrow` | `GameObject` | – | – |
| Slot Arrow Icon | `slotArrowIcon` | `Transform` | – | – |
| Power List Scroll Bar | `powerListScrollBar` | `Scrollbar` | – | – |
| Power List Wheel Element | `powerListWheelElement` | `GameObject` | – | – |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Powers Manager | `powersManager` | `otherPowers` | – | – |
| Time Bullet Manager | `timeBulletManager` | `timeBullet` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setTouchingMenuPanelState(bool state)` | タッチ状態を保持し、ダブルタップ判定で編集メニューを開き、タッチ無効化除外も設定する。 |
| `updateCurrentSelectedPowerSlotIcon(otherPowers.Powers currentPowerOnPowersManager)` | 選択中パワーのスロットだけアイコンを点灯し、名前表示と`setCurrentPowerByName`を更新する。 |
| `enableOrDisablePowerSlot(string powerName, bool state)` | 同名スロットを有効/無効化し、有効パワー数`numberOfEnabledPowers`を増減する。 |
| `editPowersSlots()` | 編集メニューの開閉を切り替え、ホイール・リスト・ポーズメニューの状態をまとめて更新する。 |
| `selectPower(powerSlotInfo slotInfo)` | 指定スロットのパワーを`powersManager`へ設定し、選択アイコンを切り替える。 |
| `changeSlotSize(powerSlotInfo slotInfo, bool setRegularSize, float sizeMultiplier, bool smoothSizeChange)` | 既存のサイズ補間コルーチンを止め、スロット拡大/縮小のコルーチンを開始する。 |
| `selectPowersSlots()` | パワーホイールの開閉を切り替え、ポーズ・時間停止・閉じる際のパワー確定を扱う。 |
| `closePowerListManagerMenus()` | 編集と選択をいったん開いた状態にしてから閉じ、両メニューを確実に閉じる。 |
| `canBeOpened()` | ポーズ中・デバイス使用中・メニュー表示中などでないかを確認し、開けるかを返す。 |
| `checkDuplicatedSlot(string powerName)` | 同じ名前のパワーが既にホイール上にあるかどうかを返す。 |
| `isEditingPowers()` | パワー編集メニューが開いているかを返すだけ。 |
| `getPowerByNumberKeyIndex(int numberKeyToSearch)` | 有効かつ指定番号キーを持つパワーのインデックスを返し、無ければ-1を返す。 |
| `updateSlotsInfo(bool isEditingPowers)` | スロット数・角度・アイコン・番号を再構成し、表示できるパワーが無ければホイールを閉じる。 |
| `assignPowerToSlot(otherPowers.Powers currentPowerToAssign, powerSlotInfo powerSlotToUse, bool slotWithPowerAssigned)` | パワーをスロットへ割り当て、番号・アイコン・選択表示・割当フラグを更新する。 |
| `playSound(AudioElement sound)` | `AudioPlayer.PlayOneShot`で指定サウンドを再生するだけ。 |
| `inputEditPowerSlots()` | パワー管理が有効で他メニューが閉じていれば、編集メニューを開閉する。 |
| `inputOpenOrClosePowersWheel(bool openPowersWheel)` | 有効時は`openPowersWheel`の値に関わらず、ホイール開閉をトグルする。 |
| `setUsedByAIState(bool state)` | AIが使用中かどうかのフラグを設定するだけ。 |
| `setPowerListManagerEnabledState(bool state)` | パワーリスト管理自体の有効フラグを設定するだけ。 |
| `setPowerListManagerEnabledStateFromEditor(bool state)` | 有効フラグを設定してから、エディタ用にコンポーネントを更新する。 |

## 内部型

- `powerSlotInfo`（class）
