# localizationFileLoader

- **種別**: class
- **namespace**: `GKC.Localization`
- **ソース**: `Localization System/localizationFileLoader.cs:12`

**概要**: CSV形式のローカライズファイルを読み書きするローダーで、言語列を辞書化し、キーや言語の追加削除をエディタ上で行う。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main File | `mainFile` | `StreamReader` | – | – |
| Main File Text | `mainFileText` | `StringBuilder` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `loadFile(string filePath, bool useResourcesPath)` | `useResourcesPath`なら`Resources`、それ以外はファイルからCSVを読んで`mainFileText`へ格納する。 |
| `GetDictionaryValues(string attributeID)` | 先頭行から`attributeID`を含む列を探し、キーとその列の値の辞書を返す。列が無ければnull。 |
| `addKey(string filePath, string key, string value, string languageName)` | エディタ専用で、対象言語の列に`key`が既にあれば値を差し替え、無ければ空欄付きで行を追加して保存する。 |
| `removeKey(string fileName, string filePath, string key, bool useResourcesPath)` | エディタ専用で、キーを含む行を削除してファイルを保存し、アセットを再読込する。 |
| `addLanguage(string filePath, string languageName)` | エディタ専用で、ヘッダに無ければ空欄を伴う言語列を追加し、`GKC_Utils.addLanguage`も呼ぶ。 |
| `addLanguageListToNewLocalizationFile(string filePath)` | エディタ専用で、ファイル内容が空なら`key`と全言語名からなるヘッダ行を書き込む。 |
