# changePlayerStateOnTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Event System/changePlayerStateOnTriggerSystem.cs:6`

**概要**: トリガーや関数呼び出しを起点に、対象プレイヤーのモード・カメラ・武器・重力・移動などの状態をまとめて変更するコンポーネント。プレイヤーは手動指定またはシーン検索で取得する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Player States Enabled | `changePlayerStatesEnabled` | `bool` | true | – |
| Disable Trigger After Enter | `disableTriggerAfterEnter` | `bool` | – | – |

### Player Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Player Mode | `changePlayerMode` | `bool` | – | – |
| Player Mode Name | `playerModeName` | `string` | – | – |

### Jump Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Jump Enabled State | `setJumpEnabledState` | `bool` | – | – |
| Jump Enabled State | `jumpEnabledState` | `bool` | – | – |
| Set Double Jump State | `setDoubleJumpState` | `bool` | – | – |
| Double Jump State | `doubleJumpState` | `bool` | – | – |

### Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Camera View State | `setCameraViewState` | `bool` | – | – |
| Set Camera To First Person | `setCameraToFirstPerson` | `bool` | – | – |
| Set New Default Third Person Camera State | `setNewDefaultThirdPersonCameraState` | `bool` | – | – |
| New Default Third Person Camera State Name | `newDefaultThirdPersonCameraStateName` | `string` | – | – |
| Set Action To Change Between Views State | `setActionToChangeBetweenViewsState` | `bool` | – | – |
| Action To Change Between Views State | `actionToChangeBetweenViewsState` | `bool` | – | – |
| Set Camera State Name | `setCameraStateName` | `bool` | – | – |
| Camera State Name | `cameraStateName` | `string` | – | – |
| Reset Camera Rotation State | `resetCameraRotationState` | `bool` | – | – |

### Input Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Player Input Action State | `setPlayerInputActionState` | `bool` | – | – |
| Player Input Action State | `playerInputActionState` | `bool` | – | – |
| Multi Axes Input Name | `multiAxesInputName` | `string` | – | – |
| Axes Input Name | `axesInputName` | `string` | – | – |
| Set Ignore Check Input Active State | `setIgnoreCheckInputActiveState` | `bool` | – | – |
| Ignore Check Input Active State | `ignoreCheckInputActiveState` | `bool` | – | – |
| Multi Axes Input Name List | `multiAxesInputNameList` | `List<string>` | – | – |
| Set Pause All Input Actions State | `setPauseAllInputActionsState` | `bool` | – | – |
| Pause All Input Action State | `pauseAllInputActionState` | `bool` | – | – |
| Set Pause Movement Axis Input State | `setPauseMovementAxisInputState` | `bool` | – | – |
| Pause Movement Axis Input State | `pauseMovementAxisInputState` | `bool` | – | – |
| Set Pause Camera Axis Input State | `setPauseCameraAxisInputState` | `bool` | – | – |
| Pause Camera Axis Input State | `pauseCameraAxisInputState` | `bool` | – | – |

### Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Action Active State | `setActionActiveState` | `bool` | – | – |
| Action Active State | `actionActiveState` | `bool` | – | – |
| Action Id | `actionId` | `int` | -1 | – |
| Enable Animator Layer On Action | `enableAnimatorLayerOnAction` | `bool` | – | – |
| Animator Layer To Enable Name | `animatorLayerToEnableName` | `string` | – | – |

### Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Draw Weapon | `drawWeapon` | `bool` | – | – |
| Draw Current Weapon | `drawCurrentWeapon` | `bool` | – | – |
| Use Quick Draw Weapon | `useQuickDrawWeapon` | `bool` | – | – |
| Draw Certain Weapon | `drawCertainWeapon` | `bool` | – | – |
| Weapon Name To Draw | `weaponNameToDraw` | `string` | – | – |
| Is Fire Weapon | `isFireWeapon` | `bool` | – | – |
| Equip Weapon If Not Equipped | `equipWeaponIfNotEquipped` | `bool` | – | – |
| Keep Weapon | `keepWeapon` | `bool` | – | – |
| Use Quick Keep Weapon | `useQuickKeepWeapon` | `bool` | – | – |

### Fire Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Carry Weapon On Lower Position State | `setCarryWeaponOnLowerPositionState` | `bool` | – | – |
| Carry Weapon On Lower Position State | `carryWeaponOnLowerPositionState` | `bool` | – | – |
| Set Can Fire Weapons State | `setCanFireWeaponsState` | `bool` | – | – |
| Can Fire Weapons State | `canFireWeaponsState` | `bool` | – | – |

### Gravity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Gravity Power State | `setGravityPowerState` | `bool` | – | – |
| Gravity Power State | `gravityPowerState` | `bool` | – | – |
| Set Zero Gravity Mode State | `setZeroGravityModeState` | `bool` | – | – |
| Zero Gravity Mode State | `zeroGravityModeState` | `bool` | – | – |
| Set Gravity Direction | `setGravityDirection` | `bool` | – | – |
| Set Gravity Manager | `setGravityManager` | `setGravity` | – | – |

### Free Floating Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Free Floating Mode State | `setFreeFloatingModeState` | `bool` | – | – |
| Free Floating Mode State | `freeFloatingModeState` | `bool` | – | – |

### Look At Target Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Look At Point State | `setLookAtPointState` | `bool` | – | – |
| Look At Point State | `lookAtPointState` | `bool` | – | – |
| Point To Look | `pointToLook` | `Transform` | – | – |
| Use Duration To Look At Point | `useDurationToLookAtPoint` | `bool` | – | – |
| Duration To Look At Point | `durationToLookAtPoint` | `float` | – | – |
| Enable Look At Point State After Duration | `enableLookAtPointStateAfterDuration` | `bool` | – | – |
| Set Look At Point Speed | `setLookAtPointSpeed` | `bool` | – | – |
| Look At Point Speed | `lookAtPointSpeed` | `float` | – | – |
| Set Max Distance To Find Target | `setMaxDistanceToFindTarget` | `bool` | – | – |
| Max Distance To Find Target | `maxDistanceToFindTarget` | `float` | – | – |
| Set Use Look Target Icon State | `setUseLookTargetIconState` | `bool` | – | – |
| Use Look Target Icon State | `useLookTargetIconState` | `bool` | – | – |
| Set Original Use Look Target Icon State | `setOriginalUseLookTargetIconState` | `bool` | – | – |

### Camera Zoom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Camera Zoom State | `setCameraZoomState` | `bool` | – | – |
| Camera Zoom State | `cameraZoomState` | `bool` | – | – |
| Use Camera Zoom Duration | `useCameraZoomDuration` | `bool` | – | – |
| Camera Zoom Duration | `cameraZoomDuration` | `float` | – | – |
| Enable Camera Zoon Input After Duration | `enableCameraZoonInputAfterDuration` | `bool` | – | – |

### Transparent Surface Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Transparent Surface Detection State | `setTransparentSurfaceDetectionState` | `bool` | – | – |
| Transparent Surface Detection State | `transparentSurfaceDetectionState` | `bool` | – | – |

### Movement Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Walk Speed Value | `setWalkSpeedValue` | `bool` | – | – |
| Walk Speed Value | `walkSpeedValue` | `float` | – | – |
| Set Original Walk Speed Value | `setOriginalWalkSpeedValue` | `bool` | – | – |
| Set Increase Walk Speed Value | `setIncreaseWalkSpeedValue` | `bool` | – | – |
| Increase Walk Speed Value | `increaseWalkSpeedValue` | `float` | – | – |
| Set Increase Walk Speed Enabled | `setIncreaseWalkSpeedEnabled` | `bool` | – | – |
| Increase Walk Speed Enabled | `increaseWalkSpeedEnabled` | `bool` | – | – |
| Set Original Increase Walk Speed Enabled Value | `setOriginalIncreaseWalkSpeedEnabledValue` | `bool` | – | – |
| Set Player Status ID | `setPlayerStatusID` | `bool` | – | – |
| Player Status ID | `playerStatusID` | `int` | – | – |
| Set Original Player Status ID | `setOriginalPlayerStatusID` | `bool` | – | – |
| Set Crouch State | `setCrouchState` | `bool` | – | – |
| Crouch State To Activate | `crouchStateToActivate` | `bool` | – | – |

### Sprint Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Sprint Enabled State | `setSprintEnabledState` | `bool` | – | – |
| Sprint Enabled State | `sprintEnabledState` | `bool` | – | – |
| Set Original Sprint Enabled State | `setOriginalSprintEnabledState` | `bool` | – | – |

### Stairs Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Stairs Adherence Value | `setStairsAdherenceValue` | `bool` | – | – |
| Stairs Max Value | `stairsMaxValue` | `float` | 0.25f | – |
| Stairs Min Value | `stairsMinValue` | `float` | 0.2f | – |
| Stairs Ground Adherence | `stairsGroundAdherence` | `float` | 8 | – |

### Root Motion Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Root Motion Active | `changeRootMotionActive` | `bool` | – | – |
| Use Root Motion Active | `useRootMotionActive` | `bool` | true | – |

### Ragdoll Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Ragdoll State | `activateRagdollState` | `bool` | – | – |
| Ragdoll Push Direction | `ragdollPushDirection` | `Transform` | – | – |
| Ragdoll Push Force Amount | `ragdollPushForceAmount` | `float` | – | – |

### Ability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Ability | `setAbility` | `bool` | – | – |
| Ability Name To Set | `abilityNameToSet` | `string` | – | – |
| Use Abilities List To Enable | `useAbilitiesListToEnable` | `bool` | – | – |
| Abilities List To Enable | `abilitiesListToEnable` | `List<string>` | new List<string> () | – |
| Use Abilities List To Disable | `useAbilitiesListToDisable` | `bool` | – | – |
| Abilities List To Disable | `abilitiesListToDisable` | `List<string>` | new List<string> () | – |

### Powers Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Current Power | `setCurrentPower` | `bool` | – | – |
| Current Power Name | `currentPowerName` | `string` | – | – |

### Map Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Compass Enable Value | `setCompassEnableValue` | `bool` | – | – |
| Compass Enabled Value | `compassEnabledValue` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remove Event Name List | `removeEventNameList` | `List<string>` | new List<string> () | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Trigger | `useEventOnTrigger` | `bool` | – | – |
| Event On Trigger | `eventOnTrigger` | `UnityEvent` | – | – |
| Send Player On Event | `sendPlayerOnEvent` | `bool` | – | – |
| Player Send Event | `playerSendEvent` | `eventParameters.eventToCallWithGameObject` | – | – |

### Player Manual Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Player Manually | `setPlayerManually` | `bool` | – | – |
| Player To Configure | `playerToConfigure` | `GameObject` | – | – |
| Current Player | `currentPlayer` | `GameObject` | – | – |
| Search Player On Scene If Not Assigned | `searchPlayerOnSceneIfNotAssigned` | `bool` | true | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `findPlayerOnScene()` | `searchPlayerOnSceneIfNotAssigned`が有効な時だけ、シーン内のメインプレイヤーを検索して`setCurrentPlayer`に渡す。 |
| `setCurrentPlayer(GameObject player)` | `currentPlayer`に引数の`player`をそのまま代入するだけの薄いセッター。 |
| `changePlayerState()` | 設定済みの状態変更を`currentPlayer`へ一括適用し、`playerSendEvent`と`eventOnTrigger`を呼び、必要なら自身を無効化する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnTrigger` | `UnityEvent` | – |
