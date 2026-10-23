# pointToLook

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Head Track/pointToLook.cs:5`

**概要**: プレイヤーカメラに注視対象として検出させるための目印コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Point To Look Enabled | `pointToLookEnabled` | `bool` | true | – |

### Component

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Point To Look Transform | `pointToLookTransform` | `Transform` | – | – |
| Explanation | `explanation` | `string` | "Put this component in an object with… | TextArea (3, 10) |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getPointToLookTransform()` | 未設定なら自身のTransformを割り当てて返す。 |
| `setPointToLookEnabledState(bool state)` | `pointToLookEnabled`を設定するだけ。 |
| `isPointToLookEnabled()` | `pointToLookEnabled`を返すだけ。 |
| `checkToRemoveThisObjectFromPlayerLockOn()` | `applyDamage`に自身の位置を渡し、死亡対象としてのロックオン解除を判定させる。 |
