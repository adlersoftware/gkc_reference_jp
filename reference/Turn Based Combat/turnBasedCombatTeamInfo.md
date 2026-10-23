# turnBasedCombatTeamInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Turn Based Combat/turnBasedCombatTeamInfo.cs:6`

**概要**: 1チーム分のキャラクターリストとチーム設定を保持するコンポーネント。リーダー判定、敗北イベントや相手チームへの報酬・経験値付与を扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Is Team Leader | `isTeamLeader` | `bool` | – | – |
| Use Team Position Data Name | `useTeamPositionDataName` | `bool` | – | – |
| Team Position Data Name | `teamPositionDataName` | `string` | – | – |
| This Team Always Select First | `thisTeamAlwaysSelectFirst` | `bool` | – | – |
| Use Custom Camera State | `useCustomCameraState` | `bool` | – | – |
| Custom Camera State | `customCameraState` | `string` | – | – |

### Character Team List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Team List | `characterTeamList` | `List<GameObject>` | new List<GameObject> () | – |

### Rewads Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Team Defeated | `useEventOnTeamDefeated` | `bool` | – | – |
| Event On Team Defeated | `eventOnTeamDefeated` | `UnityEvent` | – | – |
| Use Event On Reward For Opponent Team | `useEventOnRewardForOpponentTeam` | `bool` | – | – |
| Event On Reward For Opponent Team | `eventOnRewardForOpponentTeam` | `eventParameters.eventToCallWithGameObject` | – | – |
| Use Reward System | `useRewardSystem` | `bool` | – | – |
| Main Reward System | `mainRewardSystem` | `objectExperienceSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `isTeamLeaderValue()` | `isTeamLeader`を返すだけ。 |
| `removeDeadCharactersFromTeam()` | チームリストからnullまたは死亡しているキャラクターを削除する。 |
| `clearCharacterTeamList()` | チームリストを空にするだけ。 |
| `getCharacterTeamList()` | `characterTeamList`を返すだけ。 |
| `setCharacterTeamList(List<GameObject> newList)` | `characterTeamList`を`newList`に置き換えるだけ。 |
| `addCharacterToTeamList(GameObject newCharacter)` | 未登録なら`newCharacter`をチームリストへ追加するだけ。 |
| `removeCharacterToTeamList(GameObject newCharacter)` | 登録済みなら`newCharacter`をチームリストから削除するだけ。 |
| `checkEventsOnTeamDefeated()` | `useEventOnTeamDefeated`が有効なら敗北イベントを発火するだけ。 |
| `checkEventOnRewardForOpponentTeam(List<GameObject> opponentTeamList)` | 報酬イベントが有効なら相手チームの各キャラクターへイベントを発火し、報酬システムがあれば経験値も付与する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnTeamDefeated` | `UnityEvent` | – |
