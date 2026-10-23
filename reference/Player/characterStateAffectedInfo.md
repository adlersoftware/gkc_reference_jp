# characterStateAffectedInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/States/characterStateAffectedInfo.cs:5`

**概要**: キャラクターに付与する状態効果の基底クラス。実際の効果は派生クラスが仮想メソッドを上書きして実装する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| State Enabled | `stateEnabled` | `bool` | true | – |
| State Affected Name | `stateAffectedName` | `string` | – | – |
| State Affected Active | `stateAffectedActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateStateAffected(float stateDuration, float stateAmount)` | 中身が空の仮想メソッドで、派生クラスが時間と量を受け取って効果を実装する。 |
| `activateStateAffected(bool state)` | 中身が空の仮想メソッドで、派生クラスが有効/無効を実装する。 |
| `isStateAffectedActive()` | `stateAffectedActive` の値を返すだけ。 |
