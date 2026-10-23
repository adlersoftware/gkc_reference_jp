# tutorialInfo

- **種別**: class
- **ソース**: `Tutorial System/tutorialInfo.cs:11`
- **属性**: `System.Serializable`

**概要**: 1つのチュートリアル定義で、名前・パネル一覧・表示設定・音声や動画の情報・一度だけ再生するフラグを持つシリアライズクラス。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Name | `Name` | `string` | – | – |
| Panel Game Object | `panelGameObject` | `GameObject` | – | – |
| Tutorial Panel List | `tutorialPanelList` | `List<panelInfo>` | new List<panelInfo> () | – |
| Unlock Cursor On Tutorial Active | `unlockCursorOnTutorialActive` | `bool` | – | – |
| Use Action Button To Move Through Tutorial | `useActionButtonToMoveThroughTutorial` | `bool` | – | – |
| Press Any Button To Next Tutorial | `pressAnyButtonToNextTutorial` | `bool` | – | – |
| Time To Enable Keys | `timeToEnableKeys` | `float` | 1 | – |
| Open Tutorial Delay | `openTutorialDelay` | `float` | – | – |
| Set Custom Time Scale | `setCustomTimeScale` | `bool` | – | – |
| Custom Time Scale | `customTimeScale` | `float` | – | – |
| Use Sound On Tutorial Open | `useSoundOnTutorialOpen` | `bool` | – | – |
| Sound On Tutorial Open | `soundOnTutorialOpen` | `AudioClip` | – | – |
| On Tutorial Open Audio Element | `onTutorialOpenAudioElement` | `AudioElement` | – | – |
| Play Tutorial Only Once | `playTutorialOnlyOnce` | `bool` | – | – |
| Tutorial Played | `tutorialPlayed` | `bool` | – | – |
| Contains Video | `containsVideo` | `bool` | – | – |
| Video Info List | `videoInfoList` | `List<videoInfo>` | new List<videoInfo> () | – |
| Set Next Panel When Video Ends | `setNextPanelWhenVideoEnds` | `bool` | – | – |
| Current Video Index | `currentVideoIndex` | `int` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `InitializeAudioElements()` | `soundOnTutorialOpen`があれば、チュートリアルを開く時の`AudioElement`のクリップに設定する。 |
