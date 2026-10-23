# AIAroundManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/AIAroundManager.cs:6`

**概要**: 周囲のAI（`findObjectivesSystem`）を登録し、1体ずつ攻撃を許可する制御を行うマネージャ。一定間隔のコルーチンで待機状態、ランダムウォーク、動的障害物検出を切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| AI Manager Enabled | `AIManagerEnabled` | `bool` | true | – |
| Max Distance To Set State On AI | `maxDistanceToSetStateOnAI` | `float` | – | – |
| Only Store AI And Ignore To Set States | `onlyStoreAIAndIgnoreToSetStates` | `bool` | – | – |

### AI Management Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Time To Assign Attack To Next AI | `timeToAssignAttackToNextAI` | `float` | – | – |

### Dynamic Obstacle Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Dynamic Obstacle Detection | `useDynamicObstacleDetection` | `bool` | – | – |
| Use Random Walk Enabled | `useRandomWalkEnabled` | `bool` | – | – |
| Min Obstacle Rotation | `minObstacleRotation` | `float` | 45 | – |
| Medium Obstacle Rotation | `mediumObstacleRotation` | `float` | 65 | – |
| Maximum Obstacle Rotation | `maximumObstacleRotation` | `float` | 85 | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Send Info To Turn Based Combat System Enabled | `sendInfoToTurnBasedCombatSystemEnabled` | `bool` | – | – |
| Main Turn Based Combat System Panel Name | `mainTurnBasedCombatSystemPanelName` | `string` | "Turn Combat System" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Pause Attacks On All AI Around | `pauseAttacksOnAllAIAround` | `bool` | – | – |
| AI Manager Active | `AIManagerActive` | `bool` | – | – |
| Current Targets Amount | `currentTargetsAmount` | `int` | – | – |
| Last AI Attack Assigned Index | `lastAIAttackAssignedIndex` | `int` | -1 | – |
| Characters Around | `charactersAround` | `List<Transform>` | new List<Transform> () | – |

### Events

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Targets Change | `useEventsOnTargetsChange` | `bool` | – | – |
| Event On Targets Detected | `eventOnTargetsDetected` | `UnityEvent` | – | – |
| Event On Targets Removed | `eventOnTargetsRemoved` | `UnityEvent` | – | – |
| Use Event On First Target Detected | `useEventOnFirstTargetDetected` | `bool` | – | – |
| Event On First Target Detected | `eventOnFirstTargetDetected` | `UnityEvent` | – | – |
| Use Event On Last Target Removed | `useEventOnLastTargetRemoved` | `bool` | – | – |
| Event On Last Target Removed | `eventOnLastTargetRemoved` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Turn Based Combat System | `mainTurnBasedCombatSystem` | `turnBasedCombatSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`が動いていれば停止するだけ。 |
| `addCharacterAround(Transform newCharacter)` | 対象を`charactersAround`に追加して`findObjectivesSystem`を取得し、2体以上なら攻撃順制御コルーチンを開始する。 |
| `removeCharacterAround(Transform newCharacter)` | 対象をリストから外して通常状態に戻し、残り1体以下なら制御コルーチンを停止する。 |
| `clearCharactersAround()` | 全対象の待機・動的障害物・ランダムウォーク設定を戻してリストを空にし、コルーチンを止める。 |
| `getCharactersAround()` | `charactersAround`を返すだけ。 |
| `characterDetectedByAIAround()` | 登録AIのいずれかが`isOnSpotted`なら`true`を返す。 |
| `checkIfPlayerDetectedByAIAround(GameObject mainPlayerGameObject)` | スポット中かつ攻撃対象が指定プレイヤーであるAIがいるかを返す。 |
| `getMinDistanceToPlayer(Transform playerTransform, bool ignoreIfPlayerIsCurrentTarget)` | スポット中のAIから最短距離を返し（真なら全AI、偽なら攻撃対象がプレイヤーのAIのみ）、無ければ-1。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnTargetsDetected` | `UnityEvent` | – |
| `eventOnTargetsRemoved` | `UnityEvent` | – |
| `eventOnFirstTargetDetected` | `UnityEvent` | – |
| `eventOnLastTargetRemoved` | `UnityEvent` | – |
