# skillsLocalizationManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `languageLocalizationManager`
- **namespace**: `GKC.Localization`
- **ソース**: `Localization System/skillsLocalizationManager.cs:8`

**概要**: スキル用のローカライズを読み込み、キーから翻訳値を返す静的マネージャー。

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkFilePathValues()` | スキル用ローカライズのファイル名・形式・有効可否・Resourcesパス可否・現在パスを静的フィールドへ複製する。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static void updateLocalizationFile()` | – |
| `static void updateDictionary(string currentLanguage)` | – |
| `static string GetLocalizedValue(string key)` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`GetLocalizedValueFromEditor(string key)`, `addKey(string key, string value)`, `addLanguage(string languageName)`, `addLanguageListToNewLocalizationFile()`, `getDictionaryForEditor()`, `removeKey(string key)`, `updateFileName()`, `updateLocalizationFileExternally()`, `updateLocalizationFileFromEditor()`

</details>
