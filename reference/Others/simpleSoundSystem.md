# simpleSoundSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/simpleSoundSystem.cs:6`

**概要**: カテゴリ別の効果音リストからランダムに1つ選んで再生する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sounds Enabled | `soundsEnabled` | `bool` | true | – |

### Sound List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sound Category Info List | `soundCategoryInfoList` | `List<soundCategoryInfo>` | new List<soundCategoryInfo> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `playRandomSound()` | `soundsEnabled`が`true`の時、ランダムなカテゴリと音を選んで`AudioPlayer.PlayOneShot`で再生する。 |
| `playRandomSoundFromCategoryByName(string categoryName)` | `categoryName`一致のカテゴリからランダムな音を選んで再生し、見つからなければ何もしない。 |

## 内部型

- `soundCategoryInfo`（class）
- `soundInfo`（class）
