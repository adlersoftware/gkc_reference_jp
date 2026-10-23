# weaponObjectInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/weaponObjectInfo.cs:5`

**概要**: 武器情報の取得口を提供する基底クラスで、各メソッドは既定値を返すか空のまま。

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getWeaponName()` | 空文字を返すだけで、派生クラスでの上書きが前提。 |
| `isMeleeWeapon()` | `false`を返すだけで、派生クラスでの上書きが前提。 |
| `isFireWeapon()` | `false`を返すだけで、派生クラスでの上書きが前提。 |
| `getAmmoText()` | 空文字を返すだけ。 |
| `getProjectilesInWeaponMagazine()` | `-1`を返すだけ。 |
| `getWeaponAmmoName()` | 空文字を返すだけ。 |
| `setWeaponRemainAmmoAmount(int newRemainAmmoAmount)` | 本体が空で何もしない。 |
| `isWeaponUseRemainAmmoFromInventoryActive()` | `false`を返すだけ。 |
