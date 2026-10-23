# interactionObjectMessage

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/interactionObjectMessage.cs:6`

**概要**: トリガー内のプレイヤーへメッセージを表示するデバイス。任意でカメラ移動、操作停止、開始/終了イベントも行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Message | `message` | `string` | – | TextArea (3, 10) |
| Using Device | `usingDevice` | `bool` | – | – |
| Tag To Detect | `tagToDetect` | `List<string>` | new List<string> () | – |
| Pause Player While Reading | `pausePlayerWhileReading` | `bool` | – | – |
| Press Second Time To Stop Reading | `pressSecondTimeToStopReading` | `bool` | – | – |
| Show Message Time | `showMessageTime` | `float` | – | – |
| Move Camera To Position | `moveCameraToPosition` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Message Removed | `messageRemoved` | `bool` | – | – |
| Interaction Used | `interactionUsed` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Call Event On Interaction | `callEventOnInteraction` | `bool` | – | – |
| Call Event On Every Interaction | `callEventOnEveryInteraction` | `bool` | – | – |
| Event On Interaction | `eventOnInteraction` | `UnityEvent` | – | – |
| Event On End Interaction | `eventOnEndInteraction` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Collider | `mainCollider` | `Collider` | – | – |
| Camera Movement Manager | `cameraMovementManager` | `moveCameraToDevice` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateDevice()` | 使用状態を反転し、メッセージの表示/停止、カメラ移動、操作停止、イベント発火を行う。 |
| `checkTriggerInfo(Collider col, bool isEnter)` | タグ一致時、入場でプレイヤー各コンポーネントを取得し、退場でプレイヤー参照を解除する。 |
| `setDeviceState(bool state)` | プレイヤーの操作停止とポーズ状態を設定し、`state`に応じ制御スクリプトを停止/再開する。 |
| `removeMessage()` | `messageRemoved`を立て、デバイス一覧から自身を外してコライダーを無効化する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnInteraction` | `UnityEvent` | – |
| `eventOnEndInteraction` | `UnityEvent` | – |
