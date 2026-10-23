# AICloseCombatSystemBrain

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Close Combat/AICloseCombatSystemBrain.cs:7`
- **属性**: `System.Serializable`

**概要**: 素手のクローズコンバットAIの行動ブレイン。間合い管理とコンボ攻撃、ブロック・回避・ランダム移動の抽選を制御する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Combat System Enabled | `combatSystemEnabled` | `bool` | – | – |
| Controlled By AI | `controlledByAI` | `bool` | – | – |

### Attack Enabled Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attack Enabled | `attackEnabled` | `bool` | true | – |

### Combat Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Make Full Combos | `makeFullCombos` | `bool` | – | – |
| Use Wait Time Between Full Combos | `useWaitTimeBetweenFullCombos` | `bool` | – | – |
| Min Random Time Between Full Combos | `minRandomTimeBetweenFullCombos` | `float` | – | – |
| Max Random Time Between Full Combos | `maxRandomTimeBetweenFullCombos` | `float` | – | – |
| Use Random Time Between Attacks | `useRandomTimeBetweenAttacks` | `bool` | – | – |
| Min Random Time Between Attacks | `minRandomTimeBetweenAttacks` | `float` | – | – |
| Max Random Time Between Attacks | `maxRandomTimeBetweenAttacks` | `float` | – | – |
| Min Time Between Attacks | `minTimeBetweenAttacks` | `float` | – | – |
| Use Random Attack | `useRandomAttack` | `bool` | – | – |
| Use Always Same Attack Type | `useAlwaysSameAttackType` | `bool` | – | – |
| Same Attack Type Name | `sameAttackTypeName` | `string` | – | – |
| Alternate Attack Types | `alternateAttackTypes` | `bool` | – | – |
| Max Time To Reset Attacks State | `maxTimeToResetAttacksState` | `float` | – | – |
| Check To Force Attack If Not Used Long Time Ago | `checkToForceAttackIfNotUsedLongTimeAgo` | `bool` | – | – |
| Max Wait Time To Force Attack If Not Used Long Time Ago | `maxWaitTimeToForceAttackIfNotUsedLongTimeAgo` | `float` | 10 | – |

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

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Wait To Activate Attack Enabled | `changeWaitToActivateAttackEnabled` | `bool` | true | – |
| Activate Random Walk If Wait To Activate Attack Active | `activateRandomWalkIfWaitToActivateAttackActive` | `bool` | – | – |
| Check If Attack In Process Before Calling Next Attack | `checkIfAttackInProcessBeforeCallingNextAttack` | `bool` | true | – |
| Use Wait To Activate Attack Active Counter | `useWaitToActivateAttackActiveCounter` | `bool` | – | – |
| Check Vertical Distance To Target | `checkVerticalDistanceToTarget` | `bool` | – | – |
| Max Vertical Distance To Target | `maxVerticalDistanceToTarget` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Close Combat System Active | `closeCombatSystemActive` | `bool` | – | – |
| Waiting For Attack Active | `waitingForAttackActive` | `bool` | – | – |
| Current Combo Name Selected | `currentComboNameSelected` | `string` | – | – |
| Current Random Time To Attack | `currentRandomTimeToAttack` | `float` | – | – |
| Waiting For Full Combo Complete | `waitingForFullComboComplete` | `bool` | – | – |
| Current Min Wait Time To Next Attack | `currentMinWaitTimeToNextAttack` | `float` | – | – |
| Block Active | `blockActive` | `bool` | – | – |
| Waiting Block Active | `waitingBlockActive` | `bool` | – | – |
| Walk Active | `walkActive` | `bool` | – | – |
| Waiting Walk Active | `waitingWalkActive` | `bool` | – | – |
| Waiting Roll Active | `waitingRollActive` | `bool` | – | – |
| Can Use Attack Active | `canUseAttackActive` | `bool` | – | – |
| Inside Min Distance To Attack | `insideMinDistanceToAttack` | `bool` | – | – |
| Can Activate Attack | `canActivateAttack` | `bool` | – | – |
| Attack State Paused | `attackStatePaused` | `bool` | – | – |
| Debug Pause Attack Activation | `debugPauseAttackActivation` | `bool` | – | – |
| Behavior States Paused | `behaviorStatesPaused` | `bool` | – | – |
| Wait To Activate Attack Active | `waitToActivateAttackActive` | `bool` | – | – |
| Wait To Activate Attack Active Counter | `waitToActivateAttackActiveCounter` | `int` | 0 | – |
| Turn Based Combat Action Active | `turnBasedCombatActionActive` | `bool` | – | – |
| Ignore Other Actions To Force Attack Active | `ignoreOtherActionsToForceAttackActive` | `bool` | – | – |
| Ignore Random Walk Active | `ignoreRandomWalkActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On State Change | `useEventsOnStateChange` | `bool` | – | – |
| Even On State Enabled | `evenOnStateEnabled` | `UnityEvent` | – | – |
| Event On State Disabled | `eventOnStateDisabled` | `UnityEvent` | – | – |
| Use Event If Target Cant Be Reached But Visible | `useEventIfTargetCantBeReachedButVisible` | `bool` | – | – |
| Event If Target Cant Be Reached But Visible | `eventIfTargetCantBeReachedButVisible` | `UnityEvent` | – | – |
| Min Wait Time If Target Cant Be Reached | `minWaitTimeIfTargetCantBeReached` | `float` | 1 | – |
| Event To Change Attack Mode | `eventToChangeAttackMode` | `eventParameters.eventToCallWithString` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Close Combat System | `mainCloseCombatSystem` | `closeCombatSystem` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main Dash System | `mainDashSystem` | `dashSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateAI()` | 戦闘中、ランダム移動の終了・ジャンプ・ターゲット到達不能時のイベント発火を毎フレーム処理する。 |
| `updateMainCloseCombatAttack(bool newCanUseAttackActiveState)` | `canUseAttackActive`に引数の値を入れるだけ。 |
| `updateMainCloseCombatBehavior()` | 強制攻撃や移動・ブロック・回避の優先判定を行い、条件を満たすと`AICloseCombatAttack`を呼ぶ。 |
| `AICloseCombatAttack()` | 攻撃間隔とコンボ進行を管理し、`activateAttack`経由で次のコンボ攻撃を実行する。 |
| `resetRandomWalkState()` | 移動中ならランダム移動位置を0にし、フラグ解除とストレイフ停止を行う。 |
| `resetBlockState()` | ブロック中なら`setBlockStateWithoutInputCheck(false)`で解除し、待機フラグと時刻を更新する。 |
| `resetRollState()` | `waitingRollActive`をfalseにし、`lastTimeRollActive`を更新するだけ。 |
| `resetAttackState()` | 本体が空で何もしない。 |
| `resetStates()` | ランダム移動・ブロック・回避・攻撃の各リセットを順に呼ぶだけ。 |
| `checkIfResetStatsOnRandomWalk()` | `walkActive`なら`resetStates`を呼ぶだけ。 |
| `checkBlockState()` | 強制攻撃中でなければ、ブロック有効時に`updateBlockState`を呼ぶだけ。 |
| `updateBlockState()` | 待機・継続時間を抽選し、時間経過で`setBlockStateWithoutInputCheck`によるブロック開始・終了を切り替える。 |
| `checkRollState()` | 回避が有効で間合い内かつ待機時間が経過すると、ランダム方向へダッシュさせて回避させる。 |
| `checkWalkState()` | ランダム移動有効時、待機後に移動を開始してストレイフを有効化し、待機時は解除する。 |
| `updateInsideMinDistance(bool newInsideMinDistanceToAttack)` | 攻撃間合いの内外フラグを更新するだけ。 |
| `setCloseCombatSystemActiveState(bool state)` | 有効状態を設定してイベントを発火し、ストレイフ・コンボ・攻撃待機状態を初期化する。 |
| `checkEventsOnStateChange(bool state)` | 設定が有効なら有効化・無効化イベントを発火するだけ。 |
| `startOverride()` | `overrideTurretControlState(true)`を呼ぶだけ。 |
| `stopOverride()` | `overrideTurretControlState(false)`を呼ぶだけ。 |
| `overrideTurretControlState(bool state)` | `controlledByAI`を引数の否定値にするだけ。 |
| `setBlockEnabledState(bool state)` | `blockEnabled`を設定し、falseなら`resetBlockState`でブロックを解除する。 |
| `setRollEnabledState(bool state)` | `rollEnabled`を設定し、falseなら`resetRollState`を呼ぶ。 |
| `pauseAttackDuringXTime(float newDuration)` | 指定秒数の攻撃停止を設定し、`attackStatePaused`を立てる。 |
| `setWaitToActivateAttackActiveState(bool state)` | 攻撃待機フラグを設定し、カウンタ加減算とランダム移動の開始・停止を行う。 |
| `setUseRandomWalkEnabledState(bool state)` | `randomWalkEnabled`を設定するだけ。 |
| `setOriginalUseRandomWalkEnabledState()` | 保存した初期値に`randomWalkEnabled`を戻すだけ。 |
| `setIgnoreRandomWalkActiveState(bool state)` | `ignoreRandomWalkActive`を設定するだけ。 |
| `resetBehaviorStates()` | 各状態をリセットし、コンボ・攻撃待機・間合いフラグを初期化する。 |
| `setMinRandomTimeBetweenAttacks(float newValue)` | `minRandomTimeBetweenAttacks`を設定するだけ。 |
| `setMaxRandomTimeBetweenAttacks(float newValue)` | `maxRandomTimeBetweenAttacks`を設定するだけ。 |
| `setOriginalMinRandomTimeBetweenAttacks()` | 保存した初期値に戻すだけ。 |
| `setOriginalMaxRandomTimeBetweenAttacks()` | 保存した初期値に戻すだけ。 |
| `setMinTimeBetweenAttacks(float newValue)` | `minTimeBetweenAttacks`を設定するだけ。 |
| `setOriginalMinTimeBetweenAttacks()` | 保存した初期値に戻すだけ。 |
| `setBehaviorStatesPausedState(bool state)` | `behaviorStatesPaused`を設定するだけ。 |
| `isAIBehaviorAttackInProcess()` | `isAttackInProcess`の結果を返すだけ。 |
| `stopCurrentAttackInProcess()` | 攻撃中なら`disableCurrentAttackInProcess`で現在の攻撃を中断させる。 |
| `setTurnBasedCombatActionActiveState(bool state)` | `turnBasedCombatActionActive`を設定するだけ。 |
| `checkAIBehaviorStateOnCharacterSpawn()` | 本体が空で何もしない。 |
| `checkAIBehaviorStateOnCharacterDespawn()` | 本体が空で何もしない。 |
| `setMaxWaitTimeToForceAttackIfNotUsedLongTimeAgoValue(float newValue)` | `maxWaitTimeToForceAttackIfNotUsedLongTimeAgo`を設定するだけ。 |
| `setCheckToForceAttackIfNotUsedLongTimeAgoState(bool state)` | `checkToForceAttackIfNotUsedLongTimeAgo`を設定するだけ。 |
| `changeCurrentAttackMode(string newModeName)` | `changeAttackMode`を呼ぶだけ。 |
| `stopAttackState()` | 戦闘中に攻撃中なら、行動状態をリセットし攻撃を中断させる。 |
| `setAttackEnabledState(bool state)` | `attackEnabled`を設定するだけ。 |
| `setAttackEnabledStateFromEditor(bool state)` | `setAttackEnabledState`の後`updateComponent`を呼ぶ。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`で自身とシーンを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `evenOnStateEnabled` | `UnityEvent` | – |
| `eventOnStateDisabled` | `UnityEvent` | – |
| `eventIfTargetCantBeReachedButVisible` | `UnityEvent` | – |
