# eventTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Event System/eventTriggerSystem.cs:6`

**概要**: トリガーの進入/退出を判定し、タグ・レイヤー・対象オブジェクトの条件と要素ごとの遅延を経て、`SendMessage`/`BroadcastMessage`/`UnityEvent`/リモートイベントを実行する。オブジェクト追跡により最初の進入と最後の退出でのみ発火させる。

**公式ドキュメント抜粋**（[Event Trigger System](../../docs/major-systems/event-trigger-system.md)）

> 

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Use Same Function To Call Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Same Function In List | `useSameFunctionInList` | `bool` | – | オンにすると全イベントで共通の関数リストをまとめて呼ぶ。 |

### Use Same Object To Call Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Same Object To Call | `useSameObjectToCall` | `bool` | – | オンにすると全イベントの呼び出し先を共通のオブジェクトに統一する。 |
| Call This Object | `callThisObject` | `bool` | – | オンにすると共通の呼び出し先をこのオブジェクト自身にする。 / 表示条件: `useSameObjectToCall` がオンのとき |
| Same Object To Call | `sameObjectToCall` | `GameObject` | – | 全イベントで共通に使う呼び出し先オブジェクト。 / 表示条件: `useSameObjectToCall.boolValue && !callThisObject.boolValue` |

### Use Object To Trigger Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Object To Trigger | `useObjectToTrigger` | `bool` | – | オンにすると指定オブジェクトが触れた時だけイベントを発動する。 |
| Object Needed To Trigger | `objectNeededToTrigger` | `GameObject` | – | 発動のきっかけとして必要なオブジェクト。 / 表示条件: `useObjectToTrigger` がオンのとき |

### Tag Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Tag To Trigger | `useTagToTrigger` | `bool` | – | オンにするとタグが一致した時にイベントを発動する。 |
| Use Tag List | `useTagList` | `bool` | – | オンにすると`tagList`に含まれる複数のタグを対象にする。 / 表示条件: `useTagToTrigger` がオンのとき |
| Tag Needed To Trigger | `tagNeededToTrigger` | `string` | – | 発動対象とする単一のタグ。 / 表示条件: `useTagToTrigger` がオンのとき |

### Same Delay Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dont Use Delay | `dontUseDelay` | `bool` | – | オンにすると遅延をかけずにイベントを即座に実行する。 |
| Use Same Delay | `useSameDelay` | `bool` | – | オンにすると全イベントで`generalDelay`を共通の待ち時間として使う。 |
| General Delay | `generalDelay` | `float` | – | 全イベント共通の待ち時間（秒）。 / 表示条件: `useSameDelay` がオンのとき |
| Use Random Delay | `useRandomDelay` | `bool` | – | オンにすると共通待ち時間を`randomDelayRange`からランダムに決める。 / 表示条件: `useSameDelay` がオンのとき |
| Random Delay Range | `randomDelayRange` | `Vector2` | – | ランダム待ち時間の最小値と最大値（秒）。 / 表示条件: `useSameDelay.boolValue && useRandomDelay.boolValue` |

### Trigger Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Triggered By Button | `triggeredByButton` | `bool` | – | オンにするとトリガー判定を止め、ボタンなど外部呼び出しでのみ発動する。 |
| Trigger Event Type | `triggerEventType` | `triggerType` | – | 侵入・退出・両方のどれで発動するかと、使うイベントリストを選ぶ。 / 表示条件: `triggeredByButton` がオフのとき |

### Layer Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Layer Mask | `useLayerMask` | `bool` | – | オンにすると`layerMask`に含まれるレイヤーのコライダーだけに反応する。 |
| Layer Mask | `layerMask` | `LayerMask` | – | 反応を許可するレイヤーのマスク。 / 表示条件: `useLayerMask` がオンのとき |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Just Call On Trigger | `justCallOnTrigger` | `bool` | – | オンにするとオブジェクトやタグの条件なしで、触れた任意の相手で発動する。 |
| Call Function Every Time Triggered | `callFunctionEveryTimeTriggered` | `bool` | – | オンにすると一度発動した後も毎回再発動できる。 |
| Set Parent To Null | `setParentToNull` | `bool` | – | オンにすると発動時に自身の親を解除する。 |
| Trigger Event At Start | `triggerEventAtStart` | `bool` | – | オンにすると`Start`時にイベントを自動実行する。 |
| Loop Event At The End Enabled | `loopEventAtTheEndEnabled` | `bool` | – | オンにするとイベントを最後まで実行した後に再び発動してループする。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `eventList` | `List<eventInfo>` | new List<eventInfo> () | – |
| `enterEventList` | `List<eventInfo>` | new List<eventInfo> () | – |
| `exitEventList` | `List<eventInfo>` | new List<eventInfo> () | – |
| `sameFunctionList` | `List<string>` | new List<string> () | – |
| `tagList` | `List<string>` | new List<string> () | – |
| `eventTriggered` | `bool` | – | – |
| `coroutineActive` | `bool` | – | – |
| `objectDetected` | `GameObject` | – | – |
| `useObjectTracking` | `bool` | true | – |
| `objectsInsideTrigger` | `List<GameObject>` | new List<GameObject> () | – |
| `isEnter` | `bool` | – | – |
| `isExit` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateEventIfObjectActiveSelf()` | `gameObject`が階層上アクティブな時だけ`activateEvent`を呼ぶ条件付きラッパー。 |
| `activateEvent()` | 未発動（または毎回許可時）に`eventTriggered`を立てて親を解除し、遅延なしなら即時、ありならコルーチンで発火する。 |
| `stopEventCoroutineIfActive()` | `coroutineActive`が真なら実行中のイベントコルーチンを停止し、そのフラグを偽にする。 |
| `stopEventCoroutine()` | `eventCoroutine`がnullでなければ`StopCoroutine`で止めるだけで、`coroutineActive`は変更しない。 |
| `stopAllEventsAndDisableTriggerSystem()` | コルーチンを止め、`eventTriggered`を真・`callFunctionEveryTimeTriggered`を偽にして以後の発火を抑止する（コンポーネント自体は無効化しない）。 |
| `activateEventAtOnce()` | 遅延を待たず、`enter`/`exit`の選択を反映した対象リストの全要素を`callElementFromList`で即実行する。 |
| `callElementFromList(eventInfo currentEventInfo)` | 1件の`eventInfo`設定に従い、`SendMessage`/`BroadcastMessage`/`UnityEvent`/リモートイベントを呼び分ける。 |
| `getObjectToCall(GameObject defaultObjectToCall)` | `useSameObjectToCall`なら自身か`sameObjectToCall`を返し、そうでなければ引数のオブジェクトを返す。 |
| `checkTriggerEventEnterType(GameObject objectToCheck)` | `checkTriggerEventType`に`triggerType.enter`を渡すだけのラッパー。 |
| `checkTriggerEventExitType(GameObject objectToCheck)` | `checkTriggerEventType`に`triggerType.exit`を渡すだけのラッパー。 |
| `checkTriggerEventType(GameObject objectToCheck, triggerType trigger)` | 未発動か毎回許可の時に種別・対象・タグ・`justCallOnTrigger`を判定し、`objectDetected`を入れて`activateEvent`を呼ぶ。 |
| `getLastObjectDetected()` | 最後に検出した`objectDetected`を返すだけのゲッター。 |
| `checkTag(GameObject objectToCheck)` | `useTagToTrigger`時、タグリストまたは単一タグと一致するかを判定して返す。 |
| `checkIfObjectCanTrigger(GameObject objectToCheck)` | 対象オブジェクト一致・タグ一致・`justCallOnTrigger`のいずれかなら真を返す判定関数。 |
| `checkTriggerEventTypeByFunction()` | ボタン起因でなく未発動（または毎回許可）なら、種別判定をせず`activateEvent`を呼ぶ。 |
| `resetEventTriggered()` | `eventTriggered`を偽に戻すだけのセッター。 |
| `setEventAsTriggered()` | `eventTriggered`を真にするだけのセッター。 |
| `setObjectOnTriggerEnterExternally(GameObject newObject)` | 引数オブジェクトの`Collider`を取得し、あれば`OnTriggerEnter`を直接呼んで進入扱いにする。 |
| `setLoopEventAtTheEndEnabledState(bool state)` | `loopEventAtTheEndEnabled`を設定するだけの薄いセッター。 |
| `addNewEvent()` | `eventList`に新しい`eventInfo`を追加し、`updateComponent`で更新するエディタ用関数。 |
| `InsertEventAtIndex(int index)` | `eventList`の`index+1`の位置に新しい`eventInfo`を挿入し、`updateComponent`を呼ぶ。 |
| `setSimpleFunctionByTag(string functionName, GameObject objectTocall, string tag)` | イベントを1件追加して対象オブジェクトと関数名を設定し、`useTagToTrigger`と`tagNeededToTrigger`を上書きする。 |
| `setUseLayerMaskState(bool state)` | `useLayerMask`を設定し、`updateComponent`を呼ぶ。 |
| `setLayerMaskValue(LayerMask newLayer)` | `layerMask`を設定し、`updateComponent`を呼ぶ。 |
| `setUseTagToTriggerState(bool state)` | `useTagToTrigger`を設定し、`updateComponent`を呼ぶ。 |
| `setUseTagListState(bool state)` | `useTagList`を設定し、`updateComponent`を呼ぶ。 |
| `setTagList(List<string> newList)` | `tagList`を引数のリストで置き換え、`updateComponent`を呼ぶ。 |
| `addElementToTagList(string newElement)` | 未登録の場合のみ`tagList`に追加し、`updateComponent`を呼ぶ。 |
| `removeElementToTagList(string newElement)` | 登録済みの場合のみ`tagList`から削除し、`updateComponent`を呼ぶ。 |

## 内部型

- `triggerType`（enum）
- `eventInfo`（class）
