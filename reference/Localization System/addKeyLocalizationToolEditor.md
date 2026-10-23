# addKeyLocalizationToolEditor

- **種別**: class
- **継承 / 実装**: `EditorWindow`
- **namespace**: `GKC.Localization`
- **ソース**: `Localization System/localizationToolEditor.cs:119`

**概要**: 指定言語へ新しいキーと値を追加するエディタウィンドウ。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Key | `key` | `string` | – | – |
| Value | `value` | `string` | – | – |
| Current Language Localization Manager | `currentLanguageLocalizationManager` | `languageLocalizationManager` | – | – |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static void Open(languageLocalizationManager newLanguageLocalizationManager, string mainKey = "", string mainValue = "")` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnGUI()`

</details>
