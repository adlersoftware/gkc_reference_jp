# playerActionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Action System/playerActionSystem.cs:6`

**概要**: プレイヤー側でアクションの開始/終了を管理し、入力停止・カメラ・アニメーション・イベント・コルーチンを制御する中核コンポーネント。カスタムアクションは名前やカテゴリから起動でき、待機リストや破棄/削除の後処理も扱う。

**公式ドキュメント抜粋**（[Tutorial - Add Action System By Input](../../docs/quick-start/tutorials/tutorial-add-action-system-by-input.md)）

> Youtube Tutorial Add a new action on the input and configure the event to activate the animation action by going clicking on the root of the prefab (Player and Game Management), then the Input Manager component. Scroll down to the section Multi-Input List and open the Multi Axes List menu. Then open Player Controller in the Multi-Input List and select Add Action to add a new one. In this tutorial, we’ll be creating the action, Simple Kick. You can also put a Keyboard and/or Joystick input to activate the action here. Next, navigate to the Player Controller game object on the player character and scroll down to the Player Input Manager. Then scroll down to Multi Axes List and select the Player Controller section as we did on the Player and Game Management component. Click Add Action as before, except now on the Axe dropdown, you will see the Simple Kick Action we made. Select that. Set th…

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Action Active Animator Name | `actionActiveAnimatorName` | `string` | "Action Active" | – |
| Action ID Animator Name | `actionIDAnimatorName` | `string` | "Action ID" | – |
| Action Active Upper Body Animator Name | `actionActiveUpperBodyAnimatorName` | `string` | "Action Active Upper Body" | – |
| Horizontal Animator Name | `horizontalAnimatorName` | `string` | "Horizontal Action" | – |
| Vertical Animator Name | `verticalAnimatorName` | `string` | "Vertical Action" | – |
| Raw Horizontal Animator Name | `rawHorizontalAnimatorName` | `string` | "Raw Horizontal Action" | – |
| Raw Vertical Animator Name | `rawVerticalAnimatorName` | `string` | "Raw Vertical Action" | – |
| Last Horizontal Direction Animator Name | `lastHorizontalDirectionAnimatorName` | `string` | "Last Horizontal Direction" | – |
| Last Vertical Direction Animator Name | `lastVerticalDirectionAnimatorName` | `string` | "Last Vertical Direction" | – |
| Disable Has Exit Time Animator Name | `disableHasExitTimeAnimatorName` | `string` | "Disable Has Exit Time State" | – |
| Input Lerp Speed | `inputLerpSpeed` | `float` | 0.1f | – |
| Actions Layer Index | `actionsLayerIndex` | `int` | – | – |
| Custom Action States Enabled | `customActionStatesEnabled` | `bool` | true | – |
| Change Camera View To Third Person On Action On Any Action | `changeCameraViewToThirdPersonOnActionOnAnyAction` | `bool` | – | – |

### Action State Info Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Action State Info List | `actionStateInfoList` | `List<actionStateInfo>` | new List<actionStateInfo> () | – |

### Custom Action State Info Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Custom Action Category ID | `currentCustomActionCategoryID` | `int` | 0 | – |
| Explanation | `explanation` | `string` | "After adding, removing or modifying … | TextArea (3, 20) |
| Custom Action State Category Info List | `customActionStateCategoryInfoList` | `List<customActionStateCategoryInfo>` | new List<customActionStateCategoryInf… | – |

### Player Input To Pause During Action Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pause Input List During Action Active Always | `pauseInputListDuringActionActiveAlways` | `bool` | true | – |
| Input To Pause On Action Ifo List | `inputToPauseOnActionIfoList` | `List<inputToPauseOnActionIfo>` | new List<inputToPauseOnActionIfo> () | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Initial Action System | `setInitialActionSystem` | `bool` | – | – |
| Initial Action System To Set | `initialActionSystemToSet` | `actionSystem` | – | – |
| Use Initial Custom Action Name | `useInitialCustomActionName` | `bool` | – | – |
| Initial Custom Action Name | `initialCustomActionName` | `string` | – | – |
| Check If Action Takes Longer Duration To Resume | `checkIfActionTakesLongerDurationToResume` | `bool` | – | – |
| Max Wait To Resume If Animation Takes Longer Duration | `maxWaitToResumeIfAnimationTakesLongerDuration` | `float` | 0.8f | – |
| Raycast Distance | `raycastDistance` | `float` | 2 | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Start Action | `eventOnStartAction` | `UnityEvent` | – | – |
| Event On End Action | `eventOnEndAction` | `UnityEvent` | – | – |
| Use Event On Action Detected | `useEventOnActionDetected` | `bool` | – | – |
| Event On Action Detected | `eventOnActionDetected` | `UnityEvent` | – | – |
| Event Before Start Action | `eventBeforeStartAction` | `UnityEvent` | – | – |
| Event After End Action | `eventAfterEndAction` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Show Debug Print Custom Action Activated | `showDebugPrintCustomActionActivated` | `bool` | – | – |
| Action Found | `actionFound` | `bool` | – | – |
| Action Active | `actionActive` | `bool` | – | – |
| Playing Animation | `playingAnimation` | `bool` | – | – |
| Current Action Info Index | `currentActionInfoIndex` | `int` | – | – |
| Waiting For Next Player Input | `waitingForNextPlayerInput` | `bool` | – | – |
| Action Movement Input Active | `actionMovementInputActive` | `bool` | – | – |
| Horizontal Input | `horizontalInput` | `float` | – | – |
| Vertical Input | `verticalInput` | `float` | – | – |
| Raw Horizontal Input | `rawHorizontalInput` | `int` | – | – |
| Raw Vertical Input | `rawVerticalInput` | `int` | – | – |
| Axis Values | `axisValues` | `Vector2` | – | – |
| Raw Axis Values | `rawAxisValues` | `Vector2` | – | – |
| Current Animation Checked | `currentAnimationChecked` | `bool` | – | – |
| Start Action | `startAction` | `bool` | – | – |
| Carrying Weapons Previously | `carryingWeaponsPreviously` | `bool` | – | – |
| Using Powers Previosly | `usingPowersPreviosly` | `bool` | – | – |
| Aiming Weapons Prevously | `aimingWeaponsPrevously` | `bool` | – | – |
| Check Conditions Active | `checkConditionsActive` | `bool` | – | – |
| Current Custom Action Name | `currentCustomActionName` | `string` | – | – |
| Custom Action Active | `customActionActive` | `bool` | – | – |
| Action Found Waiting To Player Resume | `actionFoundWaitingToPlayerResume` | `bool` | – | – |
| Current Walk Direction | `currentWalkDirection` | `Vector3` | – | – |
| Walking To Direction Active | `walkingToDirectionActive` | `bool` | – | – |
| Current Action Name | `currentActionName` | `string` | – | – |
| Ignore Input Change Active | `ignoreInputChangeActive` | `bool` | – | – |
| Current Action Duration | `currentActionDuration` | `float` | – | – |
| Rotating Toward Facing Direction | `rotatingTowardFacingDirection` | `bool` | – | – |
| Moving Player To Position Target Active | `movingPlayerToPositionTargetActive` | `bool` | – | – |
| Use Position To Adjust Player Active | `usePositionToAdjustPlayerActive` | `bool` | – | – |
| Wait To Play Animation After Adjust Position Active | `waitToPlayAnimationAfterAdjustPositionActive` | `bool` | – | – |
| Current Action Info | `currentActionInfo` | `actionSystem.actionInfo` | – | – |
| Current Action System Transform | `currentActionSystemTransform` | `Transform` | – | – |
| Current Action System Game Object | `currentActionSystemGameObject` | `GameObject` | – | – |
| Action Found Waiting Resume | `actionFoundWaitingResume` | `actionSystem` | – | – |
| Action System List Stored To Play | `actionSystemListStoredToPlay` | `List<actionSystem>` | new List<actionSystem> () | – |
| Custom Action State Info Dictionary List | `customActionStateInfoDictionaryList` | `List<customActionStateInfoDictionary>` | new List<customActionStateInfoDiction… | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Collider | `mainCollider` | `Collider` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Main Headbob | `mainHeadbob` | `headBob` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |
| Main Player Input Manager | `mainPlayerInputManager` | `playerInputManager` | – | – |
| Main IK Foot System | `mainIKFootSystem` | `IKFootSystem` | – | – |
| Main Hands On Surface IK System | `mainHandsOnSurfaceIKSystem` | `handsOnSurfaceIKSystem` | – | – |
| Main Remote Event System | `mainRemoteEventSystem` | `remoteEventSystem` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Other Powers | `mainOtherPowers` | `otherPowers` | – | – |
| Main Using Devices System | `mainUsingDevicesSystem` | `usingDevicesSystem` | – | – |
| Main Player Nav Mesh System | `mainPlayerNavMeshSystem` | `playerNavMeshSystem` | – | – |
| Main AI Navmesh | `mainAINavmesh` | `AINavMesh` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main Health | `mainHealth` | `health` | – | – |
| Main Shared Action System | `mainSharedActionSystem` | `sharedActionSystem` | – | – |
| Main Shared Action Button Activator | `mainSharedActionButtonActivator` | `sharedActionButtonActivator` | – | – |
| Main Shared Action System Remote Activator | `mainSharedActionSystemRemoteActivator` | `sharedActionSystemRemoteActivator` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getCurrentActionDuration()` | 非アクティブなら0を返し、それ以外は`currentActionInfo`の再生時間を速度とAnimator倍率で補正して`delayToPlayAnimation`を足した値を返す。 |
| `setReadInputValuesForActionSystemActiveState(bool state)` | 毎フレーム入力を読むかどうかの`readInputValuesForActionSystemActiveState`を設定するだけ。 |
| `getInputValuesForActionSystem()` | 移動軸と生軸の入力値を読み、水平/垂直入力と最終方向を更新してからAnimatorパラメータへ反映する。 |
| `updateAnimatorParemeters()` | `currentCustomActionCategoryID`が0のとき、水平/垂直入力と最終方向をAnimatorのfloat/intパラメータへ補間設定する。 |
| `setPlayerActionActive(actionSystem newActionSystem)` | 再生中なら中断可否を判定して待機させ、`currentActionSystem`と`currentActionInfo`を差し替え、条件を満たせば`playAnimation`を呼ぶ。 |
| `checkConditionsToPlayAnimation()` | `actionFound`と`currentActionInfo`が有効で、開始条件がある場合はプレイヤーが移動中かを確認して再生可否を返す。 |
| `setPlayerActionDeactivate(actionSystem newActionSystem)` | 非アクティブ時のみ、待機リストと`actionFoundWaitingResume`から対象アクションを除き`actionFound`をfalseにする。 |
| `setPlayerActionDeactivate()` | 非アクティブ時のみ`actionFound`をfalseにするだけ。 |
| `playAnimation()` | 一人称可否としゃがみを処理して開始イベントを送り、`activateAnimation`か歩行を開始し、AI停止とアクション開始イベントを呼ぶ。 |
| `stopPlayAnimationCoroutine()` | 再生コルーチン`animationCoroutine`を停止するだけ。 |
| `activateAnimation()` | 再生コルーチンを開始して`pausePlayer`で状態を止め、移動先指定があれば`movePlayerToPositionTarget`も呼ぶ。 |
| `checkSetActionState()` | `setActionState`が有効なとき`actionStateName`に一致する`actionStateInfoList`の有効化/無効化イベントを発火する。 |
| `isRotatingTowardFacingDirection()` | `rotatingTowardFacingDirection`(向き変更中か)を返すだけ。 |
| `isPlayerWalkingToDirectionActive()` | `walkingToDirectionActive`(歩行移動中か)を返すだけ。 |
| `isActionActive()` | `actionActive`を返すだけ。 |
| `isPlayerMovingOn3dWorld()` | `mainPlayerController`へ委譲し、3Dワールド上で移動中かを返す。 |
| `isUsePositionToAdjustPlayerActive()` | `usePositionToAdjustPlayerActive`を返すだけ。 |
| `setWaitToPlayAnimationAfterAdjustPositionActiveState(bool state)` | `waitToPlayAnimationAfterAdjustPositionActive`を設定するだけ。 |
| `stopSetPlayerWalkState()` | 歩行コルーチン`playerWalkCoroutine`を停止し、歩行中と向き変更中のフラグをfalseにする。 |
| `setPlayerWalkState(bool playAnimationAtEnd)` | 歩行コルーチンを開始し、`playAnimationAtEnd`がtrueなら歩行終了後にアニメーション再生へ移る。 |
| `matchTarget(Vector3 matchPosition, Quaternion matchRotation, AvatarTarget target, MatchTargetWeightMask weightMask, float normalisedStartTime, float normalisedEndTime)` | マッチ中か遷移中なら中断し、現在の正規化時間が終了時間を超えていなければ`mainAnimator.MatchTarget`を実行する。 |
| `forcePlayCurrentAnimation(int newCurrentActionInfoIndex)` | 指定インデックスを`currentActionInfoIndex`に入れて`waitingForNextPlayerInput`をtrueにし、`playCurrentAnimation`を呼ぶ。 |
| `playCurrentAnimation()` | `actionFound`時に入力や外部イベントで再生可能な条件を満たせば、情報を切り替えて`playAnimation`を呼ぶ。 |
| `canPlayAnimation()` | ラグドール・接地・しゃがみ・最小距離・最小角度などの条件を確認し、アニメーションを再生できるかを返す。 |
| `stopCheckActionEventInfoList()` | イベント発生コルーチン`eventInfoListCoroutine`を停止するだけ。 |
| `checkActionEventInfoList()` | `useEventInfoList`が有効なら、遅延付きでイベントを発火するコルーチンを再起動する。 |
| `stopCheckKillOrEnterOnRagdollState()` | 死亡/ラグドール化コルーチン`killOrEnterOnRagdollStateCoroutine`を停止するだけ。 |
| `checkKillOrEnterOnRagdollState()` | `killCharacter`か`activateCharacterRagdoll`が有効なら、遅延を伴う死亡・ラグドール化コルーチンを開始する。 |
| `stopCheckSetObjectParent()` | 親子付けコルーチン`objectParentCoroutine`を停止するだけ。 |
| `checkSetObjectParent()` | `setObjectParent`が有効なら、`waitTimeToParentObject`だけ待ってから指定オブジェクトをボーンへ親子付けするコルーチンを開始する。 |
| `setActionMovementInputActiveState(bool state)` | `actionMovementInputActive`を設定するだけ。 |
| `setLastHorizontalDirectionValue(int newValue)` | `lastHorizontalDirection`を設定するだけ。 |
| `setLastVerticalDirectionValue(int newValue)` | `lastVerticalDirection`を設定するだけ。 |
| `updateLastDirectionValues()` | 最後の水平/垂直方向をAnimatorのintパラメータへ書き込むだけ。 |
| `forceActivateCustomAction(string actionName)` | `waitingForNextPlayerInput`をtrueにしてから`activateCustomAction`を呼び、待機中の入力を消費させる。 |
| `setActivateCustomActionsPausedState(bool state)` | 他カスタムアクションの起動を止める`activateCustomActionsPaused`を設定するだけ。 |
| `activateCustomActionByCategoryName(string categoryName)` | カテゴリ名が一致するアクションを探し、ランダム判定で1つ選んで`activateCustomAction`へ渡す。 |
| `activateCustomAction(string actionName)` | 名前から対象を引き状態やカメラ/カテゴリ条件と確率を確認して中断設定を反映し、`checkCustomActionToActivate`と`playCurrentAnimation`を実行する。 |
| `checkCustomActionToActivate(int currentCategoryIndex, int currentActionIndex)` | ランダムリストやしゃがみ/空中/移動時の代替から実際に使う`actionSystem`を選んで起動し、`customActionActive`をtrueにする。 |
| `stopCustomActionIfCurrentlyActive(string actionName)` | 現在再生中のアクションと一致する場合のみ停止するフラグを立てて`stopCustomAction`を呼ぶ。 |
| `stopCustomAction(string actionName)` | 名前から対象を引き条件を満たせば待機リストから外し、`resumePlayer`と停止イベント、破棄/削除チェックを行う。 |
| `pausePlayer()` | `actionActive`をtrueにして入力・カメラ・頭トラッキング・武器などを止め、開始イベントを送って`pausePlayerActivated`を立てる。 |
| `clearActionSystemListStoredToPlay()` | `actionSystemListStoredToPlay`を空にするだけ。 |
| `stopAllActions()` | 再生中なら各種コルーチンを止め、カスタムアクションか`resumePlayer`で終了処理と破棄/削除チェックを行う。 |
| `resetAllActionStates()` | `actionActive`や`currentActionSystem`などアクション関連の実行時状態をすべて初期値へ戻す。 |
| `checkIfPauseInputListDuringActionActive(bool state)` | アクション設定とフラグを確認し、入力を止める/戻す処理を`checkInputListToPauseDuringAction`へ渡す。 |
| `checkInputListToPauseDuringAction(List<inputToPauseOnActionIfo> inputList, bool state)` | `ignoreInputChangeActive`なら何もせず、stateに応じて各入力の有効状態を保存して停止、または復元する。 |
| `updateCurrentInputList()` | `inputToPauseOnActionIfoList`の各入力について現在の有効状態を`previousActiveState`へ保存する。 |
| `setIgnoreInputChangeActiveState(bool state)` | `ignoreInputChangeActive`を設定するだけ。 |
| `resumePlayer()` | `actionActive`をfalseに戻して終了イベントを送り、入力・カメラ・移動・武器・体力などを復元する。 |
| `removeActionFoundWaitingToPlayerResume()` | `actionFoundWaitingToPlayerResume`をfalseにし`actionFoundWaitingResume`をnullにするだけ。 |
| `checkDestroyAction()` | `destroyActionOnEnd`が有効なら`actionSystem`を破棄し、現在のアクション情報をクリアする。 |
| `checkRemoveAction()` | `removeActionOnEnd`が有効ならプレイヤーをリストから外し、次のアクション起動か待機リストの再生を行う。 |
| `checkIfEventOnStopAction()` | 停止時イベントと`resumeAIOnActionEnd`によるAI再開、停止時に呼ぶイベントリストの実行を行う。 |
| `enableCustomActionByName(string actionName)` | `enableOrDisableCustomActionByName`をtrueで呼ぶだけ。 |
| `disableCustomActionByName(string actionName)` | `enableOrDisableCustomActionByName`をfalseで呼ぶだけ。 |
| `enableOrDisableCustomActionByName(string actionName, bool state)` | 名前からアクションを引いて`stateEnabled`を設定し、見つからなければ何もしない。 |
| `setCustomActionTransform(string actionName, Transform newTransform)` | 名前からアクションを引き、ランダムリストやカテゴリ別の`actionSystem`へ`newTransform`を`actionTransform`として設定する。 |
| `getCurrentActionName()` | `currentActionName`を返すだけ。 |
| `getCurrentActionCategoryActive()` | `currentActionCategoryActive`を返すだけ。 |
| `getCurrentActionSystem()` | `currentActionSystem`を返すだけ。 |
| `setNewActionIDExternally(int newID)` | `actionIDAnimatorID`へ`newID`をAnimatorのintとして設定するだけ。 |
| `setActionActiveExternally(bool state)` | `actionActiveAnimatorID`へ`state`をAnimatorのboolとして設定するだけ。 |
| `setCurrentCustomActionCategoryID(int newValue)` | `currentCustomActionCategoryID`を設定するだけ。 |
| `checkChangeOfView(bool isFirstPerson)` | 一人称なら何もせず、三人称なら`mainPlayerController.resetAnimator`を呼ぶ。 |
| `inputPlayCurrentAnimation()` | 使用中デバイスとして登録されていれば`playCurrentAnimation`を呼び、そうでなければ何もしない。 |
| `inputPlayCurrentAnimationWithoutCheckingIfExistsOnaDeviceList()` | デバイスリストを確認せず、`currentActionSystemGameObject`があれば`playCurrentAnimation`を呼ぶ。 |
| `inputCheckIfResumePlayerOnJump()` | アクション中かつ`jumpCanResumePlayer`なら`stopAllActions`で終了し、ジャンプを有効にする。 |
| `getSharedActionSystem()` | `mainSharedActionSystem`を返すだけ。 |
| `getSharedActionButtonActivator()` | `mainSharedActionButtonActivator`を返すだけ。 |
| `getSharedActionSystemRemoteActivator()` | `mainSharedActionSystemRemoteActivator`を返すだけ。 |
| `isSharedActionActive()` | 共有アクションシステムがあればその`isSharedActionActive`を返し、なければfalseを返す。 |
| `isPlayerAlive()` | `mainPlayerController`が死亡していないかを返す。 |
| `addNewActionFromEditor(actionSystem newActionSystem, string newActionCategoryName, string actionSystemName, bool updateActionListActive, string actionCategory)` | 指定カテゴリ(なければOthers)へ新しい`customActionStateInfo`を追加し、必要なら`updateActionList`を呼んで成否を返す。 |
| `setNewInfoOnAction(string newActionCategoryName, string originalActionSystemName, string actionSystemName, float newDuration, float newSpeed)` | カテゴリと元名からアクションを探し、名前と`actionSystem`のアニメーション情報を更新してリストとシーンを更新する。 |
| `updateActionList(bool updatingListIngame)` | カテゴリ/アクションの索引`customActionStateInfoDictionaryList`を再構築し、エディタ時はログとシーン更新も行う。 |
| `checkActions()` | 全カテゴリのアクション数を数え、重複した名前をログ出力する。 |
| `checkActionSystemAlreadyExists(string actionName)` | `checkDuplicated`で同名アクション数を数え、1つ以上あればtrueを返す。 |
| `movePlayerToPositionTarget(Transform targetTransform)` | 移動先指定コルーチンを停止してから`movePlayerToPositionTargetCoroutine`を開始する。 |
| `stopMovePlayerToPositionTargetCoroutine()` | 移動コルーチン`movePlayerToTargetCoroutine`を停止し`movingPlayerToPositionTargetActive`をfalseにする。 |
| `checkIfSpawnActionSystem(customActionStateInfo customActionStateInfoToCheck)` | `useActionSystemPrefab`かつ未生成なら、プレハブを自身の子として生成し`mainActionSystem`へ設定する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartAction` | `UnityEvent` | – |
| `eventOnEndAction` | `UnityEvent` | – |
| `eventOnActionDetected` | `UnityEvent` | – |
| `eventBeforeStartAction` | `UnityEvent` | – |
| `eventAfterEndAction` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnAnimatorMove()`

</details>

## 内部型

- `actionStateInfo`（class）
- `customActionStateInfo`（class）
- `inputToPauseOnActionIfo`（class）
- `customActionStateCategoryInfo`（class）
- `customActionStateInfoDictionary`（class）
- `customActionCategoryIDInfo`（class）
