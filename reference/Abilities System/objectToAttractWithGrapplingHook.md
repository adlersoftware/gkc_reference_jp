# objectToAttractWithGrapplingHook

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/Custom Abilities/Grappling Hook System/objectToAttractWithGrapplingHook.cs:6`

**概要**: グラップリングフックで引き寄せられるオブジェクト側の設定。引力状態の切替、終了時の減速と速度復帰、複数 `Rigidbody` の検索を扱う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attract Object Enabled | `attractObjectEnabled` | `bool` | true | – |
| Attract Player Enabled | `attractPlayerEnabled` | `bool` | – | – |
| Enable Gravity On Deactivate Attract | `enableGravityOnDeactivateAttract` | `bool` | true | – |
| Use Reduced Velocity On Disable Attract | `useReducedVelocityOnDisableAttract` | `bool` | – | – |
| Max Reduced Speed | `maxReducedSpeed` | `float` | – | – |
| Reduced Speed Duration | `reducedSpeedDuration` | `float` | – | – |
| New Speed After Reduced Duration Multiplier | `newSpeedAfterReducedDurationMultiplier` | `float` | 1 | – |
| Ignore Apply Speed On Hook Stop On Player | `ignoreApplySpeedOnHookStopOnPlayer` | `bool` | – | – |
| Reset Player Speed On Hook Stop | `resetPlayerSpeedOnHookStop` | `bool` | – | – |

### Auto Grab Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Auto Grab Object On Close Distance | `autoGrabObjectOnCloseDistance` | `bool` | – | – |
| Min Distance To Auto Grab | `minDistanceToAutoGrab` | `float` | – | – |

### Activate Interaction Action Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Interaction Action With Object | `activateInteractionActionWithObject` | `bool` | – | – |
| Min Distance To Activate Interaction Action With Object | `minDistanceToActivateInteractionActionWithObject` | `float` | – | – |
| Object To Activate | `objectToActivate` | `GameObject` | – | – |

### Offset Position Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Hook Target Postion Offset | `useHookTargetPostionOffset` | `bool` | – | – |
| Hook Target Position Offset | `hookTargetPositionOffset` | `Vector3` | – | – |
| Use Object Target Position Transform | `useObjectTargetPositionTransform` | `bool` | – | – |
| Object Target Position Transform | `objectTargetPositionTransform` | `Transform` | – | – |

### Rigidbody Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Use Rigidbody List | `useRigidbodyList` | `bool` | – | – |
| Rigidbody List | `rigidbodyList` | `List<Rigidbody>` | new List<Rigidbody> () | – |

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Force Attraction Values | `useCustomForceAttractionValues` | `bool` | – | – |
| Custom Min Distance To Stop Attract Object | `customMinDistanceToStopAttractObject` | `float` | 5 | – |
| Custom Add Up Force For Attraction | `customAddUpForceForAttraction` | `bool` | – | – |
| Custom Up Force For Attraction | `customUpForceForAttraction` | `float` | – | – |
| Custom Add Up Force For Attraction Duration | `customAddUpForceForAttractionDuration` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attracting Object Active | `attractingObjectActive` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Attract State | `useEventsOnAttractState` | `bool` | – | – |
| Event On Activate Attract | `eventOnActivateAttract` | `UnityEvent` | – | – |
| Event On Deactivate Attract | `eventOnDeactivateAttract` | `UnityEvent` | – | – |
| Use Event After Reduce Speed | `useEventAfterReduceSpeed` | `bool` | – | – |
| Event After Reduce Speed | `eventAfterReduceSpeed` | `UnityEvent` | – | – |

### Remote Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Events On State Change | `useRemoteEventsOnStateChange` | `bool` | – | – |
| Remote Event Name List On Start | `remoteEventNameListOnStart` | `List<string>` | new List<string> () | – |
| Remote Event Name List On End | `remoteEventNameListOnEnd` | `List<string>` | new List<string> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Transform | `mainTransform` | `Transform` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.green | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.white | – |
| Gizmo Radius | `gizmoRadius` | `float` | 0.3f | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setAttractionHookRemovedByDistanceState(bool state)` | `attractionHookRemovedByDistance` を設定するだけ。 |
| `setAttractObjectState(bool state)` | `attractObjectEnabled` なら引力状態を切り替え、重力の復帰・イベント・減速処理まで行い結果を返す。 |
| `getRigidbodyToAttract()` | `mainRigidbody` を返すだけ。 |
| `checkToReduceSpeed()` | `useReducedVelocityOnDisableAttract` が有効なら既存の減速コルーチンを止めて新たに開始する。 |
| `stopCheckToReduceSpeed()` | `reduceSpeedCoroutine` が動いていれば停止する。 |
| `stopGrapplingHookAndResumeValuesWithoutForce()` | 速度記録をゼロにしてから `stopGrapplingHookAndResumeValues` を呼ぶ。 |
| `stopGrapplingHookAndResumeValues()` | 減速処理中ならコルーチンを止めて元の速度に戻し、終了イベントを発火して状態を戻す。 |
| `stopGrapplingHookIfActiveOnGrabObject()` | 減速処理中ならコルーチンを止め、速度記録と各フラグをリセットするだけ。 |
| `searchRigidbodyElements()` | 子階層の `Rigidbody` を集めてリストと `mainRigidbody` を再構築し、`updateComponent` を呼ぶ。 |
| `updateComponent()` | `GKC_Utils.updateComponent` と `updateDirtyScene` でシーン更新を通知する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnActivateAttract` | `UnityEvent` | – |
| `eventOnDeactivateAttract` | `UnityEvent` | – |
| `eventAfterReduceSpeed` | `UnityEvent` | – |
