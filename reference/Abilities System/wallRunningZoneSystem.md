# wallRunningZoneSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/wallRunningZoneSystem.cs:5`

**概要**: ゾーンに入ったプレイヤーの壁走り設定を切り替えるトリガー。退出時には元の壁走り設定へ戻す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Check | `tagToCheck` | `string` | – | – |
| Wall Running Zone Active | `wallRunningZoneActive` | `bool` | true | – |
| Wall Running Enabled | `wallRunningEnabled` | `bool` | true | – |
| Auto Use Down Movement On Wall Running Active | `autoUseDownMovementOnWallRunningActive` | `bool` | – | – |
| Auto Use Stop Wall Runnig After Delay | `autoUseStopWallRunnigAfterDelay` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | 対象タグのプレイヤーなら、`isEnter` に応じて壁走り設定を適用し、退出時は元の状態に戻す。 |
