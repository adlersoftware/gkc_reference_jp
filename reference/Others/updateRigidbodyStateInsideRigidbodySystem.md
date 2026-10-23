# updateRigidbodyStateInsideRigidbodySystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/updateRigidbodyStateInsideRigidbodySystem.cs:5`

**概要**: トリガー内に入ったRigidbodyを親Transformへ親子付けし、プレイヤーならカメラや移動状態も切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Detect Objects Enabled | `detectObjectsEnabled` | `bool` | true | – |
| Layer Mask | `layerMask` | `LayerMask` | – | – |
| Use Tag List | `useTagList` | `bool` | – | – |
| Tag List | `tagList` | `List<string>` | new List<string> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Objects On List | `objectsOnList` | `bool` | – | – |
| Game Object List | `gameObjectList` | `List<GameObject>` | new List<GameObject> () | – |
| Rigidbody Info List | `rigidbodyInfoList` | `List<rigidbodyInfo>` | new List<rigidbodyInfo> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Add Object | `useEventsOnAddObject` | `bool` | – | – |
| Event On Add Object | `eventOnAddObject` | `eventParameters.eventToCallWithGameObject` | – | – |
| Use Event On Remove Object | `useEventOnRemoveObject` | `bool` | – | – |
| Event On Remove Object | `eventOnRemoveObject` | `eventParameters.eventToCallWithGameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Main Parent | `mainParent` | `Transform` | – | – |
| Main Transform | `mainTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `removeAllObjects()` | `rigidbodyInfoList`の各要素について`removeGameObject`を呼び、登録をすべて解除する。 |
| `addGameObject(GameObject newObject)` | 検出有効時のみ、`newObject`の`Collider`を取得して`checkTriggerType`を進入扱いで呼ぶ。 |
| `removeGameObject(GameObject newObject)` | 検出有効時のみ、`newObject`の`Collider`を取得して`checkTriggerType`を退出扱いで呼ぶ。 |
| `checkTriggerType(Collider col, bool isEnter)` | レイヤーとタグで対象を絞り、`isEnter`なら親子付けとリスト登録、退出なら解除とプレイヤー状態の復元を行う。 |
| `checkIfObjectOnList(GameObject newObject)` | `gameObjectList`に`newObject`が含まれるかを返すだけ。 |

## 内部型

- `rigidbodyInfo`（class）
