# turnBasedCombatActionsSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Turn Based Combat/turnBasedCombatActionsSystem.cs:6`

**概要**: 各キャラクターのターン制戦闘アクション用コンポーネント。戦闘中の位置調整や注文実行を担い、ターン送りやUI更新などはメインの戦闘システムへ委譲する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Target Priority | `characterTargetPriority` | `int` | – | – |
| Main Transform | `mainTransform` | `Transform` | – | – |
| Player Camera Trnsform | `playerCameraTrnsform` | `Transform` | – | – |

### Extra Turns Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Use Extra Turns | `canUseExtraTurns` | `bool` | – | – |
| Amount Of Extra Turns | `amountOfExtraTurns` | `int` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Menu Panel Name | `menuPanelName` | `string` | "Turn Combat System" | – |
| Movement Speed | `movementSpeed` | `float` | 10 | – |

### Commands Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Blocked Command List | `useBlockedCommandList` | `bool` | – | – |
| Blocked Command List | `blockedCommandList` | `List<string>` | new List<string> () | – |
| Use Blocked Command Category List | `useBlockedCommandCategoryList` | `bool` | – | – |
| Blocked Command Category List | `blockedCommandCategoryList` | `List<string>` | new List<string> () | – |

### Stats Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Stats To Show List | `characterStatsToShowList` | `List<string>` | new List<string> () | – |
| Add Amount To Character Stats On Combat | `addAmountToCharacterStatsOnCombat` | `bool` | – | – |
| Simple Stat Info List | `simpleStatInfoList` | `List<simpleStatInfo>` | new List<simpleStatInfo> () | – |

### Target Selection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Select Target In Order | `selectTargetInOrder` | `bool` | true | – |
| Select Random Target | `selectRandomTarget` | `bool` | – | – |
| Select Target By Character Priority | `selectTargetByCharacterPriority` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Turn Based Combat Action Active | `turnBasedCombatActionActive` | `bool` | – | – |
| Current Combat Position | `currentCombatPosition` | `Vector3` | – | – |
| Current Combat Rotation | `currentCombatRotation` | `Vector3` | – | – |
| Adjusting Character Position In Process | `adjustingCharacterPositionInProcess` | `bool` | – | – |
| Free Combat Active | `freeCombatActive` | `bool` | – | – |
| Main Turn Based Combat System Assigned | `mainTurnBasedCombatSystemAssigned` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Remote Event System | `mainRemoteEventSystem` | `remoteEventSystem` | – | – |
| Main Character To Receive Orders | `mainCharacterToReceiveOrders` | `characterToReceiveOrders` | – | – |
| Main Turn Based Combat System | `mainTurnBasedCombatSystem` | `turnBasedCombatSystem` | – | – |
| Main AI Turn Based Combat System Brain | `mainAITurnBasedCombatSystemBrain` | `AITurnBasedCombatSystemBrain` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Combat Active | `useEventOnCombatActive` | `bool` | – | – |
| Event On Combat Active | `eventOnCombatActive` | `UnityEvent` | – | – |
| Use Event On Combat Deactivate | `useEventOnCombatDeactivate` | `bool` | – | – |
| Event On Combat Deactivate | `eventOnCombatDeactivate` | `UnityEvent` | – | – |
| Use Events If Character Alive After Combat | `useEventsIfCharacterAliveAfterCombat` | `bool` | – | – |
| Events If Character Alive After Combat | `eventsIfCharacterAliveAfterCombat` | `UnityEvent` | – | – |
| Use Events If Character Dead After Combat | `useEventsIfCharacterDeadAfterCombat` | `bool` | – | – |
| Events If Character Dead After Combat | `eventsIfCharacterDeadAfterCombat` | `UnityEvent` | – | – |
| Use Events On Character Current Turn Start | `useEventsOnCharacterCurrentTurnStart` | `bool` | – | – |
| Events On Character Current Turn Start | `eventsOnCharacterCurrentTurnStart` | `UnityEvent` | – | – |
| Use Event On Current Character Turn | `useEventOnCurrentCharacterTurn` | `bool` | – | – |
| Event On Current Character Turn | `eventOnCurrentCharacterTurn` | `UnityEvent` | – | – |
| Use Event On Current Team Turn | `useEventOnCurrentTeamTurn` | `bool` | – | – |
| Event On Current Team Turn | `eventOnCurrentTeamTurn` | `UnityEvent` | – | – |
| Use Event On Each Turn | `useEventOnEachTurn` | `bool` | – | – |
| Event On Each Turn | `eventOnEachTurn` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCanUseExtraTurnsState(bool state)` | `canUseExtraTurns`を設定するだけ。 |
| `setAmountOfExtraTurnsValue(int amount)` | `amountOfExtraTurns`を設定するだけ。 |
| `isCanUseExtraTurnsActive()` | `canUseExtraTurns`を返すだけ。 |
| `getAmountOfExtraTurns()` | `amountOfExtraTurns`を返すだけ。 |
| `isTurnBasedCombatActionActive()` | `turnBasedCombatActionActive`を返すだけ。 |
| `setTurnBasedCombatActionActiveState(bool state)` | 戦闘アクション状態を設定し、有効化時はメインシステム初期化と開始イベント、無効化時は終了イベントを実行する。 |
| `setCurrentCombatPositionAndRotationValues(Vector3 currentCombatPositionValues, Vector3 currentCombatRotationValues)` | 戦闘開始時の基準位置と回転を保存するだけ。 |
| `resetToCurrrentCombatPositionAndRotation(bool setPositionAtOnce)` | `setPositionAtOnce`なら即座に、そうでなければ移動コルーチンで保存した戦闘位置と回転へ戻す。 |
| `setCharacterPositionAtonce(Vector3 targetPosition, Vector3 targetRotation, bool adjustPlayerCameraTransform)` | 移動を止めて指定位置・回転へ即時移動し、フラグが立っていればカメラも同じ位置・回転に合わせる。 |
| `activateCharacterMovement(Vector3 targetPosition, Vector3 targetRotation, bool adjustPlayerCameraTransform)` | 移動を止めたうえで、指定位置・回転へ補間移動するコルーチンを開始する。 |
| `stopMovement()` | 移動コルーチンを停止し、位置調整中フラグを下ろすだけ。 |
| `activateOrder(string orderName)` | `mainCharacterToReceiveOrders`に`orderName`の注文を実行させるだけ。 |
| `activateOrderToAIBrain(string orderName)` | AIブレインに`orderName`の攻撃を実行させるだけ。 |
| `isAdjustingCharacterPositionInProcess()` | 位置調整中かどうかのフラグを返すだけ。 |
| `checkEventsForAliveOrDeadAfterCombat(bool state)` | `state`に応じて戦闘後の生存時または死亡時イベントを、それぞれ有効なら発火する。 |
| `checkEventsOnCharacterCurrentTurnStart()` | `useEventsOnCharacterCurrentTurnStart`が有効なら該当イベントを発火するだけ。 |
| `checkEventOnCurrentCharacterTurn()` | `useEventOnCurrentCharacterTurn`が有効なら該当イベントを発火するだけ。 |
| `checkEventOnCurrentTeamTurn()` | `useEventOnCurrentTeamTurn`が有効なら該当イベントを発火するだけ。 |
| `checkEventOnEachTurn()` | `useEventOnEachTurn`が有効なら該当イベントを発火するだけ。 |
| `checkTurnBasedCombatOnDamageReceived()` | 戦闘アクションが有効なら、UI更新とダメージ用エフェクト`activateEffect("")`を実行する。 |
| `updateAllCharacterStatsUIValue()` | 戦闘アクションが有効なら、メインのターン制戦闘システムにUI更新を依頼する。 |
| `setNextTurn()` | 戦闘アクションが有効なら、メインシステムに次ターンへの切り替えを依頼する。 |
| `setCurrentCommandNameUsed(string commandName)` | 戦闘アクションが有効なら、使用コマンド名をメインシステムへ通知する。 |
| `activateEffect(string effectName)` | 戦闘アクションが有効なら、メインシステムで指定エフェクトのイベントを発火させる。 |
| `setFreeCombatActiveState(bool state)` | `freeCombatActive`を設定するだけ。 |
| `checkIfCommandCanBeUsed(string commandName)` | ブロックリストが有効なら、`commandName`が含まれない場合のみtrueを返す。 |
| `checkIfCommandCategoryCanBeUsed(string commandCategoryName)` | ブロックリストが有効なら、指定カテゴリ名が含まれない場合のみtrueを返す。 |
| `checkTeamsDeadStateAfterCharacterDeath()` | 戦闘アクションが有効なら、自身のTransformを渡してチーム全滅判定をメインシステムに依頼する。 |
| `checkCharacterStateAfterResurrect()` | 戦闘アクションが有効なら、自身のTransformを渡して復活後の状態処理をメインシステムに依頼する。 |
| `checkPlayerStateOnDeathDuringCombat()` | 戦闘アクションが有効なら、メインシステムにプレイヤー死亡時の処理を依頼する。 |
| `inputConfirmCommand()` | 戦闘アクションが有効なら、メインシステムへコマンド確定入力を転送する。 |
| `inputCancelCommand()` | 戦闘アクションが有効なら、メインシステムへコマンドキャンセル入力を転送する。 |
| `inputSelectNextTarget()` | 戦闘アクションが有効なら、メインシステムへ次ターゲット選択入力を転送する。 |
| `inputSelectPreviousTarget()` | 戦闘アクションが有効なら、メインシステムへ前ターゲット選択入力を転送する。 |
| `inputToggleCombatMode()` | 戦闘アクションまたはフリー戦闘が有効なら、メインシステムへ戦闘モード切替入力を転送する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCombatActive` | `UnityEvent` | – |
| `eventOnCombatDeactivate` | `UnityEvent` | – |
| `eventsIfCharacterAliveAfterCombat` | `UnityEvent` | – |
| `eventsIfCharacterDeadAfterCombat` | `UnityEvent` | – |
| `eventsOnCharacterCurrentTurnStart` | `UnityEvent` | – |
| `eventOnCurrentCharacterTurn` | `UnityEvent` | – |
| `eventOnCurrentTeamTurn` | `UnityEvent` | – |
| `eventOnEachTurn` | `UnityEvent` | – |

## 内部型

- `simpleStatInfo`（class）
