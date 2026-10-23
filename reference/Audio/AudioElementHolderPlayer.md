# AudioElementHolderPlayer

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **namespace**: `GameKitController.Audio`
- **ソース**: `Audio/AudioElementHolderPlayer.cs:5`

**概要**: `AudioElementHolder`への参照を持ち、再生・停止などの呼び出しをそのまま転送するラッパー。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Audio Element Holder | `audioElementHolder` | `AudioElementHolder` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `Play()` | `audioElementHolder.Play`を呼ぶだけ。 |
| `PlayOneShot(float volumeScale)` | `volumeScale`を渡して`audioElementHolder.PlayOneShot`を呼ぶ。 |
| `PlayOneShot()` | 音量1.0で`audioElementHolder.PlayOneShot`を呼ぶ。 |
| `Stop()` | `audioElementHolder.Stop`を呼ぶだけ。 |
| `Pause()` | `audioElementHolder.Pause`を呼ぶだけ。 |
| `UnPause()` | `audioElementHolder.UnPause`を呼ぶだけ。 |
