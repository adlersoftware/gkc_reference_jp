# wallSlideJumpSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `externalControllerBehavior`
- **ソース**: `Player/Extra Movements/wallSlideJumpSystem.cs:6`

**概要**: 壁に沿って滑り落ちるスライドと壁ジャンプを扱う `externalControllerBehavior`。壁検出の有効化、スライド状態に応じたアニメ・武器・カメラの切替、ジャンプ時の回転を行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slide Enabled | `slideEnabled` | `bool` | true | – |
| Raycast Layermask | `raycastLayermask` | `LayerMask` | – | – |
| Raycast Distance | `raycastDistance` | `float` | 0.6f | – |
| Slide Active Raycast Distance | `slideActiveRaycastDistance` | `float` | 3 | – |
| Adhere To Wall Speed | `adhereToWallSpeed` | `float` | 5 | – |
| Jump Rotation Speed Third Person | `jumpRotationSpeedThirdPerson` | `float` | 1 | – |
| Jump Rotation Speed First Person | `jumpRotationSpeedFirstPerson` | `float` | 0.5f | – |
| Min Angle To Adhere To Wall | `minAngleToAdhereToWall` | `float` | 20 | – |
| Down Raycast Distance To Check To Adhere To Wall | `downRaycastDistanceToCheckToAdhereToWall` | `float` | 3 | – |
| Min Wait Time To Adhere Again | `minWaitTimeToAdhereAgain` | `float` | 0.3f | – |

### Slide Down Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slide Down On Wall | `slideDownOnWall` | `bool` | – | – |
| Slide Down On Wall Speed | `slideDownOnWallSpeed` | `float` | – | – |
| Wait Time To Start To Slide Down | `waitTimeToStartToSlideDown` | `float` | – | – |
| Stop Slide Down After Time | `stopSlideDownAfterTime` | `bool` | – | – |
| Time To Stop Slide Down | `timeToStopSlideDown` | `float` | – | – |
| Disable Slide On Wall After Time | `disableSlideOnWallAfterTime` | `bool` | – | – |
| Time To Disable Slide Down | `timeToDisableSlideDown` | `float` | – | – |
| Slide Down If Input Not Pressed | `slideDownIfInputNotPressed` | `bool` | – | – |
| Disable Slide If Input Pressed Down | `disableSlideIfInputPressedDown` | `bool` | – | – |
| Disable Slide If Input Pressed Down2 5d | `disableSlideIfInputPressedDown2_5d` | `bool` | – | – |
| Use Input Press Up To Adhere To Surface | `useInputPressUpToAdhereToSurface` | `bool` | – | – |
| Slide Down If Input Pressed | `slideDownIfInputPressed` | `bool` | – | – |
| Slide Down If Input Pressed2 5d | `slideDownIfInputPressed2_5d` | `bool` | true | – |
| Use Double Tap Down To Stop Slide | `useDoubleTapDownToStopSlide` | `bool` | – | – |

### Speed Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slide Rotation Speed Third Person | `slideRotationSpeedThirdPerson` | `float` | 200 | – |
| Slide Rotation Speed First Person | `slideRotationSpeedFirstPerson` | `float` | 100 | – |
| Impulse On Jump | `impulseOnJump` | `Vector3` | – | – |
| Impulse On Jump2 5d | `impulseOnJump2_5d` | `Vector3` | new Vector3 (0, 15, -30) | – |
| Max Velocity Change Slide | `maxVelocityChangeSlide` | `float` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slider Can Be Used | `sliderCanBeUsed` | `bool` | true | – |
| Keep Weapons | `keepWeapons` | `bool` | – | – |
| Draw Weapons If Carried Previously | `drawWeaponsIfCarriedPreviously` | `bool` | – | – |

### Third Person Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Action ID | `actionID` | `int` | 08632946 | – |
| External Controlle Behavior Active Animator Name | `externalControlleBehaviorActiveAnimatorName` | `string` | "External Behavior Active" | – |
| Action ID Animator Name | `actionIDAnimatorName` | `string` | "Action ID" | – |
| Horizontal Animator Name | `horizontalAnimatorName` | `string` | "Horizontal Action" | – |
| Input Lerp Speed | `inputLerpSpeed` | `float` | 3 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Check If Detect Slide Active | `checkIfDetectSlideActive` | `bool` | – | – |
| Slide Active | `slideActive` | `bool` | – | – |
| Is First Person Active | `isFirstPersonActive` | `bool` | – | – |
| Current Vertical Movement | `currentVerticalMovement` | `float` | – | – |
| Current Horizontal Movement | `currentHorizontalMovement` | `float` | – | – |
| Slide Down Speed Multiplier | `slideDownSpeedMultiplier` | `float` | 1 | – |
| Force Slow Down On Surface Active | `forceSlowDownOnSurfaceActive` | `bool` | – | – |
| Carrying Weapons Previously | `carryingWeaponsPreviously` | `bool` | – | – |
| Slide Down In Process | `slideDownInProcess` | `bool` | – | – |
| Wall Jump Slide Paused | `wallJumpSlidePaused` | `bool` | – | – |
| Move Input | `moveInput` | `Vector3` | – | – |
| Local Move | `localMove` | `Vector3` | – | – |
| Use Double Tap Down To Stop Slide Active | `useDoubleTapDownToStopSlideActive` | `bool` | – | – |

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

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Player Camera Transform | `playerCameraTransform` | `Transform` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setSlideImpulseForce(Vector3 forceAmount, bool useCameraDirection)` | 指定力を最大速度変更量でクランプしてプレイヤーに設定し、`AddForce` で速度変更として加える。 |
| `setJumpActive(Vector3 newImpulseOnJumpAmount)` | スライド中なら解除し、上方向と前方向の合成インパルスでジャンプさせ、検出停止とジャンプ回転を行う。 |
| `setCheckIfDetectSlideActiveState(bool state)` | 壁スライド検出の有効/無効を切り替え、外部コントローラ設定と落下ダメージ保留を更新し、無効化時はスライドも解除する。 |
| `setSlideActiveState(bool state)` | スライド状態を切り替え、地上判定・アニメーションID・武器入力・カメラ・頭追従・状態変更イベントをまとめて更新する。 |
| `setSlideEnabledState(bool state)` | false ならスライドを解除してから `slideEnabled` を設定する。 |
| `setSlideCanBeUsedState(bool state)` | `sliderCanBeUsed` を設定するだけ。 |
| `setSliderEnabledState()` | 保存値 `originalSlideEnabled` を `setSlideEnabledState` に渡すだけ。 |
| `setOriginalSliderEnabledState()` | スライド中なら検出を止め、保存値 `originalSlideEnabled` を適用する。 |
| `setSlideDownSpeedMultiplier(float newValue)` | `slideDownSpeedMultiplier` を設定するだけ。 |
| `setForceSlowDownOnSurfaceActiveState(bool state)` | `forceSlowDownOnSurfaceActive` を設定するだけ。 |
| `enableCheckIfDetectSlideActiveStateExternally()` | 既に有効なら何もせず、`setCheckIfDetectSlideActiveState(true)` を呼ぶ。 |
| `disableCheckIfDetectSlideActiveStateExternally()` | 既に無効なら何もせず、`setCheckIfDetectSlideActiveState(false)` を呼ぶ。 |
| `checkEventsOnStateChange(bool state)` | 一人称か三人称かに応じて、開始/終了の対応イベントを送出する。 |
| `setWallJumpSlidePausedState(bool state)` | true かつスライド中なら解除し、`wallJumpSlidePaused` を設定する。 |
| `rotateCharacterOnJump()` | 既存の回転コルーチンを停止し、`rotateCharacterOnJumpCoroutine` を開始する。 |
| `rotateCharacterOnJumpCoroutine()` | カメラまたはプレイヤーの向きを反転させる目標へ Slerp で回転し、角度差か経過時間で終了する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartFirstPerson` | `UnityEvent` | – |
| `eventOnEndFirstPerson` | `UnityEvent` | – |
| `eventOnStartThirdPerson` | `UnityEvent` | – |
| `eventOnEndThirdPerson` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkIfResumeExternalControllerState()`, `disableExternalControllerState()`, `setCurrentPlayerActionSystemCustomActionCategoryID()`, `setExternalForceActiveState(bool state)`, `setExternalForceEnabledState(bool state)`, `setExtraImpulseForce(Vector3 forceAmount, bool useCameraDirection)`, `setJumpActiveForExternalForce()`, `updateControllerBehavior()`

</details>
