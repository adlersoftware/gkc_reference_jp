# playerStealthSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `abilityInfo`
- **ソース**: `Abilities System/Custom Abilities/playerStealthSystem.cs:6`

**概要**: ステルスモードの状態と制限時間を管理するアビリティ。状態変化をイベントで通知し、時間切れで自動解除する。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Stealth Mode Enabled | `stealthModeEnabled` | `bool` | true | – |
| Stealth Mode Active | `stealthModeActive` | `bool` | – | – |
| Event To Activate Stealth Mode | `eventToActivateStealthMode` | `UnityEvent` | – | – |
| Event To Deactivate Stealth Mode | `eventToDeactivateStealthMode` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setStealthModeState(bool state)` | `stealthModeEnabled` なら `stealthModeActive` を更新し、有効・無効に応じたイベントを発火する。 |
| `stopSetStealthModeTimeLimit()` | `timeLimitCoroutine` が動いていれば停止する。 |
| `setStealthModeTimeLimit()` | 既存の制限時間コルーチンを止め、`timeLimit` 後にステルスを解除するコルーチンを開始する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToActivateStealthMode` | `UnityEvent` | – |
| `eventToDeactivateStealthMode` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`activateSecondaryActionOnAbility()`, `deactivateAbility()`, `disableAbility()`, `enableAbility()`, `updateAbilityState()`, `useAbilityPressDown()`, `useAbilityPressHold()`, `useAbilityPressUp()`

</details>
