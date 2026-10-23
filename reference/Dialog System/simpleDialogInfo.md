# simpleDialogInfo

- **種別**: class
- **ソース**: `Dialog System/completeDialogInfo.cs:204`
- **属性**: `System.Serializable`

**概要**: ローカライズ用テンプレートで使う簡易版のダイアログ情報クラス。本文・所有者名・音声・回答リストのみを保持する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Name | `Name` | `string` | – | – |
| ID | `ID` | `int` | – | – |
| Dialog Owner Name | `dialogOwnerName` | `string` | – | – |
| Dialog Content | `dialogContent` | `string` | – | TextArea (3, 10) |
| Dialog Line Sound | `dialogLineSound` | `AudioClip` | – | – |
| Dialog Line Audio Element | `dialogLineAudioElement` | `AudioElement` | – | – |
| Dialog Line Info List | `dialogLineInfoList` | `List<simpleDialogLineInfo>` | new List<simpleDialogLineInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `InitializeAudioElements()` | `dialogLineSound` を `dialogLineAudioElement.clip` に代入するだけ。 |
