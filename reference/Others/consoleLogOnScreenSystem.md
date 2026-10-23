# consoleLogOnScreenSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/consoleLogOnScreenSystem.cs:6`

**概要**: アプリケーションログを`Text`へ蓄積表示し、長すぎる場合は切り詰める。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Console Log Text | `consoleLogText` | `Text` | – | – |
| Max Text Length | `maxTextLength` | `int` | 3000 | – |
| Text Lenght To Remove On Max Amount | `textLenghtToRemoveOnMaxAmount` | `int` | 2500 | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `Log(string logString, string stackTrace, LogType type)` | `logString`を先頭に追記し、`maxTextLength`を超えたら先頭から`textLenghtToRemoveOnMaxAmount`文字だけ残す。 |
