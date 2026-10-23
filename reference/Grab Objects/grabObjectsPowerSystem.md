# grabObjectsPowerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Grab Objects/grabObjectsPowerSystem.cs:7`

**概要**: パワーで周囲または注視先のオブジェクトを掴み、ボタン長押しでためた力を加えて投擲するシステム。把持リスト、照準スライダー、投擲イベントを管理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grab Objects Enabled | `grabObjectsEnabled` | `bool` | – | – |
| Grab Radius | `grabRadius` | `float` | 10 | – |
| Able To Grab Tags | `ableToGrabTags` | `List<string>` | new List<string> () | – |
| Layer To Damage | `layerToDamage` | `LayerMask` | – | – |
| Layer To Detect Objects | `layerToDetectObjects` | `LayerMask` | – | – |
| Carry Objects Speed | `carryObjectsSpeed` | `float` | 5 | – |
| Min Force To Launch Objects | `minForceToLaunchObjects` | `float` | 300 | – |
| Max Force To Launch Objects | `maxForceToLaunchObjects` | `float` | 3500 | – |
| Add Force To Launch Objects Speed | `addForceToLaunchObjectsSpeed` | `float` | 1200 | – |
| Wait Time To Drop Objects | `waitTimeToDropObjects` | `float` | 1 | – |
| Use Carry Objects Position Offset | `useCarryObjectsPositionOffset` | `bool` | – | – |
| Carry Objects Position Offset | `carryObjectsPositionOffset` | `Vector3` | – | – |

### Grab Single Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grab Single Object On Camera View | `grabSingleObjectOnCameraView` | `bool` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remote Event Name List On Grab Object | `remoteEventNameListOnGrabObject` | `List<string>` | new List<string> () | – |
| Remote Event Name List On Drop Object | `remoteEventNameListOnDropObject` | `List<string>` | new List<string> () | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Check On Trigger Enter Enabled State | `setCheckOnTriggerEnterEnabledState` | `bool` | – | – |
| Check On Trigger Enter Enabled | `checkOnTriggerEnterEnabled` | `bool` | – | – |
| Layermask To Check On Trigger Enter | `layermaskToCheckOnTriggerEnter` | `LayerMask` | – | – |
| Set Use Custom Damage Amount State | `setUseCustomDamageAmountState` | `bool` | – | – |
| Use Custom Damage Amount | `useCustomDamageAmount` | `bool` | – | – |
| Custom Damage Amount | `customDamageAmount` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Carrying Objects | `carryingObjects` | `bool` | – | – |
| First Person Active | `firstPersonActive` | `bool` | – | – |
| First Person Previously Active | `firstPersonPreviouslyActive` | `bool` | – | – |
| Grabbed Object List | `grabbedObjectList` | `List<grabbedObject>` | new List<grabbedObject> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Throw Objects | `useEventsOnThrowObjects` | `bool` | – | – |
| Event On Throw Objects | `eventOnThrowObjects` | `UnityEvent` | – | – |
| Event On Drop Objects | `eventOnDropObjects` | `UnityEvent` | – | – |
| Event On Grab Object | `eventOnGrabObject` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grab Objects Manager | `grabObjectsManager` | `grabObjects` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Main Other Powers | `mainOtherPowers` | `otherPowers` | – | – |
| Carry Objects Transform | `carryObjectsTransform` | `Transform` | – | – |
| Carry Objects Transform First Person List | `carryObjectsTransformFirstPersonList` | `List<Transform>` | new List<Transform> () | – |
| Carry Objects Transform Third Person List | `carryObjectsTransformThirdPersonList` | `List<Transform>` | new List<Transform> () | – |
| Use Carry Objects Animation | `useCarryObjectsAnimation` | `bool` | true | – |
| Carry Objects Transform Animation | `carryObjectsTransformAnimation` | `Animation` | – | – |
| Carry Objects Animation Name | `carryObjectsAnimationName` | `string` | "grabObjects" | – |
| Slider | `slider` | `Slider` | – | – |
| Main Player Collider | `mainPlayerCollider` | `Collider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `grabCloseObjects()` | 未把持なら `grabRadius` 内のコライダーから掴めるものを登録し、1つ以上あれば `eventOnGrabObject` を発火する。 |
| `grabSingleObject()` | 未把持ならカメラ前方へのレイキャストで得たコライダーを掴み、成功時に `eventOnGrabObject` を発火する。 |
| `dropObjects()` | カメラ前方の着弾点を投擲方向として全把持オブジェクトを `dropObject` し、リスト・カーソル・スライダーを片付ける。 |
| `addForceToLaunchObjects()` | 待機時間の経過後、`currentForceToLaunchObjects` を増やして最小値を超えたらスライダーとカーソルを有効にする。 |
| `dropObject(grabbedObject currentGrabbedObject, Vector3 launchDirection)` | 親から外してタグとレイヤーを戻し、ためた力で投擲または落下させ、把持状態と各種イベントを更新する。 |
| `checkIfDropObject(GameObject objectToCheck)` | 把持リストから一致するものを探して `dropObject` を呼び、その参照を null にする。 |
| `setGrabObjectsEnabledState(bool state)` | `grabObjectsEnabled` に引数を代入するだけ。 |
| `inputGrabObjects()` | 忙しくなく未把持なら、アニメを再生しカメラ注視設定に応じて単体／周囲の把持を実行してためる力を 0 に戻す。 |
| `inputHoldToLaunchObjects()` | 忙しくなく把持中なら `addForceToLaunchObjects` を呼び、押下時間に応じて力をためる。 |
| `inputReleaseToLaunchObjects()` | 把持中かつ待機時間の経過後に `dropObjects` を呼び、ためた力が大きければ投擲イベント、小さければ落下イベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnThrowObjects` | `UnityEvent` | – |
| `eventOnDropObjects` | `UnityEvent` | – |
| `eventOnGrabObject` | `UnityEvent` | – |

## 内部型

- `grabbedObject`（class）
