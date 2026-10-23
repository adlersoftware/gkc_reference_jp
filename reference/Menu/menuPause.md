# menuPause

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Menu/menuPause.cs:9`

**概要**: ポーズ・ポーズメニュー・プレイヤーメニューを一元管理する中心コンポーネント。時間停止、カーソルとカメラ、HUD、タッチ操作、ブラー、各イベントの発火をまとめて切り替える。

**公式ドキュメント抜粋**（[Menu Pause](../../docs/character-level-components/character/menu-pause.md)）

> It is used to manage the main pause menu and ingame menus, allowing to add new ones (like inventory, map, mission log, etc…)

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Menu Pause Enabled | `menuPauseEnabled` | `bool` | – | – |
| Activate Death Menu When Playe Dies | `activateDeathMenuWhenPlayeDies` | `bool` | true | – |
| Close Only Sub Menu If Open On Escape | `closeOnlySubMenuIfOpenOnEscape` | `bool` | – | – |
| Scene Number For Home Menu | `sceneNumberForHomeMenu` | `int` | 0 | – |
| Save Game Automatically On Return To Home | `saveGameAutomaticallyOnReturnToHome` | `bool` | – | – |
| Pause Audio Listener On Game Paused | `pauseAudioListenerOnGamePaused` | `bool` | true | – |
| Time Scale On Game Paused | `timeScaleOnGamePaused` | `float` | 0 | – |
| Ignore Change Fixed Delta Time | `ignoreChangeFixedDeltaTime` | `bool` | – | – |
| Pause AI When Pause Menu Opened | `pauseAIWhenPauseMenuOpened` | `bool` | – | – |
| Pause Character Priority | `pauseCharacterPriority` | `int` | 1 | – |
| Ignore Select UI On Gamepad On UI Navigation | `ignoreSelectUIOnGamepadOnUINavigation` | `bool` | – | – |

### Fade Black Screen On Start Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fade Screen Active | `fadeScreenActive` | `bool` | true | – |
| Fade Screen Speed | `fadeScreenSpeed` | `float` | 2 | – |

### Canvas Group Menu Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Canvas Group | `useCanvasGroup` | `bool` | – | – |
| Fade On Panel Speed | `fadeOnPanelSpeed` | `float` | – | – |
| Fade Off Panel Speed | `fadeOffPanelSpeed` | `float` | – | – |

### Menu Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Submene Info List | `submeneInfoList` | `List<submenuInfo>` | new List<submenuInfo> () | – |
| Player Menu Info List | `playerMenuInfoList` | `List<playerMenuInfo>` | new List<playerMenuInfo> () | – |
| Ingame Menu Info List | `ingameMenuInfoList` | `List<ingameMenuInfo>` | new List<ingameMenuInfo> () | – |
| Use Default Player Menu Name To Open | `useDefaultPlayerMenuNameToOpen` | `bool` | – | – |
| Default Player Menu Name To Open | `defaultPlayerMenuNameToOpen` | `string` | – | – |
| Default Player Menu Input Enabled | `defaultPlayerMenuInputEnabled` | `bool` | true | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Between Menus Input Enabled | `changeBetweenMenusInputEnabled` | `bool` | true | – |
| Main Pause Menu Name | `mainPauseMenuName` | `string` | "Pause Menu" | – |
| Main Death Menu Name | `mainDeathMenuName` | `string` | "Die Menu" | – |

### Load Screen Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Load Screen | `useLoadScreen` | `bool` | – | – |
| Load Screen Scene | `loadScreenScene` | `int` | 1 | – |
| Use Last Scene Index As Load Screen | `useLastSceneIndexAsLoadScreen` | `bool` | true | – |
| Scene To Load Async Prefs Name | `sceneToLoadAsyncPrefsName` | `string` | "SceneToLoadAsync" | – |
| Check Loading Screen Scene Configured | `checkLoadingScreenSceneConfigured` | `bool` | true | – |
| Loading Screen Scene Name | `loadingScreenSceneName` | `string` | "Loading Screen Scene" | – |

### Restart Game Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Scene Index On Restart Game | `useCustomSceneIndexOnRestartGame` | `bool` | – | – |
| Custom Scene Index On Restart Game | `customSceneIndexOnRestartGame` | `int` | – | – |

### Touch Zone List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Touch Zone List | `touchZoneList` | `List<GameObject>` | new List<GameObject> () | – |

### Help Menu Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Input Help Menu Enabled | `inputHelpMenuEnabled` | `bool` | – | – |
| Input Help Menu Game Object | `inputHelpMenuGameObject` | `GameObject` | – | – |

### Mechanic Menu Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Mechanics Help Menu Enabled | `mechanicsHelpMenuEnabled` | `bool` | – | – |
| Mechanics Help Menu Game Object | `mechanicsHelpMenuGameObject` | `GameObject` | – | – |

### Blur Background Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Blur Panel Enabled | `blurPanelEnabled` | `bool` | true | – |
| Use Blur UI Panel On Player Menu | `useBlurUIPanelOnPlayerMenu` | `bool` | – | – |
| Use Blur UI Panel On Pause | `useBlurUIPanelOnPause` | `bool` | – | – |
| Blur UI Panel | `blurUIPanel` | `GameObject` | – | – |
| Blur UI Panel Material | `blurUIPanelMaterial` | `Material` | – | – |
| Blur UI Panel Image | `blurUIPanelImage` | `Image` | – | – |
| Blur UI Panel Value | `blurUIPanelValue` | `float` | 4.4f | – |
| Blur UI Panel Speed | `blurUIPanelSpeed` | `float` | 10 | – |
| Blur UI Panel Alpha Speed | `blurUIPanelAlphaSpeed` | `float` | 10 | – |
| Blur UI Panel Alpha Value | `blurUIPanelAlphaValue` | `float` | 120 | – |
| Blur UI Panel Parent | `blurUIPanelParent` | `Transform` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Enable Or Disable All Player HUD | `eventToEnableOrDisableAllPlayerHUD` | `eventParameters.eventToCallWithBool` | – | – |
| Event To Enable Or Disable Secondary Player HUD | `eventToEnableOrDisableSecondaryPlayerHUD` | `eventParameters.eventToCallWithBool` | – | – |
| Event To Enable Or Disable All Vehicle HUD | `eventToEnableOrDisableAllVehicleHUD` | `eventParameters.eventToCallWithBool` | – | – |
| Use Events On Pause Resume | `useEventsOnPauseResume` | `bool` | – | – |
| Event On Pause Game | `eventOnPauseGame` | `UnityEvent` | – | – |
| Event On Resume Game | `eventOnResumeGame` | `UnityEvent` | – | – |
| Use Event On Open Close Ingame Menu | `useEventOnOpenCloseIngameMenu` | `bool` | – | – |
| Event On Open Ingame Menu | `eventOnOpenIngameMenu` | `UnityEvent` | – | – |
| Event On Close Ingame Menu | `eventOnCloseIngameMenu` | `UnityEvent` | – | – |

### Menu Pause Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Canvas Info List | `canvasInfoList` | `List<canvasInfo>` | new List<canvasInfo> () | – |

### Pause Manager State/Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Cursor State | `cursorState` | `cursorStateInfo` | – | – |
| Current Player Menu Info Index | `currentPlayerMenuInfoIndex` | `int` | – | – |
| Game Paused | `gamePaused` | `bool` | false | – |
| Sub Menu Active | `subMenuActive` | `bool` | – | – |
| Using Sub Menu | `usingSubMenu` | `bool` | – | – |
| Player Menu Active | `playerMenuActive` | `bool` | – | – |
| Use Touch Controls | `useTouchControls` | `bool` | false | – |
| Using Touch Controls Previously | `usingTouchControlsPreviously` | `bool` | – | – |
| Using Device | `usingDevice` | `bool` | – | – |
| Dead | `dead` | `bool` | – | – |
| Ignore Change HUD Elements | `ignoreChangeHUDElements` | `bool` | – | – |
| Ignore Disable Touch Zone List | `ignoreDisableTouchZoneList` | `bool` | – | – |
| Pause Game Input Paused | `pauseGameInputPaused` | `bool` | – | – |
| Change Between Ingame Menu Paused | `changeBetweenIngameMenuPaused` | `bool` | – | – |
| Open Or Close Player Open Menu By Name Paused | `openOrClosePlayerOpenMenuByNamePaused` | `bool` | – | – |
| Regular Time Scale Active | `regularTimeScaleActive` | `bool` | true | – |
| Open Or Close Pause Menu Externally Paused | `openOrClosePauseMenuExternallyPaused` | `bool` | – | – |
| Open Menu System Assigned | `openMenuSystemAssigned` | `bool` | – | – |
| Previous Menu Using UI Navigation Active | `previousMenuUsingUINavigationActive` | `bool` | – | – |
| Ignore Blur Panel Active | `ignoreBlurPanelActive` | `bool` | – | – |
| Ignore Show Or Hide Mouse Cursor And Pause Hide Check On Click Externally | `ignoreShowOrHideMouseCursorAndPauseHideCheckOnClickExternally` | `bool` | – | – |
| Menu Opened With Action System Active | `menuOpenedWithActionSystemActive` | `bool` | – | – |
| Menu Opened With Action System Name | `menuOpenedWithActionSystemName` | `string` | – | – |

### UI Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hud And Menus | `hudAndMenus` | `GameObject` | – | – |
| Touch Panel | `touchPanel` | `GameObject` | – | – |
| Pause Menu | `pauseMenu` | `GameObject` | – | – |
| Pause Menu Parent | `pauseMenuParent` | `Transform` | – | – |
| Die Menu | `dieMenu` | `GameObject` | – | – |
| Black Bottom Image | `blackBottomImage` | `Image` | – | – |
| Dynamic UI Elements Parent | `dynamicUIElementsParent` | `GameObject` | – | – |
| Main Canvas | `mainCanvas` | `Canvas` | – | – |
| Main Canvas Rect Transform | `mainCanvasRectTransform` | `RectTransform` | – | – |
| Main Canvas Scaler | `mainCanvasScaler` | `CanvasScaler` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Game Manager | `mainGameManager` | `gameManager` | – | – |
| Player Input | `playerInput` | `playerInputManager` | – | – |
| Main Player HUD Manager | `mainPlayerHUDManager` | `playerHUDManager` | – | – |
| Main Canvas Camera | `mainCanvasCamera` | `Camera` | – | – |
| Input | `input` | `inputManager` | – | – |
| Time Manager | `timeManager` | `timeBullet` | – | – |
| Main Weapons Manager | `mainWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Player Health Bar Manager | `mainPlayerHealthBarManager` | `playerHealthBarManagementSystem` | – | – |
| Player Screen Objectives Manager | `playerScreenObjectivesManager` | `playerScreenObjectivesSystem` | – | – |
| Main Player Pickup Icon Manager | `mainPlayerPickupIconManager` | `playerPickupIconManager` | – | – |
| Mouse Cursor Controller Manager | `mouseCursorControllerManager` | `mouseCursorController` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | – |
| Edit Control Position Manager | `editControlPositionManager` | `editControlPosition` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateFadePanelBackgroundIn()` | 黒背景`blackBottomImage`をalpha 1で有効化し、`fadeScreenActive`を立てて方向-1のフェードを開始する。 |
| `activateFadePanelBackgroundOut()` | 黒背景をalpha 0で有効化し、`externalFadeScreenActive`を立ててalpha 1へ向かう外部フェードを開始する。 |
| `deactivateFadePanelBackground()` | 黒背景をalpha 0で非表示にし、`fadeScreenActive`と`externalFadeScreenActive`を下ろす。 |
| `setCustomFadeScreenSpeed(float newValue)` | フェード画面の速度`fadeScreenSpeed`に`newValue`を設定するだけ。 |
| `disableMenuList()` | 全サブメニューを非アクティブ化し、開いていたものは`menuOpened`を下ろして`eventOnClose`を発火する。 |
| `setOpenOrClosePauseMenuExternallyPausedState(bool state)` | 外部からのポーズメニュー操作を止める`openOrClosePauseMenuExternallyPaused`を設定するだけ。 |
| `openPauseMenuByName(string menuName)` | `openOrClosePauseMenuExternallyPaused`が真なら何もせず、そうでなければ指定名のポーズメニューを開く。 |
| `closePauseMenuByName(string menuName)` | `openOrClosePauseMenuExternallyPaused`が真なら何もせず、そうでなければ指定名のポーズメニューを閉じる。 |
| `openOrClosePauseMenuByName(string menuName, bool state)` | 指定名のポーズメニューを開閉し、他メニューを閉じて開閉イベントとゲームパッド選択、サブメニュー状態を更新する。 |
| `setPauseScreenWithoutPausingGameState(bool state)` | 時間停止はせずにポーズ画面だけを切り替え、カーソル・カメラ・入力・ブラー・各マネージャのポーズ状態を更新する。 |
| `inGameWindowOpened()` | デバイス未使用かつポイント&クリックでなく、開いているインゲームメニューが無ければtrueを返す。 |
| `getIngameMenuPanelByName(string menueName)` | 指定名のインゲームメニューに割り当てられた`ingameMenuPanel`を返し、無ければnullを返す。 |
| `setIngameMenuOpenedState(string ingameMenuName, bool state, bool activateEvents)` | 指定メニューの`menuOpened`を更新し、開閉イベント・パネルのフェード・時間スケール・AI停止・カーソル速度を反映する。 |
| `fadeInGameMenuPanel(ingameMenuInfo newIngameMenuInfo, bool fadingPanel)` | `useCanvasGroup`時のみ、既存コルーチンを止めてメニューパネルのalphaをフェードするコルーチンを開始する。 |
| `checkTouchControlsWithoutDisableThem(bool state)` | タッチ操作が以前有効だった場合に限り、`playerInput`の操作タイプを切り替え、有効化時はカーソルも表示する。 |
| `enableOrDisableTouchControlsExternally(bool state)` | `playerInput`のタッチ操作を外部から有効/無効にするだけ。 |
| `enableOrDisablePlayerMenu(bool state, bool pausePlayerMovement, bool ignoreActionActiveCheck)` | プレイヤーメニューの開閉に伴い、カーソル・タッチ操作・カメラ・移動可否・HUD・タッチゾーンをまとめて切り替える。 |
| `checkEnableOrDisableTouchZoneList(bool state)` | `ignoreDisableTouchZoneList`が偽か有効化時のみ、タッチゾーン一覧のアクティブ状態を揃える。 |
| `setIgnoreDisableTouchZoneListState(bool state)` | `ignoreDisableTouchZoneList`を設定するだけ。 |
| `usingDeviceState(bool state)` | デバイス使用中フラグ`usingDevice`を設定するだけ。 |
| `usingPointAndClickState(bool state)` | ポイント&クリック使用中フラグ`usingPointAndClick`を設定するだけ。 |
| `usingSubMenuState(bool state)` | `usingSubMenu`を設定し、`playerControllerManager`にもサブメニュー状態を通知する。 |
| `pauseGame()` | サブメニュー表示中ならメインポーズメニューへ戻し、そうでなければ`pause`を呼び、タッチボタン編集や入力編集も終了する。 |
| `setMenuPausedState(bool state)` | 親がアクティブな時だけ`gamePaused`を`state`の否定に設定し、ゲームマネージャ経由のフラグを立てて`pause`を呼ぶ。 |
| `pause()` | `gamePaused`を反転し、時間スケール・ポーズパネル・カーソル・カメラ・入力・ブラー・各種イベントを一括で切り替える。 |
| `checkEventOnPauseResumeGame(bool state)` | `useEventsOnPauseResume`が有効ならポーズ/再開イベントを発火するだけ。 |
| `checkEventOnOpenCloseInGameMenu(bool state)` | `useEventOnOpenCloseIngameMenu`が有効ならメニュー開閉イベントを発火するだけ。 |
| `setTimeScale(float newValue)` | `Time.timeScale`を設定し、固定差分時間も更新して`regularTimeScaleActive`を`newValue`が1かで更新する。 |
| `getTimeTime()` | 時間スケールが通常なら`Time.time`、それ以外は`Time.unscaledTime`を返す。 |
| `getDeltaTime()` | 時間スケールが通常なら`Time.deltaTime`、それ以外は`Time.unscaledDeltaTime`を返す。 |
| `isRegularTimeScaleActive()` | `regularTimeScaleActive`を返すだけ。 |
| `setMouseButtonPressPausedState(bool state)` | マウスボタン押下のポーズフラグ`mouseButtonPressPaused`を設定するだけ。 |
| `showOrHideMouseCursorController(bool state)` | `mouseCursorControllerManager`にカーソルコントローラの表示/非表示を依頼する。 |
| `showOrHideMouseCursorController(playerInputManager newInput, bool state, bool pausingGame)` | 指定の`playerInputManager`とポーズ有無を添えて、カーソルコントローラの表示/非表示を依頼する。 |
| `setMouseCursorControllerSpeedOnGameValue(float newValue)` | `mouseCursorControllerManager`にゲーム中のカーソル速度`newValue`を設定させる。 |
| `setOriginalMouseCursorControllerSpeedOnGameValue()` | `mouseCursorControllerManager`にカーソル速度を元の値へ戻させる。 |
| `showOrHideCursor(bool value)` | タッチ操作などの状態を考慮しつつカーソルのロックと表示を切り替え、現在/以前の状態と最終変更時刻を記録する。 |
| `setIgnoreHideCursorOnClickActiveState(bool state)` | `ignoreHideCursorOnClickActive`を設定するだけ。 |
| `showOrHideMouseCursorAndPauseHideCheckOnClickExternally(bool state)` | 無視フラグが立っていなければ、カーソルとコントローラの表示を切り替え、クリック時の非表示チェックも止める。 |
| `checkTouchControls(bool state)` | タッチ操作が以前有効だった場合にタッチ操作を切り替え、有効化時はカーソルを表示する。 |
| `updateTouchButtonsComponents()` | `editControlPositionManager`にタッチボタン構成の再取得を依頼する。 |
| `setIgnoreCheckCloseIngameMenusIfOpenedState(bool state)` | `ignoreCheckCloseIngameMenusIfOpened`を設定するだけ。 |
| `checkCloseIngameMenusIfOpened()` | プレイヤーメニュー表示中なら、開いている全インゲームメニューの閉鎖イベントを発火しパネルを閉じる。 |
| `setMenuOpenedWithActionSystemState(bool state, string menuName)` | アクションシステムで開いたメニューのフラグと名前を保存するだけ。 |
| `checkCloseMenuOpenedByActionSystem()` | プレイヤーメニューとアクション開示フラグが立っていれば、アクション中のアニメーション再生を要求する。 |
| `setIgnoreDeathStateOnMenuPauseState(bool state)` | 死亡時のメニュー処理を無視する`ignoreDeathStateOnMenuPauseState`を設定するだけ。 |
| `death()` | `dead`を立て、死亡メニューの表示・カーソル・カメラ・マウス制御を死状態に切り替える。 |
| `getUp()` | `dead`を下ろし、死亡メニューを閉じてカーソルとカメラを通常状態へ戻す。 |
| `restart()` | `pause`を呼んだ後、現在または指定のシーンインデックスでシーンを再読み込みする。 |
| `changeCameraState(bool state)` | デバイス使用中の状態を考慮しつつカメラを一時停止/再開し、現在と以前のカメラ状態を保存する。 |
| `changeCursorState(bool state)` | カメラ状態の記録だけを更新し、デバイス使用中なら以前の状態を有効扱いに補正する。 |
| `openOrClosePlayerMenu(bool state, Transform blurUIParent, bool useBlurUIPanel)` | `playerMenuActive`を設定して各マネージャへ通知し、条件を満たせばブラーパネルを切り替える。 |
| `openPlayerMenuWithBlurPanel(Transform blurUIParent)` | 最終移動時刻を更新し、ブラーが有効なら現在の`playerMenuActive`でブラーパネルを切り替える。 |
| `enterSubMenu()` | `showGUI`を偽にし`subMenuActive`を立てるだけ。 |
| `exitSubMenu()` | `showGUI`を真にし`subMenuActive`を下ろすだけ。 |
| `switchControls()` | タッチ操作の使用可否を反転し、操作切替と再ポーズ、ゲームマネージャ・入力への反映を行う。 |
| `enableOrDisableTouchControlsOutOfPauseMenu(bool state)` | ポーズ外から`useTouchControls`を設定し、タッチ操作と関連マネージャへ反映する。 |
| `setUseTouchControlsState(bool state)` | `useTouchControls`を設定するだけ。 |
| `setUseTouchControlsStateFromEditor(bool state)` | `useTouchControls`を設定してから`updateComponent`で更新する。 |
| `setBlurPanelEnabledState(bool state)` | `blurPanelEnabled`を設定するだけ。 |
| `setBlurPanelEnabledStateFromEditor(bool state)` | `blurPanelEnabled`を設定してから`updateComponent`で更新する。 |
| `isUsingTouchControls()` | `useTouchControls`を返すだけ。 |
| `confirmExit()` | `Application.Quit`でゲームを終了するだけ。 |
| `confirmGoToHomeMenu()` | 必要なら自動セーブし、時間スケールを1に戻してからホームメニューのシーンを読み込む。 |
| `enableOrDisableTouchControls(bool state)` | `input`のキーボード操作を、タッチ操作とは逆の状態に設定する。 |
| `reloadStart()` | `Start`を呼び直すだけ。 |
| `setIgnoreBlurPanelActiveState(bool state)` | `ignoreBlurPanelActive`を設定するだけ。 |
| `resetPauseMenuBlurPanel()` | ポーズメニューのブラーパネルを有効状態で再適用する。 |
| `changeBlurUIPanelValue(bool state, Transform blurUIParent, bool useBlurUIPanel)` | 各種フラグを確認し、ブラーパネルの親を付け替えてからブラー値変更コルーチンを開始する。 |
| `checkBlurSizeID()` | `blurSizeID`が未取得ならシェーダープロパティIDを取得する。 |
| `setIgnoreChangeHUDElementsState(bool state)` | `ignoreChangeHUDElements`を設定するだけ。 |
| `enableOrDisableDynamicElementsOnScreen(bool state)` | 体力バー・目標・アイコンの表示を反転させ、動的UI親のアクティブ状態を設定する。 |
| `pauseOrResumeShowHealthSliders(bool state)` | `mainPlayerHealthBarManager`に体力バー表示の一時停止/再開を委譲する。 |
| `pauseOrResumeShowObjectives(bool state)` | `playerScreenObjectivesManager`に目標表示の一時停止/再開を委譲する。 |
| `pauseOrResumeShowIcons(bool state)` | `mainPlayerPickupIconManager`にアイコン表示の一時停止/再開を委譲する。 |
| `enableOrDisableDynamicUIElementsParent(bool state)` | `dynamicUIElementsParent`のアクティブ状態を`state`に設定する。 |
| `enableOrDisableDynamicElementsOnScreenFromEditor(bool state)` | エディタ用の各マネージャ関数で表示を反転し、動的UI親のアクティブ状態を切り替える。 |
| `pauseOrResumeShowHealthSlidersFromEditor(bool state)` | `mainPlayerHealthBarManager`のエディタ用関数に体力バー表示の切替を委譲する。 |
| `pauseOrResumeShowObjectivesFromEditor(bool state)` | `playerScreenObjectivesManager`のエディタ用関数に目標表示の切替を委譲する。 |
| `pauseOrResumeShowIconsFromEditor(bool state)` | `mainPlayerPickupIconManager`のエディタ用関数にアイコン表示の切替を委譲する。 |
| `inputPauseGame()` | 入力側のポーズ禁止やゲームマネージャ由来なら中断し、外部メニューがあれば閉じ、無ければ`pauseGame`を呼ぶ。 |
| `inputReturnPauseGameFromGamepad()` | ゲームパッドの戻る入力で、ポーズ中のみ`pauseGame`を呼ぶ。 |
| `inputOpenPreviousPlayerOpenMenu()` | `changeBetweenMenusInputEnabled`が有効なら前のプレイヤーメニューを開く。 |
| `inputOpenNextPlayerOpenMenu()` | `changeBetweenMenusInputEnabled`が有効なら次のプレイヤーメニューを開く。 |
| `inputOpenOrClosePlayerMenu()` | メニュー切替中やデフォルト入力無効時は何もせず、そうでなければ`openOrClosePlayerMenu`を呼ぶ。 |
| `setPauseGameInputPausedState(bool state)` | ポーズ入力の禁止フラグ`pauseGameInputPaused`を設定するだけ。 |
| `openOrClosePlayerMenu()` | デバイス使用中は中断し、未表示なら使えるメニューを探してから現在メニューのイベントを発火する。 |
| `openNextPlayerOpenMenu()` | 切替中や運転中は中断し、使用可能な次メニューを循環探索してイベントを発火する。 |
| `openPreviousPlayerOpenMenu()` | 切替中や運転中は中断し、使用可能な前メニューを循環探索してイベントを発火する。 |
| `openPlayerOpenMenuByName(string menuName)` | 一時停止中は中断し、名前一致かつ使用可能なメニューを選んでイベントを発火する。 |
| `closePlayerMenuByName(string menuName)` | 一時停止中はアクション由来の終了や外部メニュー閉鎖のみ行い、通常時は該当メニューのイベントを発火する。 |
| `enableCanUsePreviousNextMenuButtonsState(bool state, string menuName)` | 引数`state`は使わず、指定メニューの`canUsePreviousNextMenuButtons`をtrueにする。 |
| `disableCanUsePreviousNextMenuButtonsState(bool state, string menuName)` | 引数`state`は使わず、指定メニューの`canUsePreviousNextMenuButtons`をfalseにする。 |
| `enableOrDisableCanUsePreviousNextMenuButtonsState(bool state, string menuName)` | 指定名のメニューの`canUsePreviousNextMenuButtons`を`state`に設定する。 |
| `checkcreateIngameMenuPanel(string menuName)` | 指定名のインデックスを探し、見つかれば`createIngameMenuPanel`でパネルを生成する。 |
| `setIgnoreCreateIngameMenuPanelState(bool state)` | パネル生成を抑止する`inoreCreateIngameMenuPanel`を設定するだけ。 |
| `setEnabledMenuCanBeUsedState(string menuNameToSearch)` | 指定メニューの`menuCanBeUsed`をtrueにするだけ。 |
| `setDisabledMenuCanBeUsedState(string menuNameToSearch)` | 指定メニューの`menuCanBeUsed`をfalseにするだけ。 |
| `setMenuCanBeUsedState(string menuNameToSearch, bool state)` | 指定メニューの`menuCanBeUsed`を設定し、再生中でなければコンポーネントも更新する。 |
| `checkIfMenuCanBeUsedByName(string menuNameToSearch)` | 指定メニューの`menuCanBeUsed`を返し、見つからなければtrueを返す。 |
| `setOpenOrClosePlayerOpenMenuByNamePausedState(bool state)` | 名前指定のプレイヤーメニュー開閉を止めるフラグを設定するだけ。 |
| `isOpenOrClosePlayerOpenMenuByNamePaused()` | `openOrClosePlayerOpenMenuByNamePaused`を返すだけ。 |
| `setAllowToExitMenuWithTitleMenuTextButtonActiveState(bool state)` | タイトルボタンでのメニュー終了可否フラグを設定するだけ。 |
| `setChangeBetweenIngameMenuPausedState(bool state)` | メニュー切替を禁止する`changeBetweenIngameMenuPaused`を設定するだけ。 |
| `enableOrDisablePlayerHUD(bool state)` | HUD有効/無効イベント`eventToEnableOrDisableAllPlayerHUD`を発火するだけ。 |
| `enableOrDisableSecondaryPlayerHUD(bool state)` | サブHUD有効/無効イベント`eventToEnableOrDisableSecondaryPlayerHUD`を発火するだけ。 |
| `enableOrDisableVehicleHUD(bool state)` | 車両HUD有効/無効イベント`eventToEnableOrDisableAllVehicleHUD`を発火するだけ。 |
| `getMainCanvasSizeDelta()` | `mainCanvasRectTransform`の`sizeDelta`を返すだけ。 |
| `getMainCanvas()` | `mainCanvas`を返すだけ。 |
| `getCanvasInfoList()` | `canvasInfoList`を返すだけ。 |
| `addNewCanvasToList(Canvas newCanvas)` | 未登録ならキャンバス情報を`canvasInfoList`に追加し、再生中でなければ更新する。 |
| `getCanvasInfoListByCanvasObject(Canvas newCanvas)` | 一致するキャンバスの`canvasInfo`を返し、無ければnullを返す。 |
| `isCanvasAlreadyOnInfoList(Canvas newCanvas)` | 同じキャンバスが既に一覧にあればtrueを返す。 |
| `isUsingScreenSpaceCamera()` | メインキャンバスの描画モードが`ScreenSpaceCamera`かどうかを返す。 |
| `getMainCanvasScaler()` | `mainCanvasScaler`を返すだけ。 |
| `getMainCanvasCamera()` | `mainCanvasCamera`を返すだけ。 |
| `setCanvasInfo(bool creatingCharactersOnEditor)` | メインキャンバスのサイズと描画モード、引数を`playerCameraManager`に渡す。 |
| `getMainCameraTransform()` | `playerCameraManager`のメインカメラのTransformを返す。 |
| `checkUpdateReticleActiveState(bool state)` | `playerCameraManager`に照準更新の有効/無効を委譲する。 |
| `isMenuPaused()` | `gamePaused`を返すだけ。 |
| `isGamePaused()` | `mainGameManager`にゲームポーズ状態を問い合わせて返す。 |
| `isLoadGameEnabled()` | `mainGameManager`にロード可否を問い合わせて返す。 |
| `isPlayerMenuActive()` | `playerMenuActive`を返すだけ。 |
| `saveGameInfoFromEditor(string saveInfoName)` | `mainGameManager`にエディタからのセーブ情報保存を`saveInfoName`で依頼する。 |
| `setGameVolume(float newValue)` | `AudioListener.volume`に`newValue`を設定するだけ。 |
| `setSelectedUIGameObject(GameObject newGameObject)` | 既存コルーチンを止め、次フレームでUI選択を設定するコルーチンを開始する。 |
| `isUsingGamepad()` | `input`にゲームパッド使用中かを問い合わせて返す。 |
| `setCurrentOpenMenuSystem(openMenuSystem newOpenMenuSystem)` | 外部メニューシステムを保持し、nullでないかで`openMenuSystemAssigned`を更新する。 |
| `setHeadBobPausedState(bool state)` | `playerControllerManager`にヘッドボブの一時停止状態を設定させる。 |
| `getPlayerControllerGameObject()` | `playerControllerManager`のゲームオブジェクトを返す。 |
| `getHudAndMenus()` | `hudAndMenus`を返すだけ。 |
| `setAnimatorUnscaledTimeState(bool state)` | `playerControllerManager`にアニメータの非スケール時間使用を設定させる。 |
| `getCurrentIdleID()` | `playerControllerManager`から現在のアイドルIDを取得して返す。 |
| `setCurrentIdleIDValue(float animatorIdle)` | `playerControllerManager`にアイドルID値`animatorIdle`を設定させる。 |
| `updateIdleIDOnAnimator()` | `playerControllerManager`にアニメータ上のアイドルID更新を依頼する。 |
| `setUsingDeviceState(bool state)` | `playerControllerManager`にデバイス使用状態を設定させる。 |
| `stopEditorOrGame()` | エディタなら再生を停止し、ビルドでは`confirmExit`でゲームを終了する。 |
| `updateComponent()` | `GKC_Utils`でコンポーネントとシーンのダーティ更新を行う。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static void setCursorLockState(bool state)` | – |
| `static void setCursorVisibleState(bool state)` | – |
| `static bool isCursorVisible()` | – |
| `static UnityEngine.SceneManagement.Scene getCurrentActiveScene()` | – |
| `static int getCurrentActiveSceneIndex()` | – |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnPauseGame` | `UnityEvent` | – |
| `eventOnResumeGame` | `UnityEvent` | – |
| `eventOnOpenIngameMenu` | `UnityEvent` | – |
| `eventOnCloseIngameMenu` | `UnityEvent` | – |

## 内部型

- `cursorStateInfo`（class）
- `submenuInfo`（class）
- `playerMenuInfo`（class）
- `ingameMenuInfo`（class）
- `canvasInfo`（class）
