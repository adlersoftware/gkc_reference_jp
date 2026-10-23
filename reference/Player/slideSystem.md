# slideSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `externalControllerBehavior`
- **ソース**: `Player/Extra Movements/slideSystem.cs:6`

**概要**: 斜面やスライドゾーンでのスライディング移動を制御する外部コントローラ。状態に応じて接地判定・Animator・カメラ・重力法線への張り付きを切り替え、終了時は勢いを加えて解除する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slide Enabled | `slideEnabled` | `bool` | true | – |
| Raycast Layermask | `raycastLayermask` | `LayerMask` | – | – |
| Raycast Distance | `raycastDistance` | `float` | 0.6f | – |
| Slide Active Raycast Distance | `slideActiveRaycastDistance` | `float` | 3 | – |

### Speed Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slide Speed | `slideSpeed` | `float` | – | – |
| Slide Horizontal Speed | `slideHorizontalSpeed` | `float` | – | – |
| Slide Sprint Speed | `slideSprintSpeed` | `float` | – | – |
| Slide Slow Down Sped | `slideSlowDownSped` | `float` | – | – |
| Slide Vertical Speed | `slideVerticalSpeed` | `float` | – | – |
| Slide Rotation Speed | `slideRotationSpeed` | `float` | – | – |
| Slider Can Be Used | `sliderCanBeUsed` | `bool` | true | – |
| Impulse On Jump | `impulseOnJump` | `Vector3` | – | – |
| End Of Surface Impulse | `endOfSurfaceImpulse` | `Vector3` | – | – |
| Horizontal Input Amount | `horizontalInputAmount` | `float` | 1 | – |
| Regular Slide Movement Amount | `regularSlideMovementAmount` | `float` | 0.4f | – |
| Min Wait Time To Slide Check Slide Active | `minWaitTimeToSlideCheckSlideActive` | `float` | 1 | – |

### Surface Angle Speed Multiplier Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Speed Based On Surface Angle | `changeSpeedBasedOnSurfaceAngle` | `bool` | – | – |
| Min Angle To Increase Speed | `minAngleToIncreaseSpeed` | `float` | – | – |
| Speed On Surface Angle Multiplier | `speedOnSurfaceAngleMultiplier` | `float` | – | – |
| Stop Slide If Surface Angle Too Low | `stopSlideIfSurfaceAngleTooLow` | `bool` | – | – |
| Min Angle To Stop Slide | `minAngleToStopSlide` | `float` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Max Velocity Change Slide | `maxVelocityChangeSlide` | `float` | – | – |
| Keep Weapons | `keepWeapons` | `bool` | – | – |
| Draw Weapons If Carried Previously | `drawWeaponsIfCarriedPreviously` | `bool` | – | – |
| Set New Aim Weapon Camera State | `setNewAimWeaponCameraState` | `bool` | – | – |
| Custom Default Third Person Aim Right State Name | `customDefaultThirdPersonAimRightStateName` | `string` | "Aim Right On Slide" | – |
| Custom Default Third Person Aim Left State Name | `customDefaultThirdPersonAimLeftStateName` | `string` | "Aim Left On Slide" | – |
| New Camera State | `newCameraState` | `string` | "Slide View" | – |
| Stop Slide If Obstacle Detected | `stopSlideIfObstacleDetected` | `bool` | – | – |
| Obstacle Layermask | `obstacleLayermask` | `LayerMask` | – | – |

### Manual Slide Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Manual Slide Can Be Enabled | `manualSlideCanBeEnabled` | `bool` | true | – |
| Stop Manual Slide After Time Delay | `stopManualSlideAfterTimeDelay` | `bool` | – | – |
| Time Delay To Stop Manual Slide | `timeDelayToStopManualSlide` | `float` | – | – |

### Gravity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Adhere To Surfaces Enabled | `adhereToSurfacesEnabled` | `bool` | – | – |
| Adhere To Surfaces Rotation Speed | `adhereToSurfacesRotationSpeed` | `float` | – | – |
| Disable Slide When Disabling Adhere State | `disableSlideWhenDisablingAdhereState` | `bool` | true | – |
| Reset Gravity Direction On Slide Exit Enabled | `resetGravityDirectionOnSlideExitEnabled` | `bool` | true | – |

### Third Person Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Action ID | `actionID` | `int` | 08632946 | – |
| Slide Standing Action ID | `slideStandingActionID` | `int` | 08632945 | – |
| Use Slide Standing Action ID On Manual Slide | `useSlideStandingActionIDOnManualSlide` | `bool` | – | – |
| Use Slide Standing Action ID On Trigger Slide | `useSlideStandingActionIDOnTriggerSlide` | `bool` | – | – |
| External Controlle Behavior Active Animator Name | `externalControlleBehaviorActiveAnimatorName` | `string` | "External Behavior Active" | – |
| Action ID Animator Name | `actionIDAnimatorName` | `string` | "Action ID" | – |
| Horizontal Animator Name | `horizontalAnimatorName` | `string` | "Horizontal Action" | – |
| Input Lerp Speed | `inputLerpSpeed` | `float` | 3 | – |

### Third Person Camera State Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Camera State On Third Person | `setNewCameraStateOnThirdPerson` | `bool` | – | – |
| New Camera State On Third Person | `newCameraStateOnThirdPerson` | `string` | – | – |
| Set New Camera State On FBA | `setNewCameraStateOnFBA` | `bool` | – | – |
| New Camera State On FBA | `newCameraStateOnFBA` | `string` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Check If Detect Slide Active | `checkIfDetectSlideActive` | `bool` | – | – |
| Slide Active | `slideActive` | `bool` | – | – |
| Is First Person Active | `isFirstPersonActive` | `bool` | – | – |
| Current Horizontal Movement | `currentHorizontalMovement` | `float` | – | – |
| Current Vertical Movement | `currentVerticalMovement` | `float` | – | – |
| Slide Speed Multiplier | `slideSpeedMultiplier` | `float` | 1 | – |
| Carrying Weapons Previously | `carryingWeaponsPreviously` | `bool` | – | – |
| Current Slide Transform | `currentSlideTransform` | `Transform` | – | – |
| Current Slide Speed | `currentSlideSpeed` | `float` | – | – |
| Move Input | `moveInput` | `Vector3` | – | – |
| Local Move | `localMove` | `Vector3` | – | – |
| Current Slide Zones Amount Detected | `currentSlideZonesAmountDetected` | `int` | – | – |
| Slide Activated By Slide Zone | `slideActivatedBySlideZone` | `bool` | – | – |
| Adhere To Surfaces Active | `adhereToSurfacesActive` | `bool` | – | – |
| Original Normal | `originalNormal` | `Vector3` | – | – |
| Running Active | `runningActive` | `bool` | – | – |
| Manual Slide Active | `manualSlideActive` | `bool` | – | – |
| Target Rotation | `targetRotation` | `float` | – | – |

### First Person Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On First Person | `useEventsOnFirstPerson` | `bool` | – | – |
| Event On Start First Person | `eventOnStartFirstPerson` | `UnityEvent` | – | – |
| Event On End First Person | `eventOnEndFirstPerson` | `UnityEvent` | – | – |

### Third Person Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Third Person | `useEventsOnThirdPerson` | `bool` | – | – |
| Event On Start Third Person | `eventOnStartThirdPerson` | `UnityEvent` | – | – |
| Event On End Third Person | `eventOnEndThirdPerson` | `UnityEvent` | – | – |

### Run On Slide Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Eventts On Run Slide State Change | `useEventtsOnRunSlideStateChange` | `bool` | – | – |
| Event On Start Run On Slide | `eventOnStartRunOnSlide` | `UnityEvent` | – | – |
| Event On Stop Run On Slide | `eventOnStopRunOnSlide` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Player Camera Transform | `playerCameraTransform` | `Transform` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Gravity System | `mainGravitySystem` | `gravitySystem` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setSlideImpulseForce(Vector3 forceAmount, bool useCameraDirection)` | クランプした速度変化を記録してRigidbodyへ加える（`useCameraDirection` は未使用）。 |
| `setJumpActive(Vector3 newImpulseOnJumpAmount)` | スライド中なら解除し、y成分を上・z成分を前方としてジャンプ力を加え、スライドゾーン由来でなければ検出も止める。 |
| `setCheckIfDetectSlideActiveState(bool state, bool slideActivatedBySlideZoneValue)` | 検出中のゾーン数を増減して管理し、重複が無い場合に検出状態と外部ビヘイビア登録・落下ダメージ停止を更新する。 |
| `setSlideActiveState(bool state)` | スライド状態を切り替え、接地・Animator・武器入力・足音・カメラ状態・重力法線・各種イベントをまとめて更新する。 |
| `setSlideEnabledState(bool state)` | falseならスライドを終了させ、`slideEnabled` を設定する。 |
| `setSlideCanBeUsedState(bool state)` | `sliderCanBeUsed` を設定するだけ。 |
| `setSliderEnabledState()` | `originalSlideEnabled` を渡して有効状態を戻すだけ。 |
| `setOriginalSliderEnabledState()` | スライド中なら検出を止めてから `originalSlideEnabled` に戻す。 |
| `setCurrentSlideTransform(Transform newTransform)` | 現在のスライド面Transformを設定する（null時は検出ゾーン数が0のときのみ）。 |
| `setSlideSpeedMultiplier(float newValue)` | `slideSpeedMultiplier` を設定するだけ。 |
| `setManualSlideCanBeEnabledState(bool state)` | `manualSlideCanBeEnabled` を設定するだけ。 |
| `enableCheckIfDetectSlideActiveStateExternally()` | 手動可否と現在状態を確認し、検出を有効化して `manualSlideActive` をtrueにする。 |
| `disableCheckIfDetectSlideActiveStateExternally()` | 手動スライド中のみ検出を無効化し、`manualSlideActive` をfalseにする。 |
| `checkEventsOnStateChange(bool state)` | 一人称か三人称かに応じた設定が有効なら、開始/終了イベントを発火する。 |
| `checkEventsOnRunOnSlideStateChange(bool state)` | 設定が有効なら、走行スライドの開始/停止イベントを発火する。 |
| `setAdhereToSurfacesActiveState(bool state)` | 張り付きが有効な場合のみ、無効化でスライド停止、有効化で現在の法線を保存する。 |
| `setResetGravityDirectionOnSlideExitEnabledState(bool state)` | `resetGravityDirectionOnSlideExitEnabled` を設定するだけ。 |
| `setOriginalResetGravityDirectionOnSlideExitEnabled()` | 保存した初期値に戻すだけ。 |
| `setCanUseRunPausedState(bool state)` | `canUseRunPaused` を設定するだけ。 |
| `setSlideEnabledStateFromEditor(bool state)` | 有効状態を設定してコンポーネントを更新する。 |
| `setManualSlideCanBeEnabledStateFromEditor(bool state)` | 手動スライド可否を設定してコンポーネントを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartFirstPerson` | `UnityEvent` | – |
| `eventOnEndFirstPerson` | `UnityEvent` | – |
| `eventOnStartThirdPerson` | `UnityEvent` | – |
| `eventOnEndThirdPerson` | `UnityEvent` | – |
| `eventOnStartRunOnSlide` | `UnityEvent` | – |
| `eventOnStopRunOnSlide` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`disableExternalControllerState()`, `setCurrentPlayerActionSystemCustomActionCategoryID()`, `setExternalForceActiveState(bool state)`, `setExternalForceEnabledState(bool state)`, `setExtraImpulseForce(Vector3 forceAmount, bool useCameraDirection)`, `setJumpActiveForExternalForce()`, `updateControllerBehavior()`

</details>
