# eventObjectFoundOnRaycastSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/eventObjectFoundOnRaycastSystem.cs:6`

**概要**: 指定Transformからレイキャストし、検出オブジェクトが変わった時にイベントやリモートイベントを呼ぶ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Objects Enabled | `checkObjectsEnabled` | `bool` | true | – |
| Raycast Transform | `raycastTransform` | `Transform` | – | – |
| Ray Distance To Check Object Found | `rayDistanceToCheckObjectFound` | `float` | – | – |
| Layer To Check Object Found | `layerToCheckObjectFound` | `LayerMask` | – | – |
| Check Objects On Update | `checkObjectsOnUpdate` | `bool` | – | – |

### Type of Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Events On Found Capture System | `checkEventsOnFoundCaptureSystem` | `bool` | true | – |
| Send Object On Surface Detected | `sendObjectOnSurfaceDetected` | `bool` | – | – |
| Object To Send On Surface Detected | `objectToSendOnSurfaceDetected` | `GameObject` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Events On Remote Event System | `checkEventsOnRemoteEventSystem` | `bool` | – | – |
| Remote Event To Call | `remoteEventToCall` | `string` | – | – |
| Use Remote Event List | `useRemoteEventList` | `bool` | – | – |
| Remove Event Name List | `removeEventNameList` | `List<string>` | new List<string> () | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event To Call Objec Object Detected | `useEventToCallObjecObjectDetected` | `bool` | – | – |
| Event To Call On Object Detected | `eventToCallOnObjectDetected` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateRaycastDetectionOnUpdate()` | 固定更新ごとに`checkObjectWithRaycast`を呼ぶコルーチンを開始する。 |
| `checkObjectWithRaycast()` | 前方へレイを飛ばし、検出対象が前回と違う時だけキャプチャ・リモートイベント・検出イベントを実行する。 |
| `setRaycastTransform(Transform newObject)` | `raycastTransform`に`newObject`を代入するだけ。 |
| `setCheckObjectsEnabledState(bool state)` | `checkObjectsEnabled`に`state`を代入するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToCallOnObjectDetected` | `UnityEvent` | – |
