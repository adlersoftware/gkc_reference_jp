# completeDialogInfo

- **種別**: class
- **ソース**: `Dialog System/completeDialogInfo.cs:8`
- **属性**: `System.Serializable`

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Name | `Name` | `string` | – | – |
| ID | `ID` | `int` | – | – |
| Play Dialog Without Pausing Player Actions | `playDialogWithoutPausingPlayerActions` | `bool` | – | – |
| Play Dialogs Automatically | `playDialogsAutomatically` | `bool` | true | – |
| Pause Player Actions Input | `pausePlayerActionsInput` | `bool` | – | – |
| Pause Player Movement Input | `pausePlayerMovementInput` | `bool` | – | – |
| Can Use Input To Set Next Dialog | `canUseInputToSetNextDialog` | `bool` | true | – |
| Show Full Dialog Line On Input If Text Part By Part | `showFullDialogLineOnInputIfTextPartByPart` | `bool` | true | – |
| Show Dialog Line Word By Word | `showDialogLineWordByWord` | `bool` | – | – |
| Dialog Line Word Speed | `dialogLineWordSpeed` | `float` | 0.5f | – |
| Show Dialog Line Letter By Letter | `showDialogLineLetterByLetter` | `bool` | – | – |
| Dialog Line Letter Speed | `dialogLineLetterSpeed` | `float` | 0.03f | – |
| Use Custom Text Anchor And Aligment | `useCustomTextAnchorAndAligment` | `bool` | – | – |
| Text Anchor | `textAnchor` | `TextAnchor` | TextAnchor.MiddleCenter | – |
| Stop Dialog If Player Distance Too Far | `stopDialogIfPlayerDistanceTooFar` | `bool` | – | – |
| Max Distance To Stop Dialog | `maxDistanceToStopDialog` | `float` | – | – |
| Rewind Last Dialog If Stopped | `rewindLastDialogIfStopped` | `bool` | – | – |
| Event On Dialog Stopped | `eventOnDialogStopped` | `UnityEvent` | – | – |
| Play Dialog On Trigger Enter | `playDialogOnTriggerEnter` | `bool` | – | – |
| Event To Play Dialog On Trigger Enter | `eventToPlayDialogOnTriggerEnter` | `UnityEvent` | – | – |
| Dialog Info List | `dialogInfoList` | `List<dialogInfo>` | new List<dialogInfo> () | – |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnDialogStopped` | `UnityEvent` | – |
| `eventToPlayDialogOnTriggerEnter` | `UnityEvent` | – |
