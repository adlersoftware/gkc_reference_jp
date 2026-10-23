# laserReceiver

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/laserReceiver.cs:4`

**概要**: 色付きレーザーを受けて接続先オブジェクトの関数を呼ぶレシーバー。接続中は内部の円柱が回転し続ける。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Color Needed | `colorNeeded` | `Color` | – | – |
| Connected | `connected` | `bool` | – | – |
| Object To Connect | `objectToConnect` | `GameObject` | – | – |
| Active Function Name | `activeFunctionName` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `laserConnected(Color col)` | `col`が`colorNeeded`と一致する場合のみ接続し、接続先へ`activeFunctionName`を`true`で送る。 |
| `laserDisconnected()` | 接続状態を解除し、`objectToConnect`へ`activeFunctionName`を`false`で送る。 |
