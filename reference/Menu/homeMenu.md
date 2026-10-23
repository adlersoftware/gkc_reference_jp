# homeMenu

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Menu/homeMenu.cs:6`

**概要**: ホームメニュー用の簡易メニュー管理。サブメニューの開閉とシーン読み込み、ゲーム終了処理を提供する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Initial UI Element Selected | `useInitialUIElementSelected` | `bool` | – | – |
| Initial UI Element Selected | `initialUIElementSelected` | `GameObject` | – | – |
| Main Menu Name | `mainMenuName` | `string` | "Main Menu" | – |

### Load Screen Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Load Screen | `useLoadScreen` | `bool` | – | – |
| Load Screen Scene | `loadScreenScene` | `int` | 1 | – |
| Use Last Scene Index As Load Screen | `useLastSceneIndexAsLoadScreen` | `bool` | true | – |
| Scene To Load Async Prefs Name | `sceneToLoadAsyncPrefsName` | `string` | "SceneToLoadAsync" | – |
| Check Loading Screen Scene Configured | `checkLoadingScreenSceneConfigured` | `bool` | true | – |
| Loading Screen Scene Name | `loadingScreenSceneName` | `string` | "Loading Screen Scene" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sub Menu Active | `subMenuActive` | `bool` | – | – |

### Menu Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Submenu Info List | `submenuInfoList` | `List<menuPause.submenuInfo>` | new List<menuPause.submenuInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `confirmExit()` | `Application.Quit`でゲームを終了するだけ。 |
| `loadScene(int sceneNumber)` | `GKC_Utils.loadScene`にロード画面設定を渡して`sceneNumber`のシーンを読み込む。 |
| `disableMenuList()` | 全サブメニューを非表示にし、開いていたものは`menuOpened`を下ろして`eventOnClose`を発火する。 |
| `openOrClosePauseMenuByName(string menuName, bool state)` | 指定名のメニューを開閉し、他メニューを閉じて開閉イベントとサブメニュー状態を更新する。 |
| `openPauseMenuByName(string menuName)` | `openOrClosePauseMenuByName`で指定メニューを開くだけ。 |
| `closePauseMenuByName(string menuName)` | `openOrClosePauseMenuByName`で指定メニューを閉じるだけ。 |
| `enterSubMenu()` | `subMenuActive`をtrueにするだけ。 |
| `exitSubMenu()` | `subMenuActive`をfalseにするだけ。 |
