# meleeCombatAttackStartState

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/meleeCombatAttackStartState.cs:5`

**概要**: ダメージ判定トリガーのリセットを許可するフラグを持つ小型コンポーネント。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attack Reset Enabled | `attackResetEnabled` | `bool` | true | – |
| Main Grabbed Object Melee Attack System | `mainGrabbedObjectMeleeAttackSystem` | `grabbedObjectMeleeAttackSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `resetActivateDamageTriggerCoroutine()` | `attackResetEnabled`が真なら`mainGrabbedObjectMeleeAttackSystem`の同名メソッドを呼ぶだけ。 |
