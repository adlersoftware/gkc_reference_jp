# AIFireWeaponsSystemBrain

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Custom AI Behavior/AIFireWeaponsSystemBrain.cs:6`

**概要**: 射撃武器で戦うAIの行動ブレイン。ターゲットとの距離に応じて抜刀・照準・射撃・武器切替を制御し、武器が無ければ探索や窃取も行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapons System Enabled | `weaponsSystemEnabled` | `bool` | true | – |
| Draw Weapons When Resuming AI | `drawWeaponsWhenResumingAI` | `bool` | – | – |
| Draw Weapon When Attack Mode Selected | `drawWeaponWhenAttackModeSelected` | `bool` | – | – |
| Keep Weapons If Not Targets To Attack | `keepWeaponsIfNotTargetsToAttack` | `bool` | – | – |
| Can Drop Weapon Externally Enabled | `canDropWeaponExternallyEnabled` | `bool` | true | – |

### Attack Enabled Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attack Enabled | `attackEnabled` | `bool` | – | – |

### Attack Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fire Weapon Attack Rate | `fireWeaponAttackRate` | `float` | 0.17f | – |
| Set Wait Time On Fire Weapon Blast | `setWaitTimeOnFireWeaponBlast` | `bool` | – | – |
| Wait Time Range On Fire Weapon Blast | `waitTimeRangeOnFireWeaponBlast` | `Vector2` | – | – |
| Fire Time Range Before Wait For Next Weapon Blast | `fireTimeRangeBeforeWaitForNextWeaponBlast` | `Vector2` | – | – |
| Check To Force Attack If Not Used Long Time Ago | `checkToForceAttackIfNotUsedLongTimeAgo` | `bool` | – | – |
| Max Wait Time To Force Attack If Not Used Long Time Ago | `maxWaitTimeToForceAttackIfNotUsedLongTimeAgo` | `float` | 10 | – |

### Weapons Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Weapon After Time Enabled | `changeWeaponAfterTimeEnabled` | `bool` | – | – |
| Change Weapon Randomly | `changeWeaponRandomly` | `bool` | – | – |
| Random Change Weapon Rate | `randomChangeWeaponRate` | `Vector2` | – | – |

### Weapon List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Weapon Index | `currentWeaponIndex` | `int` | – | – |
| AI Weapon Info List | `AIWeaponInfoList` | `List<AIWeaponInfo>` | new List<AIWeaponInfo> () | – |
| Use AI Weapon Range Info | `useAIWeaponRangeInfo` | `bool` | – | – |
| AI Weapon Range Info List | `AIWeaponRangeInfoList` | `List<AIWeaponRangeInfo>` | new List<AIWeaponRangeInfo> () | – |

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
| Pause Fire Weapon During Walk Enabled | `pauseFireWeaponDuringWalkEnabled` | `bool` | true | – |
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
| Check Initial Weapons On Character Spawn Enabled | `checkInitialWeaponsOnCharacterSpawnEnabled` | `bool` | true | – |
| Use Wait To Activate Attack Active Counter | `useWaitToActivateAttackActiveCounter` | `bool` | – | – |

### Search Weapons On Scene Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Search Weapons Pickups On Level If No Weapons Available | `searchWeaponsPickupsOnLevelIfNoWeaponsAvailable` | `bool` | – | – |
| Use Max Distance To Get Pickup Weapon | `useMaxDistanceToGetPickupWeapon` | `bool` | – | – |
| Max Distance To Get Pickup Weapon | `maxDistanceToGetPickupWeapon` | `float` | – | – |
| Ignore Check If Usable Weapons Prefab List Active | `ignoreCheckIfUsableWeaponsPrefabListActive` | `bool` | – | – |
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
| Weapons System Active | `weaponsSystemActive` | `bool` | – | – |
| Weapon Equiped | `weaponEquiped` | `bool` | – | – |
| Aiming Weapon | `aimingWeapon` | `bool` | – | – |
| Waiting For Attack Active | `waitingForAttackActive` | `bool` | – | – |
| Shooting Weapon | `shootingWeapon` | `bool` | – | – |
| Can Use Attack Active | `canUseAttackActive` | `bool` | – | – |
| Walk Active | `walkActive` | `bool` | – | – |
| Waiting Walk Active | `waitingWalkActive` | `bool` | – | – |
| Waiting Roll Active | `waitingRollActive` | `bool` | – | – |
| Attack State Paused | `attackStatePaused` | `bool` | – | – |
| Inside Min Distance To Attack | `insideMinDistanceToAttack` | `bool` | – | – |
| Searching Weapon | `searchingWeapon` | `bool` | – | – |
| Character Has Weapons | `characterHasWeapons` | `bool` | – | – |
| Behavior States Paused | `behaviorStatesPaused` | `bool` | – | – |
| Checking To Change Weapon Active | `checkingToChangeWeaponActive` | `bool` | – | – |
| On Spotted | `onSpotted` | `bool` | – | – |
| Change Weapon Check Active | `changeWeaponCheckActive` | `bool` | – | – |
| Wait To Activate Attack Active | `waitToActivateAttackActive` | `bool` | – | – |
| Wait To Activate Attack Active Counter | `waitToActivateAttackActiveCounter` | `int` | 0 | – |
| Current Weapon To Get | `currentWeaponToGet` | `GameObject` | – | – |
| Turn Based Combat Action Active | `turnBasedCombatActionActive` | `bool` | – | – |
| Ignore Other Actions To Force Attack Active | `ignoreOtherActionsToForceAttackActive` | `bool` | – | – |
| Current Path Distance To Target | `currentPathDistanceToTarget` | `float` | – | – |
| Min Distance To Aim | `minDistanceToAim` | `float` | – | – |
| Min Distance To Draw | `minDistanceToDraw` | `float` | – | – |
| Min Distance To Shoot | `minDistanceToShoot` | `float` | – | – |
| Check Character To Attack Radius Active | `checkCharacterToAttackRadiusActive` | `bool` | – | – |
| Current Character To Attack Radius | `currentCharacterToAttackRadius` | `float` | – | – |

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
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Dash System | `mainDashSystem` | `dashSystem` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main AI Navmesh Manager | `mainAINavmeshManager` | `AINavMesh` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateAI()` | 武器システム有効時、武器所持確認・ランダム移動の終了・武器取得・ジャンプ判定を毎フレーム処理する。 |
| `resetRandomWalkState()` | `setRandomWalkPositionState(0)`で移動を止め、待機・移動フラグと時刻を更新するだけ。 |
| `resetRollState()` | `waitingRollActive`をfalseにし、`lastTimeRollActive`に現在時刻を入れるだけ。 |
| `resetStates()` | `resetRandomWalkState`と`resetRollState`を呼び、移動と回避の状態を解除する。 |
| `checkIfResetStatsOnRandomWalk()` | `walkActive`なら`resetStates`を呼び、移動中の状態をリセットするだけ。 |
| `checkRollState()` | 回避が有効で間合い内かつ待機時間が経過すると、ランダム方向へダッシュさせて回避させる。 |
| `checkWalkState()` | 移動先・継続時間・半径を抽選し、時間経過後に`setRandomWalkPositionState`でランダム移動を開始する。 |
| `updateInsideMinDistance(bool newInsideMinDistanceToAttack)` | 攻撃間合いの内外を記録し、内側なら武器を抜かせ、外側なら照準を解除する。 |
| `updateMainFireWeaponsBehavior()` | 強制攻撃・移動・回避を判定した後、距離に応じて抜刀・照準・射撃・武器切替を制御する射撃行動の本体。 |
| `checkNoFireWeaponsAvailableState()` | 武器が無い時、レベル上の`weaponPickup`を探して経路を設定し、`searchingWeapon`を立てて取得に向かわせる。 |
| `checkAttackState()` | 攻撃有効かつ間合い内で武器切替と射撃間隔を判定し、条件を満たすと`shootTarget`を呼ぶ。 |
| `updateMainFireWeaponsAttack(bool newCanUseAttackActiveState)` | `canUseAttackActive`に引数の値を代入するだけ。 |
| `setNextWeapon()` | ランダムまたは次の有効な`AIWeaponInfo`を選び、`setNewWeaponByName`で現在武器を切り替える。 |
| `setNewWeaponByName(string weaponName)` | 名前が一致する`AIWeaponInfo`を現在武器にし、フラグとインデックスを更新する。 |
| `setWeaponsSystemActiveState(bool state)` | 有効状態を設定して戦闘イベントを発火し、必要なら武器を抜かせ、攻撃待機やカウンタを初期化する。 |
| `pauseAttackDuringXTime(float newDuration)` | 指定秒数の攻撃停止を設定し、`attackStatePaused`と開始時刻を更新する。 |
| `setWaitToActivateAttackActiveState(bool state)` | 攻撃待機フラグを設定し、カウンタ方式なら加減算、必要ならランダム移動も開始・停止する。 |
| `setUseRandomWalkEnabledState(bool state)` | `randomWalkEnabled`を引数の値にするだけ。 |
| `setOriginalUseRandomWalkEnabledState()` | 起動時に保存した`originalRandomWalkEnabled`に戻すだけ。 |
| `resetBehaviorStates()` | 移動・回避を止め、攻撃待機を解除し、武器を構える/抜くのを止めて間合いフラグをfalseにする。 |
| `setDrawOrHolsterWeaponState(bool state)` | 武器マネージャに抜刀・納刀を要求し、`weaponEquiped`と照準状態・射撃待機値を更新する。 |
| `setAimWeaponState(bool state)` | 照準の開始・停止を武器マネージャに要求し、`aimingWeapon`と射撃待機値を更新する。 |
| `setShootWeaponState(bool state)` | `shootWeapon`で射撃を開始・停止し、`shootingWeapon`と最終攻撃時刻を更新する。 |
| `dropWeapon()` | 射撃中なら止め、`dropWeaponCheckingMinDelay`が通れば武器を捨てて攻撃・所持状態をリセットする。 |
| `shootTarget()` | 照準開始から0.1秒以上経過しAIが停止中でなければ、`setShootWeaponState(true)`で射撃する。 |
| `resetAttackState()` | `weaponEquiped`と`aimingWeapon`をfalseにし、射撃待機値をリセットするだけ。 |
| `checkIfDrawWeaponsWhenResumingAI()` | 設定が有効で武器未所持なら、`setDrawOrHolsterWeaponState(true)`で抜刀させるだけ。 |
| `stopAim()` | 照準中なら`setAimWeaponState(false)`を呼んで照準を止めるだけ。 |
| `disableOnSpottedState()` | 本体が空で何もしない。 |
| `updateWeaponsAvailableState()` | `checkIfWeaponsAvailable`の結果を`characterHasWeapons`に入れるだけ。 |
| `setBehaviorStatesPausedState(bool state)` | `behaviorStatesPaused`を設定し、trueなら`resetAttackState`で攻撃状態を解除する。 |
| `isWeaponEquiped()` | `weaponEquiped`の値を返すだけ。 |
| `updateIfCarryingWeapon()` | 武器マネージャの所持判定を`weaponEquiped`に反映するだけ。 |
| `inputWeaponMeleeAttack()` | 射撃を止めたうえで`inputWeaponMeleeAttack`を呼び、武器での近接攻撃を行わせる。 |
| `stopCurrentAttackInProcess()` | 射撃中か照準中なら射撃を止め、続けて照準も解除する。 |
| `setTurnBasedCombatActionActiveState(bool state)` | `turnBasedCombatActionActive`を設定するだけ。 |
| `checkAIBehaviorStateOnCharacterSpawn()` | 設定が有効なら武器一覧を有効化し、初期武器チェックをリセットするだけ。 |
| `checkAIBehaviorStateOnCharacterDespawn()` | 本体が空で何もしない。 |
| `setMaxWaitTimeToForceAttackIfNotUsedLongTimeAgoValue(float newValue)` | `maxWaitTimeToForceAttackIfNotUsedLongTimeAgo`を設定するだけ。 |
| `setCheckToForceAttackIfNotUsedLongTimeAgoState(bool state)` | `checkToForceAttackIfNotUsedLongTimeAgo`を設定するだけ。 |
| `checkIfDisableCurrentWeaponToChangeAttackMode(string newModeName)` | 引数のモード名で`changeAttackMode`を呼ぶだけ。 |
| `changeCurrentAttackMode(string newModeName)` | `changeAttackMode`を呼び、戦闘中なら攻撃を止めてモード変更イベントを発火する。 |
| `stopAttackState()` | 戦闘中に武器所持かつ操作中なら、行動状態をリセットし`checkIfDisableCurrentWeapon`を呼ぶ。 |
| `setAttackEnabledState(bool state)` | `attackEnabled`を設定するだけ。 |
| `updateCurrentTargetSelectedInfo()` | 武器別の距離設定を適用し、ターゲットの攻撃半径を敵武器距離に加算して反映する。 |
| `setAttackEnabledStateFromEditor(bool state)` | `setAttackEnabledState`の後`updateComponent`でシーンを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`で自身とシーンを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnNoWeaponToPickFromScene` | `UnityEvent` | – |
| `eventOnNoWeaponsAvailable` | `UnityEvent` | – |
| `eventOnStealWeapon` | `UnityEvent` | – |
| `eventOnCombatActive` | `UnityEvent` | – |
| `eventOnCombatDeactivate` | `UnityEvent` | – |

## 内部型

- `AIWeaponInfo`（class）
- `AIWeaponRangeInfo`（class）
