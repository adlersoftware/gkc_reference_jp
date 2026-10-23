# pressMultipleKeysActionInputSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Input/pressMultipleKeysActionInputSystem.cs:6`

**概要**: 複数キーの同時押しや順番押しを数え、規定数に達したらイベントを発火するシステム。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Press Keys Enabled | `checkPressKeysEnabled` | `bool` | true | – |
| Number Of Keys To Press | `numberOfKeysToPress` | `int` | – | – |
| Reset Number Of Keys Pressed At End | `resetNumberOfKeysPressedAtEnd` | `bool` | – | – |
| Press Keys In Order | `pressKeysInOrder` | `bool` | – | – |

### Reset Keys Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Reset Number Of Keys Pressed If Not Correct Order | `resetNumberOfKeysPressedIfNotCorrectOrder` | `bool` | – | – |
| Reset Number Of Keys After Delay | `resetNumberOfKeysAfterDelay` | `bool` | – | – |
| Max Delay To Press Keys | `maxDelayToPressKeys` | `float` | – | – |
| Cancel Action If Max Delay Reached | `cancelActionIfMaxDelayReached` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Number Of Keys Pressed | `currentNumberOfKeysPressed` | `int` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Use On Keys Pressed | `eventToUseOnKeysPressed` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPressedKeyState(bool state)` | 押下でカウントを増減し、規定数に達したら`eventToUseOnKeysPressed` を発火、設定に応じてカウントを戻す。 |
| `setPressedKeyStateInOrder(int pressedKeyID)` | カウントと`pressedKeyID` が一致すれば増やし、不一致なら設定に応じてリセット、規定数でイベントを発火する。 |
| `setCheckPressKeysEnabledState(bool state)` | `checkPressKeysEnabled` を`state`にするだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToUseOnKeysPressed` | `UnityEvent` | – |
