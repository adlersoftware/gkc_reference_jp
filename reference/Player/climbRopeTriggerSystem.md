# climbRopeTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/climbRopeTriggerSystem.cs:5`

**概要**: 縄登りゾーン。プレイヤーが入ると上下端や親子設定を `climbRopeSystem` に渡して開始し、退場時に解除する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Check | `tagToCheck` | `string` | – | – |
| Movement Zone Active | `movementZoneActive` | `bool` | true | – |
| Bottom Transform | `bottomTransform` | `Transform` | – | – |
| Top Transform | `topTransform` | `Transform` | – | – |
| Check On Trigger Enter | `checkOnTriggerEnter` | `bool` | true | – |
| Check On Trigger Exit | `checkOnTriggerExit` | `bool` | true | – |
| Set Player As Child | `setPlayerAsChild` | `bool` | true | – |
| Player Parent Transform | `playerParentTransform` | `Transform` | – | – |
| Set New Climb Action ID | `setNewClimbActionID` | `bool` | – | – |
| New Climb Action ID | `newClimbActionID` | `int` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Events | `useRemoteEvents` | `bool` | – | – |
| Use Remote Event On Start | `useRemoteEventOnStart` | `bool` | – | – |
| Remote Event Name List On Start | `remoteEventNameListOnStart` | `List<string>` | new List<string> () | – |
| Use Remote Event On End | `useRemoteEventOnEnd` | `bool` | – | – |
| Remote Event Name List On End | `remoteEventNameListOnEnd` | `List<string>` | new List<string> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | 入場時にトリガー・親子設定・上下端・開始状態・アクションIDを設定し、退場時に子化解除・停止・端点クリア・ID復元を行う。 |
