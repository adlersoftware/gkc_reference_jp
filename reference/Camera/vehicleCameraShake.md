# vehicleCameraShake

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Vehicles/vehicleCameraShake.cs:5`

**概要**: 車両のメインカメラにヘッドボブ/シェイク状態を適用するコンポーネント。状態名ごとの回転揺れを補間し、外部シェイクは継続時間後に停止する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Head Bob Enabled | `headBobEnabled` | `bool` | – | オンにすると走行中の頭ぶれ揺れを有効にする。 |
| External Force State Name | `externalForceStateName` | `string` | – | 外部シェイクで使用する揺れステートの名前。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `bobStatesList` | `List<bobStates>` | new List<bobStates> () | – |
| `shakingActive` | `bool` | – | – |
| `ResetSpeed` | `float` | – | – |
| `playerBobState` | `bobStates` | – | – |
| `externalShake` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `startShake(string shakeName)` | 名前が現在と異なれば一致する `bobStates` を選択して他を非選択にし、揺れを有効化して更新コルーチンを開始する。 |
| `stopUpdateCoroutine()` | `updateCoroutine` を停止するだけ。 |
| `stopShake()` | 揺れを止めてカメラ回転を戻すコルーチンを開始し、状態名をクリアして更新も停止する。 |
| `getCurrentCameraTransform(Transform currentCameraTransform)` | `mainCamera` を設定し、null でないかで割り当て済みフラグを更新するだけ。 |
| `setExternalShakeState(externalShakeInfo shakeInfo)` | 外部シェイク状態を開始し、回転量・補間・速度・継続時間を `shakeInfo` から設定する。 |
| `setExternalShakeDuration()` | `externalShake` を立て、継続時間後に揺れを止めるコルーチンを開始する。 |
| `setVehicleActiveState(bool state)` | `vehicleActive` を設定するだけ。 |

## 内部型

- `bobStates`（class）
