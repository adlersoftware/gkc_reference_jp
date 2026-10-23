# AINavMesh

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/AINavMesh.cs:9`

**概要**: `NavMeshAgent`でAIキャラクターを移動させる中核コンポーネント。ターゲットや巡回地点の管理、経路計算、動的障害物回避、ジャンプ、パートナー追従、死亡・停止状態を扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Walk Speed | `walkSpeed` | `float` | 1 | – |
| Target Change Tolerance | `targetChangeTolerance` | `float` | 1 | – |
| Patrol Speed | `patrolSpeed` | `float` | – | – |
| Max Distance To Recalculate Path | `maxDistanceToRecalculatePath` | `float` | 1 | – |
| Smooth Speed When Close To Target | `smoothSpeedWhenCloseToTarget` | `bool` | true | – |
| Update Nav Mesh Position Rate | `updateNavMeshPositionRate` | `float` | 0.5f | – |
| Update Nav Mesh Position Rate2 5d | `updateNavMeshPositionRate2_5d` | `float` | 0.6f | – |
| Calculate Path Rate | `calculatePathRate` | `float` | 0.5f | – |
| Get Closest Position If Target Cant Be Reached | `getClosestPositionIfTargetCantBeReached` | `bool` | true | – |
| Ignore Look At Target Direction | `ignoreLookAtTargetDirection` | `bool` | – | – |
| Min Distance To Target Not Visible Multiplier | `minDistanceToTargetNotVisibleMultiplier` | `float` | 0.5f | – |
| Min Distance To Target Not Visible Clamp | `minDistanceToTargetNotVisibleClamp` | `float` | 1.5f | – |
| Use Min Distance Offset It Target Reached | `useMinDistanceOffsetItTargetReached` | `bool` | – | – |
| Current Distance To Target Offset | `currentDistanceToTargetOffset` | `float` | – | – |

### Regular Min Distances Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Min Distance To Friend | `minDistanceToFriend` | `float` | – | – |
| Min Distance To Enemy | `minDistanceToEnemy` | `float` | – | – |
| Min Distance To Objects | `minDistanceToObjects` | `float` | – | – |
| Min Distance To Move Back | `minDistanceToMoveBack` | `float` | – | – |

### Jump Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Off Mesh Link Jumps Enabled | `checkOffMeshLinkJumpsEnabled` | `bool` | true | – |
| Check Distance On Off Mesh Link | `checkDistanceOnOffMeshLink` | `bool` | – | – |
| Min Distance On Off Mesh Link | `minDistanceOnOffMeshLink` | `float` | – | – |
| Check Horizontal Distance On Off Mesh Link | `checkHorizontalDistanceOnOffMeshLink` | `bool` | – | – |
| Min Horizontal Distance On Off Mesh Link | `minHorizontalDistanceOnOffMeshLink` | `float` | – | – |
| Check Vertical Distance On Off Mesh Link | `checkVerticalDistanceOnOffMeshLink` | `bool` | – | – |
| Min Vertical Distance On Off Mesh Link | `minVerticalDistanceOnOffMeshLink` | `float` | – | – |
| Adjust Jump Power To Distance | `adjustJumpPowerToDistance` | `bool` | true | – |
| Regular Jump Power | `regularJumpPower` | `float` | 6 | – |
| Max Jump Power | `maxJumpPower` | `float` | 15 | – |
| Jump Multiplier Percentage | `jumpMultiplierPercentage` | `float` | 0.5f | – |

### Run From Target Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Min Distance To Run From Target | `minDistanceToRunFromTarget` | `float` | 10 | – |

### Inital Target Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Initial Target | `setInitialTarget` | `bool` | – | – |
| Initial Target Transform | `initialTargetTransform` | `Transform` | – | – |
| Set Main Player As Target | `setMainPlayerAsTarget` | `bool` | – | – |

### Partner Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add AI To Friend List Manager Event Name | `addAIToFriendListManagerEventName` | `string` | "Add AI To Friend List Manager" | – |
| Remove AI To Friend List Manager Event Name | `removeAIToFriendListManagerEventName` | `string` | "Remove AI From Friend List Manager" | – |
| Check To Leave Space To Partner | `checkToLeaveSpaceToPartner` | `bool` | – | – |
| Min Distance With Partner | `minDistanceWithPartner` | `float` | – | – |
| Max Distance To Return With Partner | `maxDistanceToReturnWithPartner` | `float` | – | – |
| Add AI As Player Partner | `addAIAsPlayerPartner` | `bool` | true | – |

### Guide Partner Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Max Distance To Partner When Guiding Him | `maxDistanceToPartnerWhenGuidingHim` | `float` | 10 | – |
| Target To Guide Out Of Range Lerp Speed | `targetToGuideOutOfRangeLerpSpeed` | `float` | 10 | – |
| Distance Offset To Set Guide Back To Range | `distanceOffsetToSetGuideBackToRange` | `float` | 1 | – |
| Return To Target To Guide When Out Of Range | `returnToTargetToGuideWhenOutOfRange` | `bool` | – | – |
| Max Distance To Return To Target To Guide | `maxDistanceToReturnToTargetToGuide` | `float` | – | – |

### Dynamic Obstacle Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Dynamic Obstacle Detection | `useDynamicObstacleDetection` | `bool` | – | – |
| Dynamic Obstacle Layer | `dynamicObstacleLayer` | `LayerMask` | – | – |
| Dynamic Avoid Speed | `dynamicAvoidSpeed` | `float` | 4 | – |
| Dynamic Raycast Distance Forward | `dynamicRaycastDistanceForward` | `float` | 3 | – |
| Dynamic Raycast Distance Diagonal | `dynamicRaycastDistanceDiagonal` | `float` | 0.5f | – |
| Dynamic Raycast Distance Sides | `dynamicRaycastDistanceSides` | `float` | 1 | – |
| Dynamic Raycast Distance Around | `dynamicRaycastDistanceAround` | `float` | 4 | – |
| Use Dynamic Obstacle When Target Is Enemy Enabled | `useDynamicObstacleWhenTargetIsEnemyEnabled` | `bool` | true | – |
| Check Custom List To Ignore On Dynamic Obstacle Enabled | `checkCustomListToIgnoreOnDynamicObstacleEnabled` | `bool` | – | – |
| Check For Extra Colliders On Owner If Detected | `checkForExtraCollidersOnOwnerIfDetected` | `bool` | – | – |
| Min Obstacle Rotation | `minObstacleRotation` | `float` | 45 | – |
| Medium Obstacle Rotation | `mediumObstacleRotation` | `float` | 65 | – |
| Maximum Obstacle Rotation | `maximumObstacleRotation` | `float` | 85 | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Pause AI | `eventToPauseAI` | `UnityEvent` | – | – |
| Event To Resume AI | `eventToResumeAI` | `UnityEvent` | – | – |
| Event On Partner Found | `eventOnPartnerFound` | `UnityEvent` | – | – |
| Event On Death | `eventOnDeath` | `UnityEvent` | – | – |
| Event On Alive | `eventOnAlive` | `UnityEvent` | – | – |

### AI State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Target | `currentTarget` | `Transform` | – | – |
| Target Is Friendly | `targetIsFriendly` | `bool` | – | – |
| Target Is Object | `targetIsObject` | `bool` | – | – |
| Nav Mesh Paused | `navMeshPaused` | `bool` | – | – |
| Patrolling | `patrolling` | `bool` | – | – |
| Patrolling Paused | `patrollingPaused` | `bool` | – | – |
| Attacking | `attacking` | `bool` | – | – |
| Following | `following` | `bool` | – | – |
| Waiting | `waiting` | `bool` | – | – |
| Hiding | `hiding` | `bool` | – | – |
| Following Target | `followingTarget` | `bool` | – | – |
| Using Sample Position | `usingSamplePosition` | `bool` | – | – |
| Checking To Resume Navmesh | `checkingToResumeNavmesh` | `bool` | – | – |
| On Ground | `onGround` | `bool` | – | – |
| Can Reach Current Target | `canReachCurrentTarget` | `bool` | – | – |
| Current Distance To Target | `currentDistanceToTarget` | `float` | – | – |
| Current Min Distance | `currentMinDistance` | `float` | – | – |
| Use Custom Min Distance | `useCustomMinDistance` | `bool` | – | – |
| Custom Min Distance | `customMinDistance` | `float` | – | – |
| Following Partner | `followingPartner` | `bool` | – | – |
| Partner Located | `partnerLocated` | `bool` | – | – |
| Leaving Space To Partner | `leavingSpaceToPartner` | `bool` | – | – |
| AI Dead | `AIDead` | `bool` | – | – |
| Move Nav Mesh Paused | `moveNavMeshPaused` | `bool` | – | – |
| Move Nav Mesh Paused During Action | `moveNavMeshPausedDuringAction` | `bool` | – | – |
| Nav Speed | `navSpeed` | `float` | 1 | – |
| Use Custom Nav Mesh Speed | `useCustomNavMeshSpeed` | `bool` | – | – |
| Custom Nav Mesh Speed | `customNavMeshSpeed` | `float` | – | – |
| Strafe Mode Active | `strafeModeActive` | `bool` | – | – |
| AI Move Input | `AIMoveInput` | `AINavMeshMoveInfo` | new AINavMeshMoveInfo () | – |
| Desired Velocity | `desiredVelocity` | `Vector3` | – | – |
| Use Half Min Distance | `useHalfMinDistance` | `bool` | – | – |
| Run From Target | `runFromTarget` | `bool` | – | – |
| Range To Target Reached | `rangeToTargetReached` | `bool` | – | – |
| Turn Based Combat Action Active | `turnBasedCombatActionActive` | `bool` | – | – |
| Locked2 5d Mode Active | `locked2_5dModeActive` | `bool` | – | – |
| Move In X Axis On2 5d Mode | `moveInXAxisOn2_5dMode` | `bool` | – | – |

### Dynamic Obstacle Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Obstacle On Forward | `obstacleOnForward` | `bool` | – | – |
| Obstacle On Right | `obstacleOnRight` | `bool` | – | – |
| Obstacle On Left | `obstacleOnLeft` | `bool` | – | – |
| Obstacle On Right Forward | `obstacleOnRightForward` | `bool` | – | – |
| Obstacle On Left Forward | `obstacleOnLeftForward` | `bool` | – | – |
| Number Of Obstacle Direction Detected | `numberOfObstacleDirectionDetected` | `int` | – | – |
| Obstacle Distance | `obstacleDistance` | `float` | – | – |
| Obstacle Detected | `obstacleDetected` | `bool` | – | – |
| Last Obstacle Detected | `lastObstacleDetected` | `GameObject` | – | – |
| Object List To Ignore On Dynamic Obstacle | `objectListToIgnoreOnDynamicObstacle` | `List<GameObject>` | new List<GameObject> () | – |

### Path Corners Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Path Corners | `pathCorners` | `List<Vector3>` | new List<Vector3> () | – |

### Guide Target Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Guiding Partner Active | `guidingPartnerActive` | `bool` | – | – |
| Partner To Guide On Range | `partnerToGuideOnRange` | `bool` | – | – |
| Current Distance To Partner To Guide | `currentDistanceToPartnerToGuide` | `float` | – | – |
| Returning To Target To Guide Active | `returningToTargetToGuideActive` | `bool` | – | – |
| Current Position Transform To Guide | `currentPositionTransformToGuide` | `Transform` | – | – |
| Temporal Target Position Transform | `temporalTargetPositionTransform` | `Transform` | – | – |

### Debug Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Dynamic Obstacle Debug Print | `showDynamicObstacleDebugPrint` | `bool` | – | – |
| Pause Movement To Target | `pauseMovementToTarget` | `bool` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Show Move Input Debug Print | `showMoveInputDebugPrint` | `bool` | – | – |
| Show Set Agent Destination Debug Print | `showSetAgentDestinationDebugPrint` | `bool` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Show Path Renderer | `showPathRenderer` | `bool` | – | – |

### Element Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Agent | `agent` | `NavMeshAgent` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | – |
| Ray Cast Position | `rayCastPosition` | `Transform` | – | – |
| AI Game Object | `AIGameObject` | `GameObject` | – | – |
| AI Transform | `AITransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `resetInitialTargetCheckedOnCharacterSpawn()` | `initialTargetChecked`を`false`に戻し、次回`Update`で初期ターゲット設定をやり直させる。 |
| `activateJumpExternally(float jumpDistance)` | `jumpDistance`に応じたジャンプ力を設定し、オフメッシュリンクを無効化して`moveNavMesh`にジャンプ入力を渡す。 |
| `setJumpPower(float newValue)` | `playerControllerManager.setJumpPower`を呼ぶだけ。 |
| `setOriginalJumpPower()` | `playerControllerManager.setOriginalJumpPower`を呼ぶだけ。 |
| `setAgentDestination(Vector3 targetPosition)` | 条件を満たした時だけ`agent.SetDestination`を呼び、目標位置と時刻を記録して`agent`の位置を`AITransform`に合わせる。 |
| `updateCurrentNavMeshPath(Vector3 targetPosition)` | 再計算条件を満たす時だけ`agent.CalculatePath`で経路を引き直して`pathCorners`を更新し、到達可否を返す。 |
| `setOnGroundState(bool state)` | `onGround`を設定するだけ。 |
| `isAIOnGround()` | `onGround`を返すだけ。 |
| `setLocked2_5dModeActiveState(bool state)` | `locked2_5dModeActive`を設定するだけ。 |
| `isLocked2_5dModeActive()` | `locked2_5dModeActive`を返すだけ。 |
| `setMoveInXAxisOn2_5dModeState(bool state)` | `moveInXAxisOn2_5dMode`を設定するだけ。 |
| `getCanReachCurrentTargetValue()` | `canReachCurrentTarget`を返すだけ。 |
| `getRemainingPathDistanceToTarget()` | 追従中で`pathCorners`が2点以上なら残り経路長を合計して返し、それ以外は-100を返す。 |
| `getCurrentDistanceToTarget()` | `currentDistanceToTarget`を返すだけ。 |
| `getMovementDirection()` | 先頭の`pathCorners`が0.1m以内なら削除し、次のコーナーへの正規化方向を返す（無ければゼロ）。 |
| `getCurrentMovementDirection()` | `currentMovementDirection`を返すだけ。 |
| `getDesiredVelocity()` | `desiredVelocity`を返すだけ。 |
| `setPauseMoveNavMeshState(bool state)` | `moveNavMeshPaused`を設定し、デバッグ時のみログを出す。 |
| `setMoveNavMeshPausedDuringActionState(bool state)` | `moveNavMeshPausedDuringAction`を設定するだけ。 |
| `setNavmeshPausedState(bool state)` | `navMeshPaused`を設定するだけ。 |
| `setCalculateMoveValueWithDirectionToTargetActiveState(bool state)` | `calculateMoveValueWithDirectionToTargetActive`を設定するだけ。 |
| `isCalculateMoveValueWithDirectionToTargetActive()` | `calculateMoveValueWithDirectionToTargetActive`を返すだけ。 |
| `updateUseExtraColliderListState()` | `playerControllerManager`から追加コライダーの使用状態と一覧、`mainCollider`を取得して保持する。 |
| `moveNavMesh(Vector3 moveInput, bool crouch, bool jump)` | 動的障害物のレイキャスト回避とガイド対象との距離補正を経て移動入力を決め、`AIMoveInput`を設定してコントローラとカメラを更新する。 |
| `setReverseMoveInputDirectionActiveState(bool state)` | `reverseMoveInputDirectionActive`を設定するだけ。 |
| `updateAIControllerInputValues()` | `playerControllerManager.Move`に`AIMoveInput`を渡すだけ。 |
| `updateAICameraInputValues()` | `playerCameraManager.Rotate`に`rayCastPosition.forward`を渡すだけ。 |
| `setAIWalkSpeed(float newValue)` | `walkSpeed`を設定するだけ。 |
| `setOriginalAIWalkSpeed(float newValue)` | 引数は使わず、保存済みの`originalAIWalkSpeed`を`setAIWalkSpeed`で戻すだけ。 |
| `setResetVerticalCameraRotationActiveState(bool state)` | `playerCameraManager.setResetVerticalCameraRotationActiveState`を呼ぶだけ。 |
| `setTurnBasedCombatActionActiveState(bool state)` | フラグを設定し、有効時はターゲット注視をオンにして移動入力をゼロにする。 |
| `pauseAI(bool state)` | `agent`の停止/再開と`eventToPauseAI`/`eventToResumeAI`の発火を行い、死亡中やターンバトル中の復帰は弾く。 |
| `setAIStateToDead()` | `AIDead`を立てて`eventOnDeath`を発火し、`reverseMoveInputDirectionActive`を解除する。 |
| `setAIStateToAlive()` | `AIDead`を下ろして`eventOnAlive`を発火し、`agent.Warp`で位置を同期する。 |
| `isAIDead()` | `AIDead`を返すだけ。 |
| `recalculatePath()` | `agent`が有効なら`isStopped`を`false`にするだけ。 |
| `jumpStart()` | 空の実装で何もしない。 |
| `jumpEnded()` | `agent`を有効化して`CompleteOffMeshLink`を呼び、停止状態とジャンプ追跡を解除して位置を同期する。 |
| `placeAIOnNewPosition(Vector3 newPosition)` | `AITransform`と`agent`を新しい位置へ移動して同期する。 |
| `setAINewRotation(Vector3 newRotation)` | `AITransform.eulerAngles`を設定するだけ。 |
| `setPatrolTarget(Transform newTarget)` | 巡回停止中なら何もせず、そうでなければ`setTarget`に委譲する。 |
| `setTarget(Transform newTarget)` | `currentTarget`を差し替え、到達判定をリセットして`checkStateOnSetTarget`を呼ぶ。 |
| `checkStateOnSetTarget()` | 空の仮想メソッドで、派生クラスでの拡張用。 |
| `getCurrentTarget()` | `currentTarget`を返すだけ。 |
| `avoidTarget(Transform targetToAvoid)` | `setTarget`で回避対象をターゲットに設定するだけ。 |
| `setAvoidTargetState(bool state)` | `runFromTarget`を設定するだけ。 |
| `removeTarget()` | `setTarget(null)`でターゲットを外すだけ。 |
| `recalculateSetAgentDestination()` | ターゲット位置にオフセットを加えて`agent`の目的地を強制再設定し、経路も再計算する。 |
| `resetCustomSpeedAndDistanceValues()` | カスタム速度とカスタム最小距離を無効化するだけ。 |
| `anyTargetToReach()` | `currentTarget`の有無を返すだけ。 |
| `setGuidingPartnerActiveState(bool state)` | フラグを設定し、有効時は現在のターゲットをガイド基準位置として保存する。 |
| `partnerFound(Transform currentPartner)` | パートナーを保存し、`setTarget`と`setPartnerFoundInfo`を呼ぶ。 |
| `setPartnerFoundInfo(Transform currentPartner)` | `partner`を保存して巡回を止め、`eventOnPartnerFound`とフレンドリスト追加のリモートイベントを発火する。 |
| `getCurrentPartner()` | `partner`を返すだけ。 |
| `setRemovePartnerPausedState(bool state)` | `removePartnerPausedState`を設定するだけ。 |
| `removeFromPartnerList()` | フレンドリスト登録が有効なら、`partnerRemoteEventSystem`経由で削除イベントを送る。 |
| `removePartner()` | パートナー登録を解除し、ターゲットがパートナーなら外して関連フラグを下ろす。 |
| `lookAtTaget(bool state)` | `ignoreLookAtTargetDirection`でなければ`AIMoveInput.lookAtTarget`を設定する。 |
| `getAgent()` | `agent`を返すだけ。 |
| `setStrafeModeActiveState(bool state)` | `AIMoveInput.strafeModeActive`を設定するだけ。 |
| `setPatrolState(bool state)` | `patrolling`を設定するだけ。 |
| `setPatrolPauseState(bool state)` | `patrollingPaused`を設定するだけ。 |
| `isPatrolPaused()` | `patrollingPaused`を返すだけ。 |
| `isPatrolling()` | `patrolling`を返すだけ。 |
| `setPatrolSpeed(float value)` | `patrolSpeed`を設定するだけ。 |
| `attack(Transform newTarget)` | ターゲットを設定し、攻撃状態のみを有効にする。 |
| `follow(Transform newTarget)` | 追従フラグを立ててターゲットを設定し、追従状態のみを有効にする。 |
| `wait(Transform newTarget)` | 引数は使わずターゲットを外し、待機状態のみを有効にする。 |
| `hide(Transform newTarget)` | ターゲットを設定し、隠れ状態のみを有効にする。 |
| `setFollowingTargetState(bool state)` | `followingTarget`を設定するだけ。 |
| `isCharacterAttacking()` | `attacking`を返すだけ。 |
| `isCharacterFollowing()` | `following`を返すだけ。 |
| `isCharacterWaiting()` | `waiting`を返すだけ。 |
| `isCharacterHiding()` | `hiding`を返すだけ。 |
| `isPartnerLocated()` | `partnerLocated`を返すだけ。 |
| `setCharacterStates(bool attackValue, bool followValue, bool waitValue, bool hideValue)` | 攻撃・追従・待機・隠れの4フラグをまとめて設定するだけ。 |
| `setTargetType(bool isFriendly, bool isObject)` | ターゲット種別を設定し、フレンド時はキャラクター状態を全て解除する。 |
| `setExtraMinDistanceState(bool state, float extraDistance)` | `state`に応じて味方/敵の最小距離に`extraDistance`を加算し、解除時は元の値へ戻す。 |
| `isFollowingTarget()` | `followingTarget`を返すだけ。 |
| `isUseHalfMinDistanceActive()` | `useHalfMinDistance`を返すだけ。 |
| `startOverride()` | `overrideTurretControlState(true)`を呼ぶだけ。 |
| `stopOverride()` | `overrideTurretControlState(false)`を呼ぶだけ。 |
| `overrideTurretControlState(bool state)` | `pauseAI`に委譲するだけ。 |
| `setDistanceToEnemy(float newDistance)` | `minDistanceToEnemy`とその元値を同じ値に設定する。 |
| `setUseDynamicObstacleDetectionState(bool state)` | `useDynamicObstacleDetection`を設定するだけ。 |
| `setOriginalUseDynamicObstacleDetection()` | 保存済みの`originalUseDynamicObstacleDetection`に戻すだけ。 |
| `addObjectToIgnoreOnDynamicObstacle(GameObject newObject)` | カスタム除外リストが有効なら、`objectListToIgnoreOnDynamicObstacle`に追加してnullを除去する。 |
| `removeObjectToIgnoreOnDynamicObstacle(GameObject newObject)` | カスタム除外リストが有効なら、対象を`objectListToIgnoreOnDynamicObstacle`から削除する。 |
| `setMinObstacleRotation(float newValue)` | `minObstacleRotation`を設定するだけ。 |
| `setMediumObstacleRotation(float newValue)` | `mediumObstacleRotation`を設定するだけ。 |
| `setMaximumObstacleRotation(float newValue)` | `maximumObstacleRotation`を設定するだけ。 |
| `enableCustomNavMeshSpeed(float newValue)` | `customNavMeshSpeed`を設定してカスタム速度の使用を有効化する。 |
| `disableCustomNavMeshSpeed()` | `useCustomNavMeshSpeed`を`false`にするだけ。 |
| `enableCustomMinDistance(float newValue)` | カスタム最小距離を有効化し`customMinDistance`を設定する。 |
| `enableHalfMinDistance()` | `useHalfMinDistance`を`true`にするだけ。 |
| `disableCustomMinDistance()` | `useCustomMinDistance`を`false`にするだけ。 |
| `setIgnoreGetClosestPositionIfTargetCantBeReachedState(bool state)` | `ignoreGetClosestPositionIfTargetCantBeReached`を設定するだけ。 |
| `setUseMinDistanceOffsetItTargetReachedState(bool state)` | `useMinDistanceOffsetItTargetReached`を設定するだけ。 |
| `setCheckCustomListToIgnoreOnDynamicObstacleEnabledState(bool state)` | `checkCustomListToIgnoreOnDynamicObstacleEnabled`を設定するだけ。 |
| `setCheckForExtraCollidersOnOwnerIfDetectedState(bool state)` | `checkForExtraCollidersOnOwnerIfDetected`を設定するだけ。 |
| `setCheckCustomListToIgnoreOnDynamicObstacleEnabledStateFromEditor(bool state)` | 設定を反映したうえで`updateComponent`を呼び、シーンをダーティにする。 |
| `setCheckForExtraCollidersOnOwnerIfDetectedStateFromEditor(bool state)` | 設定を反映したうえで`updateComponent`を呼び、シーンをダーティにする。 |
| `setMinDistanceToEnemyFromEditor(float newDistance)` | `minDistanceToEnemy`を設定してから`updateComponent`を呼ぶ。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`を呼ぶだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToPauseAI` | `UnityEvent` | – |
| `eventToResumeAI` | `UnityEvent` | – |
| `eventOnPartnerFound` | `UnityEvent` | – |
| `eventOnDeath` | `UnityEvent` | – |
| `eventOnAlive` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`Start()`

</details>
