# shootBowSimpleAIAction

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `simpleAIAction`
- **ソース**: `AI/Custom AI Behavior/shootBowSimpleAIAction.cs:5`

**概要**: `bowSystem`を操作して弓を射るAIアクションで、射撃時間や発射数、連射間隔を設定できる。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shoot Weapon Duration | `shootWeaponDuration` | `float` | 2 | – |
| Use Amount Of Projectiles To Shoot | `useAmountOfProjectilesToShoot` | `bool` | – | – |
| Amount Of Projectiles To Shoot | `amountOfProjectilesToShoot` | `int` | – | – |
| Use Fire Rate | `useFireRate` | `bool` | – | – |
| Fire Rate | `fireRate` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Aiming Weapon | `aimingWeapon` | `bool` | – | – |
| Shooting Weapon | `shootingWeapon` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Bow System | `mainBowSystem` | `bowSystem` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setShootWeaponState(bool state)` | `state`に関係なく`inputFireArrow`で矢を放ち、`shootingWeapon`に`state`を設定する。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetStatesOnActionEnd()`, `startAIAction()`, `updateSystem()`

</details>
