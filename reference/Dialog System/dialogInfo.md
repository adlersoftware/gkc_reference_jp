# dialogInfo

- **種別**: class
- **ソース**: `Dialog System/completeDialogInfo.cs:49`
- **属性**: `System.Serializable`

**概要**: 1つのダイアログ行の本文・所有者名・分岐・音声・アニメーション設定を保持するシリアライズ可能クラス。`InitializeAudioElements` は音声クリップを `AudioElement` へ橋渡しする。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Name | `Name` | `string` | – | – |
| ID | `ID` | `int` | – | – |
| Dialog Owner Name | `dialogOwnerName` | `string` | – | – |
| Dialog Content | `dialogContent` | `string` | – | TextArea (3, 10) |
| Show Previous Dialog Line On Options | `showPreviousDialogLineOnOptions` | `bool` | – | – |
| Dialog Line Info List | `dialogLineInfoList` | `List<dialogLineInfo>` | new List<dialogLineInfo> () | – |
| Event On Dialog | `eventOnDialog` | `UnityEvent` | – | – |
| Use Event To Send Player | `useEventToSendPlayer` | `bool` | – | – |
| Event To Send Player | `eventToSendPlayer` | `eventParameters.eventToCallWithGameObject` | – | – |
| Activate When Dialog Closed | `activateWhenDialogClosed` | `bool` | – | – |
| Activate Remote Trigger System | `activateRemoteTriggerSystem` | `bool` | – | – |
| Remote Trigger Name | `remoteTriggerName` | `string` | – | – |
| Use Nex Line Button | `useNexLineButton` | `bool` | true | – |
| Is End Of Dialog | `isEndOfDialog` | `bool` | – | – |
| Change To Dialog Info ID | `changeToDialogInfoID` | `bool` | – | – |
| Dialog Info ID To Activate | `dialogInfoIDToActivate` | `int` | – | – |
| Use Random Dialog Info ID | `useRandomDialogInfoID` | `bool` | – | – |
| Use Random Dialog Range | `useRandomDialogRange` | `bool` | – | – |
| Random Dialog Range | `randomDialogRange` | `Vector2` | – | – |
| Random Dialog ID List | `randomDialogIDList` | `List<int>` | new List<int> () | – |
| Check Condition For Next Line | `checkConditionForNextLine` | `bool` | – | – |
| Dialog Info ID To Activate On Condition True | `dialogInfoIDToActivateOnConditionTrue` | `int` | – | – |
| Dialog Info ID To Activate On Condition False | `dialogInfoIDToActivateOnConditionFalse` | `int` | – | – |
| Event To Check Condition For Next Line | `eventToCheckConditionForNextLine` | `UnityEvent` | – | – |
| Use Event To Send Player To Condition | `useEventToSendPlayerToCondition` | `bool` | – | – |
| Event To Send Player To Condition | `eventToSendPlayerToCondition` | `eventParameters.eventToCallWithGameObject` | – | – |
| Disable Dialog After Select | `disableDialogAfterSelect` | `bool` | – | – |
| Dialog Info ID To Jump | `dialogInfoIDToJump` | `int` | – | – |
| Dialog Info Disabled | `dialogInfoDisabled` | `bool` | – | – |
| Set Next Complete Dialog ID | `setNextCompleteDialogID` | `bool` | – | – |
| Set New Complete Dialog ID | `setNewCompleteDialogID` | `bool` | – | – |
| New Complete Dialog ID | `newCompleteDialogID` | `int` | – | – |
| Delay To Show Next Dialog Line | `delayToShowNextDialogLine` | `float` | 5 | – |
| Delay To Show This Dialog Line | `delayToShowThisDialogLine` | `float` | – | – |
| Use Dialog Line Sound | `useDialogLineSound` | `bool` | – | – |
| Dialog Line Sound | `dialogLineSound` | `AudioClip` | – | – |
| Dialog Line Audio Element | `dialogLineAudioElement` | `AudioElement` | – | – |
| Use Animations | `useAnimations` | `bool` | – | – |
| Animation Name | `animationName` | `string` | – | – |
| Delay To Play Animation | `delayToPlayAnimation` | `float` | – | – |
| Loop Animation | `loopAnimation` | `bool` | – | – |
| Use Delay To Disable Animation | `useDelayToDisableAnimation` | `bool` | – | – |
| Delay To Disable Animation | `delayToDisableAnimation` | `float` | – | – |
| Animation Used On Player | `animationUsedOnPlayer` | `bool` | – | – |
| Enable Animator Layer | `enableAnimatorLayer` | `bool` | true | – |
| Animator Layer To Enable Name | `animatorLayerToEnableName` | `string` | "Dialogue" | – |
| Character Follow Player After Dialog End | `characterFollowPlayerAfterDialogEnd` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `InitializeAudioElements()` | `dialogLineSound` を `dialogLineAudioElement.clip` に代入するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnDialog` | `UnityEvent` | – |
| `eventToCheckConditionForNextLine` | `UnityEvent` | – |
