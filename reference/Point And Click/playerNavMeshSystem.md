# playerNavMeshSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Point And Click/playerNavMeshSystem.cs:12`

**概要**: ポイントアンドクリック移動を制御するコンポーネントで、画面クリックのレイキャストから目的地を決め、`NavMeshAgent`の経路計算と移動入力を`playerControllerManager`へ渡します。動的障害物回避、デバイス使用、ウェイポイント、追従対象の管理も行います。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Nav Mesh Enabled | `playerNavMeshEnabled` | `bool` | – | – |
| Layer To Press | `layerToPress` | `LayerMask` | – | – |
| Layer For Ground | `layerForGround` | `LayerMask` | – | – |
| Layer For Elements | `layerForElements` | `LayerMask` | – | – |
| Layer To Find Ground | `layerToFindGround` | `LayerMask` | – | – |
| Search Correct Surface On High Angle | `searchCorrectSurfaceOnHighAngle` | `bool` | – | – |
| Max Surface Angle | `maxSurfaceAngle` | `float` | 80 | – |
| Look At Target Speed | `lookAtTargetSpeed` | `float` | 15 | – |
| Target Change Tolerance | `targetChangeTolerance` | `float` | 1 | – |
| Min Distance To Friend | `minDistanceToFriend` | `float` | – | – |
| Min Distance To Enemy | `minDistanceToEnemy` | `float` | – | – |
| Min Distance To Objects | `minDistanceToObjects` | `float` | – | – |
| Min Distance To Surface | `minDistanceToSurface` | `float` | – | – |
| Max Distance To Recalculate Path | `maxDistanceToRecalculatePath` | `float` | 1 | – |
| Smooth Speed When Close To Target | `smoothSpeedWhenCloseToTarget` | `bool` | true | – |
| Update Nav Mesh Position Rate | `updateNavMeshPositionRate` | `float` | 0.5f | – |
| Calculate Path Rate | `calculatePathRate` | `float` | 0.5f | – |
| Use Double Click To Move Toward Devices | `useDoubleClickToMoveTowardDevices` | `bool` | – | – |
| Time Between Clicks | `timeBetweenClicks` | `float` | – | – |
| Debug Move Enabled | `debugMoveEnabled` | `bool` | true | – |
| Use Check Hover Point And Click Elements | `useCheckHoverPointAndClickElements` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Point And Click Panel | `usePointAndClickPanel` | `bool` | – | – |
| Disable Point And Click Panel On Surface Pressed | `disablePointAndClickPanelOnSurfacePressed` | `bool` | – | – |
| Point And Click Panel | `pointAndClickPanel` | `GameObject` | – | – |
| Use Element Info Text | `useElementInfoText` | `bool` | – | – |
| Element Info Text | `elementInfoText` | `Text` | – | – |
| Use Element Name Text | `useElementNameText` | `bool` | – | – |
| Element Name Text | `elementNameText` | `Text` | – | – |
| Use Device Buttons | `useDeviceButtons` | `bool` | – | – |
| Start Use Device Button | `startUseDeviceButton` | `GameObject` | – | – |
| Stop To Use Device Button | `stopToUseDeviceButton` | `GameObject` | – | – |
| Start Use Device Button Text | `startUseDeviceButtonText` | `Text` | – | – |
| Stop To Use Device Button Text | `stopToUseDeviceButtonText` | `Text` | – | – |
| Transform To Follow | `transformToFollow` | `Transform` | – | – |
| Particles In Transform To Follow | `particlesInTransformToFollow` | `GameObject` | – | – |
| Use Particles To Target Position | `useParticlesToTargetPosition` | `bool` | true | – |
| Cancel Action Name | `cancelActionName` | `string` | "Cancel" | – |
| Ignore Click On Level If UI Detected | `ignoreClickOnLevelIfUIDetected` | `bool` | – | – |
| UI To Ignore Click List | `UIToIgnoreClickList` | `List<GameObject>` | new List<GameObject> () | – |

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

### AI State (Debug)

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Target To Reach | `targetToReach` | `Transform` | – | – |
| Current Element To Use | `currentElementToUse` | `GameObject` | – | – |
| Inside A Device Element | `insideADeviceElement` | `bool` | – | – |
| Target Is Friendly | `targetIsFriendly` | `bool` | – | – |
| Target Is Object | `targetIsObject` | `bool` | – | – |
| Target Is Surface | `targetIsSurface` | `bool` | – | – |
| Nav Mesh Paused | `navMeshPaused` | `bool` | – | – |
| Attacking | `attacking` | `bool` | – | – |
| Following | `following` | `bool` | – | – |
| Waiting | `waiting` | `bool` | – | – |
| Hiding | `hiding` | `bool` | – | – |
| Following Target | `followingTarget` | `bool` | – | – |
| Checking To Resume Navmesh | `checkingToResumeNavmesh` | `bool` | – | – |
| On Ground | `onGround` | `bool` | – | – |
| Target Selected | `targetSelected` | `bool` | – | – |
| Player Is Using Device | `playerIsUsingDevice` | `bool` | – | – |
| Using Player Navmesh Externally | `usingPlayerNavmeshExternally` | `bool` | – | – |
| Nav Speed | `navSpeed` | `float` | 1 | – |
| Current Movement Direction | `currentMovementDirection` | `Vector3` | – | – |
| Current Min Distance | `currentMinDistance` | `float` | – | – |
| Use Custom Element Min Distance | `useCustomElementMinDistance` | `bool` | – | – |
| Custom Element Min Distance | `customElementMinDistance` | `float` | – | – |
| Looking Path After Jump | `lookingPathAfterJump` | `bool` | – | – |
| Obstacle On Forward | `obstacleOnForward` | `bool` | – | – |
| Obstacle On Right | `obstacleOnRight` | `bool` | – | – |
| Obstacle On Left | `obstacleOnLeft` | `bool` | – | – |
| Obstacle On Right Forward | `obstacleOnRightForward` | `bool` | – | – |
| Obstacle On Left Forward | `obstacleOnLeftForward` | `bool` | – | – |

### Waypoint State Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Min Distance To Next Point | `minDistanceToNextPoint` | `float` | 0.5f | – |
| Waypoint List Active | `waypointListActive` | `bool` | – | – |
| Waypoint List | `waypointList` | `List<Transform>` | new List<Transform> () | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Show Path Renderer | `showPathRenderer` | `bool` | true | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Camera Game Object | `playerCameraGameObject` | `GameObject` | – | – |
| Ray Cast Position | `rayCastPosition` | `Transform` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Devices Manager | `devicesManager` | `usingDevicesSystem` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Agent | `agent` | `NavMeshAgent` | – | – |
| Line Renderer | `lineRenderer` | `LineRenderer` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`がnullでなければ停止するだけ。 |
| `checkRaycastPositionWithVector3(Vector3 raycastPosition)` | 指定位置から真下向きのRayを作り、`checkRaycastPosition`へ渡して移動先判定を行わせる。 |
| `checkRaycastPosition(Ray newRay)` | ヒット位置から目的地と対象を決め、地面なら移動先設定、要素ならクリック処理を呼んで経路を計算する。 |
| `checkPointAndClickElementPressed()` | 押した`pointAndClickElement`の種類に応じて`setTargetType`を切り替え、デバイスなら移動先・使用対象・UI表示を設定し、経路計算を続けるかを返す。 |
| `setAgentDestination(Vector3 targetPosition)` | 前回から十分離れたか一定時間経過したときだけ`agent.SetDestination`を呼び、その後`agent`をプレイヤー位置へ合わせる。 |
| `updateCurrentNavMeshPath(Vector3 targetPosition)` | 目標が大きく動いたか経過時間を超えたときに経路を再計算して`pathCorners`を更新し、経路が見つかったかを返す。 |
| `setOnGroundState(bool state)` | `onGround`を代入するだけ。 |
| `getCurrentMovementDirection()` | `currentMovementDirection`を返すだけ。 |
| `moveNavMesh(Vector3 move, bool crouch, bool jump)` | 障害物検出と回避を反映した移動量を`AIMoveInput.moveInput`へ設定し、`crouch`と`jump`も渡してカメラを進行方向へ向ける。 |
| `pauseAI(bool state)` | `navMeshPaused`を設定し、停止時は`agent`を停止/無効化、再開時はコルーチンで再開し、経路表示も切り替える。 |
| `recalculatePath()` | `agent`が有効なら`agent.isStopped`をfalseにするだけ。 |
| `jumpStart()` | 本体が空で何もしない。 |
| `jumpEnded()` | `agent`を有効化して位置を合わせ、`lookingPathAfterJump`と`navMeshPaused`を解除する。 |
| `setTarget(Transform currentTarget)` | `targetToReach`を代入するだけ。 |
| `removeTarget()` | `targetToReach`をnullにし、追従/選択/種別フラグを解除して経路表示と対象パーティクルを消す。 |
| `setCanUseTargetParticlesState(bool state)` | `canUseTargetParticles`を代入するだけ。 |
| `lookAtTaget(bool state)` | `AIMoveInput.lookAtTarget`を設定し、対象を見るかどうかだけを切り替える。 |
| `setNewWaypointList(List<Transform> newList)` | `waypointList`を差し替え、空でなければ最寄りウェイポイントへの移動を開始し、空ならリストと`currentWayPoint`をクリアする。 |
| `closestWaypoint(Vector3 currentPosition)` | `waypointList`から指定位置に最も近いものを探して`currentPointIndex`を更新し、無ければnullを返す。 |
| `isCharacterAttacking()` | `attacking`を返すだけ。 |
| `isCharacterFollowing()` | `following`を返すだけ。 |
| `isCharacterWaiting()` | `waiting`を返すだけ。 |
| `isCharacterHiding()` | `hiding`を返すだけ。 |
| `setCharacterStates(bool attackValue, bool followValue, bool waitValue, bool hideValue)` | `attacking`/`following`/`waiting`/`hiding`の4フラグをまとめて設定するだけ。 |
| `setTargetType(bool isFriendly, bool isObject, bool isSurface)` | 対象種別の3フラグを設定し、`isFriendly`ならキャラクター状態もすべて解除する。 |
| `isFollowingTarget()` | `followingTarget`を返すだけ。 |
| `setShowCursorPausedState(bool state)` | `showCursorPaused`を代入するだけ。 |
| `setPlayerNavMeshEnabledState(bool state)` | ナビメッシュ有効状態を反映し、`agent`・移動/カメラ/ポーズマネージャー・カーソル表示を切り替え、必要なら更新コルーチンを起動する。 |
| `startToUseDevice()` | `currentElementToUse`を`devicesManager`で使用し、開始/停止ボタンと文言を更新、設定に応じてパネル非表示や要素削除を行う。 |
| `stopToUseDevice()` | 使用中デバイスがあれば`useDevice`で停止し、開始ボタン表示に戻すだけ。 |
| `disablePanelInfo()` | ポイントアンドクリックパネルを非表示にし、開始/停止ボタンを両方オフにするだけ。 |
| `setStartAndStopUseDeviceButtonsState(bool startState, bool stopState)` | 開始ボタンと停止ボタンの表示をそれぞれの値に合わせるだけ。 |
| `setPointAndClickDetectedState(bool state)` | `insideADeviceElement`を代入するだけ。 |
| `setPlayerTargetPosition(Vector3 targetPosition)` | 目的地とクリック時刻を設定し、`agent`で経路を計算して成功時のみ`targetToReach`を設定、失敗時は`agent`を無効化する。 |
| `enablePlayerNavmeshWithoutPointAndClick(bool state)` | ポーズやカーソル処理を伴わずにナビメッシュ・`agent`・移動/カメラ設定を切り替え、有効時に更新コルーチンを起動する。 |
| `setUsingPlayerNavmeshExternallyState(bool state)` | `usingPlayerNavmeshExternally`を代入するだけ。 |
| `setUseDynamicObstacleDetectionState(bool state)` | `useDynamicObstacleDetection`を代入するだけ。 |
| `setOriginalUseDynamicObstacleDetection()` | 保存しておいた`originalUseDynamicObstacleDetection`へ設定を戻すだけ。 |
| `isUsingPlayerNavmeshExternallyActive()` | `usingPlayerNavmeshExternally`を返すだけ。 |
| `isPlayerNavMeshEnabled()` | `playerNavMeshEnabled`を返すだけ。 |
| `enableCustomNavMeshSpeed(float newValue)` | `customNavMeshSpeed`に値を入れ、`useCustomNavMeshSpeed`をtrueにするだけ。 |
| `disableCustomNavMeshSpeed()` | `useCustomNavMeshSpeed`をfalseにするだけ。 |
| `enableCustomMinDistance(float newValue)` | `useCustomMinDistance`をtrueにし、`customMinDistance`に値`newValue`を入れるだけ。 |
| `disableCustomMinDistance()` | `useCustomMinDistance`をfalseにするだけ。 |
