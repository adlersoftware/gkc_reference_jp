# languageCheckerUIElement

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `languageElementChecker`
- **namespace**: `GKC.Localization`
- **ソース**: `Localization System/languageCheckerUIElement.cs:8`

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Text | `mainText` | `Text` | – | – |
| Use Drop Down | `useDropDown` | `bool` | – | – |
| Main Drop Down | `mainDropDown` | `Dropdown` | – | – |
| Use UI Elements Localization Manager | `useUIElementsLocalizationManager` | `bool` | true | – |
| Use Interaction Objects Localization Manager | `useInteractionObjectsLocalizationManager` | `bool` | – | – |

### Text Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Language Localization Manager | `useLanguageLocalizationManager` | `bool` | true | – |
| Localization Key | `localizationKey` | `string` | – | – |
| Check Empty Key | `checkEmptyKey` | `bool` | true | – |
| Set Full Text With Caps Enabled | `setFullTextWithCapsEnabled` | `bool` | – | – |
| Drop Down Localization Key | `dropDownLocalizationKey` | `List<string>` | new List<string> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`updateLanguageOnElement(string currentLanguage)`

</details>
