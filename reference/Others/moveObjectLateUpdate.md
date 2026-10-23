# moveObjectLateUpdate

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/moveObjectLateUpdate.cs:4`

**概要**: `LateUpdate`でコサイン波に沿ってオブジェクトを往復移動させる簡易コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Movement Enabled | `movementEnabled` | `bool` | true | – |
| Speed | `speed` | `float` | – | – |
| Move Amount | `moveAmount` | `float` | – | – |
| Direction | `direction` | `Vector3` | Vector3.up | – |
| Use Local Position | `useLocalPosition` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Original Position | `originalPosition` | `Vector3` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableMovement()` | `setMovementEnabledState(true)`を呼ぶだけ。 |
| `disableMovement()` | `setMovementEnabledState(false)`を呼ぶだけ。 |
| `setMovementEnabledState(bool state)` | `movementEnabled`に`state`を代入するだけ。 |
| `changeMovementEnabledState()` | `movementEnabled`を反転させて設定するだけ。 |
