# ammoPickup

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `pickupType`
- **ソース**: `PickUps/Pickups Behaviour/ammoPickup.cs:5`

**概要**: 弾薬用のピックアップ。所持武器や車両武器の弾薬上限を確認して取得量を決め、`AddAmmo` または車両HUDへ加算し、残量があれば再取得イベントを送る。

## インスペクター設定

### Custom Pickup Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ammo Name | `ammoName` | `string` | – | – |
| Unable To Pick Ammo Message | `unableToPickAmmoMessage` | `string` | "You haven't weapons with this ammo t… | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setAmmoName(string newAmmoName)` | `ammoName` を設定するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkIfCanBePicked()`, `confirmTakePickup()`, `renameObject(string newName)`

</details>
