# simpleActionButton

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/simpleActionButton.cs:4`

**概要**: ボタンから指定オブジェクトへ名前でメソッドを送るだけのコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Function Name | `functionName` | `string` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Active | `objectToActive` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateDevice()` | `objectToActive`へ`functionName`のメソッドを`SendMessage`で送る（受信先が無くてもエラーにしない）。 |
