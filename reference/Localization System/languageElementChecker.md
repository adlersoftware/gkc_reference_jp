# languageElementChecker

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Localization System/languageElementChecker.cs:5`

**概要**: UI要素などに言語ごとのテキストを持たせ、言語変更時に表示を切り替えるための基底コンポーネント。

## インスペクター設定

### Language Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| UI Element Language Info List | `UIElementLanguageInfoList` | `List<UIElementLanguageInfo>` | new List<UIElementLanguageInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateLanguageOnElement()` | `GKC_Utils.getCurrentLanguage`で現在言語を取得し、引数付きの版へ渡すだけ。 |
| `updateLanguageOnElement(string currentLanguage)` | 継承先で実装する仮想メソッドで、本体が空で何もしない。 |

## 内部型

- `UIElementLanguageInfo`（class）
