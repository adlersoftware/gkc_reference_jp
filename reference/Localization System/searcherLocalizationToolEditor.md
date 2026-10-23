# searcherLocalizationToolEditor

- **種別**: class
- **継承 / 実装**: `EditorWindow`
- **namespace**: `GKC.Localization`
- **ソース**: `Localization System/localizationToolEditor.cs:10`

**概要**: ローカライズのキーを検索し、削除や新規追加を行えるエディタウィンドウ。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Value | `value` | `string` | – | – |
| Scroll | `scroll` | `Vector2` | – | – |
| Dictionary | `dictionary` | `Dictionary<string, string>` | – | – |
| Current Language Localization Manager | `currentLanguageLocalizationManager` | `languageLocalizationManager` | – | – |
| Dictionary Assigned | `dictionaryAssigned` | `bool` | false | – |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static void Open(languageLocalizationManager newLanguageLocalizationManager)` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnGUI()`

</details>
