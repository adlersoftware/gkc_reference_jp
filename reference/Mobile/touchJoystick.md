# touchJoystick

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Mobile/touchJoystick.cs:5`

**概要**: モバイル用の仮想ジョイスティック。タッチやマウスから軸値を求め、スティックの位置・表示・色を更新する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Finger Id | `fingerId` | `int` | 666 | – |
| Drag Distance | `dragDistance` | `float` | 1 | – |
| Snaps To Finger | `snapsToFinger` | `bool` | true | – |
| Hide On Release | `hideOnRelease` | `bool` | false | – |
| Touch Pad | `touchPad` | `bool` | – | – |
| Touch Pad Horizontal Extra Value | `touchPadHorizontalExtraValue` | `float` | 1 | – |
| Touch Pad Vertical Extra Value | `touchPadVerticalExtraValue` | `float` | 1 | – |
| Show Joystick | `showJoystick` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Clamp Joystick To Screen Side | `clampJoystickToScreenSide` | `bool` | – | – |
| Joystick On Right Screen Side | `joystickOnRightScreenSide` | `bool` | – | – |
| Check If Press Inside Touch Zone | `checkIfPressInsideTouchZone` | `bool` | – | – |
| Touch Zone Rect Transform | `touchZoneRectTransform` | `RectTransform` | – | – |

### Colors Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Chane Color | `useChaneColor` | `bool` | – | – |
| Change Color Speed | `changeColorSpeed` | `float` | – | – |
| Regular Base Color | `regularBaseColor` | `Color` | – | – |
| Regular Stick Color | `regularStickColor` | `Color` | – | – |
| Pressed Base Color | `pressedBaseColor` | `Color` | – | – |
| Pressed Stick Color | `pressedStickColor` | `Color` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Current Axis Value | `currentAxisValue` | `Vector2` | – | – |
| Current Touch Position | `currentTouchPosition` | `Vector2` | – | – |
| Touching | `touching` | `bool` | – | – |
| Hovering Joystick | `hoveringJoystick` | `bool` | – | – |
| Touching Previously | `touchingPreviously` | `bool` | – | – |
| Adjustin Colors | `adjustinColors` | `bool` | – | – |
| Button Color Visible | `buttonColorVisible` | `bool` | true | – |
| Joystick Clamped To Screen Side Active | `joystickClampedToScreenSideActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Stick Base | `stickBase` | `GameObject` | – | – |
| Stick | `stick` | `GameObject` | – | – |
| Base Rect Transform | `baseRectTransform` | `RectTransform` | – | – |
| Stick Rect Transform | `stickRectTransform` | `RectTransform` | – | – |
| Base Renderer | `baseRenderer` | `RawImage` | – | – |
| Stick Renderer | `stickRenderer` | `RawImage` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setHoverState(bool state)` | ホバー状態を保存し、タッチ開始位置がゾーン内なら指IDを取得してスティックを掴む。 |
| `GetAxis()` | 現在のスティック入力値`currentAxisValue`を返すだけ。 |
| `getRawAxis()` | `currentAxisValue`の符号だけを取り出した-1/0/1の軸値を返す。 |
| `setTouchPadState(bool state)` | `touchPad`を設定するだけ。 |
| `setShowJoystickState(bool state)` | `showJoystick`を設定し、ベースとスティックの表示を切り替える。 |
| `setSnapsToFingerState(bool state)` | `snapsToFinger`を設定するだけ。 |
| `setHideOnReleaseState(bool state)` | `hideOnRelease`を設定するだけ。 |
| `setJoystickColorVisibleState(bool state)` | `buttonColorVisible`を設定し、ベースとスティックの色のアルファを表示・非表示に合わせる。 |
| `touchJoystickIsPressed()` | 指で触れているか`touching`を返すだけ。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static Touch convertMouseIntoFinger()` | – |
| `static bool checkTouchPlatform()` | – |
