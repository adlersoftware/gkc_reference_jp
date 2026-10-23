# objectiveEventSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Objectives Mission System/objectiveEventSystem.cs:9`

**概要**: ミッション1件の目標状態を保持するコンポーネント。サブ目標の達成・解除、制限時間、完了や中断、報酬、HUD/マップ表示、ログ・セーブ連携を担う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Info Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Mission ID | `missionID` | `int` | – | ログやセーブでミッションを識別するID。 |
| Mission Scene | `missionScene` | `int` | – | ミッションが属するシーン番号。IDと組で識別に使う。 |

### Objective Info List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Objective Counter Instead Of List | `useObjectiveCounterInsteadOfList` | `bool` | – | オンにするとリストではなく回数カウンタで達成を数える。 |
| Objective Counter To Complete | `objectiveCounterToComplete` | `int` | – | カウンタ方式で達成に必要な回数。 / 表示条件: `useObjectiveCounterInsteadOfList` がオンのとき |

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Objective Name | `showObjectiveName` | `bool` | – | HUDに目標名のテキストを表示する。 |
| General Objective Name | `generalObjectiveName` | `string` | – | HUDやログに出すミッションの目標名。 |
| Show Objective Description | `showObjectiveDescription` | `bool` | – | HUDに目標の説明文を表示する。 |
| General Objective Description | `generalObjectiveDescription` | `string` | – | HUDやログに出す目標の説明文。 / TextArea (1, 10) |
| Objective Full Description | `objectiveFullDescription` | `string` | – | ログで表示する目標の詳細説明文。 / TextArea (1, 10) |
| Objective Location | `objectiveLocation` | `string` | "Land Fields" | ログに表示する目標の場所のテキスト。 / TextArea (1, 10) |
| Objective Rewards | `objectiveRewards` | `string` | – | ログに表示する報酬の説明テキスト。 / TextArea (2, 20) |

### UI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hide Objective Panels After X Time | `hideObjectivePanelsAfterXTime` | `bool` | – | 開始から一定時間後に目標パネルを自動で隠す。 |
| Time To Hide Objective Panel | `timeToHideObjectivePanel` | `float` | – | 目標パネルを隠すまでの待ち時間（秒）。 / 表示条件: `hideObjectivePanelsAfterXTime` がオンのとき |
| Show Amount Of Sub Objectives Complete | `showAmountOfSubObjectivesComplete` | `bool` | – | 説明文の末尾に達成数（現在/総数）を付ける。 |
| Disable Objective Panel On Mission Complete | `disableObjectivePanelOnMissionComplete` | `bool` | – | オンにすると完了時にログの目標枠を残さない。 |
| Show Mission Accepted Panel | `showMissionAcceptedPanel` | `bool` | – | ミッション受注時に受注パネルを表示する。 |
| Delay To Disable Mission Accepted Panel | `delayToDisableMissionAcceptedPanel` | `float` | – | 受注パネルを自動で消すまでの秒数。 / 表示条件: `showMissionAcceptedPanel` がオンのとき |
| Show Mission Complete Panel | `showMissionCompletePanel` | `bool` | – | ミッション完了時に完了パネルを表示する。 |
| Delay To Disable Mission Panel | `delayToDisableMissionPanel` | `float` | 3 | 完了パネルを自動で消すまでの秒数。 / 表示条件: `showMissionCompletePanel` がオンのとき |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Objectives Follows Order | `objectivesFollowsOrder` | `bool` | – | オンにするとサブ目標を順番どおりにしか達成できない。 |
| Search Player On Scene If Not Assigned | `searchPlayerOnSceneIfNotAssigned` | `bool` | true | プレイヤー未設定時にシーンから自動で探す。 |
| Add Mission To Log If Mission Starts And Not Being In Process | `addMissionToLogIfMissionStartsAndNotBeingInProcess` | `bool` | – | 未開始のまま目標達成されたらログに追加して開始する。 |
| Add Objective To Player Log System | `addObjectiveToPlayerLogSystem` | `bool` | true | 達成状況をプレイヤーの目標ログに登録する。 |
| Remove Mission Slot From Objective Log On Cancel Mission | `removeMissionSlotFromObjectiveLogOnCancelMission` | `bool` | – | キャンセル時にログからミッション枠を削除する。 |
| Cancel Mission If Player Dies Enabled | `cancelMissionIfPlayerDiesEnabled` | `bool` | – | プレイヤー死亡時に進行中ミッションをキャンセルする。 |
| Can Cancel Previous Mission To Start New One | `canCancelPreviousMissionToStartNewOne` | `bool` | – | 新しいミッション開始時に前のミッションをキャンセルする。 |
| Mission Can Be Cancelled Enabled | `missionCanBeCancelledEnabled` | `bool` | true | ミッションのキャンセル操作を許可する。 |
| Mission Can Be Replayed | `missionCanBeReplayed` | `bool` | – | 完了後にもう一度開始できるようにする。 |

### Save/Load Mission Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Save Game On Mission Complete | `saveGameOnMissionComplete` | `bool` | – | ミッション完了時にセーブを実行する。 |
| Save On Each Sub Objective Complete | `saveOnEachSubObjectiveComplete` | `bool` | – | サブ目標を達成するたびにセーブする。 |
| Update Subobjectives Complete On Load Game | `updateSubobjectivesCompleteOnLoadGame` | `bool` | true | ロード時にサブ目標の達成状況を反映する。 |
| Resume Mission On Load Game If Not Complete | `resumeMissionOnLoadGameIfNotComplete` | `bool` | – | 未完了ミッションをロード時に自動で再開する。 |
| Reset Subobjectives If Cancelling Mission | `resetSubobjectivesIfCancellingMission` | `bool` | true | キャンセル時にサブ目標の達成状況をリセットする。 |

### Time Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Time Limit | `useTimeLimit` | `bool` | – | 制限時間を有効にし、HUDにタイマーを出す。 |
| Timer Speed | `timerSpeed` | `float` | – | タイマーの減り速度の倍率。大きいほど速く減る。 / 表示条件: `useTimeLimit` がオンのとき |
| Minutes To Complete | `minutesToComplete` | `float` | – | 制限時間の分。秒と合算して初期値になる。 / 表示条件: `useTimeLimit` がオンのとき / Range (0, 60) |
| Seconds To Complete | `secondsToComplete` | `float` | – | 制限時間の秒。分と合算して初期値になる。 / 表示条件: `useTimeLimit` がオンのとき / Range (0, 60) |
| Second Sound Timer Lower Than | `secondSoundTimerLowerThan` | `float` | – | 残りこの秒数以下で毎秒の警告音を鳴らす。 / 表示条件: `useTimeLimit` がオンのとき |
| Second Timer Sound | `secondTimerSound` | `AudioClip` | – | 残り時間が少ない時に鳴らす警告音のクリップ。 / 表示条件: `useTimeLimit` がオンのとき |
| Second Timer Audio Element | `secondTimerAudioElement` | `AudioElement` | – | 警告音を再生するための`AudioElement`設定。 / 表示条件: `useTimeLimit` がオンのとき |
| Time To Hide Objective Panel | `timeToHideObjectivePanel` | `float` | – | 目標パネルを隠すまでの待ち時間（秒）。 / 表示条件: `useTimeLimit` がオンのとき |

### Objective Complete Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event When Objective Complete | `eventWhenObjectiveComplete` | `UnityEvent` | – | 目標達成時に実行するイベント。 |
| Event When Objective Complete Send Player | `eventWhenObjectiveCompleteSendPlayer` | `eventParameters.eventToCallWithGameObject` | – | 達成時にプレイヤーを引数に渡して呼ぶイベント。 |

### Objective Not Complete Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Call Event When Objective Not Complete | `callEventWhenObjectiveNotComplete` | `bool` | – | 未達成やキャンセル時に失敗イベントを呼ぶ。 |
| Event When Objective Not Complete | `eventWhenObjectiveNotComplete` | `UnityEvent` | – | 未達成やキャンセル時に実行するイベント。 / 表示条件: `callEventWhenObjectiveNotComplete` がオンのとき |

### Objective Start Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Objective Start | `useEventOnObjectiveStart` | `bool` | – | ミッション開始時にイベントを呼ぶ。 |
| Event On Objective Start | `eventOnObjectiveStart` | `UnityEvent` | – | ミッション開始時に実行するイベント。 / 表示条件: `useEventOnObjectiveStart` がオンのとき |

### Reward Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event Objective Complete Reward | `useEventObjectiveCompleteReward` | `bool` | – | 達成報酬イベントを有効にする。 |
| Give Reward On Objective Complete | `giveRewardOnObjectiveComplete` | `bool` | – | 達成時に報酬付与処理を実行する。 / 表示条件: `useEventObjectiveCompleteReward` がオンのとき |
| Event Objective Complete Reward | `eventObjectiveCompleteReward` | `eventParameters.eventToCallWithGameObject` | – | 報酬付与時にプレイヤーを渡して呼ぶイベント。 / 表示条件: `useEventObjectiveCompleteReward` がオンのとき |

### Load Game & Objective Complete Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event When Loading Game And Objective Complete | `useEventWhenLoadingGameAndObjectiveComplete` | `bool` | – | ロード時に完了済みならイベントを呼ぶ。 |
| Event When Loading Game And Objective Complete | `eventWhenLoadingGameAndObjectiveComplete` | `UnityEvent` | – | ロード時、完了済みミッションで実行するイベント。 / 表示条件: `useEventWhenLoadingGameAndObjectiveComplete` がオンのとき |

### Mission Level Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Min Player Level | `useMinPlayerLevel` | `bool` | – | 受注にプレイヤーレベルの条件を設ける。 |
| Min Player Level | `minPlayerLevel` | `int` | – | 受注に必要なプレイヤーの最低レベル。 / 表示条件: `useMinPlayerLevel` がオンのとき |
| Event On Not Enough Level | `eventOnNotEnoughLevel` | `UnityEvent` | – | レベル不足で受注できない時に実行するイベント。 / 表示条件: `useMinPlayerLevel` がオンのとき |

### Map Object Information Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Enable All Map Object Information At Once | `enableAllMapObjectInformationAtOnce` | `bool` | – | 開始時に全サブ目標のマップアイコンを出す。 |
| Enable All Map Object Information On Time | `enableAllMapObjectInformationOnTime` | `bool` | – | 一定時間後に全マップアイコンをまとめて出す。 |
| Time To Enable All Map Object Information | `timeToEnableAllMapObjectInformation` | `float` | – | 全マップアイコンを出すまでの待ち時間（秒）。 / 表示条件: `enableAllMapObjectInformationOnTime` がオンのとき |
| Use Extra List Map Object Information | `useExtraListMapObjectInformation` | `bool` | – | 追加のマップ情報リストもアイコン生成の対象にする。 |

### Sounds Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Sound On Objective Complete | `useSoundOnSubObjectiveComplete` | `bool` | – | サブ目標達成時に効果音を鳴らす。 |
| Sound On Objective Complete | `soundOnSubObjectiveComplete` | `AudioClip` | – | サブ目標達成時に鳴らす効果音クリップ。 / 表示条件: `useSoundOnSubObjectiveComplete` がオンのとき |
| Sound On Objective Complete | `subObjectiveCompleteAudioElement` | `AudioElement` | – | 達成音を再生するための`AudioElement`設定。 / 表示条件: `useSoundOnSubObjectiveComplete` がオンのとき |
| Use Sound On Objective Not Complete | `useSoundOnObjectiveNotComplete` | `bool` | – | 未達成やキャンセル時に音を鳴らす。 |
| Sound On Objective Not Complete | `soundOnObjectiveNotComplete` | `AudioClip` | – | 未達成時に鳴らす効果音クリップ。 / 表示条件: `useSoundOnObjectiveNotComplete` がオンのとき |
| Objective Not Complete Audio Element | `objectiveNotCompleteAudioElement` | `AudioElement` | – | 未達成音を再生する`AudioElement`設定。 / 表示条件: `useSoundOnObjectiveNotComplete` がオンのとき |

### Mission Text Info Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Timer Panel Name | `timerPanelName` | `string` | "Timer" | タイマーHUDを探す時のパネル名。 |
| Timer Text Panel Name | `timerTextPanelName` | `string` | "Timer Text" | タイマー表示テキストを探す時の名前。 |
| Objective Info Main Panel Name | `objectiveInfoMainPanelName` | `string` | "Objective Info" | 目標情報の親パネルを探す時の名前。 |
| Objective Text Info Panel Name | `objectiveTextInfoPanelName` | `string` | "Objective Name Text" | 目標名テキストを探す時の名前。 |
| Objective Description Text Name | `objectiveDescriptionTextName` | `string` | "Objective Description Text" | 目標説明テキストを探す時の名前。 |
| Objective Info Panel Name | `objectiveInfoPanelName` | `string` | "Objective Info Panel" | 目標情報パネル本体を探す時の名前。 |

### Other Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Remote Event System | `mainRemoteEventSystem` | `remoteEventSystem` | – | サブ目標達成時にリモートイベントを送るための参照。 |

### Player Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Current Player Manually | `setCurrentPlayerManually` | `bool` | – | オンにするとプレイヤーを手動で指定する。 |
| Current Player To Configure | `currentPlayerToConfigure` | `GameObject` | – | 手動指定時に使うプレイヤーのゲームオブジェクト。 / 表示条件: `setCurrentPlayerManually` がオンのとき |

### Current State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Number Of Objectives | `numberOfObjectives` | `int` | – | 有効な目標の総数。開始時に自動計算される。 |
| Current Sub Objective Index | `currentSubObjectiveIndex` | `int` | – | 現在のサブ目標の進行位置（達成済み数）。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `missionAccepted` | `bool` | – | – |
| `rewardsObtained` | `bool` | – | – |
| `objectiveInProcess` | `bool` | – | – |
| `objectiveComplete` | `bool` | – | – |
| `objectiveInfoList` | `List<objectiveInfo>` | new List<objectiveInfo> () | – |
| `extraListMapObjectInformation` | `List<mapObjectInformation>` | new List<mapObjectInformation> () | – |
| `showDebugPrint` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `initializeNumberOfObjectives()` | `numberOfObjectives`を0に戻し、カウンタ方式なら`objectiveCounterToComplete`、リスト方式なら有効な要素数で再設定する。 |
| `convertSeconds()` | `totalSecondsTimer`を分と秒に分け、`MM:SS`形式の文字列にして返すだけ。 |
| `increaseObjectiveCounter()` | カウンタ方式の時のみ達成数を進め、規定数に達すれば`setObjectiveComplete`、未達なら時間加算・セーブ・UI更新を行う。 |
| `addSubObjectiveComplete(string subObjectiveName)` | `Name`一致のサブ目標を達成済みにしてログへ通知し、順序違反なら中断、全達成なら完了、未達なら次目標の表示を更新する。 |
| `decreaseObjectiveCounter()` | 実行中かつ先頭`objectiveInfo`が達成済みの時だけ達成を解除し、ログ更新と未完了イベントの後に`currentSubObjectiveIndex`を減らす。 |
| `removeSubObjectiveComplete(string subObjectiveName)` | 実行中に`Name`一致の達成済みサブ目標を未達成へ戻し、順序違反なら中断、そうでなければ未完了イベントを呼び出して添字を減らす。 |
| `findPlayerOnScene()` | `searchPlayerOnSceneIfNotAssigned`が有効なら、シーン上のメインプレイヤーを`setCurrentPlayer`に渡す。 |
| `setCurrentPlayer(GameObject newPlayer)` | `currentPlayer`を設定し、`playerComponentsManager`から目標ログ・HUD・経験値システムを取得して割り当て完了フラグを立てる。 |
| `startObjective()` | 前提を確認して`objectiveInProcess`を立て、開始イベント・ログ登録・受注パネル・HUDとマップ情報の更新をまとめて行う。 |
| `updateUIElements()` | 実行中なら保持中の目標名と説明を言語設定に応じて翻訳し、HUDテキストとサブ目標数表示を更新する。 |
| `setMissionInfoOnHUd()` | 制限時間を初期化しHUD要素を検索したうえで、現在のサブ目標か全体の名前・説明を表示フラグに従って反映する。 |
| `checkShowAmountOfSubObjectivesComplete(string newTextContent)` | `showAmountOfSubObjectivesComplete`が有効なら説明文に`(現在/総数)`を付けて目標説明テキストへ設定する。 |
| `setMissionInfoOnMap()` | 各`objectiveInfo`と追加リストの`mapObjectInformation`にマップアイコンを生成し、一括有効でなければ最初の1件だけ表示する。 |
| `addObjectiveToPlayerLogMenu()` | ログシステムへ全体目標名・説明・場所・報酬を渡して`addObjective`を呼び、目標一覧に登録する。 |
| `resetAllSubObjectives()` | 全`objectiveInfo`の`subObjectiveComplete`を偽にし、ログ側のサブ目標達成状態も偽に更新する。 |
| `setSubObjectiveCompleteListState(List<bool> subObjectiveCompleteList)` | 受け取った達成状態リストを各`objectiveInfo`へ反映し、真の数で`currentSubObjectiveIndex`を数え直す。 |
| `cancelPreviousObjective()` | `cancellingMisionActive`を立ててから`stopObjective`を呼び、キャンセル中は未完了サウンドを鳴らさないようにする。 |
| `cancelCurrentMissionRemotely()` | `isObjectiveInProcess`が真の場合のみ`stopObjective`を呼び、遠隔からミッションを中断させる。 |
| `stopObjective()` | `objectiveInProcess`を下ろしてHUDとマップ表示を消し、サブ目標のリセット、ログの`cancelObjective`、未完了イベントを行う。 |
| `setObjectiveComplete()` | 完了状態にしてHUDを消し、完了イベント・報酬・完了パネル・セーブを実行してログへ`objectiveComplete`を通知する。 |
| `setObjectiveAsCompleteOnLoad(bool rewardsObtainedValue)` | ロード時に完了状態を復元し、`rewardsObtainedValue`で報酬取得状態とログを更新、ロード用完了イベントを呼ぶ。 |
| `giveRewardToPlayer()` | 未取得なら`eventObjectiveCompleteReward`をプレイヤー付きで呼び、取得済みフラグとログの報酬状態を真にする。 |
| `isRewardsObtained()` | `rewardsObtained`の値を返すだけ。 |
| `setRewardsObtanedState(bool state)` | `rewardsObtained`を指定値に設定するだけ。 |
| `isMissionAccepted()` | `missionAccepted`の値を返すだけ。 |
| `isObjectiveInProcess()` | `objectiveInProcess`の値を返すだけ。 |
| `setMissionAcceptedState(bool state)` | `missionAccepted`を指定値に設定するだけ。 |
| `checkInCallEventWhenObjectiveNotComplete()` | `callEventWhenObjectiveNotComplete`が有効な時のみ`eventWhenObjectiveNotComplete`を呼び出す。 |
| `disableHUDElements()` | タイマー・目標名・説明・情報パネルの各HUD要素を、存在すれば非アクティブにする。 |
| `playAudioSourceShoot(AudioElement clip)` | `mainAudioSource`をクリップに割り当ててから、`AudioPlayer.PlayOneShot`で1回再生する。 |
| `disableObjectivePanelsAfterXTime()` | 既存のコルーチンを停止し、`timeToHideObjectivePanel`秒後にパネルを隠すコルーチンを開始する。 |
| `stopDisableObjectivePanelCoroutine()` | `disableObjectivePanelCoroutine`が存在すれば停止するだけ。 |
| `addSubObjectiveCompleteFromEditor(string subObjectiveName)` | `addSubObjectiveComplete`をそのまま呼び出すだけ。 |
| `setObjectiveCompleteFromEditor()` | 実行中の場合のみ`setObjectiveComplete`を呼び出す。 |
| `isObjectiveComplete()` | `objectiveComplete`の値を返すだけ。 |
| `getMissionCanBeReplayed()` | `missionCanBeReplayed`の値を返すだけ。 |
| `isMissionCanBeCancelledEnabled()` | `missionCanBeCancelledEnabled`の値を返すだけ。 |
| `isCancelMissionIfPlayerDiesEnabled()` | `cancelMissionIfPlayerDiesEnabled`の値を返すだけ。 |
| `isRemoveMissionSlotFromObjectiveLogOnCancelMissionEnabled()` | `removeMissionSlotFromObjectiveLogOnCancelMission`の値を返すだけ。 |
| `checkRemoteEventsOnSubObjectiveComplete(List<string> removeEventNameList)` | `mainRemoteEventSystem`がある時、リストの各イベント名を`callRemoteEvent`で順に実行する。 |
| `assignIDToMission(int newID)` | `missionID`を新しい値に設定し、`updateComponent`でシーンを更新する。 |
| `assignMissionScene(int newMissionScene)` | `missionScene`を新しい値に設定し、`updateComponent`でシーンを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`を呼び、エディタ上の変更をシーンへ反映する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnNotEnoughLevel` | `UnityEvent` | – |
| `eventWhenObjectiveComplete` | `UnityEvent` | – |
| `eventWhenObjectiveNotComplete` | `UnityEvent` | – |
| `eventOnObjectiveStart` | `UnityEvent` | – |
| `eventWhenLoadingGameAndObjectiveComplete` | `UnityEvent` | – |

## 内部型

- `objectiveInfo`（class）
