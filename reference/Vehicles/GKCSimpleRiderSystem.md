# GKCSimpleRiderSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `mainRiderSystem`
- **ソース**: `Vehicles/GKCSimpleRiderSystem.cs:7`

**概要**: 座席単位の簡易ライダー/乗降システム。プレイヤーやAIを運転席・助手席へ乗降させ、乗客ごとのコンポーネント参照と状態ID、HUD・入力・カメラ・武器の切り替えを管理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Name | `vehicleName` | `string` | – | – |
| Player Is Always Driver | `playerIsAlwaysDriver` | `bool` | true | – |
| Vehicle Radius | `vehicleRadius` | `float` | 3 | – |
| Player Visible In Vehicle | `playerVisibleInVehicle` | `bool` | true | – |
| Reset Camera Rotation When Get Off | `resetCameraRotationWhenGetOff` | `bool` | – | – |
| Reset Animator Driving State ID | `resetAnimatorDrivingStateID` | `int` | 666777 | – |
| Obstacle Layer | `obstacleLayer` | `LayerMask` | – | – |
| Check If Driver Is On Ground On Get Off | `checkIfDriverIsOnGroundOnGetOff` | `bool` | – | – |
| Ignore Obstacle Check On Get Off Enabled | `ignoreObstacleCheckOnGetOffEnabled` | `bool` | – | – |

### Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hide Player Weapons While Driving | `hidePlayerWeaponsWhileDriving` | `bool` | – | – |
| Draw Fire Weapon If Carrying Previously | `drawFireWeaponIfCarryingPreviously` | `bool` | true | – |
| Draw Melee Weapon If Carrying Previously | `drawMeleeWeaponIfCarryingPreviously` | `bool` | true | – |

### Vehicle Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Vehicle Weapons Enabled | `useVehicleWeaponsEnabled` | `bool` | – | – |
| Vehicle Weapon System Use Rotation Input | `vehicleWeaponSystemUseRotationInput` | `bool` | – | – |
| Default Vehicle Weapon System Camera Transform | `defaultVehicleWeaponSystemCameraTransform` | `Transform` | – | – |

### UI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disable Player HUD Enabled | `disablePlayerHUDEnabled` | `bool` | true | – |
| Show Vehicle HUD | `showVehicleHUD` | `bool` | – | – |

### GameObject Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Game Object | `vehicleGameObject` | `GameObject` | – | – |
| Passenger Parent | `passengerParent` | `Transform` | – | – |
| Custom Vehicle Game Object | `customVehicleGameObject` | `GameObject` | – | – |
| Vehicle Camera Direction | `vehicleCameraDirection` | `Transform` | – | – |

### Ride Object On Start Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Start Game In This Vehicle | `startGameInThisVehicle` | `bool` | – | – |
| Set Current Player Manually | `setCurrentPlayerManually` | `bool` | – | – |
| Search Player On Scene If Not Assigned | `searchPlayerOnSceneIfNotAssigned` | `bool` | true | – |
| Player For Vehicle | `playerForVehicle` | `GameObject` | – | – |

### Rider Single Driver Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| IK Rider Info | `IKRiderInfo` | `IKDrivingSystem.IKDrivingInformation` | – | – |

### Rider Driver And Passengers Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| IK Vehicle Passengers List | `IKVehiclePassengersList` | `List<IKDrivingSystem.IKDrivingInformation>` | new List<IKDrivingSystem.IKDrivingInf… | – |

### Override System Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Use Override System | `objectUseOverrideSystem` | `bool` | – | – |
| Main Object To Override System | `mainObjectToOverrideSystem` | `objectToOverrideSystem` | – | – |

### Gravity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Driver Gravity When Gets Off | `changeDriverGravityWhenGetsOff` | `bool` | true | – |
| Regular Gravity | `regularGravity` | `Vector3` | new Vector3 (0, 1, 0) | – |
| Current Normal | `currentNormal` | `Vector3` | new Vector3 (0, 1, 0) | – |
| Min Angle Difference To Regular Gravity To Change When Get Off | `minAngleDifferenceToRegularGravityToChangeWhenGetOff` | `float` | 40 | – |
| Check Vehicle Up Direction For Gravity On Get Off | `checkVehicleUpDirectionForGravityOnGetOff` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Collider Parts | `colliderParts` | `List<Collider>` | new List<Collider> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Rider Active | `riderActive` | `bool` | – | – |
| Destroyed | `destroyed` | `bool` | – | – |
| Current Rider Game Object | `currentRiderGameObject` | `GameObject` | – | – |
| Is Being Driven | `isBeingDriven` | `bool` | – | – |
| Passenger Is Getting On | `passengerIsGettingOn` | `bool` | – | – |
| Passenger Game Object List | `passengerGameObjectList` | `List<GameObject>` | new List<GameObject> () | – |
| Passenger Components List | `passengerComponentsList` | `List<IKDrivingSystem.passengerComponents>` | new List<IKDrivingSystem.passengerCom… | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Driver Get On | `useEventOnDriverGetOn` | `bool` | – | – |
| Event On Driver Get On | `eventOnDriverGetOn` | `eventParameters.eventToCallWithGameObject` | – | – |
| Use Event On Driver Get Off | `useEventOnDriverGetOff` | `bool` | – | – |
| Event On Driver Get Off | `eventOnDriverGetOff` | `eventParameters.eventToCallWithGameObject` | – | – |
| Use Event On Start Game | `useEventOnStartGame` | `bool` | – | – |
| Delay To Activate Events On Start | `delayToActivateEventsOnStart` | `float` | – | – |
| Event On Start Game | `eventOnStartGame` | `UnityEvent` | – | – |

### Remote Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Events On Passengers | `useRemoteEventsOnPassengers` | `bool` | – | – |
| Remote Event Name List Get On | `remoteEventNameListGetOn` | `List<string>` | new List<string> () | – |
| Remote Event Name List Get Off | `remoteEventNameListGetOff` | `List<string>` | new List<string> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Input Action Manager | `mainInputActionManager` | `inputActionManager` | – | – |
| Main Vehicle Rigidbody | `mainVehicleRigidbody` | `Rigidbody` | – | – |
| Main Vehicle Weapon System | `mainVehicleWeaponSystem` | `vehicleWeaponSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPlayerToStartGameOnThisVehicle(GameObject newPlayer)` | ゲーム開始時に乗せるプレイヤーを設定し、開始乗車フラグを立てて自動乗車チェックを無効化する。 |
| `setDriverExternally(GameObject currentDriver)` | 対象を運転者として設定し、`usingDevicesSystem` 経由で車両に乗せる。AIの場合は直接配置する。 |
| `setPassengerExternally(GameObject currentDriver)` | 運転席ではなく助手席へ乗せる設定で乗車させ、AIとプレイヤーで処理を分ける。 |
| `stopDriveVehicleExternally()` | 運転中なら `usingDevicesSystem` に車両を再登録してデバイス使用を実行し、降車させる。 |
| `activateDevice()` | 1人用車両でなければ、乗車/降車の乗客処理を実行する。 |
| `setRiderState(bool state)` | ライダーの乗車状態を設定し、必要ならプレイヤー探索を行ってから乗降処理を呼ぶ。 |
| `startOrStopObjectToOverride(bool state)` | 座席情報と乗客コンポーネントを更新し、HUD・入力・カメラ・武器・イベントを乗降に合わせ切り替える。 |
| `startOrStopVehicle(bool state)` | 降車位置と座席を決め、アクションシステムまたは直接配置で乗客を乗降させる。 |
| `stopEnterExitActionSystemOnPassengerCoroutine(Coroutine passengerCoroutine)` | 渡されたコルーチンがnullでなければ停止するだけ。 |
| `enableOrDisablePlayerVisibleInVehicle(bool state, IKDrivingSystem.passengerComponents newPassengerComponents)` | 一人称以外ではキャラメッシュと武器メッシュを、一人称ではキャラメッシュ本体の表示を切り替える。 |
| `getGetOffPosition(IKDrivingSystem.IKDrivingInformation passengerInfo)` | 座席の降車側設定に応じ、右または左の降車位置を返す。 |
| `removePassengerInfo(IKDrivingSystem.IKDrivingInformation passengerInfo)` | 乗客の状態IDや接地状態を元に戻し、乗客リストと座席情報から該当者を削除する。 |
| `getPassengerGetOffPosition(GameObject currentPassenger)` | 空席を探して乗客を登録し、障害物を調べて降車可能な位置を返す。 |
| `setPassengerGravityState(IKDrivingSystem.passengerComponents currentPassengerComponents)` | 降車時、車両の上方向が通常重力と十分異なればプレイヤーの重力法線をその向きに変更する。 |
| `setChangeDriverGravityWhenGetsOffState(bool state)` | `changeDriverGravityWhenGetsOff` を設定するだけ。 |
| `setCurrentNormal(Vector3 newValue)` | `currentNormal` を設定するだけ。 |
| `getHUDBars(playerHUDManager newVehicleHUDInfo, playerHUDManager.vehicleHUDElements hudElements, bool drivingState)` | HUDの弾薬要素を取得し、武器システムと乗車状態に応じて弾薬表示とカーソルを切り替える。 |
| `setWeaponState(bool state)` | 武器システムが有効なら武器状態を変更し、弾薬表示と車両カーソルの表示を切り替える。 |
| `setVehicleWeaponsComponents()` | 未初期化なら武器システムのコンポーネントを初期化し、初期化済みフラグを立てる。 |
| `getAmmo(string ammoName, int amount)` | 武器システムがあれば、武器名を指定して弾薬を追加する。 |
| `setDestroyedState(bool state)` | `destroyed` を設定するだけ。 |
| `setWeaponName(string name, int ammoPerClip, int clipSize)` | 武器名テキストと弾薬スライダーの最大値・現在値を更新する。 |
| `useAmmo(int clipSize, int remainAmmo)` | 弾薬表示を「残弾/総弾」形式で更新し、残弾が-1なら無限として`Inf`を表示する。 |
| `reactivateCollidersIfPossible()` | 各コライダーを一度無効化して再度有効にし、当たり判定を再評価させる。 |
| `getIKVehiclePassengerInfo(GameObject passenger)` | 指定乗客に一致する `IKDrivingInformation` を探して返す。 |
| `setPassengerInfo(IKDrivingSystem.IKDrivingInformation passengerInfo, GameObject passenger)` | 未登録なら乗客を追加して座席に割り当て、乗車処理ならtrueを返す。 |
| `getRiderGameObject(GameObject newRiderGameObject)` | `currentRiderGameObject` を設定するだけ。 |
| `setPassengerComponents(GameObject currentPassenger)` | 乗客の各コンポーネントを収集し、状態IDを退避して初期化したうえで乗客リストに追加する。 |
| `checkDriverHeadMeshOnCameraViewChange(bool isFirstPersonCamera)` | 運転中なら運転者の頭部スケールを一人称/三人称の視点に合わせて変更する。 |
| `findPlayerOnScene()` | 設定が有効ならシーン内のプレイヤーを探してライダーに設定する。 |
| `killCharacterOnVehicle()` | 運転中なら降車位置を車両上方に設定して降車させ、その後キャラクターを死亡させる。 |
| `ejectCharacterFromVehicle()` | 運転中なら降車位置を車両上方に設定して降車させる。 |
| `getOffFromVehicle()` | 運転中ならデバイス使用を実行して降車させる。 |
| `getVehicleName()` | `vehicleName` を返すだけ。 |
| `isVehicleFull()` | 乗客リストの数と座席数が一致するかどうかを返す。 |
| `getDriverSeatPassengerIndex()` | 運転席の座席インデックスを返し、運転席が無ければ-1を返す。 |
| `getClosestSeatToPassengerIndex(GameObject currentPassenger)` | 搭乗可否を満たす空席のうち、乗客に最も近い席のインデックスを返す。 |
| `setPauseDriverGetOffInputActionState(bool state)` | 運転中なら運転者の降車ボタンの入力可否を切り替える。 |
| `inputGetOffFromVehicle()` | 運転中なら `getOffFromVehicle` を呼ぶだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartGame` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkIfDetectSurfaceBelongToVehicle(Collider surfaceFound)`, `getCurrentDriver()`, `getCustomVehicleTransform()`, `getVehicleCollider()`, `getVehicleGameObject()`, `getVehicleRadius()`, `isBeingDrivenActive()`, `setCurrentPassenger(GameObject passenger)`, `setEnteringOnVehicleFromDistanceState(bool state)`, `setPlayerVisibleInVehicleState(bool state)`

</details>
