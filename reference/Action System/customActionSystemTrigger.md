# customActionSystemTrigger

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Action System/customActionSystemTrigger.cs:5`

**概要**: トリガーの入退室をフックに、`playerActionSystem`のカスタムアクションを名前指定で開始/停止する補助コンポーネント。角度・距離条件と`actionTransform`の差し替えに対応する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Action On Enter | `activateActionOnEnter` | `bool` | – | – |
| Activate Action On Exit | `activateActionOnExit` | `bool` | – | – |
| Action To Activate Name | `actionToActivateName` | `string` | – | – |
| Stop Action Active | `stopActionActive` | `bool` | – | – |

### Condition Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Min Angle To Activate Action | `useMinAngleToActivateAction` | `bool` | – | – |
| Min Angle To Activate Action | `minAngleToActivateAction` | `float` | – | – |
| Check Opposite Angle | `checkOppositeAngle` | `bool` | – | – |
| Action System Direction Transform | `actionSystemDirectionTransform` | `Transform` | – | – |
| Use Min Distance To Activate Action | `useMinDistanceToActivateAction` | `bool` | – | – |
| Min Distance To Activate Action | `minDistanceToActivateAction` | `float` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Custom Action System Transform | `setCustomActionSystemTransform` | `bool` | – | – |
| Custom Action System Transform | `customActionSystemTransform` | `Transform` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPlayerOnEnter(GameObject newPlayer)` | `activateActionOnEnter`が有効なら入室したプレイヤーで`activateCustomAction`を呼ぶ。 |
| `setPlayerOnExit(GameObject newPlayer)` | `activateActionOnExit`が有効なら退室したプレイヤーで`activateCustomAction`を呼ぶ。 |
| `activateCustomAction(GameObject newPlayer)` | 角度と距離の条件を満たす場合のみ、`stopActionActive`なら停止、そうでなければ`actionTransform`を差し替えてアクションを起動する。 |
