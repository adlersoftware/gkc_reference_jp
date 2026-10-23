# languageLocalizationManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **namespace**: `GKC.Localization`
- **ソース**: `Localization System/languageLocalizationManager.cs:10`

**概要**: 各ローカライズ管理コンポーネントの基底クラスで、ファイルパスの解決や言語ファイルの存在確認、言語変更イベントを提供する。編集・辞書取得系は継承先で実装する仮想メソッド。

## インスペクター設定

### Language Tool Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Language To Edit | `currentLanguageToEdit` | `string` | "English" | – |
| File Path | `filePath` | `string` | "Assets/Game Kit Controller/Scripts/E… | – |
| File Path Build | `filePathBuild` | `string` | "./Localization/" | – |
| File Format | `fileFormat` | `string` | ".csv" | – |
| File Name | `fileName` | `string` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Local File Path | `useLocalFilePath` | `bool` | – | – |
| Use Resources Path | `useResourcesPath` | `bool` | – | – |
| Localization Enabled | `localizationEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Language Change | `useEventsOnLanguageChange` | `bool` | – | – |
| Event On Language Change | `eventOnLanguageChange` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateFileName()` | 継承先で実装する仮想メソッドで、本体が空で何もしない。 |
| `updateLocalizationFileExternally()` | 継承先で実装する仮想メソッドで、本体が空で何もしない。 |
| `checkEventsOnLanguageChange()` | `useEventsOnLanguageChange`が有効なら`eventOnLanguageChange`を発火する。 |
| `getDictionaryForEditor()` | エディタ用辞書を返す仮想メソッドで、常にnullを返すだけ。 |
| `updateLocalizationFileFromEditor()` | 継承先で実装する仮想メソッドで、本体が空で何もしない。 |
| `GetLocalizedValueFromEditor(string key)` | エディタ用の値を返す仮想メソッドで、常に空文字を返すだけ。 |
| `addKey(string key, string value)` | 継承先で実装する仮想メソッドで、本体が空で何もしない。 |
| `removeKey(string key)` | 継承先で実装する仮想メソッドで、本体が空で何もしない。 |
| `addLanguage(string languageName)` | 継承先で実装する仮想メソッドで、本体が空で何もしない。 |
| `addLanguageListToNewLocalizationFile()` | 継承先で実装する仮想メソッドで、本体が空で何もしない。 |
| `getCurrentFilePath()` | エディタ上でローカルパス未使用なら`filePath`、それ以外は`filePathBuild`を返す。 |
| `isUseResourcesPathActive()` | `useResourcesPath`が有効か、タッチ端末ならtrueを返す。 |
| `checkIfLanguageFileExists()` | 言語ファイルのパスを解決し、存在しなければ空ファイルを作成してパスをログ出力する。 |
| `updateComponent()` | コンポーネント更新とシーンのダーティ更新を行うだけ。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static bool languageFileExists(string newFilePath, bool useResourcesPathValue, string fileNameValue)` | – |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnLanguageChange` | `UnityEvent` | – |
