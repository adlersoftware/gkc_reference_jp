# dialogSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Dialog System/dialogSystem.cs:11`

**概要**: プレイヤー側でダイアログ UI を表示し、行送り・回答選択・文字送り・音声・アニメーションを制御するコンポーネント。`dialogContentSystem` から受け取った内容でパネルと選択肢を更新する。

**公式ドキュメント抜粋**（[Dialog System](../../docs/character-level-components/character/dialog-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dialog Enabled | `dialogEnabled` | `bool` | true | – |
| Use Extra Text After Dialog Owner Name | `useExtraTextAfterDialogOwnerName` | `bool` | true | – |
| Extra Text After Dialog Owner Name | `extraTextAfterDialogOwnerName` | `string` | ": " | – |
| Ignore Extra Text If Owner Name Is Empty | `ignoreExtraTextIfOwnerNameIsEmpty` | `bool` | – | – |

### Answers Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Regular Answer Color | `regularAnswerColor` | `Color` | Color.white | – |
| Not Available Answer Color | `notAvailableAnswerColor` | `Color` | Color.red | – |
| Available Answer Color | `availableAnswerColor` | `Color` | Color.green | – |

### Animator Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dialogue Active Animator Name | `dialogueActiveAnimatorName` | `string` | "Dialogue Active" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Current Language | `currentLanguage` | `string` | – | – |
| Dialog Panel Info List | `dialogPanelInfoList` | `List<dialogPanelInfo>` | new List<dialogPanelInfo> () | – |
| Current Dialog Content System | `currentDialogContentSystem` | `dialogContentSystem` | – | – |
| Previous Dialog Content System | `previousDialogContentSystem` | `dialogContentSystem` | – | – |
| Current Dialog Content Index | `currentDialogContentIndex` | `int` | – | – |
| Dialog Active | `dialogActive` | `bool` | – | – |
| Dialog In Process | `dialogInProcess` | `bool` | – | – |
| Play Dialog Without Pausing Player Actions | `playDialogWithoutPausingPlayerActions` | `bool` | – | – |
| Show Dialog Line Word By Word | `showDialogLineWordByWord` | `bool` | – | – |
| Show Dialog Line Letter By Letter | `showDialogLineLetterByLetter` | `bool` | – | – |
| Play Dialogs Automatically | `playDialogsAutomatically` | `bool` | – | – |
| Can Use Input To Set Next Dialog | `canUseInputToSetNextDialog` | `bool` | – | – |
| Show Full Dialog Line On Input If Text Part By Part | `showFullDialogLineOnInputIfTextPartByPart` | `bool` | – | – |
| Use Custom Text Anchor And Aligment | `useCustomTextAnchorAndAligment` | `bool` | – | – |
| Stop Dialog If Player Distance Too Far | `stopDialogIfPlayerDistanceTooFar` | `bool` | – | – |
| Max Distance To Stop Dialog | `maxDistanceToStopDialog` | `float` | – | – |
| Rewind Last Dialog If Stopped | `rewindLastDialogIfStopped` | `bool` | – | – |
| Texting Showing Part By Part | `textingShowingPartByPart` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Pause Player Actions Input | `eventOnPausePlayerActionsInput` | `UnityEvent` | – | – |
| Event On Resume Player Actions Input | `eventOnResumePlayerActionsInput` | `UnityEvent` | – | – |

### Dialog Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dialog Panel | `dialogPanel` | `GameObject` | – | – |
| Current Dialog Owner Name Text | `currentDialogOwnerNameText` | `Text` | – | – |
| Dialog Content Without Options | `dialogContentWithoutOptions` | `GameObject` | – | – |
| Dialog Content With Options | `dialogContentWithOptions` | `GameObject` | – | – |
| Main Line Text | `mainLineText` | `Text` | – | – |
| Main Line Text Without Options | `mainLineTextWithoutOptions` | `Transform` | – | – |
| Main Line Text With Options | `mainLineTextWithOptions` | `Transform` | – | – |
| Dialog Options Panel | `dialogOptionsPanel` | `GameObject` | – | – |
| Dialog Options Panel Rect Transform | `dialogOptionsPanelRectTransform` | `RectTransform` | – | – |
| Dialog Options Parent | `dialogOptionsParent` | `Transform` | – | – |
| Next Line Button | `nextLineButton` | `GameObject` | – | – |
| Close Dialog Button | `closeDialogButton` | `GameObject` | – | – |
| Dialog Options Scroll Rect | `dialogOptionsScrollRect` | `ScrollRect` | – | – |
| Dialog Options Scroll Rect Rect Transform | `dialogOptionsScrollRectRectTransform` | `RectTransform` | – | – |
| Dialog Option Prefab | `dialogOptionPrefab` | `GameObject` | – | – |
| Dialog Options With Dialog Line Position | `dialogOptionsWithDialogLinePosition` | `RectTransform` | – | – |
| Dialog Options Without Dialog Line Position | `dialogOptionsWithoutDialogLinePosition` | `RectTransform` | – | – |
| Dialog Options List Size With Dialog | `dialogOptionsListSizeWithDialog` | `RectTransform` | – | – |
| Dialog Options List Size Without Dialog | `dialogOptionsListSizeWithoutDialog` | `RectTransform` | – | – |
| Simple Dialog Content | `simpleDialogContent` | `GameObject` | – | – |
| Simple Dialog Text | `simpleDialogText` | `Text` | – | – |
| Dialog Audio Source | `dialogAudioSource` | `AudioSource` | – | – |

### Component Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Game Object | `playerGameObject` | `GameObject` | – | – |
| Using Devices Manager | `usingDevicesManager` | `usingDevicesSystem` | – | – |
| Main Player Stats System | `mainPlayerStatsSystem` | `playerStatsSystem` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setNewDialogContent(dialogContentSystem newDialogContent)` | 新しいダイアログ内容と現在言語を読み込み、行一覧・設定を反映してパネル表示やイベント実行まで行う。 |
| `playDialogWithoutPausingPlayer()` | 自動再生が有効なら自動送りコルーチンを開始し、無効なら1行ずつ表示する処理に切り替える。 |
| `inputPlayNextDialogWioutPausingPlayer()` | 入力で1行進める。文字送り中は全文表示し、通常は次行送りか終了処理を行う。 |
| `playDialogWithoutPausingPlayerOneByOne()` | 実行中の自動送りを止め、`dialogInProcess` を立てて先頭行の表示を始める。 |
| `playNextDialogWithoutPausingPlayer()` | インデックスを進めて次の行を表示し、末尾を超えたら `closeDialog` で終了する。 |
| `playNextDialogWithoutPausingPlayerShowingDialogLinePartByPart()` | インデックスを進めたうえで文字送りコルーチンを開始し、行を部分表示する。 |
| `stopPlayNextDialogWithoutPausingPlayerShowingDialogLinePartByPartCoroutine()` | `textingShowingPartByPart` を false にし、文字送りコルーチンが有れば停止する。 |
| `stopPlayDialogWithoutPausingPlayerCoroutine()` | 自動送りコルーチンが有れば停止するだけ。 |
| `setNextDialog()` | 現在行の設定に従い、固定 ID・ランダム・条件イベント・次行送りのいずれかで表示行を進める。 |
| `setNextDialogWithConditionCheckResult(bool state)` | `state` に応じた遷移先 ID へ移動し、範囲外なら `closeDialog` を呼ぶ。 |
| `closeDialogIfActive()` | `dialogActive` が true のときだけ `closeDialog` を呼ぶ。 |
| `closeDialog()` | 再生コルーチンと UI を閉じ、入力復帰・終了イベント・AI 復帰・音声停止・外部状態解除を行う。 |
| `setDialogContentAnswer(Button buttonToCheck)` | 押された回答ボタンを特定し、遷移先 ID や条件イベント、行の無効化を適用して表示を更新する。 |
| `setDialogAnswerConditionCheckResult(bool state)` | 保留中の回答インデックスを使い、`state` に応じた遷移先 ID へ移動して表示を更新する。 |
| `checkDialogEvents()` | 現在行のプレイヤー送信イベント・`eventOnDialog`・遠隔イベントを実行する。 |
| `updateDialogContent()` | 現在行の本文・選択肢・文字色・音声・アニメーション・選択中 UI をまとめて更新する。 |
| `disableDialogCharacterAnimatorState(float delayAmount)` | `delayAmount` 秒後にアニメータ状態を解除するコルーチンを開始する。 |
| `stopDisableDialogCharacterAnimatorStateCoroutine()` | アニメータ解除用コルーチンが有れば停止するだけ。 |
| `setDialogAnimatorState(bool state)` | `mainAnimator` の bool とプレイヤーのルートモーション設定を切り替える。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnPausePlayerActionsInput` | `UnityEvent` | – |
| `eventOnResumePlayerActionsInput` | `UnityEvent` | – |

## 内部型

- `dialogPanelInfo`（class）
