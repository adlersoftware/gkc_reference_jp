# gameLanguageSelector

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Localization System/gameLanguageSelector.cs:8`

**概要**: ゲーム全体の現在言語を管理するシングルトンで、言語変更時に各ローカライズ管理とシーン内の要素表示をまとめて更新する。PlayerPrefsへの保存や起動時のシステム言語チェックも担う。

**公式ドキュメント抜粋**（[Game Language Selector](../../docs/player-controller-components/elements-used-by-other-components/game-language-selector.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Language Selection Enabled | `languageSelectionEnabled` | `bool` | true | – |
| Language Name List | `languageNameList` | `List<string>` | new List<string> () | – |

### Language Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Language | `currentLanguage` | `string` | "English" | – |
| Update Elements On Language Change | `updateElementsOnLanguageChange` | `bool` | true | – |
| Check Language Active | `checkLanguageActive` | `bool` | true | – |
| Check Update Current Language By Player Prefs On Start | `checkUpdateCurrentLanguageByPlayerPrefsOnStart` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Language Updated By Settings | `languageUpdatedBySettings` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check System Language On Start | `checkSystemLanguageOnStart` | `bool` | – | – |
| Event On Language Check At Start | `eventOnLanguageCheckAtStart` | `eventParameters.eventToCallWithString` | – | – |
| Update UI Drop Down On Language On Start | `updateUIDropDownOnLanguageOnStart` | `bool` | – | – |
| Language Drop Down | `languageDropDown` | `Dropdown` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateCurrentLanguageByPlayerPrefs()` | `Current Language`キーが保存されていればその値を読み、`setGameLanguage`で適用する。 |
| `setCurrentLanguagePlayerPrefsValue()` | `currentLanguage`が空でなければ`Current Language`キーへ保存するだけ。 |
| `getComponentInstance()` | 自身を静的インスタンスに登録し、既に別インスタンスがあればこのオブジェクトを破棄する。 |
| `setGameLanguageByIndex(int languageIndex)` | `languageIndex`番目の言語名を取り出して`setGameLanguage`を呼ぶだけ。 |
| `setGameLanguage(string languageSelected)` | 有効時のみ`GKC_Utils`の言語を変更し、全ローカライズと要素を更新してPlayerPrefsへ保存する。 |
| `updateAllLanguageElementCheckerOnScene()` | 言語変更時の更新が有効なら、シーン内の全`languageElementChecker`へ現在言語を適用する。 |
| `addLanguage(string newName)` | 一覧に未登録なら`newName`を言語リストへ追加するだけ。 |
| `removeLanguage(string newName)` | 一覧に存在すれば`newName`を言語リストから削除するだけ。 |
| `setNewLanguageList(List<string> newNameList)` | 言語リストをクリアし、`newNameList`の内容で置き換えるだけ。 |
| `updateLanguageDropDown()` | ドロップダウン各項目の表示を`UIElementsLocalizationManager`の翻訳値へ差し替えて再描画する。 |
| `assignNewLanguageDropDown(Dropdown newDropDown)` | `languageDropDown`の参照を差し替えるだけ。 |
| `checkIfLanguageDropDownAssignedAndUpdate(Dropdown newDropDown)` | 未割り当てなら`newDropDown`を設定し、その後ドロップダウン表示を更新する。 |
| `getCurrentLanguageList()` | 言語名リストの参照を返すだけ。 |
| `setCurrentLanguage(string newLanguage)` | `currentLanguage`を設定するだけ。 |
| `getCurrentLanguage()` | `currentLanguage`を返すだけ。 |
| `setCurrentLanguageFromEditor(string newLanguage)` | `currentLanguage`を設定したうえで`updateComponent`を呼ぶ。 |
| `updateComponent()` | コンポーネント更新とシーンのダーティ更新を行うだけ。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |
| `static bool isCheckLanguageActive()` | – |
