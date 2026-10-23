# playerCharactersManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Game Manager/playerCharactersManager.cs:8`

**概要**: シーン上のプレイヤー達をリスト管理し、生成・ID割り当て・カメラ/HUD/マップ設定・操作キャラの切替をまとめて行うマネージャー。セーブ処理も各プレイヤーの`saveGameSystem`へ中継する。

**公式ドキュメント抜粋**（[Player Characters Manager](../../docs/toplevelcomponents/player-and-game-management/player-characters-manager.md)）

> Used for the management of multiple players in the same scene, for the use of local multiplayer and the switch companion AI.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Search Players At Start | `searchPlayersAtStart` | `bool` | – | 起動時にシーンの全`playerController`をプレイヤー登録する。 |
| Ignore Check Empty Characters On Start Enabled | `ignoreCheckEmptyCharactersOnStartEnabled` | `bool` | – | 起動時の空のプレイヤー要素のチェックを省略する。 |
| Current Number Of Players | `currentNumberOfPlayers` | `int` | 1 | ローカルプレイヤー数。カメラ分割とUI解像度の設定に使う。 |
| Main Character | `mainCharacter` | `GameObject` | – | メインプレイヤーとして扱う親`GameObject`。 |
| New Player Position Offset | `newPlayerPositionOffset` | `Vector3` | – | 追加プレイヤーを配置する時に加える位置のずれ。 |
| Regular Reference Resolution | `regularReferenceResolution` | `Vector2` | new Vector2 (1280, 720) | シングルプレイ時のCanvasの基準解像度。 |
| Split Reference Resolution | `splitReferenceResolution` | `Vector2` | new Vector2 (2560, 1440) | 画面分割時のCanvasの基準解像度。 |
| Camera State Name To Use | `cameraStateNameToUse` | `string` | "1 Player" | プレイヤーカメラに適用するカメラ状態の名前。 |

### Configure/Spawn Multiple Players On Awake Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Configure Local Multiplayer Characters On Awake | `configureLocalMultiplayerCharactersOnAwake` | `bool` | – | 起動時に複数プレイヤーを設定・生成する。 |
| Number Of Players On Awake | `numberOfPlayersOnAwake` | `int` | – | 起動時に設定するローカルプレイヤー数。 |
| Camera State Name On Awake | `cameraStateNameOnAwake` | `string` | – | 起動時に適用するカメラ状態の名前。 |
| Extra Player Prefab | `extraPlayerPrefab` | `GameObject` | – | 追加のローカルプレイヤーを生成するプレハブ。 |
| Initial Multiplayer Spawn Position | `initialMultiplayerSpawnPosition` | `Transform` | – | 複数プレイヤーの初期配置位置と向き。 |

### Online Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Online Player Prefab | `onlinePlayerPrefab` | `GameObject` | – | オンラインプレイヤーを生成するプレハブ。 |
| Use Transform Position List To Spawn Online Player | `useTransformPositionListToSpawnOnlinePlayer` | `bool` | – | オンラインプレイヤーの生成位置に`Transform`リストを使う。 |
| Spawn Online Players On Start | `spawnOnlinePlayersOnStart` | `bool` | – | 起動時にオンラインプレイヤーを生成する。 |
| Number Of Online Players To Spawn On Start | `numberOfOnlinePlayersToSpawnOnStart` | `int` | – | 起動時に生成するオンラインプレイヤーの数。 / 表示条件: `spawnOnlinePlayersOnStart` がオンのとき |

### Use AI As Partner To Switch Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Current Character To Control And AI At Start | `setCurrentCharacterToControlAndAIAtStart` | `bool` | – | 開始時に操作キャラを設定し他をAIにする切替を有効にする。 |
| Keep Active Only Current Player Selected | `keepActiveOnlyCurrentPlayerSelected` | `bool` | – | 選択中のキャラ以外を非アクティブにして切り替える。 |
| Change Camera Position At Once On Character Change | `changeCameraPositionAtOnceOnCharacterChange` | `bool` | – | キャラ切替時にカメラを即座に移動させる。 |
| Set Current Player Position To Previous Character | `setCurrentPlayerPositionToPreviousCharacter` | `bool` | – | 切替先のキャラを前のキャラの位置と向きに移動させる。 |
| Current Character To Control Name | `currentCharacterToControlName` | `string` | "Player 1" | 開始時に操作するキャラクターの名前。 |
| Delay Time To Change Between Characters | `delayTimeToChangeBetweenCharacters` | `float` | 1 | キャラクターを切り替えられるようになるまでの秒数。 |

### Dynamic Split Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Dynamic Split Screen System | `mainDynamicSplitScreenSystem` | `dynamicSplitScreenSystem` | – | 2人プレイ時に使う動的スプリットスクリーンシステム。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `playerList` | `List<playerInfo>` | new List<playerInfo> () | – |
| `cameraStatesList` | `List<cameraStates>` | new List<cameraStates> () | – |
| `extraCharacterList` | `List<GameObject>` | new List<GameObject> () | – |
| `auxPlayerList` | `List<GameObject>` | new List<GameObject> () | – |
| `currentPlayeraInfoActive` | `playerInfo` | – | – |
| `cameraStatesListString` | `string []` | – | – |
| `currentCameraStateIndex` | `int` | – | – |
| `transformPositionListToSpawnOnlinePlayer` | `List<Transform>` | new List<Transform> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 自身を`Instance`に登録し、既に別インスタンスがあれば自身のGameObjectを破棄する。初期化済みなら何もしない。 |
| `getComponentInstanceOnApplicationPlaying()` | 再生中のみ`getComponentInstance`を呼び、インスタンスを登録する。 |
| `checkPlayerElementsOnScene()` | プレイヤー要素にnullがあれば`searchPlayersOnTheLevel`でシーンから再取得する。 |
| `spawnPlayerOnSceneForMultiplayer()` | `onlinePlayerPrefab`を生成し、オンライン用プレイヤーとして登録する。 |
| `addSpawnedPlayerOnSceneForMultiplayerWithCustomPositionRotation(GameObject newCharacter, Vector3 newPosition, Quaternion newRotation)` | 指定位置と回転を一時フラグに退避して`addSpawnedPlayerOnSceneForMultiplayer`を呼び、登録後にフラグを戻す。 |
| `addSpawnedPlayerOnSceneForMultiplayer(GameObject newCharacter)` | 新キャラを子にし、`playerComponentsManager`から情報を登録して出現位置も設定する。 |
| `addExtraPlayerOnSceneForMultiplayer(int numberOfExtraPlayers)` | `extraPlayerPrefab`を指定数生成して子にし、プレイヤー情報を更新した後、全員を初期マルチ位置からずらして配置する。 |
| `addNewPlayerSpawned(GameObject newPlayer)` | 新プレイヤーを子にし、プレイヤー情報を再取得した後、カメラ・HUD・ID・マップを再設定する。 |
| `setNewPositionToPlayersOnScene(List<Transform> positionList)` | 各プレイヤーを`positionList`の同インデックスの位置・回転へ設定するが、要素数の判定条件が逆になっている。 |
| `updatePlayersInfoOnTheLevel()` | `searchPlayersOnTheLevel(false, false)`を呼び、プレイヤー情報を作り直すだけ。 |
| `checkNotNullPlayerElements()` | リストが空、または操作オブジェクトがnullの要素があればtrueを返す。 |
| `searchPlayersOnTheLevel(bool creatingNewPlayers, bool creatingCharactersOnEditor)` | シーン内の`playerController`からAI操作でないものを集め、`playerList`を作り直して各情報を登録する。 |
| `setExtraCharacterList()` | メインキャラ以外のプレイヤー親オブジェクトを`extraCharacterList`に詰め直し、エディタ状態を更新する。 |
| `setPlayerID(bool creatingCharactersOnEditor)` | 各プレイヤーに1始まりのIDを割り当て、`useOnlyKeyboard`のプレイヤー分だけIDを減らして重複を避ける。 |
| `setNumberOfPlayers(bool creatingCharactersOnEditor)` | `currentNumberOfPlayers`に合わせてメインキャラを複製するか余剰キャラを削除し、プレイヤー情報を再構築する。 |
| `setCameraConfiguration(bool creatingCharactersOnEditor)` | `cameraStateNameToUse`の状態から各カメラの`rect`を設定し、マルチ時はキャンバスを分割用設定へ切り替える。 |
| `updateCanvasValuesByPlayer(GameObject playerControllerGameObject, GameObject pauseManagerObject, GameObject newCanvasPanel)` | 指定プレイヤーの`menuPause`に新キャンバスを登録し、マルチ時のみ分割用のカメラ設定を適用する。 |
| `updateHUD(bool creatingCharactersOnEditor)` | 全プレイヤーの`pauseManager.setCanvasInfo`を呼んでHUDを更新するだけ。 |
| `assignMapSystem(bool creatingCharactersOnEditor)` | `mapCreator`を取得し、無ければ生成した上で、各プレイヤーの`mapSystem`をマップへ登録する。 |
| `updateMainPlayerComponentsOnGameManager(bool creatingCharactersOnEditor)` | `mainCharacter`があれば`GKC_Utils.updateMainPlayerComponentsOnGameManager`に渡すだけ。 |
| `enableOrDisableSingleCameraState(bool state, bool creatingCharactersOnEditor)` | 各プレイヤーカメラの複数ターゲット追従を`state`にし、有効時は全プレイヤーのTransformを追従対象に設定する。 |
| `enableOrDisableDynamicSplitCameraState(bool state, bool creatingCharactersOnEditor)` | 2人以上なら`mainDynamicSplitScreenSystem`を`state`で有効化し、各プレイヤーの動的UI表示を反転設定する。 |
| `getCameraStateByName(string cameraStateName)` | 名前が一致する`cameraStates`を返し、見つからなければnullを返す。 |
| `setAsCurrentPlayerActive(string playerName)` | 現在プレイヤーの位置・回転を退避し、指定名のプレイヤーをその位置へ移してアクティブにする。 |
| `setAsCurrentCharacterToControlByName(string playerName)` | 指定名のキャラを操作対象にし、他をAI化して、カメラ・入力・HUD・コンパニオン設定を切り替える。 |
| `toogleUseOnlyKeyboardGamepad(string playerName)` | 指定プレイヤーの`useOnlyKeyboard`を反転してIDを振り直し、シーンをダーティにする。 |
| `setNextCharacterToControl()` | 操作対象インデックスを次へ進め（末尾なら0へ戻す）、`setAsCurrentCharacterToControlByName`を呼ぶ。 |
| `setAsCurrentCharacterToControlByPlayerGameObject(GameObject playerGameObjectToSearch)` | 一致するプレイヤーが見つかれば、その名前で操作キャラを切り替える。 |
| `setAsCurrentCharacterToControlByPlayerTransform(Transform playerTransformToSearch)` | nullでなければTransformのGameObjectで操作キャラ切替を試みる。 |
| `getPauseManagerFromPlayerByIndex(int index)` | 範囲内ならそのプレイヤーの`menuPause`を、範囲外ならnullを返す。 |
| `setCharactersManagerPauseState(bool state)` | AI操作でないプレイヤーのみ、`menuPause`のポーズ状態を`state`に合わせる。 |
| `isCharacterInList(GameObject characterToSearch)` | 指定オブジェクトがプレイヤーリストに含まれるかを返す。 |
| `anyCharacterDead()` | いずれかのプレイヤーが死亡していればtrueを返す。 |
| `getMainPlayerController()` | 先頭プレイヤーの`playerController`を返し、居なければnullを返す。 |
| `getMainPlayerGameObject()` | 先頭プレイヤーのGameObjectを返し、居なければnullを返す。 |
| `getMainPlayerCamera()` | 先頭プレイヤーの`playerCamera`を返し、居なければnullを返す。 |
| `getMainPlayerCameraComponent()` | 先頭プレイヤーの`Camera`を返し、居なければnullを返す。 |
| `getMainPlayerCameraTransform()` | 先頭プレイヤーのカメラTransformを返し、居なければnullを返す。 |
| `getMainPlayerTransform()` | 先頭プレイヤーのTransformを返し、居なければnullを返す。 |
| `getMainPlayerPauseManager()` | 先頭プレイヤーの`menuPause`を返し、居なければnullを返す。 |
| `getPlayerList()` | 操作オブジェクトのみを詰めた新しい`List<GameObject>`を返し、空ならnullを返す。 |
| `getCameraStateListString()` | `cameraStatesList`の名前をstring配列に詰め直し、エディタ状態を更新する。 |
| `inputSetNextCharacterToControl()` | 開始時設定が有効で、一定時間経過し操作中でもなければ、次のキャラへの切替を実行する。 |
| `getPlayerListCount()` | `playerList`の要素数を返すだけ。 |
| `checkGameInfoToLoad(int lastSaveNumber, string currentSaveDataPath, string extraFileString)` | 各プレイヤーの`saveGameSystem`に同じ引数でセーブ情報の読み込み確認を流す。 |
| `deleteGameInfo(int saveNumberToDelete, string currentSaveDataPath, string extraFileString)` | 各プレイヤーの`saveGameSystem`にセーブデータ削除を流す。 |
| `showSaveInfoDebug(int saveNumberToShow, string currentSaveDataPath, string extraFileString)` | 各プレイヤーの`saveGameSystem`にセーブ情報のデバッグ表示を流す。 |
| `checkComponentsToInitialize()` | プレイヤー要素を確認した後、各プレイヤーの`saveGameSystem`の初期化チェックを呼ぶ。 |
| `checkSaveInfoListToLoadOnStartOnAllScenes()` | 各プレイヤーの`saveGameSystem`に、全シーン共通の開始時読み込みリスト確認を流す。 |
| `saveGameInfoFromEditor(int lastSaveNumber, string infoTypeName, string extraFileString)` | 各プレイヤーの`saveGameSystem`にエディタからのセーブ保存を流す。 |
| `saveGameWhenReturningHomeMenu()` | 各プレイヤーの`saveGameSystem`にホームメニュー帰還時の保存を流す。 |
| `checkIfPlayerIsLookingAtDeadTarget(Transform deadTarget, Transform placeToShoot)` | 各プレイヤーカメラの注視対象が死亡対象と一致するか調べ、一致すれば注視とロックオンを解除する。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static void checkPanelsActiveOnGamepadOrKeyboard(bool checkKeyboard, int playerID)` | – |

## 内部型

- `playerInfo`（class）
- `cameraStates`（class）
- `cameraInfo`（class）
