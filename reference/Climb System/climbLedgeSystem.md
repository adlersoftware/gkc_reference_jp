# climbLedgeSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Climb System/climbLedgeSystem.cs:6`

**概要**: レッジの検出から掴み・登攀・ジャンプ・落下までをレイキャストとアニメーションで制御し、状態に応じてプレイヤーを停止・復帰させる。

**公式ドキュメント抜粋**（[Climb Ledge System](../../docs/player-controller-components/non-essential-components/climb-ledge-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Climb Ledge Active | `climbLedgeActive` | `bool` | – | – |
| Use Hang From Ledge Icon | `useHangFromLedgeIcon` | `bool` | – | – |
| Use Fixed Device Icon Position | `useFixedDeviceIconPosition` | `bool` | – | – |
| Keep Weapons On Ledge Detected | `keepWeaponsOnLedgeDetected` | `bool` | – | – |
| Draw Weapons After Climb Ledge If Previously Carried | `drawWeaponsAfterClimbLedgeIfPreviouslyCarried` | `bool` | – | – |

### Climb Animator Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Climb Ledge Action ID | `climbLedgeActionID` | `int` | 1 | – |
| Hold On Ledge Action Name | `holdOnLedgeActionName` | `string` | "Hold On Ledge" | – |
| Action Active Animator Name | `actionActiveAnimatorName` | `string` | "Action Active" | – |
| Action ID Animator Name | `actionIDAnimatorName` | `string` | "Action ID" | – |
| Match Start Value | `matchStartValue` | `float` | – | – |
| Match End Value | `matchEndValue` | `float` | – | – |
| Match Mask Value | `matchMaskValue` | `Vector3` | – | – |
| Match Mask Rotation Value | `matchMaskRotationValue` | `float` | – | – |
| Base Layer Index | `baseLayerIndex` | `int` | 0 | – |

### Raycast Ledge Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Climb Ledge Ray Forward Distance | `climbLedgeRayForwardDistance` | `float` | 1 | – |
| Climb Ledge Ray Down Distance | `climbLedgeRayDownDistance` | `float` | 1 | – |
| Layer Mask To Check | `layerMaskToCheck` | `LayerMask` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Only Grab Ledge If Moving Forward | `onlyGrabLedgeIfMovingForward` | `bool` | – | – |
| Min Wait To Climb After Hold On Ledge | `minWaitToClimbAfterHoldOnLedge` | `float` | 0.6f | – |
| Adjust To Hold On Ledge Position Speed | `adjustToHoldOnLedgePositionSpeed` | `float` | 3 | – |
| Adjust To Hold On Ledge Rotation Speed | `adjustToHoldOnLedgeRotationSpeed` | `float` | 10 | – |
| Hold On Ledge Offset | `holdOnLedgeOffset` | `Vector3` | – | – |
| Hold On Ledge Offset FBA | `holdOnLedgeOffsetFBA` | `Vector3` | new Vector3 (0, -1.65f, -0.8f) | – |
| Climb Ledge Target Position Offset Third Person | `climbLedgeTargetPositionOffsetThirdPerson` | `Vector3` | – | – |
| Climd Ledge Target Position Offset First Person | `climdLedgeTargetPositionOffsetFirstPerson` | `Vector3` | – | – |
| Climd Ledge Target Position Offset First FBA | `climdLedgeTargetPositionOffsetFirstFBA` | `Vector3` | new Vector3 (0, 0.64f, 0.15f) | – |
| Hand Offset | `handOffset` | `float` | 0.2f | – |
| Time To Climb Ledge Third Person | `timeToClimbLedgeThirdPerson` | `float` | 2 | – |
| Time To Climb Ledge First Person | `timeToClimbLedgeFirstPerson` | `float` | 1 | – |
| Climb Ledge Speed First Person | `climbLedgeSpeedFirstPerson` | `float` | 1 | – |
| Climb If Surface Found Below Player | `climbIfSurfaceFoundBelowPlayer` | `bool` | – | – |
| Check For Ledge Zones Active | `checkForLedgeZonesActive` | `bool` | true | – |

### Ledge Below Check Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check For Hang From Ledge On Ground | `checkForHangFromLedgeOnGround` | `bool` | – | – |
| Check Ledge Zone Detected By Raycast | `checkLedgeZoneDetectedByRaycast` | `bool` | – | – |
| Raycast Radius To Check Surface Below Player | `raycastRadiusToCheckSurfaceBelowPlayer` | `float` | – | – |
| Check For Hang From Ledge On Ground Raycast Distance | `checkForHangFromLedgeOnGroundRaycastDistance` | `float` | – | – |
| Only Hang From Ledge If Player Is Not Moving | `onlyHangFromLedgeIfPlayerIsNotMoving` | `bool` | – | – |
| Time To Cancel Hang From Ledge If Not Found | `timeToCancelHangFromLedgeIfNotFound` | `float` | 3 | – |
| Can Cancel Hang From Ledge | `canCancelHangFromLedge` | `bool` | – | – |
| Has To Look At Ledge Position On First Person | `hasToLookAtLedgePositionOnFirstPerson` | `bool` | – | – |
| Use Max Distance To Camera Center | `useMaxDistanceToCameraCenter` | `bool` | – | – |
| Max Distance To Camera Center | `maxDistanceToCameraCenter` | `float` | – | – |

### Auto Climb Ledge Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Auto Climb In Third Person | `autoClimbInThirdPerson` | `bool` | – | – |
| Auto Climb In First Person | `autoClimbInFirstPerson` | `bool` | – | – |

### Jump Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Jump When Hold Ledge | `canJumpWhenHoldLedge` | `bool` | – | – |
| Jump Force When Hold Ledge | `jumpForceWhenHoldLedge` | `float` | 10 | – |
| Jump Force Mode | `jumpForceMode` | `ForceMode` | – | – |

### Grab Surface On Air Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Grab To Surface On Air Input Enabled | `canGrabToSurfaceOnAirInputEnabled` | `bool` | – | – |
| Can Grab Any Surface On Air | `canGrabAnySurfaceOnAir` | `bool` | – | – |
| Use Grab Surface Amount Limit | `useGrabSurfaceAmountLimit` | `bool` | – | – |
| Grab Surface Amount Limit | `grabSurfaceAmountLimit` | `int` | – | – |
| Current Grab Surface Amount | `currentGrabSurfaceAmount` | `int` | – | – |
| Use Surfaces To Check Tags On Grab Surface By Input | `useSurfacesToCheckTagsOnGrabSurfaceByInput` | `bool` | – | – |
| Surfaces To Check Tags Grab Surface By Input List | `surfacesToCheckTagsGrabSurfaceByInputList` | `List<string>` | new List<string> () | – |
| Check Move Input Direction On Jump | `checkMoveInputDirectionOnJump` | `bool` | – | – |
| Jump Rotation Speed Third Person | `jumpRotationSpeedThirdPerson` | `float` | 1 | – |
| Jump Rotation Speed First Person | `jumpRotationSpeedFirstPerson` | `float` | 0.5f | – |
| Jump Force When Hold Ledge On Opposite Direction | `jumpForceWhenHoldLedgeOnOppositeDirection` | `float` | 15 | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events | `useEvents` | `bool` | – | – |
| Event On Ledge Grabbed | `eventOnLedgeGrabbed` | `UnityEvent` | – | – |
| Event On Ledge Lose | `eventOnLedgeLose` | `UnityEvent` | – | – |
| Event On Ledge Climbed | `eventOnLedgeClimbed` | `UnityEvent` | – | – |
| Event On Start Ledge Climb | `eventOnStartLedgeClimb` | `UnityEvent` | – | – |
| Event On Ledge Jump | `eventOnLedgeJump` | `UnityEvent` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | – | – |
| Gizmo Radius | `gizmoRadius` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Avoid Player Grab Ledge | `avoidPlayerGrabLedge` | `bool` | – | – |
| Ledge Zone Found | `ledgeZoneFound` | `bool` | – | – |
| Activate Climb Action | `activateClimbAction` | `bool` | – | – |
| Can Start To Climb Ledge | `canStartToClimbLedge` | `bool` | – | – |
| Climbing Ledge | `climbingLedge` | `bool` | – | – |
| Can Use Climb Ledge | `canUseClimbLedge` | `bool` | – | – |
| Can Climb Current Ledge Zone | `canClimbCurrentLedgeZone` | `bool` | true | – |
| Stop Grab Ledge | `stopGrabLedge` | `bool` | – | – |
| Direction Angle | `directionAngle` | `float` | – | – |
| Surface To Hang On Ground Found | `surfaceToHangOnGroundFound` | `bool` | – | – |
| Moving Toward Surface To Hang | `movingTowardSurfaceToHang` | `bool` | – | – |
| Previously Moving Toward Surface To Hang | `previouslyMovingTowardSurfaceToHang` | `bool` | – | – |
| On Air While Searching Ledge To Hang | `onAirWhileSearchingLedgeToHang` | `bool` | – | – |
| Ledge Zone Close Enough To Screen Center | `ledgeZoneCloseEnoughToScreenCenter` | `bool` | – | – |
| Current Distance To Target | `currentDistanceToTarget` | `float` | – | – |
| Can Check For Hang From Ledge On Ground | `canCheckForHangFromLedgeOnGround` | `bool` | true | – |
| Climb Ledge Action Activated | `climbLedgeActionActivated` | `bool` | – | – |
| Lose Ledge Action Activated | `loseLedgeActionActivated` | `bool` | – | – |
| Grabbing Surface | `grabbingSurface` | `bool` | – | – |
| Climb Ledge Action Paused | `climbLedgeActionPaused` | `bool` | – | – |
| Other Climb Action Active | `otherClimbActionActive` | `bool` | – | – |

### Climb Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Climb Ledge Ray Position | `climbLedgeRayPosition` | `Transform` | – | – |
| Climb Ledge Ray Down Position | `climbLedgeRayDownPosition` | `Transform` | – | – |
| Hold Ledge Zone | `holdLedgeZone` | `Transform` | – | – |
| Climb Ledg Zone | `climbLedgZone` | `Transform` | – | – |
| Hang From Ledge On Ground Raycast Position | `hangFromLedgeOnGroundRaycastPosition` | `Transform` | – | – |
| Hang From Ledge Icon | `hangFromLedgeIcon` | `GameObject` | – | – |
| Hang From Ledge Icon Rect Transform | `hangFromLedgeIconRectTransform` | `RectTransform` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Player Input | `playerInput` | `playerInputManager` | – | – |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | – |
| Powers Manager | `powersManager` | `otherPowers` | – | – |
| Head Bob Manager | `headBobManager` | `headBob` | – | – |
| Gravity Manager | `gravityManager` | `gravitySystem` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Animator | `animator` | `Animator` | – | – |
| Main Collider | `MainCollider` | `Collider` | – | – |
| Using Devices Manager | `usingDevicesManager` | `usingDevicesSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableHangFromLedgeIcon(bool state)` | `hangFromLedgeIcon`の表示を`state`に合わせて切り替える。 |
| `resumePlayer()` | 親設定や各種フラグを戻し、プレイヤーの移動・カメラ・アニメータを通常状態へ復帰させる。 |
| `startClimbLedgeAction()` | 登攀可否を確認し、ルートモーションを有効化して登攀アニメーションと移動を開始する。 |
| `startLoseLedgeAction()` | 掴んでいる時のみ下向きの速度を与えて`resumePlayer`し、レッジ喪失イベントを発火する。 |
| `loseAnyGrabbedSurface()` | `grabbingSurface`中なら`resumePlayer`で掴みを解除するだけ。 |
| `MatchTarget(Vector3 matchPosition, Quaternion matchRotation, AvatarTarget target, MatchTargetWeightMask weightMask, float normalisedStartTime, float normalisedEndTime)` | 遷移中や終了後でなければ`animator.MatchTarget`を呼び、位置と回転をアニメーションに合わせる。 |
| `adjustHoldOnLedge()` | 既存コルーチンを止め、プレイヤーを掴み位置へ移動・回転させるコルーチンを開始する。 |
| `stopAdjustHoldOnLedgeCoroutine()` | 調整コルーチンを停止し、調整中フラグを解除する。 |
| `climbLedgeOnFirstPersonMovement()` | 既存コルーチンを止め、一人称用の位置移動コルーチンを開始する。 |
| `stopClimbLedgeOnFirstPersonMovementCoroutine()` | 一人称移動コルーチンがあれば停止するだけ。 |
| `rotateTowardLedgeOnFirstPerson()` | 移動コルーチンを止め、カメラをレッジの壁向きへ回すコルーチンを開始する。 |
| `stopRotateTowardLedgeOnFirstPersonCoroutine()` | 一人称の回転コルーチンがあれば停止するだけ。 |
| `setLedgeZoneFoundState(bool state)` | レッジゾーン確認が有効な時のみ`ledgeZoneFound`を設定する。 |
| `setNewRaycastDistance(float forwardDistance, float downDistance, Vector3 newCheckDownRaycastOffset)` | ゾーン確認が有効な時のみ前方・下方のレイ距離と下方チェックのオフセットを差し替える。 |
| `setOriginalRaycastDistance()` | 保存済みのレイ距離へ戻し、下方オフセットをゼロにする。 |
| `setCanClimbCurrentLedgeZoneState(bool state)` | `canClimbCurrentLedgeZone`を設定するだけ。 |
| `setCanGrabAnySurfaceOnAirActiveState(bool state)` | 空中での面掴み入力の有効フラグを設定するだけ。 |
| `setCanGrabAnySurfaceOnAirState(bool state)` | 空中で任意の面を掴めるかのフラグを設定するだけ。 |
| `inputJumpOnHoldLedge()` | レッジ保持中のジャンプ入力で、入力方向に応じた飛び出しや真上ジャンプを行いイベントを出す。 |
| `inputGrabSurface()` | 空中面掴み入力が有効なら`activateGrabToSurfaceAction`を呼ぶだけ。 |
| `activateGrabToSurfaceAction()` | 停止・ポーズ・デバイス使用中などを除いた条件を満たす時、面の掴み処理へ進む。 |
| `activateGrabToSurfaceActionExternally(bool state, Transform newLedgeTransform)` | 外部から掴み対象を指定して掴みを起動し、重複や直後の再呼び出しは無視する。 |
| `canGrabToSurface()` | 接地・登攀中・壁走り・水泳・飛行などの状態を除いて掴み可能かを返す。 |
| `enableOrDisableGrabToSurfaceState()` | 掴み中なら解除し、そうでなければ前方レイで面を探して停止・位置合わせ・掴みイベントを行う。 |
| `setPlayerPauseState()` | 移動や重力、頭トラック、アニメータを止め、レッジ掴み姿勢へ切り替える。 |
| `activateGrabLedge()` | 複数のレイキャストでレッジ位置と登攀位置を求め、プレイヤーを停止して位置合わせと掴みイベントを行う。 |
| `setClimbLedgeActiveState(bool state)` | `climbLedgeActive`を設定するだけ。 |
| `setClimbLedgeActiveStateFromEditor(bool state)` | `climbLedgeActive`を設定してコンポーネントを更新する。 |
| `checkEventOnLedgeGrabbed()` | `useEvents`が有効なら`eventOnLedgeGrabbed`を発火する。 |
| `checkEventOnLedgeLose()` | `useEvents`が有効なら`eventOnLedgeLose`を発火する。 |
| `checkEventOnLedgeClimbed()` | `useEvents`が有効なら`eventOnLedgeClimbed`を発火する。 |
| `checkEventOnStartLedgeClimb()` | `useEvents`が有効なら`eventOnStartLedgeClimb`を発火する。 |
| `checkEventOnLedgeJump()` | `useEvents`が有効なら`eventOnLedgeJump`を発火する。 |
| `setAvoidPlayerGrabLedgeValue(bool state)` | `avoidPlayerGrabLedge`を設定するだけ。 |
| `stopHangFromLedge()` | ハング検索の入力上書きや各フラグを初期化し、必要ならハングアイコンを消す。 |
| `setCanCheckForHangFromLedgeOnGroundState(bool state)` | `canCheckForHangFromLedgeOnGround`を設定するだけ。 |
| `setOnlyHangFromLedgeIfPlayerIsNotMovingValue(bool state)` | `onlyHangFromLedgeIfPlayerIsNotMoving`を設定するだけ。 |
| `setOnlyHangFromLedgeIfPlayerIsNotMovingOriginalValue()` | `onlyHangFromLedgeIfPlayerIsNotMoving`を保存済みの初期値へ戻すだけ。 |
| `setClimbLedgeActionPausedState(bool state)` | `climbLedgeActionPaused`を設定するだけ。 |
| `setOtherClimbActionActiveState(bool state)` | `otherClimbActionActive`を設定するだけ。 |
| `setGrabToSurfaceInputPausedState(bool state)` | `grabToSurfaceInputPaused`を設定するだけ。 |
| `stopSetClimbLedgeActionPausedStateWithDurationCoroutine()` | ポーズ用コルーチンがあれば停止するだけ。 |
| `setClimbLedgeActionPausedStateWithDuration(float pauseDuration)` | 既存コルーチンを止め、指定時間だけ登攀ポーズと掴み禁止を立てるコルーチンを開始する。 |
| `rotateCharacterOnJump()` | ジャンプ時の回転コルーチンを開始するだけ。 |
| `rotateCharacterOnJumpCoroutine()` | `currentDirectionToRotatePlayer`方向へ、一人称/FBAならカメラ、三人称ならプレイヤーを徐々に回す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnLedgeGrabbed` | `UnityEvent` | – |
| `eventOnLedgeLose` | `UnityEvent` | – |
| `eventOnLedgeClimbed` | `UnityEvent` | – |
| `eventOnStartLedgeClimb` | `UnityEvent` | – |
| `eventOnLedgeJump` | `UnityEvent` | – |
