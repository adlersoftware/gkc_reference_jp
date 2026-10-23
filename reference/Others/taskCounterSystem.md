# taskCounterSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/taskCounterSystem.cs:6`

**概要**: タスクの達成数を数えるカウンターで、指定タスクの完了/取消、順序制約、完了・取り消しイベント、リセット処理を提供する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Task Counter Enabled | `taskCounterEnabled` | `bool` | true | – |
| Number Of Tasks | `numberOfTasks` | `int` | – | – |
| Reset Counter On Task Complete | `resetCounterOnTaskComplete` | `bool` | – | – |

### Task Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Task Info List | `taskInfoList` | `List<taskInfo>` | new List<taskInfo> () | – |
| Make Tasks In Order Enabled | `makeTasksInOrderEnabled` | `bool` | – | – |
| Reset Task Counter On Incorrect Order | `resetTaskCounterOnIncorrectOrder` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Task Counter | `currentTaskCounter` | `int` | – | – |
| Task Complete | `taskComplete` | `bool` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Task Counter Complete | `eventOnTaskCounterComplete` | `UnityEvent` | – | – |
| Check If Undo Task Complete | `checkIfUndoTaskComplete` | `bool` | – | – |
| Event On Undo Task Complete | `eventOnUndoTaskComplete` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `increaseTaskCounter()` | `increaseMultipleTaskCounter(1)` を呼ぶだけ。 |
| `decreaseTaskCounter()` | `increaseMultipleTaskCounter(-1)` でカウンタを1減らす。 |
| `completeTaskCounter()` | `numberOfTasks` 分を加算して一気に完了状態にする。 |
| `addTaskCompleteState(string taskName)` | 指定名の未完了タスクを完了にしてカウンタを1増やし、順序設定に反する場合は処理しない。 |
| `removeTaskCompleteState(string taskName)` | 指定名の完了済みタスクを未完了に戻してカウンタを1減らす。 |
| `resetTasksListCompleteState()` | 全タスクの完了状態とカウンタをリセットする。 |
| `decreaseMultipleTaskCounter(int newValue)` | 符号を反転して `increaseMultipleTaskCounter` に委譲するだけ。 |
| `increaseMultipleTaskCounter(int newValue)` | カウンタを加減し、上限到達で完了イベント、減少時に完了取り消しイベントを発火する。 |
| `setTaskCounterEnabledState(bool state)` | `taskCounterEnabled` を設定するだけ。 |
| `resetTaskCounter()` | `currentTaskCounter` を0にするだけ。 |
| `setTaskCompleteState(bool state)` | `taskComplete` を設定するだけ。 |
| `resetTaskCounterAndDisableTaskComplete()` | カウンタを0に戻し、同時に完了フラグも false にする。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnTaskCounterComplete` | `UnityEvent` | – |
| `eventOnUndoTaskComplete` | `UnityEvent` | – |

## 内部型

- `taskInfo`（class）
