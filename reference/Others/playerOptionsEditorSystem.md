# playerOptionsEditorSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/playerOptionsEditorSystem.cs:7`

**概要**: オプション画面の各UI（スクロールバー/スライダー/トグル/ドロップダウン）と設定イベントを対応付けて管理するコンポーネントで、既定値への復元も行う。

**公式ドキュメント抜粋**（[Player Options Editor System](../../docs/character-level-components/character/player-options-editor-system.md)）

> Used to configure the different in-game settings, related to stuff like graphic settings, mouse sensitivity, movement, and camera rotation and orientation values, show tutorials in-game or disable them, game volume, etc.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Options Editor Enabled | `playerOptionsEditorEnabled` | `bool` | true | 有効にすると起動時に各オプション値の初期化を実行する。 |
| Initialize Options Only When Loading Game | `initializeOptionsOnlyWhenLoadingGame` | `bool` | – | オンにするとセーブ読込時のみ初期値を適用する。 |
| Save Current Player Options To Save File | `saveCurrentPlayerOptionsToSaveFile` | `bool` | true | 現在のオプション値をセーブデータに保存するかどうか。 |

### Debug State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Values Initialized | `valuesInitialized` | `bool` | – | 初期化処理が完了したかを示す実行時状態フラグ。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `optionInfoList` | `List<optionInfo>` | new List<optionInfo> () | – |
| `isLoadingGame` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setIsLoadingGameState(bool state)` | `isLoadingGame` を設定するだけ。 |
| `isLoadingGameState()` | `isLoadingGame` を返すだけ。 |
| `setOptionByScrollBar(Scrollbar scrollBarToSearch)` | 一致するスクロールバーの値を0/1に補正し、設定に応じて真偽を反転してイベントを発火する。 |
| `setOptionBySlider(Slider sliderToSearch)` | 一致するスライダーの値を保持してイベントを発火し、必要なら数値テキストも更新する。 |
| `setOptionByToggle(Toggle toggleToSearch)` | 一致するトグルの状態を反転設定に従ってイベント発火し、値を保持する。 |
| `setOptionByDropDown(Dropdown dropDownToSearch)` | 一致するドロップダウンの選択テキストを通知し、必要なら選択インデックスのイベントも発火する。 |
| `setDefaultValues()` | 有効な全オプションを既定値に戻し、それぞれの設定反映処理を呼び出す。 |
| `enableOptionByName(string optionName)` | `enableOrDisableOptionByName` を true で呼ぶだけ。 |
| `disableOptionByName(string optionName)` | `enableOrDisableOptionByName` を false で呼ぶだけ。 |
| `enableOrDisableOptionByName(string optionName, bool state)` | 名前一致のオプションの `optionEnabled` を設定し、コンポーネントを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent` と `updateDirtyScene` で表示とシーンを更新する。 |

## 内部型

- `optionInfo`（class）
