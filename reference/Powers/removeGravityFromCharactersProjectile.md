# removeGravityFromCharactersProjectile

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `projectileSystem`
- **ソース**: `Powers/New Projectiles Behaviors/removeGravityFromCharactersProjectile.cs:6`

**概要**: 着弾地点の範囲内のキャラから、重力を一時的に外す弾。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remote Event Name | `remoteEventName` | `string` | "Remove Gravity From Character" | – |
| Main Area Effect On Area | `mainAreaEffectOnArea` | `applyEffectOnArea` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkObjectDetected(Collider col)` | 当たると範囲エフェクトを有効化し、弾を停止して効果音とパーティクルを出し消滅させる。 |
| `applyEffect(GameObject objectToAffect)` | 対象の`remoteEventSystem`を探し、重力除去の遠隔イベントを送る。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetProjectile()`

</details>
