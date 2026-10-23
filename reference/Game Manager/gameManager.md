# gameManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Game Manager/gameManager.cs:9`

**概要**: ゲーム全体の状態（ポーズ、プレイ時間、FPS上限、チャプター名、セーブパス、タッチ操作可否）を保持し、セーブ/ロードとプレイヤー構成の窓口になる。

**公式ドキュメント抜粋**（[Game Manager](../../docs/toplevelcomponents/player-and-game-management/game-manager.md)）

> It contains some settings related to the save of info, like the path used for it and the main name for the files along with other minor settings.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Limit Fps | `limitFps` | `bool` | – | – |
| Update Limit Fps If Change Detected | `updateLimitFpsIfChangeDetected` | `bool` | – | – |
| Target Fps | `targetFps` | `int` | 60 | – |

### Chapter Info

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Chapter Info | `chapterInfo` | `string` | – | – |

### Save Info

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Load Enabled | `loadEnabled` | `bool` | – | – |
| Use Relative Path | `useRelativePath` | `bool` | – | – |
| Load Player Position Enabled | `loadPlayerPositionEnabled` | `bool` | true | – |
| Load Player Position On Scene Change Enabled | `loadPlayerPositionOnSceneChangeEnabled` | `bool` | true | – |
| Check Player Driving State On Load Enabled | `checkPlayerDrivingStateOnLoadEnabled` | `bool` | true | – |
| Delete All Player Prefs On Load Enabled | `deleteAllPlayerPrefsOnLoadEnabled` | `bool` | true | – |
| Save Info List To Load On Start On All Scenes Enabled Only When Loading | `saveInfoListToLoadOnStartOnAllScenesEnabledOnlyWhenLoading` | `bool` | – | – |

### Load Screen Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Load Screen | `useLoadScreen` | `bool` | – | – |
| Load Screen Scene | `loadScreenScene` | `int` | 1 | – |
| Use Last Scene Index As Load Screen | `useLastSceneIndexAsLoadScreen` | `bool` | true | – |
| Scene To Load Async Prefs Name | `sceneToLoadAsyncPrefsName` | `string` | "SceneToLoadAsync" | – |
| Check Loading Screen Scene Configured | `checkLoadingScreenSceneConfigured` | `bool` | true | – |
| Loading Screen Scene Name | `loadingScreenSceneName` | `string` | "Loading Screen Scene" | – |

### Version Number Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Version Number | `versionNumber` | `string` | "3-01" | – |

### Save File Names Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Save Game Folder Name | `saveGameFolderName` | `string` | "Save" | – |
| Save File Name | `saveFileName` | `string` | "Save State" | – |
| Save Capture Folder | `saveCaptureFolder` | `string` | "Captures" | – |
| Save Capture File Name | `saveCaptureFileName` | `string` | "Photo" | – |
| Touch Controls Position Folder Name | `touchControlsPositionFolderName` | `string` | "Touch Buttons Position" | – |
| Touch Controls Position File Name | `touchControlsPositionFileName` | `string` | "Touch Positions" | – |
| Save Input File Folder Name | `saveInputFileFolderName` | `string` | "Input" | – |
| Save Input File Name | `saveInputFileName` | `string` | "Input File" | – |
| Default Input Save File Name | `defaultInputSaveFileName` | `string` | "Default Input File" | – |
| File Extension | `fileExtension` | `string` | ".txt" | – |
| Slot By Save Station | `slotBySaveStation` | `int` | – | – |
| Save Camera Capture | `saveCameraCapture` | `bool` | true | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |

### Debug Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Save Number To Load | `saveNumberToLoad` | `int` | -1 | – |
| Current Persistent Data Path | `currentPersistentDataPath` | `string` | – | – |
| Current Save Data Path | `currentSaveDataPath` | `string` | – | – |

### Save List Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Save List | `saveList` | `List<saveGameSystem.saveStationInfo>` | new List<saveGameSystem.saveStationIn… | – |

### Current Game State Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Game Paused | `gamePaused` | `bool` | – | – |
| Use Touch Controls | `useTouchControls` | `bool` | false | – |
| Touch Platform | `touchPlatform` | `bool` | – | – |
| Play Time | `playTime` | `float` | – | – |

### Game Manager Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Characters Manager | `charactersManager` | `playerCharactersManager` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Main Player Game Object | `mainPlayerGameObject` | `GameObject` | – | – |
| Main Player Camera Game Object | `mainPlayerCameraGameObject` | `GameObject` | – | – |
| Current Player Camera | `currentPlayerCamera` | `playerCamera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 自身を`Instance`に登録し、既に別インスタンスがあれば自身のGameObjectを破棄する。 |
| `getComponentInstanceOnApplicationPlaying()` | 再生中のみ`getComponentInstance`を呼び、インスタンスを登録する。 |
| `deleteGameInfo(int saveNumberToDelete)` | ロードが有効なら、バージョン付き拡張子とパスを添えて`charactersManager`へセーブ削除を依頼する。 |
| `showSaveInfoDebug(int saveNumberToShow)` | ロードが有効なら、パスと拡張子を添えて`charactersManager`へセーブ情報の表示を依頼する。 |
| `saveGameInfoFromEditor(string infoTypeName)` | ロード有効かつ保存番号が設定済みなら、`charactersManager`へエディタからの保存を依頼する。 |
| `saveGameWhenReturningHomeMenu()` | ロードが有効なら、`charactersManager`へホームメニュー帰還時の保存を依頼する。 |
| `getPlayerPrefsInfo(saveGameSystem.saveStationInfo save)` | セーブ地点の番号・位置・回転・車両状態を`PlayerPrefs`に書き込み、`GKC_Utils.loadScene`でシーンを読み込む。 |
| `getDataPath()` | `useRelativePath`に応じてセーブフォルダのパスを作り、無ければ作成して末尾に`/`を付けて返す。 |
| `getDataName()` | セーブファイル名とバージョン番号を連結して返すだけ。 |
| `getVersionNumber()` | `versionNumber`を返すだけ。 |
| `getFileExtension()` | `fileExtension`を返すだけ。 |
| `getCurrentSaveList()` | `saveList`を返すだけ。 |
| `setSaveList(List<saveGameSystem.saveStationInfo> currentList)` | 受け取ったリストを`saveList`に代入するだけ。 |
| `getLastSaveNumber()` | PlayerPrefsの`saveNumber`を優先し、無ければ`saveNumberToLoad`から直近のセーブ番号を求める。 |
| `getSlotBySaveStation()` | `slotBySaveStation`を返すだけ。 |
| `setGamePauseState(bool state)` | `gamePaused`を`state`にするだけ。 |
| `isGamePaused()` | `gamePaused`を返すだけ。 |
| `isUsingTouchControls()` | `useTouchControls`を返すだけ。 |
| `setUseTouchControlsState(bool state)` | `useTouchControls`を`state`にするだけ。 |
| `setCharactersManagerPauseState(bool state)` | `charactersManager`のポーズ状態を`state`にするだけ。 |
| `getMainPlayerController()` | `charactersManager`からメインプレイヤーの`playerController`をそのまま返す。 |
| `anyCharacterDead()` | `charactersManager`に問い合わせ、死亡キャラの有無を返す。 |
| `getSaveCaptureFolder()` | `saveCaptureFolder`を返すだけ。 |
| `getSaveCaptureFileName()` | `saveCaptureFileName`を返すだけ。 |
| `getTouchControlsPositionFolderName()` | `touchControlsPositionFolderName`を返すだけ。 |
| `getTouchControlsPositionFileName()` | `touchControlsPositionFileName`にバージョン番号を付けて返す。 |
| `isLoadGameEnabled()` | `loadEnabled`を返すだけ。 |
| `setNewChapterName(string newName)` | `chapterInfo`を`newName`にするだけ。 |
| `getChapterName()` | `chapterInfo`を返すだけ。 |
| `getPlayTime()` | `playTime`を返すだけ。 |
| `setPlayTimeValue(float newValue)` | `playTime`を`newValue`にするだけ。 |
| `setMainCamera(Camera newCamera)` | `mainCamera`を差し替えるだけ。 |
| `setMainPlayerGameObject(GameObject newMainPlayerGameObject)` | `mainPlayerGameObject`を差し替えるだけ。 |
| `setMainPlayerCameraGameObject(GameObject newMainPlayerCameraGameObject)` | `mainPlayerCameraGameObject`を差し替えるだけ。 |
| `setCurrentPlayerCamera(playerCamera newCurrentPlayerCamera)` | `currentPlayerCamera`を差し替えるだけ。 |
| `updateMainPlayerComponentsOnGameManager(GameObject newPlayerParent)` | 親から`playerComponentsManager`を探し、メインプレイヤー・カメラ・カメラGameObjectを設定してエディタ状態を更新する。 |
| `setUseTouchControlsStateFromEditor(bool state)` | エディタ用に`useTouchControls`を設定し、コンポーネントとシーンを更新する。 |
| `setCurrentPersistentDataPath()` | `Application.persistentDataPath`を`currentPersistentDataPath`に取り直して更新する。 |
| `deletePlayerPrefs()` | `PlayerPrefs.DeleteAll`で全セーブ設定を消し、ログを出す。 |
| `openCurrentSaveFolder()` | 現在のセーブパスを求め、`showExplorer`でエクスプローラを開く。 |
| `showExplorer(string itemPath)` | パスが存在すれば`explorer.exe /select`でエクスプローラを開く。 |
| `getCurrentDataPath()` | 永続パスを更新してセーブ用パスを`currentSaveDataPath`に設定し、エディタ状態を更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`でGameManagerの変更をエディタへ反映する。 |
