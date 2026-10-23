# AIPatrolSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/AIPatrolSystem.cs:7`

**概要**: `AIWayPointPatrol`の巡回リストを使い、最寄り・次・ランダムなウェイポイントを選んで待ち時間コルーチンを挟みながら`AINavMesh`の目標と速度を更新する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Paused | `paused` | `bool` | – | – |
| Min Distance To Next Point | `minDistanceToNextPoint` | `float` | 0.6f | – |
| Patrol Speed | `patrolSpeed` | `float` | 0.2f | – |
| Return To Patrol Speed | `returnToPatrolSpeed` | `float` | 1 | – |
| Move On Reverse Patrol Direction Enabled | `moveOnReversePatrolDirectionEnabled` | `bool` | – | – |
| Use Current Patrol Index On Start | `useCurrentPatrolIndexOnStart` | `bool` | – | – |
| Current Patrol Index | `currentPatrolIndex` | `int` | 0 | – |

### Patrol Time Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use General Wait Time | `useGeneralWaitTime` | `bool` | true | – |
| General Wait Time Between Points | `generalWaitTimeBetweenPoints` | `float` | – | – |
| Move Between Patrols In Order | `moveBetweenPatrolsInOrder` | `bool` | true | – |
| Fixed Time To Change Between Patrols | `fixedTimeToChangeBetweenPatrols` | `float` | – | – |

### Random Patrol Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Between Point Randomly | `changeBetweenPointRandomly` | `bool` | true | – |
| Change Randomly Probability | `changeRandomlyProbability` | `int` | 1 | Range (0, 10) |
| Use Time To Change Between Point Randomly | `useTimeToChangeBetweenPointRandomly` | `bool` | – | – |
| Use Random Time To Change Patrol | `useRandomTimeToChangePatrol` | `bool` | – | – |
| Random Time Limits | `randomTimeLimits` | `Vector2` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Returning To Patrol | `returningToPatrol` | `bool` | – | – |
| AI Is Destroyed | `AIIsDestroyed` | `bool` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Radius | `gizmoRadius` | `float` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Patrol Wait | `useEventsOnPatrolWait` | `bool` | – | – |
| Events On Patrol Wait | `eventsOnPatrolWait` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Patrol Path | `patrolPath` | `AIWayPointPatrol` | – | An AIWayPointPatrol path in your scene that this AI should follow. To create one add a GameObject with AIWayPointPatrol component and edit the Way Points then drag the GameObject here. |
| AI Character | `AICharacter` | `Transform` | – | – |
| Main AI Navmesh | `mainAINavmesh` | `AINavMesh` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `pauseOrPlayPatrol(bool state)` | `paused`を設定し、デバッグ時のみログを出す。 |
| `isPatrolPaused()` | `paused`を返すだけ。 |
| `closestWaypoint(Vector3 currentPosition)` | 指定位置に最も近いウェイポイントを探して`currentPatrolIndex`等を更新し、そのTransformを返す。 |
| `setNextPatrolList()` | 次の巡回リストへ進み（末尾は0に戻る）、その中の最寄り地点を新しい目標に設定する。 |
| `setNextWaypoint()` | 前のコルーチンを止め、待ち時間後に次（逆順設定時は前）のウェイポイントへ進めるコルーチンを開始する。 |
| `setNextRandomWaypoint()` | 待ち時間後に別の巡回リストとウェイポイントをランダムに選ぶコルーチンを開始する。 |
| `setClosestWayPoint()` | 最寄りウェイポイントを現在の目標に設定し、巡回を有効化して速度を適用する。 |
| `setCurrentPatrolTarget(Transform newTarget)` | `AINavMesh`に巡回目標を渡し、巡回状態を有効にする。 |
| `setReturningToPatrolState(bool state)` | 引数は使わず復帰フラグを立て、復帰用速度を`AINavMesh`に設定する。 |
| `resumePatrolStateOnAI()` | 巡回の一時停止を解除し、最寄りウェイポイントから巡回を再開する。 |
| `pausePatrolStateOnAI()` | 巡回を一時停止し、`AINavMesh`の巡回状態を無効にする。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventsOnPatrolWait` | `UnityEvent` | – |
