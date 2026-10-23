# setRigidbodyStateSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/setRigidbodyStateSystem.cs:6`

**概要**: リストまたは半径検索で集めたRigidbodyをまとめて非キネマティックにし、指定方向の力や爆発力、リモートイベントを適用するコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Force Mode | `forceMode` | `ForceMode` | – | – |
| Force Amount | `forceAmount` | `float` | – | The force direction in external transform use the UP direction of that transform |
| Explosion Radius | `explosionRadius` | `float` | – | – |
| Explosio Upward Amount | `explosioUpwardAmount` | `float` | – | – |
| Check To Add Rigidbody If Not Found | `checkToAddRigidbodyIfNotFound` | `bool` | – | – |
| Unparent Rigidbody | `unparentRigidbody` | `bool` | – | – |

### Rigidbody List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Rigidbody List | `rigidbodyList` | `List<GameObject>` | new List<GameObject> () | – |

### Detect Rigidbodies Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Search Rigidbodies On Radius Enabled | `searchRigidbodiesOnRadiusEnabled` | `bool` | – | – |
| Radius To Search | `radiusToSearch` | `float` | – | – |
| Radius Layer | `radiusLayer` | `LayerMask` | – | – |
| Main Transform Center | `mainTransformCenter` | `Transform` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remove Event Name List | `removeEventNameList` | `List<string>` | new List<string> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `searchRigidbodiesInRadius()` | 半径検索が有効なら中心から`radiusToSearch`の球内の剛体を`rigidbodyList`に重複なく追加する。 |
| `setKinematicState(bool state)` | `rigidbodyList`の各剛体の`isKinematic`を、引数の値に関係なくfalseにする。 |
| `addForce(Transform forceDirection)` | 各剛体を非キネマティックにし、`forceDirection.up * forceAmount`の力を加える。 |
| `addExplosiveForce(Transform explosionCenter)` | 各剛体に`explosionCenter`から`forceAmount`の爆発力を加える。 |
| `addExplosiveForceUsingObjectsMass(Transform explosionCenter)` | 各剛体に質量を掛けた`forceAmount`の爆発力を加える。 |
| `addForceToThis(Transform forceDirection)` | 自身の剛体（必要なら追加）に`forceDirection.up * forceAmount`の力を加える。 |
| `checkRemoteEventsOnRigidbodyList()` | フラグ有効時、各剛体の`remoteEventSystem`に`removeEventNameList`のイベントを送る。 |
