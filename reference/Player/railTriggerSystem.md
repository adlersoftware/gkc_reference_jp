# railTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/railTriggerSystem.cs:5`

**概要**: レールモードの開始/終了トリガー。入場時にスプラインと移動時間を渡し、退場時にレールを解除する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Check | `tagToCheck` | `string` | – | – |
| Rail Zone Active | `railZoneActive` | `bool` | true | – |
| Bezier Duration | `bezierDuration` | `float` | – | – |
| Rail Spline | `railSpline` | `BezierSpline` | – | – |
| Check On Trigger Enter | `checkOnTriggerEnter` | `bool` | true | – |
| Check On Trigger Exit | `checkOnTriggerExit` | `bool` | true | – |

### Reverse Direction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Can Change Direction Enabled | `setCanChangeDirectionEnabled` | `bool` | – | – |
| Can Change Direction Enabled | `canChangeDirectionEnabled` | `bool` | – | – |

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
| `checkTriggerInfo(Collider col, bool isEnter)` | 入場時にスプライン・時間・レール開始・方向反転設定を渡し、退場時にレール停止・スプライン解除・設定復元を行う。 |
