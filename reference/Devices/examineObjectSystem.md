# examineObjectSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/examineObjectSystem.cs:8`

**概要**: オブジェクトをカメラ前に寄せ、回転・ズームで調べるためのデバイス。調べポイント押下の順序判定、メッセージ、イベント、使用終了や無効化を受け持つ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Can Be Rotated | `objectCanBeRotated` | `bool` | – | – |
| Rotation Speed | `rotationSpeed` | `float` | – | – |
| Horizontal Rotation Enabled | `horizontalRotationEnabled` | `bool` | true | – |
| Vertical Rotation Enabled | `verticalRotationEnabled` | `bool` | true | – |
| Zoom Can Be Used | `zoomCanBeUsed` | `bool` | – | – |
| Rotation Enabled | `rotationEnabled` | `bool` | true | – |
| Activate Action Screen | `activateActionScreen` | `bool` | true | – |
| Action Screen Name | `actionScreenName` | `string` | "Examine Object" | – |
| Use Examine Message | `useExamineMessage` | `bool` | – | – |
| Examine Message | `examineMessage` | `string` | – | TextArea (1, 10) |

### Press Positions Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Press Places In Order | `pressPlacesInOrder` | `bool` | – | – |
| Current Place Pressed Index | `currentPlacePressedIndex` | `int` | – | – |
| Use Incorrect Place Pressed Message | `useIncorrectPlacePressedMessage` | `bool` | – | – |
| Incorrect Place Pressed Message | `incorrectPlacePressedMessage` | `string` | – | TextArea (1, 10) |
| Incorrect Place Pressed Message Duration | `incorrectPlacePressedMessageDuration` | `float` | – | – |

### Canvas Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Uses Canvas | `objectUsesCanvas` | `bool` | – | – |
| Main Canvas | `mainCanvas` | `Canvas` | – | – |
| Use Trigger On Top Of Canvas | `useTriggerOnTopOfCanvas` | `bool` | – | – |
| Trigger On Top Of Canvas | `triggerOnTopOfCanvas` | `GameObject` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Using Device | `usingDevice` | `bool` | – | – |
| Current Player | `currentPlayer` | `GameObject` | – | – |
| Rotation Paused | `rotationPaused` | `bool` | – | – |

### Examine Place List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Examine Place List | `examinePlaceList` | `List<examinePlaceInfo>` | new List<examinePlaceInfo> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Secundary Cancel Examine Function | `useSecundaryCancelExamineFunction` | `bool` | – | – |
| Secundary Cancel Examine Function | `secundaryCancelExamineFunction` | `UnityEvent` | new UnityEvent () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Transform | `objectTransform` | `Transform` | – | – |
| Move Device To Camera Manager | `moveDeviceToCameraManager` | `moveDeviceToCamera` | – | – |
| Electronic Device Manager | `electronicDeviceManager` | `electronicDevice` | – | – |
| Main Collider | `mainCollider` | `Collider` | – | – |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `showExamineMessage(bool state)` | `showingMessage` を更新し、プレイヤー取得後にメッセージ表示か停止を呼ぶ。 |
| `stopExamineDevice()` | `usingDevicesManager` があれば `useDevice` を呼び調べる操作を終える。 |
| `disableAndRemoveExamineDevice()` | デバイストリガー無視とコライダー無効化を行い、リストから外して調べられなくする。 |
| `cancelExamine()` | `secundaryCancelExamineFunction` に永続リスナーがあるとき発火するだけ。 |
| `pauseOrResumePlayerInteractionButton(bool state)` | `state` の逆値で使用ボタンの有効状態を設定するだけ。 |
| `examineDevice()` | `usingDevice` を反転し、開始時はプレイヤー取得、終了時はメッセージ解除と回転再開、アクション画面も同期する。 |
| `setExamineDeviceState(bool state)` | `usingDevice` を `state` にし、false ならタッチと回転停止を解除、プレイヤー側状態も更新する。 |
| `setRotationState(bool state)` | `rotationPaused` を `!state` にして回転の一時停止を切り替えるだけ。 |
| `getPlayerComponents()` | 現在のプレイヤーから各マネージャと調べ用カメラを取得し、自分を調べ対象として登録する。 |
| `checkExaminePlaceInfo(Transform examinePlaceToCheck)` | 一致する調べポイントの順序判定・メッセージ・イベント・使用終了・無効化・効果音をまとめて実行する。 |
| `setExaminePlaceEnabledState(Transform examinePlaceToCheck)` | `examinePlaceToCheck` に一致する調べポイントを `elementPlaceDisabled` にするだけ。 |
| `inputSetZoomValue(bool state)` | 調べ中で回転操作が有効かつ `zoomCanBeUsed` のとき、`changeDeviceZoom` でズームを切り替える。 |
| `inputResetRotation()` | 調べ中で回転・ズームが有効なとき `resetRotation` を呼び回転を初期化する。 |
| `inputResetRotationAndPosition()` | 同じ条件で `resetRotationAndPosition` を呼び、回転と位置を戻す。 |
| `inputCancelExamine()` | 調べ中かつ `useSecundaryCancelExamineFunction` のとき `cancelExamine` を呼ぶ。 |
| `inputCheckIfMessage()` | 調べ中で `useExamineMessage` が有効なとき、メッセージ表示を反転させる。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `secundaryCancelExamineFunction` | `UnityEvent` | – |

## 内部型

- `examinePlaceInfo`（class）
