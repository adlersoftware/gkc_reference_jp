# addGrenadeToThrowAwayFromCharacter

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/addGrenadeToThrowAwayFromCharacter.cs:5`

**概要**: 投擲グレナードをプレイヤーのアビリティ所持数へ足し引きする補助コンポーネント。確定時は投射物を投げられる状態へ戻す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Grenade On Character Enabled | `checkGrenadeOnCharacterEnabled` | `bool` | true | – |
| Throw Grenade Ability Name | `throwGrenadeAbilityName` | `string` | "Throw Grenade" | – |
| Message Panel Name | `messagePanelName` | `string` | "Return Grenade" | – |
| Set Throw Grenade Ability Automatically | `setThrowGrenadeAbilityAutomatically` | `bool` | true | – |
| Main Projectile System | `mainProjectileSystem` | `projectileSystem` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Player | `currentPlayer` | `GameObject` | – | – |
| Confirm Throw Grenade Active | `confirmThrowGrenadeActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `addGrenadeToCharacterSystem(GameObject playerToCheck)` | `currentPlayer`を設定し、有効なら`checkPlayer(true)`で所持数を1増やす。 |
| `removeGrenadeToCharacterSystem()` | `currentPlayer`がいれば`checkPlayer(false)`を呼び、所持数と外部投射物の設定を解除する。 |
| `confirmThrowAwayGrenade()` | `confirmThrowGrenadeActive`を立て、投射物の発射済み状態を戻して元の所有者との衝突判定を再有効化する。 |
