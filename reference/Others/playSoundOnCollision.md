# playSoundOnCollision

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/playSoundOnCollision.cs:5`
- **属性**: `RequireComponent (typeof(AudioElementHolder))`

**概要**: 衝突時に効果音を再生し、最低速度を条件にできる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Min Speed For Sound | `useMinSpeedForSound` | `bool` | – | – |
| Min Speed For Sound | `minSpeedForSound` | `float` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |
| Audio Element Holder | `audioElementHolder` | `AudioElementHolder` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `playSound()` | `audioElementHolder`とその`audioElement`がnullでなければ`AudioPlayer.Play`で音を再生する。 |
