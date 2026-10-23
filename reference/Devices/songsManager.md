# songsManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/Radio/songsManager.cs:11`

**概要**: フォルダ内の音声ファイルと内部リストを読み込み、ラジオ用の曲リストを提供するシングルトン管理。

**公式ドキュメント抜粋**（[Songs Manager](../../docs/additional-managers/songs-manager.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Load Sounds In Folder Enabled | `loadSoundsInFolderEnabled` | `bool` | true | – |
| Absolute Path Build | `absolutePathBuild` | `string` | "." | – |
| Absolute Path Editor | `absolutePathEditor` | `string` | "Music" | – |
| Valid Extensions | `validExtensions` | `List<string>` | new List<string> { ".ogg", ".wav" } | – |

### Internal Songs List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Internal Songs List | `useInternalSongsList` | `bool` | – | – |
| Internal Clips | `internalClips` | `List<AudioClip>` | new List<AudioClip> () | – |
| Internal Audio Elements | `internalAudioElements` | `List<AudioElement>` | new List<AudioElement> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Songs Loaded | `songsLoaded` | `bool` | – | – |
| Clips | `clips` | `List<AudioClip>` | new List<AudioClip> () | – |
| Audio Elements | `audioElements` | `List<AudioElement>` | new List<AudioElement> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Game System Manager | `gameSystemManager` | `gameManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 初期化済みなら何もせず、重複インスタンスは破棄、それ以外は静的参照を自身に設定する。 |
| `getSongsList()` | `audioElements`を返すだけ。 |
| `allSongsLoaded()` | `songsLoaded`を返すだけ。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |
