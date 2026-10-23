# smartphoneDevice

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/New Weapon Behaviors/smartphoneDevice.cs:7`

**概要**: 武器として持つスマートフォンを表現し、画面・カメラ・フラッシュ・ズームを制御するコンポーネント。写真撮影、キャプチャ保存、撮影対象イベント、ズーム更新コルーチンを扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Make Photos | `canMakePhotos` | `bool` | – | – |
| Use Photo Sound | `usePhotoSound` | `bool` | – | – |
| Photo Sound | `photoSound` | `AudioClip` | – | – |
| Photo Audio Element | `photoAudioElement` | `AudioElement` | – | – |
| Can Use Flash | `canUseFlash` | `bool` | – | – |
| Flash Duration | `flashDuration` | `float` | 0.1f | – |
| Store Captures Enabled | `storeCapturesEnabled` | `bool` | true | – |

### Raycast Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Capsule Raycast | `useCapsuleRaycast` | `bool` | – | – |
| Capsule Cast Radius | `capsuleCastRadius` | `float` | – | – |

### Zoom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Use Zoom | `canUseZoom` | `bool` | – | – |
| Max Zoom Amout | `maxZoomAmout` | `float` | – | – |
| Min Zoom Amount | `minZoomAmount` | `float` | – | – |
| Zoom Speed | `zoomSpeed` | `float` | – | – |

### Check Objects On Capture Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Object Found On Capture | `checkObjectFoundOnCapture` | `bool` | – | – |
| Layer To Check Object Found | `layerToCheckObjectFound` | `LayerMask` | – | – |
| Ray Distance To Check Object Found | `rayDistanceToCheckObjectFound` | `float` | – | – |
| Raycast Transform | `raycastTransform` | `Transform` | – | – |
| Use Override System On Capture | `useOverrideSystemOnCapture` | `bool` | – | – |
| Send Object On Capture | `sendObjectOnCapture` | `bool` | – | – |
| Object To Send On Capture | `objectToSendOnCapture` | `GameObject` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Capture | `useEventOnCapture` | `bool` | – | – |
| Event On Capture | `eventOnCapture` | `UnityEvent` | – | – |
| Use Events On Camera View Change | `useEventsOnCameraViewChange` | `bool` | – | – |
| Event On Camera View Change To Third Person | `eventOnCameraViewChangeToThirdPerson` | `UnityEvent` | – | – |
| Event On Camera View Change To First Person | `eventOnCameraViewChangeToFirstPerson` | `UnityEvent` | – | – |
| Use Events On Smartphone Turn On Off | `useEventsOnSmartphoneTurnOnOff` | `bool` | – | – |
| Event On Smartphone Turned On | `eventOnSmartphoneTurnedOn` | `UnityEvent` | – | – |
| Event On Smartphone Turned Off | `eventOnSmartphoneTurnedOff` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| First Person Active | `firstPersonActive` | `bool` | – | – |
| Is Activated | `isActivated` | `bool` | – | – |
| Perspective System Located | `perspectiveSystemLocated` | `bool` | – | – |

### Smartphone Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Smartphone Camera | `smartphoneCamera` | `GameObject` | – | – |
| Smartphone Screen Canvas | `smartphoneScreenCanvas` | `GameObject` | – | – |
| Smartphone Screen Center | `smartphoneScreenCenter` | `GameObject` | – | – |
| Camera Flash | `cameraFlash` | `GameObject` | – | – |
| Main Screen Center | `mainScreenCenter` | `Transform` | – | – |
| Screen Center | `screenCenter` | `Transform` | – | – |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |
| Smartphone Main Camera | `smartphoneMainCamera` | `Camera` | – | – |

### Player Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Camera Transform | `playerCameraTransform` | `Transform` | – | – |
| Weapon Manager | `weaponManager` | `playerWeaponSystem` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Camera Capture Manager | `cameraCaptureManager` | `cameraCaptureSystem` | – | – |
| Main Override Element Control System | `mainOverrideElementControlSystem` | `overrideElementControlSystem` | – | – |
| Main Event Object Found On Raycast System | `mainEventObjectFoundOnRaycastSystem` | `eventObjectFoundOnRaycastSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の`updateCoroutine`を停止するだけ。 |
| `takePhoto()` | 撮影可能ならサウンドとフラッシュ、キャプチャ保存、視点システム確認、対象レイキャスト、撮影イベントを実行する。 |
| `checkFlash()` | フラッシュ使用が有効なら既存コルーチンを止め、`flashDuration`だけ点灯するコルーチンを開始する。 |
| `changeZoom()` | ズーム中フラグを反転するだけ。 |
| `turnOn()` | `isActivated`をtrueにして`setSmartphoneState`を呼ぶだけ。 |
| `turnOff()` | `isActivated`をfalseにして`setSmartphoneState`を呼ぶだけ。 |
| `changeSmartphoneState()` | 現在の状態を反転して`setSmartphoneState`を呼ぶだけ。 |
| `setSmartphoneState(bool state)` | 画面・中心・カメラの表示とズーム状態を切り替え、レイヤー設定・イベント・更新コルーチンを制御する。 |
| `playSound()` | 撮影音が有効ならピッチを確認して`AudioPlayer`で1ショット再生するだけ。 |
| `setCurrentPerspectiveSystem(cameraPerspectiveSystem perspective)` | 視点システムを設定し、nullでないかをフラグに反映するだけ。 |
| `removeCurrentPerspectiveSystem()` | 視点システム参照をnullにしてフラグもfalseにするだけ。 |
| `getSmarthphoneMainCamera()` | スマートフォンのメインカメラを返すだけ。 |
| `setUseEventOnCaptureState(bool state)` | 撮影時イベントの使用フラグを設定するだけ。 |
| `setStoreCapturesEnabledState(bool state)` | キャプチャ保存の有効フラグを設定するだけ。 |
| `setUseOverrideSystemOnCaptureState(bool state)` | 撮影時の上書きシステム使用フラグを設定するだけ。 |
| `rotateScreenToRight()` | 画面とカメラのローカル回転をゼロに戻すだけ。 |
| `rotateScreenToLeft()` | 画面とカメラのローカル回転をZ軸180度に設定するだけ。 |
| `setFirstOrThirdPersonViewState(bool state)` | 一人称かどうかのフラグを設定し、視点変更イベントが有効なら対応するイベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCapture` | `UnityEvent` | – |
| `eventOnCameraViewChangeToThirdPerson` | `UnityEvent` | – |
| `eventOnCameraViewChangeToFirstPerson` | `UnityEvent` | – |
| `eventOnSmartphoneTurnedOn` | `UnityEvent` | – |
| `eventOnSmartphoneTurnedOff` | `UnityEvent` | – |
