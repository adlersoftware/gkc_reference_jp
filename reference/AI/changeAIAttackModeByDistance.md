# changeAIAttackModeByDistance

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/changeAIAttackModeByDistance.cs:5`

**概要**: ターゲットとの距離に応じてAIの攻撃モードを近距離/遠距離（ランダム選択可）へ切り替え、距離が離れている時はスプリントさせるコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Attack Mode Based On Distance To Target | `changeAttackModeBasedOnDistanceToTarget` | `bool` | – | – |
| Max Distance For Short Range Attack Mode | `maxDistanceForShortRangeAttackMode` | `float` | – | – |
| Short Range Attack Mode Name | `shortRangeAttackModeName` | `string` | – | – |
| Long Range Attack Mode Name | `longRangeAttackModeName` | `string` | – | – |
| Use Random Short Range Attack Mode | `useRandomShortRangeAttackMode` | `bool` | – | – |
| Random Short Range Attack Mode List | `randomShortRangeAttackModeList` | `List<string>` | new List<string> () | – |
| Use Random Long Range Attack Mode | `useRandomLongRangeAttackMode` | `bool` | – | – |
| Random Long Range Attack Mode List | `randomLongRangeAttackModeList` | `List<string>` | new List<string> () | – |

### Sprint Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Sprint Based On Distance To Target | `useSprintBasedOnDistanceToTarget` | `bool` | – | – |
| Min Distance To Target To Sprint | `minDistanceToTargetToSprint` | `float` | – | – |

### Debug Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Short Range Attack Mode Active | `shortRangeAttackModeActive` | `bool` | – | – |
| Long Range Attack Mode Active | `longRangeAttackModeActive` | `bool` | – | – |
| Ignore Change Attack Mode Based On Distance To Target | `ignoreChangeAttackModeBasedOnDistanceToTarget` | `bool` | – | – |
| Sprint Active | `sprintActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `initializeElements()` | `mainPlayerController`が未設定なら`mainFindObjectivesSystem`から取得して保持する。 |
| `checkChangeAttackModeBasedOnDistanceToTarget()` | 距離が`maxDistanceForShortRangeAttackMode`未満なら近距離、以上なら遠距離モードへ切り替え、遠い時は走らせる。 |
| `resetAttackModeActiveState()` | 近距離/遠距離のフラグを下ろし、スプリント中なら`forceStopRun`で停止する。 |
| `setChangeAttackModeBasedOnDistanceToTargetState(bool state)` | `changeAttackModeBasedOnDistanceToTarget`を設定するだけ。 |
| `setIgnoreChangeAttackModeBasedOnDistanceToTargetState(bool state)` | `ignoreChangeAttackModeBasedOnDistanceToTarget`を設定するだけ。 |
| `setUseSprintBasedOnDistanceToTargetState(bool state)` | `useSprintBasedOnDistanceToTarget`を設定するだけ。 |
| `setChangeAttackModeBasedOnDistanceToTargetStateFromEditor(bool state)` | 設定を反映したうえで`updateComponent`を呼び、シーンをダーティにする。 |
| `setUseSprintBasedOnDistanceToTargetStateFromEditor(bool state)` | 設定を反映したうえで`updateComponent`を呼び、シーンをダーティにする。 |
