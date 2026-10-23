# customActionOpenMenuSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Menu/customActionOpenMenuSystem.cs:5`

**概要**: 外部からメニュー開閉処理を差し込むための基底クラス。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Custom Action Enabled | `customActionEnabled` | `bool` | true | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `openOrCloseMenu(bool state, GameObject currentPlayer)` | 本体が空の仮想メソッドで、派生クラス側で開閉処理を実装する。 |
