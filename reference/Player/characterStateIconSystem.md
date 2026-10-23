# characterStateIconSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/characterStateIconSystem.cs:6`

**概要**: キャラクターの状態に応じて、一人称/三人称用のアイコン表示と効果音を切り替えるコンポーネント。状態名から該当エントリを探して表示を更新する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| States Enabled | `statesEnabled` | `bool` | true | – |
| Use Icons Only On Screen | `useIconsOnlyOnScreen` | `bool` | – | – |

### Character States List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character State Info List | `characterStateInfoList` | `List<characterStateInfo>` | new List<characterStateInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Character State Name | `currentCharacterStateName` | `string` | – | – |
| Current Character State | `currentCharacterState` | `characterStateInfo` | – | – |
| Hide After Time | `hideAfterTime` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableCharacterIcon(characterStateInfo characterState, bool state)` | 状態有効時、一人称・デバイス使用・画面表示設定に応じて一人称/三人称アイコンの `SetActive` を切り替える。 |
| `checkCharacterStateIconForViewChange()` | 三人称アイコンがあれば現在状態で表示更新を呼ぶ。 |
| `setCharacterStateIcon(string stateName)` | 名前一致の状態を探して他を非表示にし、対象を表示して時間非表示と効果音を設定する。 |
| `disableCharacterStateIcon()` | 全状態のアイコンを非表示にし、`currentCharacterStateName` を空にする。 |
| `playSound(AudioElement sound)` | `sound` が null でなければ `AudioPlayer.PlayOneShot` で再生する。 |
| `enableOrDisableCharacterStateSound(bool state, string characterStateName)` | 名前一致の状態の `useSound` を state に設定する。 |
| `enableCharacterStateSound(string characterStateName)` | `enableOrDisableCharacterStateSound(true, ...)` を呼ぶだけ。 |
| `disableCharacterStateSound(string characterStateName)` | `enableOrDisableCharacterStateSound(false, ...)` を呼ぶだけ。 |
| `enableCharacterStateSoundFromEditor(string characterStateName)` | 効果音を有効にしてから `updateComponent` を呼ぶ。 |
| `disableCharacterStateSoundFromEditor(string characterStateName)` | 効果音を無効にしてから `updateComponent` を呼ぶ。 |

## 内部型

- `characterStateInfo`（class）
