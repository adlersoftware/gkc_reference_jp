# filesChecker

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/filesChecker.cs:6`

**概要**: エディタ用のプリファブ検査ツールで、指定パス以下のプレファブの位置・回転・スケールやAudioSourceを確認する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Prefabs Path | `prefabsPath` | `string` | "Assets/Game Kit Controller/Prefabs/I… | – |
| Show Object List Info Print | `showObjectListInfoPrint` | `bool` | – | – |
| Show Only Uncentererd Info | `showOnlyUncentererdInfo` | `bool` | – | – |
| Show Unscaled Print | `showUnscaledPrint` | `bool` | – | – |
| Search On Sub Folders | `searchOnSubFolders` | `bool` | – | – |
| Reset Transform Values | `resetTransformValues` | `bool` | – | – |
| Reset Scale Values | `resetScaleValues` | `bool` | – | – |
| Check For Audio Source | `checkForAudioSource` | `bool` | – | – |
| Show Only MP3 Source | `showOnlyMP3Source` | `bool` | – | – |
| Check Sound Name | `checkSoundName` | `bool` | – | – |
| Sound Name To Check | `soundNameToCheck` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkPrefabs()` | `prefabsPath`以下の`.prefab`を読み込み、中心位置やスケールのずれ、AudioSourceのクリップ情報を集計して出力する。 |
