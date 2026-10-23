# ledgeZoneSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Climb System/ledgeZoneSystem.cs:5`

**概要**: レッジゾーンのトリガーで、プレイヤーの登攀可否やレイキャスト距離などを一時的に切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Check | `tagToCheck` | `string` | – | – |
| Ledge Zone Active | `ledgeZoneActive` | `bool` | true | – |
| Check Down Raycast Offset | `checkDownRaycastOffset` | `Vector3` | – | – |
| Climb Ledge Forward Ray Distance | `climbLedgeForwardRayDistance` | `float` | – | – |
| Climb Ledge Down Ray Distance | `climbLedgeDownRayDistance` | `float` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ledge Zone Can Be Climbed | `ledgeZoneCanBeClimbed` | `bool` | true | – |
| Avoid Player Grab Ledge | `avoidPlayerGrabLedge` | `bool` | – | – |
| Can Check For Hang From Ledge On Ground | `canCheckForHangFromLedgeOnGround` | `bool` | true | – |
| Only Hang From Ledge If Player Is Not Moving | `onlyHangFromLedgeIfPlayerIsNotMoving` | `bool` | true | – |
| Can Grab Any Surface On Air Active | `canGrabAnySurfaceOnAirActive` | `bool` | true | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | 対象タグのプレイヤーへゾーン検出状態・レイ距離・各種可否を設定し、退出時に元の値へ戻す。 |
