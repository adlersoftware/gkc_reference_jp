# saveGameSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Save System/saveGameSystem.cs:13`
- **属性**: `System.Serializable`

**概要**: セーブステーションのUIとセーブ/ロード処理を束ねる管理コンポーネント。スロット一覧を`BinaryFormatter`で`.txt`へ読み書きし、各`saveInfo`へ個別データの保存・読込を委譲する。

**公式ドキュメント抜粋**（[Save Game System](../../docs/character-level-components/character/save-game-system.md)）

> It manages the main save system menu that the player can use at any moment in-game. Of course, the game can use only save stations in fixed places to save the game, instead of allowing you to save at any moment.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Scene To Load New Game | `sceneToLoadNewGame` | `int` | – | – |
| Save Station Id | `saveStationId` | `int` | – | – |
| Is Physical Save Station | `isPhysicalSaveStation` | `bool` | true | – |
| Use Player Camera Orientation | `usePlayerCameraOrientation` | `bool` | – | – |
| Manual Save Enabled | `manualSaveEnabled` | `bool` | true | – |
| Default Player ID | `defaultPlayerID` | `int` | 0 | – |

### Current Scene Index Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Custom Current Scene Index | `setCustomCurrentSceneIndex` | `bool` | – | – |
| Custom Current Scene Index | `customCurrentSceneIndex` | `int` | – | – |

### Load Screen Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Load Screen | `useLoadScreen` | `bool` | – | – |
| Load Screen Scene | `loadScreenScene` | `int` | 1 | – |
| Use Last Scene Index As Load Screen | `useLastSceneIndexAsLoadScreen` | `bool` | true | – |
| Scene To Load Async Prefs Name | `sceneToLoadAsyncPrefsName` | `string` | "SceneToLoadAsync" | – |
| Check Loading Screen Scene Configured | `checkLoadingScreenSceneConfigured` | `bool` | true | – |
| Loading Screen Scene Name | `loadingScreenSceneName` | `string` | "Loading Screen Scene" | – |

### Checkpoint Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Checkpoint Slot Can Be Deleted Enabled | `checkpointSlotCanBeDeletedEnabled` | `bool` | – | – |
| Delete Hidden Checkpoint Save On New Game Enabled | `deleteHiddenCheckpointSaveOnNewGameEnabled` | `bool` | – | – |
| Delete Hidden Checkpoint Save On Continue Game Enabled | `deleteHiddenCheckpointSaveOnContinueGameEnabled` | `bool` | – | – |
| Overwrite Checkpoint Slot When Saving On Return To Home | `overwriteCheckpointSlotWhenSavingOnReturnToHome` | `bool` | – | – |

### Save Game Icon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Saving Icon | `useSavingIcon` | `bool` | – | – |
| Use Canvas Group On Show Saving Game Panel | `useCanvasGroupOnShowSavingGamePanel` | `bool` | true | – |
| Show Saving Game Panel Duration | `showSavingGamePanelDuration` | `float` | 3 | – |
| Show Saving Game Panel Fade Speed | `showSavingGamePanelFadeSpeed` | `float` | 5 | – |
| Saving Game Animation Name | `savingGameAnimationName` | `string` | – | – |
| Animation Speed | `animationSpeed` | `float` | 0.5f | – |

### Physical Save Station Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Animation Name | `animationName` | `string` | – | – |
| Save Position Layermask | `savePositionLayermask` | `LayerMask` | – | – |

### Save Element List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Save Info List | `saveInfoList` | `List<saveInfo>` | new List<saveInfo> () | – |
| Save Info List To Load On Start On All Scenes Enabled | `saveInfoListToLoadOnStartOnAllScenesEnabled` | `bool` | – | – |
| Save Number To Load On Start On All Scenes | `saveNumberToLoadOnStartOnAllScenes` | `int` | 143 | – |
| Save Info List To Load On Start On All Scenes | `saveInfoListToLoadOnStartOnAllScenes` | `List<saveInfo>` | new List<saveInfo> () | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Chapter Text Field | `chapterTextField` | `string` | "Chapter" | – |
| Save Text Field | `saveTextField` | `string` | "Save" | – |
| Disable Buttons Color | `disableButtonsColor` | `Color` | – | – |
| Capture Resolution | `captureResolution` | `Vector2` | – | – |

### Custom Save Element List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Custom Save List Info List | `customSaveListInfoList` | `List<customSaveListInfo>` | new List<customSaveListInfo> () | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event If Game To Continue Available | `useEventIfGameToContinueAvailable` | `bool` | – | – |
| Eventf Game To Continue Available | `eventfGameToContinueAvailable` | `UnityEvent` | – | – |

### Event Settings On Save/Load Game

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Save Game | `useEventOnSaveGame` | `bool` | – | – |
| Event On Save Game | `eventOnSaveGame` | `eventParameters.eventToCallWithInteger` | – | – |
| Use Event On Load Game | `useEventOnLoadGame` | `bool` | – | – |
| Event On Load Game | `eventOnLoadGame` | `eventParameters.eventToCallWithInteger` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Info | `showDebugInfo` | `bool` | – | – |
| Ignore Show Debug Info On Save | `ignoreShowDebugInfoOnSave` | `bool` | – | – |
| Ignore Show Debug Info On Load | `ignoreShowDebugInfoOnLoad` | `bool` | – | – |
| Using Save Station | `usingSaveStation` | `bool` | – | – |
| Can Save | `canSave` | `bool` | – | – |
| Can Load | `canLoad` | `bool` | – | – |
| Can Delete | `canDelete` | `bool` | – | – |
| Save Game List Elements | `saveGameListElements` | `List<buttonInfo>` | new List<buttonInfo> () | – |
| Main Save Station Info | `mainSaveStationInfo` | `saveStationInfo` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Save Station Position | `saveStationPosition` | `Transform` | – | – |
| Saving Icon | `savingIcon` | `GameObject` | – | – |
| Player Camera Game Object | `playerCameraGameObject` | `GameObject` | – | – |
| Player Controller Game Object | `playerControllerGameObject` | `GameObject` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera Manager | `mainPlayerCameraManager` | `playerCamera` | – | – |
| Main Player Components Manager | `mainPlayerComponentsManager` | `playerComponentsManager` | – | – |
| Game Manager Component | `gameManagerComponent` | `gameManager` | – | – |
| Save Menu | `saveMenu` | `GameObject` | – | – |
| Save Button | `saveButton` | `Image` | – | – |
| Load Button | `loadButton` | `Image` | – | – |
| Delete Button | `deleteButton` | `Image` | – | – |
| Scroll Bar | `scrollBar` | `Scrollbar` | – | – |
| Save Game List | `saveGameList` | `GameObject` | – | – |
| Photo Capturer | `photoCapturer` | `Camera` | – | – |

### Save Game System Info Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slot Info Number Debug | `slotInfoNumberDebug` | `int` | – | – |
| Show All Game Info Debug | `showAllGameInfoDebug` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `startGameSystem()` | `gameManager`を取得し、データパス・スロットUI・非表示のチェックポイント/自動セーブ枠を初期化して`initialized`を立てる。 |
| `addSaveSlot(int index)` | スロットプレハブを複製して`Save Game Slot (index+2)`と命名し、`buttonInfo`を一覧へ追加する。 |
| `setSaveGameTransformInfo(Transform savePosition, bool canUsePlayerCameraOrientation)` | セーブ位置と角度を`mainSaveStationInfo`へ格納し、許可時はカメラとピボットの角度も保存する。 |
| `activateSaveStation()` | `usingSaveStation`を反転し、メニュー表示・`loadStates`・駅アニメの正逆再生を切り替える。 |
| `openSaveGameMenu()` | `loadStates`で一覧を更新し、ボタン色を戻してセーブ位置とスクロールを再設定する。 |
| `getSaveButtonSelected(Button button)` | 押されたボタンの番号を`currentButtonIndex`に保持し、情報の有無でセーブ/ロード/削除の可否と色を切り替える。 |
| `showSaveInfoDebug()` | `showAllGameInfoDebug`なら全体を、そうでなければ該当スロットを表示して`gameManager`のデバッグ出力を呼ぶ。 |
| `showSaveInfoDebug(int saveNumberToDelete, string currentSaveDataPath, string extraFileString)` | `loadInfoEnabled`な各`saveInfo`でパスを組み立て、第1引数の番号を`showSaveInfoDebug`へ渡す。 |
| `newGame()` | 必要なら非表示チェックポイントを削除し、`PlayerPrefs`の`loadingGame`を0にして新規ゲームのシーンを読み込む。 |
| `continueGame()` | 自動セーブ以外で最も新しい日時のスロットを探し、その情報を`gameManager`へ渡して続きから開始する。 |
| `saveGameOnHiddenSlotIndex(int saveSlotIndex)` | 指定スロットへ、カスタム位置なし・非チェックポイント・非表示の条件でセーブする。 |
| `setSavingGameManuallyActiveState(bool state)` | 手動セーブ中かどうかのフラグ`savingGameManuallyActive`を設定するだけ。 |
| `saveGame()` | 選択中ボタンのスロットを`infoAdded`にして手動セーブフラグを立て、`saveCurrentGame`を呼ぶ。 |
| `saveGameBySlotIndex(int slotIndex)` | 指定スロットのボタンを選択状態にして`canSave`を立て、`saveGame`を呼ぶ。 |
| `playSavingGameAnimation()` | `CanvasGroup`使用時はフェード表示を、そうでなければセーブアイコンのアニメ再生を行う。 |
| `showSavingGamePanelInfo()` | 実行中のコルーチンを止め、アイコンをフェードイン→待機→フェードアウトするコルーチンを開始する。 |
| `saveGameCheckpoint(Transform customTransform, int checkpointID, int checkpointSceneID, bool overwriteThisCheckpointActive, bool savingGameToChangeScene, bool autoSaveGameOnSceneChangeEnabled)` | 自動ロード用かチェックポイント用の枠を選び、同一チェックポイントなら中止、そうでなければ位置を設定して`saveCurrentGame`を呼ぶ。 |
| `saveCurrentGame(int saveSlotIndex, bool useCustomSaveTransform, bool isCheckpointSave, int checkpointID, int checkpointSceneID, bool savingGameToChangeScene, bool showSaveSlot, bool saveGameInfoActive)` | セーブ情報を更新して一覧を`.txt`へ`BinaryFormatter`で書き出し、各`saveInfo`を保存し自動ロード枠へ複製する。 |
| `saveCustomInfoList(string listName)` | 指定名のカスタムリストに含まれる`saveInfo`だけを、そのリストの`saveNumber`で保存する。 |
| `saveGameInfoFromEditor(int saveNumberToLoad, string infoTypeName, string extraFileString)` | `infoTypeName`に一致する`saveInfo`の`saveGameFromEditor`を、エディタから呼び出す。 |
| `saveGameOnCheckpointSlot()` | `saveGameWhenReturningHomeMenu`を呼ぶだけの別名メソッド。 |
| `saveGameWhenReturningHomeMenu()` | 手動セーブフラグを立ててから、ホームメニュー復帰用に`saveGameCheckpoint`を呼び、フラグを戻す。 |
| `getSaveInfoList()` | `saveInfoList`をそのまま返すだけ。 |
| `checkGameInfoToLoad(int lastSaveNumber, string currentSaveDataPath, string extraFileString)` | 各`saveInfo`で`loadGame`を呼び、自動ロードでない場合は自動ロード枠の情報を選択スロットへ複製する。 |
| `deleteGameInfo(int saveNumberToDelete, string currentSaveDataPath, string extraFileString)` | 有効な各`saveInfo`に対し、指定セーブ番号のデータ削除を`deleteGameInfo`へ委譲する。 |
| `checkComponentsToInitialize()` | 各`saveInfo`の`initializeValuesOnComponent`を呼び、必要なら名前をデバッグ出力する。 |
| `checkSaveInfoListToLoadOnStartOnAllScenes()` | フラグとリストが有効なとき、開始時読込用の各`saveInfo`へ`checkSaveInfoToLoadOnStartOnAllScenes`を渡す。 |
| `updateSaveSlotContent(int saveSlotIndex, saveStationInfo newSave)` | スロットUIのアイコン(PNG)・チャプター名・プレイ時間・番号・日時のテキストを更新する。 |
| `reloadLastCheckpoint()` | 自動ロード用でない最初のチェックポイント枠を選び、`canLoad`を立てて`loadGame`を呼ぶ。 |
| `activateAutoLoad()` | `usedForAutoLoadSave`の枠を選んで`canLoad`を立て、`loadGame`を呼ぶ。 |
| `loadGameBySlotIndex(int slotIndexToLoad)` | 範囲内なら指定スロットを選択状態にして`canLoad`を立て、`loadGame`を呼ぶ。 |
| `loadGame()` | 現在のスロット番号に一致するセーブを一覧から取り、`gameManager`へ渡して`eventOnLoadGame`を発火する。 |
| `deleteAllGames()` | 全スロットを順に確認し、削除可能と判定したものだけ`deleteGame`で消す。 |
| `deleteGame()` | 対象スロットのPNGを削除し、一覧から項目を除いてUIを空表示にし、`.txt`を再シリアライズする。 |
| `changeButtonsColor(bool state, bool save, bool load, bool delete)` | 各ボタンの色と`canSave`等の可否を設定し、`state`がfalseなら選択中ボタンを解除する。 |
| `loadStates()` | セーブ一覧を読み込み、各スロットUIへ内容を反映し、空き枠は空表示、手動セーブ無効時は通常枠を隠す。 |
| `setPhotoCapturerState(bool state)` | 物理セーブステーションのときだけ`photoCapturer.enabled`を切り替える。 |
| `loadFile()` | `BinaryFormatter`でセーブ一覧の`.txt`を読み込み、`List<saveStationInfo>`として返す。 |
| `isThereSaveSlotsLoaded()` | ファイルを読み込み、`showSaveSlot`が真のセーブが1件でもあればtrueを返す。 |
| `setStationIde(int idValue)` | `mainSaveStationInfo.id`を設定するだけ。 |
| `showSaveList(List<saveStationInfo> saveList)` | `showDebugInfo`が有効なときだけ、一覧の各要素を`showSaveSlotInfo`で出力する。 |
| `showSaveSlotInfo(saveStationInfo saveSlot, int saveIndex)` | 1件分のチャプター・位置・シーン番号・ID・セーブ番号・時間・日時を`print`する。 |
| `getPlayerComponents()` | 未取得なら`electronicDeviceManager`から現在のプレイヤーを取り、操作・カメラの各参照を埋める。 |
| `resetScroll(Scrollbar scrollBarToReset)` | 2フレーム待ってからスクロールバーの値を1にするコルーチンを開始する。 |
| `getLastSaveSlotIndex()` | スロットUIリストの末尾インデックスを返す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventfGameToContinueAvailable` | `UnityEvent` | – |

## 内部型

- `saveStationInfo`（class）
- `buttonInfo`（class）
- `customSaveListInfo`（class）
