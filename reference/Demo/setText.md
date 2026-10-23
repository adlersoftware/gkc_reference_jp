# setText

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Demo/setText.cs:5`

**概要**: `Text`/`TextMesh`の文字列を看板メッシュに反映し、プレイヤーがトリガー内にいる間だけ`MeshRenderer`を表示するデモ用コンポーネント。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Editing Text | `editingText` | `bool` | – | – |
| Show Gizmo | `showGizmo` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getmainMeshRendererComponent()` | `mainMeshRenderer`がnullの時だけ`GetComponent<MeshRenderer>()`で取得して保持する。 |
