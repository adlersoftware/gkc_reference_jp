# walkOnBalanceTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/walkOnBalanceTriggerSystem.cs:5`

**概要**: バランス移動ゾーンのトリガー。入場時にウェイポイントや親子設定をプレイヤーへ渡して移動を開始し、退場時に解除する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Check | `tagToCheck` | `string` | – | – |
| Movement Zone Active | `movementZoneActive` | `bool` | true | – |
| Main Simple Waypoint System | `mainSimpleWaypointSystem` | `simpleWaypointSystem` | – | – |
| Check On Trigger Enter | `checkOnTriggerEnter` | `bool` | true | – |
| Check On Trigger Exit | `checkOnTriggerExit` | `bool` | true | – |
| Set Player As Child | `setPlayerAsChild` | `bool` | true | – |
| Player Parent Transform | `playerParentTransform` | `Transform` | – | – |

### Jump On Target Position Reached Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Jump On End State | `setJumpOnEndState` | `bool` | – | – |
| Jump On End State | `jumpOnEndState` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

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
| `checkTriggerInfo(Collider col, bool isEnter)` | 入場時に移動設定を渡して開始し、退場時に解除してジャンプ設定を戻す。 |
