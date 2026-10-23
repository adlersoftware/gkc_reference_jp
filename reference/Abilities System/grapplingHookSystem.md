# grapplingHookSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/Custom Abilities/Grappling Hook System/grapplingHookSystem.cs:7`

**概要**: フック先の表面検出、スイング/引き寄せ力の毎フレーム適用、対象剛体の吸引、外部コントローラやカメラ・アニメーションの切り替えを担う。対象オブジェクトの`objectToAttractWithGrapplingHook`設定により吸引方法や遠隔イベントも変化する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grappling Hook Enabled | `grapplingHookEnabled` | `bool` | true | – |
| Max Raycast Distance | `maxRaycastDistance` | `float` | 100 | – |
| Layer To Check Surfaces | `layerToCheckSurfaces` | `LayerMask` | – | – |
| Min Distance To Attract | `minDistanceToAttract` | `float` | 0.5f | – |
| Apply Speed On Hook Stop | `applySpeedOnHookStop` | `bool` | – | – |
| Extra Speed On Hook Stop Multiplier | `extraSpeedOnHookStopMultiplier` | `float` | 1 | – |
| Rotate Player Toward Target Direction | `rotatePlayerTowardTargetDirection` | `bool` | – | – |
| Rotate Player Speed | `rotatePlayerSpeed` | `float` | – | – |
| Min Angle Difference To Rotate Player | `minAngleDifferenceToRotatePlayer` | `float` | – | – |
| Extra Force On Hook Stop Multiplier | `extraForceOnHookStopMultiplier` | `float` | 4 | – |
| Max Force To Apply On Hook Stop | `maxForceToApplyOnHookStop` | `float` | 40 | – |

### Swing Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Swing Forces Active | `useSwingForcesActive` | `bool` | – | – |
| Gravity Force Down | `gravityForceDown` | `float` | 9.8f | – |
| Gravity Force Down Multiplier2 5d | `gravityForceDownMultiplier2_5d` | `float` | 0.8f | – |
| Hook Pull Force On Ground | `hookPullForceOnGround` | `float` | 300 | – |
| Hook Pull Force On Air | `hookPullForceOnAir` | `float` | 300 | – |
| Hook Manual Extend Force | `hookManualExtendForce` | `float` | 130 | – |
| Hook Manual Pull Force | `hookManualPullForce` | `float` | 130 | – |
| Hook Pull Force Multiplier2 5d | `hookPullForceMultiplier2_5d` | `float` | 0.2f | – |
| Hook Pull Force Mode | `hookPullForceMode` | `ForceMode` | – | – |
| Swing Damper | `swingDamper` | `float` | 6 | – |
| Swing Damper2 5d | `swingDamper2_5d` | `float` | 2 | – |
| Air Control Precision Regular Speed | `airControlPrecisionRegularSpeed` | `float` | 3 | – |
| Air Control Precision Increased Speed | `airControlPrecisionIncreasedSpeed` | `float` | 7 | – |
| Duration Auto Pull On Throw Hook On Ground | `durationAutoPullOnThrowHookOnGround` | `float` | 0.5f | – |
| Duration Auto Pull On Throw Hook On Air | `durationAutoPullOnThrowHookOnAir` | `float` | 0.5f | – |
| Use Max Swing Length | `useMaxSwingLength` | `bool` | – | – |
| Max Swing Length | `maxSwingLength` | `float` | – | – |
| Raycast Distance To Check Below Player | `raycastDistanceToCheckBelowPlayer` | `float` | 5 | – |
| Jump On Swing Enabled | `jumpOnSwingEnabled` | `bool` | true | – |
| Jump On Swing Force Amount | `jumpOnSwingForceAmount` | `Vector3` | – | – |
| Jump On Swing Force Amount2 5d | `jumpOnSwingForceAmount2_5d` | `Vector3` | new Vector3 (0, 5, 0) | – |
| Check If Too Close To Ground To Stop Swing | `checkIfTooCloseToGroundToStopSwing` | `bool` | – | – |
| Min Distance To Stop Swing On Ground Detected | `minDistanceToStopSwingOnGroundDetected` | `float` | – | – |
| Only Check If Close To Ground When Automatic Pull Not Active | `onlyCheckIfCloseToGroundWhenAutomaticPullNotActive` | `bool` | – | – |
| Swing Force Mode | `swingForceMode` | `ForceMode` | ForceMode.Impulse | – |
| Max Swing Speed Clamp | `maxSwingSpeedClamp` | `float` | 40 | – |
| Manual Pull Enabled | `manualPullEnabled` | `bool` | true | – |
| Manual Extend Enabled | `manualExtendEnabled` | `bool` | true | – |
| Chain Next Swing If Input Hold | `chainNextSwingIfInputHold` | `bool` | – | – |
| Min Time To Keep Swing Before Next | `minTimeToKeepSwingBeforeNext` | `float` | 1 | – |
| Min Wait Time To Throw Next Swing | `minWaitTimeToThrowNextSwing` | `float` | 0.5f | – |
| Stop Swing Hold Chain If Not Surface Located | `stopSwingHoldChainIfNotSurfaceLocated` | `bool` | true | – |
| Get Closest Surface If Not Found On Main Raycast | `getClosestSurfaceIfNotFoundOnMainRaycast` | `bool` | – | – |
| Swing Closest Surface Angle Search Range | `swingClosestSurfaceAngleSearchRange` | `Vector2` | new Vector2 (-40, 40) | – |
| Probability To Use Jump On Swing End | `probabilityToUseJumpOnSwingEnd` | `float` | 30 | – |

### Attract Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attract Objects Enabled | `attractObjectsEnabled` | `bool` | true | – |
| Regular Attraction Force | `regularAttractionForce` | `float` | – | – |
| Increased Attraction Force | `increasedAttractionForce` | `float` | – | – |
| Min Distance To Stop Attract Object | `minDistanceToStopAttractObject` | `float` | – | – |
| Add Up Force For Attraction | `addUpForceForAttraction` | `bool` | – | – |
| Up Force For Attraction | `upForceForAttraction` | `float` | – | – |
| Add Up Force For Attraction Duration | `addUpForceForAttractionDuration` | `float` | – | – |

### Movement Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Regular Movement Speed | `regularMovementSpeed` | `float` | 6 | – |
| Increased Movement Speed | `increasedMovementSpeed` | `float` | – | – |
| Input Movement Multiplier | `inputMovementMultiplier` | `float` | 3 | – |
| Air Control Amount | `airControlAmount` | `float` | 20 | – |
| Use Vertical Movement On Hook | `useVerticalMovementOnHook` | `bool` | – | – |
| Ignore Back Wards Movement On Hook | `ignoreBackWardsMovementOnHook` | `bool` | – | – |
| Add Vertical Falling Speed | `addVerticalFallingSpeed` | `bool` | – | – |
| Vertical Falling Speed | `verticalFallingSpeed` | `float` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check If Object Stuck | `checkIfObjectStuck` | `bool` | true | – |
| Time To Stop Hook If Stuck | `timeToStopHookIfStuck` | `float` | 2 | – |
| Min Distance To Check Stuck | `minDistanceToCheckStuck` | `float` | 1 | – |

### External Controller Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check External Controller States To Ignore | `checkExternalControllerStatesToIgnore` | `bool` | – | – |
| Other External Controller Info List | `otherExternalControllerInfoList` | `List<otherExternalControllerInfo>` | new List<otherExternalControllerInfo> () | – |
| Avoid List Of External Controller States | `avoidListOfExternalControllerStates` | `bool` | – | – |
| External Controller To Avoid List | `externalControllerToAvoidList` | `List<string>` | new List<string> () | – |

### Action System Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Custom Action Category ID | `customActionCategoryID` | `int` | -1 | – |
| Regular Action Category ID | `regularActionCategoryID` | `int` | -1 | – |

### Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Camera State On Third Person | `changeCameraStateOnThirdPerson` | `bool` | – | – |
| Camera State Name On Grappling Hook Activate | `cameraStateNameOnGrapplingHookActivate` | `string` | – | – |
| Camera State Name On Grappling Hook Deactivate | `cameraStateNameOnGrapplingHookDeactivate` | `string` | – | – |
| Keep Camera State Active While On Air | `keepCameraStateActiveWhileOnAir` | `bool` | – | – |
| Change Fov On Hook Active | `changeFovOnHookActive` | `bool` | – | – |
| Change Fov Speed | `changeFovSpeed` | `float` | – | – |
| Regula Fov | `regulaFov` | `float` | – | – |
| Increase Speed Fov | `increaseSpeedFov` | `float` | – | – |
| Use Camera Shake | `useCameraShake` | `bool` | – | – |
| Regular Camera Shake Name | `regularCameraShakeName` | `string` | – | – |
| Increase Camara Shake Name | `increaseCamaraShakeName` | `string` | – | – |

### Animator Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Animator State | `setAnimatorState` | `bool` | – | – |
| Hook Start Action Name | `hookStartActionName` | `string` | – | – |
| Hook End Action Name | `hookEndActionName` | `string` | – | – |
| Hook Start Action ID | `hookStartActionID` | `int` | – | – |
| Hook End Action ID | `hookEndActionID` | `int` | – | – |
| Action Active Animator Name | `actionActiveAnimatorName` | `string` | "Action Active" | – |
| Action ID Animator Name | `actionIDAnimatorName` | `string` | "Action ID" | – |
| Min Distance Percentage To Use Hook End Action | `minDistancePercentageToUseHookEndAction` | `float` | 0.1f | – |

### Swing Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Swing Jump On Air | `useSwingJumpOnAir` | `bool` | – | – |
| Swing Jump On Air ID | `swingJumpOnAirID` | `int` | 39475 | – |
| Swing Moving Pass Center ID | `swingMovingPassCenterID` | `int` | 92783 | – |
| Swing Moving Forward ID | `swingMovingForwardID` | `int` | 92782 | – |

### Throw Hook Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Animation To Throw Hook | `useAnimationToThrowHook` | `bool` | – | – |
| Use Animation To Throw Hook Only On Ground | `useAnimationToThrowHookOnlyOnGround` | `bool` | – | – |
| Throw Hook Animation Name | `throwHookAnimationName` | `string` | – | – |
| Throw Hook Animation Duration | `throwHookAnimationDuration` | `float` | – | – |
| Throw Animation In Process | `throwAnimationInProcess` | `bool` | – | – |
| Check If Surface Detected Before Animation | `checkIfSurfaceDetectedBeforeAnimation` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Grappling Hook Active | `grapplingHookActive` | `bool` | – | – |
| Grappling Hook Update Active | `grapplingHookUpdateActive` | `bool` | – | – |
| Current Force To Apply | `currentForceToApply` | `Vector3` | – | – |
| Movement Direction | `movementDirection` | `Vector3` | – | – |
| Current Distance | `currentDistance` | `float` | – | – |
| Current Movement Speed | `currentMovementSpeed` | `float` | – | – |
| Current Grappling Hook Target | `currentGrapplingHookTarget` | `Transform` | – | – |
| Angle To Target Direction | `angleToTargetDirection` | `float` | – | – |
| Attracting Object Active | `attractingObjectActive` | `bool` | – | – |
| Checking To Remove Hook Active | `checkingToRemoveHookActive` | `bool` | – | – |
| Manual Extend Active | `manualExtendActive` | `bool` | – | – |
| Manual Pull Active | `manualPullActive` | `bool` | – | – |
| Automatic Pull Active | `automaticPullActive` | `bool` | – | – |
| Current Min Distance To Stop Attract Object | `currentMinDistanceToStopAttractObject` | `float` | – | – |
| Attract Player Active | `attractPlayerActive` | `bool` | – | – |
| Ignore Apply Speed On Hook Stop On Player | `ignoreApplySpeedOnHookStopOnPlayer` | `bool` | – | – |
| Reset Player Speed On Hook Stop | `resetPlayerSpeedOnHookStop` | `bool` | – | – |
| Is Camera Type Free | `isCameraTypeFree` | `bool` | – | – |
| Is Player Moving On3d World | `isPlayerMovingOn3dWorld` | `bool` | – | – |

### Debug Attract

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Force Attraction Values | `useCustomForceAttractionValues` | `bool` | – | – |
| Custom Min Distance To Stop Attract Object | `customMinDistanceToStopAttractObject` | `float` | – | – |
| Custom Add Up Force For Attraction | `customAddUpForceForAttraction` | `bool` | – | – |
| Custom Up Force For Attraction | `customUpForceForAttraction` | `float` | – | – |
| Custom Add Up Force For Attraction Duration | `customAddUpForceForAttractionDuration` | `float` | – | – |

### Debug Swing

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Swing Gravity Forces | `swingGravityForces` | `Vector3` | Vector3.zero | – |
| Swing Hold Input Active | `swingHoldInputActive` | `bool` | – | – |
| Angle With Center | `angleWithCenter` | `float` | – | – |
| Swing Pass Center Checked | `swingPassCenterChecked` | `bool` | – | – |
| Swing Movement Direction | `swingMovementDirection` | `Vector3` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Grappling Hook | `useEventsOnGrapplingHook` | `bool` | – | – |
| Event On Grappling Hook Activate | `eventOnGrapplingHookActivate` | `UnityEvent` | – | – |
| Event On Grappling Hook Deactivate | `eventOnGrapplingHookDeactivate` | `UnityEvent` | – | – |
| Event With Direction On Hook Active | `eventWithDirectionOnHookActive` | `eventParameters.eventToCallWithVector3` | – | – |
| Use Events On Change Camera View | `useEventsOnChangeCameraView` | `bool` | – | – |
| Event On Set First Person View | `eventOnSetFirstPersonView` | `UnityEvent` | – | – |
| Event On Set Third Person View | `eventOnSetThirdPersonView` | `UnityEvent` | – | – |
| Event To Send New Grappling Hook Tip Transform | `eventToSendNewGrapplingHookTipTransform` | `eventParameters.eventToCallWithTransform` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grappling Hook Tip Transform | `grapplingHookTipTransform` | `Transform` | – | – |
| Player Controller Transform | `playerControllerTransform` | `Transform` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Gravity System | `mainGravitySystem` | `gravitySystem` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Remote Event System | `mainRemoteEventSystem` | `remoteEventSystem` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |
| Main Swing Rigidbody | `mainSwingRigidbody` | `Rigidbody` | – | – |
| Main Swing Collider | `mainSwingCollider` | `Collider` | – | – |
| Swing Joint | `swingJoint` | `SpringJoint` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopGrapplingHookCoroutine()` | `grapplingHookCoroutine`を止め`grapplingHookUpdateActive`をfalseにして更新を停止する。 |
| `stopCheckinGrapplingHookCameraStateAfterDeactivateCoroutine()` | 着地待ちのカメラ復帰コルーチンを停止し、待機フラグをfalseにする。 |
| `TransformDirectionHorizontal(Transform t, Vector3 v)` | `t`で方向変換した`v`から水平成分だけを取り出し、正規化したベクトルを返す。 |
| `ToHorizontal(Vector3 v)` | `v`を`Vector3.up`の平面へ射影して水平成分だけを返すだけ。 |
| `applyHookForces()` | フック先までの距離を測り、スイングまたは引き寄せ/入力方向を合成して`setExternalForceOnAir`で移動力を与える。 |
| `applyAttractionForces()` | 引っ掛けた剛体をプレイヤー側へ引き寄せ、`linearVelocity`に力を設定して毎フレーム更新する。 |
| `checkIfObjectIsMoving()` | `checkIfObjectStuck`時、一定時間でフック先との距離が変わらなければ`removeHook`で外す。 |
| `removeHook()` | フックを非アクティブ化し、空中外力やアクションカテゴリ、吸引対象の状態と遠隔イベントを解除する。 |
| `setGrapplingHookTarget(Transform newTarget)` | `currentGrapplingHookTarget`に`newTarget`を代入するだけ。 |
| `setGrapplingHookEnabledState(bool state)` | `grapplingHookEnabled`を設定し、無効化時は`removeGrapplingHook`でフックを外す。 |
| `checkThrowGrapplingHook()` | レイキャストで表面を探し、命中点へフック先を付け`grapplingHookActive`を立ててコルーチンとイベントを開始する。 |
| `removeGrapplingHook()` | フック使用中に`checkingToRemoveHookActive`を立て、既に立っていれば`removeHook`で解除する。 |
| `checkRemoveGrapplingHook()` | 有効時に`removeGrapplingHook`を呼び、スイング保持入力中なら中断してコルーチンを止める。 |
| `checkEventsOnGrapplingHook(bool state)` | `useEventsOnGrapplingHook`時、`state`に応じフックの開始/終了イベントを発火する。 |
| `checkExternalControllerBehaviorToPause(string behaviorName)` | フック中、現在の外部コントローラ行動名が一致したらその行動を一時停止し、対応イベントを発火する。 |
| `pauseOrResumePlayerState(bool state)` | フック開始/終了に合わせ、重力・接地・IK・カメラ・FOV・終了時の慣性力を一括で切り替える。 |
| `setIgnoreApplySpeedOnHookStopTemporallyState(bool state)` | フック中のみ、停止時の慣性力を一時的に無視するフラグを設定するだけ。 |
| `inputThrowGrapplingHook()` | 入力でフック投擲を開始し、アニメーション使用時は表面確認後にジョイント追加、未使用時は`checkThrowGrapplingHook`を呼ぶ。 |
| `inputRemoveGrapplingHook()` | `checkRemoveGrapplingHook`を呼ぶだけ。 |
| `inputIncreaseOrDecreaseMovementSpeed(bool state)` | フック中の`increaseSpeedActive`を設定し、FOVとカメラシェイクを高速用/通常用に切り替える。 |
| `inputThrowGrapplingHookIfTargetLocated()` | 目標が設定済みのとき、フック中なら外し、そうでなければ投擲入力を行う。 |
| `inputSetManualPullActiveState(bool state)` | `manualPullEnabled`かつスイング中に`manualPullActive`を設定し、拡張側を解除する。 |
| `inputSetManualExtendActiveState(bool state)` | `manualExtendEnabled`かつスイング中に`manualExtendActive`を設定し、引き寄せ側を解除する。 |
| `inputToggleManualPullActiveState()` | `manualPullActive`を反転して`inputSetManualPullActiveState`へ渡すだけ。 |
| `inputUseJumpOnSwing()` | スイング中にフックを外し、上方向と前方向の力を`useJumpPlatform`で加えてジャンプさせる。 |
| `inputSetSwingHoldInputActive(bool state)` | 保持連続スイングの入力を設定し、開始でコルーチンを起動、終了でジャンプか解除を抽選する。 |
| `setAttractObjectsEnabled(bool state)` | `attractObjectsEnabled`に`state`を代入するだけ。 |
| `setUseSwingForcesActiveState(bool state)` | `useSwingForcesActive`に`state`を代入するだけ。 |
| `setCurrentPlayerActionSystemCustomActionCategoryID(bool state)` | `state`に応じカスタム用/通常用のアクションカテゴリIDをプレイヤーへ設定する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnGrapplingHookActivate` | `UnityEvent` | – |
| `eventOnGrapplingHookDeactivate` | `UnityEvent` | – |
| `eventOnSetFirstPersonView` | `UnityEvent` | – |
| `eventOnSetThirdPersonView` | `UnityEvent` | – |

## 内部型

- `otherExternalControllerInfo`（class）
