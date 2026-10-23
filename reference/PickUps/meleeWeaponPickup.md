# meleeWeaponPickup

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `pickupType`
- **ソース**: `PickUps/Pickups Behaviour/meleeWeaponPickup.cs:5`

**概要**: 近接武器用のピックアップ。インベントリに保存できる場合のみ取得可とし、取得時はメッセージ・サウンド・レベルからの削除を行う。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Name | `weaponName` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setMeleeWeaponName(string newWeaponName)` | `weaponName` を設定するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkIfCanBePicked()`, `confirmTakePickup()`, `renameObject(string newName)`

</details>
