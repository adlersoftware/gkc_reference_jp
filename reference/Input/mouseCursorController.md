# mouseCursorController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Input/mouseCursorController.cs:6`

**概要**: ゲームパッドの軸入力でマウスカーソルを動かすコントローラ。右/左スティックの入力を`SetCursorPos` で実カーソルへ反映し、表示状態と速度を管理する。

**公式ドキュメント抜粋**（[Mouse Cursor Controller](../../docs/toplevelcomponents/player-and-game-management/mouse-cursor-controller.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Mouse Cursor Enabled | `useMouseCursorEnabled` | `bool` | true | – |
| Use Smooth Cursor Speed On Game | `useSmoothCursorSpeedOnGame` | `bool` | true | – |
| Cursor Speed On Game | `cursorSpeedOnGame` | `float` | 400 | – |
| Cursor Speed On Pause Menu | `cursorSpeedOnPauseMenu` | `float` | 7 | – |
| Cursor Lerp Speed | `cursorLerpSpeed` | `float` | 10 | – |
| Enable Gamepad Cursor On Pause | `enableGamepadCursorOnPause` | `bool` | true | – |
| Time To Reset Cursor After Disable | `timeToResetCursorAfterDisable` | `float` | 1 | – |
| Use Mouse Limits | `useMouseLimits` | `bool` | true | – |
| Activate Cursor On Start | `activateCursorOnStart` | `bool` | – | – |
| Use Fixed Time Enabled | `useFixedTimeEnabled` | `bool` | – | – |

### Input Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Horizontal X String | `horizontalXString` | `string` | "Horizontal X" | – |
| Vertical Y String | `verticalYString` | `string` | "Vertical Y" | – |
| Mouse X String | `mouseXString` | `string` | "Mouse X" | – |
| Mouse Y String | `mouseYString` | `string` | "Mouse Y" | – |
| Button Index | `buttonIndex` | `int` | 0 | – |
| Joystick Number | `joystickNumber` | `int` | 1 | – |
| Use Right Joystick Axis | `useRightJoystickAxis` | `bool` | true | – |
| Use Both Joysticks | `useBothJoysticks` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Ignore Mouse Cursor Update Active | `ignoreMouseCursorUpdateActive` | `bool` | – | – |
| Use Try Catch On Update Cursor Active | `useTryCatchOnUpdateCursorActive` | `bool` | – | – |
| Current Mouse Speed | `currentMouseSpeed` | `float` | – | – |
| Current Resolution | `currentResolution` | `Vector2` | – | – |
| Cursor Position | `cursorPosition` | `Vector2` | – | – |
| Using Actual Mouse | `usingActualMouse` | `bool` | – | – |
| Screen Focused | `screenFocused` | `bool` | – | – |
| Cursor Currently Active | `cursorCurrentlyActive` | `bool` | – | – |
| Cursor Previously Active | `cursorPreviouslyActive` | `bool` | – | – |
| Mouse Limits | `mouseLimits` | `Vector2` | – | – |
| Horizontal Limit Configured | `horizontalLimitConfigured` | `bool` | – | – |
| Vertical Limit Configured | `verticalLimitConfigured` | `bool` | – | – |
| Real Mouse Axis Input | `realMouseAxisInput` | `Vector2` | – | – |
| Axis Input | `axisInput` | `Vector2` | – | – |
| Ignore Set Selected Game Object On UI By Gamepad | `ignoreSetSelectedGameObjectOnUIByGamepad` | `bool` | – | – |
| Player Input Located | `playerInputLocated` | `bool` | – | – |
| Input Located | `inputLocated` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Input | `playerInput` | `playerInputManager` | – | – |
| Input | `input` | `inputManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 未初期化なら自身を`Instance` に登録し、既に別インスタンスがあれば自身のGameObjectを破棄する。 |
| `getComponentInstanceOnApplicationPlaying()` | 再生中のみ`getComponentInstance` を呼ぶだけ。 |
| `showOrHideMouseController(playerInputManager newInput, bool state, int newJoystickNumber, bool pausingGame)` | 入力がnullかキーボード専用でない場合に限り`playerInput` とジョイスティック番号を更新し、表示切替本体を呼ぶ。 |
| `setIgnoreSetSelectedGameObjectOnUIByGamepadState(bool state)` | `ignoreSetSelectedGameObjectOnUIByGamepad` を`state`にするだけ。 |
| `showOrHideMouseController(bool state, bool pausingGame)` | ゲームパッド使用時のみカーソル状態と前回状態を更新し、必要なら位置をリセットしてUIへフォーカスを当てる。 |
| `resetCursorPosition()` | 実カーソル位置を取得して内部座標を合わせ、初回は画面解像度から移動リミットを設定する。 |
| `getCursorPos()` | `cursorPos` を返すだけ。 |
| `setUseRightOrLeftJoysticsAxis(bool state)` | `useRightJoystickAxis` を`state`にするだけ。 |
| `getCurrentJoystickNumber()` | `joystickNumber` を返すだけ。 |
| `setMouseCursorControllerSpeedOnGameValue(float newValue)` | 初回だけ元の速度を退避してから`cursorSpeedOnGame` を`newValue`に更新する。 |
| `setOriginalMouseCursorControllerSpeedOnGameValue()` | 退避した元の速度があれば`setMouseCursorControllerSpeedOnGameValue` で戻すだけ。 |
| `getMouseAxis()` | `playerInput` があればカーソル状態に応じたマウス軸を、無ければ`Input.GetAxis` の合成値を返す。 |
| `getMovementAxis()` | `playerInput` があればカーソル状態に応じた移動軸を、無ければ`Input.GetAxis` の合成値を返す。 |

## 内部型

- `Point`（struct）
