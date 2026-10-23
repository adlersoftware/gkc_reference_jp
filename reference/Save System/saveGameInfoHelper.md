# saveGameInfoHelper

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Save System/saveGameInfoHelper.cs:6`

**概要**: セーブの有無を調べてイベントを発火し、`PlayerPrefs`の`saveNumber`を管理する補助コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Save State On Start Enabled | `checkSaveStateOnStartEnabled` | `bool` | true | – |

### Components Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Save Game System | `mainSaveGameSystem` | `saveGameSystem` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Home Menu Opened | `eventOnHomeMenuOpened` | `UnityEvent` | – | – |
| Event On Game Saves Located | `eventOnGameSavesLocated` | `UnityEvent` | – | – |
| Event On Game Saves Not Located | `eventOnGameSavesNotLocated` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkIfGameCanContinue()` | ホームメニューイベントを発火し、`startGameSystem`後にセーブの有無で保存済み/未保存のイベントを呼び分ける。 |
| `storeSaveNumberOnPlayerPrefs(int newValue)` | `PlayerPrefs`の`saveNumber`に値を書き、内部変数と`Delete Player Prefs Active`も更新する。 |
| `removeSaveNumberOnPlayerPrefs()` | 保持中の番号が`PlayerPrefs`の値と一致するときだけ`saveNumber`と`Delete Player Prefs Active`を削除する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnHomeMenuOpened` | `UnityEvent` | – |
| `eventOnGameSavesLocated` | `UnityEvent` | – |
| `eventOnGameSavesNotLocated` | `UnityEvent` | – |
