# GKCConditionInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Condition System/GKCConditionInfo.cs:6`

**概要**: トリガーに進入したプレイヤーを対象に条件判定を行う基底コンポーネントで、完了/未完了イベントとコルーチンによる毎フレーム判定、トリガー出入りのイベントを提供する。実際の条件内容は派生クラスで実装する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Condition Check Enabled | `conditionCheckEnabled` | `bool` | – | – |
| Search Player On Scene If Not Assigned | `searchPlayerOnSceneIfNotAssigned` | `bool` | – | – |
| Layermask To Check | `layermaskToCheck` | `LayerMask` | – | – |
| Check Condition Complete On Trigger Enter Enabled | `checkConditionCompleteOnTriggerEnterEnabled` | `bool` | true | – |

### Coroutine Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Condition On Coroutine | `checkConditionOnCoroutine` | `bool` | – | – |
| Stop Coroutine On Condition Complete | `stopCoroutineOnConditionComplete` | `bool` | – | – |
| Stop Coroutine On Condition Not Complete | `stopCoroutineOnConditionNotComplete` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Condition Complete | `eventOnConditionComplete` | `UnityEvent` | – | – |
| Event On Condition Not Complete | `eventOnConditionNotComplete` | `UnityEvent` | – | – |
| Use Event On Trigger Enter | `useEventOnTriggerEnter` | `bool` | – | – |
| Event On Trigger Enter | `eventOnTriggerEnter` | `UnityEvent` | – | – |
| Use Event On Trigger Exit | `useEventOnTriggerExit` | `bool` | – | – |
| Event On Trigger Exit | `eventOnTriggerExit` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Check Condition Paused | `checkConditionPaused` | `bool` | – | – |
| Current Player | `currentPlayer` | `GameObject` | – | – |
| Coroutine Update In Process | `coroutineUpdateInProcess` | `bool` | – | – |
| Condition Coroutine | `conditionCoroutine` | `Coroutine` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `findPlayerOnScene()` | `searchPlayerOnSceneIfNotAssigned`がtrueなら、シーンのメインプレイヤーを`setCurrentPlayer`に渡す。 |
| `checkIfPlayerAssigned()` | 割当済みならtrue、未割当なら`findPlayerOnScene`で検索し、見つからなければ警告を出してfalseを返す。 |
| `setCurrentPlayer(GameObject newPlayer)` | `currentPlayer`を更新し、nullでなければ割当済みフラグをtrueにする。 |
| `checkIfConditionComplete()` | 本体が空で何もしない(派生クラスで条件判定を実装する)。 |
| `checkIfConditionCompleteAndReturnResult()` | 本体が空で、常にfalseを返す(派生クラスでの上書き用)。 |
| `setConditionResult(bool state)` | デバッグ出力後、結果に応じて完了/未完了イベントを実行し、対応する設定が有効なら更新コルーチンを停止する。 |
| `checkTriggerInfo(Collider col, bool isEnter)` | 有効かつ非ポーズ時、レイヤー一致を確認し、進入なら相手をプレイヤーとして条件システムへ登録して判定、退出なら解除して退出イベントを実行する。 |
| `setCheckConditionPausedState(bool state)` | `checkConditionPaused`に`state`を代入するだけ。 |
| `stopUpdateCoroutine()` | 実行中の`conditionCoroutine`をStopCoroutineし、更新中フラグをfalseにするだけ。 |
| `checkFunctionOnTriggerExit()` | コルーチン判定モードの時だけ`stopUpdateCoroutine`を呼ぶ。 |
| `checkConditionOnUpdateState()` | 本体が空で何もしない(`updateCoroutine`から毎FixedUpdate呼ばれる上書き用)。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnConditionComplete` | `UnityEvent` | – |
| `eventOnConditionNotComplete` | `UnityEvent` | – |
| `eventOnTriggerEnter` | `UnityEvent` | – |
| `eventOnTriggerExit` | `UnityEvent` | – |
