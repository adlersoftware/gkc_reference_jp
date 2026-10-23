# shootFireWeaponSimpleAIAction

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `simpleAIAction`
- **ソース**: `AI/Custom AI Behavior/shootFireWeaponSimpleAIAction.cs:5`

**概要**: `playerWeaponsManager`を通じて銃器を射撃するAIアクションで、射撃時間や発射数を設定できる。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shoot Weapon Duration | `shootWeaponDuration` | `float` | 2 | – |
| Use Amount Of Projectiles To Shoot | `useAmountOfProjectilesToShoot` | `bool` | – | – |
| Amount Of Projectiles To Shoot | `amountOfProjectilesToShoot` | `int` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Aiming Weapon | `aimingWeapon` | `bool` | – | – |
| Shooting Weapon | `shootingWeapon` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setShootWeaponState(bool state)` | 操作主体に応じ射撃入力か`shootWeapon(state)`を呼び、`shootingWeapon`と最終射撃時刻を更新する。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetStatesOnActionEnd()`, `startAIAction()`, `updateSystem()`

</details>
