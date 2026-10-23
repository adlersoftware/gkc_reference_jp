# elementOnSceneHelper

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Save System/Elements On Scene/elementOnSceneHelper.cs:5`

**概要**: `elementOnScene`の処理を外部から呼ぶための中継コンポーネント。`checkElementOnSceneEnabled`がfalse、または参照がnullなら何もしない。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Element On Scene Enabled | `checkElementOnSceneEnabled` | `bool` | true | – |
| Main Element On Scene | `mainElementOnScene` | `elementOnScene` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setElementActiveStateToMainElementOnSceneManager(bool state)` | `mainElementOnScene`の同名メソッドへ状態をそのまま渡す。 |
| `setNewInstantiatedElementOnSceneManagerIngameWithInfo()` | `mainElementOnScene`へ新規生成要素の登録を依頼する。 |
| `setElementActiveState(bool state)` | `mainElementOnScene`のアクティブ状態を設定する。 |
| `getElementScene()` | `mainElementOnScene.elementScene`を返し、無効時は-1を返す。 |
| `getElementID()` | `mainElementOnScene.elementID`を返し、無効時は-1を返す。 |
| `setStatsSearchingByInfo(int currentElementScene, int currentElementID)` | シーン番号とIDを`mainElementOnScene`へ渡して統計検索を依頼する。 |
