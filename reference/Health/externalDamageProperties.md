# externalDamageProperties

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/externalDamageProperties.cs:5`

**概要**: ダメージの発生源を保持する小さなコンポーネント。`currentDamageOwner`を差し替え、変更時にイベントで通知する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Set Damage Owner | `eventToSetDamageOwner` | `eventParameters.eventToCallWithGameObject` | – | – |
| Current Damage Owner | `currentDamageOwner` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setDamageOwner(GameObject newOwner)` | `currentDamageOwner`を`newOwner`に差し替え、`eventToSetDamageOwner`を発火する。 |
