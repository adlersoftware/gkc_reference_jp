# externalStatsManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Stats System/externalStatsManager.cs:5`

**概要**: `playerStatsSystem`への外部更新を中継するクラス。一時的なステータス名を保持し、無効時は何もしない。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Stats System | `mainPlayerStatsSystem` | `playerStatsSystem` | – | – |
| Stats Manager Enabled | `statsManagerEnabled` | `bool` | true | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setTemporalStatName(string statName)` | 有効時のみ、一時的なステータス名`temporalStatName`を保持する。 |
| `updatePlayerStateOfTemporalStat(float statExtraValue)` | 有効かつ名前が空でなければ、保持した名前で値を更新し、その後名前を空にする。 |
| `updateStatValueExternally(string statName, float newValue)` | 有効時のみ、`mainPlayerStatsSystem`の同名メソッドへ値をそのまま渡す。 |
| `updateStatValueExternally(int statIndex, float newValue)` | 有効時のみ、`mainPlayerStatsSystem`のインデックス指定版へ値をそのまま渡す。 |
