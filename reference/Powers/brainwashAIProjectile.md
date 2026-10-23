# brainwashAIProjectile

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `projectileSystem`
- **ソース**: `Powers/New Projectiles Behaviors/brainwashAIProjectile.cs:6`

**概要**: `projectileSystem`を継承した弾で、命中したキャラクターを指定陣営・タグ・名前へ洗脳し、プレイヤーをパートナーに設定できる。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Faction To Configure | `factionToConfigure` | `string` | "Friend Soldiers" | – |
| Set New Name | `setNewName` | `bool` | – | – |
| New Name | `newName` | `string` | – | – |
| AI Is Friend | `AIIsFriend` | `bool` | – | – |
| New Tag | `newTag` | `string` | "friend" | – |
| Follow Partner On Trigger Enabled | `followPartnerOnTriggerEnabled` | `bool` | true | – |
| Set Player As Partner | `setPlayerAsPartner` | `bool` | true | – |
| Use Remote Events | `useRemoteEvents` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkObjectDetected(Collider col)` | 命中効果が有効なら着弾音を再生して弾を停止し、対象キャラクターを指定陣営へ洗脳した後`disableBullet`で消す。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetProjectile()`

</details>
