# weaponListManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/weaponListManager.cs:11`

**概要**: 武器ホイールUIを管理し、スロットの表示・武器選択・二丁持ち・ポーズやタイムスケール連携を扱う。

**公式ドキュメント抜粋**（[Weapon List Manager](../../docs/character-level-components/character/weapon-list-manager.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon List Manager Enabled | `weaponListManagerEnabled` | `bool` | – | – |
| Range | `range` | `Vector2` | new Vector2 (5f, 3f) | – |
| Rotation HUD Speed | `rotationHUDSpeed` | `float` | 20 | – |
| Time To Show Weapon Slots Wheel | `timeToShowWeaponSlotsWheel` | `float` | 1 | – |
| Number Of Weapon Slots | `numberOfWeaponSlots` | `int` | 8 | – |
| Use Blur UI Panel | `useBlurUIPanel` | `bool` | true | – |
| Draw Selected Weapon | `drawSelectedWeapon` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slow Down Time When Menu Active | `slowDownTimeWhenMenuActive` | `bool` | – | – |
| Time Scale When Menu Active | `timeScaleWhenMenuActive` | `float` | – | – |
| Select Weapon On Menu Close | `selectWeaponOnMenuClose` | `bool` | – | – |
| Use Sound On Slot | `useSoundOnSlot` | `bool` | – | – |
| Sound Effect | `soundEffect` | `AudioClip` | – | – |
| Sound Effect Audio Element | `soundEffectAudioElement` | `AudioElement` | – | – |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |
| Change Current Slot Size | `changeCurrentSlotSize` | `bool` | – | – |
| Change Current Slot Speed | `changeCurrentSlotSpeed` | `float` | – | – |
| Change Current Slot Multiplier | `changeCurrentSlotMultiplier` | `float` | – | – |
| Distance From Center To Select Weapon | `distanceFromCenterToSelectWeapon` | `float` | 10 | – |
| Player Can Move State Paused On Menu Opened | `playerCanMoveStatePausedOnMenuOpened` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Selecting Weapon | `selectingWeapon` | `bool` | – | – |
| Using Dual Wepaon | `usingDualWepaon` | `bool` | – | – |
| Selecting Right Weapon | `selectingRightWeapon` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Used By AI | `usedByAI` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Slots Menu | `weaponSlotsMenu` | `GameObject` | – | – |
| Weapons List Element | `weaponsListElement` | `GameObject` | – | – |
| Weapons Slots Wheel | `weaponsSlotsWheel` | `Transform` | – | – |
| Current Weapon Name Text | `currentWeaponNameText` | `Text` | – | – |
| Complete Weapons Wheel | `completeWeaponsWheel` | `GameObject` | – | – |
| Slot Arrow | `slotArrow` | `Transform` | – | – |
| Slot Arrow Icon | `slotArrowIcon` | `Transform` | – | – |
| Right Hand Wheel Position | `rightHandWheelPosition` | `RectTransform` | – | – |
| Left Hand Wheel Position | `leftHandWheelPosition` | `RectTransform` | – | – |
| Dual Hand Icon | `dualHandIcon` | `RectTransform` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Time Bullet Manager | `timeBulletManager` | `timeBullet` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setTouchingMenuPanelState(bool state)` | `fingerPressingTouchPanel`を設定し、タッチゾーン無効化を無視する状態をポーズ管理へ渡す。 |
| `selectWeapon(weaponSlotInfo slotInfo)` | 二丁持ち可否を判定してから武器マネージャへ選択を渡し、スロットの選択アイコンを更新する。 |
| `changeSlotSize(weaponSlotInfo slotInfo, bool setRegularSize, float sizeMultiplier, bool smoothSizeChange)` | 既存のサイズ変更を止め、通常サイズか倍率適用かとスムーズさを指定して拡縮コルーチンを開始する。 |
| `selectWeaponsSlots(bool state)` | ホイールの開閉に応じてポーズ・メニュー・弾丸時間・スロット情報を切り替え、閉じる時は選択武器を確定する。 |
| `canBeOpened()` | ポーズ中・デバイス使用中・無効時・武器モード外・メニュー中・近接攻撃中なら偽を返し、それ以外は真を返す。 |
| `udpateSlotsInfo()` | 綴り違いの名前で`updateSlotsInfo()`を呼ぶだけ。 |
| `updateSlotsInfo()` | 所持武器数から角度を割り出し、各スロットへ名前・アイコン・弾薬・選択状態を割り当てて並べる。 |
| `playSound(AudioElement sound)` | `sound`がnullでなければ`AudioPlayer.PlayOneShot`で鳴らすだけ。 |
| `inputOpenOrCloseWeaponsWheel(bool openWeaponsWheel)` | 引数に応じて`selectWeaponsSlots(true)`か`selectWeaponsSlots(false)`を呼ぶだけ。 |
| `setSelectingWeaponState(bool state)` | `usingDualWepaon`を`state`にするだけ。 |
| `setRightOrLeftWeapon(bool state)` | 二丁持ちが使える構成なら、右手か左手かに応じてホイール位置とアイコンの向きを切り替える。 |
| `setUsedByAIState(bool state)` | `usedByAI`を`state`にするだけ。 |
| `setWeaponListManagerEnabledState(bool state)` | `weaponListManagerEnabled`を`state`にするだけ。 |
| `setWeaponListManagerEnabledStateFromEditor(bool state)` | 有効状態を設定した後、`updateComponent`でコンポーネントとシーンを更新する。 |

## 内部型

- `weaponSlotInfo`（class）
