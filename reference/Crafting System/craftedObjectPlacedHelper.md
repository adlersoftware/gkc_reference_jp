# craftedObjectPlacedHelper

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Crafting System/craftedObjectPlacedHelper.cs:6`

**概要**: 設置済みオブジェクトに付く補助コンポーネント。設置/回収イベント、設置状態、回収可否、ステーション接続解除の伝播を提供する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Name | `objectName` | `string` | – | – |
| Main Game Object | `mainGameObject` | `GameObject` | – | – |
| Object Can Be Taken Back To Inventory Enabled | `objectCanBeTakenBackToInventoryEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Placed | `objectPlaced` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Place Or Take Back Object | `useEventsOnPlaceOrTakeBackObject` | `bool` | – | – |
| Event On Place Object | `eventOnPlaceObject` | `UnityEvent` | – | – |
| Event On Take Back Object | `eventOnTakeBackObject` | `UnityEvent` | – | – |
| Use Events To Send Player On Place Or Take Back Object | `useEventsToSendPlayerOnPlaceOrTakeBackObject` | `bool` | – | – |
| Events To Send Player On Place Object | `eventsToSendPlayerOnPlaceObject` | `eventParameters.eventToCallWithGameObject` | – | – |
| Events To Send Player On Take Back Object | `eventsToSendPlayerOnTakeBackObject` | `eventParameters.eventToCallWithGameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getObjectName()` | `objectName`を返すだけ。 |
| `getObject()` | `mainGameObject`を返すだけ。 |
| `checkEventsOnStateChange(bool state)` | イベント有効時のみ、trueで設置イベント、falseで回収イベントを発火する。 |
| `checkStateOnTakeObjectBack()` | `mainGameObject`に`craftingStationSystem`があれば、その回収時状態チェックを呼ぶ。 |
| `checkEventsOnStateChangeWithPlayer(bool state, GameObject currentPlayer)` | プレイヤー付きイベント有効時のみ、設置/回収イベントに`currentPlayer`を渡して発火する。 |
| `setObjectPlacedState(bool state)` | `objectPlaced`を設定するだけ。 |
| `isObjectPlaced()` | `objectPlaced`を返すだけ。 |
| `setObjectCanBeTakenBackToInventoryEnabledState(bool state)` | `objectCanBeTakenBackToInventoryEnabled`を設定するだけ。 |
| `isObjectCanBeTakenBackToInventoryEnabled()` | `objectCanBeTakenBackToInventoryEnabled`を返すだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnPlaceObject` | `UnityEvent` | – |
| `eventOnTakeBackObject` | `UnityEvent` | – |
