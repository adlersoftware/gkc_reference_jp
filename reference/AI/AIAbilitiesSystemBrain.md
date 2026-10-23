# AIAbilitiesSystemBrain

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Custom AI Behavior/AIAbilitiesSystemBrain.cs:6`

**概要**: `playerAbilitiesSystem` をAIから操作し、能力リストから次の能力を選んで発動するブレイン。距離・角度・確率・クールダウンを判定し、能力ごとの押下保持/トグルや継続時間、開始/終了イベントを扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| System Enabled | `systemEnabled` | `bool` | true | – |
| Current Min Distance To Attack | `currentMinDistanceToAttack` | `float` | 7 | – |

### Attack Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attack Enabled | `attackEnabled` | `bool` | – | – |
| Random Attack Range Rate | `randomAttackRangeRate` | `Vector2` | – | – |

### Abilities Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Ability After Time Enabled | `changeAbilityAfterTimeEnabled` | `bool` | – | – |
| Change Ability Randomly | `changeAbilityRandomly` | `bool` | – | – |
| Random Change Ability Rate | `randomChangeAbilityRate` | `Vector2` | – | – |
| Use Custom List To Change Ability | `useCustomListToChangeAbility` | `bool` | – | – |
| Custom List To Change Ability | `customListToChangeAbility` | `List<string>` | new List<string> () | – |
| Use Custom List To Change Ability Info List | `useCustomListToChangeAbilityInfoList` | `bool` | – | – |
| Custom List To Change Ability Info List | `customListToChangeAbilityInfoList` | `List<customListToChangeAbilityInfo>` | new List<customListToChangeAbilityInf… | – |

### Abilities List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Ability Index | `currentAbilityIndex` | `int` | – | – |
| AI Ability Info List | `AIAbilityInfoList` | `List<AIAbilityInfo>` | new List<AIAbilityInfo> () | – |
| Current Ability State Index | `currentAbilityStateIndex` | `int` | – | – |
| AI Ability States Info List | `AIAbilityStatesInfoList` | `List<AIAbilityStatesInfo>` | new List<AIAbilityStatesInfo> () | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Wait To Activate Attack Enabled | `changeWaitToActivateAttackEnabled` | `bool` | true | – |
| Use Wait To Activate Attack Active Counter | `useWaitToActivateAttackActiveCounter` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| System Active | `systemActive` | `bool` | – | – |
| Waiting For Attack Active | `waitingForAttackActive` | `bool` | – | – |
| Can Use Attack Active | `canUseAttackActive` | `bool` | – | – |
| Attack State Paused | `attackStatePaused` | `bool` | – | – |
| Inside Min Distance To Attack | `insideMinDistanceToAttack` | `bool` | – | – |
| Current Attack Rate | `currentAttackRate` | `float` | – | – |
| Ability In Process | `abilityInProcess` | `bool` | – | – |
| On Spotted | `onSpotted` | `bool` | – | – |
| Checking To Change Ability Active | `checkingToChangeAbilityActive` | `bool` | – | – |
| Wait To Activate Attack Active | `waitToActivateAttackActive` | `bool` | – | – |
| Wait To Activate Attack Active Counter | `waitToActivateAttackActiveCounter` | `int` | 0 | – |
| Turn Based Combat Action Active | `turnBasedCombatActionActive` | `bool` | – | – |
| Current Path Distance To Target | `currentPathDistanceToTarget` | `float` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Combat Active | `useEventsOnCombatActive` | `bool` | – | – |
| Event On Combat Active | `eventOnCombatActive` | `UnityEvent` | – | – |
| Event On Combat Deactivate | `eventOnCombatDeactivate` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main AI Navmesh Manager | `mainAINavmeshManager` | `AINavMesh` | – | – |
| Main Player Abilities System | `mainPlayerAbilitiesSystem` | `playerAbilitiesSystem` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateAI()` | `systemActive` なら`AIPaused` を更新するだけで、分岐内は空。 |
| `resetStates()` | 中身が空で、何もしない。 |
| `updateInsideMinDistance(bool newInsideMinDistanceToAttack)` | `insideMinDistanceToAttack` に`newInsideMinDistanceToAttack` を代入するだけで、分岐は空。 |
| `updateBehavior()` | システム有効・AI非停止・ターン制アクション非実行の時だけ`checkAttackState` を呼ぶ。 |
| `checkAttackState()` | 攻撃可否・距離・角度・確率・能力クールダウンを判定し、成立時に`attackTarget` を呼んで次回攻撃間隔を再抽選する。 |
| `setChangeAbilityAfterTimeEnabledState(bool state)` | `changeAbilityAfterTimeEnabled` に`state` を代入するだけ。 |
| `setNextAbility()` | ランダム/順次・カスタムリストの設定に従って有効な次能力を探し、`setNewAbilityByName` で切り替える。 |
| `updateAIAttackState(bool newCanUseAttackActiveState)` | `canUseAttackActive` に`newCanUseAttackActiveState` を代入するだけ。 |
| `setSystemEnabledState(bool state)` | 値が変わる時だけ`systemEnabled` を更新し、`setSystemActiveState` に反映する。 |
| `setSystemActiveState(bool state)` | 有効化時は現在の能力/状態を再設定して攻撃間隔を抽選し、イベント発火と待機カウンタのリセットも行う。 |
| `pauseAttackDuringXTime(float newDuration)` | 指定時間`attackStatePaused` をtrueにし、`checkAttackState` の攻撃を遅延させる。 |
| `setWaitToActivateAttackActiveState(bool state)` | カウンタ方式に対応しつつ`waitToActivateAttackActive` を設定するだけ。 |
| `resetBehaviorStates()` | `resetStates` を呼び、`waitingForAttackActive` と射程内フラグをfalseにする。 |
| `attackTarget()` | 行動一時停止コルーチンを開始して`abilityInProcess` を立て、保持/トグルなら入力保持コルーチン、通常は能力入力と開始イベントで発動する。 |
| `resetAttackState()` | 中身が空で、何もしない。 |
| `disableOnSpottedState()` | 中身が空で、何もしない。 |
| `setAndActivateAbilityByName(string abilityName)` | `setNewAbilityByName` で能力を設定してから`attackTarget` で発動し、次回攻撃間隔を抽選し直す。 |
| `setNewAbilityByName(string abilityName)` | 名前一致の能力を現在能力に設定し、旧能力の`isCurrentAbility` をfalseにして`currentAbilityIndex` を更新する。 |
| `setNewMinDistanceToAttack(float newValue)` | `currentMinDistanceToAttack` に`newValue` を代入するだけ。 |
| `setNewAbilityStateByName(string abilityStateName)` | 名前一致の能力状態を設定し、その`minDistanceToAttack` を現在値へ反映して`currentAbilityStateIndex` を更新する。 |
| `stopCurrentAttackInProcess()` | `abilityInProcess` の時だけ、行動一時停止と入力保持のコルーチンを停止する。 |
| `setTurnBasedCombatActionActiveState(bool state)` | `turnBasedCombatActionActive` に`state` を代入するだけ。 |
| `isAbilityInProcess()` | `abilityInProcess` を返すだけ。 |
| `checkAIBehaviorStateOnCharacterSpawn()` | 中身が空で、スポーン時の処理は行わない。 |
| `checkAIBehaviorStateOnCharacterDespawn()` | 中身が空で、デスポーン時の処理は行わない。 |
| `setChangeAbilityRandomlyState(bool state)` | `changeAbilityRandomly` に`state` を代入するだけ。 |
| `setUseCustomListToChangeAbilityState(bool state)` | `useCustomListToChangeAbility` に`state` を代入するだけ。 |
| `setCustomListToChangeAbility(List<string> newList)` | `customListToChangeAbility` に`newList` を代入するだけ。 |
| `setUseCustomListToChangeAbilityInfoListState(bool state)` | `useCustomListToChangeAbilityInfoList` に`state` を代入するだけ。 |
| `setCustomListToChangeAbilityInfoListByName(string newName)` | 名前一致の項目だけ`isCustomListActive` をtrueにし、他の項目はfalseにする。 |
| `setAttackEnabledState(bool state)` | `attackEnabled` に`state` を代入するだけ。 |
| `setAttackEnabledStateFromEditor(bool state)` | `setAttackEnabledState` の後に`updateComponent` でシーンを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent` と`updateDirtyScene` でインスペクタとシーンを更新するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCombatActive` | `UnityEvent` | – |
| `eventOnCombatDeactivate` | `UnityEvent` | – |

## 内部型

- `AIAbilityInfo`（class）
- `AIAbilityStatesInfo`（class）
- `customListToChangeAbilityInfo`（class）
