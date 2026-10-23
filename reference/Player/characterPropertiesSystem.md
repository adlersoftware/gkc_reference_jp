# characterPropertiesSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/States/characterPropertiesSystem.cs:5`

**概要**: キャラクターに付与された状態（炎上・毒など）の有効化をまとめるコンポーネント。名前が一致する `characterStateAffectedInfo` へ処理を委譲する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Characeter States Affected Enabled | `characeterStatesAffectedEnabled` | `bool` | true | – |

### States List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character State Affected Info List | `characterStateAffectedInfoList` | `List<characterStateAffectedInfo>` | new List<characterStateAffectedInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateStateAffected(string stateName, float stateDuration, float stateAmount)` | 名前一致かつ有効な項目へ、時間と量を渡して状態を有効化する。 |
| `activateStateAffected(string stateName)` | `activateOrDeactivateStateAffected(stateName, true)` を呼ぶだけ。 |
| `deactivateStateAffected(string stateName)` | `activateOrDeactivateStateAffected(stateName, false)` を呼ぶだけ。 |
| `activateOrDeactivateStateAffected(string stateName, bool state)` | 全体有効時、名前一致かつ有効な項目へ bool 版の `activateStateAffected` を渡す。 |
| `getCharacterStateAffectedInfoByName(string stateName)` | 名前が一致する `characterStateAffectedInfo` を返し、無ければ null を返す。 |
| `getCharacterStateAffectedInfoGameObjectByName(string stateName)` | 名前一致の状態情報の `gameObject` を返し、無ければ null を返す。 |
