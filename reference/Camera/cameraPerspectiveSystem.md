# cameraPerspectiveSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Captures/cameraPerspectiveSystem.cs:7`

**概要**: プレイヤーが目標物をカメラ内に収めると「撮影成功」と判定するシステム。距離・角度・画面内判定を行い、撮影音、オブジェクトの有効化、イベント、近接音を扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Look List | `objectToLookList` | `List<GameObject>` | new List<GameObject> () | – |
| Max Distance | `maxDistance` | `float` | – | – |
| Max Angle | `maxAngle` | `float` | – | – |
| Proximity Sound Rate | `proximitySoundRate` | `float` | – | – |
| Max Pitch Value | `maxPitchValue` | `float` | 3 | – |
| Layer For Users | `layerForUsers` | `LayerMask` | – | – |
| Activate Object On Capture | `activateObjectOnCapture` | `bool` | – | – |
| Object To Active List | `objectToActiveList` | `List<GameObject>` | new List<GameObject> () | – |
| Disable Object On Capture | `disableObjectOnCapture` | `bool` | – | – |
| Object To Disable List | `objectToDisableList` | `List<GameObject>` | new List<GameObject> () | – |

### Sounds Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Capture Sound | `useCaptureSound` | `bool` | – | – |
| Capture Sound | `captureSound` | `AudioClip` | – | – |
| Capture Audio Element | `captureAudioElement` | `AudioElement` | – | – |
| Use Proximity Sound | `useProximitySound` | `bool` | – | – |
| Proximity Sound | `proximitySound` | `AudioClip` | – | – |
| Proximity Audio Element | `proximityAudioElement` | `AudioElement` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Capture Taken Correctly | `captureTakenCorrectly` | `bool` | – | – |
| Player Inside | `playerInside` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event Function | `useEventFunction` | `bool` | – | – |
| Event Function | `eventFunction` | `UnityEvent` | new UnityEvent () | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Arrow Length | `gizmoArrowLength` | `float` | 1 | – |
| Gizmo Arrow Angle | `gizmoArrowAngle` | `float` | 20 | – |
| Gizmo Arrow Color | `gizmoArrowColor` | `Color` | Color.white | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Position To Stay | `positionToStay` | `Transform` | – | – |
| Position To Look | `positionToLook` | `Transform` | – | – |
| Bip Audio Source | `bipAudioSource` | `AudioSource` | – | – |
| Capture Audio Source | `captureAudioSource` | `AudioSource` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の `updateCoroutine` を停止するだけ。 |
| `checkCurrentPlayerPosition(Transform playerPosition, Transform cameraTransform, Camera deviceCamera)` | 距離と角度、対象物の画面内判定がすべて成立すれば撮影成功として効果音・オブジェクト切替・イベントを実行し、更新を止める。 |
| `playSound()` | `useCaptureSound` が有効なら、ピッチを整えて撮影音を一度再生する。 |
| `checkTriggerInfo(Collider col, bool isEnter)` | レイヤー一致時、進入ならプレイヤーと `smartphoneDevice` を登録して近接音コルーチンを開始し、退出なら解除して停止する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventFunction` | `UnityEvent` | – |
