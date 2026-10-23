# sceneLoadSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Menu/sceneLoadSystem.cs:7`

**概要**: シーン選択メニューのスロット生成と読み込みを担当。リストのシーン番号を連番で振り直すユーティリティも持つ。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Instantiate Scene Panels Activated | `instantiateScenePanelsActivated` | `bool` | true | オンにすると開始時にシーン一覧の枠を自動生成する。 |
| Main Menu Content | `mainMenuContent` | `GameObject` | – | シーン読込時に非表示にするメインメニューの親。 |
| Scene Load Menu | `sceneLoadMenu` | `GameObject` | – | スクロール位置調整のため一時的に開くシーン選択メニュー。 |
| Scene Slot Prefab | `sceneSlotPrefab` | `GameObject` | – | シーンごとに生成する枠のプレハブ。 |
| Scene Slots Parent | `sceneSlotsParent` | `Transform` | – | 生成したシーン枠を並べる親トランスフォーム。 |
| Main Scrollbar | `mainScrollbar` | `Scrollbar` | – | 一覧のスクロールバーで、表示時に値をリセットする。 |
| Main Scroll Rect | `mainScrollRect` | `ScrollRect` | – | 一覧のスクロール領域で、表示位置を初期化する。 |
| Starting Scene Index | `startingSceneIndex` | `int` | 1 | シーン番号を振るときの開始インデックス。 |
| Add Scene Number To Name | `addSceneNumberToName` | `bool` | true | オンにすると枠名の前に番号を付けて表示する。 |

### Load Screen Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Load Screen | `useLoadScreen` | `bool` | – | オンにするとロード画面シーンを経由して読み込む。 |
| Load Screen Scene | `loadScreenScene` | `int` | 1 | 経由するロード画面シーンのビルドインデックス。 |
| Use Last Scene Index As Load Screen | `useLastSceneIndexAsLoadScreen` | `bool` | true | オンにするとビルド設定の最後のシーンをロード画面にする。 |
| Scene To Load Async Prefs Name | `sceneToLoadAsyncPrefsName` | `string` | "SceneToLoadAsync" | 次に読むシーン番号を保存する`PlayerPrefs`のキー名。 |
| Check Loading Screen Scene Configured | `checkLoadingScreenSceneConfigured` | `bool` | true | オンにするとロード画面のシーン名が想定どおりか確認する。 |
| Loading Screen Scene Name | `loadingScreenSceneName` | `string` | "Loading Screen Scene" | ロード画面として期待するシーンの名前。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `sceneInfoList` | `List<sceneInfo>` | new List<sceneInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `loadScene(Button buttonToCheck)` | メインメニューを隠し、一致するボタンのシーン番号でロード画面付きの読み込みを行う。 |
| `setSceneNumberInOrder()` | 各要素の`sceneNumber`に開始番号からの連番を振り、コンポーネントを更新する。 |
| `setSceneNumberInOrderByIndex(int index)` | `index`以降の要素だけに開始番号からの連番を振り直して更新する。 |
| `enableAddSceneToListByIndex(int index)` | `index`以降の要素の`addSceneToList`をtrueにして更新する。 |
| `disableAddSceneToListByIndex(int index)` | `index`以降の要素の`addSceneToList`をfalseにして更新する。 |
| `updateComponent()` | `GKC_Utils`でコンポーネントとシーンのダーティ更新を行う。 |

## 内部型

- `sceneInfo`（class）
- `sceneSlotInfo`（class）
