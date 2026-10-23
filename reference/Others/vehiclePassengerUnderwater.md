# vehiclePassengerUnderwater

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/vehiclePassengerUnderwater.cs:6`

**概要**: 車両の乗員が水中に入ったかをカメラ位置で判定し、水中エフェクト用のイベントを発火する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Passenger Under Water State Enabled | `passengerUnderWaterStateEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Passenger Underwater Active | `vehiclePassengerUnderwaterActive` | `bool` | – | – |
| Camera Below Water | `cameraBelowWater` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Camera Underwater Effect | `useEventOnCameraUnderwaterEffect` | `bool` | – | – |
| Event On Camera Under Water Start | `eventOnCameraUnderWaterStart` | `UnityEvent` | – | – |
| Event On Camera Under Water End | `eventOnCameraUnderWaterEnd` | `UnityEvent` | – | – |
| Use Events On Underwater State Change | `useEventsOnUnderwaterStateChange` | `bool` | – | – |
| Event On Start Under Water | `eventOnStartUnderWater` | `UnityEvent` | – | – |
| Event On End Underwater | `eventOnEndUnderwater` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Current Swim Trigger | `currentSwimTrigger` | `BoxCollider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`があれば停止するだけ。 |
| `disableVehiclePassengerUnderwaterStateWithoutCallingEvents()` | 有効時のみ状態と`cameraBelowWater`を`false`にし、更新コルーチンを止める（イベントは呼ばない）。 |
| `setVehiclePassengerUnderwaterState(bool state)` | 設定有効かつ状態変化時のみ、更新コルーチンの開始/停止と水中状態のイベント発火を行う。 |
| `setCurrentSwimTrigger(BoxCollider newCollider)` | `currentSwimTrigger`を差し替え、nullでないかを`currentSwimTriggerLocated`に記録する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCameraUnderWaterStart` | `UnityEvent` | – |
| `eventOnCameraUnderWaterEnd` | `UnityEvent` | – |
| `eventOnStartUnderWater` | `UnityEvent` | – |
| `eventOnEndUnderwater` | `UnityEvent` | – |
