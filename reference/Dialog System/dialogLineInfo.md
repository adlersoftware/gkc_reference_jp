# dialogLineInfo

- **種別**: class
- **ソース**: `Dialog System/completeDialogInfo.cs:134`
- **属性**: `System.Serializable`

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Name | `Name` | `string` | – | – |
| ID | `ID` | `int` | – | – |
| Dialog Line Content | `dialogLineContent` | `string` | – | TextArea (3, 10) |
| Dialog Info ID To Activate | `dialogInfoIDToActivate` | `int` | – | – |
| Use Random Dialog Info ID | `useRandomDialogInfoID` | `bool` | – | – |
| Use Random Dialog Range | `useRandomDialogRange` | `bool` | – | – |
| Random Dialog Range | `randomDialogRange` | `Vector2` | – | – |
| Random Dialog ID List | `randomDialogIDList` | `List<int>` | new List<int> () | – |
| Activate Remote Trigger System | `activateRemoteTriggerSystem` | `bool` | – | – |
| Remote Trigger Name | `remoteTriggerName` | `string` | – | – |
| Dialog Line Button | `dialogLineButton` | `Button` | – | – |
| Disable Line After Select | `disableLineAfterSelect` | `bool` | – | – |
| Line Disabled | `lineDisabled` | `bool` | – | – |
| Use Stat To Show Line | `useStatToShowLine` | `bool` | – | – |
| Stat Name | `statName` | `string` | – | – |
| Stat Is Amount | `statIsAmount` | `bool` | – | – |
| Min State Value | `minStateValue` | `float` | – | – |
| Bool State Value | `boolStateValue` | `bool` | – | – |
| Answer Not Available | `answerNotAvailable` | `bool` | – | – |
| Extra Dialog Line Content | `extraDialogLineContent` | `string` | – | – |
| Check Condition For Next Line | `checkConditionForNextLine` | `bool` | – | – |
| Dialog Info ID To Activate On Condition True | `dialogInfoIDToActivateOnConditionTrue` | `int` | – | – |
| Dialog Info ID To Activate On Condition False | `dialogInfoIDToActivateOnConditionFalse` | `int` | – | – |
| Event To Check Condition For Next Line | `eventToCheckConditionForNextLine` | `UnityEvent` | – | – |
| Use Event To Send Player To Condition | `useEventToSendPlayerToCondition` | `bool` | – | – |
| Event To Send Player To Condition | `eventToSendPlayerToCondition` | `eventParameters.eventToCallWithGameObject` | – | – |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToCheckConditionForNextLine` | `UnityEvent` | – |
