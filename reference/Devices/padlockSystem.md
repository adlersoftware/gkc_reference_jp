# padlockSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/padlockSystem.cs:11`

**概要**: 数字ホイール式の南京錠で、タッチ・キーボード・マウスホイールの入力から現在のコードを組み立てる。`correctCode` と一致すると解錠して `unlockObject` を呼ぶ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Code On Wheels | `currentCodeOnWheels` | `string` | – | – |
| Correct Code | `correctCode` | `string` | – | – |
| Rotate Wheel Speed | `rotateWheelSpeed` | `float` | – | – |
| Numbers Per Wheel | `numbersPerWheel` | `int` | – | – |
| Wait Delay After Unlock | `waitDelayAfterUnlock` | `float` | – | – |

### Interaction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Allow To Use Keyboard | `allowToUseKeyboard` | `bool` | – | – |
| Use Swipe To Rotate Wheels | `useSwipeToRotateWheels` | `bool` | – | – |
| Min Swipe Dist | `minSwipeDist` | `float` | – | – |
| Use Swipe And Click For Wheels | `useSwipeAndClickForWheels` | `bool` | – | – |
| Allow Keyboard Controls | `allowKeyboardControls` | `bool` | – | – |
| Use Mouse Wheel To Rotate Active | `useMouseWheelToRotateActive` | `bool` | true | – |

### Wheel Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Wheels | `wheels` | `List<wheelInfo>` | new List<wheelInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Device | `usingDevice` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Unlock | `useEventsOnUnlock` | `bool` | – | – |
| Event On Unlock | `eventOnUnlock` | `UnityEvent` | – | – |
| Call Events After Activate Unlock | `callEventsAfterActivateUnlock` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Reset Button | `resetButton` | `GameObject` | – | – |
| Resolve Button | `resolveButton` | `GameObject` | – | – |
| Corret Pass Sound | `corretPassSound` | `AudioClip` | – | – |
| Corret Pass Audio Element | `corretPassAudioElement` | `AudioElement` | – | – |
| Key Press Sound | `keyPressSound` | `AudioClip` | – | – |
| Key Press Audio Element | `keyPressAudioElement` | `AudioElement` | – | – |
| Current Wheel Mark | `currentWheelMark` | `Transform` | – | – |
| Current Wheel Mark Offset | `currentWheelMarkOffset` | `Vector3` | – | – |
| Audio Source | `audioSource` | `AudioSource` | – | – |
| Device Manager | `deviceManager` | `electronicDevice` | – | – |
| Examine Object Manager | `examineObjectManager` | `examineObjectSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentWheelIndex(int amount)` | `amount` だけホイール番号を加算し折り返して、`currentWheelMark` をその位置へ動かす。 |
| `setPreviousNumber()` | 回転方向を 1 にして、`checkNumber` に -1 を渡し前の数字へ回す。 |
| `setNextNumber()` | 回転方向を -1 にして、`checkNumber` に -1 を渡し次の数字へ回す。 |
| `activatePadlock()` | `usingDevice` を反転し、開始時はプレイヤーと入力管理を取得して自分を現在のパドロックに登録する。 |
| `checkNumberByKeyboard(int number)` | ホイール回転中なら無視し、指定数字を設定してから次のホイールへ選択を移す。 |
| `checkNumber(wheelInfo wheel, int wheelNumber)` | ホイールの数字を設定または増減して回転を始め、コード更新後に `correctCode` と一致すれば解錠する。 |
| `getCurrentCodeOnWheels()` | 各ホイールの `currentNumber` を連結した文字列を返すだけ。 |
| `setLockedState(bool state)` | `state` が true なら正解音・`unlocked`・コライダー無効化・解錠イベント・`unlockObject`・使用終了を実行する。 |
| `checkRotateWheel(int direction, wheelInfo wheel, int number)` | 引数をそのまま渡して `rotateCenter` コルーチンを開始するだけ。 |
| `rotateCenter(int direction, wheelInfo wheel, int number)` | `number` から目標角度を求めて Slerp 回転し、`wheelRotating` とリセット状態を解除する。 |
| `resetPadLock()` | `resetingPadlock` を立てて全ホイールを 0 に戻し、選択番号を先頭へ戻す。 |
| `setCorrectCode()` | `resetingPadlock` を立てて `correctCode` の各桁をホイールに設定し、選択を先頭へ戻す。 |
| `changeExamineObjectState(bool state)` | `examineObjectManager` があれば `setExamineDeviceState` を呼ぶだけ。 |
| `inputRotateWheel(bool directionUp)` | マウスホイール回転が有効なとき、現在のホイールを `directionUp` で次か前の数字へ回す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnUnlock` | `UnityEvent` | – |

## 内部型

- `wheelInfo`（class）
