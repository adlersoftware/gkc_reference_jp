# bulletTimeFiringSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `OnAnimatorIKComponent`
- **ソース**: `Player/Extra Movements/bulletTimeFiringSystem.cs:6`

**概要**: バレットタイム中の射撃姿勢やジャンプ・起き上がり動作を扱う `OnAnimatorIKComponent`。移動状態に応じてアニメーション、起き上がり方向イベント、時間スケールを切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Movement Enabled | `movementEnabled` | `bool` | true | – |
| Look Direction Forward Offset | `lookDirectionForwardOffset` | `float` | 1000 | – |
| Time For Raising Hands | `timeForRaisingHands` | `float` | 0.5f | – |
| Only Active If Using Fire Weapons | `onlyActiveIfUsingFireWeapons` | `bool` | – | – |
| Body Weight Lerp Speed | `bodyWeightLerpSpeed` | `float` | 1 | – |

### Get Up Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Get Up After Delay On Ground | `getUpAfterDelayOnGround` | `bool` | – | – |
| Delay To Get Up On Ground | `delayToGetUpOnGround` | `float` | – | – |
| Min Wait To Check On Ground State | `minWaitToCheckOnGroundState` | `float` | – | – |

### Weapons Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Keep Weapons During Action | `keepWeaponsDuringAction` | `bool` | – | – |
| Draw Weapons After Action | `drawWeaponsAfterAction` | `bool` | – | – |
| Use Only When Using Fire Weapons | `useOnlyWhenUsingFireWeapons` | `bool` | – | – |

### Time Bullet Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Time Bullet | `useTimeBullet` | `bool` | – | – |
| Time Bullet Scale | `timeBulletScale` | `float` | 0.5f | – |
| Use Time Bullet Duration | `useTimeBulletDuration` | `bool` | – | – |
| Time Bullet Duration | `timeBulletDuration` | `float` | – | – |
| Use Events On Time Bullet | `useEventsOnTimeBullet` | `bool` | – | – |
| Event On Time Bullet Start | `eventOnTimeBulletStart` | `UnityEvent` | – | – |
| Event On Time Bullet End | `eventOnTimeBulletEnd` | `UnityEvent` | – | – |

### Time Bullet Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Unscaled Time On Animator | `setUnscaledTimeOnAnimator` | `bool` | – | – |
| Set Character Animation Speed | `setCharacterAnimationSpeed` | `bool` | – | – |
| Character Animation Speed | `characterAnimationSpeed` | `float` | 1.6f | – |

### Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Jump Force | `jumpForce` | `float` | – | – |
| Push Force | `pushForce` | `float` | – | – |
| Extra Speed On Fall | `extraSpeedOnFall` | `float` | – | – |
| Add Extra Speed On Fall Duration | `addExtraSpeedOnFallDuration` | `float` | – | – |
| Delay To Add Extra Speed On Fall | `delayToAddExtraSpeedOnFall` | `float` | – | – |

### Third Person Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Action ID | `actionID` | `int` | 323565 | – |
| Action ID With Roll | `actionIDWithRoll` | `int` | 323566 | – |
| Start Action With Roll | `startActionWithRoll` | `bool` | – | – |
| Roll On Start Duration | `rollOnStartDuration` | `float` | – | – |
| External Controlle Behavior Active Animator Name | `externalControlleBehaviorActiveAnimatorName` | `string` | "External Behavior Active" | – |
| Action ID Animator Name | `actionIDAnimatorName` | `string` | "Action ID" | – |
| Horizontal Animator Name | `horizontalAnimatorName` | `string` | "Horizontal Action" | – |
| Vertical Animator Name | `verticalAnimatorName` | `string` | "Vertical Action" | – |

### Third Person Camera State Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Camera State On Third Person | `setNewCameraStateOnThirdPerson` | `bool` | – | – |
| New Camera State On Third Person | `newCameraStateOnThirdPerson` | `string` | – | – |

### Action System Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Custom Action Category ID | `customActionCategoryID` | `int` | -1 | – |
| Regular Action Category ID | `regularActionCategoryID` | `int` | -1 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Movement Active | `movementActive` | `bool` | – | – |
| Arms IK Active | `armsIKActive` | `bool` | – | – |
| Current Time For Rising Hands | `currentTimeForRisingHands` | `float` | – | – |
| Current Arms Weight | `currentArmsWeight` | `float` | – | – |
| Arms Weight | `armsWeight` | `float` | 1 | – |
| Player Is Carrying Weapons | `playerIsCarryingWeapons` | `bool` | – | – |
| Look Direction Target | `lookDirectionTarget` | `Vector3` | – | – |
| Ground Detected After Jump | `groundDetectedAfterJump` | `bool` | – | – |
| Is Full Body Awareness Active | `isFullBodyAwarenessActive` | `bool` | – | – |
| Body Weight | `bodyWeight` | `float` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Start | `eventOnStart` | `UnityEvent` | – | – |
| Event On End | `eventOnEnd` | `UnityEvent` | – | – |
| Event On Get Up Forward | `eventOnGetUpForward` | `UnityEvent` | – | – |
| Event On Get Up Backward | `eventOnGetUpBackward` | `UnityEvent` | – | – |
| Event On Get Up Right | `eventOnGetUpRight` | `UnityEvent` | – | – |
| Event On Get Up Left | `eventOnGetUpLeft` | `UnityEvent` | – | – |
| Event On Get Up Forward From Back | `eventOnGetUpForwardFromBack` | `UnityEvent` | – | – |
| Event On Get Up Backward From Back | `eventOnGetUpBackwardFromBack` | `UnityEvent` | – | – |
| Event On Get Up Right From Back | `eventOnGetUpRightFromBack` | `UnityEvent` | – | – |
| Event On Get Up Left From Back | `eventOnGetUpLeftFromBack` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Player Input | `playerInput` | `playerInputManager` | – | – |
| Main Time Bullet | `mainTimeBullet` | `timeBullet` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setMovementActiveState(bool state)` | 移動状態を切り替え、開始時はジャンプと時間停止、終了時は方向別の起き上がりイベントを出す。 |
| `stopActivateJumpForcesCoroutine()` | ジャンプ力コルーチンを停止し、`jumpCoroutineActive` を false にする。 |
| `disableMovement()` | 移動中ならジャンプ力コルーチンを止め、フラグを戻して `setPlayerState(false)` を呼ぶ。 |
| `resetActionIdOnTimeBulletJump()` | `actionIDAnimatorID` の Animator 整数値を 0 にするだけ。 |
| `setCurrentPlayerActionSystemCustomActionCategoryID()` | 移動中は custom、そうでなければ regular のアクションカテゴリIDを、-1 より大きい場合のみ設定する。 |
| `inputSetTimeBullettFiring()` | `checkIfSetBulletTimeFiringState()` を呼ぶだけ。 |
| `checkEventOnStateChange(bool state)` | 開始なら `eventOnStart`、終了なら `eventOnEnd` を送出する。 |
| `setMovementEnabledState(bool state)` | `movementEnabled` を設定するだけ。 |
| `setMovementEnabledStateFromEditor(bool state)` | 値を設定してから `updateComponent` を呼ぶ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnTimeBulletStart` | `UnityEvent` | – |
| `eventOnTimeBulletEnd` | `UnityEvent` | – |
| `eventOnStart` | `UnityEvent` | – |
| `eventOnEnd` | `UnityEvent` | – |
| `eventOnGetUpForward` | `UnityEvent` | – |
| `eventOnGetUpBackward` | `UnityEvent` | – |
| `eventOnGetUpRight` | `UnityEvent` | – |
| `eventOnGetUpLeft` | `UnityEvent` | – |
| `eventOnGetUpForwardFromBack` | `UnityEvent` | – |
| `eventOnGetUpBackwardFromBack` | `UnityEvent` | – |
| `eventOnGetUpRightFromBack` | `UnityEvent` | – |
| `eventOnGetUpLeftFromBack` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`updateOnAnimatorIKState()`

</details>
