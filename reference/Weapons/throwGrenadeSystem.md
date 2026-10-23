# throwGrenadeSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/throwGrenadeSystem.cs:7`

**概要**: 投擲グレナードの所持数をHUDへ表示し、投擲開始と確定の入力でイベントを発火するシステム。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Throw Grenade Enabled | `throwGrenadeEnabled` | `bool` | true | – |
| Grenade Inventory Object Name | `grenadeInventoryObjectName` | `string` | "Grenade" | – |
| Check Inventory Info | `checkInventoryInfo` | `bool` | true | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Start Throw Grenade | `eventOnStartThrowGrenade` | `UnityEvent` | – | – |
| Event On Confirm Throw Grenade | `eventOnConfirmThrowGrenade` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grenade Info Panel | `grenadeInfoPanel` | `GameObject` | – | – |
| Grenade Amount Text | `grenadeAmountText` | `Text` | – | – |
| Main Inventory Manager | `mainInventoryManager` | `inventoryManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkGrenadesInfo()` | 投擲が有効なら所持数表示を更新し、無効なら`grenadeInfoPanel`を閉じる。 |
| `inputStartThrowGrenade()` | 所持数を確認し、0より多ければ`canConfirmThrowGrenade`を立てて開始イベントを発火する。 |
| `inputConfirmThrowGrenade()` | 確定可能なときだけ確定イベントを発火し、所持数表示を更新する。 |
| `updateGrenadeAmountText()` | インベントリからグレナード数を取り、負値を0にして`grenadeAmountText`へ表示する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartThrowGrenade` | `UnityEvent` | – |
| `eventOnConfirmThrowGrenade` | `UnityEvent` | – |
