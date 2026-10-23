# computerDevice

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/computerDevice.cs:11`

**概要**: パスワード入力式の端末。押されたキーを画面のコード文字列へ反映し、Enterで照合して一致時にアンロック状態へ切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Locked | `locked` | `bool` | – | – |
| Code | `code` | `string` | – | – |
| Unlocked Color | `unlockedColor` | `Color` | – | – |
| Number Letter To Start To Move Password Text | `numberLetterToStartToMovePasswordText` | `int` | – | – |
| Password Text Move Distace Per Letter | `passwordTextMoveDistacePerLetter` | `float` | – | – |
| Allow To Use Keyboard | `allowToUseKeyboard` | `bool` | – | – |
| Disable Use Device Action Button | `disableUseDeviceActionButton` | `bool` | – | – |

### Sound Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Wrong Pass Sound | `wrongPassSound` | `AudioClip` | – | – |
| Wrong Pass Audio Element | `wrongPassAudioElement` | `AudioElement` | – | – |
| Corret Pass Sound | `corretPassSound` | `AudioClip` | – | – |
| Corret Pass Audio Element | `corretPassAudioElement` | `AudioElement` | – | – |
| Key Press Sound | `keyPressSound` | `AudioClip` | – | – |
| Key Press Audio Element | `keyPressAudioElement` | `AudioElement` | – | – |

### Allowed Key List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Allowed Keys List | `allowedKeysList` | `List<string>` | new List<string> () | – |

### Text Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Password Text | `passwordText` | `string` | "Password" | – |
| Unlocked Text | `unlockedText` | `string` | "Unlocked" | – |
| Left Shift Key | `leftShiftKey` | `string` | "leftshift" | – |
| Number Key | `numberKey` | `string` | "alpha" | – |
| Space Key | `spaceKey` | `string` | "space" | – |
| Delete Key | `deleteKey` | `string` | "delete" | – |
| Back Space Key | `backSpaceKey` | `string` | "backspace" | – |
| Enter Key | `enterKey` | `string` | "enter" | – |
| Return Key | `returnKey` | `string` | "return" | – |
| Caps Lock Key | `capsLockKey` | `string` | "capslock" | – |

### Debug Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Using Device | `usingDevice` | `bool` | – | – |
| Print Keys Pressed | `printKeysPressed` | `bool` | – | – |
| Keys List | `keysList` | `List<Image>` | new List<Image> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Computer Unlocked | `useEventOnComputerUnlocked` | `bool` | – | – |
| Event On Computer Unlocked | `eventOnComputerUnlocked` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Keyboard | `keyboard` | `GameObject` | – | – |
| Current Code | `currentCode` | `Text` | – | – |
| State Text | `stateText` | `Text` | – | – |
| Computer Locked Content | `computerLockedContent` | `GameObject` | – | – |
| Computer Unlocked Content | `computerUnlockedContent` | `GameObject` | – | – |
| Wall Paper | `wallPaper` | `Image` | – | – |
| Audio Source | `audioSource` | `AudioSource` | – | – |
| Device Manager | `deviceManager` | `electronicDevice` | – | – |
| Input | `input` | `inputManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateComputer()` | `usingDevice`を反転し、`disableUseDeviceActionButton`時はプレイヤーの使用ボタン有効状態も切り替える。 |
| `checkKeyPressed(string keyPressed)` | 押下キーを許可リストと照合して入力文字列を編集し、Enter時に`code`と一致すれば`enableAccessToCompturer`を呼ぶ。 |
| `unlockComputer()` | 画面切替フラグ`changeScreen`を立てるだけ。 |
| `enableAccessToCompturer()` | 正解音を鳴らし`unlocked`と表示を更新して`unlockObject`を呼び、解除イベントを発火する。 |
| `unlockComputerWithUsb()` | `unlockComputer`と`enableAccessToCompturer`を続けて呼び、USBによる解除を反映する。 |
| `playSound(AudioElement clipToPlay)` | `clipToPlay`が未設定でなければ`AudioPlayer.PlayOneShot`で再生する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnComputerUnlocked` | `UnityEvent` | – |
