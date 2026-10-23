# objectsStatsSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Stats System/Objects Stats/objectsStatsSystem.cs:5`

**概要**: 複数の`objectStatsSystem`をリストで管理し、名前からの参照や有効状態の切り替えを行う。`increaseStat`は本体が未実装。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Objects Stats System Enabled | `objectsStatsSystemEnabled` | `bool` | true | – |
| Object Stats System List | `objectStatsSystemList` | `List<objectStatsSystem>` | new List<objectStatsSystem> () | – |

### Object Stats Template Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Stats Info Template Data List | `objectStatsInfoTemplateDataList` | `List<objectStatsInfoTemplateData>` | new List<objectStatsInfoTemplateData> () | – |

### Object Stats List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Stats Info List | `objectStatsInfoList` | `List<objectStatsInfo>` | new List<objectStatsInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getObjectStatsInfoTemplateDataList()` | `objectStatsInfoTemplateDataList`をそのまま返すだけ。 |
| `addObjectStatsSystem(objectStatsSystem newObjectStatsSystem)` | 有効時のみ、リストに未登録の`objectStatsSystem`を追加する。 |
| `getStatsFromObjectByName(string objectName)` | 名前一致のオブジェクトのテンプレートから`objectStatInfoList`を返し、無効や不一致ならnull。 |
| `objectCanBeUpgraded(string objectName)` | 名前一致のオブジェクトが登録されているかを返し、システム無効時はfalse。 |
| `increaseStat(string statName, float statExtraValue)` | 本体はコメントアウトされており、有効判定のみで実際の加算は行わない。 |
| `setObjectsStatsSystemEnabledState(bool state)` | `objectsStatsSystemEnabled`を設定するだけ。 |
| `setObjectsStatsSystemEnabledStateFromEditor(bool state)` | エディタ用に`setObjectsStatsSystemEnabledState`を呼ぶだけ。 |
