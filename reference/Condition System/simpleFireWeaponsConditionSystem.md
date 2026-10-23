# simpleFireWeaponsConditionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Condition System/simpleFireWeaponsConditionSystem.cs:6`

**概要**: `IKWeaponSystem`の状態(エイム中、一人称/三人称、フルボディアウェアネス、現在武器)から条件結果を判定し、完了/未完了イベントを実行する。`conditionResultCompleteIfAnyConditionTrue`でカメラ/エイム系条件のANDとORを切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Condition Check Enabled | `conditionCheckEnabled` | `bool` | – | – |
| Check If Current Weapon | `checkIfCurrentWeapon` | `bool` | – | – |
| Check If Aiming Weapon | `checkIfAimingWeapon` | `bool` | – | – |
| Check If Third Person Active | `checkIfThirdPersonActive` | `bool` | – | – |
| Check If First Person Active | `checkIfFirstPersonActive` | `bool` | – | – |
| Check If Full Body Awareness Active | `checkIfFullBodyAwarenessActive` | `bool` | – | – |
| Condition Result Complete If Any Condition True | `conditionResultCompleteIfAnyConditionTrue` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Condition Complete | `eventOnConditionComplete` | `UnityEvent` | – | – |
| Event On Condition Not Complete | `eventOnConditionNotComplete` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main IK Weapon System | `mainIKWeaponSystem` | `IKWeaponSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkIfConditionComplete()` | `conditionCheckEnabled`がfalseならreturnし、内部計算した条件結果を`setConditionResult`へ渡す。 |
| `setConditionResult(bool state)` | デバッグ出力後、`state`に応じて完了または未完了のイベントをInvokeするだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnConditionComplete` | `UnityEvent` | – |
| `eventOnConditionNotComplete` | `UnityEvent` | – |
