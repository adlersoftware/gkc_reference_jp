# consoleMode

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/Console Mode/consoleMode.cs:8`

**概要**: ゲーム内デバッグコンソールで、キー入力からコマンド文字列を組み立て、登録済みコマンドの検証・実行、補完、履歴、オブジェクトのスポーンを行う。

**公式ドキュメント抜粋**（[Console Mode](../../docs/character-level-components/character/console-mode.md)）

> 

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Console Mode Enabled | `consoleModeEnabled` | `bool` | true | オンにすると入力からコンソールを開閉できる。 |
| Incorrect Command Message | `incorrectCommandMessage` | `string` | – | 存在しないコマンドを入力したときに表示するテキスト。 |
| Line Spacing Amount | `lineSpacingAmount` | `float` | – | 履歴1行あたりの縦間隔。行数に応じて表示位置をずらす。 |
| Console Opened | `consoleOpened` | `bool` | – | コンソールを開いているかどうかの状態。実行時に切り替わる。 |
| Max Radius To Instantiate | `maxRadiusToInstantiate` | `float` | – | `spawn`で生成するオブジェクトを散らすランダム半径。 |
| Deleting Text Rate | `deletingTextRate` | `float` | 0.3f | 削除キーを押し続けたとき、1文字消す間隔（秒）。 |
| Start Deleting Time Amount | `startDeletingTimeAmount` | `float` | 0.5f | 削除キーを押してから連続削除が始まるまでの遅延（秒）。 |

### Element Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Console Window | `consoleWindow` | `GameObject` | – | コンソールUIのルート。開閉時にアクティブを切り替える。 |
| Command Text Parent | `commandTextParent` | `Transform` | – | 実行コマンドの履歴テキストを並べる親Transform。 |
| Command Text Parent Rect Transform | `commandTextParentRectTransform` | `RectTransform` | – | 履歴の親RectTransform。行数に応じて位置をスクロールする。 |
| Current Console Command Text | `currentConsoleCommandText` | `Text` | – | 入力中のコマンド表示と、履歴行の複製元になるText。 |
| Input | `input` | `inputManager` | – | キー入力を取得するinputManager。未設定なら自動で検索する。 |
| Player Input | `playerInput` | `playerInputManager` | – | コンソール表示中にプレイヤー入力を止めるplayerInputManager。 |
| Pause Manager | `pauseManager` | `menuPause` | – | コンソール開閉時にカーソルやポーズを制御するmenuPause。 |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | 開いている間だけ停止させるプレイヤーのplayerController。 |
| Main Game Manager | `mainGameManager` | `gameManager` | – | コンソール開閉時にゲームのポーズを切り替えるgameManager。 |
| Spawn Position | `spawnPosition` | `Transform` | – | `spawn`で生成するオブジェクトの位置と向きの基準。 |
| Command List Scroll Rect | `commandListScrollRect` | `ScrollRect` | – | コンソール履歴をスクロールするScrollRect。 |

### Key Names Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tab Key Name | `tabKeyName` | `string` | "tab" | 入力中のコマンドを補完するTabキーの識別名。 |
| Delete Key Name | `deleteKeyName` | `string` | "delete" | 1文字削除に使うDeleteキーの識別名。 |
| Space Key Name | `spaceKeyName` | `string` | "space" | コマンドに空白を挿入するSpaceキーの識別名。 |
| Back Space Key Name | `backSpaceKeyName` | `string` | "backspace" | 1文字削除に使うBackspaceキーの識別名。 |
| Return Key Name | `returnKeyName` | `string` | "return" | コマンドを実行するReturnキーの識別名。 |
| Enter Key Name | `enterKeyName` | `string` | "enter" | コマンドを実行するEnterキーの識別名。 |
| Left Shift Key Name | `leftShiftKeyName` | `string` | "leftshift" | 大文字と小文字を切り替える左Shiftキーの識別名。 |
| Down Arrow Key Name | `downArrowKeyName` | `string` | "downarrow" | 入力履歴を新しい方向へたどる下矢印キーの識別名。 |
| Up Arrow Key Name | `upArrowKeyName` | `string` | "uparrow" | 入力履歴を古い方向へたどる上矢印キーの識別名。 |
| Alpha Key Name | `alphaKeyName` | `string` | "alpha" | 英字キーを表す接頭辞。押された文字の判定に使う。 |
| Capslock Key Name | `capslockKeyName` | `string` | "capslock" | 大文字と小文字を切り替えるCapsLockキーの識別名。 |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | コマンド解析や補完の過程をログ出力するデバッグ用。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `commandInfoList` | `List<commandInfo>` | new List<commandInfo> () | – |
| `allowedKeysList` | `List<string>` | new List<string> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateConsoleCoroutine()` | `consoleCoroutine` が存在すれば停止するだけ。 |
| `checkKeyPressed(string keyPressed)` | 押されたキーを解釈し、履歴移動・Tab補完・文字削除・Enter 実行などの入力処理を行う。 |
| `resetAutocompleteParameters()` | オートコンプリート状態・候補インデックス・検索文字列を初期化するだけ。 |
| `checkCurrentCommand(string currentCommand)` | 入力コマンドを履歴に追加して照合し、数値/真偽/名前パラメータを検証して対応イベントを実行し成否を返す。 |
| `createNewCommandText(string commandContent)` | 空文字なら何もせず、コマンド表示用テキストを複製・追加して行数とスクロール位置を更新する。 |
| `setScrollRectPosition(Vector3 position)` | 既存のスクロールコルーチンを停止し、指定位置へ移動するコルーチンを開始する。 |
| `showCommandList()` | 登録済みコマンドを名前と説明の組で一覧表示する。 |
| `clearCommandList()` | 生成したコマンドテキストを破棄し、行数・履歴・スクロール位置をリセットする。 |
| `openOrCloseConsoleMode(bool state)` | 同じ状態なら何もせず、コンソール表示とポーズ・カーソル・入力などの関連状態をまとめて切り替える。 |
| `stopDeletingText()` | 連続削除の状態フラグを2つとも false にするだけ。 |
| `checkPrefabsManager()` | 未取得なら `GKC_Utils.addPrefabsManagerToScene` でプレハブマネージャを取得し、有無を記録する。 |
| `spawnObject()` | 直前のコマンド文字列から名前と個数を解析し、プレハブをスポーン位置周辺に生成して結果を表示する。 |
| `showSpawnObjectsList()` | プレハブマネージャに登録された全オブジェクト名を一覧表示する。 |
| `spawnGameObject(GameObject objectToSpawn, Vector3 position, Quaternion rotation)` | 指定オブジェクトを指定位置・回転で生成し、位置を再設定する。 |
| `killAllEnemies()` | `killCharacters(false)` を呼び、Player/friend 以外と判定された生存キャラクターを倒す。 |
| `killAllCharacters()` | `killCharacters(true)` を呼び、生存している全キャラクターを倒す。 |
| `destroyAllVehicles()` | シーン内の全 `vehicleHUDManager` に対して `destroyVehicle` を呼ぶ。 |
| `inputActivateConsoleMode()` | コンソール有効かつ他メニューが開いていなければ、コンソールの開閉を切り替える。 |
| `setConsoleModeEnabledState(bool state)` | `consoleModeEnabled` を設定するだけ。 |
| `addCommand()` | `Name` が `New Command` のコマンド定義を追加し、インスペクタを更新する。 |
| `setConsoleModeEnabledStateFromEditor(bool state)` | 状態を設定したうえで `updateComponent` を呼び、シーンをダーティにする。 |
| `updateComponent()` | `GKC_Utils.updateComponent` と `updateDirtyScene` を呼び、表示とシーンを更新する。 |

## 内部型

- `commandInfo`（class）
