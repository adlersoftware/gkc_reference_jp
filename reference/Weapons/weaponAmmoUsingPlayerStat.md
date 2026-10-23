# weaponAmmoUsingPlayerStat

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/weaponAmmoUsingPlayerStat.cs:6`

**概要**: 射撃時に武器弾薬の代わりにプレイヤーステータスを消費する小さなブリッジ。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Stats System | `mainPlayerStatsSystem` | `playerStatsSystem` | – | – |
| Stat To Use Name | `statToUseName` | `string` | – | – |
| Amount To Use Per Shoot | `amountToUsePerShoot` | `float` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `useWeaponAmmo()` | `statToUseName`のステータスを`amountToUsePerShoot`だけ消費する。 |
