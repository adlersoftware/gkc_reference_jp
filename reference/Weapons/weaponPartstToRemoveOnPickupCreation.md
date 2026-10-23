# weaponPartstToRemoveOnPickupCreation

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/weaponPartstToRemoveOnPickupCreation.cs:5`

**概要**: 拾い物用の武器モデルを作る際に、不要なパーツを削除するための小さなコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object List To Remove | `objectListToRemove` | `List<GameObject>` | new List<GameObject> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `removeWeaponObjects()` | リスト内のオブジェクトを`DestroyImmediate`で消してからリストを空にする。 |
