# windOnObjectState

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/windOnObjectState.cs:5`

**概要**: オブジェクトが風を受けている状態と、その風向き・風力を保持する小さな状態クラス。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Wind Detect Enabled | `windDetectEnabled` | `bool` | true | – |
| Wind Direction | `windDirection` | `Vector3` | – | – |
| Wind Force | `windForce` | `float` | – | – |
| Ignore Apply Other Forces On Object | `ignoreApplyOtherForcesOnObject` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Wind Detected | `windDetected` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setWindDetectedState(bool state)` | `windDetectEnabled`が`true`の時だけ`windDetected`を`state`に更新する。 |
| `setWindDirectionValues(Vector3 newValues)` | `windDirection`に`newValues`を代入するだけ。 |
| `setWindForceValue(float newValue)` | `windForce`に`newValue`を代入するだけ。 |
| `isWindDetected()` | `windDetected`の値をそのまま返すだけ。 |
| `getwindDirection()` | `windDetected`が`true`なら`windDirection`、そうでなければ`Vector3.zero`を返す。 |
| `getWindForce()` | `windDetected`が`true`なら`windForce`、そうでなければ0を返す。 |
