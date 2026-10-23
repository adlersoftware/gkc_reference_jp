# objectiveLogSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Objectives Mission System/objectiveLogSystem.cs:8`

**概要**: プレイヤーの目標ログメニューを管理するコンポーネント。ミッションスロットの生成・削除、選択内容の表示、メニュー開閉、達成・報酬状態の記録を担う。

**公式ドキュメント抜粋**（[Objective Log System](../../docs/character-level-components/character/objective-log-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Open Menu Enabled | `openMenuEnabled` | `bool` | true | – |
| Objective Menu Active | `objectiveMenuActive` | `bool` | true | – |
| Check Min Level On Missions | `checkMinLevelOnMissions` | `bool` | – | – |
| Button Usable | `buttonUsable` | `Color` | – | – |
| Button Not Usable | `buttonNotUsable` | `Color` | – | – |
| Save Current Player Missions To Save File | `saveCurrentPlayerMissionsToSaveFile` | `bool` | – | – |
| Menu Panel Name | `menuPanelName` | `string` | "Objective Log System" | – |
| Main Mission Manager Name | `mainMissionManagerName` | `string` | "Mission Manager" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Objective Menu Opened | `objectiveMenuOpened` | `bool` | – | – |
| Objective In Process | `objectiveInProcess` | `bool` | – | – |
| Objective Slot Info List | `objectiveSlotInfoList` | `List<objectiveSlotInfo>` | new List<objectiveSlotInfo> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event If System Disabled | `useEventIfSystemDisabled` | `bool` | – | – |
| Event If System Disabled | `eventIfSystemDisabled` | `UnityEvent` | – | – |

### UI Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Objective Menu Game Object | `objectiveMenuGameObject` | `GameObject` | – | – |
| Objective Slot Prefab | `objectiveSlotPrefab` | `GameObject` | – | – |
| Objective Name Text | `objectiveNameText` | `Text` | – | – |
| Objective Description Text | `objectiveDescriptionText` | `Text` | – | – |
| Objective Full Description Text | `objectiveFullDescriptionText` | `Text` | – | – |
| Objective Rewards Text | `objectiveRewardsText` | `Text` | – | – |
| Active Objective Button Image | `activeObjectiveButtonImage` | `Image` | – | – |
| Cancel Objective Button Image | `cancelObjectiveButtonImage` | `Image` | – | – |
| Objective List Content | `objectiveListContent` | `Transform` | – | – |
| Mission List Scrollbar | `missionListScrollbar` | `Scrollbar` | – | – |
| Mission Info Scrollbar | `missionInfoScrollbar` | `Scrollbar` | – | – |
| Mission Reward Scrollbar | `missionRewardScrollbar` | `Scrollbar` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Game Object | `playerControllerGameObject` | `GameObject` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Main Objective Manager | `mainObjectiveManager` | `objectiveManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `initializeMissionValues()` | `objectiveMenuActive`が無効なら無効イベントを呼んで終了し、有効なら`objectiveManager`を検索・生成して目標テキストを空にする。 |
| `getObjectiveEventSystem(int missionID, int missionSceneToSearch)` | `mainObjectiveManagerLocated`が真なら`mainObjectiveManager`へIDとシーンを渡して検索し、そうでなければnullを返す。 |
| `checkEventOnSystemDisabled()` | `useEventIfSystemDisabled`が有効な時のみ`eventIfSystemDisabled`を呼び出す。 |
| `setButtonsColor(bool activeObjectiveColor, bool cancelObjectiveColor)` | 受注とキャンセルの各ボタンの色を、引数の真偽に応じて`buttonUsable`か`buttonNotUsable`に設定する。 |
| `activeObjective()` | 選択中スロットのミッションが開始可能なら`startObjective`を呼び、実行中アイコンを出してボタン色と現在の対象を更新する。 |
| `cancelObjective()` | キャンセル可否を確認し、未完了なら`stopObjective`を呼んで実行中アイコンを消し、ボタン色を更新する。 |
| `objectiveComplete(objectiveEventSystem currentObjectiveEventSystem)` | 一致スロットへ`updateObjectiveCompleteSlotInfo`を適用して`objectiveInProcess`を偽にする。 |
| `updateObjectiveCompleteSlotInfo(int objectiveSlotIndex)` | 完了スロットのアイコンを消して完了パネルとテキストを表示し、ログ登録設定に応じてスロット表示を切り替えて完了を記録する。 |
| `checkUpdateObjectiveSlotInfo(objectiveEventSystem currentObjectiveEventSystem)` | 一致スロットの完了パネル・完了テキスト・実行中アイコンの表示を、現在の完了/実行状態に合わせて更新する。 |
| `updateSubObjectiveCompleteListSlotInfo(int objectiveSlotIndex, List<bool> subObjectiveCompleteList)` | 指定スロットの`subObjectiveCompleteList`を渡されたリストで置き換えるだけ。 |
| `activeObjective(objectiveEventSystem currentObjectiveEventSystem)` | 一致スロットの実行中アイコンを表示し、現在の対象と`missionInProcess`・`objectiveInProcess`を真にする。 |
| `cancelObjective(objectiveEventSystem currentObjectiveEventSystem)` | 一致スロットの実行中アイコンを消して実行中フラグを下ろし、削除設定が有効なら`removeObjectiveSlotFromMenu`でスロットを消す。 |
| `cancelCurrentMissionOnPlayerDead()` | 現在のミッションが死亡時キャンセル設定なら`cancelPreviousObjective`を呼んで中断させる。 |
| `cancelPreviousObjective()` | 現在のミッションが実行中なら、その`cancelPreviousObjective`を呼び出すだけ。 |
| `getCurrentObjectiveEventSystem()` | `currentObjectiveEventManager`を返すだけ。 |
| `showObjectiveInformation(GameObject objectiveSlot)` | 選択スロットを切り替えて目標名・説明・報酬を表示し、ミッション状態に応じて受注/キャンセルボタンの色を設定する。 |
| `updateUIElements()` | 実行中なら対象ミッションのHUDを更新し、全スロットの目標名と場所を言語設定に応じてアイコン要素へ反映する。 |
| `updateObjectiveTextContent(string objectiveName, string objectiveDescription, string objectiveFullDescription, string objectiveRewards)` | 4つの引数を必要に応じて翻訳し、目標名・説明・詳細・報酬の各テキストへ設定する。 |
| `addObjective(string objectiveName, string objectiveDescription, string objectiveFullDescription, string objectiveLocation, string objectiveRewards, objectiveEventSystem currentObjectiveEventSystem, bool addObjectiveToPlayerLogSystem)` | 重複を避けて目標スロットを生成または再利用し、各テキストと受注状態、サブ目標達成リストを記録する。 |
| `removeObjectiveSlotFromMenu(int missionID, int missionScene)` | IDとシーンが一致するスロットを破棄してリストから削除し、選択状態と表示テキストを空に戻す。 |
| `openOrCloseObjectiveMenu(bool state)` | メニュー使用可否を確認して目標メニューを開閉し、ポーズ連携・選択解除・スクロール位置のリセットまで行う。 |
| `checkOpenOrCloseObjectiveMenuFromTouch()` | `pauseManager`が同名メニューの開閉を止めていない場合のみ、タッチ用の開閉処理へ進む。 |
| `openOrCLoseObjectiveMenuFromTouch()` | `objectiveMenuOpened`を反転して`openOrCloseObjectiveMenu`を呼ぶだけ。 |
| `inputOpenOrCloseObjectiveMenu()` | `openMenuEnabled`と`objectiveMenuActive`を確認し、他メニューで停止中でなければ目標メニューを開閉する。 |
| `resetScrollBarPosition(Scrollbar scrollBarToReset, ref Coroutine scrollBarCoroutine)` | 既存コルーチンを停止し、2フレーム待ってから`value`を1にする`resetScroll`を開始する。 |
| `resetPanelSlotsRectTransform(Transform panelTransform, ScrollRect panelScrollRect)` | レイアウトリビルド後に2フレーム待って`verticalNormalizedPosition`を1へ戻すコルーチンを開始する。 |
| `isObjectiveMenuActive()` | `objectiveMenuActive`の値を返すだけ。 |
| `isObjectiveInProcess()` | `objectiveInProcess`の値を返すだけ。 |
| `isCheckMinLevelOnMissionsEnabled()` | `checkMinLevelOnMissions`の値を返すだけ。 |
| `setObtainedRewardState(int missionID, int missionScene, bool state)` | IDとシーンが一致する全スロットの`rewardObtained`を指定値に設定する。 |
| `setSubObjectiveCompleteState(int missionID, int missionScene, int subObjectiveIndex, bool state)` | IDとシーンが一致するスロットの`subObjectiveCompleteList`について、範囲内なら指定インデックスを更新する。 |
| `setObjectiveMenuActiveState(bool state)` | `objectiveMenuActive`を指定値に設定するだけ。 |
| `setOpenMenuEnabled(bool state)` | `openMenuEnabled`を指定値に設定するだけ。 |
| `setObjectiveMenuActiveStateFromEditor(bool state)` | `objectiveMenuActive`を設定したうえで`updateComponent`によりシーンを更新する。 |
| `setOpenMenuEnabledFromEditor(bool state)` | `openMenuEnabled`を設定したうえで`updateComponent`によりシーンを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventIfSystemDisabled` | `UnityEvent` | – |

## 内部型

- `objectiveSlotInfo`（class）
