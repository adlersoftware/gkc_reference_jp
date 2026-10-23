# checkObjectOnTrigger

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Grab Objects/checkObjectOnTrigger.cs:6`

**概要**: トリガー内に入った配置可能オブジェクトをリストで保持し、配置／退出に応じて UnityEvent を発火する判定コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Put Object System Enabled | `putObjectSystemEnabled` | `bool` | true | – |
| Use Certain Object To Place | `useCertainObjectToPlace` | `bool` | – | – |
| Certain Object To Place | `certainObjectToPlace` | `GameObject` | – | – |
| Object Name To Place | `objectNameToPlace` | `string` | – | – |
| Use Object Name List To Place | `useObjectNameListToPlace` | `bool` | – | – |
| Object Name List To Place | `objectNameListToPlace` | `List<string>` | new List<string> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Any Object Placed | `anyObjectPlaced` | `bool` | – | – |
| Objects Placed List | `objectsPlacedList` | `List<GameObject>` | new List<GameObject> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Object Placed | `useEventOnObjectPlaced` | `bool` | – | – |
| Object Placed Event | `objectPlacedEvent` | `UnityEvent` | – | – |
| Use Event On Object Removed | `useEventOnObjectRemoved` | `bool` | – | – |
| Object Removed Event | `objectRemovedEvent` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkObjectOnTriggerEnter(GameObject newObject)` | 配置可能かつ未登録ならリストに追加し、`objectPlacedEvent` を発火して `anyObjectPlaced` を true にする。 |
| `checkObjectOnTriggerExit(GameObject newObject)` | 配置可能かつ登録済みならリストから外し、空なら `anyObjectPlaced` を false にして削除イベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `objectPlacedEvent` | `UnityEvent` | – |
| `objectRemovedEvent` | `UnityEvent` | – |
