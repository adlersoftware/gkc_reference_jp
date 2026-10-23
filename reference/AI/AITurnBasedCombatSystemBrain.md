# AITurnBasedCombatSystemBrain

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Custom AI Behavior/AITurnBasedCombatSystemBrain.cs:6`

**概要**: ターン制戦闘で手番キャラクターの攻撃コマンドを自動選択するブレインで、カテゴリとコマンドを確率・前回使用・ステータス消費で抽選する。`characterToReceiveOrders` 経由で発注し、手番の開始/終了や位置合わせ、死亡時の手番送りも処理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| System Enabled | `systemEnabled` | `bool` | true | – |
| Check Distance To Target Enabled | `checkDistanceToTargetEnabled` | `bool` | – | – |
| Current Min Distance To Attack | `currentMinDistanceToAttack` | `float` | 7 | – |
| Default Match Offset | `defaultMatchOffset` | `float` | 1 | – |

### Attack Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attack Enabled | `attackEnabled` | `bool` | – | – |
| Min Wait To Activate Attack | `minWaitToActivateAttack` | `float` | 0.5f | – |
| Use Probability To Use Attack | `useProbabilityToUseAttack` | `bool` | – | – |
| Probability To Use Attack | `probabilityToUseAttack` | `float` | – | Range (0, 100) |
| Ignore Probability To Check Category | `ignoreProbabilityToCheckCategory` | `bool` | – | – |
| Ignore Probability To Use Attack | `ignoreProbabilityToUseAttack` | `bool` | – | – |
| Ignore Use Stat To Use Action | `ignoreUseStatToUseAction` | `bool` | – | – |
| Ignore If Last Category Previously Selected | `ignoreIfLastCategoryPreviouslySelected` | `bool` | – | – |
| Ignore If Last Attack Previously Selected | `ignoreIfLastAttackPreviouslySelected` | `bool` | – | – |
| Turn Based Combat Attack Category Info List | `turnBasedCombatAttackCategoryInfoList` | `List<turnBasedCombatAttackCategoryInfo>` | new List<turnBasedCombatAttackCategor… | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| System Active | `systemActive` | `bool` | – | – |
| Is Current Character Turn | `isCurrentCharacterTurn` | `bool` | – | – |
| AI On Player Team | `AIOnPlayerTeam` | `bool` | – | – |
| Last Attack Used Index | `lastAttackUsedIndex` | `int` | -1 | – |
| Last Category Index | `lastCategoryIndex` | `int` | -1 | – |
| Current Attack In Process | `currentAttackInProcess` | `bool` | – | – |
| Delay To Activete Attack In Process | `delayToActiveteAttackInProcess` | `bool` | – | – |
| Current Command Name | `currentCommandName` | `string` | – | – |
| Waiting For Attack Active | `waitingForAttackActive` | `bool` | – | – |
| Can Use Attack Active | `canUseAttackActive` | `bool` | – | – |
| Attack State Paused | `attackStatePaused` | `bool` | – | – |
| Inside Min Distance To Attack | `insideMinDistanceToAttack` | `bool` | – | – |
| Wait To Activate Attack Active | `waitToActivateAttackActive` | `bool` | – | – |
| Block Active | `blockActive` | `bool` | – | – |
| Current Target | `currentTarget` | `GameObject` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Combat Active | `useEventsOnCombatActive` | `bool` | – | – |
| Event On Combat Active | `eventOnCombatActive` | `UnityEvent` | – | – |
| Event On Combat Deactivate | `eventOnCombatDeactivate` | `UnityEvent` | – | – |
| Use Event If Block Active On Current Turn | `useEventIfBlockActiveOnCurrentTurn` | `bool` | – | – |
| Event If Block Active On Current Turn | `eventIfBlockActiveOnCurrentTurn` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main AI Navmesh Manager | `mainAINavmeshManager` | `AINavMesh` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Character To Receive Orders | `mainCharacterToReceiveOrders` | `characterToReceiveOrders` | – | – |
| Main Turn Based Combat Actions System | `mainTurnBasedCombatActionsSystem` | `turnBasedCombatActionsSystem` | – | – |
| Main Match Player To Target System | `mainMatchPlayerToTargetSystem` | `matchPlayerToTargetSystem` | – | – |
| Main Player Stats System | `mainPlayerStatsSystem` | `playerStatsSystem` | – | – |
| Main Health | `mainHealth` | `health` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateAI()` | `systemActive` 時に`AIPaused` を更新するだけで、分岐内は空。 |
| `checkStateOnCharacterDead()` | 手番キャラの死亡時は`setNextTurn` で手番を送って各フラグを解除し、非手番ならチーム全滅判定を呼ぶ。 |
| `resetStates()` | 中身が空で、何もしない。 |
| `updateInsideMinDistance(bool newInsideMinDistanceToAttack)` | `insideMinDistanceToAttack` に値を代入するだけで、分岐は空。 |
| `updateBehavior()` | システム有効かつAI非停止時のみ経路距離を取得して`checkAttackState` を呼ぶ。 |
| `checkAttackState()` | 攻撃有効・射程・待機・手番・確率・行動中判定を確認し、条件成立時に`attackTarget` でコマンドを発注する。 |
| `updateAIAttackState(bool newCanUseAttackActiveState)` | `canUseAttackActive` に`newCanUseAttackActiveState` を代入するだけ。 |
| `setSystemEnabledState(bool state)` | 値が変わる時のみ`systemEnabled` を更新し`setSystemActiveState` を呼ぶ。 |
| `setSystemActiveState(bool state)` | 有効状態を更新し、無効化時は手番・攻撃・遅延・ブロックの各フラグを解除してから戦闘イベントを発火する。 |
| `pauseAttackDuringXTime(float newDuration)` | 指定時間`attackStatePaused` をtrueにして攻撃を一時停止する。 |
| `setWaitToActivateAttackActiveState(bool state)` | `waitToActivateAttackActive` に`state` を代入するだけ。 |
| `resetBehaviorStates()` | `resetStates` を呼び、`waitingForAttackActive` と射程内フラグをfalseにする。 |
| `attackTarget()` | カテゴリとコマンドを有効/確率/前回使用/ステータスで抽選し、`lastAttackUsedIndex` を更新して`activateAttack` を呼ぶ。 |
| `activateAttackByName(string attackName)` | 有効なカテゴリ内から名前一致のコマンドを探して現在コマンドに設定し、`activateAttack` で発注する。 |
| `setBlockActiveState(bool state)` | `blockActive` に`state` を代入するだけ。 |
| `resetAttackState()` | 中身が空で、何もしない。 |
| `disableOnSpottedState()` | 中身が空で、何もしない。 |
| `setNewMinDistanceToAttack(float newValue)` | `currentMinDistanceToAttack` に`newValue` を代入するだけ。 |
| `setAIOnPlayerTeamState(bool state)` | `AIOnPlayerTeam` に`state` を代入するだけ。 |
| `setIsCurrentCharacterTurn(bool state)` | 手番フラグを設定し、trueならAI再開・対象設定・攻撃時刻更新、falseならAI停止と対象クリアを行う。ブロック時のイベントも発火する。 |
| `setCurrentCharacterTurnTarget(GameObject newTarget)` | `currentTarget` に`newTarget` を代入するだけ。 |
| `setNextTurn()` | `systemActive` かつ自分の手番の時だけ`mainTurnBasedCombatActionsSystem.setNextTurn()` を呼ぶ。 |
| `setCurrentTurnBasedCombatAttackComplete()` | `setNextTurn` を呼ぶだけのエイリアス。 |
| `activateMatchPosition(float customMatchOffset)` | 0より大きい値を優先して`mainMatchPlayerToTargetSystem.activateMatchPosition` を呼び、対象との位置合わせを開始する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCombatActive` | `UnityEvent` | – |
| `eventOnCombatDeactivate` | `UnityEvent` | – |
| `eventIfBlockActiveOnCurrentTurn` | `UnityEvent` | – |

## 内部型

- `turnBasedCombatAttackCategoryInfo`（class）
- `turnBasedCombatAttackInfo`（class）
