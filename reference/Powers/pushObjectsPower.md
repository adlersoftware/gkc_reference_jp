# pushObjectsPower

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/New Powers Behaviors/pushObjectsPower.cs:6`

**概要**: 周囲のオブジェクトを中心から押し出すパワー。範囲内の`Rigidbody`へ力を加え、ダメージや遠隔イベントも任意で行う。

**公式ドキュメント抜粋**（[Tutorial - Add Action System By Input](../../docs/quick-start/tutorials/tutorial-add-action-system-by-input.md)）

> Youtube Tutorial Add a new action on the input and configure the event to activate the animation action by going clicking on the root of the prefab (Player and Game Management), then the Input Manager component. Scroll down to the section Multi-Input List and open the Multi Axes List menu. Then open Player Controller in the Multi-Input List and select Add Action to add a new one. In this tutorial, we’ll be creating the action, Simple Kick. You can also put a Keyboard and/or Joystick input to activate the action here. Next, navigate to the Player Controller game object on the player character and scroll down to the Player Input Manager. Then scroll down to Multi Axes List and select the Player Controller section as we did on the Player and Game Management component. Click Add Action as before, except now on the Axe dropdown, you will see the Simple Kick Action we made. Select that. Set th…

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Power Enabled | `powerEnabled` | `bool` | true | – |
| Layer | `layer` | `LayerMask` | – | – |
| Push Objects From Center Position | `pushObjectsFromCenterPosition` | `bool` | – | – |
| Push Objects From Player Forward Direction | `pushObjectsFromPlayerForwardDirection` | `bool` | – | – |
| Use Max Angle With Camera Face Direction | `useMaxAngleWithCameraFaceDirection` | `bool` | – | – |
| Max Angle With Camera Face Direction | `maxAngleWithCameraFaceDirection` | `float` | – | – |
| Use Raycast To Push Objects | `useRaycastToPushObjects` | `bool` | – | – |
| Layer For Raycast Surface Detection | `layerForRaycastSurfaceDetection` | `LayerMask` | – | – |
| Use Max Angle With Player Face Direction | `useMaxAngleWithPlayerFaceDirection` | `bool` | – | – |
| Max Angle With Player Face Direction | `maxAngleWithPlayerFaceDirection` | `float` | – | – |
| Max Raycast Distance | `maxRaycastDistance` | `float` | – | – |
| Ignore Tag List | `ignoreTagList` | `List<string>` | new List<string> () | – |
| Use Message To Push Characters Found | `useMessageToPushCharactersFound` | `bool` | true | – |
| Message Name To Send | `messageNameToSend` | `string` | "pushCharacter" | – |

### Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Apply Damage On Found Objects | `applyDamageOnFoundObjects` | `bool` | – | – |
| Damage To Apply | `damageToApply` | `float` | – | – |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Can Activate Reaction System Temporally | `canActivateReactionSystemTemporally` | `bool` | – | – |
| Damage Reaction ID | `damageReactionID` | `int` | -1 | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |

### Force Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Force To Apply | `forceToApply` | `float` | 4000 | – |
| Force Mode | `forceMode` | `ForceMode` | – | – |
| Can Apply Force To Vehicles | `canApplyForceToVehicles` | `bool` | true | – |
| Apply Force To Vehicles Multiplier | `applyForceToVehiclesMultiplier` | `float` | 0.2f | – |
| Apply Force To Found Objects Only Once | `applyForceToFoundObjectsOnlyOnce` | `bool` | – | – |
| Check Ragdolls Detected | `checkRagdollsDetected` | `bool` | – | – |
| Ragdoll Multiplier Force | `ragdollMultiplierForce` | `float` | 1 | – |

### Others Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Push Center Distance | `useCustomPushCenterDistance` | `bool` | – | – |
| Push Center Distance | `pushCenterDistance` | `float` | – | – |
| Search For Objects On Update | `searchForObjectsOnUpdate` | `bool` | – | – |
| Check If Object In Front Of Player | `checkIfObjectInFrontOfPlayer` | `bool` | – | – |

### Magnetize Objects To AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Magnetize Object To Close AI Enemies | `magnetizeObjectToCloseAIEnemies` | `bool` | – | – |
| Mount Point Name To Magnetize | `mountPointNameToMagnetize` | `string` | – | – |
| Magnetize Force Amount | `magnetizeForceAmount` | `float` | – | – |
| Max Distance To Magnetize | `maxDistanceToMagnetize` | `float` | – | – |
| Magnetize Only Lock On AI | `magnetizeOnlyLockOnAI` | `bool` | – | – |
| Add Launched Object Component To Detected Objects | `addLaunchedObjectComponentToDetectedObjects` | `bool` | – | – |
| Use Events On Found Object To Magnetize Result | `useEventsOnFoundObjectToMagnetizeResult` | `bool` | – | – |
| Event On Found Object To Magnetize | `eventOnFoundObjectToMagnetize` | `UnityEvent` | – | – |
| Event On Not Found Object To Magnetize | `eventOnNotFoundObjectToMagnetize` | `UnityEvent` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remote Event Name List | `remoteEventNameList` | `List<string>` | new List<string> () | – |
| Call Remote Events Before Applying Force | `callRemoteEventsBeforeApplyingForce` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Use Of Power Paused | `useOfPowerPaused` | `bool` | – | – |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Update Coroutine Active | `updateCoroutineActive` | `bool` | – | – |
| Vehicles Rigidbody Found List | `vehiclesRigidbodyFoundList` | `List<Rigidbody>` | new List<Rigidbody> () | – |
| Game Objects Found List | `gameObjectsFoundList` | `List<GameObject>` | new List<GameObject> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Weapon System | `mainPlayerWeaponSystem` | `playerWeaponSystem` | – | – |
| Player Game Object | `playerGameObject` | `GameObject` | – | – |
| Center Position | `centerPosition` | `Transform` | – | – |
| Powers Manager | `powersManager` | `otherPowers` | – | – |
| Push Objects Center | `pushObjectsCenter` | `Transform` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main AI Around Manager | `mainAIAroundManager` | `AIAroundManager` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 更新コルーチンが動作中なら停止し、稼働フラグを下ろす。 |
| `activatePowerWithUpdate()` | 毎フレーム探索の設定なら更新コルーチンを開始し、そうでなければ1回だけ発動する。 |
| `deactivatePowerWithUpdate()` | 毎フレーム探索の設定かつ有効なら、更新コルーチンを停止する。 |
| `activatePower()` | 中心の周囲のコライダーを取得し、対象ごとに力を計算して弾き飛ばす。 |
| `checkObjectToApplyForce(GameObject currentObject)` | タグや前方判定を通過した対象へメッセージ・ダメージ・力を与え、乗り物リストや遠隔イベントも処理する。 |
| `setPowerEnabledState(bool state)` | 有効フラグを設定し、初期化とリストのクリア、更新コルーチンの開始/停止を行う。 |
| `setPowerEnabledStateOneFrame()` | 1フレームだけ有効化して発動し、すぐ無効に戻す。 |
| `cleanGameObjectFoundList()` | 検出済みオブジェクトのリストを空にするだけ。 |
| `checkRemoteEvent(GameObject objectToCheck)` | 遠隔イベント設定が有効なら、対象の`remoteEventSystem`へ登録済みの名前を送る。 |
| `setUseRemoteEventOnObjectsFoundState(bool state)` | 検出対象へ遠隔イベントを送るかどうかのフラグを設定するだけ。 |
| `setUseMessageToPushCharactersFoundState(bool state)` | 検出したキャラへ押し出しメッセージを送るかどうかのフラグを設定するだけ。 |
| `setUseOfPowerPausedState(bool state)` | パワー使用を一時停止するフラグを設定するだけ。 |
| `setNewPushCenterDistance(float newValue)` | 中心から探索する距離`pushCenterDistance`を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnFoundObjectToMagnetize` | `UnityEvent` | – |
| `eventOnNotFoundObjectToMagnetize` | `UnityEvent` | – |
