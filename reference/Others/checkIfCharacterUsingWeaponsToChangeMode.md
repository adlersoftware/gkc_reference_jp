# checkIfCharacterUsingWeaponsToChangeMode

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/checkIfCharacterUsingWeaponsToChangeMode.cs:6`

**概要**: プレイヤーが武器を使用しているかをコルーチンで監視し、状態変化に応じてモード切替のイベントを扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check State Enabled | `checkStateEnabled` | `bool` | true | – |
| Check State At Start Enabled | `checkStateAtStartEnabled` | `bool` | – | – |
| Min Time To Call Events On No Carrying Weapons | `minTimeToCallEventsOnNoCarryingWeapons` | `float` | – | – |
| Check State If Not Aiming Fire Weapons | `checkStateIfNotAimingFireWeapons` | `bool` | – | – |
| Check State If Not Using Melee Attack | `checkStateIfNotUsingMeleeAttack` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Carrying Weapons | `carryingWeapons` | `bool` | – | – |
| Not Carrying Weapons Event Called | `notCarryingWeaponsEventCalled` | `bool` | – | – |
| Coroutine Active | `coroutineActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Not Carrying Weapons | `eventOnNotCarryingWeapons` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateCheck()` | `checkStateEnabled`が`true`の時、既存コルーチンを止めて監視コルーチンを開始し`coroutineActive`を立てる。 |
| `stopCheck()` | `checkStateEnabled`が`true`の時、監視コルーチンを停止する。 |
| `stopUpdateCheckCoroutine()` | 実行中ならコルーチンを止め、`carryingWeapons`などのフラグと`coroutineActive`をリセットする。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnNotCarryingWeapons` | `UnityEvent` | – |
