# shootPowerSimpleAIAction

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `simpleAIAction`
- **ソース**: `AI/Custom AI Behavior/shootPowerSimpleAIAction.cs:5`

**概要**: `otherPowers`を通じて特殊能力の発動入力を送るAIアクションで、発動時間や発射数を設定できる。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shoot Power Duration | `shootPowerDuration` | `float` | 2 | – |
| Use Amount Of Projectiles To Shoot | `useAmountOfProjectilesToShoot` | `bool` | – | – |
| Amount Of Projectiles To Shoot | `amountOfProjectilesToShoot` | `int` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Aiming Power | `aimingPower` | `bool` | – | – |
| Shooting Power | `shootingPower` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Other Powers | `mainOtherPowers` | `otherPowers` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setShootWeaponState(bool state)` | `inputHoldShootPower`等の発動入力を送り、`shootingPower`に`state`を設定する。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetStatesOnActionEnd()`, `startAIAction()`, `updateSystem()`

</details>
