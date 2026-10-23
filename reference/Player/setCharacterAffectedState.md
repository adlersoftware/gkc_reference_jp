# setCharacterAffectedState

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/States/setCharacterAffectedState.cs:5`

**概要**: 衝突したプレイヤーへ状態効果を付与する小さなコンポーネント。対象の `characterPropertiesSystem` に名前・時間・量を渡す。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Affect State Enabled | `affectStateEnabled` | `bool` | true | – |
| Character State Affected Name | `characterStateAffectedName` | `string` | – | – |
| State Duration | `stateDuration` | `float` | – | – |
| State Amount | `stateAmount` | `float` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkObjectDetected(GameObject objectToDamage)` | 対象から `characterPropertiesSystem` を取得し、名前・時間・量で状態を有効化する。 |
