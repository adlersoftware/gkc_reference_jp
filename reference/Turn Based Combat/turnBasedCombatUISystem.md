# turnBasedCombatUISystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `ingameMenuPanel`
- **ソース**: `Turn Based Combat/turnBasedCombatUISystem.cs:7`

**概要**: ターン制戦闘のUIと進行を管理するコンポーネント。コマンド選択、ターゲット選択、チーム情報の構築、ターン送り、戦闘開始・終了やインベントリ使用のUI処理を担う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Min Wait Time To Start Combat | `minWaitTimeToStartCombat` | `float` | 2.5f | – |
| Layer To Check Character Target On Press | `layerToCheckCharacterTargetOnPress` | `LayerMask` | – | – |
| Lose Combat If Player Dies Enabled | `loseCombatIfPlayerDiesEnabled` | `bool` | – | – |
| Pause Rest Of AI On Scene During Combat | `pauseRestOfAIOnSceneDuringCombat` | `bool` | – | – |
| Select First Turn Randomly If No Turn For Enemy | `selectFirstTurnRandomlyIfNoTurnForEnemy` | `bool` | – | – |

### Combat Result Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Run From Combat Enabled | `runFromCombatEnabled` | `bool` | true | – |
| Respawn Enemy Team On Original Position On Combat Run | `respawnEnemyTeamOnOriginalPositionOnCombatRun` | `bool` | – | – |
| Resurrect Enemy Team On Combat Run | `resurrectEnemyTeamOnCombatRun` | `bool` | – | – |
| Respawn Enemy Team On Original Position On Combat Lost | `respawnEnemyTeamOnOriginalPositionOnCombatLost` | `bool` | – | – |
| Heal Enemy Team If Run Away | `healEnemyTeamIfRunAway` | `bool` | – | – |
| Holster Weapons After Combat | `holsterWeaponsAfterCombat` | `bool` | – | – |
| Holster Weapons On Player After Combat | `holsterWeaponsOnPlayerAfterCombat` | `bool` | – | – |
| Use Respawn Positions On Combat Run | `useRespawnPositionsOnCombatRun` | `bool` | – | – |
| Max Radius To Respawn | `maxRadiusToRespawn` | `float` | 3 | – |

### Turn Combat Command Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Command Category Info List | `commandCategoryInfoList` | `List<commandCategoryInfo>` | new List<commandCategoryInfo> () | – |

### UI Panel Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Panel Category Info List | `panelCategoryInfoList` | `List<panelCategoryInfo>` | new List<panelCategoryInfo> () | – |

### Input Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Turn Based Combat Input Name | `mainTurnBasedCombatInputName` | `string` | "Turn Based Combat System" | – |
| Custom Input To Pause On Action Info List | `customInputToPauseOnActionInfoList` | `List<playerActionSystem.inputToPauseOnActionIfo>` | new List<playerActionSystem.inputToPa… | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Stat Name Letters Info List | `statNameLettersInfoList` | `List<turnBasedCombatChararcterUIInfoObject.statNameLettersInfo>` | new List<turnBasedCombatChararcterUII… | – |
| Toggle Turn And Free Combat Input Enabled | `toggleTurnAndFreeCombatInputEnabled` | `bool` | true | – |
| Min Distance To Resume Turn Combat | `minDistanceToResumeTurnCombat` | `float` | 30 | – |
| Min Wait To Show Exit Combat After Result | `minWaitToShowExitCombatAfterResult` | `float` | 2 | – |
| Reset Character Positions Smoothly | `resetCharacterPositionsSmoothly` | `bool` | true | – |
| Reset Character Positions Smoothly On Combat Start | `resetCharacterPositionsSmoothlyOnCombatStart` | `bool` | true | – |
| Horizontal Limit On Right Screen Category Panel | `horizontalLimitOnRightScreenCategoryPanel` | `float` | 400 | – |
| Horizontal Limit On Right Screen Confirmation Panel | `horizontalLimitOnRightScreenConfirmationPanel` | `float` | 400 | – |

### Inventory Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Next Turn On Inventory Item Used | `setNextTurnOnInventoryItemUsed` | `bool` | – | – |
| Use Inventory Item Message Content | `useInventoryItemMessageContent` | `string` | "-ITEM- used" | – |
| Item Name Field | `itemNameField` | `string` | "-ITEM-" | – |
| Use Inventory Item Command Duration | `useInventoryItemCommandDuration` | `float` | 3 | – |
| Unable To Use Object Message Content | `unableToUseObjectMessageContent` | `string` | "-ITEM- can't be used right now" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Show Stats Debug Print | `showStatsDebugPrint` | `bool` | – | – |
| Combat Active | `combatActive` | `bool` | – | – |
| Main Turn Based Combat System Assigned | `mainTurnBasedCombatSystemAssigned` | `bool` | – | – |
| Menu Opened | `menuOpened` | `bool` | – | – |
| Current Turn For Player Team | `currentTurnForPlayerTeam` | `bool` | – | – |
| Player Team Position Data Name | `playerTeamPositionDataName` | `string` | – | – |
| Enemy Team Position Data Name | `enemyTeamPositionDataName` | `string` | – | – |
| Current Turn Character Index | `currentTurnCharacterIndex` | `int` | – | – |
| Use Custom Camera State | `useCustomCameraState` | `bool` | – | – |
| Custom Camera State | `customCameraState` | `string` | – | – |
| Delay To Activate Command Active | `delayToActivateCommandActive` | `bool` | – | – |
| Playing Command Active | `playingCommandActive` | `bool` | – | – |
| Turn Combat Active | `turnCombatActive` | `bool` | true | – |
| Free Combat Active | `freeCombatActive` | `bool` | – | – |
| Selecting Target For Command Active | `selectingTargetForCommandActive` | `bool` | – | – |
| Show Panel Object On Right Or Left Side Screen | `showPanelObjectOnRightOrLeftSideScreen` | `bool` | – | – |
| Show Confirmation Panel Object On Right Or Left Side Screen | `showConfirmationPanelObjectOnRightOrLeftSideScreen` | `bool` | – | – |
| Current Amount Of Extra Turns | `currentAmountOfExtraTurns` | `int` | -1 | – |

### Combat Result Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| All Player Team Dead | `allPlayerTeamDead` | `bool` | – | – |
| All Enemy Team Dead | `allEnemyTeamDead` | `bool` | – | – |
| Combat Finished | `combatFinished` | `bool` | – | – |
| Combat Winned | `combatWinned` | `bool` | – | – |

### Characters Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Team Character List | `playerTeamCharacterList` | `List<characterInfo>` | new List<characterInfo> () | – |
| Enemy Team Character List | `enemyTeamCharacterList` | `List<characterInfo>` | new List<characterInfo> () | – |
| Turn Based Combat Chararcter UI Info List | `turnBasedCombatChararcterUIInfoList` | `List<turnBasedCombatChararcterUIInfoObject.turnBasedCombatChararcterUIInfo>` | new List<turnBasedCombatChararcterUII… | – |
| Current Character Info | `currentCharacterInfo` | `characterInfo` | – | – |
| Full Character On Combat List | `fullCharacterOnCombatList` | `List<GameObject>` | new List<GameObject> () | – |
| Number Of Characters On Player Team | `numberOfCharactersOnPlayerTeam` | `int` | – | – |
| Number Of Characters On Enemy Team | `numberOfCharactersOnEnemyTeam` | `int` | – | – |

### Inventory Items Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Inventory Object Name Selected | `currentInventoryObjectNameSelected` | `string` | – | – |
| Inventory Item Selected | `inventoryItemSelected` | `bool` | – | – |
| Simple UI Button Info Inventory Button List | `simpleUIButtonInfoInventoryButtonList` | `List<simpleUIButtonInfo>` | new List<simpleUIButtonInfo> () | – |

### Teams Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Turn Based Combat Team Info | `playerTurnBasedCombatTeamInfo` | `turnBasedCombatTeamInfo` | – | – |
| Enemy Turn Based Combat Team Info | `enemyTurnBasedCombatTeamInfo` | `turnBasedCombatTeamInfo` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Turn Based Combat System | `mainTurnBasedCombatSystem` | `turnBasedCombatSystem` | – | – |
| Main Friend List Manager | `mainFriendListManager` | `friendListManager` | – | – |
| Main Player | `mainPlayer` | `GameObject` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Using Devices System | `mainUsingDevicesSystem` | `usingDevicesSystem` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Main Player Input Manager | `mainPlayerInputManager` | `playerInputManager` | – | – |
| Main Inventory Manager | `mainInventoryManager` | `inventoryManager` | – | – |
| Main Player Components Manager | `mainPlayerComponentsManager` | `playerComponentsManager` | – | – |
| Main Canvas Scaler | `mainCanvasScaler` | `CanvasScaler` | – | – |

### UI Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Action Buttons Panel | `mainActionButtonsPanel` | `RectTransform` | – | – |
| Player Team Stats UI Prefab | `playerTeamStatsUIPrefab` | `GameObject` | – | – |
| Enemy Team Stats UI Prefab | `enemyTeamStatsUIPrefab` | `GameObject` | – | – |
| Player Team Health Slider Parent | `playerTeamHealthSliderParent` | `RectTransform` | – | – |
| Eney Team Health Slider Parent | `eneyTeamHealthSliderParent` | `RectTransform` | – | – |
| Current Character Icon | `currentCharacterIcon` | `RectTransform` | – | – |
| Current Character Target Icon | `currentCharacterTargetIcon` | `RectTransform` | – | – |
| Command Description Game Object | `commandDescriptionGameObject` | `GameObject` | – | – |
| Command Description Text | `commandDescriptionText` | `Text` | – | – |
| Exit Combat After Result Panel | `exitCombatAfterResultPanel` | `GameObject` | – | – |
| Toggle Combat Mode Touch Button | `toggleCombatModeTouchButton` | `GameObject` | – | – |
| Input Actions Panel | `inputActionsPanel` | `GameObject` | – | – |

### UI Inventory Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory Items Panel Parent | `inventoryItemsPanelParent` | `Transform` | – | – |
| Inventory Item Button Prefab | `inventoryItemButtonPrefab` | `GameObject` | – | – |
| Confirm Use Inventory Item Panel | `confirmUseInventoryItemPanel` | `GameObject` | – | – |
| Check Right Or Left Side For Confirm Use Inventory Item Panel | `checkRightOrLeftSideForConfirmUseInventoryItemPanel` | `bool` | – | – |
| Right Side Confirm Use Inventory Item Panel | `rightSideConfirmUseInventoryItemPanel` | `RectTransform` | – | – |
| Left Side Confirm Use Inventory Item Panel | `leftSideConfirmUseInventoryItemPanel` | `RectTransform` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Combat Winned | `eventOnCombatWinned` | `UnityEvent` | – | – |
| Event On Combat Lost | `eventOnCombatLost` | `UnityEvent` | – | – |
| Event On Run From Combat | `eventOnRunFromCombat` | `UnityEvent` | – | – |
| Use Event On Command Used | `useEventOnCommandUsed` | `bool` | – | – |
| Event On Command Used | `eventOnCommandUsed` | `eventParameters.eventToCallWithString` | – | – |
| Use Event On Not Enough Stat On Commnad | `useEventOnNotEnoughStatOnCommnad` | `bool` | – | – |
| Event On Not Enough Stat On Commnad | `eventOnNotEnoughStatOnCommnad` | `eventParameters.eventToCallWithString` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopMenuCoroutineUpdate()` | `menuCoroutine`が実行中なら停止するだけ。 |
| `setCurrentCommandNameUsed(string commandName)` | コマンド使用イベントが有効なら、`commandName`を付けてイベントを発火するだけ。 |
| `confirmCurrentCommand()` | 選択中コマンドを確定し、対象への注視設定とUI非表示の後、遅延の有無に応じてコマンド実行を開始する。 |
| `cancelCurrentCommand()` | ターゲット選択状態を解除し、対象アイコンと確認パネルを非表示にする。 |
| `confirmPassTurn()` | 位置リセットを有効にした状態で`setNextTurn`を呼び、ターンを進める。 |
| `setEnemyTeamTurnDirectly()` | 敵チームのターンへ強制切替するフラグを立てて`setNextTurn`を呼ぶ。 |
| `setNextTurn()` | 必要に応じ両チームの位置をリセットし、パネルを閉じてコマンド状態を解除した後、全キャラクターのステータスUIを更新する。 |
| `stopCommandCoroutine()` | `commandCoroutine`を停止し、コマンド実行中フラグを下ろすだけ。 |
| `runFromCurrentCombat()` | 戦闘中なら敵の蘇生や位置・ターゲットのリセット、武器収納、プレイヤーのリスポーンを行い、メニューを閉じて逃走イベントを発火する。 |
| `finishCurrentCombat()` | 戦闘中ならメニューパネルを閉じるだけ。 |
| `enableOrDisabeExitCombatAfterResultPanel(bool state)` | リザルト後の戦闘終了パネルの表示状態を`state`に合わせるだけ。 |
| `exitFromCombatAfterWinningOrLoosing()` | 敗北・勝利に応じてチームの敗北・報酬イベントとキャラクターの蘇生・リスポーンを行い、戦闘を終えてフリー戦闘を解除する。 |
| `checkMainPlayerStateBeforeActivateCombat()` | プレイヤーが運転中なら降車させ、一人称・全身表示中なら三人称視点へ切り替えて戦闘開始に備える。 |
| `isCombatActive()` | `combatActive`の値を返すだけ。 |
| `setCharacterTeamsInfo()` | メニュー表示中に両チームの情報を再構築し、死亡者を除いて各キャラクターのUI情報を作成し、初期ターンを設定する。 |
| `openPanelInfo(GameObject buttonObject)` | 全パネルを閉じたうえで押されたボタンのパネルを開き、確認パネルがあれば画面端の判定で左右の表示位置を調整する。 |
| `confirmCurrentCategoryCommnand()` | `currentPanelInfo`のパネルを表示し、画面端の判定で左右の位置に配置したうえで選択イベントを発火する。 |
| `cancelCurrentCategoryCommnand()` | `currentPanelInfo`の確認パネルを非表示にするだけ。 |
| `closeAllPanelInfo()` | 全パネルのパネルオブジェクトと確認パネルを非表示にし、インベントリ使用確認パネルも閉じる。 |
| `showCurrentCommandDescription(GameObject buttonObject)` | 対象コマンドを探し、ホバー表示が有効なら説明テキストを表示し、無効なら説明を閉じる。 |
| `disableCurrentCommandDescription()` | コマンド説明用オブジェクトを非表示にするだけ。 |
| `checkButtonPressed(GameObject buttonObject)` | コマンド実行中や遅延中でなければ、押されたボタンのコマンド判定`checkButton`を呼ぶ。 |
| `addNewTurnBasedCombatChararcterUIInfo(GameObject characterUIOwner, GameObject sliderPrefab, string ownerName, int objectID, Transform healtSlidersParent, characterInfo newCharacterInfo)` | キャラクターのステータスUIを生成または再利用し、名前・所有者・IDを設定して表示対象ステータスのスライダーを初期化する。 |
| `updateAllCharacterStatsUIValue()` | 両チームの全キャラクターについて`updateCharacterStatsUIValue`を呼ぶ。 |
| `updateCharacterStatsUIValue(GameObject characterUIOwner, playerStatsSystem mainPlayerStatsSystem)` | UI所有者が一致するキャラクターの割り当て済みステータスについて、最大値・現在値・数値テキストを更新する。 |
| `allCharactersPositionAdjusted()` | 生存している全キャラクターの位置調整が完了していればtrueを返す。 |
| `getFirstCharacterAliveOfEnemyTeam()` | 敵チームで最初に見つかった生存キャラクターの情報を返し、いなければnullを返す。 |
| `getFirstCharacterAliveOfPlayerTeam()` | プレイヤーチームで最初に見つかった生存キャラクターの情報を返し、いなければnullを返す。 |
| `checkTeamsDeadStateAfterCharacterDeath(Transform characterTransform)` | どちらかのチームが全滅していれば`setNextTurn`を呼ぶ。引数`characterTransform`は使用しない。 |
| `checkPlayerStateOnDeathDuringCombat()` | 本体は実質空で、プレイヤー死亡時の処理はコメントアウトされている。 |
| `checkCharacterStateAfterResurrect(Transform characterTransform)` | 戦闘中なら復活したキャラクターをチーム状態へ戻し、次ターンでの両チーム位置調整を有効にする。 |
| `isAllEnemyTeamDead()` | 敵チームの全キャラクターが死亡していればtrueを返す。 |
| `isAllPlayerTeamDead()` | プレイヤーチームの全キャラクターが死亡していればtrueを返す。 |
| `getEnemyTeamAliveAmount()` | 敵チームの生存キャラクター数を数えて返す。 |
| `getPlayerTeamAliveAmount()` | プレイヤーチームの生存キャラクター数を数えて返す。 |
| `checkInputListToPauseDuringAction(List<playerActionSystem.inputToPauseOnActionIfo> inputList, bool state)` | 入力リストの各マルチアクシスを、`state`がtrueなら現在状態を保存して停止し、falseなら保存した状態へ戻す。 |
| `selectInventoryItem(GameObject inventoryButton)` | 対応するインベントリボタンを検索し、見つかればアイテム名を選択状態に保存して使用確認パネルを表示する。 |
| `showInventoryItemListPanel()` | 既存のアイテムボタンを非表示にし、使用可能で個数が1以上のインベントリアイテムを一覧に追加して表示する。 |
| `updateInventoryItemListPanel()` | `showInventoryItemListPanel`を呼び直すだけ。 |
| `confirmToUseInventoryItem()` | 選択中アイテムを使用し、成功時は一覧とUIを更新して必要なら次ターンへ進め、失敗時は使用不可メッセージを表示する。 |
| `cancelUseInventoryItem()` | アイテム選択状態を解除し、使用確認パネルを閉じるだけ。 |
| `inputSelectNextOrPreviousCharacterTarget(bool state)` | メニュー表示中のみ、`state`に応じて次または前のターゲットへ切り替える。 |
| `inputConfirmCommandOnCurrentCharacterTarget()` | メニュー表示中でターゲット選択中かつ対象がいれば、`confirmCurrentCommand`を呼ぶ。 |
| `inputConfirmCommand()` | メニュー表示中かつプレイヤーチームのターンなら`confirmCurrentCommand`を呼ぶ。 |
| `inputCancelCommand()` | メニュー表示中かつプレイヤーチームのターンなら`cancelCurrentCommand`を呼ぶ。 |
| `inputSelectNextTarget()` | メニュー表示中かつプレイヤーチームのターンなら、次のターゲットを選択する。 |
| `inputSelectPreviousTarget()` | メニュー表示中かつプレイヤーチームのターンなら、前のターゲットを選択する。 |
| `setFreeCombatActiveStateOnAllCharacters(bool state)` | 両チームの全キャラクターのアクションシステムにフリー戦闘状態を設定するだけ。 |
| `inputToggleCombatMode()` | メニュー表示中ならフリー戦闘へ、非表示のフリー戦闘中なら操作可能な状態でのターン制戦闘へ切り替える。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCombatWinned` | `UnityEvent` | – |
| `eventOnCombatLost` | `UnityEvent` | – |
| `eventOnRunFromCombat` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`initializeMenuPanel()`, `openOrCloseMenuPanel(bool state)`

</details>

## 内部型

- `panelCategoryInfo`（class）
- `panelInfo`（class）
- `commandCategoryInfo`（class）
- `commandInfo`（class）
- `characterInfo`（class）
