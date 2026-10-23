# AIMeleeCombatSystemBrain

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Melee Combat System/AIMeleeCombatSystemBrain.cs:6`

**概要**: 近接武器AIの行動ブレイン。武器の抜刀・攻撃コンボ・ブロック・パリィカウンターを管理し、武器が無ければ探索や窃取を行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Combat System Enabled | `combatSystemEnabled` | `bool` | true | – |
| Make Full Combos | `makeFullCombos` | `bool` | – | – |
| Use Wait Time Between Full Combos | `useWaitTimeBetweenFullCombos` | `bool` | – | – |
| Min Random Time Between Full Combos | `minRandomTimeBetweenFullCombos` | `float` | – | – |
| Max Random Time Between Full Combos | `maxRandomTimeBetweenFullCombos` | `float` | – | – |
| Keep Weapons If Not Targets To Attack | `keepWeaponsIfNotTargetsToAttack` | `bool` | – | – |

### Attack Enabled Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attack Enabled | `attackEnabled` | `bool` | – | – |

### Attack Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Random Attack | `useRandomAttack` | `bool` | – | – |
| Use Always Same Attack Type | `useAlwaysSameAttackType` | `bool` | – | – |
| Same Attack Type Name | `sameAttackTypeName` | `string` | – | – |
| Alternate Attack Types | `alternateAttackTypes` | `bool` | – | – |
| Check To Force Attack If Not Used Long Time Ago | `checkToForceAttackIfNotUsedLongTimeAgo` | `bool` | – | – |
| Max Wait Time To Force Attack If Not Used Long Time Ago | `maxWaitTimeToForceAttackIfNotUsedLongTimeAgo` | `float` | 10 | – |

### Random Time Attack Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Random Time Between Attacks | `useRandomTimeBetweenAttacks` | `bool` | – | – |
| Min Random Time Between Attacks | `minRandomTimeBetweenAttacks` | `float` | – | – |
| Max Random Time Between Attacks | `maxRandomTimeBetweenAttacks` | `float` | – | – |
| Min Time Between Attacks | `minTimeBetweenAttacks` | `float` | – | – |

### Attack Types Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Melee Attack Types | `meleeAttackTypes` | `List<string>` | new List<string> () | – |
| Melee Attack Types Amount | `meleeAttackTypesAmount` | `List<int>` | new List<int> () | – |

### Drop Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Drop Weapon Externally Enabled | `canDropWeaponExternallyEnabled` | `bool` | true | – |
| Draw Random Weapon On Weapon Drop | `drawRandomWeaponOnWeaponDrop` | `bool` | – | – |

### Block Attack Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Block Enabled | `blockEnabled` | `bool` | – | – |
| Random Block Wait Time | `randomBlockWaitTime` | `Vector2` | – | – |
| Random Block Duration | `randomBlockDuration` | `Vector2` | – | – |

### Roll/Dodge Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Roll Enabled | `rollEnabled` | `bool` | – | – |
| Random Roll Wait Time | `randomRollWaitTime` | `Vector2` | – | – |
| Min Wait Time After Roll Active | `minWaitTimeAfterRollActive` | `float` | 1.3f | – |
| Roll Movement Direction List | `rollMovementDirectionList` | `List<Vector2>` | new List<Vector2> () | – |

### Random Walk Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Random Walk Enabled | `randomWalkEnabled` | `bool` | – | – |
| Random Walk Wait Time | `randomWalkWaitTime` | `Vector2` | – | – |
| Random Walk Duration | `randomWalkDuration` | `Vector2` | – | – |
| Random Walk Radius | `randomWalkRadius` | `Vector2` | – | – |
| Ignore Random Walk In Front Direction Enabled | `ignoreRandomWalkInFrontDirectionEnabled` | `bool` | true | – |

### Jump To Target Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Jump To Target On Range Distance | `jumpToTargetOnRangeDistance` | `bool` | – | – |
| Range Distance To Jump To Target | `rangeDistanceToJumpToTarget` | `Vector2` | – | – |
| Avoid Attack On Air | `avoidAttackOnAir` | `bool` | true | – |
| Min Time To Jump Again | `minTimeToJumpAgain` | `float` | 4 | – |
| Use Jump Probability | `useJumpProbability` | `bool` | – | – |
| Jump Probability | `jumpProbability` | `float` | – | Range (0, 100) |
| Set New Jump Force | `setNewJumpForce` | `bool` | – | – |
| New Jump Force | `newJumpForce` | `float` | – | – |
| Set New Jump Force Min Distance | `setNewJumpForceMinDistance` | `bool` | – | – |
| New Jump Force Min Distance | `newJumpForceMinDistance` | `float` | – | – |

### Melee Weapon At Distance Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Melee Attack At Distance Rate | `meleeAttackAtDistanceRate` | `float` | – | – |
| Event To Start Aim Melee Weapon | `eventToStartAimMeleeWeapon` | `UnityEvent` | – | – |
| Event To Stop Aim Melee Weapon | `eventToStopAimMeleeWeapon` | `UnityEvent` | – | – |
| Event To Melee Attack At Distance | `eventToMeleeAttackAtDistance` | `UnityEvent` | – | – |
| Min Wait Time To Aim Melee Weapon After Draw | `minWaitTimeToAimMeleeWeaponAfterDraw` | `float` | 2 | – |
| Use Melee Attack At Distance If Target Cant Be Reached | `useMeleeAttackAtDistanceIfTargetCantBeReached` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check If Attack In Process Before Calling Next Attack | `checkIfAttackInProcessBeforeCallingNextAttack` | `bool` | true | – |
| Change Wait To Activate Attack Enabled | `changeWaitToActivateAttackEnabled` | `bool` | true | – |
| Activate Random Walk If Wait To Activate Attack Active | `activateRandomWalkIfWaitToActivateAttackActive` | `bool` | – | – |
| Check Initial Weapons On Character Spawn Enabled | `checkInitialWeaponsOnCharacterSpawnEnabled` | `bool` | true | – |
| Use Wait To Activate Attack Active Counter | `useWaitToActivateAttackActiveCounter` | `bool` | – | – |
| Check Vertical Distance To Target | `checkVerticalDistanceToTarget` | `bool` | – | – |
| Max Vertical Distance To Target | `maxVerticalDistanceToTarget` | `float` | – | – |

### Check Target State Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Current Target State | `checkCurrentTargetState` | `bool` | – | – |
| Activate Block If Target Attack | `activateBlockIfTargetAttack` | `bool` | – | – |
| Probability To Active Block If Target Attack | `probabilityToActiveBlockIfTargetAttack` | `float` | 100 | Range (0, 100) |
| Reaction Time To Active Block If Target Attack | `reactionTimeToActiveBlockIfTargetAttack` | `float` | – | – |
| Random Block Duration If Target Attack | `randomBlockDurationIfTargetAttack` | `Vector2` | – | – |
| Random Wait Time To Activate Block If Target Attack | `randomWaitTimeToActivateBlockIfTargetAttack` | `Vector2` | – | – |
| Min Tim To Check To Block From Attack After Fail | `minTimToCheckToBlockFromAttackAfterFail` | `float` | 1.8f | – |
| Max Time To Reset Block From Attack Fail | `maxTimeToResetBlockFromAttackFail` | `float` | 5 | – |
| Use Event To Cancel Attack To Activate Auto Block | `useEventToCancelAttackToActivateAutoBlock` | `bool` | – | – |
| Event To Cancel Attack To Activate Block | `eventToCancelAttackToActivateBlock` | `UnityEvent` | – | – |
| Activate Parry Counter On Perfect Block | `activateParryCounterOnPerfectBlock` | `bool` | – | – |
| Event To Activate Parry Counter On Perfect Block | `eventToActivateParryCounterOnPerfectBlock` | `UnityEvent` | – | – |
| Use Probablity To Activate Parry Counter On Perfect Block | `useProbablityToActivateParryCounterOnPerfectBlock` | `bool` | – | – |
| Probablity To Activate Parry Counter On Perfect Block | `probablityToActivateParryCounterOnPerfectBlock` | `float` | – | Range (0, 100) |
| Use Delay To Activate Parry Counter On Perfect Block | `useDelayToActivateParryCounterOnPerfectBlock` | `bool` | – | – |
| Delay To Activate Parry Counter On Perfect Block | `delayToActivateParryCounterOnPerfectBlock` | `float` | – | – |

### Search Weapons On Scene Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Search Weapons Pickups On Level If No Weapons Available | `searchWeaponsPickupsOnLevelIfNoWeaponsAvailable` | `bool` | – | – |
| Use Max Distance To Get Pickup Weapon | `useMaxDistanceToGetPickupWeapon` | `bool` | – | – |
| Max Distance To Get Pickup Weapon | `maxDistanceToGetPickupWeapon` | `float` | – | – |
| Use Event On No Weapon To Pick From Scene | `useEventOnNoWeaponToPickFromScene` | `bool` | – | – |
| Event On No Weapon To Pick From Scene | `eventOnNoWeaponToPickFromScene` | `UnityEvent` | – | – |
| Use Events On No Weapons Available | `useEventsOnNoWeaponsAvailable` | `bool` | – | – |
| Use Events On No Weapons Available After Check Weapons On Scene | `useEventsOnNoWeaponsAvailableAfterCheckWeaponsOnScene` | `bool` | – | – |
| Event On No Weapons Available | `eventOnNoWeaponsAvailable` | `UnityEvent` | – | – |

### Steal Weapons From Targets Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Steal Weapon From Current Target | `stealWeaponFromCurrentTarget` | `bool` | – | – |
| Probability To Steal Weapon | `probabilityToStealWeapon` | `float` | 0 | Range (0, 100) |
| Steal Weapon Only If Not Pickups Located | `stealWeaponOnlyIfNotPickupsLocated` | `bool` | – | – |
| Use Max Distance To Steal Weapon | `useMaxDistanceToStealWeapon` | `bool` | – | – |
| Max Distance To Get Steal Weapon | `maxDistanceToGetStealWeapon` | `float` | – | – |
| Use Event On Steal | `useEventOnSteal` | `bool` | – | – |
| Event On Steal Weapon | `eventOnStealWeapon` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Show Attack Debug Print | `showAttackDebugPrint` | `bool` | – | – |
| Show Check Attack State Debug Print | `showCheckAttackStateDebugPrint` | `bool` | – | – |
| Weapon Equiped | `weaponEquiped` | `bool` | – | – |
| Combat System Active | `combatSystemActive` | `bool` | – | – |
| Can Do Attack | `canDoAttack` | `bool` | – | – |
| Waiting For Attack Active | `waitingForAttackActive` | `bool` | – | – |
| Waiting For Full Combo Complete | `waitingForFullComboComplete` | `bool` | – | – |
| Can Use Attack Active | `canUseAttackActive` | `bool` | – | – |
| Attack State Paused | `attackStatePaused` | `bool` | – | – |
| Inside Min Distance To Attack | `insideMinDistanceToAttack` | `bool` | – | – |
| Current Action Priority | `currentActionPriority` | `int` | 1 | – |
| Current Melee Weapon At Distance | `currentMeleeWeaponAtDistance` | `bool` | – | – |
| Aiming Melee Weapon | `aimingMeleeWeapon` | `bool` | – | – |
| Character Has Weapons | `characterHasWeapons` | `bool` | – | – |
| Wait To Activate Attack Active | `waitToActivateAttackActive` | `bool` | – | – |
| Wait To Activate Attack Active Counter | `waitToActivateAttackActiveCounter` | `int` | 0 | – |
| Current Weapon To Get | `currentWeaponToGet` | `GameObject` | – | – |
| Walk Active | `walkActive` | `bool` | – | – |
| Waiting Walk Active | `waitingWalkActive` | `bool` | – | – |
| Block Active | `blockActive` | `bool` | – | – |
| Waiting Block Active | `waitingBlockActive` | `bool` | – | – |
| Waiting Roll Active | `waitingRollActive` | `bool` | – | – |
| Roll Paused | `rollPaused` | `bool` | – | – |
| Current Target Assigned | `currentTargetAssigned` | `bool` | – | – |
| Behavior States Paused | `behaviorStatesPaused` | `bool` | – | – |
| Current Combo Name Selected | `currentComboNameSelected` | `string` | – | – |
| Searching Weapon | `searchingWeapon` | `bool` | – | – |
| Turn Based Combat Action Active | `turnBasedCombatActionActive` | `bool` | – | – |
| Ignore Other Actions To Force Attack Active | `ignoreOtherActionsToForceAttackActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Combat Active | `useEventsOnCombatActive` | `bool` | – | – |
| Event On Combat Active | `eventOnCombatActive` | `UnityEvent` | – | – |
| Event On Combat Deactivate | `eventOnCombatDeactivate` | `UnityEvent` | – | – |
| Use Event If Target Cant Be Reached But Visible | `useEventIfTargetCantBeReachedButVisible` | `bool` | – | – |
| Event If Target Cant Be Reached But Visible | `eventIfTargetCantBeReachedButVisible` | `UnityEvent` | – | – |
| Min Wait Time If Target Cant Be Reached | `minWaitTimeIfTargetCantBeReached` | `float` | 1 | – |
| Event To Change Attack Mode | `eventToChangeAttackMode` | `eventParameters.eventToCallWithString` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Grabbed Object Melee Attack System | `mainGrabbedObjectMeleeAttackSystem` | `grabbedObjectMeleeAttackSystem` | – | – |
| Main Dash System | `mainDashSystem` | `dashSystem` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main Melee Weapons Grabbed Manager | `mainMeleeWeaponsGrabbedManager` | `meleeWeaponsGrabbedManager` | – | – |
| Main AI Navmesh Manager | `mainAINavmeshManager` | `AINavMesh` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateAI()` | 戦闘中、武器情報取得・移動終了・武器探索・ターゲット攻撃への自動ブロック抽選を毎フレーム処理する。 |
| `resetRandomWalkState()` | ランダム移動位置を0にして待機・移動フラグを解除し、時刻を更新する。 |
| `resetBlockState()` | ブロック中なら`inputDeactivateBlock`で解除し、待機フラグと時刻を更新する。 |
| `resetRollState()` | `waitingRollActive`をfalseにし時刻を更新するだけ。 |
| `dropWeapon()` | 条件を満たすと`dropMeleeWeaponsExternally`で武器を捨て、所持状態を更新して次の武器を抜かせる。 |
| `resetAttackState()` | 本体が空で何もしない。 |
| `resetStates()` | 各リセットを呼び、`currentActionPriority`を1〜2で抽選し直す。 |
| `checkIfResetStatsOnRandomWalk()` | `walkActive`なら`resetStates`を呼ぶだけ。 |
| `checkBlockState()` | 強制攻撃中でなければ、ブロック有効時に`updateBlockState`を呼ぶ。 |
| `updateBlockState()` | 優先度と待機時間に応じて`inputActivateBlock`でブロックの開始・終了を制御する。 |
| `checkRollState()` | 優先度2で回避待機が完了すると、ランダム方向へのダッシュで回避する。 |
| `checkWalkState()` | ランダム移動有効時、待機後に移動を開始してストレイフを有効にする。 |
| `updateInsideMinDistance(bool newInsideMinDistanceToAttack)` | 攻撃間合いを記録し、内側なら未所持時に近接武器を抜かせ、外側なら照準を解除する。 |
| `updateMainMeleeBehavior()` | 移動・ブロック・回避などの優先判定の後、武器所持なら`checkAttackState`、無ければ武器探索へ回す。 |
| `checkNoMeleeWeaponsAvailableState()` | 武器が無い時、`meleeWeaponPickup`や物理オブジェクトを探して経路を設定し、取得や窃取を試みる。 |
| `checkAttackState()` | 攻撃間隔とコンボを管理して`useAttack`で攻撃し、遠距離武器時は射撃イベントを発火する。 |
| `useAttack(string attackType)` | `activateGrabbedObjectMeleeAttack`に攻撃タイプ名を渡して攻撃を発生させる。 |
| `updateMainMeleeAttack(bool newCanUseAttackActiveState)` | `canUseAttackActive`を設定するだけ。 |
| `setCombatSystemActiveState(bool state)` | 有効状態を設定してイベントを発火し、武器マネージャ取得や優先度抽選、待機状態の初期化を行う。 |
| `pauseAttackDuringXTime(float newDuration)` | 指定秒数の攻撃停止を`currentPauseAttackStateDuration`に設定する。 |
| `setWaitToActivateAttackActiveState(bool state)` | 攻撃待機フラグを設定し、カウンタやランダム移動の開始・停止を行う。 |
| `setUseRandomWalkEnabledState(bool state)` | `randomWalkEnabled`を設定するだけ。 |
| `setOriginalUseRandomWalkEnabledState()` | 保存した初期値に戻すだけ。 |
| `resetBehaviorStates()` | 各状態と攻撃フラグをリセットし、照準や武器の所持状態、間合いフラグを初期化する。 |
| `setDrawOrHolsterWeaponState(bool state)` | 未所持なら`drawOrKeepMeleeWeapon`で抜かせ、所持中なら納めさせて`weaponEquiped`を更新する。 |
| `setCurrentMeleeWeaponAtDistanceState(bool state)` | `currentMeleeWeaponAtDistance`を設定し、falseなら照準を解除する。 |
| `setPauseRollState(bool state)` | `rollPaused`を設定し、trueなら回避状態をリセットする。 |
| `checkIfDrawMeleeWeaponAfterResumingAI()` | 戦闘中かつ未所持なら近接武器を抜かせ、`checkIfDrawMeleeWeaponActive`をfalseにする。 |
| `updateWeaponsAvailableState()` | 所持数を確認して`characterHasWeapons`を更新するだけ。 |
| `setBehaviorStatesPausedState(bool state)` | `behaviorStatesPaused`を設定するだけ。 |
| `setSameAttackTypeNameValue(string newValue)` | `sameAttackTypeName`を設定するだけ。 |
| `isWeaponEquiped()` | `weaponEquiped`を返すだけ。 |
| `isAIBehaviorAttackInProcess()` | 攻撃中かどうかを返すだけ。 |
| `checkIfActivateParryCounterOnPerfectBlock()` | 確率判定と遅延設定に従い、即時またはコルーチンでパリィカウンターイベントを発火する。 |
| `stopCurrentAttackInProcess()` | 攻撃中なら`disableCurrentAttackInProcess`で中断させる。 |
| `setTurnBasedCombatActionActiveState(bool state)` | `turnBasedCombatActionActive`を設定するだけ。 |
| `checkAIBehaviorStateOnCharacterSpawn()` | 設定が有効なら`resetStartWithWeaponCheckedOnCharacterSpawn`を呼ぶだけ。 |
| `checkAIBehaviorStateOnCharacterDespawn()` | 本体が空で何もしない。 |
| `setMaxWaitTimeToForceAttackIfNotUsedLongTimeAgoValue(float newValue)` | `maxWaitTimeToForceAttackIfNotUsedLongTimeAgo`を設定するだけ。 |
| `setCheckToForceAttackIfNotUsedLongTimeAgoState(bool state)` | `checkToForceAttackIfNotUsedLongTimeAgo`を設定するだけ。 |
| `checkIfDisableCurrentWeaponToChangeAttackMode(string newModeName)` | `changeAttackMode`を呼ぶだけ。 |
| `changeCurrentAttackMode(string newModeName)` | `changeAttackMode`を呼ぶだけ。 |
| `stopAttackState()` | 武器所持かつ攻撃中なら状態をリセットし、抜刀アニメを無視して武器を納めさせる。 |
| `setAttackEnabledState(bool state)` | `attackEnabled`を設定するだけ。 |
| `setAttackEnabledStateFromEditor(bool state)` | `setAttackEnabledState`の後`updateComponent`を呼ぶ。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`で自身とシーンを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToStartAimMeleeWeapon` | `UnityEvent` | – |
| `eventToStopAimMeleeWeapon` | `UnityEvent` | – |
| `eventToMeleeAttackAtDistance` | `UnityEvent` | – |
| `eventToCancelAttackToActivateBlock` | `UnityEvent` | – |
| `eventToActivateParryCounterOnPerfectBlock` | `UnityEvent` | – |
| `eventOnNoWeaponToPickFromScene` | `UnityEvent` | – |
| `eventOnNoWeaponsAvailable` | `UnityEvent` | – |
| `eventOnStealWeapon` | `UnityEvent` | – |
| `eventOnCombatActive` | `UnityEvent` | – |
| `eventOnCombatDeactivate` | `UnityEvent` | – |
| `eventIfTargetCantBeReachedButVisible` | `UnityEvent` | – |
