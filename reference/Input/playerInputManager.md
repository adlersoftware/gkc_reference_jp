# playerInputManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Input/playerInputManager.cs:11`

**概要**: プレイヤーごとの入力抽象化コンポーネントで、`inputManager`から移動・カメラ軸、アクション、タッチ、ゲームパッドの状態を取得する。`multiAxesList`のアクション判定と`buttonEvent`発火、入力の有効/停止、タッチパネル操作を担当する。

**公式ドキュメント抜粋**（[Player Input Manager](../../docs/player-controller-components/player-controller/player-input-manager.md)）

> Once all the input actions are configured in Input Manager, the player gets that list of actions and to each one, an event is configured along with setting the type of press key (down, hold or release) to activate that action. So it makes the player call the jump function when the key jump is pressed through an event calling such function. It also manages the gamepad and mobile input, along with the axis for movement and camera.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player ID | `playerID` | `int` | – | プレイヤーを識別するID。入力軸名の解決に使う。 |
| Show Debug Actions | `showDebugActions` | `bool` | – | ONにすると押されたアクション名をログ出力する。 |
| Use Only Keyboard | `useOnlyKeyboard` | `bool` | – | ONにするとキーボード入力のみを使う。 |

### Sensitivity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Mouse Sensitivity | `mouseSensitivity` | `float` | – | マウス入力の感度に掛ける倍率。 / Range (0, 10) |
| Use Vertical And Horizontal Gamepad Sensitivity | `useVerticalAndHorizontalGamepadSensitivity` | `bool` | – | ONにするとパッド感度を縦横別々に設定する。 |
| Left Gamepad Joystick Horizontal Sensitivity | `leftGamepadJoystickHorizontalSensitivity` | `float` | 1 | 左スティック横方向の入力感度。 / 表示条件: `useVerticalAndHorizontalGamepadSensitivity` がオンのとき / Range (0, 10) |
| Left Gamepad Joystick Vertical Sensitivity | `leftGamepadJoystickVerticalSensitivity` | `float` | 1 | 左スティック縦方向の入力感度。 / 表示条件: `useVerticalAndHorizontalGamepadSensitivity` がオンのとき / Range (0, 10) |
| Right Gamepad Joystick Horizontal Sensitivity | `rightGamepadJoystickHorizontalSensitivity` | `float` | 1 | 右スティック横方向の入力感度。 / 表示条件: `useVerticalAndHorizontalGamepadSensitivity` がオンのとき / Range (0, 10) |
| Right Gamepad Joystick Vertical Sensitivity | `rightGamepadJoystickVerticalSensitivity` | `float` | 1 | 右スティック縦方向の入力感度。 / 表示条件: `useVerticalAndHorizontalGamepadSensitivity` がオンのとき / Range (0, 10) |
| Left Gamepad Joystick Sensitivity | `leftGamepadJoystickSensitivity` | `float` | 1 | 左スティック全体の入力感度。 / Range (0, 10) |
| Right Gamepad Joystick Sensitivity | `rightGamepadJoystickSensitivity` | `float` | 1 | 右スティック全体の入力感度。 / Range (0, 10) |
| Left Touch Sensitivity | `leftTouchSensitivity` | `float` | – | タッチ移動入力の感度に掛ける倍率。 / Range (0, 10) |
| Right Touch Sensitivity | `rightTouchSensitivity` | `float` | – | タッチカメラ入力の感度に掛ける倍率。 / Range (0, 10) |

### Control Orientation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Movement Orientation | `useMovementOrientation` | `bool` | – | ONにすると移動入力の縦横を反転できる。 |
| Horizontal Movement Orientation | `horizontalMovementOrientation` | `int` | 1 | 移動入力の横方向の向き（1か-1）。 / 表示条件: `useMovementOrientation` がオンのとき / Range (-1, 1) |
| Vertical Movement Orientation | `verticalMovementOrientation` | `int` | 1 | 移動入力の縦方向の向き（1か-1）。 / 表示条件: `useMovementOrientation` がオンのとき / Range (-1, 1) |
| Use Camera Orientation | `useCameraOrientation` | `bool` | – | ONにするとカメラ入力の縦横を反転できる。 |
| Horizontal Camera Orientation | `horizontalCameraOrientation` | `int` | 1 | カメラ入力の横方向の向き（1か-1）。 / 表示条件: `useCameraOrientation` がオンのとき / Range (-1, 1) |
| Vertical Camera Orientation | `verticalCameraOrientation` | `int` | 1 | カメラ入力の縦方向の向き（1か-1）。 / 表示条件: `useCameraOrientation` がオンのとき / Range (-1, 1) |

### Touch Controls Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Touch Movement Control | `touchMovementControl` | `touchJoystick` | – | タッチ移動に使うジョイスティック。 |
| Touch Camera Control | `touchCameraControl` | `touchJoystick` | – | タッチカメラ操作に使うジョイスティック。 |
| Touch Panel | `touchPanel` | `GameObject` | – | タッチ操作UIをまとめたパネル。 |
| Using Touch Movement Joystick | `usingTouchMovementJoystick` | `bool` | true | ONにするとタッチ移動をジョイスティックで行う。 |
| Input Lerp Speed Touch Movement Buttons | `inputLerpSpeedTouchMovementButtons` | `float` | 5 | タッチ移動ボタン入力が目標値へ近づく速さ。 |
| Use Horizonta Touch Movement Buttons | `useHorizontaTouchMovementButtons` | `bool` | – | ONにすると横移動用のタッチボタンを表示する。 |
| Use Vertical Touch Movement Buttons | `useVerticalTouchMovementButtons` | `bool` | – | ONにすると縦移動用のタッチボタンを表示する。 |
| Horizontal Touch Movement Buttons | `horizontalTouchMovementButtons` | `GameObject` | – | 横移動用タッチボタンの親オブジェクト。 |
| Vertical Touch Movement Buttons | `verticalTouchMovementButtons` | `GameObject` | – | 縦移動用タッチボタンの親オブジェクト。 |

### Input State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Input Enabled | `inputEnabled` | `bool` | true | OFFにするとプレイヤーの入力処理を止める。 |
| Player Is Non Local Avatar | `playerIsNonLocalAvatar` | `bool` | – | ONにすると他プレイヤーが操作するアバターとして扱う。 |
| Player Non Local Avatar ID | `playerNonLocalAvatarID` | `int` | – | 非ローカルアバターを識別するID。 |
| Movement Axis | `movementAxis` | `Vector2` | – | 現在の移動入力値（横・縦）。 |
| Mouse Axis | `mouseAxis` | `Vector2` | – | 現在のカメラ入力値（横・縦）。 |
| Raw Movement Axis | `rawMovementAxis` | `Vector2` | – | 平滑化していない生の移動入力値。 |
| Ignore All Actions Input | `ignoreAllActionsInput` | `bool` | – | ONにするとボタン系アクションを全て無視する。 |
| Ignore All Axis Input | `ignoreAllAxisInput` | `bool` | – | ONにすると移動・カメラの軸入力を全て無視する。 |

### Manual Control Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Manual Control Active | `manualControlActive` | `bool` | – | ONにすると手動で指定した入力値を使う。 |
| Manual Movement Horizontal Input | `manualMovementHorizontalInput` | `float` | – | 手動制御時の横移動入力値。 / 表示条件: `manualControlActive` がオンのとき / Range (-1, 1) |
| Manual Movement Vertical Input | `manualMovementVerticalInput` | `float` | – | 手動制御時の縦移動入力値。 / 表示条件: `manualControlActive` がオンのとき / Range (-1, 1) |
| Manual Mouse Horizontal Input | `manualMouseHorizontalInput` | `float` | – | 手動制御時の横カメラ入力値。 / 表示条件: `manualControlActive` がオンのとき / Range (-1, 1) |
| Manual Mouse Vertical Input | `manualMouseVerticalInput` | `float` | – | 手動制御時の縦カメラ入力値。 / 表示条件: `manualControlActive` がオンのとき / Range (-1, 1) |

### Player Element Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Input | `input` | `inputManager` | – | 軸やボタン名を解決する入力管理コンポーネント。 |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | 入力対象のプレイヤーコントローラーの参照。 |
| Main Player Input Panel System | `mainPlayerInputPanelSystem` | `playerInputPanelSystem` | – | タッチパネルやアクション画面を管理する参照。 |
| Edit Input Panel Prefab | `editInputPanelPrefab` | `GameObject` | – | 入力編集パネルを生成するプレハブ。 |
| Edit Input Menu | `editInputMenu` | `GameObject` | – | 入力設定を編集するメニューのオブジェクト。 |
| Current Input Panel List Text | `currentInputPanelListText` | `GameObject` | – | 現在の入力パネル名を表示するテキスト。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `multiAxesList` | `List<multiAxes>` | new List<multiAxes> () | – |
| `inputCurrentlyActive` | `bool` | true | – |
| `ignoreGamepad` | `bool` | – | – |
| `allowKeyboardAndGamepad` | `bool` | – | – |
| `allowGamepadInTouchDevice` | `bool` | – | – |
| `pressingTouchHorizontalRightInput` | `bool` | – | – |
| `pressingTouchHorizontalLeftInput` | `bool` | – | – |
| `pressingTouchVerticalUpInput` | `bool` | – | – |
| `pressingTouchVerticalDownInput` | `bool` | – | – |
| `usingGamepad` | `bool` | – | – |
| `usingKeyBoard` | `bool` | – | – |
| `usingTouchControls` | `bool` | – | – |
| `gameManagerPaused` | `bool` | – | – |
| `horizontalString` | `string` | "Horizontal" | – |
| `verticalString` | `string` | "Vertical" | – |
| `mouseXString` | `string` | "Mouse X" | – |
| `mouseYString` | `string` | "Mouse Y" | – |
| `horizontalXString` | `string` | "Horizontal X" | – |
| `verticalYString` | `string` | "Vertical Y" | – |
| `inputPaused` | `bool` | – | – |
| `showSingleMultiAxes` | `bool` | – | – |
| `currentMultiAxesToShow` | `int` | – | – |
| `hideSingleMultiAxes` | `bool` | – | – |
| `inputCurrentlyActiveInfoList` | `List<inputCurrentlyActiveInfo>` | new List<inputCurrentlyActiveInfo> () | – |
| `overrideInputValuesActive` | `bool` | – | – |
| `ignorePlayerActionsInput` | `bool` | – | – |
| `axisInputPaused` | `bool` | – | – |
| `movementAxisInputPaused` | `bool` | – | – |
| `cameraAxisInputPaused` | `bool` | – | – |
| `touchButtonList` | `List<touchButtonListener>` | new List<touchButtonListener> () | – |
| `touchButtonsInfoList` | `List<touchButtonsInfo>` | new List<touchButtonsInfo> () | – |
| `usingPlayerMenu` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `isAnyMenuActive()` | ゲームマネージャー停止中か、プレイヤーメニューまたはサブメニュー使用中なら`true`を返す。 |
| `getAuxMovementAxis()` | 上書きや手動入力の前の元の移動軸`auxMovementAxis`を返すだけ。 |
| `getAuxRawMovementAxis()` | 上書きや手動入力の前の元の生移動軸`auxRawMovementAxis`を返すだけ。 |
| `changeControlsType(bool state)` | `state`に合わせてタッチ操作一式と画面アクションボタンの表示を切り替える。 |
| `enableOrDisableTouchControls(bool state)` | タッチパネル・カメラ用ジョイスティック・移動操作をまとめて`state`で切り替える。 |
| `enableOrDisableTouchMovementControl(bool state)` | 移動用ジョイスティックのGameObjectを`state`でアクティブ/非アクティブにする。 |
| `enableOrDisableTouchCameraControl(bool state)` | カメラ用ジョイスティックのGameObjectを`state`でアクティブ/非アクティブにする。 |
| `setTouchMovementControl(touchJoystick newTouchJoystick)` | 移動用`touchJoystick`参照を`newTouchJoystick`に差し替えるだけ。 |
| `setTouchCameraControl(touchJoystick newTouchJoystick)` | カメラ用`touchJoystick`参照を`newTouchJoystick`に差し替えるだけ。 |
| `getTouchMovementControl()` | 移動用`touchJoystick`を返すだけ。 |
| `getTouchCameraControl()` | カメラ用`touchJoystick`を返すだけ。 |
| `enableOrDisableTouchMovementJoystickForButtons(bool state)` | `usingTouchMovementJoystick`に応じ、移動ジョイスティックか方向ボタン群の表示を切り替える。 |
| `setJoystickColorVisibleState(bool state)` | 移動・カメラ両方のタッチジョイスティックへ色表示状態`state`を渡す。 |
| `setOriginalTouchMovementInputState()` | 保存した初期値へ移動ジョイスティック設定を戻し、移動操作の表示を有効にする。 |
| `setUsingTouchMovementJoystickState(bool state)` | 移動にジョイスティックを使うか`state`で設定するだけ。 |
| `getPlayerRawMovementAxis()` | 入力無効・停止・全軸無視・死亡時は零、それ以外は生移動軸を返す。 |
| `getPlayerRawMovementAxisWithoutCheckingEnabled()` | `inputEnabled`を見ず、停止・全軸無視・死亡時のみ零にして生移動軸を返す。 |
| `getPlayerMovementAxis()` | 入力無効・停止・全軸無視・死亡時は零、それ以外は`movementAxis`を返す。 |
| `getPlayerMovementAxisWithoutCheckingEnabled()` | `inputEnabled`と全軸無視を見ず、停止・死亡時のみ零にして`movementAxis`を返す。 |
| `getPlayerMouseAxis()` | 入力無効・停止・全軸無視・死亡時は零、それ以外はカメラ軸を返す。 |
| `getRealMovementAxisInput()` | `Horizontal`と`Vertical`軸をRewiredまたは旧Inputから直接読みVector2で返す。 |
| `getRealMouseAxisInput()` | `Mouse X`と`Mouse Y`軸を直接読みVector2で返す。 |
| `getRealMouseRawAxisInput()` | `Mouse X`と`Mouse Y`を`GetAxisRaw`で読みVector2で返す。 |
| `getRealMouseGamepadAxisInput()` | プレイヤーID付きカメラ軸名からゲームパッド右スティックの値を読む。 |
| `getRealMovementGamepadAxisInput()` | プレイヤーID付き`Horizontal X`と`Vertical Y`から左スティックの値を読む。 |
| `getRealMovementAxisInputAnyType()` | タッチ・ゲームパッド・キーボードのうち現在の操作方式に応じた移動軸を返す。 |
| `sendInputSignalExternally(int multiAxesIndex, int axesIndex)` | 本体がコメントのみで何もしない。 |
| `getInputSignalExternally(int multiAxesIndex, int axesIndex)` | 入力有効時のみ指定マルチ軸アクションの`buttonEvent`を発火する。 |
| `sendAxisInputSignalExternally()` | 本体がコメントのみで何もしない。 |
| `getAxisInputSignalExternally(Vector2 newMovementAxis, Vector2 newRawMovementAxis, Vector2 newMouseAxis)` | 受信した移動・生移動・カメラ軸の3値を対応する軸フィールドへ書き込む。 |
| `checkPlayerInputButtonFromMultiAxesList(int multiAxesIndex, int axesIndex, inputManager.buttonType type, bool canBeUsedOnPausedGame)` | 入力有効時のみ指定アクションの押下を`inputManager`へ問い合わせて返す。 |
| `checkPlayerInputButtonWithoutEvents(int multiAxesStringIndex, int axesStringIndex, inputManager.buttonType buttonType)` | 入力有効時のみ指定アクションの押下をイベント無しで判定して返す。 |
| `checkNumberInput(int numberAmount)` | 0〜9キーの押下を調べ押された数字を返し、無ければ-1を返す。 |
| `setPlayerInputEnabledState(bool state)` | 入力全体の有効状態`inputEnabled`を設定するだけ。 |
| `setIgnorePlayerActionsInputState(bool state)` | アクション入力の無視フラグ`ignorePlayerActionsInput`を設定するだけ。 |
| `setPlayerInputEnabledStateWithDelay(bool state)` | `false`なら即無効化し、`true`なら0.3秒後に有効化するコルーチンを開始する。 |
| `setInputCurrentlyActiveState(bool state)` | ポーズ中も入力を有効にするか`inputCurrentlyActive`に設定するだけ。 |
| `toggleInputCurrentlyActiveState()` | `inputCurrentlyActive`の真偽を反転するだけ。 |
| `setPlayerID(int newID)` | `playerID`を`newID`に設定するだけ。 |
| `getPlayerID()` | `playerID`を返すだけ。 |
| `switchPlayerID(int newID)` | IDを設定し、対応するUnityジョイスティック番号から軸名文字列を再構築する。 |
| `isPlayerNonLocalAvatar()` | 非ローカルアバターか`playerIsNonLocalAvatar`を返すだけ。 |
| `setPlayerIsNonLocalAvatarState(bool state)` | 非ローカルアバター状態`playerIsNonLocalAvatar`を設定するだけ。 |
| `getPlayerNonLocalAvatarID()` | `playerNonLocalAvatarID`を返すだけ。 |
| `setPlayerNonLocalAvatarID(int newID)` | `playerNonLocalAvatarID`を設定するだけ。 |
| `setPlayerInputActionState(bool playerInputActionState, string multiAxesInputName, string axesInputName)` | 名前一致のマルチ軸内アクションの`actionEnabled`をまとめて設定する。 |
| `getPlayerInputMultiAxesState(string multiAxesInputName)` | 指定名マルチ軸の`currentlyActive`を返し、見つからなければ`false`を返す。 |
| `updateCurrentActiveInputList()` | 死亡時は何もせず、各マルチ軸の現在の有効状態をリストへ退避する。 |
| `setCurrentActiveInputList()` | 退避した`inputCurrentlyActiveInfoList`の状態を各マルチ軸へ書き戻す。 |
| `setPlayerInputMultiAxesState(bool playerInputMultiAxesState, string multiAxesInputName)` | 名前一致のマルチ軸の`currentlyActive`を設定して終了する。 |
| `setPlayerInputMultiAxesStateAndGetPreviousState(bool playerInputMultiAxesState, string multiAxesInputName)` | 名前一致のマルチ軸を設定し、変更前の状態を返す。 |
| `setIgnoreCheckInputActiveStateOnList(bool ignoreCheckInputActiveValue, List<string> multiAxesInputNameList)` | 名前一覧の各マルチ軸に`ignoreCheckInputActive`をまとめて設定する。 |
| `setIgnoreEnablePlayerInputMultiAxesActiveState(bool state)` | マルチ軸の有効化を無視するフラグを`state`に設定するだけ。 |
| `enablePlayerInputMultiAxes(string multiAxesInputName)` | 無視フラグが立っていなければ指定マルチ軸を`currentlyActive`にする。 |
| `disablePlayerInputMultiAxes(string multiAxesInputName)` | 指定名マルチ軸の`currentlyActive`を`false`にする。 |
| `overrideInputValues(Vector2 newInputValues, bool overrideState)` | 上書き用の移動軸値と有効フラグを設定するだけ。 |
| `setManuaInputValues(Vector2 newMovementInputValues, Vector2 newMouseInputValues)` | 手動操作を有効にし、移動・マウス軸の手動入力を設定する。 |
| `disableManuaInput()` | 手動入力`manualControlActive`を`false`にするだけ。 |
| `setIgnoreOverrideInputState(bool state)` | 上書き入力の無視フラグ`ignoreOverrideInput`を設定するだけ。 |
| `getInputManager()` | `inputManager`参照を返すだけ。 |
| `isUsingTouchControls()` | `inputManager`へタッチ操作中か問い合わせて返す。 |
| `isUsingTouchControlsOnGameManager()` | ゲームマネージャー側のタッチ操作設定を`inputManager`経由で返す。 |
| `updateIsUsingTouchControlsState()` | `inputManager`から取得したタッチ操作状態を`usingTouchControls`へ反映する。 |
| `getButtonKey(string buttonName)` | `inputManager`から指定ボタン名のキー割り当て文字列を取得して返す。 |
| `setAvoidInputActiveState(bool state)` | ポーズ中にアクション入力を避けるフラグ`avoidInputActive`を設定するだけ。 |
| `getTouchPanel()` | タッチパネルのGameObjectを返すだけ。 |
| `setTouchPanelActiveState(bool state)` | タッチパネルのGameObjectを`state`でアクティブ/非アクティブにする。 |
| `getEditInputPanelPrefab()` | 入力編集パネルのプレハブを返すだけ。 |
| `getEditInputMenu()` | 入力編集メニューのGameObjectを返すだけ。 |
| `getCurrentInputPanelListText()` | 現在の入力パネル一覧テキストのGameObjectを返すだけ。 |
| `setHorizontalMovementOrientationValue(int newValue)` | 水平移動の反転値`horizontalMovementOrientation`を整数で設定するだけ。 |
| `setVerticalMovementOrientationValue(int newValue)` | 垂直移動の反転値`verticalMovementOrientation`を整数で設定するだけ。 |
| `setHorizontalCameraOrientationValue(int newValue)` | 水平カメラの反転値`horizontalCameraOrientation`を整数で設定するだけ。 |
| `setVerticalCameratOrientationValue(int newValue)` | 垂直カメラの反転値`verticalCameraOrientation`を整数で設定するだけ。 |
| `setHorizontalMovementOrientationValue(bool state)` | `state`が真なら1、偽なら-1を水平移動の反転値として設定する。 |
| `setVerticalMovementOrientationValue(bool state)` | `state`が真なら1、偽なら-1を垂直移動の反転値として設定する。 |
| `setHorizontalCameraOrientationValue(bool state)` | `state`が真なら1、偽なら-1を水平カメラの反転値として設定する。 |
| `setVerticalCameratOrientationValue(bool state)` | `state`が真なら1、偽なら-1を垂直カメラの反転値として設定する。 |
| `setPressingTouchHorizontalRightInputState(bool state)` | タッチ右入力の押下状態`pressingTouchHorizontalRightInput`を設定するだけ。 |
| `setPressingTouchHorizontalLeftInputState(bool state)` | タッチ左入力の押下状態`pressingTouchHorizontalLeftInput`を設定するだけ。 |
| `setPressingTouchVerticalUpInputState(bool state)` | タッチ上入力の押下状態`pressingTouchVerticalUpInput`を設定するだけ。 |
| `setPressingTouchVerticalDownInputState(bool state)` | タッチ下入力の押下状態`pressingTouchVerticalDownInput`を設定するだけ。 |
| `pauseOrResumeInput(bool state)` | 入力停止フラグ`inputPaused`を設定するだけ。 |
| `setAxisInputPausedState(bool state)` | 軸入力停止フラグ`axisInputPaused`を設定するだけ。 |
| `setIgnoreAllActionsInputState(bool state)` | 全アクション入力の無視フラグを`state`に設定するだけ。 |
| `setMovementAxisInputPausedState(bool state)` | 移動軸の停止フラグ`movementAxisInputPaused`を設定するだけ。 |
| `setCameraAxisInputPausedState(bool state)` | カメラ軸の停止フラグ`cameraAxisInputPaused`を設定するだけ。 |
| `toggleAxisInputPausedState()` | `axisInputPaused`を反転するだけ。 |
| `setIgnorePlayerIsDeadOnCameraAxisState(bool state)` | 死亡中もカメラ軸入力を許可するフラグを設定するだけ。 |
| `setInputPausedForExternalComponentsState(bool state)` | 外部コンポーネント向けの入力停止フラグを設定するだけ。 |
| `isInputPausedForExternalComponents()` | 外部コンポーネント向けの入力停止フラグを返すだけ。 |
| `getTouchPanelsList()` | `mainPlayerInputPanelSystem`からタッチパネル情報の一覧を取得して返す。 |
| `storeTouchButtonList()` | 各タッチパネルのボタンを収集し、ボタン情報リストと一覧を再構築する。 |
| `getTouchButtonsInfoList()` | リストが空なら収集を実行し、タッチボタン情報リストを返す。 |
| `getTouchButtonList()` | リストが空なら収集を実行し、`touchButtonListener`一覧を返す。 |
| `checkStoreTouchButtonListIfListEmpty()` | どちらかのリストが空ならタッチボタン一覧を再収集する。 |
| `enableTouchPanelByName(string panelName)` | 指定名のタッチパネルを有効にする。 |
| `disableTouchPanelByName(string panelName)` | 指定名のタッチパネルを無効にする。 |
| `enableOrDisableTouchPanelByName(string panelName, bool state)` | 指定名のタッチパネルを`state`で有効/無効にする。 |
| `enableTouchPanelSchemeByName(string panelName)` | 指定名のタッチパネルスキームを有効にする。 |
| `enablePreviousTouchPanelScheme()` | 直前のタッチパネルスキームへ戻す。 |
| `enableOrDisableActionScreen(string actionScreenName)` | 指定名の画面アクションの表示を切り替える。 |
| `enableOrDisableActionScreen(string actionScreenName, bool state)` | 指定名の画面アクションを`state`で表示/非表示にする。 |
| `enableActionScreen(string actionScreenName)` | 指定名の画面アクションを表示する。 |
| `disableActionScreen(string actionScreenName)` | 指定名の画面アクションを非表示にする。 |
| `enablePreviousActionScreen()` | 直前の画面アクションへ戻す。 |
| `enableSingleActionScreen(string actionScreenName)` | 指定名の画面アクションだけを表示する。 |
| `enableOrDisableScreenActionParent(bool state)` | 画面アクションの親オブジェクトを`state`で有効/無効にする。 |
| `checkPanelsActiveOnGamepadOrKeyboard(bool checkKeyboard)` | パネル側の判定と最終押下デバイスの記録を`checkKeyboard`に従い更新する。 |
| `setScreenActionPanelsEnabledState(bool state)` | 画面アクションパネル群の有効状態を`state`に設定する。 |
| `resetButtonStateOnTouchButtonList()` | `inputManager`経由でタッチボタンの押下状態をリセットする。 |
| `setUsingPlayerMenuState(bool state)` | プレイヤーメニュー使用中フラグ`usingPlayerMenu`を設定するだけ。 |
| `isUsingPlayerMenu()` | `usingPlayerMenu`を返すだけ。 |
| `setRightSensitivityValue(float sensitivityValue)` | 右タッチジョイスティック感度`rightTouchSensitivity`を設定するだけ。 |
| `setLeftSensitivityValue(float sensitivityValue)` | 左タッチジョイスティック感度`leftTouchSensitivity`を設定するだけ。 |
| `setMouseSensitivityValue(float sensitivityValue)` | マウス感度`mouseSensitivity`を設定するだけ。 |
| `setLeftGamepadJoystickSensitivityValue(float sensitivityValue)` | 左ゲームパッドスティック感度`leftGamepadJoystickSensitivity`を設定するだけ。 |
| `setRightGamepadJoystickSensitivityValue(float sensitivityValue)` | 右ゲームパッドスティック感度`rightGamepadJoystickSensitivity`を設定するだけ。 |
| `setLeftGamepadJoystickHorizontalSensitivityValue(float sensitivityValue)` | 左スティックの水平感度`leftGamepadJoystickHorizontalSensitivity`を設定する。 |
| `setLeftGamepadJoystickVerticalSensitivityValue(float sensitivityValue)` | 左スティックの垂直感度`leftGamepadJoystickVerticalSensitivity`を設定するだけ。 |
| `setRightGamepadJoystickHorizontalSensitivityValue(float sensitivityValue)` | 右スティックの水平感度`rightGamepadJoystickHorizontalSensitivity`を設定する。 |
| `setRightGamepadJoystickVerticalSensitivityValue(float sensitivityValue)` | 右スティックの垂直感度`rightGamepadJoystickVerticalSensitivity`を設定するだけ。 |
| `isKeyboardButtonPressed(string multiAxesName, string axesName)` | プレイヤーIDと名前を`inputManager`へ渡しキーボード押下を判定する。 |
| `isUsingGamepad()` | `inputManager`へゲームパッド使用中か問い合わせて返す。 |
| `isPlayerDead()` | 直前の更新で取得した死亡状態`playerIsDead`を返すだけ。 |
| `isInputPaused()` | `inputPaused`を返すだけ。 |
| `isGameManagerPaused()` | `inputManager`へゲームマネージャーのポーズ状態を問い合わせて返す。 |
| `areTouchJoysticksPressed()` | 移動・カメラ両タッチジョイスティックのいずれかが押されているかを返す。 |
| `checkButtonPressedOnGamepadOrKeyboard(bool checkKeyboard)` | `checkKeyboard`に応じキーボード/ゲームパッドの最終押下フラグを切り替える。 |
| `openInputMenu()` | `inputManager`が未取得なら探索し、見つかれば入力メニューを開く。 |
| `setEditInputMenuOpenedState(bool state)` | `inputManager`を必要時に探索し、入力編集メニューの開閉状態を設定する。 |
| `cancelEditingInput()` | `inputManager`を必要時に探索し、入力の編集をキャンセルする。 |
| `checkIfSaveInputAfterRebind()` | `inputManager`を必要時に探索し、リバインド後の入力保存を確認する。 |
| `setNextInputPanel()` | `inputManager`を必要時に探索し、次の入力パネルへ切り替える。 |
| `setPreviousInputPanel()` | `inputManager`を必要時に探索し、前の入力パネルへ切り替える。 |
| `startEditingInput(GameObject button)` | `inputManager`を必要時に探索し、指定`button`の入力編集を開始する。 |
| `addNewAxes()` | `inputManager`のマルチ軸名を複製した新規マルチ軸を追加して更新する。 |
| `addNewAction(int multiAxesIndex)` | 指定マルチ軸へ、対応する入力マネージャーのアクション名を複製した新規アクションを追加する。 |
| `setAxesActionName(int multiAxesIndex, int axesIndex)` | 指定アクションの`actionName`を選択中インデックスの名前から設定し、未設定なら警告する。 |
| `updateMultiAxesList()` | `inputManager`のマルチ軸名と照合して各要素のインデックスと名前リストを更新する。 |
| `updateAxesList(int multiAxesListIndex)` | 指定マルチ軸内の各アクションを`inputManager`のアクション名と照合して更新する。 |
| `setAllAxesList(int multiAxesListIndex)` | 指定マルチ軸のアクション一覧を`inputManager`のアクションから作り直す。 |
| `findInputManagerAndUpdateComponent()` | `inputManager`が未設定なら探索し、見つかった場合にコンポーネントを更新する。 |
| `updateCurrentInputValues()` | ログを出し各マルチ軸の`axesCount`を再計算してコンポーネントを更新する。 |
| `setMultiAxesEnabledState(bool state)` | 全マルチ軸の`currentlyActive`を`state`に設定してコンポーネントを更新する。 |
| `setAllActionsEnabledState(int multiAxesListIndex, bool state)` | 指定マルチ軸の全アクションの`actionEnabled`を設定してコンポーネントを更新する。 |

## 内部型

- `multiAxes`（class）
- `Axes`（class）
- `inputCurrentlyActiveInfo`（class）
