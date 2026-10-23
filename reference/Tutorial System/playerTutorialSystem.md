# playerTutorialSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Tutorial System/playerTutorialSystem.cs:15`

**概要**: チュートリアルのパネル送り・動画再生・入力停止をまとめて行い、カーソルやカメラ、ポーズ状態をチュートリアル表示に合わせて切り替える管理コンポーネント。

**公式ドキュメント抜粋**（[Player Tutorial System](../../docs/character-level-components/character/player-tutorial-system.md)）

> Used to manage the player tutorial UI and the different tutorials configured on it.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tutorials Enabled | `tutorialsEnabled` | `bool` | – | ONにするとチュートリアル表示の要求を受け付ける。 |
| Instantiate Tutorial Panel If Not Found | `instantiateTutorialPanelIfNotFound` | `bool` | – | ONならUI未配置時にパネルを自動生成する。 |
| Min Time To Press Key | `minTimeToPressKey` | `float` | 0.4f | パネル送りキーを受け付ける最小間隔（秒）。 |

### Tutorial State (Debug)

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tutorial Opened | `tutorialOpened` | `bool` | – | チュートリアルが表示中かどうかの実行時状態。 |
| Main Tutorial UI System Found | `mainTutorialUISystemFound` | `bool` | – | UIシステムを検出できたかを示す実行時フラグ。 |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tutorial Panel Prefab | `tutorialPanelPrefab` | `GameObject` | – | UIが無い時に生成するチュートリアルパネルのプレハブ。 |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | 入力の停止や再開に使う`playerController`。 |
| Pause Manager | `pauseManager` | `menuPause` | – | ポーズ状態の確認やメニュー制御に使う`menuPause`。 |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | チュートリアル開始音を再生する`AudioSource`。 |
| Main Tutorial UI System | `mainTutorialUISystem` | `tutorialUISystem` | – | パネルや動画を提供する`tutorialUISystem`。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `currentTutorialIndex` | `int` | – | – |
| `currentTutorialPanelIndex` | `int` | – | – |
| `tutorialsPanel` | `Transform` | – | – |
| `videoAudioSource` | `AudioSource` | – | – |
| `tutorialInfoList` | `List<tutorialInfo>` | new List<tutorialInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopCheckTutorialOpenedState()` | チュートリアル開閉の監視コルーチンが存在すれば停止するだけ。 |
| `checkTutorialOpenedState()` | 既存の監視を止め、開閉状態を短い間隔で更新し続けるコルーチンを開始する。 |
| `activatingTutorialByNameFromEditor()` | エディタからの起動であることを示す`activatingTutorialByNameFromEditorState`を立てるだけ。 |
| `activateTutorialByName(string tutorialName)` | 名前が一致するチュートリアルを選び、一度だけ再生の設定を確認して最初のパネルを開く。 |
| `checkOpenOrCloseTutorial(bool state)` | メニューでポーズ中なら即座に開閉し、そうでなければ入力を止めて遅延付きで開くコルーチンを開始する。 |
| `stopCheckOpenOrCloseTutorial()` | チュートリアル開閉用のコルーチンが存在すれば停止するだけ。 |
| `setNextPanelOnTutorial()` | 現在パネルを隠して次を表示し、動画があれば再生、末尾ならチュートリアルを閉じる。 |
| `setPreviousPanelOnTutorial()` | 現在パネルを隠して`currentTutorialPanelIndex`を1つ戻し、戻したパネルも非表示にする。 |
| `openOrCloseTutorial(bool opened)` | 開閉状態に応じてパネル表示、入力停止、カーソル・カメラ・ポーズ状態、タイムスケールを切り替える。 |
| `resumePlayerInput()` | 再開コルーチンを止め、タイムスケール0なら即座に、そうでなければ0.5秒後にプレイヤー入力を再開する。 |
| `stopResumePlayerInputCoroutine()` | プレイヤー入力の再開コルーチンが存在すれば停止するだけ。 |
| `playTutorialVideo(tutorialInfo newTutorialInfo)` | 既存の動画コルーチンを止め、`newTutorialInfo`の動画を再生するコルーチンを開始する。 |
| `stopTutorialVideoCoroutine()` | 再生中の動画と音声を止め、動画コルーチンが存在すれば停止する。 |
| `closeTutorial()` | 現在パネルとチュートリアル全体を非表示にし、動画があれば止めて`currentVideoIndex`を0に戻す。 |
| `callNextTutorialPanel()` | チュートリアル表示中かつアクションボタン送りの設定なら`setNextPanelOnTutorial`を呼ぶ。 |
| `resetAllTutorials()` | 全チュートリアルのパネルを非表示にし、各チュートリアルの先頭パネルだけを表示状態に戻す。 |
| `setTutorialsEnabledState(bool state)` | チュートリアルの有効フラグ`tutorialsEnabled`を設定するだけ。 |
| `setTutorialUISystem(tutorialUISystem newTutorialUISystem)` | `mainTutorialUISystem`を設定してコンポーネントを更新するだけ。 |
| `instantiateTutorialPanelPrefab()` | UIシステムが未設定なら、チュートリアルパネルのプレハブを生成してプレイヤー側システムを検索させる。 |
| `setTutorialsEnabledStateFromEditor(bool state)` | 有効状態を設定したうえでコンポーネントを更新するだけ。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とシーン更新でインスペクタ表示を更新するだけ。 |
