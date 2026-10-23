# rotateObjectWithRegularUpdate

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/rotateObjectWithRegularUpdate.cs:6`

**概要**: `Update`で毎フレーム`mainTransform`を`speed`と`direccion`に従って回転させ、停止や回転リセットも提供するコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Direccion | `direccion` | `Vector3` | – | – |
| Speed | `speed` | `float` | 1 | – |
| Rotation Enabled | `rotationEnabled` | `bool` | true | – |
| Reset Rotation Speed | `resetRotationSpeed` | `float` | 5 | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Transform | `mainTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableRotation()` | `rotationEnabled`を反転するだけ。 |
| `increaseRotationSpeedTenPercentage()` | `speed`を現在値の1.1倍に増やすだけ。 |
| `setRotationEnabledState(bool state)` | 回転リセットのコルーチンを止めてから`rotationEnabled`を`state`にする。 |
| `disableRotation()` | `setRotationEnabledState(false)`を呼ぶだけ。 |
| `enableRotation()` | `setRotationEnabledState(true)`を呼ぶだけ。 |
| `resetRotation()` | 回転コルーチンを止め、向きを`Quaternion.identity`へ補間するコルーチンを開始する。 |
| `stopRotation()` | 実行中の`rotationCoroutine`があれば停止するだけ。 |
| `setRandomDirectionToCurrent()` | `direccion`にランダムで+1か-1を掛けて回転方向を反転または維持する。 |
| `setNewRotationSpeed(float newValue)` | `speed`を`newValue`にするだけ。 |
| `setEnabledState(bool state)` | コンポーネントの`enabled`を`state`にするだけ。 |
