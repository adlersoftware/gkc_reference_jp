# waterSurfaceSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/waterSurfaceSystem.cs:5`

**概要**: 水面の高さ・法線・密度などを外部へ提供する基底クラス。各メソッドは`virtual`で既定値だけを返し、実処理は派生クラスが上書きする。

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `GetWaterLevel(Vector3 worldPoint)` | `worldPoint`の水面高さを返す基底実装で、常に-1を返す。 |
| `GetSurfaceNormal(Vector3 worldPoint)` | `worldPoint`の水面法線を返す基底実装で、常に`Vector3.zero`を返す。 |
| `getGravityForce()` | 水面で働く重力ベクトルを返す基底実装で、常に`Vector3.zero`を返す。 |
| `getDensity()` | 水の密度を返す基底実装で、常に-1を返す。 |
| `CalculateVolume_Mesh(Mesh mesh, Transform trans)` | `mesh`と`trans`から体積を求める基底実装で、常に-1を返す。 |
| `IsPointInsideCollider(Vector3 point, Collider collider, ref Bounds colliderBounds)` | `point`が`collider`内かを判定する基底実装で、`colliderBounds`も更新せず常に`false`を返す。 |
