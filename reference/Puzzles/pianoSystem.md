# pianoSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Puzzles/pianoSystem.cs:7`

**概要**: 鍵盤を名前で識別して発音と押下アニメーションを行い、曲データの自動演奏もできるコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Key Rotation Amount | `keyRotationAmount` | `int` | 30 | – |
| Key Rotation Speed | `keyRotationSpeed` | `float` | 30 | – |
| Song To Play | `songToPlay` | `string` | – | TextArea (1, 10) |
| Play Rate | `playRate` | `float` | 0.3f | – |
| Song Line Length | `songLineLength` | `int` | – | – |
| Song Line Delay | `songLineDelay` | `float` | – | – |

### Key Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Key Info List | `keyInfoList` | `List<keyInfo>` | new List<keyInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Using Piano | `usingPiano` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event When Auto Play Song Ends | `useEventWhenAutoPlaySongEnds` | `bool` | – | – |
| Event When Auto Play Song Ends | `eventWhenAutoPlaySongEnds` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `autoPlaySong()` | `songToPlay`を`playSong`へ渡すだけ。 |
| `playSong(string songNotes)` | 既存の演奏コルーチンを止め、`songNotes`を再生するコルーチンを開始する。 |
| `checkPressedKey(string keyName)` | ピアノ使用中なら`keyName`に一致する鍵の音を鳴らして回転させる。 |
| `rotatePressedKey(keyInfo currentKeyInfo)` | 対象鍵の既存コルーチンを止め、押下回転のコルーチンを開始する。 |
| `playSound(AudioElement clipSound)` | `clipSound`がnullでなければ`AudioPlayer`で一度だけ再生する。 |
| `startOrStopUsingPiano()` | 使用状態を反転させるだけ。 |
| `setUsingPianoState(bool state)` | 使用フラグを設定し、使用開始時は`AudioSource`の有無を確認する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventWhenAutoPlaySongEnds` | `UnityEvent` | – |

## 内部型

- `keyInfo`（class）
