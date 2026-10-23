# bowHolderSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/bowHolderSystem.cs:6`

**概要**: 弓の装着位置を持ち、矢の装填・射撃・照準開始終了などのタイミングでUnityEventを発火するハブ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Bow Weapon ID | `bowWeaponID` | `int` | – | – |
| Can Use Multiple Arrow Type | `canUseMultipleArrowType` | `bool` | – | – |
| Bow Weapon ID List | `bowWeaponIDList` | `List<int>` | new List<int> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Load Arrow | `eventOnLoadArrow` | `UnityEvent` | – | – |
| Event On Fire Arrow | `eventOnFireArrow` | `UnityEvent` | – | – |
| Event On Start Aim | `eventOnStartAim` | `UnityEvent` | – | – |
| Event On End Aim | `eventOnEndAim` | `UnityEvent` | – | – |
| Event On Cancel Bow Action | `eventOnCancelBowAction` | `UnityEvent` | – | – |
| Event On Max Pull Bow Multiplier Start | `eventOnMaxPullBowMultiplierStart` | `UnityEvent` | – | – |
| Event On Max Pull Bow Multiplier End | `eventOnMaxPullBowMultiplierEnd` | `UnityEvent` | – | – |

### Debug Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkEventOnLoadArrow()` | `eventOnLoadArrow`を発火し、デバッグ時のみログを出す。 |
| `checkEventOnFireArrow()` | `eventOnFireArrow`を発火し、デバッグ時のみログを出す。 |
| `checkEventOnStartAim()` | `eventOnStartAim`を発火し、デバッグ時のみログを出す。 |
| `checkEventOnEndAim()` | `eventOnEndAim`を発火し、デバッグ時のみログを出す。 |
| `checkEventOnCancelBowAction()` | `eventOnCancelBowAction`を発火し、デバッグ時のみログを出す。 |
| `checkEventOnMaxPullBowMultiplierStart()` | `eventOnMaxPullBowMultiplierStart`を発火し、デバッグ時のみログを出す。 |
| `checkEventOnMaxPullBowMultiplierEnd()` | `eventOnMaxPullBowMultiplierEnd`を発火し、デバッグ時のみログを出す。 |
| `getBowWeaponID()` | `bowWeaponID`を返すだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnLoadArrow` | `UnityEvent` | – |
| `eventOnFireArrow` | `UnityEvent` | – |
| `eventOnStartAim` | `UnityEvent` | – |
| `eventOnEndAim` | `UnityEvent` | – |
| `eventOnCancelBowAction` | `UnityEvent` | – |
| `eventOnMaxPullBowMultiplierStart` | `UnityEvent` | – |
| `eventOnMaxPullBowMultiplierEnd` | `UnityEvent` | – |
