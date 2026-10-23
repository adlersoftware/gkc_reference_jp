# jetpackSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `externalControllerBehavior`
- **ソース**: `Player/Extra Movements/jetpackSystem.cs:7`

**概要**: `externalControllerBehavior` を継承したジェットパック用モード。装備/使用状態、燃料、ターボ、推力パーティクル、IK、カメラFOV、HUD表示を一括して制御する。

## インスペクター設定

### Main Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Jetpack Enabled | `jetpackEnabled` | `bool` | – | – |
| Jetpack Force | `jetpackForce` | `float` | – | – |
| Jetpack Air Speed | `jetpackAirSpeed` | `float` | – | – |
| Jetpack Air Control | `jetpackAirControl` | `float` | – | – |
| Turbo Enabled | `turboEnabled` | `bool` | true | – |
| Jetpack Turbo Horizontal Speed | `jetpackTurboHorizontalSpeed` | `float` | 5 | – |
| Jetpack Turbo Vertical Speed | `jetpackTurboVerticalSpeed` | `float` | 5 | – |
| Use Force Mode | `useForceMode` | `bool` | – | – |
| Force Mode | `forceMode` | `ForceMode` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disable Jetpack Mesh When Not Equipped | `disableJetpackMeshWhenNotEquipped` | `bool` | true | – |
| Jetpack Horizontal Speed On Aim Multiplier | `jetpackHorizontalSpeedOnAimMultiplier` | `float` | 0.5f | – |
| Jetpack Vertical Speed On Aim Multiplier | `jetpackVerticalSpeedOnAimMultiplier` | `float` | 0.5f | – |
| Shake Camera State Name | `shakeCameraStateName` | `string` | "Use Jetpack Turbo" | – |
| Use Custom Jetpack Up Direction | `useCustomJetpackUpDirection` | `bool` | – | – |
| Custom Jetpack Up Direction | `customJetpackUpDirection` | `Transform` | – | – |
| Used By AI | `usedByAI` | `bool` | – | – |

### Fuel Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Jetpack Fuel Amount | `jetpackFuelAmount` | `float` | – | – |
| Jetpack Fuel Rate | `jetpackFuelRate` | `float` | – | – |
| Regenerative Speed | `regenerativeSpeed` | `float` | – | – |
| Time To Regenerate | `timeToRegenerate` | `float` | – | – |

### Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Jetpack Animation | `useJetpackAnimation` | `bool` | true | – |
| Jetpack Mode Name | `jetpackModeName` | `string` | "Jetpack Mode" | – |
| Regular Air ID | `regularAirID` | `int` | -1 | – |
| Jetpack ID | `jetpackID` | `int` | 2 | – |
| Use IK Jetpack | `useIKJetpack` | `bool` | – | – |
| Animation Name | `animationName` | `string` | – | – |

### Particles Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Thrusts Particles | `thrustsParticles` | `List<ParticleSystem>` | new List<ParticleSystem> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Jet Pack Equiped | `jetPackEquiped` | `bool` | – | – |
| Using Jetpack | `usingJetpack` | `bool` | – | – |
| Turbo Active | `turboActive` | `bool` | – | – |
| Jetpack Mode Paused | `jetpackModePaused` | `bool` | – | – |

### Event Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Start Using Jetpack | `eventOnStartUsingJetpack` | `UnityEvent` | – | – |
| Event On Stop Using Jetpack | `eventOnStopUsingJetpack` | `UnityEvent` | – | – |
| Event On State Enabled | `eventOnStateEnabled` | `UnityEvent` | – | – |
| Event On State Disabled | `eventOnStateDisabled` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Jetpack | `jetpack` | `GameObject` | – | – |
| Jetpack HUD Info | `jetpackHUDInfo` | `GameObject` | – | – |
| Jetpack Slider | `jetpackSlider` | `Slider` | – | – |
| Fuel Amount Text | `fuelAmountText` | `Text` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Jet Pack Animation | `jetPackAnimation` | `Animation` | – | – |
| IK Manager | `IKManager` | `IKSystem` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `canUseJetpack()` | 燃料が残っており、かつ `jetpackModePaused` が false のときだけ true を返す。 |
| `startOrStopJetpack(bool state)` | `usingJetpack` を切り替え、アニメ、外部コントローラ、パーティクル、IK、airID、イベント、ターボ解除を更新する。 |
| `changeThrustsParticlesState(bool state)` | 推力パーティクルを state に応じて再生し、停止時は loop を false にする。 |
| `enableOrDisableJetpack(bool state)` | 装備状態を切り替え、HUD/メッシュ、外部コントローラ、イベントを更新し、解除時は使用中なら停止する。 |
| `getJetpackFuel(float amount)` | 燃料を加算して最大値でクランプし、UIとスライダーを更新する。 |
| `getJetpackFuelAmountToPick()` | スライダー最大値から現在の燃料を引いた残量を返す。 |
| `enableOrDisableJetPackMesh(bool state)` | `jetpack` メッシュの表示を切り替え、未装備時は非表示設定を優先する。 |
| `removeJetpackMesh()` | `jetpack` オブジェクトを `DestroyImmediate` で削除する。 |
| `setUsedByAIState(bool state)` | `usedByAI` を設定するだけ。 |
| `enableOrDisableTurbo(bool state)` | ターボ状態を設定し、カメラFOVとシェイク、空中速度IDを切り替える。 |
| `setJetpackEnabledState(bool state)` | 装備中なら解除してから `jetpackEnabled` を設定する。 |
| `setOriginalJetpackEnabledState()` | 保存値 `originalJetpackEnabled` を `setJetpackEnabledState` に渡すだけ。 |
| `setJetpackModePausedState(bool state)` | true かつ使用中なら停止し、`jetpackModePaused` を設定する。 |
| `inputStartOrStopJetpack(bool state)` | 装備中・非運転・使用可能の条件を満たすとき `startOrStopJetpack` を呼ぶ。 |
| `inputChangeTurboState(bool state)` | 装備中・使用中・ターボ有効なら、エイム中は保留フラグを立て、それ以外は `enableOrDisableTurbo` を呼ぶ。 |
| `setJetpackEnabledStateFromEditor(bool state)` | `setJetpackEnabledState` を呼んだ後に `updateComponent` を実行する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartUsingJetpack` | `UnityEvent` | – |
| `eventOnStopUsingJetpack` | `UnityEvent` | – |
| `eventOnStateEnabled` | `UnityEvent` | – |
| `eventOnStateDisabled` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`disableExternalControllerState()`, `setCurrentPlayerActionSystemCustomActionCategoryID()`, `updateControllerBehavior()`

</details>
