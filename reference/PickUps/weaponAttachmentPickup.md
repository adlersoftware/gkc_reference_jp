# weaponAttachmentPickup

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `pickupType`
- **ソース**: `PickUps/Pickups Behaviour/weaponAttachmentPickup.cs:5`

**概要**: 武器アタッチメント用のピックアップ。インベントリへ保存するか、所持武器へ装着できるかを判定し、取得メッセージとサウンドを出して消える。

## インスペクター設定

### Custom Pickup Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Name | `weaponName` | `string` | – | – |
| Attachment Name | `attachmentName` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setAttachmentName(string newName)` | `attachmentName` を設定するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkIfCanBePicked()`, `confirmTakePickup()`

</details>
