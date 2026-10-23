# tutorialUISystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Tutorial System/tutorialUISystem.cs:5`

**概要**: チュートリアルのパネル・動画プレイヤー・音声・`tutorialInfo`リストを保持し、プレイヤー側チュートリアルシステムに参照を渡すUIコンポーネント。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tutorials Panel | `tutorialsPanel` | `Transform` | – | チュートリアルUIを表示するパネル。 |
| Video Audio Source | `videoAudioSource` | `AudioSource` | – | チュートリアル動画の音声を再生する`AudioSource`。 |
| Main Video Player Panel | `mainVideoPlayerPanel` | `Transform` | – | チュートリアル動画を再生する`VideoPlayer`のパネル。 |
| Main Player Tutorial System | `mainPlayerTutorialSystem` | `playerTutorialSystem` | – | 連携する`playerTutorialSystem`への参照。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `tutorialInfoList` | `List<tutorialInfo>` | new List<tutorialInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getTutorialsPanel()` | `tutorialsPanel`を返すだけ。 |
| `getVideoAudioSource()` | 動画用の`videoAudioSource`を返すだけ。 |
| `getMainVideoPlayerPanel()` | `mainVideoPlayerPanel`を返すだけ。 |
| `getTutorialInfoList()` | `tutorialInfoList`を返すだけ。 |
| `activateTutorialByName(string tutorialName)` | プレイヤー側システムにエディタ起動のフラグを立ててから、名前を指定してチュートリアルを起動する。 |
| `searchPlayerTutorialSystem()` | 未設定ならシーンから`playerTutorialSystem`を探し、見つかれば自身をUIシステムとして登録する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`でインスペクタ表示を更新するだけ。 |
