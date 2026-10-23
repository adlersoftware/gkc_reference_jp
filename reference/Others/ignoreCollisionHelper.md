# ignoreCollisionHelper

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/ignoreCollisionHelper.cs:5`

**概要**: 指定レイヤーやタグのオブジェクトとの衝突を`Physics.IgnoreCollision`で無視し、その記録と復帰・一時的な有効化を扱う補助コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Collision Check Enabled | `collisionCheckEnabled` | `bool` | true | – |
| Layer To Ignore | `layerToIgnore` | `LayerMask` | – | – |
| Ignore By Tag Enabled | `ignoreByTagEnabled` | `bool` | – | – |
| Tag To Ignore List | `tagToIgnoreList` | `List<string>` | new List<string> () | – |
| Store Objects Ignored | `storeObjectsIgnored` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Objects Ignored List | `objectsIgnoredList` | `List<Collider>` | new List<Collider> () | – |
| Objects Stored | `objectsStored` | `bool` | – | – |

### Component

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Collider | `mainCollider` | `Collider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCollisionCheckEnabledState(bool state)` | `collisionCheckEnabled`を`state`にするだけ。 |
| `reactivateIgnoredCollisionsStored()` | 保存した`objectsIgnoredList`の各コライダーとの衝突無視を解除し、リストを空にする。 |
| `clearObjectsIgnoredList()` | `objectsIgnoredList`を空にし、`objectsStored`をfalseにするだけ。 |
| `enableComponentTemporaryAndReactivateCollisionsStoredWithDelay(float duration)` | `duration`秒だけ衝突チェックを有効にし、同じ時間の後に衝突無視を解除する。 |
| `enableComponentTemporary(float duration)` | `duration`秒間だけ`collisionCheckEnabled`をtrueにする。 |
| `disableComponentTemporary(float duration)` | コルーチンを止めて`collisionCheckEnabled`をfalseにし、`duration`は使われない。 |
| `enableOrDisableComponentTemporary(bool state, float duration)` | `state`で即時に切り替え、trueなら`duration`秒後に自動で無効化する。 |
| `reactivateCollisionsStoredWithDelay(float duration)` | `duration`秒待ってから保存済みの衝突無視を解除するコルーチンを開始する。 |
