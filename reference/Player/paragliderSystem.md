# paragliderSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `externalControllerBehavior`
- **ソース**: `Player/Extra Movements/paragliderSystem.cs:6`

**概要**: パラグライダーで滑空するモードを提供する `externalControllerBehavior`。重力と上昇力を調整して落下を緩め、カメラや接地アニメーションも切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Paraglider Mode Enabled | `paragliderModeEnabled` | `bool` | true | – |
| Gravity Force | `gravityForce` | `float` | -9.8f | – |
| Gravity Multiplier | `gravityMultiplier` | `float` | – | – |
| Min Wait Time To Activate Paraglider | `minWaitTimeToActivateParaglider` | `float` | 0.6f | – |
| Air Speed | `airSpeed` | `float` | 25 | – |
| Air Control | `airControl` | `float` | 10 | – |

### Extra Force Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Extra Up Force | `addExtraUpForce` | `bool` | – | – |
| Extra Up Force Amount | `extraUpForceAmount` | `float` | 5 | – |
| Remove Extra Up Force After Delay | `removeExtraUpForceAfterDelay` | `bool` | – | – |
| Delay To Remove Extra Up Force | `delayToRemoveExtraUpForce` | `float` | – | – |

### Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Regular Air ID | `regularAirID` | `int` | -1 | – |
| Paraglider ID | `paragliderID` | `int` | 1 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Paraglider Mode Paused | `paragliderModePaused` | `bool` | – | – |
| Paraglider Mode Active | `paragliderModeActive` | `bool` | – | – |
| Player Is Moving | `playerIsMoving` | `bool` | – | – |
| External Force Active | `externalForceActive` | `bool` | – | – |
| Externa Force Direction | `externaForceDirection` | `Vector3` | – | – |
| External Force Amount | `externalForceAmount` | `float` | – | – |
| Checking To Activate Paraglider | `checkingToActivateParaglider` | `bool` | – | – |
| External Forces Counter | `externalForcesCounter` | `int` | – | – |
| Use Last Time Paraglider Pause Active | `useLastTimeParagliderPauseActive` | `bool` | – | – |
| Previous Gravity Force | `previousGravityForce` | `float` | -1000 | – |
| Previous Gravity Multiplier | `previousGravityMultiplier` | `float` | -1000 | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On State Enabled | `eventOnStateEnabled` | `UnityEvent` | – | – |
| Event On State Disabled | `eventOnStateDisabled` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableParagliderMode(bool state)` | 滑空状態を切り替え、外部コントローラ、airID、イベント、スローフォール、重力の保存/復元、接地アニメーションを更新する。 |
| `inputToggletParagliderActiveState()` | 滑空中なら終了し、そうでなければ判定フラグを反転して開始/終了を要求する。 |
| `inputSetParagliderActiveState(bool state)` | 地上・FF/無重力・壁走り・水泳・運転・空中外部動作中は中止し、直近停止時間を確認してから判定コルーチンを開始/終了する。 |
| `stopCheckingToActivateParagliderCoroutine()` | `checkingToActivateCoroutine` が null でなければ停止するだけ。 |
| `setParagliderModePausedState(bool state)` | true かつ滑空中なら終了し、`paragliderModePaused` を設定する。 |
| `setUseLastTimeParagliderPauseActive(float newDuration)` | 再使用禁止フラグを立て、現在時刻と指定時間を保存する。 |
| `setParagliderModeEnabledState(bool state)` | 滑空中なら終了してから `paragliderModeEnabled` を設定する。 |
| `setOriginalParagliderModeEnabledState()` | 保存値 `originalParagliderModeEnabled` で有効状態を戻す。 |
| `setParagliderModeEnabledStateFromEditor(bool state)` | 値を設定してから `updateComponent` を呼ぶ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStateEnabled` | `UnityEvent` | – |
| `eventOnStateDisabled` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`disableExternalControllerState()`, `isBehaviorActive()`, `isCharacterOnGround()`, `setCurrentPlayerActionSystemCustomActionCategoryID()`, `setExternalForceActiveState(bool state)`, `updateControllerBehavior()`, `updateExternalForceActiveState(Vector3 forceDirection, float forceAmount)`

</details>
