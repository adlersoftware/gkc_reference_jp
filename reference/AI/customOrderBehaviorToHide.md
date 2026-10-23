# customOrderBehaviorToHide

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `customOrderBehavior`
- **ソース**: `AI/Custom Orders/customOrderBehaviorToHide.cs:5`

**概要**: 隠れ注文用に、シーン内の`AIHidePositionsManager`が持つ隠れ位置から対象を選ぶビヘイビア。

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getClosestHidePosition(Transform AIFriend)` | `AIHidePositionsManager`を保持し、`AIFriend`から最も近い隠れ位置を返す。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`activateOrder(Transform character)`, `getCustomTarget(Transform character, Transform orderOwner)`

</details>
