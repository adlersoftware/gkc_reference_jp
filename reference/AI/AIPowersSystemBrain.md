# AIPowersSystemBrain

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Custom AI Behavior/AIPowersSystemBrain.cs:6`

**概要**: パワー（照準・射撃）系の攻撃をAIから操作するブレインで、照準/射撃入力の送信と攻撃間隔を制御する。ランダム歩行・ロール・強制攻撃タイマー、戦闘イベント、ターン制戦闘フラグも併せて管理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| System Enabled | `systemEnabled` | `bool` | true | – |

### Attack Enabled Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attack Enabled | `attackEnabled` | `bool` | – | – |

### Attack Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attack Rate | `attackRate` | `float` | 0.17f | – |
| Set Wait Time On Fire Power Blast | `setWaitTimeOnFirePowerBlast` | `bool` | – | – |
| Wait Time Range On Fire Power Blast | `waitTimeRangeOnFirePowerBlast` | `Vector2` | – | – |
| Fire Time Range Before Wait For Next Power Blast | `fireTimeRangeBeforeWaitForNextPowerBlast` | `Vector2` | – | – |
| Check To Force Attack If Not Used Long Time Ago | `checkToForceAttackIfNotUsedLongTimeAgo` | `bool` | – | – |
| Max Wait Time To Force Attack If Not Used Long Time Ago | `maxWaitTimeToForceAttackIfNotUsedLongTimeAgo` | `float` | 10 | – |

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
| Pause Fire Power During Walk Enabled | `pauseFirePowerDuringWalkEnabled` | `bool` | true | – |
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

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| System Active | `systemActive` | `bool` | – | – |
| Aiming Power | `aimingPower` | `bool` | – | – |
| Shooting Power | `shootingPower` | `bool` | – | – |
| Waiting For Attack Active | `waitingForAttackActive` | `bool` | – | – |
| Can Use Attack Active | `canUseAttackActive` | `bool` | – | – |
| Walk Active | `walkActive` | `bool` | – | – |
| Waiting Walk Active | `waitingWalkActive` | `bool` | – | – |
| Waiting Roll Active | `waitingRollActive` | `bool` | – | – |
| Attack State Paused | `attackStatePaused` | `bool` | – | – |
| Inside Min Distance To Attack | `insideMinDistanceToAttack` | `bool` | – | – |
| Behavior States Paused | `behaviorStatesPaused` | `bool` | – | – |
| Wait To Activate Attack Active | `waitToActivateAttackActive` | `bool` | – | – |
| Wait To Activate Attack Active Counter | `waitToActivateAttackActiveCounter` | `int` | 0 | – |
| Turn Based Combat Action Active | `turnBasedCombatActionActive` | `bool` | – | – |
| Ignore Other Actions To Force Attack Active | `ignoreOtherActionsToForceAttackActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Combat Active | `useEventsOnCombatActive` | `bool` | – | – |
| Event On Combat Active | `eventOnCombatActive` | `UnityEvent` | – | – |
| Event On Combat Deactivate | `eventOnCombatDeactivate` | `UnityEvent` | – | – |
| Event To Change Attack Mode | `eventToChangeAttackMode` | `eventParameters.eventToCallWithString` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Other Powers | `mainOtherPowers` | `otherPowers` | – | – |
| Main Dash System | `mainDashSystem` | `dashSystem` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main AI Navmesh Manager | `mainAINavmeshManager` | `AINavMesh` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateAI()` | `systemActive` かつAI非停止時のみ、歩行の時間切れ/目標到達で`resetRandomWalkState` を呼び、設定時は`checkJumpState` も呼ぶ。 |
| `resetRandomWalkState()` | `setRandomWalkPositionState(0)` でランダム歩行を解除し、待機/歩行フラグをfalseにして最終歩行時刻を更新する。 |
| `resetRollState()` | `waitingRollActive` をfalseにし、`lastTimeRollActive` を現在時刻にしてロール待機を解除するだけ。 |
| `resetStates()` | `resetRandomWalkState` と`resetRollState` を呼び、歩行とロールの待機状態をまとめて解除する。 |
| `checkIfResetStatsOnRandomWalk()` | `walkActive` の時だけ`resetStates` を呼び、歩行中の状態をリセットする。 |
| `checkRollState()` | ロール有効かつ射程内で、待機時間経過後に`activateDashStateWithCustomDirection` でランダム方向へ回避する。 |
| `checkWalkState()` | ランダム歩行有効時、待機/歩行を交互に切り替え、`setRandomWalkPositionState` で半径内の新目的地を設定する。 |
| `updateInsideMinDistance(bool newInsideMinDistanceToAttack)` | 射程内フラグを更新し、`attackAlwaysOnPlace` なら強制的にtrue、射程外なら`setAimState(false)` で照準を止める。 |
| `updateBehavior()` | 強制攻撃タイマー、歩行・ロール、照準/射撃を順に処理し、攻撃開始待ちなら待機して`checkAttackState` を呼ぶ。 |
| `checkAttackState()` | 攻撃有効・射程内・ポーズ・攻撃可否を確認し、`attackRate` 経過後に照準して`shootTarget` で射撃する。 |
| `updateAIAttackState(bool newCanUseAttackActiveState)` | `canUseAttackActive` に`newCanUseAttackActiveState` を代入するだけ。 |
| `setSystemActiveState(bool state)` | `systemEnabled` の時のみ`systemActive` を更新し、戦闘イベントを発火して攻撃時刻と待機カウンタを初期化する。 |
| `pauseAttackDuringXTime(float newDuration)` | 指定時間`attackStatePaused` をtrueにし、`checkAttackState` の攻撃を一時停止させる。 |
| `setWaitToActivateAttackActiveState(bool state)` | カウンタ方式にも対応して攻撃開始待ちを設定し、ランダム歩行の開始/解除も連動させる。 |
| `resetBehaviorStates()` | `resetStates` を呼び、`waitingForAttackActive`・`aimingPower`・射程内フラグをfalseにする。 |
| `setAimState(bool state)` | 照準パワーを開始/停止し、停止時は射撃も止めて連射待機タイマーをリセットする。最後に`aimingPower` を更新する。 |
| `shootTarget()` | `startShootPower`/`holdShootPower` で射撃し、`shootingPower` をtrue、攻撃時刻を更新して強制攻撃フラグを解除する。 |
| `resetAttackState()` | `aimingPower` をfalseにし、連射待機タイマーをリセットするだけ。 |
| `stopAim()` | `aimingPower` がtrueの時だけ`setAimState(false)` を呼ぶ。 |
| `disableOnSpottedState()` | 中身が空で、何もしない。 |
| `startAimPower()` | `aimingPower` がfalseなら`mainOtherPowers.inputSetAimPowerState(true)` で照準入力を送る。 |
| `stopAimPower()` | `aimingPower` がtrueなら`inputSetAimPowerState(false)` で照準入力を解除する。 |
| `startShootPower()` | `mainOtherPowers.inputHoldOrReleaseShootPower(true)` を呼び、射撃の押下を送るだけ。 |
| `holdShootPower()` | `mainOtherPowers.inputHoldShootPower()` を呼び、射撃入力の保持を送るだけ。 |
| `stopShootPower()` | `inputHoldOrReleaseShootPower(false)` で射撃を離し、`shootingPower` をfalseにする。 |
| `setBehaviorStatesPausedState(bool state)` | `behaviorStatesPaused` を設定し、trueの時は`resetAttackState` を呼ぶ。 |
| `stopCurrentAttackInProcess()` | `aimingPower` の時だけ`stopAim` を呼んで攻撃を中断する。 |
| `setTurnBasedCombatActionActiveState(bool state)` | `turnBasedCombatActionActive` に`state` を代入するだけ。 |
| `checkAIBehaviorStateOnCharacterSpawn()` | 中身が空で、スポーン時の処理は行わない。 |
| `checkAIBehaviorStateOnCharacterDespawn()` | 中身が空で、デスポーン時の処理は行わない。 |
| `setMaxWaitTimeToForceAttackIfNotUsedLongTimeAgoValue(float newValue)` | `maxWaitTimeToForceAttackIfNotUsedLongTimeAgo` に`newValue` を代入するだけ。 |
| `setCheckToForceAttackIfNotUsedLongTimeAgoState(bool state)` | `checkToForceAttackIfNotUsedLongTimeAgo` に`state` を代入するだけ。 |
| `checkIfDisableCurrentWeaponToChangeAttackMode(string newModeName)` | `changeAttackMode(newModeName)` を呼ぶだけで、武器無効化の判定はしない。 |
| `changeCurrentAttackMode(string newModeName)` | `changeAttackMode(newModeName)` を呼ぶだけの公開ラッパー。 |
| `stopAttackState()` | `systemActive` 時のみ照準状態を確認し、プレイヤーが行動中なら`resetBehaviorStates` を呼ぶ。デバッグ出力付き。 |
| `setAttackEnabledState(bool state)` | `attackEnabled` に`state` を代入するだけ。 |
| `setAttackEnabledStateFromEditor(bool state)` | `setAttackEnabledState` の後に`updateComponent` を呼び、シーンを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent` と`updateDirtyScene` でインスペクタ表示とシーンのダーティ状態を更新するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCombatActive` | `UnityEvent` | – |
| `eventOnCombatDeactivate` | `UnityEvent` | – |
