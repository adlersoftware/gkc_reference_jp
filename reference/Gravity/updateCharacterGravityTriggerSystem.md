# updateCharacterGravityTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Gravity/updateCharacterGravityTriggerSystem.cs:5`

**概要**: トリガーに入ったキャラクターの重力法線を、指定Transformの上方向へ切り替えるコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Update Gravity Enabled | `updateGravityEnabled` | `bool` | true | – |
| Player Tag | `playerTag` | `string` | "Player" | – |
| Ignore Update Gravity If Character Has Different Direction | `ignoreUpdateGravityIfCharacterHasDifferentDirection` | `bool` | – | – |
| Max Gravity Angle Difference | `maxGravityAngleDifference` | `float` | – | – |
| Ignore Recalculate Surface | `ignoreRecalculateSurface` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Gravity Direction Transform | `gravityDirectionTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerType(Collider col, bool isEnter)` | nullやトリガーのColliderを除外し、オブジェクトの重力判定へ渡す。 |
| `checkObjectOnGravitySystem(GameObject objectToCheck, bool isEnter)` | タグ一致時、角度差条件を満たせば`gravityDirectionTransform`の上方向で法線を更新する。 |
