# playerExperienceSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Experience System/playerExperienceSystem.cs:9`

**概要**: プレイヤーの経験値・レベル・スキルポイントを管理し、レベルアップ時のパネル表示、ステータス加算とスキル解放、経験値倍率、経験値メニューUIを扱うコンポーネント。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Experience System Enabled | `experienceSystemEnabled` | `bool` | true | ONにすると経験値の獲得とレベル処理を有効にする。 |
| Current Level Experience Amount | `currentLevelExperienceAmount` | `int` | – | 現在レベルで獲得済みの経験値量。 |
| Current Level Experience To Next Level | `currentLevelExperienceToNextLevel` | `int` | – | 次のレベルまでに必要な経験値量。 |
| Total Experience Amount | `totalExperienceAmount` | `int` | – | 累計で獲得した経験値の総量。 |
| Total Experience Points | `totalExperiencePoints` | `int` | – | スキル解放に使うスキルポイント数。 |
| Current Level | `currentLevel` | `int` | 1 | 現在のプレイヤーレベルの値。 |
| Total Experience Amount Limit | `totalExperienceAmountLimit` | `int` | 9999999 | 累計経験値の上限値。超えると頭打ちになる。 |
| Experience Text Movement Speed | `experienceTextMovementSpeed` | `float` | – | 獲得経験値テキストが移動する速さ。 |
| Experience Text Movement Delay | `experienceTextMovementDelay` | `float` | – | テキストが移動を始めるまでの遅延秒数。 |
| Play Sound On Level Up Enabled | `playSoundOnLevelUpEnabled` | `bool` | true | ONにするとレベルアップ時に効果音を再生する。 |
| Time To Show Level Up Panel | `timeToShowLevelUpPanel` | `float` | – | レベルアップパネルを表示しておく秒数。 |
| Experience Amount Text Offset | `experienceAmountTextOffset` | `float` | – | 画面外テキストを画面端へ寄せる位置の比率。 / Range (0, 1) |
| Use Max Level | `useMaxLevel` | `bool` | – | ONにすると到達できる最大レベルを制限する。 |
| Max Level | `maxLevel` | `int` | – | レベルアップできる上限のレベル値。 |
| Hide Experience Slider After Time | `hideExperienceSliderAfterTime` | `bool` | – | ONにすると経験値スライダーを一定時間後に隠す。 |
| Time To Hide Experience Slider | `timeToHideExperienceSlider` | `float` | – | スライダーを隠すまでの表示秒数。 |
| Experience Menu Active | `experienceMenuActive` | `bool` | true | ONにすると経験値メニューを開く入力を受け付ける。 |
| Call Event On Level Reached On Load Enabled | `callEventOnLevelReachedOnLoadEnabled` | `bool` | true | ONにするとロード時に到達済みレベルのイベントを呼ぶ。 |
| Current Experience Multiplier | `currentExperienceMultiplier` | `float` | 1 | 獲得経験値に掛ける現在の倍率。 |
| Experience Multipler Enabled | `experienceMultiplerEnabled` | `bool` | – | 経験値倍率が現在有効かどうかの状態。 |
| Extra Text On Level Number | `extraTextOnLevelNumber` | `string` | "LV " | レベル表示の前に付ける文字列。 |
| Extra Text On New Level Number | `extraTextOnNewLevelNumber` | `string` | "LV " | レベルアップ表示の前に付ける文字列。 |
| Total Experience Points Name | `totalExperiencePointsName` | `string` | "Skill Points" | スキルポイントを保存するステータス名。 |
| Total Experience Amount Name | `totalExperienceAmountName` | `string` | "Experience" | 累計経験値を保存するステータス名。 |
| Current Level Experience Amount Name | `currentLevelExperienceAmountName` | `string` | "Current Level Experience Amount" | 現在レベル経験値を保存するステータス名。 |
| Current Level Experience To Next Level Name | `currentLevelExperienceToNextLevelName` | `string` | "Current Level Experience To Next Lev… | 次レベル必要経験値を保存するステータス名。 |
| Current Level Name | `currentLevelName` | `string` | "Level" | 現在レベルを保存するステータス名。 |
| Set Level Manually | `setLevelManually` | `bool` | – | ONにすると開始時のレベルを手動設定値から決める。 |
| XP Extra String | `XPExtraString` | `string` | " XP" | 獲得経験値テキストの末尾に付ける文字列。 |
| Menu Panel Name | `menuPanelName` | `string` | "Experience System" | ポーズ管理に登録するメニューの識別名。 |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Experience Multipler Enabled | `eventOnExperienceMultiplerEnabled` | `UnityEvent` | – | 経験値倍率が有効になった時に呼ばれるイベント。 / 表示条件: `showEventSettings` がオンのとき |
| Event On Experience Multipler Disabled | `eventOnExperienceMultiplerDisabled` | `UnityEvent` | – | 経験値倍率が終了した時に呼ばれるイベント。 / 表示条件: `showEventSettings` がオンのとき |
| Event On Experience Without Text Position | `eventOnExperienceWithoutTextPosition` | `eventParameters.eventToCallWithString` | – | テキスト位置未設定時に経験値文字列を渡すイベント。 / 表示条件: `showEventSettings` がオンのとき |
| Event On Experience Menu Opened | `eventOnExperienceMenuOpened` | `UnityEvent` | – | 経験値メニューを開いた時に呼ばれるイベント。 / 表示条件: `showEventSettings` がオンのとき |
| Event On Experience Menu Closed | `eventOnExperienceMenuClosed` | `UnityEvent` | – | 経験値メニューを閉じた時に呼ばれるイベント。 / 表示条件: `showEventSettings` がオンのとき |
| Use Event If System Disabled | `useEventIfSystemDisabled` | `bool` | – | ONにするとシステム無効時に専用イベントを呼ぶ。 / 表示条件: `showEventSettings` がオンのとき |
| Event If System Disabled | `eventIfSystemDisabled` | `UnityEvent` | – | 経験値システムが無効な時に呼ばれるイベント。 / 表示条件: `showEventSettings && useEventIfSystemDisabled.boolValue` |

### Main Component Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Skill Manager | `playerSkillManager` | `playerSkillsSystem` | – | スキル解放を処理するスキル管理コンポーネント。 / 表示条件: `showElementSettings` がオンのとき |
| Player Stats Manager | `playerStatsManager` | `playerStatsSystem` | – | 経験値やレベルをステータスとして反映する参照。 / 表示条件: `showElementSettings` がオンのとき |
| Main Camera | `mainCamera` | `Camera` | – | 経験値テキストの画面座標計算に使うカメラ。 / 表示条件: `showElementSettings` がオンのとき |
| Pause Manager | `pauseManager` | `menuPause` | – | 経験値メニューの開閉とポーズを制御する参照。 / 表示条件: `showElementSettings` がオンのとき |
| Level Up Audio Source | `levelUpAudioSource` | `AudioSource` | – | レベルアップ音を再生するオーディオソース。 / 表示条件: `showElementSettings` がオンのとき |
| Level Up Audio Clip | `levelUpAudioClip` | `AudioClip` | – | レベルアップ時に再生するオーディオクリップ。 / 表示条件: `showElementSettings` がオンのとき |
| Level Up Audio Element | `levelUpAudioElement` | `AudioElement` | – | レベルアップ音を再生するオーディオ要素。 / 表示条件: `showElementSettings` がオンのとき |
| Current Level Text | `currentLevelText` | `Text` | – | 現在レベルを表示するUIテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Level Up Panel | `levelUpPanel` | `GameObject` | – | レベルアップ時に表示するパネル。 / 表示条件: `showElementSettings` がオンのとき |
| Level Up Text | `levelUpText` | `Text` | – | レベルアップ後のレベルを表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Experience Text Target Position | `experienceTextTargetPosition` | `RectTransform` | – | 獲得経験値テキストが移動する目標位置。 / 表示条件: `showElementSettings` がオンのとき |
| Experience Slider Transform | `experienceSliderTransform` | `RectTransform` | – | 経験値テキストの移動距離計算に使う位置。 / 表示条件: `showElementSettings` がオンのとき |
| Experience Slider | `experienceSlider` | `Slider` | – | 現在レベル経験値を表示するスライダー。 / 表示条件: `showElementSettings` がオンのとき |
| Experience Slider Panel | `experienceSliderPanel` | `GameObject` | – | 経験値スライダーをまとめたパネル。 / 表示条件: `showElementSettings` がオンのとき |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | 経験値メニュー操作時に状態を参照するプレイヤー。 / 表示条件: `showElementSettings` がオンのとき |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | メインカメラを取得するためのプレイヤーカメラ。 / 表示条件: `showElementSettings` がオンのとき |
| Experience Menu Game Object | `experienceMenuGameObject` | `GameObject` | – | 経験値メニューとして開閉するゲームオブジェクト。 / 表示条件: `showElementSettings` がオンのとき |
| Experience Obtanied Text Prefab | `experienceObtaniedTextPrefab` | `GameObject` | – | 獲得経験値テキストを生成するプレハブ。 / 表示条件: `showElementSettings` がオンのとき |
| Experience Obtained Text Parent | `experienceObtainedTextParent` | `Transform` | – | 獲得経験値テキストを配置する親要素。 / 表示条件: `showElementSettings` がオンのとき |
| Experience Multiplier Text Panel | `experienceMultiplierTextPanel` | `GameObject` | – | 経験値倍率を表示するパネル。 / 表示条件: `showElementSettings` がオンのとき |
| Experience Multipler Text | `experienceMultiplerText` | `Text` | – | 現在の経験値倍率を表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Experience Slider Panel Position Inside Menu | `experienceSliderPanelPositionInsideMenu` | `Transform` | – | メニュー内でスライダーパネルを置く位置。 / 表示条件: `showElementSettings` がオンのとき |
| Experience Slider Panel Position Outside Menu | `experienceSliderPanelPositionOutsideMenu` | `Transform` | – | メニュー外でスライダーパネルを置く位置。 / 表示条件: `showElementSettings` がオンのとき |
| Stats Menu Panel | `statsMenuPanel` | `GameObject` | – | ステータス一覧を表示するメニューパネル。 / 表示条件: `showElementSettings` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `levelInfoList` | `List<levelInfo>` | new List<levelInfo> () | – |
| `statUIInfoList` | `List<statUIInfo>` | new List<statUIInfo> () | – |
| `experienceMenuOpened` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkEventOnSystemDisabled()` | `useEventIfSystemDisabled`が有効な時だけ`eventIfSystemDisabled`を発火する。 |
| `checkIncreasePlayerLevel()` | 現在レベル経験値が必要量以上ならレベルを上げ、ステータス加算とスキル解放を行って`true`を返す。 |
| `getExperienceAmount(int newExperienceAmount)` | システムが無効なら何もせず、有効な時は位置指定なしの経験値取得処理を呼び出すだけ。 |
| `getExperienceAmount(int newExperienceAmount, Transform objectTransform, bool useTransformAsExpTextPosition, string extraExperienceText)` | 経験値に倍率を掛けて加算し、連続レベルアップを判定して、`objectTransform`位置に取得テキストを出す。 |
| `updateExperienceInfo()` | スライダーの最大値を次レベル必要経験値、値を現在経験値に設定し、レベル表示も更新する。 |
| `showLevelUpPanel()` | 既存の表示コルーチンを止めてから、レベルアップパネルを一定時間表示するコルーチンを開始する。 |
| `stopShowLevelUpPanelCoroutine()` | レベルアップパネル表示用コルーチンが存在すれば停止するだけ。 |
| `showExperienceSlider()` | 既存のコルーチンを止め、経験値スライダーを一定時間後に隠すコルーチンを開始する。 |
| `stopShowExperienceSliderCoroutine()` | 経験値スライダーの自動非表示コルーチンが存在すれば停止するだけ。 |
| `openOrCloseExperienceMenu(bool state)` | メニュー使用可否を確認し、経験値メニューの開閉とポーズ状態、スライダーの親と表示を切り替える。 |
| `enableOrDisableHUD(bool state)` | `hideExperienceSliderAfterTime`が無効な時だけ、経験値スライダーの表示を`state`に合わせる。 |
| `openOrCLoseObjectiveMenuFromTouch()` | 経験値メニューの開閉状態を反転して`openOrCloseExperienceMenu`を呼ぶだけ。 |
| `inputOpenOrCloseObjectiveMenu()` | `experienceMenuActive`の時、メニュー入力が停止中でなければ経験値メニューを開閉する。 |
| `updateStatsInfo()` | `statUIInfoList`の各項目に、数値または真偽値のステータスを前後テキスト付きで表示する。 |
| `initializeCurrentLevelExperienceAmount(float newValue)` | 現在レベル経験値を`newValue`の整数値に設定し、コンポーネントを更新する。 |
| `initializeTotalExperienceAmount(float newValue)` | 累計経験値`totalExperienceAmount`を`newValue`の整数値に設定して更新する。 |
| `initializeTotalExperiencePointsAmount(float newValue)` | スキルポイント`totalExperiencePoints`を`newValue`の整数値に設定して更新する。 |
| `initializeCurrentLevelAmount(float newValue)` | 現在レベルを`newValue`の整数値に設定し、コンポーネントを更新する。 |
| `increaseTotalExperiencePointsAmount(float extraValue)` | スキルポイントに`extraValue`の整数値を加算するだけ。 |
| `increaseTotalExperienceAmount(float extraValue)` | 累計経験値に、`extraValue`へ経験値倍率を掛けた整数値を加算する。 |
| `initializeCurrentLevelExperienceToNextLevelAmount(float newValue)` | 次レベルまでの必要経験値を`newValue`の整数値に設定して更新する。 |
| `updateCurrentLevelAmountWithoutUpdatingStatManager(int statId, float amount)` | StatManager更新用のコールバックで、`statId`を無視して現在レベルだけを設定する。 |
| `updateTotalExperiencePointsAmountWithoutUpdatingStatManager(int statId, float amount)` | `statId`を無視し、スキルポイントだけを`amount`の整数値に設定する。 |
| `updateTotalExperienceAmountWithoutUpdatingStatManager(int statId, float amount)` | `statId`を無視し、累計経験値だけを`amount`の整数値に設定する。 |
| `updateCurrentLevelExperienceToNextLevelAmountWithoutUpdatingStatManager(int statId, float amount)` | `statId`を無視し、次レベル必要経験値だけを`amount`の整数値に設定する。 |
| `updateCurrentLevelExperienceAmountWithoutUpdatingStatManager(int statId, float amount)` | `statId`を無視し、現在レベル経験値だけを`amount`の整数値に設定する。 |
| `getCurrentLevel()` | 現在レベルを返すだけ。 |
| `getSkillPointsAmount()` | スキルポイントとして扱う`totalExperiencePoints`を返すだけ。 |
| `useSkillPoints(int amountToUse)` | スキルポイントを`amountToUse`分減らし、0未満なら0に戻してStatManagerと表示を更新する。 |
| `getSkillPoints(int amountToUse)` | スキルポイントを`amountToUse`分加算し、StatManagerの値を更新する。 |
| `setExperienceMultiplier(float experienceMultiplierAmount, float experienceMultiplierDuration)` | 倍率コルーチンを止め、指定倍率を指定秒数だけ適用するコルーチンを開始する。 |
| `stopSetExperienceMultiplier()` | 経験値倍率のコルーチンが存在すれば停止するだけ。 |
| `enableOrDisableStatsMenuPanel(bool state)` | ステータスメニューパネルの表示を`state`に合わせるだけ。 |
| `setExperienceSystemEnabledState(bool state)` | 経験値システムの有効フラグ`experienceSystemEnabled`を設定するだけ。 |
| `setHideExperienceSliderAfterTimeState(bool state)` | スライダーを時間で隠す設定`hideExperienceSliderAfterTime`を切り替えるだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnExperienceMultiplerEnabled` | `UnityEvent` | – |
| `eventOnExperienceMultiplerDisabled` | `UnityEvent` | – |
| `eventOnExperienceMenuOpened` | `UnityEvent` | – |
| `eventOnExperienceMenuClosed` | `UnityEvent` | – |
| `eventIfSystemDisabled` | `UnityEvent` | – |

## 内部型

- `levelInfo`（class）
- `statInfo`（class）
- `experienceObtainedInfo`（class）
- `statUIInfo`（class）
