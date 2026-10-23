# playerLadderSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Ladder System/playerLadderSystem.cs:6`

**概要**: プレイヤー側のはしご制御。はしごトリガーに応じて検出状態・重力・カメラ・足音・入力を切り替え、昇降とジャンプ離脱を扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ladder Moovement Speed | `ladderMoovementSpeed` | `float` | 5 | – |
| Ladder Vertical Movement Amount | `ladderVerticalMovementAmount` | `float` | 0.3f | – |
| Ladder Horizontal Movement Amount | `ladderHorizontalMovementAmount` | `float` | 0.1f | – |
| Min Angle To Inverse Direction | `minAngleToInverseDirection` | `float` | 100 | – |
| Use Always Horizontal Movement On Ladder | `useAlwaysHorizontalMovementOnLadder` | `bool` | – | – |
| Use Always Local Movement Direction | `useAlwaysLocalMovementDirection` | `bool` | – | – |
| Min Angle Vertical Direction | `minAngleVerticalDirection` | `float` | 60 | – |
| Max Angle Vertical Direction | `maxAngleVerticalDirection` | `float` | 120 | – |
| Layer To Check Ladder End | `layerToCheckLadderEnd` | `LayerMask` | – | – |
| Climb Ladder Foot Step State Name | `climbLadderFootStepStateName` | `string` | "Climb Ladders" | – |

### FBA Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Use Simple Ladders On FBA | `canUseSimpleLaddersOnFBA` | `bool` | – | – |

### Jump Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Jump On Third Person Enabled | `jumpOnThirdPersonEnabled` | `bool` | – | – |
| Jump On First Person Enabled | `jumpOnFirstPersonEnabled` | `bool` | – | – |
| Impulse On Jump | `impulseOnJump` | `Vector3` | – | – |
| Impulse On Jump2 5d | `impulseOnJump2_5d` | `Vector3` | new Vector3 (0, 15, -30) | – |
| Jump Rotation Speed Third Person | `jumpRotationSpeedThirdPerson` | `float` | 1 | – |
| Jump Rotation Speed First Person | `jumpRotationSpeedFirstPerson` | `float` | 0.5f | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pause Input On Use Ladders Enabled | `pauseInputOnUseLaddersEnabled` | `bool` | – | – |
| Custom Input To Pause On Action Info List | `customInputToPauseOnActionInfoList` | `List<playerActionSystem.inputToPauseOnActionIfo>` | new List<playerActionSystem.inputToPa… | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Ladder Located | `ladderLocated` | `bool` | – | – |
| Ladder Found First Person | `ladderFoundFirstPerson` | `bool` | – | – |
| Ladder Found Third Person | `ladderFoundThirdPerson` | `bool` | – | – |
| Ladder End Detected | `ladderEndDetected` | `bool` | – | – |
| Ladder Start Detected | `ladderStartDetected` | `bool` | – | – |
| Movement Direction | `movementDirection` | `int` | – | – |
| Ladder Vertical Input | `ladderVerticalInput` | `float` | – | – |
| Ladder Horizontal Input | `ladderHorizontalInput` | `float` | – | – |
| Ladder Angle | `ladderAngle` | `float` | – | – |
| Ladder Signed Angle | `ladderSignedAngle` | `float` | – | – |
| Current Vertical Input | `currentVerticalInput` | `float` | – | – |
| Current Horizontal Input | `currentHorizontalInput` | `float` | – | – |
| Ladder Movement Direction | `ladderMovementDirection` | `Vector3` | – | – |
| Moving On Ladder | `movingOnLadder` | `bool` | – | – |
| Moving On Ladder Previously | `movingOnLadderPreviously` | `bool` | – | – |
| Ladder Direction Transform | `ladderDirectionTransform` | `Transform` | – | – |
| Ladder Raycast Direction Transform | `ladderRaycastDirectionTransform` | `Transform` | – | – |
| Moving On Ladder On FBA Active | `movingOnLadderOnFBAActive` | `bool` | – | – |
| Change View To FBA Active | `changeViewToFBAActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Third Person | `useEventsOnThirdPerson` | `bool` | – | – |
| Event On Located Ladder On Third Person | `eventOnLocatedLadderOnThirdPerson` | `UnityEvent` | – | – |
| Event On Removed Ladder On Third Person | `eventOnRemovedLadderOnThirdPerson` | `UnityEvent` | – | – |
| Use Events On Jump | `useEventsOnJump` | `bool` | – | – |
| Event On Jump | `eventOnJump` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | – |
| Player Camera Transform | `playerCameraTransform` | `Transform` | – | – |
| Player Pivot Transform | `playerPivotTransform` | `Transform` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Melee Weapons Grabbed Manager | `mainMeleeWeaponsGrabbedManager` | `meleeWeaponsGrabbedManager` | – | – |
| Main Player Input Manager | `mainPlayerInputManager` | `playerInputManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setLadderFoundState(bool state, ladderSystem newLadderSystem)` | `state`に応じて検出状態と現在のはしごを設定し、重力・接地判定・カメラ・足音を止めて昇降状態に切り替える。 |
| `setLadderDirectionTransform(Transform newLadderDirectionTransform, Transform newLadderRaycastDirectionTransform)` | `ladderDirectionTransform`と`ladderRaycastDirectionTransform`を設定するだけ。 |
| `setLadderHorizontalMovementState(bool state)` | `useLadderHorizontalMovement`を設定するだけ。 |
| `setMoveInLadderCenterState(bool state)` | `moveInLadderCenter`を設定するだけ。 |
| `isLadderFound()` | `ladderFoundFirstPerson`を返し、一人称ではしご上にいるかを示す。 |
| `setUseLocalMovementDirectionState(bool state)` | `useLocalMovementDirection`を設定するだけ。 |
| `checkLadderEventsOnThirdPerson(bool state)` | `useEventsOnThirdPerson`が有効なら、三人称でのはしご検出・解除イベントを発火する。 |
| `rotateCharacterOnJump()` | 既存の回転コルーチンを止め、逆向きに回すコルーチンを開始する。 |
| `rotateCharacterOnJumpCoroutine()` | 視点別の回転速度で、カメラまたは本体を正面と逆向きになるまで補間回転する。 |
| `checkEventOnJump()` | `useEventsOnJump`が有効なら、`eventOnJump`と現在のはしごのジャンプイベントを呼ぶ。 |
| `inputJumpFromLadder()` | はしご上にいる場合のみ`activeJumpOnLadder`を呼び、離脱ジャンプを実行する。 |
| `activeJumpOnLadder()` | 視点別の許可設定を確認し、`impulseOnJump`の力を加えてはしごからジャンプし回転を始める。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnLocatedLadderOnThirdPerson` | `UnityEvent` | – |
| `eventOnRemovedLadderOnThirdPerson` | `UnityEvent` | – |
| `eventOnJump` | `UnityEvent` | – |
