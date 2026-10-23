# editControlPosition

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Input/editControlPosition.cs:12`
- **属性**: `System.Serializable`

**概要**: タッチボタンをドラッグで移動させ、その位置をファイルへ保存・読み込みする編集コンポーネント。編集モードの開始・取消と既定位置への復帰を提供する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Load Buttons Position Enabled | `loadButtonsPositionEnabled` | `bool` | false | – |
| Initialize Touch Buttons Position Enabled | `initializeTouchButtonsPositionEnabled` | `bool` | false | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Buttons | `buttons` | `List<RectTransform>` | new List<RectTransform> () | – |
| Main Game Manager Located | `mainGameManagerLocated` | `bool` | – | – |

### Button Info Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Buttons Pos | `buttonsPos` | `List<Vector2>` | new List<Vector2> () | – |
| Button Pos Default | `buttonPosDefault` | `List<Vector2>` | new List<Vector2> () | – |
| Touch Button List | `touchButtonList` | `List<touchButtonListener>` | new List<touchButtonListener> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Input | `input` | `inputManager` | – | – |
| Main Game Manager | `mainGameManager` | `gameManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の`mainUpdateCoroutine` があれば停止するだけ。 |
| `checkSettings()` | `gameManager` を探し、未初期化なら相対パス設定と保存先パスを一度だけ取得する。 |
| `getDataPath()` | 相対パスか`persistentDataPath` かでフォルダを決め、無ければ作成し末尾に`/` を付けたパスを返す。 |
| `getTouchButtons()` | `gameManager` のロード設定が有効なら、位置の`Load` と現在位置の退避を初期化フラグに応じて行う。 |
| `getTouchButtonsComponents()` | `input` を取得し、タッチボタンの`RectTransform`、既定位置、`touchButtonListener` をリストに集め直す。 |
| `activateEdit()` | 編集モードを反転し、開始時はボタン入力を止めて更新コルーチンを開始、終了時は位置を集めて`Save` する。 |
| `disableEdit()` | 編集中なら編集モードをfalseにし、各ボタンを退避しておいた位置へ戻す。 |
| `changeToDefault()` | 全ボタンを既定位置`buttonPosDefault` に戻してから`Save` する。 |
| `changeButtonsState(bool state)` | 各`touchButtonListener` の`enabled` を`state`にし、編集中の誤タップを防ぐ。 |
| `Save()` | 各ボタン位置を`BinaryFormatter` でテキストファイルへ書き出し、書き出した値で`buttonsPos` を作り直す。 |
| `Load()` | 保存ファイルがあればX/Yのリストを読み出し、件数がボタン数と一致する場合のみ位置を復元する。 |
