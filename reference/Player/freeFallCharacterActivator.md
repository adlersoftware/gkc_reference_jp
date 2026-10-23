# freeFallCharacterActivator

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/freeFallCharacterActivator.cs:6`

**概要**: 落下速度に応じてフリーフォール状態へ切り替えるコンポーネント。落下ターボや通常状態への復帰、開始判定のリセットを扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Character Fall Enabled | `checkCharacterFallEnabled` | `bool` | true | – |
| Min Time On Air To Activate Free Fall | `minTimeOnAirToActivateFreeFall` | `float` | 2 | – |
| Regular Air ID | `regularAirID` | `int` | -1 | – |
| Free Fall ID | `freeFallID` | `int` | 3 | – |
| Set New Camera State On Free Fall Active | `setNewCameraStateOnFreeFallActive` | `bool` | – | – |
| New Camera State On Free Fall | `newCameraStateOnFreeFall` | `string` | – | – |
| Capsule Collider Center | `capsuleColliderCenter` | `Vector3` | new Vector3 (0, 1, 0) | – |
| Use Min Fall Speed To Activate State | `useMinFallSpeedToActivateState` | `bool` | – | – |
| Min Fall Speed To Activate State | `minFallSpeedToActivateState` | `float` | – | – |
| Avoid Fall Damage On Free Fall | `avoidFallDamageOnFreeFall` | `bool` | – | – |
| Avoid Fall Damage On Free Fall Only On Turbo | `avoidFallDamageOnFreeFallOnlyOnTurbo` | `bool` | – | – |

### Turbo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fall Turbo Enabled | `fallTurboEnabled` | `bool` | true | – |
| Fall Turbo Multiplier | `fallTurboMultiplier` | `float` | 2 | – |
| Use Camera Shake | `useCameraShake` | `bool` | – | – |
| Regular Camera Shake Name | `regularCameraShakeName` | `string` | – | – |
| Use Max Fall Speed | `useMaxFallSpeed` | `bool` | – | – |
| Max Fall Speed | `maxFallSpeed` | `float` | – | – |
| Use Event On Landing With Turbo | `useEventOnLandingWithTurbo` | `bool` | – | – |
| Event On Landing With Turbo | `eventOnLandingWithTurbo` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Checking Free Fall | `checkingFreeFall` | `bool` | – | – |
| Free Fall Active | `freeFallActive` | `bool` | – | – |
| Free Fall Paused | `freeFallPaused` | `bool` | – | – |
| Fall Turbo Active | `fallTurboActive` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Free Fall State Change | `useEventsOnFreeFallStateChange` | `bool` | – | – |
| Event On Free Fall Active | `eventOnFreeFallActive` | `UnityEvent` | – | – |
| Event On Free Fall Deactivate | `eventOnFreeFallDeactivate` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `disableFreeFallActiveState()` | リセットフラグを false にし、`setFreeFallState(false)` を呼ぶ。 |
| `setFreeFallPausedState(bool state)` | false かつフリーフォール中なら通常値へ戻して停止し、`freeFallPaused` を設定する。 |
| `checkFallSpeed()` | 最低落下速度の使用時のみ縦速度と比較した結果を返し、未使用なら常に true を返す。 |
| `setResetCheckOnFreeFallActiveState(bool state)` | `resetCheckOnFreeFallActive` を設定するだけ。 |
| `inputEnableOrDisableFallTurbo(bool state)` | 落下ターボが有効かつフリーフォール中なら `setTurboState` を呼ぶ。 |
| `stopFreeFallStateIfActive()` | フリーフォール中なら通常値へ戻し、`disableFreeFallActiveState` を呼ぶ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnLandingWithTurbo` | `UnityEvent` | – |
| `eventOnFreeFallActive` | `UnityEvent` | – |
| `eventOnFreeFallDeactivate` | `UnityEvent` | – |
