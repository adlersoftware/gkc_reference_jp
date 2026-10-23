# overrideElementControlSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Override System/overrideElementControlSystem.cs:7`

**概要**: プレイヤーが他のキャラクターや乗り物、Rigidbodyを操作(オーバーライド)する制御系。対象検出、カメラ移動、プレイヤーの停止、開始・終了処理を担う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Raycast Distance | `raycastDistance` | `float` | – | – |
| Raycast Radius | `raycastRadius` | `float` | 0.3f | – |
| Use Tags To Check | `useTagsToCheck` | `bool` | – | – |
| Allowed Tags To Control | `allowedTagsToControl` | `List<string>` | new List<string> () | – |
| Hide Player While Controlling | `hidePlayerWhileControlling` | `bool` | – | – |
| Reapear Close To Controller Object | `reapearCloseToControllerObject` | `bool` | – | – |
| Disable Map On Override | `disableMapOnOverride` | `bool` | – | – |
| Use Smooth Transition | `useSmoothTransition` | `bool` | – | – |
| Launch Camera Speed | `launchCameraSpeed` | `float` | – | – |
| Back Camera Speed | `backCameraSpeed` | `float` | – | – |
| Camera Rotation Speed | `cameraRotationSpeed` | `float` | 2 | – |
| Reapear Close Camera Speed | `reapearCloseCameraSpeed` | `float` | – | – |
| Stop Override Touch Button Name | `stopOverrideTouchButtonName` | `string` | "Activate Devices" | – |
| Check For External Objects To Drive Or Ride Enabled | `checkForExternalObjectsToDriveOrRideEnabled` | `bool` | true | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Force On Reapear | `addForceOnReapear` | `bool` | – | – |
| Force On Reapear | `forceOnReapear` | `float` | – | – |
| Force Mode On Reapear | `forceModeOnReapear` | `ForceMode` | ForceMode.Force | – |

### Start Game Controlling Character Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Start Controlling Character | `startControllingCharacter` | `bool` | – | – |
| Use Smooth Transition At Start | `useSmoothTransitionAtStart` | `bool` | – | – |
| Character To Control At Start | `characterToControlAtStart` | `GameObject` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On State Change | `useEventsOnStateChange` | `bool` | – | – |
| Even On State Enabled | `evenOnStateEnabled` | `UnityEvent` | – | – |
| Event On State Disabled | `eventOnStateDisabled` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Using Override | `usingOverride` | `bool` | – | – |
| Launching Camera | `launchingCamera` | `bool` | – | – |
| Controlling Vehicle | `controllingVehicle` | `bool` | – | – |
| Is Default Controller | `isDefaultController` | `bool` | – | – |
| Controller Found On Mesh | `controllerFoundOnMesh` | `bool` | – | – |
| Player Components Paused | `playerComponentsPaused` | `bool` | – | – |
| Temporal Object List | `temporalObjectList` | `List<GameObject>` | new List<GameObject> () | – |
| Input Stop Override Control Paused | `inputStopOverrideControlPaused` | `bool` | – | – |
| Current Character | `currentCharacter` | `GameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Raycast Position | `raycastPosition` | `Transform` | – | – |
| Default Override Controller | `defaultOverrideController` | `GameObject` | – | – |
| Player Camera Transform | `playerCameraTransform` | `Transform` | – | – |
| Main Camera | `mainCamera` | `Transform` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Devices Manager | `devicesManager` | `usingDevicesSystem` | – | – |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | – |
| Head Bo Manager | `headBoManager` | `headBob` | – | – |
| States Manager | `statesManager` | `playerStatesManager` | – | – |
| Map System Manager | `mapSystemManager` | `mapSystem` | – | – |
| Main Remote Event System | `mainRemoteEventSystem` | `remoteEventSystem` | – | – |
| Input | `input` | `inputManager` | – | – |
| Main Player HUD Manager | `mainPlayerHUDManager` | `playerHUDManager` | – | – |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | – |
| Main Melee Weapons Grabbed Manager | `mainMeleeWeaponsGrabbedManager` | `meleeWeaponsGrabbedManager` | – | – |
| Step Manager | `stepManager` | `footStepManager` | – | – |
| Main Player Abilities System | `mainPlayerAbilitiesSystem` | `playerAbilitiesSystem` | – | – |
| Main Player Transform | `mainPlayerTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopCurrentOverrideControl()` | オーバーライド中のみ、アビリティ由来なら解除処理、乗り物なら降車、それ以外なら`stopOverride`を実行する。 |
| `checkElementToControl()` | `raycastPosition`を引数に持つオーバーロードを呼ぶだけ。 |
| `checkElementToControl(Transform newRaycastPosition)` | 指定位置からレイキャストし、当たった範囲内のコライダーを順に試して操作対象の確保を試みる。 |
| `setCheckForExternalObjectsToDriveOrRideEnabledState(bool state)` | `checkForExternalObjectsToDriveOrRideEnabled`を設定するだけ。 |
| `isCheckForExternalObjectsToDriveOrRideEnabled()` | `checkForExternalObjectsToDriveOrRideEnabled`を返すだけ。 |
| `overrideElementControl(GameObject objectToControl)` | 対象が操作可能か判定して各コンポーネントを用意し、プレイヤーを停止してカメラを移動させ、オーバーライドを開始する。 |
| `resetValues()` | `isDefaultController`と`controllerFoundOnMesh`をfalseにするだけ。 |
| `launchCameraToTarget(bool launchingToCharacter)` | 既存のカメラ移動コルーチンを止め、対象へ、またはプレイヤーへカメラを移動するコルーチンを開始する。 |
| `setControllerRigidbodyVelocity(bool state)` | `state`に応じ操作前後のRigidbody速度を取得して、速度変数に保存するだけ。 |
| `startOverride()` | オーバーライド中フラグを立てて状態変更イベントを発火し、乗り物なら運転を、それ以外なら入力管理の制御開始を実行する。 |
| `pauseOrPlayPlayerComponents(bool state)` | プレイヤーの制御・カメラ・HUD・ヘッドボブ・武器などを`state`に応じて停止または再開し、使用デバイス状態も更新する。 |
| `checkCharacterMesh(bool state)` | 一人称視点や`hidePlayerWhileControlling`に応じて、プレイヤーのメッシュ・コライダー・武器表示を切り替える。 |
| `stopOverride()` | 乗り物以外ならキャラクターを再出現させてカメラを戻し、内部状態をリセットして状態変更イベントと停止ボタンを更新する。 |
| `reapearCharacter()` | 再出現設定が有効なら、対象やカメラ位置を基にプレイヤーとカメラを再配置し、必要なら力を加える。 |
| `setDeadState()` | 本体が空で何もしない。 |
| `checkEventsOnStateChange(bool state)` | `useEventsOnStateChange`が有効なら、`state`に応じて有効・無効イベントを発火する。 |
| `enableOrDisableStopOverridButton(bool state)` | タッチ操作時のみ、入力マネージャー経由で停止用タッチボタンを`state`に応じて有効または無効にする。 |
| `setCurrentOverrideActivatedByAbilityState(bool state)` | `currentOverrideActivatedByAbility`を設定するだけ。 |
| `setCurrentAbilityNameUsedToActivateOverride(string abilityName)` | `abilityNameUsedToActivateOverride`を設定するだけ。 |
| `addNewTemporalObject(GameObject newObject)` | 未登録なら`newObject`を一時オブジェクトリストへ追加するだけ。 |
| `removeNewTemporalObject(GameObject newObject)` | 登録済みなら`newObject`を一時オブジェクトリストから削除するだけ。 |
| `checkIfTemporalObjectOnList(GameObject newObject)` | `newObject`が一時オブジェクトリストに含まれるか返すだけ。 |
| `setInputStopOverrideControlPausedState(bool state)` | `inputStopOverrideControlPaused`を設定するだけ。 |
| `inputStopOverrideControl()` | 停止入力が無効化されておらずオーバーライド中なら、`stopCurrentOverrideControl`を呼ぶ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `evenOnStateEnabled` | `UnityEvent` | – |
| `eventOnStateDisabled` | `UnityEvent` | – |
