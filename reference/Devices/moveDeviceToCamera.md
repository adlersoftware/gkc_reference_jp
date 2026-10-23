# moveDeviceToCamera

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/moveDeviceToCamera.cs:6`

**概要**: デバイス本体をプレイヤーカメラの前に引き寄せて観察させるコンポーネント。終了時は元の親・位置・回転へ戻す。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Device Game Object | `deviceGameObject` | `GameObject` | – | カメラの前へ移動させて表示する機器のゲームオブジェクト。 |
| Smooth Camera Movement | `smoothCameraMovement` | `bool` | true | オンにすると機器の移動を補間して滑らかにする。 |
| Use Fixed Lerp Movement | `useFixedLerpMovement` | `bool` | true | オンにすると距離ではなく固定速度で機器を補間移動する。 / 表示条件: `smoothCameraMovement` がオンのとき |
| Fixed Lerp Movement Speed | `fixedLerpMovementSpeed` | `float` | 2 | 固定補間移動での1秒あたりの補間進行量。 / 表示条件: `smoothCameraMovement.boolValue && useFixedLerpMovement.boolValue` |
| Camera Movement Speed Third Person | `cameraMovementSpeedThirdPerson` | `float` | 2 | 三人称時の機器移動速度で、移動時間の計算に使う。 / 表示条件: `smoothCameraMovement` がオンのとき |
| Camera Movement Speed First Person | `cameraMovementSpeedFirstPerson` | `float` | 1 | 一人称時の機器移動速度で、移動時間の計算に使う。 / 表示条件: `smoothCameraMovement` がオンのとき |
| Distance From Camera | `distanceFromCamera` | `float` | – | カメラ前方どれだけ離して機器を置くかの距離。 |
| Rotate Object On Camera Direction Enabled | `rotateObjectOnCameraDirectionEnabled` | `bool` | true | オンにすると機器をカメラの向きに合わせて回転させる。 |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer To Examinate Devices | `layerToExaminateDevices` | `string` | – | 調査中に機器の子オブジェクトへ一時的に設定するレイヤー名。 |
| Activate Examinate Object System | `activateExaminateObjectSystem` | `bool` | – | 使用時に`examineObjectManager`の調査処理を呼ぶ。 |
| Object Has Active Rigidbody | `objectHasActiveRigidbody` | `bool` | – | オンにすると移動中は機器のRigidbodyをキネマティックにする。 |
| Disable Player Mesh Game Object | `disablePlayerMeshGameObject` | `bool` | true | オンにすると使用中にプレイヤーのメッシュを非表示にする。 |
| Ignore FBA Active If Disable Player Mesh | `ignoreFBAActiveIfDisablePlayerMesh` | `bool` | – | FBAが有効でもプレイヤーメッシュの無効化を適用する。 |
| Use Blur UI Panel | `useBlurUIPanel` | `bool` | – | オンにすると調査カメラの背景にブラーパネルを表示する。 |
| Use Examine Device Camera Enabled | `useExamineDeviceCameraEnabled` | `bool` | true | 調査用カメラに切り替え、機器をそのカメラだけに描画させる。 |
| Set New Mouse Cursor Controller Speed | `setNewMouseCursorControllerSpeed` | `bool` | – | 使用中だけマウスカーソル速度を別の値に差し替える。 |
| New Mouse Cursro Controller Speed | `newMouseCursroControllerSpeed` | `float` | – | 差し替えるマウスカーソル速度の値。 / 表示条件: `setNewMouseCursorControllerSpeed` がオンのとき |
| Hide Mouse Cursor If Using Gamepad | `hideMouseCursorIfUsingGamepad` | `bool` | – | ゲームパッド操作中は使用中にカーソルを隠す。 |

### HUD Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disable All Player HUD | `disableAllPlayerHUD` | `bool` | – | 使用中はプレイヤーHUDをすべて非表示にする。 |
| Disable Secondary Player HUD | `disableSecondaryPlayerHUD` | `bool` | true | `disableAllPlayerHUD`がオフの時、サブHUDのみ隠す。 |
| Disable Interaction Touch Button On Using Device | `disableInteractionTouchButtonOnUsingDevice` | `bool` | true | 使用中はインタラクション用のタッチボタンを隠す。 |

### Zoom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Max Zoom Distance | `maxZoomDistance` | `float` | – | ズームアウト時のカメラからの最大距離。 |
| Min Zoom Distance | `minZoomDistance` | `float` | – | ズームイン時のカメラからの最小距離。 |
| Zoom Speed | `zoomSpeed` | `float` | – | ズーム時に1秒あたりに距離を変える量。 |

### Collider List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Device Trigger | `deviceTrigger` | `Collider` | – | 使用中に無効化する機器側のトリガーコライダー。 |

### Disabled Object List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use List Of Disabled Objects | `useListOfDisabledObjects` | `bool` | – | `disabledObjectList`のオブジェクトを開始時に無効化する。 |

### Weapons Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Keep Weapons If Carrying | `keepWeaponsIfCarrying` | `bool` | – | 武器を持ったまま使用できるようにする。 |
| Draw Weapons If Previously Carrying | `drawWeaponsIfPreviouslyCarrying` | `bool` | – | 使用終了時に以前持っていた武器を再び構えさせる。 / 表示条件: `keepWeaponsIfCarrying` がオンのとき |
| Keep Only If Player Is On First Person | `keepOnlyIfPlayerIsOnFirstPerson` | `bool` | – | 一人称の時だけ武器の保持と再構えを行う。 / 表示条件: `keepWeaponsIfCarrying` がオンのとき |
| Disable Weapons Directly On Start | `disableWeaponsDirectlyOnStart` | `bool` | – | 使用開始時に所持武器を即座に無効化する。 / 表示条件: `keepWeaponsIfCarrying` がオンのとき |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Examine Object Manager | `examineObjectManager` | `examineObjectSystem` | – | 調査処理を担当する`examineObjectSystem`への参照。 |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | 移動中に物理を止める機器のRigidbody。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `disabledObjectList` | `List<GameObject>` | new List<GameObject> () | – |
| `colliderListToDisable` | `List<Collider>` | new List<Collider> () | – |
| `colliderListButtons` | `List<Collider>` | new List<Collider> () | – |
| `ignoreDeviceTriggerEnabled` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `moveCamera(bool state)` | デバイスをカメラの子にして手前へ移動し、操作停止や武器・HUD・コライダーを切替、終了時は元の位置と親へ戻す。 |
| `checkCameraPosition()` | 実行中の移動コルーチンを止め、`adjustCamera`を再開始する。 |
| `setRigidbodyState(bool state)` | `objectHasActiveRigidbody`のとき、元値を退避して重力と`isKinematic`を切り替える。 |
| `setCurrentPlayer(GameObject player)` | プレイヤーを保持し、制御・カメラ・武器・足音などの各コンポーネントを取得する。 |
| `setColliderListState(bool state)` | 指定コライダー群の有効状態を設定し、プレイヤーとの衝突判定を`deviceEnabled`に応じ無視させる。 |
| `setIgnoreDeviceTriggerEnabledState(bool state)` | `ignoreDeviceTriggerEnabled`を設定するだけ。 |
| `setLayerList()` | 子`Transform`を走査して元レイヤーを記録し、`disabledObjectList`の要素を非アクティブ化する。 |
| `setLayerListState(bool state)` | 記録した各オブジェクトのレイヤーを、元の値か`layerToExaminateDevices`へ切り替える。 |
| `changeDeviceZoom(bool zoomIn)` | `zoomIn`に応じカメラからの距離を増減し、上下限でクランプして移動を再開する。 |
| `resetRotation()` | 現在位置を目標に、回転だけを`Quaternion.identity`へ戻して移動を再開する。 |
| `resetRotationAndPosition()` | 初期距離の正面位置と`Quaternion.identity`回転を目標にして移動を再開する。 |

## 内部型

- `layerInfo`（class）
