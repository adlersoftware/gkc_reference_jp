# shieldSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/shieldSystem.cs:7`

**概要**: `useShield`と`shieldAmount`を保持し、被弾時のダメージ肩代わり、時間経過での自動回復、スライダーや`healthBarManager`への反映を行う。状態変化時には`eventOnStartShield`や`eventOnDamageShield`などのイベントを発火する。

**公式ドキュメント抜粋**（[Shield System](../../docs/player-controller-components/elements-used-by-other-components/shield-system.md)）

> Used to absorb the damage received by the character until its value reaches 0 and can be only refilled after x time without receiving damage or getting shield pickups on the scene, in a very similar way to borderlands games.

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Shield | `useShield` | `bool` | – | – |
| Max Shield Amount | `maxShieldAmount` | `float` | – | – |
| Shield Amount | `shieldAmount` | `float` | 100 | – |
| Regenerate Shield | `regenerateShield` | `bool` | – | – |
| Constant Shield Regenerate | `constantShieldRegenerate` | `bool` | – | – |
| Regenerate Shield Speed | `regenerateShieldSpeed` | `float` | 0 | – |
| Regenerate Shield Time | `regenerateShieldTime` | `float` | – | – |
| Regenerate Shield Amount | `regenerateShieldAmount` | `float` | – | – |
| Use Health Bar Manager | `useHealthBarManager` | `bool` | true | – |
| Shield Stat Name | `shieldStatName` | `string` | "Current Shield" | – |
| Max Shield Stat Name | `maxShieldStatName` | `string` | "Max Shield" | – |
| Main Manager Name | `mainManagerName` | `string` | "Health Bar Manager" | – |

### Shield Slider Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Shield Bar Panel Enabled | `showShieldBarPanelEnabled` | `bool` | true | – |
| Hide Slider When Not Damage Received | `hideSliderWhenNotDamageReceived` | `bool` | – | – |
| Time To Hide Slider After Damage | `timeToHideSliderAfterDamage` | `float` | – | – |
| Main Slider Parent | `mainSliderParent` | `RectTransform` | – | – |
| Hidden Slider Parent | `hiddenSliderParent` | `RectTransform` | – | – |
| Main Slider Transform | `mainSliderTransform` | `RectTransform` | – | – |

### Events Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Start Shield | `eventOnStartShield` | `UnityEvent` | – | – |
| Event On Damage Shield | `eventOnDamageShield` | `UnityEvent` | – | – |
| Event On Damage Shield With Attacker | `eventOnDamageShieldWithAttacker` | `eventParameters.eventToCallWithGameObject` | – | – |
| Event On Shield Destroyed | `eventOnShieldDestroyed` | `UnityEvent` | – | – |
| Event On Start Regenerate Shield | `eventOnStartRegenerateShield` | `UnityEvent` | – | – |
| Event To Check If Shield Is Active | `eventToCheckIfShieldIsActive` | `UnityEvent` | – | – |
| Event To Check If Shield Is Not Active | `eventToCheckIfShieldIsNotActive` | `UnityEvent` | – | – |
| Event To Check If Shield Is Destroyed | `eventToCheckIfShieldIsDestroyed` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shield Panel | `shieldPanel` | `GameObject` | – | – |
| Shield Slider | `shieldSlider` | `Slider` | – | – |
| Shield Slider Text | `shieldSliderText` | `Text` | – | – |
| Main Health | `mainHealth` | `health` | – | – |
| Health Bar Manager | `healthBarManager` | `healthBarManagementSystem` | – | – |
| Player Stats Manager | `playerStatsManager` | `playerStatsSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `startShieldComponents()` | `healthBarManager`を取得し、スライダー初期化と`eventOnStartShield`発火、`originalUseShield`保存を行う。 |
| `disableShield()` | `setUseShieldState(false)`を呼び出してシールドを無効化するだけ。 |
| `updateSliderState()` | 被弾から`regenerateShieldTime`経過後、継続なら速度×`deltaTime`、そうでなければ`regenerateShieldAmount`を加算する。 |
| `updateShieldSlider(float value)` | `shieldSlider`の値と表示を更新し、`healthBarManager`と`playerStatsManager`の値も更新する。 |
| `updateShieldSliderMaxValue(float newMaxValue)` | `shieldSlider.maxValue`と`healthBarManager`側の最大値を更新し、スライダー非表示の判定を再開する。 |
| `checkHideSliderParent()` | `hideSliderWhenNotDamageReceived`時に既存コルーチンを止め、時刻を記録して非表示用コルーチンを開始する。 |
| `getShield(float amount)` | `shieldAmount`に`amount`を加え最大値で制限し、0から回復したら`eventOnStartRegenerateShield`を発火する。 |
| `setDeadState(bool state)` | `dead`フラグを`state`に設定するだけ。 |
| `receiveDamage(float damageAmount, GameObject attacker)` | `useShield`かつ残量がある時だけダメージを肩代わりし、各イベント発火とスライダー更新後に`true`を返す。 |
| `getShieldAmountToLimit()` | `maxShieldAmount`から`auxShieldAmount`を引いた残りの受け入れ可能量を返すだけ。 |
| `addAuxShieldAmount(float amount)` | `auxShieldAmount`に`amount`を加算するだけ。 |
| `increaseMaxShieldAmount(float newAmount)` | `maxShieldAmount`に`newAmount`を加算し、スライダー最大値を更新する。 |
| `setShieldAmountOnMaxValue()` | `getShield`に最大値との差分を渡し、シールドを満タンにする。 |
| `increaseRegenerateShieldSpeed(float newAmount)` | `regenerateShieldSpeed`に`newAmount`を加算するだけ。 |
| `initializeShieldAmount(float newValue)` | `shieldAmount`を`newValue`で上書きするだけで、スライダーは更新しない。 |
| `initializeMaxShieldAmount(float newValue)` | `maxShieldAmount`を`newValue`で上書きするだけで、スライダーは更新しない。 |
| `initializeRegenerateShieldSpeed(float newValue)` | `regenerateShieldSpeed`を`newValue`で上書きするだけ。 |
| `increaseMaxShieldAmountByMultiplier(float amountMultiplier)` | `maxShieldAmount`に`amountMultiplier`を掛け、最大値・現在値・スライダー・統計値を更新する。 |
| `updateShieldAmountWithoutUpdatingStatManager(int statId, float amount)` | `shieldAmount`を`amount`にして内部スライダーと`auxShieldAmount`を更新し、`statId`は使用しない。 |
| `updateMaxShieldAmountWithoutUpdatingStatManager(int statId, float amount)` | `maxShieldAmount`を`amount`にして内部スライダーの最大値だけを更新し、`statId`は使用しない。 |
| `updateRegenerateShieldSpeedAmountWithoutUpdatingStatManager(int statId, float amount)` | `regenerateShieldSpeed`を`amount`にするだけで、`statId`は使用しない。 |
| `setUseShieldState(bool state)` | `useShield`を設定し、`showShieldBarPanelEnabled`なら`shieldPanel`の表示も切り替える。 |
| `setShowShieldBarPanelEnabledState(bool state)` | `showShieldBarPanelEnabled`を`state`に設定するだけ。 |
| `setOriginalUseShieldState()` | `startShieldComponents`で保存した`originalUseShield`を`setUseShieldState`に渡して戻す。 |
| `checkEventsForShieldState()` | `useShield`と`shieldAmount`に応じて有効・破壊・無効の3種類のイベントを撃ち分ける。 |
| `getCurrentShieldAmount()` | `shieldAmount`を返すだけ。 |
| `setShowShieldBarPanelEnabledStateFromEditor(bool state)` | 設定を変更した後、`GKC_Utils`でコンポーネントとシーンのダーティ更新を行う（エディタ用）。 |
| `setUseShieldStateFromEditor(bool state)` | `setUseShieldState`を呼んだ後、`GKC_Utils`でコンポーネントとシーンの更新を行う（エディタ用）。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartShield` | `UnityEvent` | – |
| `eventOnDamageShield` | `UnityEvent` | – |
| `eventOnShieldDestroyed` | `UnityEvent` | – |
| `eventOnStartRegenerateShield` | `UnityEvent` | – |
| `eventToCheckIfShieldIsActive` | `UnityEvent` | – |
| `eventToCheckIfShieldIsNotActive` | `UnityEvent` | – |
| `eventToCheckIfShieldIsDestroyed` | `UnityEvent` | – |
