# playSoundOnTriggerEnter

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/playSoundOnTriggerEnter.cs:6`

**概要**: トリガー進入時に一度だけ効果音を再生する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sound To Play | `soundToPlay` | `AudioClip` | – | – |
| Sound To Play Audio Element | `soundToPlayAudioElement` | `AudioElement` | – | – |
| Tag List To Check | `tagListToCheck` | `List<string>` | new List<string> () | – |
| Playing Sound | `playingSound` | `bool` | – | – |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |
| Use Event Trigger System | `useEventTriggerSystem` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `playSound()` | 再生中でなければ`AudioPlayer.PlayOneShot`で`soundToPlayAudioElement`を鳴らし、`playingSound`を立てる。 |
