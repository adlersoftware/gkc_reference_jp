# parentAssignedSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Gravity/parentAssignedSystem.cs:5`

**概要**: 重力の親として使うGameObjectを保持し、必要なら自身で補完して返す小さなコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Parent Game Object | `parentGameObject` | `GameObject` | – | – |

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Parent Assigned | `parentAssigned` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `assignParent(GameObject newParent)` | 親GameObjectを設定し、nullでないかで`parentAssigned`を更新する。 |
| `getAssignedParent()` | 未設定なら自身を親として補完し、割り当て済みの親を返す。 |
| `getAssignedParentTransform()` | `getAssignedParent`と同じ補完を行い、親のTransformを返す。 |
