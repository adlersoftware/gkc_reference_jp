# tagLayerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/tagLayerSystem.cs:8`

**概要**: Unityエディタ専用（`#if UNITY_EDITOR`）で、ProjectSettings/TagManagerのタグとレイヤーを追加・削除し、一覧を再取得する補助コンポーネント。

**公式ドキュメント抜粋**（[Tag Layer System](../../docs/toplevelcomponents/player-and-game-management/tag-layer-system.md)）

> 

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Tag Manager

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| New Tag To Add | `newTag` | `string` | – | 入力した名前のタグをプロジェクトのタグ一覧へ追加する。 / 表示条件: `tagMenu` がオンのとき |

### Layer Manager

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Min Layer Index To Check | `minLayerIndexToCheck` | `int` | 8 | レイヤー一覧で扱う最小インデックス。既定は8のユーザー領域。 / 表示条件: `layerMenu` がオンのとき |
| New Layer To Add | `newLayer` | `string` | – | 空いているレイヤースロットへ新しいレイヤーを追加する。 / 表示条件: `layerMenu` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `tagList` | `List<string>` | new List<string> () | – |
| `layerList` | `List<string>` | new List<string> () | – |
| `temporalTagList` | `List<string>` | new List<string> () | – |
| `temporalLayerList` | `List<string>` | new List<string> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `addTag(string tagToAdd)` | TagManagerに未登録なら`tagToAdd`をタグに追加し、`tagList`を再取得してエディタを更新する。 |
| `removeTag(string tagToRemove)` | `tagToRemove`と同名のタグをTagManagerから削除し、`tagList`を再取得してエディタを更新する。 |
| `addTagList(List<string> tagListToAdd)` | `tagListToAdd`の各要素を`addTag`で追加した後、エディタを更新する。 |
| `addCurrentTagList()` | `tagList`を`temporalTagList`に複製し、`addTagList`でまとめて追加する。 |
| `getTagList()` | `tagList`を空にしてTagManagerのタグ名を全件詰め直し、エディタを更新する。 |
| `addLayer(string layerToAdd)` | 8番目以降の空きレイヤー枠に`layerToAdd`を書き込み、`layerList`を再取得して更新する。 |
| `removeLayer(string layerToRemove)` | `layerToRemove`と同名のレイヤーをTagManagerから削除し、`layerList`を再取得して更新する。 |
| `addLayerList(List<string> layerListToAdd)` | 8番目以降の枠へ`layerListToAdd`を順番に上書きし、`layerList`を再取得して更新する。 |
| `addCurrentLayerList()` | `layerList`を`temporalLayerList`に複製し、`addLayerList`でまとめて書き込む。 |
| `getLayerList()` | `layerList`を空にし、8番目以降のレイヤー名を詰め直してエディタを更新する。 |
| `updateEditor()` | `GKC_Utils.updateComponent`でこのコンポーネントのインスペクタ表示を更新するだけ。 |
