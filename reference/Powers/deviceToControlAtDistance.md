# deviceToControlAtDistance

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/New Powers Behaviors/deviceToControlAtDistance.cs:5`

**概要**: 遠隔操作パワー用に、実際に操作するデバイスを指定する小さなコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Device To Control Enabled | `deviceToControlEnabled` | `bool` | true | – |
| Device To Control Game Object | `deviceToControlGameObject` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `isDeviceToControlEnabled()` | 遠隔操作対象の有効フラグを返すだけ。 |
| `getDeviceToControlGameObject()` | 操作対象を返し、未設定なら自身を設定して返す。 |
