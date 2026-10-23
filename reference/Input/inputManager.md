# inputManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Input/inputManager.cs:18`
- **属性**: `System.Serializable`

**概要**: GKCの全入力を一元管理するMonoBehaviourで、アクショングループ(`multiAxes`)ごとにキーボード・ゲームパッド・タッチの割り当てを保持する。リバインドUIの生成、押下判定、設定の保存/読み込み、タッチボタン管理も担う。

**公式ドキュメント抜粋**（[Input Manager](../../docs/toplevelcomponents/player-and-game-management/input-manager.md)）

> You can check all the actions in the pause menu by pressing Esc, then selecting Edit Control Input. In that window, you can see all the actions defined in the custom Input Manager. This component is assigned in the gameObject Player And Menu Management. In the inspector you can add and remove as many groups of actions as needed. These groups are divided into Axes, so the input of the controller can be organized into a separate group from the camera, another group for weapons, powers, menus, vehicles, etc… For this, go to Multi Axes List and open it: Inside every group, you can add, remove, enable and disable every action and assign a keyboard button, a gamepad button, and a touch button. Also, you can edit the path to save the current map button, by pressing the button Save Settings. This file will be stored in the persistent path by default or in a relative path to your project folder i…

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Action Keys On Menu | `showActionKeysOnMenu` | `bool` | true | オフにするとキー割当メニューを開けなくする。 |
| Check Input Manager Elements On Start Enabled | `checkInputManagerElementsOnStartEnabled` | `bool` | true | オンで起動時に各入力要素を検索・初期化する。 |

### Gamepad Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Gamepad | `ignoreGamepad` | `bool` | – | オンでゲームパッドを無視しキーボード操作のみにする。 |
| Allow Keyboard And Gamepad | `allowKeyboardAndGamepad` | `bool` | – | オンでキーボードとゲームパッドの同時使用を許可する。 |
| Allow Gamepad In Touch Device | `allowGamepadInTouchDevice` | `bool` | – | タッチ端末でもゲームパッド入力を有効にする。 |
| Check Connected Gamepad Rate | `checkConnectedGamepadRate` | `float` | – | 接続ゲームパッドを再確認する間隔（秒）。 |

### Debug Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Missing Input Warning Messages Enabled | `showMissingInputWarningMessagesEnabled` | `bool` | true | オンで未設定アクションの警告をログに出す。 |
| Show Keyboard Pressed | `showKeyboardPressed` | `bool` | – | オンでキー入力時にキー名をログ出力する。 / If true any keypress will be logged to the Debug console. |
| Show Keyboard Pressed Action | `showKeyboardPressedAction` | `bool` | – | オンでキー入力時に対応するアクション名も出力。 |
| Show Gamepad Pressed | `showGamepadPressed` | `bool` | – | オンでゲームパッド入力時にボタン名を出力する。 |
| Show Gamepad Pressed Action | `showGamepadPressedAction` | `bool` | – | オンでゲームパッド入力時に対応アクション名も出力。 |
| Show Pressed Key When Editing Input | `showPressedKeyWhenEditingInput` | `bool` | – | 入力再割当中に押されたキー名をログに出す。 |
| Show Debug Key Pressed | `showDebugKeyPressed` | `bool` | – | オンで押された全キーコードをログに出力する。 |

### Input State (DEBUG)

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Gamepad | `usingGamepad` | `bool` | – | ゲームパッドが使用中かどうかを示す内部状態。 |
| Only One Player | `onlyOnePlayer` | `bool` | – | 接続ゲームパッドが1台以下かどうかを示す状態。 |
| Using Key Board | `usingKeyBoard` | `bool` | – | キーボード入力が有効な状態かどうか。 |
| Number Of Gamepads | `numberOfGamepads` | `int` | -1 | 検出されている接続ゲームパッドの台数。 |
| Last Button Pressed On Gamepad | `lastButtonPressedOnGamepad` | `bool` | – | 直近の入力がゲームパッドだったかを示すフラグ。 |
| Last Key Pressed On Keyboard | `lastKeyPressedOnKeyboard` | `bool` | – | 直近の入力がキーボードだったかを示すフラグ。 |
| Use Touch Controls | `useTouchControls` | `bool` | – | タッチ操作が有効かどうかを示す実行時の状態。 |
| Editing Input | `editingInput` | `bool` | – | 入力の再割当待ちかどうかを示す実行時の状態。 |

### Rebing Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Input Key Duplicated On Rebind Action | `checkInputKeyDuplicatedOnRebindAction` | `bool` | – | オンで他アクションと重複するキーの割当を禁止する。 |
| Check Input Key Duplicated Only On Same Input Category | `checkInputKeyDuplicatedOnlyOnSameInputCategory` | `bool` | – | 重複チェックを同じ入力カテゴリ内だけに限定する。 |

### Save/Load Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Load Option | `loadOption` | `loadType` | – | 起動時に設定をファイルから読むか、インスペクタ値を使うか。 |
| Use Custom Input File Name | `useCustomInputFileName` | `bool` | – | エディタでの保存・読込に独自ファイル名を使う。 / 表示条件: `showHideSaveLoadOptions` がオンのとき |
| Custom Input File Name | `customInputFileName` | `string` | – | 使用する入力ファイル名（拡張子は自動付与）。 / 表示条件: `showHideSaveLoadOptions && useCustomInputFileName.boolValue` |
| Use Custom Input File Path Name | `useCustomInputFilePathName` | `bool` | true | オンで入力ファイルの保存先フォルダを指定する。 / 表示条件: `showHideSaveLoadOptions && useCustomInputFileName.boolValue` |
| Custom Input File Path Name | `customInputFilePathName` | `string` | "Assets/Game Kit Controller/Input" | 入力ファイルを置くフォルダのパス。 / 表示条件: `useCustomInputFileName.boolValue && useCustomInputFilePathName.boolValue` |

### Input Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Edit Input Panel Prefab | `editInputPanelPrefab` | `GameObject` | – | リバインド画面のパネルを生成するプレハブ。 |
| Edit Input Menu | `editInputMenu` | `GameObject` | – | リバインド画面全体のルート`GameObject`。 |
| Current Input Panel List Text | `currentInputPanelListText` | `Text` | – | 選択中パネル名を表示する`Text`。 |
| Characters Manager | `charactersManager` | `playerCharactersManager` | – | プレイヤー一覧を取得する`playerCharactersManager`。 |
| Pause Manager | `pauseManager` | `menuPause` | – | ポーズメニュー参照。タッチ操作の有効切替に使用。 |
| Main Game Manager | `mainGameManager` | `gameManager` | – | タッチ操作設定や保存パスを参照する`gameManager`。 |

### Rebind Input Menu Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Create Rebind Input Menu With Current Axes | `createRebindInputMenuWithCurrentAxes` | `bool` | – | オンで現在のアクション数からリバインド画面を自動生成。 |
| Rebind Input Menu Panels Amount | `rebindInputMenuPanelsAmount` | `int` | – | 自動生成をオフにした時のパネル数。 |
| Rebind Input Menu Actions Per Panel Amount | `rebindInputMenuActionsPerPanelAmount` | `int` | – | 1パネルあたりに表示するアクション数。 |

### Show Current Input Action List Settings Filter

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Action Key To Filter | `actionKeyToFilter` | `KeyCode` | – | 一覧表示を絞り込むキーボードキー。 |
| Joystick Button To Filter | `joystickButtonToFilter` | `joystickButtons` | – | 一覧表示を絞り込むゲームパッドボタン。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `axes` | `List<Axes>` | new List<Axes> () | – |
| `multiAxesList` | `List<multiAxes>` | new List<multiAxes> () | – |
| `useRelativePath` | `bool` | – | – |
| `buttonsDisabledAtStart` | `List<GameObject>` | new List<GameObject> () | – |
| `gamepadList` | `List<gamepadInfo>` | new List<gamepadInfo> () | – |
| `controllerToUnityIndexMap` | `Dictionary<int, int>` | new Dictionary<int, int>() | – |
| `playerInputManagerList` | `List<playerInputManager>` | new List<playerInputManager> () | – |
| `touchPlatform` | `bool` | – | – |
| `gameCurrentlyPaused` | `bool` | – | – |
| `multiAxesEditButtonInputList` | `List<multiAxesEditButtonInput>` | new List<multiAxesEditButtonInput> () | – |
| `touchButtonList` | `List<touchButtonListener>` | new List<touchButtonListener> () | – |
| `touchButtonsInfoList` | `List<touchButtonsInfo>` | new List<touchButtonsInfo> () | – |
| `touchButtonsStringInfoList` | `List<touchButtonsStringInfo>` | new List<touchButtonsStringInfo> () | – |
| `buttonsToIgnoreSetVisibleStateList` | `List<touchButtonListener>` | new List<touchButtonListener> () | – |
| `currentInputPanelListIndex` | `int` | 0 | – |
| `register` | `Dictionary<string, Dictionary<JoystickData.ButtonTypes, int>>` | – | – |
| `joystickNames` | `string []` | – | – |
| `joystickName` | `string` | – | – |
| `touchButtonListString` | `string []` | – | – |
| `currentInputActionList` | `List<string>` | new List<string> () | – |
| `customInputFileList` | `string []` | – | – |
| `customInputFileListAssigned` | `bool` | – | – |
| `useMultipleGamepadDictionary` | `bool` | – | – |
| `currentNumberOfTouchButtonsPressed` | `int` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 自身をシングルトン`Instance`として登録し、既に別インスタンスがあれば自身を破棄する。 |
| `getComponentInstanceOnApplicationPlaying()` | 再生中のみ`getComponentInstance`を呼び、シングルトンを初期化する。 |
| `checkInputManagerElementsOnStart()` | 起動時にタッチ判定やプレイヤー入力、ゲームマネージャ設定を取得し、入力読込とゲームパッド一覧構築を行う。 |
| `updatePlayerInputManagerList()` | 各プレイヤーの入力を更新させ、`pauseManager`未設定時はメインプレイヤー情報を設定する。 |
| `setMainPlayerInfo(playerInputManager newPlayerInputManager, menuPause newMenuPause)` | 対象プレイヤーを入力マネージャリストへ追加し、メニュー用テキストとプリファブ、`pauseManager`を設定する。 |
| `isUsingGamepad()` | `usingGamepad`を返すだけ。 |
| `isUsingKeyBoard()` | `usingKeyBoard`を返すだけ。 |
| `isUsingTouchControls()` | `usingTouchControls`を返すだけ。 |
| `isUsingTouchControlsOnGameManager()` | `mainGameManager.isUsingTouchControls`の結果を返すだけ。 |
| `isGameManagerPaused()` | `gameManagerPaused`を返すだけ。 |
| `isAllowKeyboardAndGamepad()` | `allowKeyboardAndGamepad`を返すだけ。 |
| `isAllowGamepadInTouchDevice()` | `allowGamepadInTouchDevice`を返すだけ。 |
| `setEditInputMenuOpenedState(bool state)` | `editInputMenuOpened`を設定するだけ。 |
| `openInputMenu()` | キー表示が無効なら何もせず、編集メニューを生成して最初のパネルを開き、アクション名とキー名を表示する。 |
| `reloadInputMenu()` | 現在の入力パネルとアクションのキー表示を再更新する。 |
| `setKeyNamesInActionsList()` | 編集パネル内の各ボタンに、アクション名とキーボード/ゲームパッドのキー名を設定する。 |
| `updateCurrentInputPanel(int index)` | 指定インデックスのパネルだけを表示し、パネル名のテキスト表示とスクロール位置をリセットする。 |
| `resetScroll(Scrollbar scrollBarToReset)` | 2フレーム待ってからスクロールバーの値を1に戻すコルーチンを開始する。 |
| `resetPanelSlotsRectTransform(Transform panelTransform, ScrollRect panelScrollRect)` | レイアウトを強制再構築してから`panelScrollRect`の縦位置を先頭に戻すコルーチンを開始する。 |
| `setNextInputPanel()` | 次の有効な入力パネルへ循環して移動し、表示を更新する。 |
| `setPreviousInputPanel()` | 前の有効な入力パネルへ循環して移動し、表示を更新する。 |
| `destroyRebindMenusAndActionsPanels()` | 生成済みの入力編集パネルを破棄してリストを空にし、インスペクタを更新する。 |
| `instantiateRebindMenusAndActionsPanels(bool updateComponentActive)` | `editInputPanelPrefab`からアクション数分の入力パネルとボタンを生成して登録し、必要なら更新する。 |
| `saveButtonsInput()` | 編集パネルのキー値をアクションへ反映し、`saveFileName`にアクション一覧をバイナリで保存する。 |
| `getDataPath(string fileNameToUse)` | 相対/永続パスとカスタムパスから保存先フォルダを決め、無ければ作成してファイル名を連結したパスを返す。 |
| `loadButtonsInput()` | `loadOption`に応じて保存ファイルかインスペクタ設定からアクションを読み込み、タッチ参照と件数を更新する。 |
| `saveButtonsInputFromInspector(string fileNameToUse)` | インスペクタのアクション設定を複製し、指定ファイル名でバイナリ保存する。 |
| `loadButtonsInputFromInspector(string fileNameToUse)` | 指定ファイルが存在すればデシリアライズして`multiAxesList`を置き換え、無ければ警告を出す。 |
| `getGameManagerSettings()` | `mainGameManager`から保存フォルダ名・ファイル名・相対パス設定を取得し、永続データパスを更新する。 |
| `setCurrentInputToDefault()` | ゲームマネージャ設定を取得し、既定ファイルから入力を読み込んでインスペクタを更新する。 |
| `loadButtonsInspectorFromSaveFile()` | 設定を取得し、再生中でなければカスタム名または通常の保存ファイルを読み込んでインスペクタを更新する。 |
| `saveCurrentInputAsDefault()` | 現在のアクション設定を既定ファイル名で保存する。 |
| `saveButtonsInputToSaveFile()` | カスタム名または通常の保存ファイル名へ現在の入力設定を保存する。 |
| `showCustomInputFileList()` | 指定フォルダ内の`.txt`を列挙し、パスと拡張子を除いた名前を`customInputFileList`へ格納する。 |
| `changeKeyValue(string keyButton, int multiAxesIndex, int axesIndex)` | 指定アクションの`key`を`KeyCode`へ変換して設定し、`keyButton`も更新する。 |
| `changeGamepadKeyValue(string keyButton, int multiAxesIndex, int axesIndex)` | 指定アクションの`joystickButton`を列挙値へ変換して設定する。 |
| `getButtonKey(string actionName)` | アクション名からキー文字列を検索し、ゲームパッド使用中ならジョイスティックボタン名を返す。 |
| `startEditingInput(GameObject button)` | 編集中でなければコルーチンを開始し、対象ボタンの表示を「...」にしてキー入力を待つ。 |
| `isEditingInput()` | `editingInput`を返すだけ。 |
| `cancelEditingInput()` | 編集状態を解除し、対象ボタンの表示を以前の値へ戻す。 |
| `checkIfSaveInputAfterRebind()` | 新しいキーが割り当てられていれば`saveButtonsInput`で保存し、フラグを戻す。 |
| `getValidKeyCodes()` | `KeyCode`の全列挙値を`validKeyCodes`へ取得するだけ。 |
| `getKeyPressed(buttonType type, bool canBeUsedOnGamePaused)` | ポーズ状態とタッチ設定を確認し、`type`に応じた押下中のキー名を返す（無ければ空文字）。 |
| `checkJoystickButton(string joystickString, buttonType type)` | タッチとキーボードの設定を確認し、指定ジョイスティックボタンの押下/離上を判定する。 |
| `checkPlayerInputButtonFromMultiAxesList(int multiAxesIndex, int axesIndex, buttonType type, int controllerNumber, bool canBeUsedOnPausedGame, bool useOnlyKeyboard)` | タッチ優先でキーボードとゲームパッドの押下を判定し、入力元が変わったら切替イベントを発火する。 |
| `getKeyboardButtonFromMultiAxesList(int multiAxesIndex, int axesIndex, buttonType type, bool canBeUsedOnPausedGame)` | インデックスと有効状態を検証し、指定アクションのキーやマウスホイール入力を判定する。 |
| `isKeyboardButtonPressed(int controllerNumber, string multiAxesName, string axesName)` | グループ名とアクション名から入力を検索し、タッチ・キーボード・ゲームパッドの押下状態を返す。 |
| `getTouchButtonFromMultiAxesList(int multiAxesIndex, int axesIndex, buttonType type)` | 指定アクションに割り当てたタッチボタンのタッチ開始・継続・終了を判定する。 |
| `getJoystickButtonFromMultiAxesList(int multiAxesIndex, int axesIndex, buttonType type, int controllerNumber, bool canBeUsedOnPausedGame)` | コントローラ番号を検証し、割り当てたゲームパッドボタンまたは軸の押下を判定する。 |
| `getAxisValue(int numberPlayer, int keyPressed, int multiAxesIndex, int axesIndex, buttonType type)` | `gamepadList`の軸名からトリガーや十字キーの値を読み、`type`に応じて押下判定と前回状態を更新する。 |
| `setGamepadLeftTriggersInfo(int numberPlayer, bool left, int multiAxesIndex, int axesIndex)` | `usingLeftTrigger`を設定するだけ。 |
| `setGamepadRightTriggersInfo(int numberPlayer, bool right, int multiAxesIndex, int axesIndex)` | `usingRightTrigger`を設定するだけ。 |
| `setGamepadLeftTriggersInfoDown(int numberPlayer, bool left, int multiAxesIndex, int axesIndex)` | `leftTriggerDown`を設定するだけ。 |
| `setGamepadRightTriggersInfoDown(int numberPlayer, bool right, int multiAxesIndex, int axesIndex)` | `rightTriggerDown`を設定するだけ。 |
| `getGamePadLeftTriggersInfo(int numberPlayer, int multiAxesIndex, int axesIndex)` | `usingLeftTrigger`を返すだけ。 |
| `getGamePadRightTriggersInfo(int numberPlayer, int multiAxesIndex, int axesIndex)` | `usingRightTrigger`を返すだけ。 |
| `getGamePadLeftTriggersInfoDown(int numberPlayer, int multiAxesIndex, int axesIndex)` | `leftTriggerDown`を返すだけ。 |
| `getGamePadRightTriggersInfoDown(int numberPlayer, int multiAxesIndex, int axesIndex)` | `rightTriggerDown`を返すだけ。 |
| `getGamePadDPadXInfoPositive(int numberPlayer, int multiAxesIndex, int axesIndex)` | `usingDPadXPositive`を返すだけ。 |
| `setGamepadDPadXInfoPositive(int numberPlayer, bool DPad, int multiAxesIndex, int axesIndex)` | `usingDPadXPositive`を設定するだけ。 |
| `getGamePadDPadXInfoPositiveDown(int numberPlayer, int multiAxesIndex, int axesIndex)` | `DPadXPositiveDown`を返すだけ。 |
| `setGamepadDPadXInfoPositiveDown(int numberPlayer, bool DPad, int multiAxesIndex, int axesIndex)` | `DPadXPositiveDown`を設定するだけ。 |
| `getGamePadDPadXInfoNegative(int numberPlayer, int multiAxesIndex, int axesIndex)` | `usingDPadXNegative`を返すだけ。 |
| `setGamepadDPadXInfoNegative(int numberPlayer, bool DPad, int multiAxesIndex, int axesIndex)` | `usingDPadXNegative`を設定するだけ。 |
| `getGamePadDPadXInfoNegativeDown(int numberPlayer, int multiAxesIndex, int axesIndex)` | `DPadXNegativeDown`を返すだけ。 |
| `setGamepadDPadXInfoNegativeDown(int numberPlayer, bool DPad, int multiAxesIndex, int axesIndex)` | `DPadXNegativeDown`を設定するだけ。 |
| `getGamePadDPadYInfoPositive(int numberPlayer, int multiAxesIndex, int axesIndex)` | `usingDPadYPositive`を返すだけ。 |
| `setGamepadDPadYInfoPositive(int numberPlayer, bool DPad, int multiAxesIndex, int axesIndex)` | `usingDPadYPositive`を設定するだけ。 |
| `getGamePadDPadYInfoPositiveDown(int numberPlayer, int multiAxesIndex, int axesIndex)` | `DPadYPositiveDown`を返すだけ。 |
| `setGamepadDPadYInfoPositiveDown(int numberPlayer, bool DPad, int multiAxesIndex, int axesIndex)` | `DPadYPositiveDown`を設定するだけ。 |
| `getGamePadDPadYInfoNegative(int numberPlayer, int multiAxesIndex, int axesIndex)` | `usingDPadYNegative`を返すだけ。 |
| `setGamepadDPadYInfoNegative(int numberPlayer, bool DPad, int multiAxesIndex, int axesIndex)` | `usingDPadYNegative`を設定するだけ。 |
| `getGamePadDPadYInfoNegativeDown(int numberPlayer, int multiAxesIndex, int axesIndex)` | `DPadYNegativeDown`を返すだけ。 |
| `setGamepadDPadYInfoNegativeDown(int numberPlayer, bool DPad, int multiAxesIndex, int axesIndex)` | `DPadYNegativeDown`を設定するだけ。 |
| `setRegister()` | 実行プラットフォームに応じて`register`へジョイスティックのボタン割り当て表を設定する。 |
| `setKeyboardControls(bool state)` | タッチ操作を`state`の逆に設定し、ゲームマネージャと各プレイヤーの操作種別も切り替える。 |
| `setKeyboardControlsFromEditor(bool state)` | エディタ用にタッチ操作を切り替え、各プレイヤーの操作種別を変更してインスペクタを更新する。 |
| `setUseTouchControlsState(bool state)` | `useTouchControls`を設定するだけ。 |
| `updateInputInspector()` | 再生中でなければ更新ログを出し、コンポーネントとシーンのダーティ更新を行う。 |
| `isInTouchButtonToDisableList(GameObject touchButtonGameObject)` | 起動時に無効化するタッチボタン一覧に含まれるかを返す。 |
| `setGamePadList()` | 接続中のジョイスティックから`gamepadList`と対応表を構築し、ボタン/軸名や使用入力を更新する。 |
| `setPauseState(bool state)` | `gameCurrentlyPaused`を設定するだけ。 |
| `enableTouchButtonByName(string touchButtonName)` | 名前が一致するタッチボタンを`enableOrDisableTouchButtonByName`で有効にする。 |
| `disableTouchButtonByName(string touchButtonName)` | 名前が一致するタッチボタンを`enableOrDisableTouchButtonByName`で無効にする。 |
| `enableOrDisableTouchButtonByName(bool state, string touchButtonName)` | 名前が一致する最初のタッチボタンの`SetActive`を`state`に切り替える。 |
| `isTouchPlatform()` | `touchPlatform`を返すだけ。 |
| `increaseCurrentNumberOfTouchButtonsPressed()` | 押下中のタッチボタン数を1増やすだけ。 |
| `decreaseCurrentNumberOfTouchButtonsPressed()` | 押下中のタッチボタン数を1減らし、負なら0に補正する。 |
| `getCurrentNumberOfTouchButtonsPressed()` | 押下中のタッチボタン数を返すだけ。 |
| `checkButtonPressedOnGamepadOrKeyboard(bool checkKeyboard)` | 最後に操作した入力元フラグを、キーボードかゲームパッドに設定する。 |
| `enableMultiAxesInputByName(string multiAxesName)` | 名前が一致するアクショングループを有効化する。 |
| `disableMultiAxesInputByName(string multiAxesName)` | 名前が一致するアクショングループを無効化する。 |
| `enableOrDisableMultiAxesInputByName(bool state, string multiAxesName)` | 名前が一致するアクショングループの`currentlyActive`を設定する。 |
| `addNewAxe(int axeListIndex)` | 指定グループに既定名の新規アクションを追加し、インスペクタを更新する。 |
| `addNewAxesList()` | 既定名の新しいアクショングループを追加し、インスペクタを更新する。 |
| `removeAxesList(int multiAxesIndex)` | 指定インデックスのアクショングループを削除して警告を表示し、インスペクタを更新する。 |
| `getAxesListIndexByName(string axesName)` | 名前が一致するアクショングループのインデックスを返し、無ければ-1を返す。 |
| `removeAxesElement(int multiAxesIndex, int axesIndex)` | 指定グループから指定アクションを削除して警告を表示し、インスペクタを更新する。 |
| `removeTouchPanel(int touchPanelIndex)` | タッチパネルを削除し、各アクションのパネル/ボタン参照を名前から再設定して更新する。 |
| `removeTouchButton(int touchPanelIndex, int touchButtonIndex)` | タッチボタンを削除し、各アクションのボタン参照を名前から再設定して更新する。 |
| `getTouchButtonList()` | メインプレイヤーのタッチパネルからタッチボタン一覧とパネル情報を再構築する。 |
| `setNewTouchButtonListByPlayerInputManager(playerInputManager currentPlayerInputManager)` | 指定プレイヤーのタッチボタン一覧とパネル情報をそのまま代入する。 |
| `setTouchButtonVisibleState(bool state)` | 無視リスト以外のタッチボタンと各プレイヤーのジョイスティックの表示状態を切り替える。 |
| `resetButtonStateOnTouchButtonList()` | 全タッチボタンの押下状態をリセットする。 |
| `checkNullElementsOnPlayerInputManagerList()` | プレイヤー入力リストが空、またはnull要素を含む場合にtrueを返す。 |
| `toggleTouchButtonsVisibleState()` | タッチボタンの表示状態を反転させて反映する。 |
| `getTouchButtonListString()` | タッチパネル/ボタン一覧を取得し、表示用文字列とリストを更新する。 |
| `selectMainTouchButtonPanelOnEditor()` | メインプレイヤーのタッチパネルをエディタ上で選択する。 |
| `updateTouchButtonListString()` | パネル名とボタン名から選択用の文字列配列と`touchButtonsStringInfoList`を再構築する。 |
| `updateTouchButtonList()` | 各アクションのタッチパネル/ボタン名からインデックスを引き直し、見つからなければ0に戻す。 |
| `getTouchPanelIndexByName(string touchPanelName)` | 名前が一致するタッチパネルのインデックスを返し、無ければ-1を返す。 |
| `getTouchButtonIndexByName(string touchPanelName, string touchButtonName)` | パネル名とボタン名からタッチボタンのインデックスを返し、無ければ-1を返す。 |
| `showCurrentInputActionList(bool showOnlyKeys, bool showOnlyJoystick)` | 表示指定とフィルタに応じ、全アクションのキー/ジョイスティック情報を一覧テキストへ組み立てる。 |
| `showCurrentInputActionListByKeyFilter()` | キーフィルタを一時的に有効にしてアクション一覧を生成し、フィルタを戻す。 |
| `showCurrentInputActionListByJoystickFilter()` | ジョイスティックフィルタを一時的に有効にして一覧を生成し、フィルタを戻す。 |
| `clearInputActionListText()` | `currentInputActionList`を空にしてインスペクタを更新する。 |

## 内部型

- `buttonType`（enum）
- `loadType`（enum）
- `Axes`（class）
- `joystickButtons`（enum）
- `gamepadInfo`（class）
- `multiGamepadAxisInfo`（class）
- `gamepadAxisInfo`（class）
- `multiAxes`（class）
- `multiAxesEditButtonInput`（class）
- `touchButtonsInfo`（class）
- `touchButtonsStringInfo`（class）
