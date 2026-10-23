# setObjectParentSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/setObjectParentSystem.cs:5`

**概要**: 子オブジェクトのリストを指定した親Transformへ付け替える（開始時の自動実行にも対応）。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Parent Transform | `parentTransform` | `Transform` | – | – |
| Reset Child Local Position | `resetChildLocalPosition` | `bool` | – | – |
| Set Parent On Start | `setParentOnStart` | `bool` | – | – |
| Set Null Parent | `setNullParent` | `bool` | – | – |

### Child List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Child List | `childList` | `List<Transform>` | new List<Transform> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setObjectsParent()` | `parentTransform`があれば`childList`をその子にし、必要ならローカル位置を0に、親が無く`setNullParent`なら親を外す。 |
| `setParentTransform(Transform newTransform)` | `parentTransform`に`newTransform`を代入するだけ。 |
| `getParentTransform()` | `parentTransform`をそのまま返すだけ。 |
| `setParentOnStartState(bool state)` | `setParentOnStart`に`state`を代入するだけ。 |
| `setParentOnStartStateFromEditor(bool state)` | 状態を設定したうえで`updateComponent`を呼び、エディタ上のシーンを更新する。 |
