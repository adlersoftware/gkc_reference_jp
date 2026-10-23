# wallSlideJumpZoneSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/wallSlideJumpZoneSystem.cs:5`

**概要**: 壁スライド用ゾーンのトリガー。入場時に滑り落ち速度と減速設定を適用して検出を有効化し、退場時に元へ戻す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Check | `tagToCheck` | `string` | – | – |
| Slide Zone Active | `slideZoneActive` | `bool` | true | – |
| Slide Down Speed Multiplier | `slideDownSpeedMultiplier` | `float` | 1 | – |
| Force Slow Down On Surface Active | `forceSlowDownOnSurfaceActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | 入場時に滑り落ち速度倍率と表面減速を設定して壁スライド検出を有効化し、退場時に倍率1・減速なし・検出無効へ戻す。 |
