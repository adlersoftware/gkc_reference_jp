# ignoreCollisionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/ignoreCollisionSystem.cs:5`

**概要**: 指定コライダーとの衝突を無視させる設定をまとめて行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Collision Enabled | `ignoreCollisionEnabled` | `bool` | true | – |
| Use Collider List | `useColliderList` | `bool` | – | – |
| Collider List | `colliderList` | `List<Collider>` | new List<Collider> () | – |
| Activate Check On Start | `activateCheckOnStart` | `bool` | – | – |
| Collider To Ignore | `colliderToIgnore` | `Collider` | – | – |
| Force Ignore Collision In Between Objects On Collider List | `forceIgnoreCollisionInBetweenObjectsOnColliderList` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Collider | `mainCollider` | `Collider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateIgnoreCollision(Collider objectToIgnore)` | 有効時、`useColliderList`ならリスト各員と無視設定し、そうでなければ`mainCollider`との`Physics.IgnoreCollision`を有効にする。 |
