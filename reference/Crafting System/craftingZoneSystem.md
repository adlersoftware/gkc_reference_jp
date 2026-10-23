# craftingZoneSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Crafting System/craftingZoneSystem.cs:5`

**概要**: トリガーゾーン。タグ一致のプレイヤーが出入りした際に、配置モードの一時停止状態を切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Check | `tagToCheck` | `string` | – | – |
| Set Crafting Zone Enabled State | `setCraftingZoneEnabledState` | `bool` | – | – |
| Crafting Zone Enabled State | `craftingZoneEnabledState` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | タグ一致時のみ、入場でゾーン設定を反転した一時停止状態にし、退場で保存済みの元状態に戻す。 |
