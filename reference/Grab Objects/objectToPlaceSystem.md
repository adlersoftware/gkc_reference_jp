# objectToPlaceSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Grab Objects/objectToPlaceSystem.cs:7`

**概要**: 配置対象オブジェクト（ケーブル端末など）が配置済み・把持中・他オブジェクト接続中かを保持する。`putObjectSystem` との接続、イベント通知、周囲の配置先探索を仲介する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Placed Enabled | `objectToPlacedEnabled` | `bool` | true | – |
| Object Can Call Placed Event | `objectCanCallPlacedEvent` | `bool` | true | – |
| Object Can Call Removed Event | `objectCanCallRemovedEvent` | `bool` | true | – |
| Object Name | `objectName` | `string` | – | – |

### Secondary Object To Place Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Secondary Object To Place Connected | `useSecondaryObjectToPlaceConnected` | `bool` | – | – |
| Secondary Object To Place System | `secondaryObjectToPlaceSystem` | `objectToPlaceSystem` | – | – |

### Connect To Others Objects To Place Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Search Other Objects To Place On Drop Enabled | `searchOtherObjectsToPlaceOnDropEnabled` | `bool` | – | – |
| Other Objects To Place On Drop Name | `otherObjectsToPlaceOnDropName` | `string` | – | – |
| Custom Place To Put Other Object To Place Transform | `customPlaceToPutOtherObjectToPlaceTransform` | `Transform` | – | – |
| Use Other Objects To Place On Drop Name List | `useOtherObjectsToPlaceOnDropNameList` | `bool` | – | – |
| Other Objects To Place On Drop Info List | `otherObjectsToPlaceOnDropInfoList` | `List<otherObjectsToPlaceOnDropInfo>` | new List<otherObjectsToPlaceOnDropInf… | – |
| Max Distance To Search Other Objects To Place Around | `maxDistanceToSearchOtherObjectsToPlaceAround` | `float` | – | – |
| Use Find Objects On Scene For Other Objects To Place | `useFindObjectsOnSceneForOtherObjectsToPlace` | `bool` | – | – |
| Layer To Search Other Objects To Place Around | `layerToSearchOtherObjectsToPlaceAround` | `LayerMask` | – | – |
| Radius To Search Other Objects To Place Around | `radiusToSearchOtherObjectsToPlaceAround` | `float` | – | – |

### Search Objects On Drop Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Search Put Object Systems Around On Drop Enabled | `searchPutObjectSystemsAroundOnDropEnabled` | `bool` | – | – |
| Max Distance To Search Put Objects Systems Around | `maxDistanceToSearchPutObjectsSystemsAround` | `float` | – | – |
| Use Find Objects On Scene | `useFindObjectsOnScene` | `bool` | – | – |
| Layer To Search Put Object Systems Around | `layerToSearchPutObjectSystemsAround` | `LayerMask` | – | – |
| Radius To Search Put Object Systems Around | `radiusToSearchPutObjectSystemsAround` | `float` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Place To Put Object Transform | `useCustomPlaceToPutObjectTransform` | `bool` | – | – |
| Custom Place To Put Object Transform | `customPlaceToPutObjectTransform` | `Transform` | – | – |
| Check Name On Put Object System To Call Event | `checkNameOnPutObjectSystemToCallEvent` | `bool` | – | – |
| Name On Put Object System To Call Event | `nameOnPutObjectSystemToCallEvent` | `string` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Object In Grabbed State | `objectInGrabbedState` | `bool` | – | – |
| Object Placed | `objectPlaced` | `bool` | – | – |
| Secondary Object To Place Connected State | `secondaryObjectToPlaceConnectedState` | `bool` | – | – |
| Connected To Other Object To Place | `connectedToOtherObjectToPlace` | `bool` | – | – |
| Adjusting Object To Place In Process | `adjustingObjectToPlaceInProcess` | `bool` | – | – |
| Current Put Object System | `currentPutObjectSystem` | `putObjectSystem` | – | – |
| Other Object To Place Connected | `otherObjectToPlaceConnected` | `objectToPlaceSystem` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Object Placed State Changed | `useEventOnObjectPlacedStateChanged` | `bool` | – | – |
| Event On Object Placed | `eventOnObjectPlaced` | `UnityEvent` | – | – |
| Event On Object Removed | `eventOnObjectRemoved` | `UnityEvent` | – | – |
| Use Event On Connected To Other Object State Changed | `useEventOnConnectedToOtherObjectStateChanged` | `bool` | – | – |
| Event On Connected To Other Object | `eventOnConnectedToOtherObject` | `UnityEvent` | – | – |
| Event On Disconnected To Other Object | `eventOnDisconnectedToOtherObject` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getObjectName()` | `objectName` をそのまま返すだけ。 |
| `assignPutObjectSystem(putObjectSystem putObjectSystemToAssign)` | `currentPutObjectSystem` に引数の `putObjectSystem` を代入するだけ。 |
| `setObjectPlaceState(bool state)` | 配置済みフラグ `objectPlaced` に引数を代入するだけ。 |
| `isObjectPlaced()` | 配置済みフラグ `objectPlaced` を返すだけ。 |
| `isObjectInGrabbedState()` | 把持中フラグ `objectInGrabbedState` を返すだけ。 |
| `setObjectToPlacedEnabledState(bool state)` | 配置機能の有効フラグ `objectToPlacedEnabled` に引数を代入するだけ。 |
| `isobjectToPlacedEnabled()` | 配置機能の有効フラグ `objectToPlacedEnabled` を返すだけ。 |
| `canObjectCanCallPlacedEvent()` | 配置イベントを呼んでよいかの `objectCanCallPlacedEvent` を返すだけ。 |
| `canObjectCanCallRemovedEvent()` | 削除イベントを呼んでよいかの `objectCanCallRemovedEvent` を返すだけ。 |
| `setObjectCanCallPlacedEventState(bool state)` | `objectCanCallPlacedEvent` に引数を代入するだけ。 |
| `setObjectCanCallRemovedEventState(bool state)` | `objectCanCallRemovedEvent` に引数を代入するだけ。 |
| `isUseCustomPlaceToPutObjectTransformActive()` | 専用配置位置を使う `useCustomPlaceToPutObjectTransform` を返すだけ。 |
| `getCustomPlaceToPutObjectTransform()` | 専用配置位置 `customPlaceToPutObjectTransform` を返すだけ。 |
| `isUseSecondaryObjectToPlaceConnectedEnabled()` | もう一方の端との連動設定 `useSecondaryObjectToPlaceConnected` を返すだけ。 |
| `isSecondaryObjectToPlaceConnected()` | 二次側の接続状態 `secondaryObjectToPlaceConnectedState` を返すだけ。 |
| `getOtherObjectsToPlaceOnDropName()` | 接続先を探す名前 `otherObjectsToPlaceOnDropName` を返すだけ。 |
| `isConnectedToOtherObjectToPlace()` | 他オブジェクトと接続中かの `connectedToOtherObjectToPlace` を返すだけ。 |
| `setAdjustingObjectToPlaceInProcessState(bool state)` | 配置調整中フラグ `adjustingObjectToPlaceInProcess` に引数を代入するだけ。 |
| `isAdjustingObjectToPlaceInProcess()` | 配置調整中フラグ `adjustingObjectToPlaceInProcess` を返すだけ。 |
| `removeObjectIfPlaced()` | 配置済みなら把持状態に戻し、`Rigidbody` の `isKinematic` を解除して重力を有効にする。 |
| `removeObjectIfConnectedToOtherObject()` | 他オブジェクトと接続中なら把持状態に戻し、`Rigidbody` の `isKinematic` を解除して重力を有効にする。 |
| `setObjectInGrabbedState(bool state)` | 配置有効時のみ把持状態を設定し、配置中なら解除して `removePlacedObject` と配置解除イベントを呼ぶ。 |
| `checkToSetStateOnSecondaryObjectToPlaceOnObjectPlaceStateChange(bool state, objectToPlaceSystem originalObjectToPlace)` | 30回で打ち切る再帰で接続先の端へ `state` を伝播し、各端のイベントを呼ぶ。 |
| `checkStateOnExtremesDisconnected()` | 接続が切れた端のうち配置済みのもののイベントとイベント呼び出し可否を解除し、二次側へ false を伝播する。 |
| `checkStateOnExtremesOnObjectPlaced()` | 配置済みかつ名前条件を満たす場合に、二次側オブジェクトへ true を伝播してイベントを呼ぶ。 |
| `checkNameOnPutObjectSystemToCallEventResult(ref bool result, objectToPlaceSystem originalObjectToPlace)` | 名前チェックが無効なら `result` を true にし、有効なら配置先名の一致を端まで再帰的に調べて `result` を更新する。 |
| `checkIfExtremeConnected(ref bool result, bool ignoreIfThisObjectPlaced, objectToPlaceSystem originalObjectToPlace)` | 配置済みでイベント可なら `result` を true にし、そうでなければ接続先の端まで再帰して接続を判定する。 |
| `setSecondaryObjectToPlaceConnectedState(bool state)` | `secondaryObjectToPlaceConnectedState` を設定し、配置／解除イベントを出させる。 |
| `checkEventsOnCurrentPutObjectSystemState(bool state)` | `currentPutObjectSystem` へ、可否フラグを確認しつつ配置／解除イベントを出させる。 |
| `checkEventOnObjectPlacedStateChanged(bool state)` | 設定が有効なら `state` に応じて `eventOnObjectPlaced` か `eventOnObjectRemoved` を発火する。 |
| `checkEventOnConnectedToOtherObjectStateChanged(bool state)` | 設定が有効なら `state` に応じて接続／切断の UnityEvent を発火する。 |
| `setConnectedToOtherObjectToPlaceState(bool state, objectToPlaceSystem newObjectToPlaceSystem)` | 接続／切断を設定し、親子付け・`Rigidbody` の kinematic・コリジョン無視・両端のイベントと接続状態をまとめて更新する。 |
| `checkObjectsAround()` | 範囲内の `putObjectSystem` と接続対象の `objectToPlaceSystem` を探し、最近傍への配置または接続を行う。 |
| `checkIfObjectNameIsCompatible(string nameToCheck)` | 名前リスト使用時のみ `otherObjectsToPlaceOnDropInfoList` に同名があるかを返し、未使用なら常に true を返す。 |
| `getCustomPlaceToPutOtherObjectToPlaceTransform(string nameToCheck)` | 名前リストの一致項目の専用配置トランスフォームを返し、無ければ既定のものを返す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnObjectPlaced` | `UnityEvent` | – |
| `eventOnObjectRemoved` | `UnityEvent` | – |
| `eventOnConnectedToOtherObject` | `UnityEvent` | – |
| `eventOnDisconnectedToOtherObject` | `UnityEvent` | – |

## 内部型

- `otherObjectsToPlaceOnDropInfo`（class）
