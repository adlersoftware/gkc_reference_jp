# dualWieldMeleeWeaponObjectSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/dualWieldMeleeWeaponObjectSystem.cs:5`

**概要**: 左手に持たせる二刀流用の近接武器オブジェクトとその`hitCombat`の攻撃判定を管理する。

## インスペクター設定

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Hit Combat | `mainHitCombat` | `hitCombat` | – | – |
| Current Grabbed Object Melee Attack System | `currentGrabbedObjectMeleeAttackSystem` | `grabbedObjectMeleeAttackSystem` | – | – |
| Melee Weapon Object | `meleeWeaponObject` | `Transform` | – | – |
| Melee Weapon Parent | `meleeWeaponParent` | `Transform` | – | – |
| Melee Weapon Hand Transform Reference | `meleeWeaponHandTransformReference` | `Transform` | – | – |
| Melee Weapon Transform Reference | `meleeWeaponTransformReference` | `Transform` | – | – |
| Raycast Check Transfrom | `raycastCheckTransfrom` | `Transform` | – | – |
| Main Damage Position Transform | `mainDamagePositionTransform` | `Transform` | – | – |

### Cutting Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Cut Position Transform | `cutPositionTransform` | `Transform` | – | – |
| Cut Direction Transform | `cutDirectionTransform` | `Transform` | – | – |
| Plane Definer1 | `planeDefiner1` | `Transform` | – | – |
| Plane Definer2 | `planeDefiner2` | `Transform` | – | – |
| Plane Definer3 | `planeDefiner3` | `Transform` | – | – |

### Damage Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Raycast Check Transfrom List | `raycastCheckTransfromList` | `List<Transform>` | new List<Transform> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableDualWieldMeleeweapobObject(grabbedObjectMeleeAttackSystem newGrabbedObjectMeleeAttackSystem, bool useEventsOnDamageDetected)` | 左手指定位置に武器を親子付けし、`hitCombat`のレイヤー/タグ/コライダーを設定して元サイズを保存し、表示する。 |
| `enableOrDisableDualWieldMeleeWeaponObject(bool state)` | `meleeWeaponObject`のアクティブ状態を指定値と異なる場合のみ切り替えるだけ。 |
| `disableDualWieldMeleeweapobObject()` | `hitCombat`のコライダーを無効にし、武器を`meleeWeaponParent`へ戻して位置と回転を基準値に戻す。 |
| `setHitCombatScale(Vector3 newScale)` | `hitCombat`のBoxColliderの`size`を指定値に設定するだけ。 |
| `setHitCombatScaleMultiplier(float newMultiplier)` | `hitCombat`のBoxColliderの`size`に指定倍率を掛けるだけ。 |
| `setHitCombatOffset(Vector3 newValue)` | `hitCombat`のBoxColliderの`center`を指定値に設定するだけ。 |
| `setOriginalHitCombatScale()` | 保存しておいた元のコライダーサイズへ`setHitCombatScale`で戻すだけ。 |
| `setOriginalHitCombatOffset()` | 保存しておいた元のコライダー中心へ`setHitCombatOffset`で戻すだけ。 |
