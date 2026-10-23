# simpleGameLanguageSelector

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Localization System/simpleGameLanguageSelector.cs:7`

**概要**: メインの`gameLanguageSelector`を探して言語設定を委譲する簡易セレクタで、変更時にドロップダウン更新と独自イベントを行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Game Language Selector | `mainGameLanguageSelector` | `gameLanguageSelector` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Game Language Selector Located | `gameLanguageSelectorLocated` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Language Change | `useEventOnLanguageChange` | `bool` | – | – |
| Event On Language Change | `eventOnLanguageChange` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Language Drop Down | `languageDropDown` | `Dropdown` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setGameLanguageByIndex(int languageIndex)` | メインの`gameLanguageSelector`へインデックスで言語を設定し、ドロップダウン更新とイベントを行う。 |
| `setGameLanguage(string languageSelected)` | 同じくメインの選択コンポーネントへ言語名を渡し、ドロップダウン更新とイベント発火を行う。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnLanguageChange` | `UnityEvent` | – |
