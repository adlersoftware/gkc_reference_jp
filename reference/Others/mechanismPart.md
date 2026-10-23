# mechanismPart

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/mechanismPart.cs:4`

**概要**: 歯車機構の回転パーツで、速度・回転の有効状態・歯車の装着状態を保持して`Update`で回す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Enable Rotation | `enableRotation` | `bool` | – | – |
| Mechanim Type | `mechanimType` | `int` | – | – |
| Rotate Direction | `rotateDirection` | `Vector3` | – | – |
| Rotation Speed | `rotationSpeed` | `float` | 10 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Gear Activated | `gearActivated` | `bool` | – | – |
| Rotatory Gear Engaged | `rotatoryGearEngaged` | `bool` | – | – |

### Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Rotor | `rotor` | `GameObject` | – | – |
| Gear | `gear` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setVelocity(float v)` | `rotationSpeed`に`v`を代入するだけ。 |
| `setEnableRotationState(bool state)` | `enableRotation`に`state`を代入するだけ。 |
| `setGearActivatedState(bool state)` | `gearActivated`を`state`にし、`gear`の`rotatoryGear`へ回転有効を伝えてタグを`box`に変える。 |
