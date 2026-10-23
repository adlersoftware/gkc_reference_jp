# grabbedObjectState

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Grab Objects/grabbedObjectState.cs:6`

**概要**: オブジェクトが把持されているかを保持する状態コンポーネントで、把持者・無重力室・物理把持の各フラグを管理する。把持／解放時の UnityEvent も持つ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remove Component On Drop Object | `removeComponentOnDropObject` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inside Zero Gravity Room | `insideZeroGravityRoom` | `bool` | – | – |
| Grabbed | `grabbed` | `bool` | – | – |
| Carrying Object Physically | `carryingObjectPhysically` | `bool` | – | – |
| Current Holder | `currentHolder` | `GameObject` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Grabbed State | `useEventsOnGrabbedState` | `bool` | – | – |
| Event On Grab Object | `eventOnGrabObject` | `UnityEvent` | – | – |
| Event On Drop Object | `eventOnDropObject` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Zero Gravity Room | `currentZeroGravityRoom` | `zeroGravityRoomSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setGrabbedState(bool state)` | `grabbed` を設定し、`useEventsOnGrabbedState` が有効なら把持／解放の UnityEvent を発火する。 |
| `isGrabbed()` | `grabbed` を返すだけ。 |
| `setCurrentHolder(GameObject current)` | `currentHolder` に引数を代入するだけ。 |
| `getCurrentHolder()` | `currentHolder` を返すだけ。 |
| `setInsideZeroGravityRoomState(bool state)` | `insideZeroGravityRoom` に引数を代入するだけ。 |
| `isInsideZeroGravityRoom()` | `insideZeroGravityRoom` を返すだけ。 |
| `setCurrentZeroGravityRoom(zeroGravityRoomSystem gravityRoom)` | `currentZeroGravityRoom` に引数を代入するだけ。 |
| `getCurrentZeroGravityRoom()` | `currentZeroGravityRoom` を返すだけ。 |
| `checkGravityRoomState()` | `insideZeroGravityRoom` なら `currentZeroGravityRoom` に自分を渡して室内状態を通知する。 |
| `setCarryingObjectPhysicallyState(bool state)` | `carryingObjectPhysically` に引数を代入するだけ。 |
| `isCarryingObjectPhysically()` | `carryingObjectPhysically` を返すだけ。 |
| `removeGrabbedObjectComponent()` | `removeComponentOnDropObject` が有効なら自分自身のコンポーネントを `Destroy` する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnGrabObject` | `UnityEvent` | – |
| `eventOnDropObject` | `UnityEvent` | – |
