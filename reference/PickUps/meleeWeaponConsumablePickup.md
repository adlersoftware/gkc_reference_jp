# meleeWeaponConsumablePickup

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `pickupType`
- **ソース**: `PickUps/Pickups Behaviour/meleeWeaponConsumablePickup.cs:5`

**概要**: 近接武器の消耗品用ピックアップ。インベントリ保存時のみ取得可能とし、取得時はメッセージとサウンドを出してレベルから取り除く。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Consumable Name | `weaponConsumableName` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setWeaponConsumableName(string newWeaponConsumableName)` | `weaponConsumableName` を設定するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkIfCanBePicked()`, `confirmTakePickup()`

</details>
