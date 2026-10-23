# objectiveStationUISystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Objectives Mission System/objectiveStationUISystem.cs:8`

**概要**: ステーションとキャラクターの目標パネルを管理するUI。ミッション一覧の生成・選択・受注・報酬取得と、完了/受注メッセージの表示を担う。

**公式ドキュメント抜粋**（[Objective Station UI System](../../docs/character-level-components/character/objective-station-ui-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Objective Station UI Enabled | `objectiveStationUIEnabled` | `bool` | true | – |
| Menu Opened | `menuOpened` | `bool` | – | – |
| Button Usable | `buttonUsable` | `Color` | – | – |
| Button Not Usable | `buttonNotUsable` | `Color` | – | – |
| Only Active New Mission If No Previous In Process | `onlyActiveNewMissionIfNoPreviousInProcess` | `bool` | – | – |
| Only Add New Missions To Player Log Menu Without Activate Them | `onlyAddNewMissionsToPlayerLogMenuWithoutActivateThem` | `bool` | – | – |
| Use Blur UI Panel | `useBlurUIPanel` | `bool` | – | – |

### Mission Panel Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dissable Objective Accepted Panel Delay | `dissableObjectiveAcceptedPanelDelay` | `float` | – | – |
| Delay To Dissable Character Panel After Accept Mission | `delayToDissableCharacterPanelAfterAcceptMission` | `float` | – | – |
| No Missions Available Text | `noMissionsAvailableText` | `string` | "NO MISSIONS AVAILABLE" | – |
| Disable Mission Complete Panel After Time | `disableMissionCompletePanelAfterTime` | `bool` | – | – |
| Delay To Disable Mission Panel | `delayToDisableMissionPanel` | `float` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Missions With Higher Level | `showMissionsWithHigherLevel` | `bool` | true | – |
| Event On Mission With Higher Level | `eventOnMissionWithHigherLevel` | `UnityEvent` | – | – |
| Event On Mission Accepted | `eventOnMissionAccepted` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Objective Info List | `currentObjectiveInfoList` | `List<objectiveStationSystem.objectiveInfo>` | new List<objectiveStationSystem.objec… | – |
| Objective Slot Info List | `objectiveSlotInfoList` | `List<objectiveLogSystem.objectiveSlotInfo>` | new List<objectiveLogSystem.objective… | – |
| Current Objective Station System | `currentObjectiveStationSystem` | `objectiveStationSystem` | – | – |

### Objective UI Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Objective Slot Prefab | `objectiveSlotPrefab` | `GameObject` | – | – |
| Objective List Content | `objectiveListContent` | `Transform` | – | – |
| Objective Name Text | `objectiveNameText` | `Text` | – | – |
| Objective Description Text | `objectiveDescriptionText` | `Text` | – | – |
| Objective Full Description Text | `objectiveFullDescriptionText` | `Text` | – | – |
| Objective Rewards Text | `objectiveRewardsText` | `Text` | – | – |
| Accept Objective Button Image | `acceptObjectiveButtonImage` | `Image` | – | – |
| Mission Complete Panel | `missionCompletePanel` | `GameObject` | – | – |
| Mission Complete Name Text | `missionCompleteNameText` | `Text` | – | – |
| Mission Complete Rewards Text | `missionCompleteRewardsText` | `Text` | – | – |
| Objective Station Menu | `objectiveStationMenu` | `GameObject` | – | – |
| Mission Accepted Panel | `missionAcceptedPanel` | `GameObject` | – | – |
| Mission Accepted Name Text | `missionAcceptedNameText` | `Text` | – | – |

### Character Objective UI Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Objective Panel Game Object | `characterObjectivePanelGameObject` | `GameObject` | – | – |
| Character Objective Name Text | `characterObjectiveNameText` | `Text` | – | – |
| Character Objective Description Text | `characterObjectiveDescriptionText` | `Text` | – | – |
| Character Objective Full Description Text | `characterObjectiveFullDescriptionText` | `Text` | – | – |
| Character Objective Rewards Text | `characterObjectiveRewardsText` | `Text` | – | – |
| Character Accept Mission Button | `characterAcceptMissionButton` | `GameObject` | – | – |
| Chracter Get Mission Reward Button | `chracterGetMissionRewardButton` | `GameObject` | – | – |

### Other Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Game Object | `playerControllerGameObject` | `GameObject` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Using Devices Manager | `usingDevicesManager` | `usingDevicesSystem` | – | – |
| Main Player Experience System | `mainPlayerExperienceSystem` | `playerExperienceSystem` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Main Objective Log System | `mainObjectiveLogSystem` | `objectiveLogSystem` | – | – |
| Main Objective Manager | `mainObjectiveManager` | `objectiveManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setButtonsColor(bool activeObjectiveColor)` | 受注ボタンの色を、引数がtrueなら`buttonUsable`、falseなら`buttonNotUsable`に設定する。 |
| `setCurrentObjectiveStationSystem(objectiveStationSystem newObjectiveStationSystem)` | 使用中ステーションを保持し、その`useCharacterObjectivePanel`の設定をこのUIに反映するだけ。 |
| `openOrCloseObjectiveStationMenu(bool state)` | 目標パネルを開閉し、ポーズ・カーソル・カメラ・操作を連動させ、開く時は一覧を再構築して先頭を選択する。 |
| `setObjectiveInfoList()` | キャラクター用なら現在ミッションの文言とボタンを更新し、ステーション用ならスロットを再生成して完了/受注済み表示を設定する。 |
| `checkPressedMission(GameObject objectiveSlot)` | 選択スロットを切り替えて文言と選択アイコンを更新し、完了済みで未受領なら報酬を付与し、状態に応じて受注ボタンの色を変える。 |
| `updateChracterObjectiveTextContent(string objectiveName, string objectiveDescription, string objectiveFullDescription, string objectiveRewards)` | キャラクター用パネルの名前・説明・詳細・報酬テキストを、必要ならローカライズして設定する。 |
| `updateObjectiveTextContent(string objectiveName, string objectiveDescription, string objectiveFullDescription, string objectiveRewards)` | ステーション用パネルの名前・説明・詳細・報酬テキストを、必要ならローカライズして設定する。 |
| `acceptMissionFromObjectiveStationPanel()` | 選択中ミッションをレベル条件と進行状況の確認後に開始またはログへ追加し、アイコン・受注メッセージ・ログ表示を更新する。 |
| `acceptMissionFromCharacterObjectivePanel()` | キャラクターの現ミッションを条件確認後に開始し、受注メッセージを出して、遅延後に端末操作でパネルを閉じるコルーチンを開始する。 |
| `checkStartCurrentMission()` | ステーションに開始遅延があれば既存コルーチンを止めて遅延開始し、なければ即座に`startCurrentMission`を呼ぶ。 |
| `startCurrentMission()` | 進行中ミッションの有無と設定に応じて、現ミッションを開始するか目標ログへ追加するだけ。 |
| `stopAcceptMissionFromCharacterObjectivePanelCoroutine()` | 受注後にパネルを閉じる`acceptMissionFromCharacterCoroutine`があれば停止するだけ。 |
| `getMissionRewardFromCharacterObjectivePanel()` | 未受領なら完了メッセージを出して報酬を付与し、受領済み状態にして報酬ボタンを隠す。 |
| `openOrCloseObjectiveMenuFromTouch()` | `menuOpened`を反転して`openOrCloseObjectiveStationMenu`を呼ぶだけ。 |
| `openOrCloseObjectiveStationMenuByButton()` | `useDevice`で端末を使用し、ステーション側の使用中フラグを現在の`menuOpened`に合わせる。 |
| `showMissionCompleteMessage()` | 時間指定があれば遅延付きの一時表示を、なければ完了パネルの表示と情報設定を行う。 |
| `showMissionCompleteMessageTemporarily()` | 既定の`delayToDisableMissionPanel`を渡して時間指定版を呼ぶだけ。 |
| `showMissionCompleteMessageTemporarily(float delayToDisablePanel)` | 既存コルーチンを止め、指定遅延で完了パネルを出して自動で閉じるコルーチンを開始する。 |
| `checkIfMissionsAvailableInCharacter()` | キャラクター用パネルで現ミッションが完了・報酬受領済みならインデックスを進め、次があれば一覧更新、なければ空表示にする。 |
| `enableAndSetMissionCompletePanelInfo()` | 完了パネルを表示し、現在のミッション(スロットまたはログ)を特定して名前と報酬をローカライズして設定する。 |
| `disableMissionCompletePanel()` | `missionCompletePanel`を非表示にするだけ。 |
| `showMissionAcceptedMessage(string missionAcceptedMessage, float delayToDisableMissionAcceptedPanelValue)` | 未初期化なら何もせず、既存コルーチンを止めて指定文言と遅延で受注メッセージ表示を開始する。 |
| `showMissionAcceptedMessage(string missionAcceptedMessage)` | 既定の`dissableObjectiveAcceptedPanelDelay`を渡して遅延指定版を呼ぶだけ。 |
| `disableMissionAcceptedPanel()` | `missionAcceptedPanel`を非表示にするだけ。 |
| `enableAndSetMissionAcceptedPanelInfo(string missionAcceptedMessage)` | 受注パネルを表示し、文言を必要ならローカライズして`missionAcceptedNameText`に設定する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnMissionWithHigherLevel` | `UnityEvent` | – |
| `eventOnMissionAccepted` | `UnityEvent` | – |
