# meleeWeaponAttackListInfoSocket

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/meleeWeaponAttackListInfoSocket.cs:5`

**概要**: 武器の攻撃情報とテンプレートのコピーを`grabPhysicalObjectMeleeAttackSystem`へ仲介するソケット。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Melee Weapon Attack Info | `mainMeleeWeaponAttackInfo` | `meleeWeaponAttackInfo` | – | – |
| Main Grab Physical Object Melee Attack System | `mainGrabPhysicalObjectMeleeAttackSystem` | `grabPhysicalObjectMeleeAttackSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `copyWeaponInfoToTemplate(bool settingInfoOnEditorTime)` | `mainGrabPhysicalObjectMeleeAttackSystem`に攻撃情報を渡し、テンプレートへ情報をコピーさせる。 |
| `copyTemplateToWeaponAttackInfo(bool settingInfoOnEditorTime)` | 同じく攻撃情報を渡したうえで、テンプレートから武器の攻撃情報へ逆コピーさせる。 |
