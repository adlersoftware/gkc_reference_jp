# radioSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/Radio/radioSystem.cs:10`

**概要**: 曲リストと `AudioSource` を管理し、再生・停止・一時停止・次/前/ランダム曲・音量・スライダーと曲名表示を更新する。曲は `songsManager` から取得する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Radio Volume | `radioVolume` | `float` | – | – |
| Play Songs On Start | `playSongsOnStart` | `bool` | – | – |
| Play Songs On Active | `playSongsOnActive` | `bool` | – | – |
| Play Songs Randomly | `playSongsRandomly` | `bool` | – | – |
| Repeat List | `repeatList` | `bool` | – | – |
| Main Manager Name | `mainManagerName` | `string` | "Songs Manager" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Playing Song | `playingSong` | `bool` | – | – |
| Song Paused | `songPaused` | `bool` | – | – |
| Current Song Length | `currentSongLength` | `float` | – | – |
| Radio Active | `radioActive` | `bool` | – | – |
| Moving Song Lenght Slider | `movingSongLenghtSlider` | `bool` | – | – |
| Clips | `clips` | `List<AudioClip>` | new List<AudioClip> () | – |
| Audio Elements | `audioElements` | `List<AudioElement>` | new List<AudioElement> () | – |
| Current Index | `currentIndex` | `int` | 0 | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Volume Scrollbar | `volumeScrollbar` | `Scrollbar` | – | – |
| Current Song Name Text | `currentSongNameText` | `Text` | – | – |
| Song Lenght Slider | `songLenghtSlider` | `Slider` | – | – |
| Play Button | `playButton` | `GameObject` | – | – |
| Pause Button | `pauseButton` | `GameObject` | – | – |
| Song List Content | `songListContent` | `GameObject` | – | – |
| Song List Element Parent | `songListElementParent` | `GameObject` | – | – |
| Song List Element | `songListElement` | `GameObject` | – | – |
| Source | `source` | `AudioSource` | – | – |
| Main Songs Manager | `mainSongsManager` | `songsManager` | – | – |
| Current Song Audio Element | `_currentSongAudioElement` | `AudioElement` | new AudioElement () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `playCurrentSong()` | 再生中なら現在曲を再開し、未再生なら `PlayCurrent` で頭から再生して `songPaused` を解除する。 |
| `stopCurrentSong()` | 現在曲を停止し `playingSong` を偽にしてスライダーを 0 に戻す。 |
| `pauseCurrentSong()` | `songPaused` を真にして現在曲を一時停止するだけ。 |
| `setNextSong()` | 曲一覧が空なら何もせず、ランダムか次曲へ `currentIndex` を進めて再生する。 |
| `setPreviousSong()` | 曲一覧が空なら何もせず、前曲（先頭なら末尾）へ `currentIndex` を戻して再生する。 |
| `setRandomSong()` | ランダムに曲を選び直して再生する。 |
| `setRandomSongIndex()` | 現在と異なる曲番号を最大 100 回まで抽選して `currentIndex` に設定する。 |
| `setRadioVolume()` | `volumeScrollbar.value` を `radioVolume` と `AudioSource.volume` に反映する。 |
| `setPlaySongsRandomlyState(bool state)` | `playSongsRandomly` を `state` に設定するだけ。 |
| `setRepeatListState(bool state)` | `repeatList` を `state` に設定するだけ。 |
| `setMovingSongLenghtSliderState(bool state)` | 再生中のみ `movingSongLenghtSlider` を `state` に設定する。 |
| `setSongPart()` | 再生中にスライダー値×曲長の位置へ再生時間を移動する。 |
| `setRadioActiveState(bool state)` | `radioActive` を設定し、有効時は設定に応じ再生、無効時は停止して曲一覧を閉じる。 |
| `setOnlyRadioActiveState(bool state)` | `radioActive` を `state` に設定するだけ。 |
| `setPlayPauseButtonState(bool state)` | `playButton` と `pauseButton` の表示を `state` に応じ切替えるだけ。 |
| `selectSongOnList(GameObject songButtonPressed)` | ボタンのテキストに一致する曲を探して `currentIndex` を設定し再生する。 |
| `getSongsList()` | `songsManager` から曲一覧を取得し、曲名のリスト要素を生成して並べる。 |
