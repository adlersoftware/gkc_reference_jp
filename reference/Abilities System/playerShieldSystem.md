# playerShieldSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `abilityInfo`
- **ソース**: `Abilities System/Custom Abilities/playerShieldSystem.cs:5`

**概要**: プレイヤーのシールドと手元レーザーを扱うアビリティ。飛来する弾を防ぎ、貯めた弾を撃ち返す機能も持つ。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shield Enabled | `shieldEnabled` | `bool` | – | – |
| Shield Active | `shieldActive` | `bool` | – | – |
| Laser Active | `laserActive` | `bool` | – | – |
| Laser Ability Enabled | `laserAbilityEnabled` | `bool` | true | – |
| Layer To Damage | `layerToDamage` | `LayerMask` | – | – |
| Return Projectiles Detected Enabled | `returnProjectilesDetectedEnabled` | `bool` | true | – |
| Destro Projectiles Stored If Shield Disabled | `destroProjectilesStoredIfShieldDisabled` | `bool` | – | – |

### Component Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shield | `shield` | `GameObject` | – | – |
| Armor Surface Manager | `armorSurfaceManager` | `armorSurfaceSystem` | – | – |
| Player Laser Game Object | `playerLaserGameObject` | `GameObject` | – | – |
| Laser Player Manager | `laserPlayerManager` | `laserPlayer` | – | – |
| Main Other Powers | `mainOtherPowers` | `otherPowers` | – | – |
| Pivot Camera Transform | `pivotCameraTransform` | `Transform` | – | – |
| Player Camera Transform | `playerCameraTransform` | `Transform` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Player Collider | `playerCollider` | `Collider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setActiveShieldState(bool state)` | プレイヤーが多忙でなければ `setShieldState` を呼んでシールドを切り替える。 |
| `setShieldState(bool state)` | 条件を満たす時だけ `shieldActive` とシールド表示を切り替え、`checkIfDestroyProjectiles` を呼ぶ。 |
| `activateLaserForceField(Vector3 pos)` | レーザー照射状態にしてシールドを表示し、`pos` を当たり位置として `laserPlayer` に渡して弾を破棄する。 |
| `deactivateLaserForceField()` | `laserActive` を下げてシールドと手元レーザーを消し、`removeLaserInfo` でレーザー参照を外す。 |
| `setShieldEnabledState(bool state)` | `shieldEnabled` を設定するだけ。 |
| `returnEnemyProjectiles()` | 条件を満たす時、画面中央のレイキャスト先を狙って貯めた弾を `throwProjectilesStored` で撃ち返す。 |
| `setLaser(GameObject l, laserDevice.laserType type)` | `currentLaser` と `lasertype` を設定するだけ。 |
| `setLaserRefractionLimit(int value)` | `laserPlayerManager.reflactionLimit` に `value + 1` を設定するだけ。 |
| `setLaserAbilityEnabledState(bool state)` | `laserAbilityEnabled` を設定するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`activateSecondaryActionOnAbility()`, `deactivateAbility()`, `disableAbility()`, `enableAbility()`, `updateAbilityState()`, `useAbilityPressDown()`, `useAbilityPressHold()`, `useAbilityPressUp()`

</details>
