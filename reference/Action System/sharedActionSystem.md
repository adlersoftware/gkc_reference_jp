# sharedActionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Action System/Shared Action System/sharedActionSystem.cs:8`

**概要**: キャラクター同士で共有するアクションを管理するコンポーネント。アクション名から情報を検索して条件判定を行い、成立するとアクション用オブジェクトを配置して2体のキャラのアクションを同期再生する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shared Action Enabled | `sharedActionEnabled` | `bool` | true | – |
| Check Character Status To Stop Shared Action Enabled | `checkCharacterStatusToStopSharedActionEnabled` | `bool` | true | – |

### Shared Action List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shared Action System Info List | `sharedActionSystemInfoList` | `List<sharedActionSystemInfo>` | new List<sharedActionSystemInfo> () | – |

### Shared Action Activated Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remote Shared Action System Info List | `remoteSharedActionSystemInfoList` | `List<remoteSharedActionSystemInfo>` | new List<remoteSharedActionSystemInfo… | – |

### Shared Action Activated Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Random Shared Action Info List Enabled | `useRandomSharedActionInfoListEnabled` | `bool` | – | – |
| Random Shared Action Info List | `randomSharedActionInfoList` | `List<randomSharedActionInfo>` | new List<randomSharedActionInfo> () | – |

### Actions To Ignore Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Actions To Ignore List | `useActionsToIgnoreList` | `bool` | – | – |
| Actions To Ignore List | `actionsToIgnoreList` | `List<string>` | new List<string> () | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Stats Check Enabled | `ignoreStatsCheckEnabled` | `bool` | – | – |
| Ignore Shared Action Zones Enabled | `ignoreSharedActionZonesEnabled` | `bool` | – | – |

### AI Around Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pause AI Around During Action Active | `pauseAIAroundDuringActionActive` | `bool` | – | – |
| Pause AI Attack Around During Action Active | `pauseAIAttackAroundDuringActionActive` | `bool` | – | – |
| Enable Random Walk On AI Around During Action Active | `enableRandomWalkOnAIAroundDuringActionActive` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| First Character Is Player | `firstCharacterIsPlayer` | `bool` | – | – |
| Shared Action Active | `sharedActionActive` | `bool` | – | – |
| First Character | `firstCharacter` | `GameObject` | – | – |
| Second Character | `secondCharacter` | `GameObject` | – | – |
| Current External Character | `currentExternalCharacter` | `GameObject` | – | – |
| Last Shared Action Found | `lastSharedActionFound` | `bool` | – | – |
| Using Shared Action Zone Result | `usingSharedActionZoneResult` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Shared Action Activated | `useEventsOnSharedActionActivated` | `bool` | – | – |
| Events On Shared Action Activated | `eventsOnSharedActionActivated` | `UnityEvent` | – | – |
| Use Events On Shared Action Condition Not Achieved | `useEventsOnSharedActionConditionNotAchieved` | `bool` | – | – |
| Events On Shared Action Condition Not Achieved | `eventsOnSharedActionConditionNotAchieved` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Transform | `characterTransform` | `GameObject` | – | – |
| Main Player Stats System | `mainPlayerStatsSystem` | `playerStatsSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setExternalCharacter(GameObject newCharacter)` | `currentExternalCharacter`に`newCharacter`を設定するだけ。 |
| `setFirstCharacter(GameObject newCharacter)` | `firstCharacter`に`newCharacter`を設定するだけ。 |
| `setSecondCharacter(GameObject newCharacter)` | `secondCharacter`に`newCharacter`を設定するだけ。 |
| `isLastSharedActionFound()` | 直前のアクション起動が成功したかどうかを返すだけ。 |
| `isSharedActionEnabled()` | `sharedActionEnabled`の値を返すだけ。 |
| `isSharedActionActive()` | `sharedActionActive`の値、つまり共有アクション実行中かどうかを返すだけ。 |
| `activateRandomSharedActionByName(string actionName)` | ランダム設定が有効な時、`actionName`の情報から無作為に選んだ名前で起動する。 |
| `activateSharedActionByName(string actionName)` | 名前で条件を判定し、成功時は`lastSharedActionFound`をtrueにしてコルーチンを開始、失敗時はイベント発火。 |
| `stopUpdateCoroutine()` | `updateCoroutine`が実行中なら停止するだけ。 |
| `stopSharedActionDueToCharactersUnableToFinish()` | 両キャラのアクションと待機状態を解除し、`sharedActionActive`をfalseにしてオブジェクトを非表示にする。 |
| `setSharedActionEnabledState(bool state)` | `sharedActionEnabled`に`state`を設定するだけ。 |
| `setSharedActionEnabledStateFromEditor(bool state)` | 状態を設定した後、`updateComponent`でシーンを更新するエディタ用関数。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventsOnSharedActionActivated` | `UnityEvent` | – |
| `eventsOnSharedActionConditionNotAchieved` | `UnityEvent` | – |

## 内部型

- `sharedActionSystemInfo`（class）
- `randomSharedActionInfo`（class）
- `sharedActionTemporalInfo`（class）
