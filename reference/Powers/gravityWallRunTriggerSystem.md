# gravityWallRunTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/gravityWallRunTriggerSystem.cs:5`

**概要**: `tagToCheck`のプレイヤーがトリガーに出入りすると、その`gravityWallRunSystem`の壁走りやアニメ速度を外部から切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Check | `tagToCheck` | `string` | – | – |
| Wall Running Zone Active | `wallRunningZoneActive` | `bool` | true | – |
| Activate Run Action | `activateRunAction` | `bool` | – | – |
| Stop Wall Running On Enter | `stopWallRunningOnEnter` | `bool` | – | – |
| Stop Wall Running On Exit | `stopWallRunningOnExit` | `bool` | – | – |
| Set New Anim Speed Multiplier On Wall Run | `setNewAnimSpeedMultiplierOnWallRun` | `bool` | – | – |
| Anim Speed Multiplier On Wall Run | `animSpeedMultiplierOnWallRun` | `float` | 2 | – |
| Set Force Walk Wall Active Externally | `setForceWalkWallActiveExternally` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | `isEnter`が真なら対象プレイヤーの壁走りを開始し、偽なら停止・アニメ速度復元・強制歩行解除を行う。 |
