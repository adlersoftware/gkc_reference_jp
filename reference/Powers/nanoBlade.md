# nanoBlade

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `projectileSystem`
- **ソース**: `Powers/nanoBlade.cs:6`

**概要**: `projectileSystem`を継承した投擲弾で、命中したオブジェクトや最寄りのラグドールボーンに弾を固定し、ダメージと衝撃力を与える。

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkObjectDetected(Collider col)` | 命中時に軌跡を消して弾をキネマティック化し、対象か最寄りラグドールボーンへ親子付けして即死またはダメージと力を与える。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetProjectile()`

</details>
