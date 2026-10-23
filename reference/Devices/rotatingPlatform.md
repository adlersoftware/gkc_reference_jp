# rotatingPlatform

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/rotatingPlatform.cs:5`

**概要**: 指定軸・角度・速度で回転を繰り返す足場。1回転後に`rotationDelay`だけ待って再び回り始める。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Rotation Active | `rotationActive` | `bool` | true | – |
| Rotation Speed | `rotationSpeed` | `float` | – | – |
| Rotation Delay | `rotationDelay` | `float` | – | – |
| Rotation Amount | `rotationAmount` | `float` | – | – |
| Rotation Axis | `rotationAxis` | `Vector3` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `rotatePlatform()` | 既存の回転コルーチンを止め、回転コルーチンを開始する。 |
| `stopRotationCoroutine()` | 実行中の回転コルーチンを止めるだけ。 |
| `setRotationActiveState(bool state)` | `rotationActive`を設定し、有効なら回転を開始、無効ならコルーチンを停止する。 |
