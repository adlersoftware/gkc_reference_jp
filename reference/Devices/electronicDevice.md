# electronicDevice

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/electronicDevice.cs:8`

**概要**: Action System で使う端末の使用状態を管理し、プレイヤーのトリガー進入/退出、カメラ移動、使用開始/停止イベントを処理する。`usingDevicesSystem` のデバイス一覧への登録・解除も担う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Tag | `playerTag` | `string` | "Player" | プレイヤー判定に使うタグ。このタグを持つコライダーだけが使用者として登録される。 |
| Use Only For Trigger | `useOnlyForTrigger` | `bool` | – | オンにすると侵入時に指定関数を呼ぶだけで、使用状態を切り替えない。 |
| Function To Set Player | `functionToSetPlayer` | `string` | – | 侵入時にプレイヤーへ送る`SendMessage`の関数名。 |
| Activate Device On Trigger Enter | `activateDeviceOnTriggerEnter` | `bool` | – | オンにするとプレイヤーが触れた時点で自動的にデバイスを使用状態にする。 |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Move Camera To Device | `useMoveCameraToDevice` | `bool` | – | オンにするとデバイス使用時にカメラをデバイス位置へ移動させる。 |
| Disable Device When Stop Using | `disableDeviceWhenStopUsing` | `bool` | – | オンにするとプレイヤーがトリガーから離れた時に使用を終了する。 |
| Stop Using Device When Unlock | `stopUsingDeviceWhenUnlock` | `bool` | – | オンにするとロック解除の通知を受けた時にデバイスの使用を終了する。 |
| Disable And Remove Device When Unlock | `disableAndRemoveDeviceWhenUnlock` | `bool` | – | オンにするとロック解除時にデバイスを操作対象リストから外す。 |
| Disable Device Interaction After Using Once | `disableDeviceInteractionAfterUsingOnce` | `bool` | – | オンにすると一度使用を終えると操作対象から外し、再使用できなくする。 |

### Camera Component Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Movement Manager | `cameraMovementManager` | `moveCameraToDevice` | – | カメラをデバイスへ移動させる`moveCameraToDevice`への参照。 |
| Device Movement Manager | `deviceMovementManager` | `moveDeviceToCamera` | – | デバイス自体をカメラ位置へ移動させる`moveDeviceToCamera`への参照。 |

### Free Interaction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Free Interaction | `useFreeInteraction` | `bool` | – | オンにすると使用中の再操作で状態を切り替えず、自由操作イベントだけを実行する。 |
| Use Free Interaction Event | `useFreeInteractionEvent` | `bool` | – | オンにすると自由操作時に`freeInteractionEvent`を実行する。 / 表示条件: `useFreeInteraction` がオンのとき |
| Free Interaction Event | `freeInteractionEvent` | `UnityEvent` | – | 自由操作時に呼び出すイベント。 / 表示条件: `useFreeInteraction.boolValue && useFreeInteractionEvent.boolValue` |

### Activate Device Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Function To Use Device | `functionToUseDevice` | `UnityEvent` | new UnityEvent () | 使用状態が切り替わるたびに呼び出されるイベント。 |

### Device State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | オンにすると状態遷移のデバッグログをコンソールに出力する。 |

### Activate Event If Unable To Use Device Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Event If Unable To Use Device | `activateEventIfUnableToUseDevice` | `bool` | – | オンにすると使用不可の時に`unableToUseDeviceEvent`を実行する。 |
| Unable To Use Device Event | `unableToUseDeviceEvent` | `UnityEvent` | new UnityEvent () | デバイスが使用できない時に実行するイベント。 / 表示条件: `activateEventIfUnableToUseDevice` がオンのとき |

### Unlock Function Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Unlock Function Call | `unlockFunctionCall` | `UnityEvent` | new UnityEvent () | ロック解除時に実行するイベント。 |

### Lock Function Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Lock Function Call | `lockFunctionCall` | `UnityEvent` | new UnityEvent () | ロック時に実行するイベント。 |

### Activate Event On Trigger Stay Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Event On Trigger Stay | `activateEventOnTriggerStay` | `bool` | – | オンにするとプレイヤーがトリガー内にいる間、一定間隔でイベントを実行する。 |
| Trigger Stay Event | `triggerStayEvent` | `UnityEvent` | new UnityEvent () | プレイヤーがトリガー内にいる間に繰り返し実行するイベント。 / 表示条件: `activateEventOnTriggerStay` がオンのとき |
| Event On Trigger Stay Rate | `eventOnTriggerStayRate` | `float` | – | トリガー滞在中にイベントを繰り返す間隔（秒）。 / 表示条件: `activateEventOnTriggerStay` がオンのとき |

### Activate Event On Trigger Enter Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Event On Trigger Enter | `activateEventOnTriggerEnter` | `bool` | – | オンにするとプレイヤーがトリガーに入った時にイベントを実行する。 |
| Trigger Enter Event | `triggerEnterEvent` | `UnityEvent` | new UnityEvent () | プレイヤーがトリガーに入った時に実行するイベント。 / 表示条件: `activateEventOnTriggerEnter` がオンのとき |
| Send Player On Trigger Enter | `sendPlayerOnTriggerEnter` | `bool` | – | オンにすると侵入時にプレイヤーを引数としてイベントに渡す。 |
| Event To Send Player On Trigger Enter | `eventToSendPlayerOnTriggerEnter` | `eventParameters.eventToCallWithGameObject` | – | トリガー侵入時にプレイヤーを引数に受け取るイベント。 / 表示条件: `sendPlayerOnTriggerEnter` がオンのとき |

### Activate Event On Trigger Exit Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Event On Trigger Exit | `activateEventOnTriggerExit` | `bool` | – | オンにするとプレイヤーがトリガーから出た時にイベントを実行する。 |
| Trigger Exit Event | `triggerExitEvent` | `UnityEvent` | new UnityEvent () | プレイヤーがトリガーから出た時に実行するイベント。 / 表示条件: `activateEventOnTriggerExit` がオンのとき |
| Send Player On Trigger Exit | `sendPlayerOnTriggerExit` | `bool` | – | オンにすると退出時にプレイヤーを引数としてイベントに渡す。 |
| Event To Send Player On Trigger Exit | `eventToSendPlayerOnTriggerExit` | `eventParameters.eventToCallWithGameObject` | – | トリガー退出時にプレイヤーを引数に受け取るイベント。 / 表示条件: `sendPlayerOnTriggerExit` がオンのとき |

### Send Current Player On Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Send Current Player On Event | `sendCurrentPlayerOnEvent` | `bool` | – | オンにするとプレイヤー発見時に現在のプレイヤーをイベントに渡す。 |
| Set Current Player Event | `setCurrentPlayerEvent` | `eventParameters.eventToCallWithGameObject` | – | プレイヤー発見時に現在のプレイヤーを引数に受け取るイベント。 / 表示条件: `sendCurrentPlayerOnEvent` がオンのとき |

### Start/Stop Using Device Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Start Using Device | `useEventOnStartUsingDevice` | `bool` | – | オンにすると使用開始時に`eventOnStartUsingDevice`を実行する。 |
| Event On Start Using Device | `eventOnStartUsingDevice` | `UnityEvent` | – | デバイスの使用開始時に実行するイベント。 / 表示条件: `useEventOnStartUsingDevice` がオンのとき |
| Use Event On Stop Using Device | `useEventOnStopUsingDevice` | `bool` | – | オンにすると使用終了時に`eventOnStopUsingDevice`を実行する。 |
| Event On Stop Using Device | `eventOnStopUsingDevice` | `UnityEvent` | – | デバイスの使用終了時に実行するイベント。 / 表示条件: `useEventOnStopUsingDevice` がオンのとき |

### Condition Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Condition System To Start Device | `useConditionSystemToStartDevice` | `bool` | – | オンにすると使用開始前に開始用の条件を判定し、未達なら開始しない。 |
| Main GKC Condition Info To Start Device | `mainGKCConditionInfoToStartDevice` | `GKCConditionInfo` | – | 使用開始を許可するか判定する条件。未達なら開始を中止する。 / 表示条件: `useConditionSystemToStartDevice` がオンのとき |
| Use Condition System To Stop Device | `useConditionSystemToStopDevice` | `bool` | – | オンにすると使用終了前に終了用の条件を判定し、未達なら終了しない。 |
| Main GKC Condition Info To Stop Device | `mainGKCConditionInfoToStopDevice` | `GKCConditionInfo` | – | 使用終了を許可するか判定する条件。未達なら終了を中止する。 / 表示条件: `useConditionSystemToStopDevice` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `usingDevice` | `bool` | – | – |
| `currentPlayer` | `GameObject` | – | – |
| `deviceCanBeUsed` | `bool` | true | – |
| `playerInside` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateDevice()` | `deviceCanBeUsed` と条件を確認し、`usingDevice` を反転して `setDeviceState` を呼ぶ。 |
| `setDeviceState(bool state)` | `usingDevice` を `state` にして `functionToUseDevice` と開始・停止イベントを実行する。 |
| `moveCamera(bool state)` | カメラ/デバイス移動マネージャの `moveCamera` を呼び、引数ではなく `usingDevice` を渡す。 |
| `setCurrentUser(GameObject newPlayer)` | 未使用時のみ `currentPlayer` を `newPlayer` にし、両移動マネージャへも通知する。 |
| `setPlayerManually(GameObject newPlayer)` | `newPlayer` の `Collider` を取得して `checkTriggerInfo` を進入扱いで呼ぶだけ。 |
| `checkTriggerInfo(Collider col, bool isEnter)` | プレイヤーの進入/退出で `playerFoundList`・`currentPlayer`・使用状態・各イベントを更新する。 |
| `setUsingDeviceState(bool state)` | `usingDevice` を `state` に設定するだけ。 |
| `getCurrentPlayer()` | 現在の使用者 `currentPlayer` を返すだけ。 |
| `unlockObject()` | `unlockFunctionCall` を実行し、設定時はデバイスを一覧から削除する。 |
| `lockObject()` | `lockFunctionCall` が登録されていれば実行するだけ。 |
| `removeDeviceFromListWithoutDisablingDevice()` | デバイスを無効化せず、発見済みプレイヤー全員の使用リストから外す。 |
| `clearDeviceList()` | 発見済みプレイヤー全員の `usingDevicesSystem` のデバイス一覧を空にする。 |
| `addDeviceToList()` | 発見済みプレイヤー全員の使用リストへ、重複しないよう自身を追加する。 |
| `removeDeviceFromList()` | 各プレイヤーの使用リストから外し、自身のタグを `Untagged` にする。 |
| `removeDeviceFromListOnAllPlayersOnSceneWithoutDisablingDevice()` | `GKC_Utils` の同名処理を呼び、無効化せず全プレイヤーのリストから外す。 |
| `removeDeviceFromListExternalCall()` | 各プレイヤーの `removeDeviceFromListExternalCall` を呼び、タグを `Untagged` にする。 |
| `stopUsindDevice()` | `stopUsingDeviceWhenUnlock` が有効なときだけ `setDeviceState(false)` を呼ぶ。 |
| `stopUseDeviceToPlayer()` | `currentPlayer` の `usingDevicesSystem.useDevice` を呼んで使用を終了させる。 |
| `reloadDeviceStringActionOnPlayer()` | 各プレイヤーの `reloadDeviceStringActionOnPlayer` を自身を対象に呼ぶ。 |
| `setDeviceCanBeUsedState(bool state)` | `deviceCanBeUsed` を `state` に設定するだけ。 |
| `cancelUseElectronicDevice()` | 使用中の場合のみ `activateDevice` を呼んで使用を取消す。 |
| `useDeviceObjectExternally(GameObject currentPlayer)` | `GKC_Utils.useDeviceObjectExternally` にプレイヤーと自身を渡して外部から使用させる。 |
| `useDeviceObjectExternallyForCharacterInside()` | `currentPlayer` がいれば `GKC_Utils.useDeviceObjectExternally` で外部使用させる。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `freeInteractionEvent` | `UnityEvent` | – |
| `functionToUseDevice` | `UnityEvent` | – |
| `unlockFunctionCall` | `UnityEvent` | – |
| `lockFunctionCall` | `UnityEvent` | – |
| `triggerStayEvent` | `UnityEvent` | – |
| `triggerEnterEvent` | `UnityEvent` | – |
| `triggerExitEvent` | `UnityEvent` | – |
| `unableToUseDeviceEvent` | `UnityEvent` | – |
| `eventOnStartUsingDevice` | `UnityEvent` | – |
| `eventOnStopUsingDevice` | `UnityEvent` | – |
