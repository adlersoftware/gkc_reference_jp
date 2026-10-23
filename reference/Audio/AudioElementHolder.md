# AudioElementHolder

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **namespace**: `GameKitController.Audio`
- **ソース**: `Audio/AudioElementHolder.cs:5`

**概要**: `AudioElement`を1つ保持し、`AudioPlayer`の静的APIへ再生・停止などを委譲するコンポーネント。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Audio Element | `audioElement` | `AudioElement` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `Play()` | `audioElement`を`AudioPlayer.Play`で再生する。 |
| `PlayOneShot(float volumeScale)` | `audioElement`を`volumeScale`の音量で`PlayOneShot`再生する。 |
| `PlayOneShot()` | 音量1.0で`PlayOneShot`を呼ぶ。 |
| `Stop()` | `AudioPlayer.Stop`で`audioElement`を停止する。 |
| `Pause()` | `AudioPlayer.Pause`で`audioElement`を一時停止する。 |
| `UnPause()` | `AudioPlayer.UnPause`で`audioElement`の再生を再開する。 |
