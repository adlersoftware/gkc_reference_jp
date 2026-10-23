# weaponPickup

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `pickupType`
- **ソース**: `PickUps/Pickups Behaviour/weaponPickup.cs:5`

**概要**: 武器そのものを拾うピックアップ。`playerWeaponsManager` で所持状況やエイム中・武器切替中かを確認して取得可否を決め、取得・インベントリ保存・メッセージ表示を行う。

## インスペクター設定

### Custom Pickup Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Name | `weaponName` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setWeaponName(string newWeaponName)` | `weaponName` を設定するだけ。 |
| `getWeaponName()` | `weaponName` を返すだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkIfCanBePicked()`, `confirmTakePickup()`, `renameObject(string newName)`

</details>
