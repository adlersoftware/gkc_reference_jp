# audioClipBip

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/Projectiles/audioClipBip.cs:6`

**概要**: ビープ音を時間経過でピッチと間隔を変えながら鳴らし続け、投射物などの警告音を担うコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Play Time | `playTime` | `float` | – | – |
| Play Rate | `playRate` | `float` | – | – |
| Increase Pitch Speed | `increasePitchSpeed` | `float` | – | – |
| Increase Play Rate Speed | `increasePlayRateSpeed` | `float` | – | – |
| Play Bip At Start | `playBipAtStart` | `bool` | true | – |
| Play Bip On Enable | `playBipOnEnable` | `bool` | – | – |
| Sound Clip | `soundClip` | `AudioClip` | – | – |
| Sound Clip Audio Element | `soundClipAudioElement` | `AudioElement` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Last Time Played | `lastTimePlayed` | `float` | – | – |
| Total Time Played | `totalTimePlayed` | `float` | – | – |
| Audio Played | `audioPlayed` | `bool` | – | – |
| Bip Activated | `bipActivated` | `bool` | – | – |
| Original Play Rate | `originalPlayRate` | `float` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `increasePlayTime(float extraTime)` | 未初期化なら初期化し、`playTime`を`extraTime`にして計測を開始し`bipActivated`を立てる。 |
| `disableBip()` | `bipActivated`を下ろし、ピッチ・再生間隔・最終再生時刻を初期値へ戻す。 |
