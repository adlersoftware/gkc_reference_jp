# dialogContentSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Dialog System/dialogContentSystem.cs:6`

**概要**: キャラクター1体分のダイアログ内容（複数の `completeDialogInfo`）を保持するコンポーネント。プレイヤーの `dialogSystem` と連携して開始・終了を切り替え、イベント・AI 停止・アニメータ制御も担当する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dialog Content ID | `dialogContentID` | `int` | – | ダイアログ管理が内容を検索するID。 |
| Dialog Content Scene | `dialogContentScene` | `int` | – | 検索に使うシーン番号。セーブ復元と対応。 |
| Current Dialog Index | `currentDialogIndex` | `int` | – | 現在再生する会話のリスト番号。 |
| Dialog Owner | `dialogOwner` | `GameObject` | – | この会話の所有者となるキャラクター。 |
| Show Dialog Onwer Name | `showDialogOnwerName` | `bool` | – | 会話UIに話者の名前を表示する。 |

### AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pause AI On Dialog Start | `pauseAIOnDialogStart` | `bool` | – | 会話開始時にAIの動作を止める。 |
| Resume AI On Dialog End | `resumeAIOnDialogEnd` | `bool` | – | 会話終了時に停止したAIを再開する。 |
| Interrupt Wander Around State If Active On Dialog Start | `interruptWanderAroundStateIfActiveOnDialogStart` | `bool` | – | 会話開始時に徘徊状態を中断させる。 |
| Disable Wander Around State On Dialog End | `disableWanderAroundStateOnDialogEnd` | `bool` | – | 会話終了時に徘徊状態を解除する。 |

### Animations Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Animations | `useAnimations` | `bool` | – | 会話中にアニメーターの制御を行う。 |
| Main Animator | `mainAnimator` | `Animator` | – | 会話状態を切り替えるAnimator。 / 表示条件: `useAnimations` がオンのとき |
| Main Player Controller | `mainPlayerController` | `playerController` | – | ルートモーション設定を切り替える対象の制御。 / 表示条件: `useAnimations` がオンのとき |
| Dialogue Active Animator Name | `dialogueActiveAnimatorName` | `string` | "Dialogue Active" | 会話中にtrueにするAnimatorのbool名。 / 表示条件: `useAnimations` がオンのとき |
| Player Animations On Dialog Enabled | `playerAnimationsOnDialogEnabled` | `bool` | true | 会話中にプレイヤー側のアニメも再生する。 / 表示条件: `useAnimations` がオンのとき |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Start End Dialog | `useEventsOnStartEndDialog` | `bool` | – | 会話の開始と終了でイベントを呼ぶ。 |
| Event On Start Dialog | `eventOnStartDialog` | `UnityEvent` | – | 会話開始時に実行するイベント。 / 表示条件: `useEventsOnStartEndDialog` がオンのとき |
| Event On End Dialog | `eventOnEndDialog` | `UnityEvent` | – | 会話終了時に実行するイベント。 / 表示条件: `useEventsOnStartEndDialog` がオンのとき |

### Add Dialog To Character Manually Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| New Character To Add Dialog | `newCharacterToAddDialog` | `GameObject` | – | 会話を追加する相手を指定する欄。 |

### Dialog Content Template Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Dialog Content Template | `useDialogContentTemplate` | `bool` | – | 言語別テンプレートから会話内容を取得する。 |
| Main Dialog Content Template | `mainDialogContentTemplate` | `dialogContentTemplate` | – | 言語別の会話内容を持つテンプレート。 / 表示条件: `useDialogContentTemplate` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `completeDialogInfoList` | `List<completeDialogInfo>` | new List<completeDialogInfo> () | – |
| `dialogActive` | `bool` | – | – |
| `dialogInProcess` | `bool` | – | – |
| `playingExternalDialog` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentPlayer(GameObject newPlayer)` | `currentPlayer` に `newPlayer` を代入するだけ。 |
| `activateDialog()` | `dialogActive` を反転し、開始時はプレイヤーの `dialogSystem` に自身を渡して会話を開始する。 |
| `setDialogInProcessState(bool state)` | `dialogInProcess` を設定し、false なら `dialogActive` も false にする。 |
| `activateEventOnDialogStopped()` | 現在のダイアログがプレイヤー非停止設定なら `eventOnDialogStopped` を実行する。 |
| `setNextCompleteDialogIndex()` | `currentDialogIndex` を1つ進め、末尾を超えると最後のインデックスに留める。 |
| `setPrevioustCompleteDialogIndex()` | `currentDialogIndex` を1つ戻し、0未満になると0に留める。 |
| `setCompleteDialogIndex(int newIndex)` | `currentDialogIndex` に `newIndex` を設定し、一覧数を超える場合は末尾に補正する。 |
| `setPlayingExternalDialogState(bool state)` | `playingExternalDialog` を設定するだけ。 |
| `checkIfPlayDialogOnTriggerEnter()` | 前回のコルーチンを停止し、1フレーム後にトリガー用イベントを呼ぶコルーチンを開始する。 |
| `disableDialogCharacterAnimatorState(float delayAmount)` | `useAnimations` 有効時のみ、`delayAmount` 秒後にアニメータを解除するコルーチンを開始する。 |
| `stopDisableDialogCharacterAnimatorStateCoroutine()` | アニメータ解除用コルーチンが実行中なら停止するだけ。 |
| `setDialogAnimatorState(bool state)` | `mainAnimator` の bool と `mainPlayerController` のルートモーション設定をまとめて切り替える。 |
| `enableAnimatorLayerWeight(string animatorLayerName)` | `mainPlayerController` の同名メソッドに委譲してアニメータレイヤーの重みを有効にする。 |
| `checkEventsOnDialog(bool state)` | `useEventsOnStartEndDialog` 有効時、`state` で開始/終了イベントを呼び分ける。 |
| `checkIfPauseOrResumeAI(bool state)` | `dialogOwner` の AI を、開始時は徘徊中断と停止、終了時は再開と徘徊無効に切り替える。 |
| `checkIfAIFollowPlayerAfterDialogEnd(bool state)` | `state` かつ `currentPlayer` があるとき、`dialogOwner` の AI にプレイヤーを登録する。 |
| `setDialogAnswerConditionCheckResult(bool state)` | `dialogActive` のとき、プレイヤーの `dialogSystem` へ条件判定結果を転送する。 |
| `setNextDialogWithConditionCheckResult(bool state)` | `dialogActive` のとき、プレイヤーの `dialogSystem` へ条件分岐結果を転送する。 |
| `getCompleteDialogInfoTemplateByLanguageName(string languageName)` | `language` が一致するテンプレートを返し、見つからなければ `null` を返す。 |
| `getDialogContentID()` | `dialogContentID` を返すだけ。 |
| `getDialogContentScene()` | `dialogContentScene` を返すだけ。 |
| `getCurrentDialogIndex()` | `currentDialogIndex` を返すだけ。 |
| `addNewDialog()` | 空の `completeDialogInfo` を ID 付きで一覧に追加し、`updateComponent` を呼ぶ。 |
| `addNewLine(int dialogIndex)` | 指定ダイアログに空の `dialogInfo` を ID 付きで追加し、`updateComponent` を呼ぶ。 |
| `addNewAnswer(int dialogIndex, int lineIndex)` | 指定行に空の `dialogLineInfo` を ID 付きで追加し、`updateComponent` を呼ぶ。 |
| `assignIDToDialog(int newID)` | `dialogContentID` を設定して `updateComponent` を呼ぶ。 |
| `assignDialogContentScene(int newScene)` | `dialogContentScene` を設定して `updateComponent` を呼ぶ。 |
| `setDialogOwnerGameObject(GameObject newOwner)` | `dialogOwner` を設定し、`playerController` からアニメータ取得と追従対象の設定を行う。 |
| `addDialogToCharacterManually()` | `newCharacterToAddDialog` があれば所有者として設定し、そのフィールドを空にして更新する。 |
| `addDialogContentToTemplate()` | 現在のダイアログ内容を `English` 言語のテンプレートとして複製し、一覧に追加する。 |
| `updateComponent()` | `GKC_Utils` 経由でコンポーネントとシーンのダーティ更新を行う。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartDialog` | `UnityEvent` | – |
| `eventOnEndDialog` | `UnityEvent` | – |
