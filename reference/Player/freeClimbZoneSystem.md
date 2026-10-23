# freeClimbZoneSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/freeClimbZoneSystem.cs:5`

**概要**: フリークライム可能なゾーン。プレイヤーがトリガーへ入退場したときにクライム検出の有効化と自動掴みを行い、親子付けの設定も公開する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Check | `tagToCheck` | `string` | – | – |
| Climb Zone Active | `climbZoneActive` | `bool` | true | – |
| Activate Climb Check On Trigger Enter | `activateClimbCheckOnTriggerEnter` | `bool` | true | – |
| Stop Climb On Trigger Exit | `stopClimbOnTriggerExit` | `bool` | – | – |
| Activate Climb State Automatically On Enter | `activateClimbStateAutomaticallyOnEnter` | `bool` | – | – |
| Climb Automatically Only If Player On Air | `climbAutomaticallyOnlyIfPlayerOnAir` | `bool` | – | – |

### Action Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Surface To Climb Enabled | `ignoreSurfaceToClimbEnabled` | `bool` | – | – |
| Allow Climb Surface On Input Enabled | `allowClimbSurfaceOnInputEnabled` | `bool` | – | – |
| Activate Auto Slide Down On Surface | `activateAutoSlideDownOnSurface` | `bool` | – | – |
| Movement Input Disabled On Surface | `movementInputDisabledOnSurface` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Player As Child | `setPlayerAsChild` | `bool` | – | – |
| Player Parent Transform | `playerParentTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | ゾーン有効かつタグ一致時、入場ならクライム検出を有効化して設定に応じ自動で掴み、退場なら設定に応じ検出を無効化する。 |
| `checkPlayerParentState()` | 子化設定が有効なら親Transformを、無効なら null を返す。 |
| `isIgnoreSurfaceToClimbEnabled()` | `ignoreSurfaceToClimbEnabled` を返すだけ。 |
| `setIgnoreSurfaceToClimbEnabledState(bool state)` | `ignoreSurfaceToClimbEnabled` を設定するだけ。 |
| `isAllowClimbSurfaceOnInputEnabled()` | `allowClimbSurfaceOnInputEnabled` を返すだけ。 |
