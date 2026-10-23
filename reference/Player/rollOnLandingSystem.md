# rollOnLandingSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/rollOnLandingSystem.cs:6`

**概要**: 空中で入力すると着地時にローリングする「着地ロール」を扱う。入力の受付時間と空中時間を判定し、コルーチンでロールを実行する。

**公式ドキュメント抜粋**（[Roll On Landing System](../../docs/player-controller-components/non-essential-components/roll-on-landing-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Roll Onlanding Enabled | `rollOnlandingEnabled` | `bool` | true | – |
| Roll On Landing Check Duration | `rollOnLandingCheckDuration` | `float` | – | – |
| Events On Roll Landing Delay | `eventsOnRollLandingDelay` | `float` | – | – |
| Distance From Ground To Activate Roll On Landing | `distanceFromGroundToActivateRollOnLanding` | `float` | 1 | – |
| Min Wait To Activate Roll On Landing Input | `minWaitToActivateRollOnLandingInput` | `float` | 0.5f | – |
| Raycast Layermask | `raycastLayermask` | `LayerMask` | – | – |
| Use Max Time On Air To Activate Roll On Landing | `useMaxTimeOnAirToActivateRollOnLanding` | `bool` | – | – |
| Max Time On Air To Activate Roll On Landing | `maxTimeOnAirToActivateRollOnLanding` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Roll On Landing Check Active | `rollOnLandingCheckActive` | `bool` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Events On Roll On Landing Third Person | `eventsOnRollOnLandingThirdPerson` | `UnityEvent` | – | – |
| Events On Roll On Landing First Person | `eventsOnRollOnLandingFirstPerson` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCancelCheckRollOnLandingOnceActive(bool state)` | キャンセルフラグを設定し、`lastTimeCancelCheckRoll` に現在時刻を記録する。 |
| `inputActivateRollOnLanding()` | 直後0.7秒・接地中・各種条件では中止し、問題なければロールを開始する。 |
| `inputDeactivateRollOnLanding()` | 無効時や接地中は何もせず、そうでなければロールコルーチンを停止する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventsOnRollOnLandingThirdPerson` | `UnityEvent` | – |
| `eventsOnRollOnLandingFirstPerson` | `UnityEvent` | – |
