# tutorialActivatorSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Tutorial System/tutorialActivatorSystem.cs:5`

**概要**: 名前を指定してチュートリアルを起動する小さなコンポーネントで、有効フラグと名前に付ける接尾辞を持つ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tutorial Enabled | `tutorialEnabled` | `bool` | true | – |
| Tutorial Name | `tutorialName` | `string` | – | – |
| Extra String | `extraString` | `string` | "Controls" | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateTutorial(GameObject newPlayer)` | 有効時、`tutorialName`と`extraString`を繋いだ名前で起動を依頼する（`newPlayer`は未使用）。 |
| `setTutorialEnabledState(bool state)` | `tutorialEnabled`フラグを設定するだけ。 |
