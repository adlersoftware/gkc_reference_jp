# moveObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Demo/moveObject.cs:4`

**概要**: `originalPosition`を基準に、`direction`・`speed`・`moveAmount`でコサイン波の往復移動をFixedUpdateで行うデモ用コンポーネント。`useLocalPosition`でローカル座標とワールド座標を切り替える。公開メソッドは移動の有効/無効の切り替えのみ。

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
| `enableMovement()` | `movementEnabled`をtrueにする`setMovementEnabledState`を呼ぶだけ。 |
| `disableMovement()` | `movementEnabled`をfalseにする`setMovementEnabledState`を呼ぶだけ。 |
| `setMovementEnabledState(bool state)` | 往復移動の実行を制御する`movementEnabled`に`state`を代入するだけ。 |
| `changeMovementEnabledState()` | `movementEnabled`を現在値の反転に切り替える。 |
