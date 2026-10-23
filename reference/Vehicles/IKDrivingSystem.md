# IKDrivingSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `mainRiderSystem`
- **ソース**: `Vehicles/IKDrivingSystem.cs:6`

**概要**: 車両の座席と乗員を管理し、乗降処理・IK目標・カメラ切替・運転手の取得・破壊時の排出や爆発を担当する。`mainRiderSystem`を継承し、各席の`IKDrivingInformation`を保持する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Driver Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle | `vehicle` | `GameObject` | – | 運転対象の車両本体オブジェクト。乗車位置やカメラ基準の算出に使われる。 |
| Vehicel Camera Game Object | `vehicelCameraGameObject` | `GameObject` | – | 車両カメラの基準オブジェクト。降車時のカメラ向きや射出方向の計算に使う。 |
| Use Custom Vehicle Game Object | `useCustomVehicleGameObject` | `bool` | – | 車両本体とは別のオブジェクトを基準Transformとして使うかどうか。 |
| Custom Vehicle Game Object | `customVehicleGameObject` | `GameObject` | – | 基準として使うオブジェクト。揺れる車体や砲塔などの追従に使う。 / 表示条件: `useCustomVehicleGameObject` がオンのとき |
| Player Is Always Driver | `playerIsAlwaysDriver` | `bool` | true | 空いていればプレイヤーを必ず運転席に座らせるかどうか。 |
| Hide Player From NPCs | `hidePlayerFromNPCs` | `bool` | – | ONにするとNPCへ現在の運転者を返さず、プレイヤーを隠す。 |
| Player Visible In Vehicle | `playerVisibleInVehicle` | `bool` | true | ONなら搭乗中もプレイヤーのメッシュを表示し、OFFなら隠す。 |
| Hide Player Weapons While Driving | `hidePlayerWeaponsWhileDriving` | `bool` | – | ONにすると乗車中は装備中の武器メッシュを非表示にする。 |
| Can Be Driven Remotely | `canBeDrivenRemotely` | `bool` | – | プレイヤーが乗らずに遠隔操作で運転できるようにするかどうか。 |
| Reset Animator Driving State ID | `resetAnimatorDrivingStateID` | `int` | 666777 | 降車時に設定するアクションID。運転ポーズを解除する。 |
| Ignore Obstacle Check On Get Off Enabled | `ignoreObstacleCheckOnGetOffEnabled` | `bool` | – | ONにすると降車位置の障害物判定を省略し、常に降車可能にする。 |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Can Be Stolen | `vehicleCanBeStolen` | `bool` | – | NPCが運転中の車両をプレイヤーが奪えるようにするかどうか。 |
| Check If Stealer Selecting Driver Seat | `checkIfStealerSelectingDriverSeat` | `bool` | – | 奪う際に運転席を選んでいる場合だけ成功させるかどうか。 |
| Use Remote Events On Previuos Driver On Steal | `useRemoteEventsOnPreviuosDriverOnSteal` | `bool` | – | 奪った際、元の運転者へリモートイベントを送るかどうか。 |
| Force Passengers To Get Off On External Destroy | `forcePassengersToGetOffOnExternalDestroy` | `bool` | – | 外部要因で車両が破壊された時、乗員を強制的に降ろすかどうか。 |

### Passengers Weapons Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Draw Fire Weapon If Carrying Previously | `drawFireWeaponIfCarryingPreviously` | `bool` | true | 降車時、乗る前に持っていた射撃武器を再び構えるかどうか。 |
| Draw Melee Weapon If Carrying Previously | `drawMeleeWeaponIfCarryingPreviously` | `bool` | true | 降車時、乗る前に持っていた近接武器を再び構えるかどうか。 |

### Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Reset Camera Rotation When Get On | `resetCameraRotationWhenGetOn` | `bool` | true | 乗車時にプレイヤーカメラの向きを車両の正面へ合わせるかどうか。 |
| Reset Camera Rotation When Get Off | `resetCameraRotationWhenGetOff` | `bool` | – | 降車時にカメラの向きをプレイヤーの背後へ戻すかどうか。 |
| Set Player Camera State On Get Off | `setPlayerCameraStateOnGetOff` | `bool` | – | 降車時にプレイヤーのカメラステートを指定値へ切り替えるかどうか。 |
| Set Player Camera State On First Person On Get Off | `setPlayerCameraStateOnFirstPersonOnGetOff` | `bool` | – | 降車時、一人称カメラへ切り替えるかどうか。 / 表示条件: `setPlayerCameraStateOnGetOff` がオンのとき |
| Player Camera State On Get Off | `playerCameraStateOnGetOff` | `string` | – | 降車時に適用するプレイヤーカメラステートの名前。 / 表示条件: `setPlayerCameraStateOnGetOff.boolValue && !setPlayerCameraStateOnFirstPersonOnGetOff.boolValue` |
| Set Vehicle Camera State On Get On | `setVehicleCameraStateOnGetOn` | `bool` | – | 乗車時に車両カメラのステートを指定値へ切り替えるかどうか。 |
| Set Vehicle Camera State On First Person On Get On | `setVehicleCameraStateOnFirstPersonOnGetOn` | `bool` | – | 乗車時、車両カメラを一人称視点にするかどうか。 / 表示条件: `setVehicleCameraStateOnGetOn` がオンのとき |
| Vehicle Camera State On Get On | `vehicleCameraStateOnGetOn` | `string` | – | 乗車時に適用する車両カメラステートの名前。 / 表示条件: `setVehicleCameraStateOnGetOn` がオンのとき |

### Eject Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Eject Player When Destroyed | `ejectPlayerWhenDestroyed` | `bool` | – | 車両破壊時に乗員を射出するか、その場で死亡させるかの切り替え。 |
| Ejecting Player Force | `ejectingPlayerForce` | `float` | – | 破壊時に乗員を射出する力の大きさ。 / 表示条件: `ejectPlayerWhenDestroyed` がオンのとき |
| Activate Free Floating Mode On Eject | `activateFreeFloatingModeOnEject` | `bool` | – | 射出されたプレイヤーをフリーフローティング状態へ移行するかどうか。 |
| Activate Free Floating Mode On Eject Delay | `activateFreeFloatingModeOnEjectDelay` | `float` | 0.5f | フリーフローティングへ切り替えるまでの遅延秒数。 |

### Explosion Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Explosion Force When Destroyed | `useExplosionForceWhenDestroyed` | `bool` | – | 破壊時に爆発を起こし、範囲へダメージと力を与えるかどうか。 |
| Explosion Radius | `explosionRadius` | `float` | – | 爆発が影響を及ぼす範囲の半径。 / 表示条件: `useExplosionForceWhenDestroyed` がオンのとき |
| Explosion Force | `explosionForce` | `float` | – | 爆発で対象を吹き飛ばす力の強さ。 / 表示条件: `useExplosionForceWhenDestroyed` がオンのとき |
| Explosion Damage | `explosionDamage` | `float` | – | 爆発で対象に与えるダメージ量。 / 表示条件: `useExplosionForceWhenDestroyed` がオンのとき |
| Ignore Shield | `ignoreShield` | `bool` | – | 爆発ダメージがシールドを無視するかどうか。 / 表示条件: `useExplosionForceWhenDestroyed` がオンのとき |
| Damage Type ID | `damageTypeID` | `int` | -1 | 爆発ダメージの種類ID。耐性や表示の分類に使う。 / 表示条件: `useExplosionForceWhenDestroyed` がオンのとき |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | 爆発ダメージをガードで防げるようにするかどうか。 / 表示条件: `useExplosionForceWhenDestroyed` がオンのとき |
| Search Closest Weak Spot | `searchClosestWeakSpot` | `bool` | – | 爆発時に最も近い弱点を探してダメージを与えるかどうか。 / 表示条件: `useExplosionForceWhenDestroyed` がオンのとき |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | 爆発で影響したオブジェクトへリモートイベントを送るかどうか。 / 表示条件: `useExplosionForceWhenDestroyed` がオンのとき |
| Remove Event Name | `removeEventName` | `string` | – | 影響を受けたオブジェクトへ送るリモートイベント名。 / 表示条件: `useExplosionForceWhenDestroyed` がオンのとき |
| Push Characters On Explosion | `pushCharactersOnExplosion` | `bool` | true | 爆発でキャラクターを吹き飛ばすかどうか。 / 表示条件: `useExplosionForceWhenDestroyed` がオンのとき |
| Apply Explosion Force To Vehicles | `applyExplosionForceToVehicles` | `bool` | true | 爆発の力を乗り物にも適用するかどうか。 / 表示条件: `useExplosionForceWhenDestroyed` がオンのとき |
| Explosion Force To Vehicles Multiplier | `explosionForceToVehiclesMultiplier` | `float` | 0.2f | 乗り物へ与える爆発力の倍率値。 / 表示条件: `useExplosionForceWhenDestroyed.boolValue && applyExplosionForceToVehicles.boolValue` |
| Kill Objects In Radius | `killObjectsInRadius` | `bool` | – | 爆発範囲内の対象を即座に破壊するかどうか。 / 表示条件: `useExplosionForceWhenDestroyed` がオンのとき |
| Force Mode | `forceMode` | `ForceMode` | – | 爆発力を加えるForceMode（力か加速度かなど）。 / 表示条件: `useExplosionForceWhenDestroyed` がオンのとき |
| Use Layer Mask | `useLayerMask` | `bool` | – | 爆発対象をレイヤーで絞り込むかどうか。 / 表示条件: `useExplosionForceWhenDestroyed` がオンのとき |
| Layer | `layer` | `LayerMask` | – | 爆発対象とするレイヤーのマスク。 / 表示条件: `useExplosionForceWhenDestroyed.boolValue && useLayerMask.boolValue` |

### Shake Passengers Body Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Collision Force Direction To Passengers | `addCollisionForceDirectionToPassengers` | `bool` | – | ONにすると衝突の勢いを乗員の体の揺れに反映する。 |
| Extra Collision Force Amount | `extraCollisionForceAmount` | `Vector3` | Vector3.one | 衝突の揺れを各軸で増減させる倍率。 / 表示条件: `addCollisionForceDirectionToPassengers` がオンのとき |
| Use Min Collision Force | `useMinCollisionForce` | `bool` | – | 一定以下の衝突では揺れを発生させないようにするかどうか。 / 表示条件: `addCollisionForceDirectionToPassengers` がオンのとき |
| Min Collision Force | `minCollisionForce` | `float` | – | 揺れを発生させる最小の衝突力。 / 表示条件: `addCollisionForceDirectionToPassengers.boolValue && useMinCollisionForce.boolValue` |

### Debug Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Debug Collision Force | `debugCollisionForce` | `Vector3` | – | エディタから衝突の揺れをテストする際に使う力の値。 / 表示条件: `addCollisionForceDirectionToPassengers` がオンのとき |
| Add Angular Direction To Passengers | `addAngularDirectionToPassengers` | `bool` | – | ONにすると旋回や横揺れを乗員の体の傾きに反映する。 |
| Vehicle Stability Speed | `vehicleStabilitySpeed` | `float` | 1 | 旋回による揺れが元の姿勢へ戻る速さ。 / 表示条件: `addAngularDirectionToPassengers` がオンのとき |
| Extra Angular Directio Amount | `extraAngularDirectioAmount` | `Vector3` | – | 旋回による傾きを各軸で増減させる倍率。 / 表示条件: `addAngularDirectionToPassengers` がオンのとき |

### Start Game In Vehicle Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Start Game In This Vehicle | `startGameInThisVehicle` | `bool` | – | ゲーム開始時、この車両にプレイヤーを乗せた状態で始めるかどうか。 |
| Player For Vehicle | `playerForVehicle` | `GameObject` | – | 開始時に乗せるプレイヤーのオブジェクト。 / 表示条件: `startGameInThisVehicle` がオンのとき |

### Action Screen Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Action Screen | `activateActionScreen` | `bool` | – | 乗車中にアクション画面を開けるようにするかどうか。 |
| Action Screen Name | `actionScreenName` | `string` | – | 有効にするアクション画面の名前。 / 表示条件: `activateActionScreen` がオンのとき |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Driver Get On | `useEventOnDriverGetOn` | `bool` | – | 運転者が乗車した時にイベントを呼ぶかどうか。 |
| Event On Driver Get On | `eventOnDriverGetOn` | `eventParameters.eventToCallWithGameObject` | – | 運転者が乗車した時に実行するイベント。 / 表示条件: `useEventOnDriverGetOn` がオンのとき |
| Use Event On Driver Get Off | `useEventOnDriverGetOff` | `bool` | – | 運転者が降車した時にイベントを呼ぶかどうか。 |
| Event On Driver Get Off | `eventOnDriverGetOff` | `eventParameters.eventToCallWithGameObject` | – | 運転者が降車した時に実行するイベント。 / 表示条件: `useEventOnDriverGetOff` がオンのとき |
| Send Players Enter Exit Trigger To Event | `sendPlayersEnterExitTriggerToEvent` | `bool` | – | 乗降トリガーへ入退場したプレイヤーをイベントへ渡すかどうか。 |
| Event To Send Players Enter Trigger To Event | `eventToSendPlayersEnterTriggerToEvent` | `eventParameters.eventToCallWithGameObject` | – | トリガー進入時にプレイヤーを引数として呼ぶイベント。 / 表示条件: `sendPlayersEnterExitTriggerToEvent` がオンのとき |
| Event To Send Players Exit Trigger To Event | `eventToSendPlayersExitTriggerToEvent` | `eventParameters.eventToCallWithGameObject` | – | トリガー退出時にプレイヤーを引数として呼ぶイベント。 / 表示条件: `sendPlayersEnterExitTriggerToEvent` がオンのとき |

### Remote Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Events On Passengers | `useRemoteEventsOnPassengers` | `bool` | – | 乗降時に乗員のリモートイベントを呼ぶかどうか。 |

### Vehicle Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Action Manager | `actionManager` | `inputActionManager` | – | 車両の入力を管理する`inputActionManager`への参照。 / 表示条件: `showVehicleElements` がオンのとき |
| Vehicle Camera Manager | `vehicleCameraManager` | `vehicleCameraController` | – | 車両カメラを制御する`vehicleCameraController`への参照。 / 表示条件: `showVehicleElements` がオンのとき |
| HUD Manager | `HUDManager` | `vehicleHUDManager` | – | 車両の体力や速度を表示する`vehicleHUDManager`への参照。 / 表示条件: `showVehicleElements` がオンのとき |
| Current Vehicle Weapon System | `currentVehicleWeaponSystem` | `vehicleWeaponSystem` | – | 車両に搭載された武器システムへの参照。 / 表示条件: `showVehicleElements` がオンのとき |
| Vehicle Gravity Manager | `vehicleGravityManager` | `vehicleGravityControl` | – | 車両の重力方向を制御するコンポーネントへの参照。 / 表示条件: `showVehicleElements` がオンのとき |
| Main Collider | `mainCollider` | `Collider` | – | 車両のメインコライダー。破壊時や遠隔操作時に無効化される。 / 表示条件: `showVehicleElements` がオンのとき |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | シーンビューに座席位置などのギズモを表示するかどうか。 |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | – | ギズモのラベルや線に使う色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Radius | `gizmoRadius` | `float` | 0.1f | ギズモ内で表示する球の半径の大きさ。 / 表示条件: `showGizmo` がオンのとき |
| Use Handle For Vertex | `useHandleForVertex` | `bool` | – | 各ポイントをフリーハンドルで移動できるようにするかどうか。 / 表示条件: `showGizmo` がオンのとき |
| Handle Radius | `handleRadius` | `float` | – | フリーハンドルとして表示する球の半径。 / 表示条件: `showGizmo.boolValue && useHandleForVertex.boolValue` |
| Handle Gizmo Color | `handleGizmoColor` | `Color` | – | フリーハンドルの表示に使う色。 / 表示条件: `showGizmo.boolValue && useHandleForVertex.boolValue` |
| Use Position Handle | `usePositionHandle` | `bool` | true | 位置ハンドル（矢印）で移動できるようにするかどうか。 / 表示条件: `showGizmo` がオンのとき |
| Show Debug Print | `showDebugPrint` | `bool` | – | 乗降や障害物判定などのデバッグログを出力するかどうか。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `IKVehiclePassengersList` | `List<IKDrivingInformation>` | new List<IKDrivingInformation> () | – |
| `controlsMenuOpened` | `bool` | – | – |
| `showSettings` | `bool` | – | – |
| `isBeingDrivenRemotely` | `bool` | – | – |
| `remoteEventsOnPreviuosDriverOnStealList` | `List<string>` | new List<string> () | – |
| `remoteEventNameListGetOn` | `List<string>` | new List<string> () | – |
| `remoteEventNameListGetOff` | `List<string>` | new List<string> () | – |
| `passengerGameObjectList` | `List<GameObject>` | new List<GameObject> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateSeatsStates()` | 乗車中の各席で角方向を減衰させ、ステアリング入力値をHUDから更新する。 |
| `setNewAngularDirection(Vector3 newValue)` | `extraAngularDirectioAmount`を掛けた値を新しい角方向として保持する。 |
| `setCollisionForceDirectionToPassengers(Vector3 forceDirection)` | 衝突力を各乗員の`currentSeatShake`に設定してIKを揺らす。 |
| `setPassengerFirstPersonState(bool state, GameObject passengerToCheck)` | 対象乗員の`currentlyOnFirstPerson`を設定するだけ。 |
| `setPlayerToStartGameOnThisVehicle(GameObject newPlayer)` | 開始時にこの車両へ乗せるプレイヤーを設定し、判定済みフラグを戻す。 |
| `setDriverExternally(GameObject currentDriver)` | 指定キャラを運転席に乗せるため、使用デバイス（AIは専用処理）経由で車両を使わせる。 |
| `setPassengerExternally(GameObject currentDriver)` | `playerIsAlwaysDriver`を一時的にfalseにして運転席以外へ乗車させる。 |
| `destroyVehicle()` | カメラと車両を自身の子に戻してから、このゲームオブジェクトを破棄する。 |
| `fixDestroyedVehicle()` | 破壊フラグ`vehicleDestroyed`をfalseにするだけ。 |
| `setMainColliderEnabledState(bool state)` | `mainCollider`の有効状態を設定するだけ。 |
| `disableVehicle()` | 破壊時に搭乗者の排出・爆発・武器とカメラの停止・デバイス一覧からの除去を行う。 |
| `ejectVehiclePassengersOnSelfDestruct(float ejectPassengerFoce)` | 自爆時用に、指定した力を渡して`ejectVehiclePassengers`を呼ぶだけ。 |
| `ejectVehiclePassengers(bool ejectPassenger, float ejectForce)` | 全乗員を降ろし、指定時は力を加えて射出、非表示ならメッシュを戻す。 |
| `checkIgnorPassengersCollidersState(List<passengerComponents> auxPassengerComponentsList)` | 乗員コライダーとの衝突を一時的に無視するコルーチンを開始する。 |
| `setActivateFreeFloatingModeOnEjectEnabledState(bool state)` | `activateFreeFloatingModeOnEjectEnabled`を設定するだけ。 |
| `startOrStopVehicle(GameObject currentPassenger, Transform passengerParent, Vector3 normal, Vector3 nextPlayerPos)` | 乗降処理の本体で、席の空きを反転しイベント実行後にアクションまたは直接配置へ進む。 |
| `stopEnterExitActionSystemOnPassengerCoroutine(Coroutine passengerCoroutine)` | コルーチンがnullでなければ停止するだけ。 |
| `setPlayerCameraDirectionWithVehicleCameraDirection(passengerComponents currentPassengerComponents)` | 車両カメラの回転とピボットをプレイヤーカメラへコピーし、視線角度も設定する。 |
| `checkIfNotDrivenRemotely(bool currentPassengerIsPlayer)` | 遠隔操作可能かつプレイヤー本人のときだけfalseを返す判定。 |
| `setCanBeDrivenRemotelyState(bool state)` | `canBeDrivenRemotely`を設定するだけ。 |
| `getCanBeDrivenRemotelyValue()` | `canBeDrivenRemotely`を返すだけ。 |
| `enableOrDisablePlayerVisibleInVehicle(bool state, passengerComponents currentPassengerComponents)` | 一人称以外ではメッシュと武器表示を、一人称ではキャラメッシュを切り替える。 |
| `checkCameraTranslationByPlayerCamera(bool state, playerCamera playerCameraManager)` | 既存の移動を止め、プレイヤーカメラ用の移動コルーチンを開始して保持する。 |
| `stopCameraTranslationByPlayerCamera(playerCamera playerCameraManager)` | プレイヤーカメラに保持された移動コルーチンを停止する。 |
| `checkCameraTranslation(bool state, passengerComponents currentPassengerComponents)` | 既存の移動コルーチンを止め、乗員用のカメラ移動コルーチンを開始して保持する。 |
| `stopCheckCameraTranslation(Coroutine moveCameraCoroutine)` | コルーチンがnullでなければ停止するだけ。 |
| `setPlayerCameraParentAndPosition(Transform mainCameraTransform, playerCamera playerCameraManager)` | 車両カメラを運転状態にし、メインカメラを車両カメラの子にして移動を開始する。 |
| `checkDisableShowControlsMenu()` | 操作説明メニューが開いていれば閉じる。 |
| `inputOpenOrCloseControlsMenu(bool state)` | ポーズメニューが開いていなければ、操作説明メニューの開閉を呼ぶ。 |
| `openOrCloseControlsMenu(bool state)` | メニュー開閉に合わせカーソル・カメラ・武器・タッチ操作・HUDを一括で切り替える。 |
| `setUnlockCursorState(bool state)` | カーソル固定を切り替えカメラと武器を停止し、変化がなければfalseを返す。 |
| `setCameraAndWeaponsPauseState(bool state)` | 車両カメラの一時停止と武器停止を同じ状態に設定する。 |
| `pauseOrPlayVehicleCamera(bool state)` | `vehicleCameraManager`のカメラ一時停止を呼ぶだけ。 |
| `getcurrentDriver()` | 運転席の乗員を返し、いなければ最初の乗員、それもいなければnullを返す。 |
| `getLastDriver()` | 最後に運転席にいた`currentPassengerDriverComponents`の乗員を返す。 |
| `currentDriverIsAI()` | 運転席にAI乗員が座っていればtrueを返す。 |
| `getOffFromVehicleToDriverAI()` | 運転手がAIなら、そのAIを車両から降ろす処理を呼ぶ。 |
| `getHUDManager()` | `HUDManager`を返すだけ。 |
| `getPassengerGetOffPosition(GameObject currentPassenger)` | 席設定と障害物判定から降車位置を求め、乗車直後は`Vector3.zero`、不可なら`-Vector3.one`を返す。 |
| `getGetOffPosition(IKDrivingInformation passengerInfo)` | 席の設定に応じて右または左の降車位置を返す。 |
| `getClosestSeatToPassengerIndex(GameObject currentPassenger)` | 運転可否を考慮し、空いている席のうち最も近い席の番号を返す。 |
| `getClosestSeatToPassengerIndexWithoutStateCheck(GameObject currentPassenger)` | 空き状態を無視して最も近い席の番号を返す。 |
| `getDriverSeatPassengerIndex()` | 運転席の番号を返し、見つからなければ-1を返す。 |
| `getIKVehiclePassengerInfo(GameObject passenger)` | 指定乗員に対応する`IKDrivingInformation`を返す。 |
| `setPassengerInfo(IKDrivingInformation passengerInfo, GameObject passenger)` | 未登録なら乗員リストと席に登録し、乗車処理用にtrueを返す。 |
| `setPassengerComponents(GameObject currentPassenger)` | プレイヤー各コンポーネントを取得して乗員情報を作り、状態IDを0に戻して追加する。 |
| `removePassengerInfo(IKDrivingInformation passengerInfo)` | 乗員情報を削除し、保存した状態・アイドル・ストレイフIDを復元する。 |
| `addPassenger()` | 「New Seat」という新しい席データを追加し、シーンを更新する。 |
| `getPassengerGameObjectList()` | 乗員のゲームオブジェクト一覧を返すだけ。 |
| `checkTriggerInfo(Collider col, bool isEnter)` | トリガーの出入りで使用デバイス一覧と乗員一覧を更新し、イベントを送る。 |
| `getPassengersInsideTrigger()` | トリガー内の乗員一覧を返すだけ。 |
| `isVehicleFull()` | 乗員数と席数が同じならtrueを返す。 |
| `arePassengerSeatsFull()` | 運転席以外に空席がなければtrueを返す。 |
| `isVehicleEmpty()` | 乗員がいない、または乗車状態でなければtrueを返す。 |
| `getVehicleSeatsAmount()` | 席数を返すだけ。 |
| `getMainCollider()` | `mainCollider`を返すだけ。 |
| `checkActivateActionScreen(bool state, playerController playerControllerManager)` | 設定が有効なら、プレイヤー入力のアクション画面表示を切り替える。 |
| `getOffFromVehicle()` | 運転中なら、運転手の使用デバイス経由で降車を実行する。 |
| `isVehicleBeingDriven()` | HUDに問い合わせて運転中かどうかを返す。 |
| `isForcingPassengersToGetOffOnVehicleDestroyedActive()` | 破壊時の強制降車処理中かどうかを返す。 |
| `checkStateOnDestroyVehicleExternally()` | 強制降車の設定が有効なら、全乗員を降ろす。 |
| `forceAllPassengersToGetOffFromVehicle()` | 強制降車フラグを立てて力を0に全乗員を降ろし、フラグを戻す。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とシーンのダーティ更新を行う。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`getCustomVehicleTransform()`, `getVehicleCameraGameObject()`, `getVehicleGameObject()`, `getVehicleGravityControl()`, `setEjectPlayerWhenDestroyedState(bool state)`, `setPlayerVisibleInVehicleState(bool state)`, `setResetCameraRotationWhenGetOnState(bool state)`, `setTriggerToDetect(Collider newCollider)`

</details>

## 内部型

- `IKDrivingInformation`（class）
- `IKDrivingPositions`（class）
- `IKDrivingKneePositions`（class）
- `seatInfo`（class）
- `passengerComponents`（class）
