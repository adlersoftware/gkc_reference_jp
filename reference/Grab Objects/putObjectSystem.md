# putObjectSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Grab Objects/putObjectSystem.cs:7`

**概要**: オブジェクトを受け取って配置する側のコンポーネントで、トリガー進入／退出や名前条件で対象を判定する。配置位置への移動、配置／解除イベント、配置数の管理を行う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Put Object System Enabled | `putObjectSystemEnabled` | `bool` | true | オンにするとこの配置先へオブジェクトを置けるようになる。 |
| Use Certain Object To Place | `useCertainObjectToPlace` | `bool` | – | オンにすると特定のオブジェクトだけを配置対象にする。 |
| Certain Object To Place | `certainObjectToPlace` | `GameObject` | – | 配置を許可する特定のオブジェクトの参照。 / 表示条件: `useCertainObjectToPlace` がオンのとき |
| Object Name | `objectName` | `string` | – | この配置先を識別する名前で、イベント名の照合に使われる。 |
| Use Object Name List To Place | `useObjectNameListToPlace` | `bool` | – | オンにすると複数のオブジェクト名を配置対象として扱う。 |
| Object Name To Place | `objectNameToPlace` | `string` | – | 配置を許可するオブジェクトの名前。 |
| Place To Put Object | `placeToPutObject` | `Transform` | – | 配置時にオブジェクトを親子付けする位置のトランスフォーム。 |
| Place Object Position Speed | `placeObjectPositionSpeed` | `float` | – | 配置位置へ移動する速さで、距離から移動時間を算出する。 |
| Place Object Rotation Speed | `placeObjectRotationSpeed` | `float` | – | 配置時の回転速度として設定する値（現行コードでは未参照）。 |
| Disable Object Once Is Placed | `disableObjectOnceIsPlaced` | `bool` | – | オンにすると配置後にそのオブジェクトの配置と掴みを無効化する。 |
| Min Wait To Put Same Object Again | `minWaitToPutSameObjectAgain` | `float` | 0.7f | 同じオブジェクトを再び置けるようになるまでの待ち秒数。 |
| Update Trigger State After Wait | `updateTriggerStateAfterWait` | `bool` | – | オンにすると待ち時間後にトリガーを再取得して判定を更新する。 |
| Destroy Object Once Placed | `destroyObjectOncePlaced` | `bool` | – | オンにすると配置位置に収まったオブジェクトを破壊する。 |
| Ignore Trigger Enter Exit Functions Enabled | `ignoreTriggerEnterExitFunctionsEnabled` | `bool` | – | オンにするとトリガーの出入りでは配置判定を行わない。 |

### Limit Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Rotation Limit | `useRotationLimit` | `bool` | – | オンにすると角度制限を満たす向きでのみ配置できる。 |
| Max Up Rotation Angle | `maxUpRotationAngle` | `float` | 30 | 配置を許可する上方向の回転角度の上限。 / 表示条件: `useRotationLimit` がオンのとき |
| Max Forward Rotation Angle | `maxForwardRotationAngle` | `float` | 30 | 配置を許可する前方向の回転角度の上限。 / 表示条件: `useRotationLimit` がオンのとき |
| Use Position Limit | `usePositionLimit` | `bool` | – | オンにすると一定距離内にある場合だけ配置できる。 |
| Max Position Distance | `maxPositionDistance` | `float` | – | 配置を許可する、この配置先からの最大距離。 / 表示条件: `usePositionLimit` がオンのとき |

### Objects To Place Before Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Needs Other Object Placed Before | `needsOtherObjectPlacedBefore` | `bool` | – | オンにすると規定数のオブジェクトが配置済みでないと置けない。 |
| Number Of Objects To Place Before | `numberOfObjectsToPlaceBefore` | `int` | – | 配置を許可する前に必要な配置済みオブジェクト数。 / 表示条件: `needsOtherObjectPlacedBefore` がオンのとき |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Wait To Object Placed To Call Event | `waitToObjectPlacedToCallEvent` | `bool` | – | オンにすると配置位置へ移動し終えてからイベントを呼ぶ。 |
| Object Placed Event | `objectPlacedEvent` | `UnityEvent` | – | オブジェクトが配置されたときに呼ばれるイベント。 |
| Object Removed Event | `objectRemovedEvent` | `UnityEvent` | – | 配置済みオブジェクトが外されたときに呼ばれるイベント。 |

### Remove Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Limit To Check If Object Removed | `useLimitToCheckIfObjectRemoved` | `bool` | – | オンにすると距離を監視して外れた時点で配置解除する。 |
| Min Distance To Remove Object | `minDistanceToRemoveObject` | `float` | – | 配置済みオブジェクトを外したと判定する距離のしきい値。 / 表示条件: `useLimitToCheckIfObjectRemoved` がオンのとき |

### Sounds Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Sound Effect On Object Placed | `useSoundEffectOnObjectPlaced` | `bool` | – | オンにすると配置時に効果音を再生する。 |
| Sound Effect On Object Placed | `soundEffectOnObjectPlaced` | `AudioClip` | – | 配置時に再生する効果音のクリップ。 / 表示条件: `useSoundEffectOnObjectPlaced` がオンのとき |
| On Object Placed Audio Element | `onObjectPlacedAudioElement` | `AudioElement` | – | 配置音を再生するためのオーディオ要素。 / 表示条件: `useSoundEffectOnObjectPlaced` がオンのとき |
| Use Sound Effect On Object Removed | `useSoundEffectOnObjectRemoved` | `bool` | – | オンにすると配置解除時に効果音を再生する。 |
| Sound Effect On Object Removed | `soundEffectOnObjectRemoved` | `AudioClip` | – | 配置解除時に再生する効果音のクリップ。 / 表示条件: `useSoundEffectOnObjectRemoved` がオンのとき |
| On Object Removed Audio Element | `onObjectRemovedAudioElement` | `AudioElement` | – | 配置解除音を再生するためのオーディオ要素。 / 表示条件: `useSoundEffectOnObjectRemoved` がオンのとき |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | 効果音を再生するオーディオソース。 |
| Main Trigger | `mainTrigger` | `Collider` | – | 配置判定に使うトリガーコライダー。 |

### Current State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Inside Trigger | `objectInsideTrigger` | `bool` | – | オブジェクトがトリガー内にあるかを示す実行時状態。 |
| Object Placed | `objectPlaced` | `bool` | – | オブジェクトが配置済みかを示す実行時状態。 |
| Current Object Placed | `currentObjectPlaced` | `GameObject` | – | 現在配置されているオブジェクトの参照。 |
| Current Object To Place System | `currentObjectToPlaceSystem` | `objectToPlaceSystem` | – | 配置中オブジェクトの配置システムの参照。 |
| Checking If Object Is Removed | `checkingIfObjectIsRemoved` | `bool` | – | 配置解除の距離判定中かを示す実行時フラグ。 |
| Object Adjusted To Place Position | `objectAdjustedToPlacePosition` | `bool` | – | オブジェクトが配置位置に収まり終えたかを示すフラグ。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `objectNameListToPlace` | `List<string>` | new List<string> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `destroyCurrentObjectPlaced()` | 配置位置への調整が済んでいれば `removeObject` の後に `currentObjectPlaced` を `Destroy` する。 |
| `checkTriggerInfo(bool isEnter, GameObject objectToCheck)` | `checkObjectToPlace` へそのまま渡すだけ。 |
| `placeObject(GameObject objectToCheck)` | 外部から進入扱いで `checkObjectToPlace` を呼び、対象オブジェクトの配置を試みる。 |
| `checkIfCanBePlaced(bool objectPlacedPreviously)` | 前提配置数を満たせば `Rigidbody` を kinematic にし、移動を開始して `objectPlaced` を true にする。 |
| `canBeDragged(GameObject objectToCheck)` | 特定オブジェクト指定か `objectToPlaceSystem` の名前条件で判定し、配置可能ならその `GameObject`、不可なら null を返す。 |
| `moveObjectToPlace(bool objectPlacedPreviously)` | 移動と待機の既存コルーチンを止めてから `placeObjectIntoPosition` コルーチンを開始する。 |
| `stopMoveObjectToPlaceCoroutine()` | `placeObjectCoroutine` があれば `StopCoroutine` するだけ。 |
| `removePlacedObject()` | `useLimitToCheckIfObjectRemoved` なら距離判定用フラグを立て、そうでなければ `removeObject` を実行する。 |
| `dropCurrentObjectPlaced(bool reactivateObjectToUseOnPlaceSystem)` | 配置を解除し、引数が true なら配置元の状態とイベントを戻し、`Rigidbody` に前方への力を加えて落とす。 |
| `removeObject()` | 解除イベントと効果音を出し、コルーチン停止・親子解除・`objectPlaced` を false・参照の null 化を行う。 |
| `checkEventsOnObjectPlacedOrRemoved(bool state)` | `state` に応じて `objectPlacedEvent` か `objectRemovedEvent` を発火するだけ。 |
| `disableObjectPlacedFromGrab()` | 配置中のオブジェクトのタグを `Untagged` にするだけ。 |
| `increaseNumberObjectsPlaced()` | `currentNumberObjectsPlaced` を 1 増やすだけ。 |
| `decreaseNumberObjectsPlaced()` | `currentNumberObjectsPlaced` を 1 減らし、負になったら 0 に戻す。 |
| `resetNumberObjectsPlaced()` | 移動コルーチンを止め、配置数を 0 にして配置・進入・調整の各フラグを false にする。 |
| `playSound(AudioElement soundToPlay)` | null でなければ `AudioPlayer.PlayOneShot` でその `AudioElement` を再生する。 |
| `pausePutObject()` | 既存の待機コルーチンを止めて `pausePutObjectCoroutine` を開始する。 |
| `stopPausePutObjectCoroutine()` | `pauseCoroutine` があれば `StopCoroutine` するだけ。 |
| `isPutObjectSystemEnabled()` | `putObjectSystemEnabled` を返すだけ。 |
| `getObjectName()` | `objectName` を返すだけ。 |
| `getPlaceToPutObjectPosition()` | `placeToPutObject` があればその position、無ければ自身の position を返す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `objectPlacedEvent` | `UnityEvent` | – |
| `objectRemovedEvent` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnTriggerEnter(Collider col)`, `OnTriggerExit(Collider col)`

</details>
