# simpleChainSaw

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/New Weapon Behaviors/simpleChainSaw.cs:6`

**概要**: チェーンソーの起動状態と燃料消費、ピボットの手動・自動回転を扱う武器挙動。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Rotation Pivot | `mainRotationPivot` | `Transform` | – | – |
| Initial Pivot Rotation | `initialPivotRotation` | `float` | – | – |
| Use Fixed Vertical Horizontal Rotations | `useFixedVerticalHorizontalRotations` | `bool` | – | – |
| Angle Rotation Amount | `angleRotationAmount` | `float` | – | – |
| Rotation Speed | `rotationSpeed` | `float` | – | – |
| Manual Rotation Amount | `manualRotationAmount` | `float` | – | – |
| Max Rotation Angle | `maxRotationAngle` | `float` | 80 | – |
| Min Rotation Angle | `minRotationAngle` | `float` | -10 | – |

### Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Fuel Enabled | `useFuelEnabled` | `bool` | true | – |
| Use Fuel Rate | `useFuelRate` | `float` | – | – |
| Amount Fuel Used | `amountFuelUsed` | `int` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Chainsaw Active | `chainsawActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Activate Chainsaw | `eventOnActivateChainsaw` | `UnityEvent` | – | – |
| Event On Deactivate Chainsaw | `eventOnDeactivateChainsaw` | `UnityEvent` | – | – |
| Event On Rotate Weapon | `eventOnRotateWeapon` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Manager | `weaponManager` | `playerWeaponSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`があれば停止するだけ。 |
| `activateChainSaw()` | `activateOrDeactivateChainsaw(true)`を呼ぶだけ。 |
| `deactivateChainSaw()` | `activateOrDeactivateChainsaw(false)`を呼ぶだけ。 |
| `rotatePivotToRight()` | `mainRotationPivot`を`manualRotationAmount`だけZ軸正方向へ回し、最大角度内に収める。 |
| `rotatePivotToLeft()` | `mainRotationPivot`を`manualRotationAmount`だけZ軸負方向へ回し、最小角度内に収める。 |
| `changePivotRotation()` | 回転中でなければ角度を決めて回転イベントを出し、ピボットを目標角へ補間するコルーチンを開始する。 |
| `stopChangePivotRotation()` | `rotationCoroutine`があれば停止するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnActivateChainsaw` | `UnityEvent` | – |
| `eventOnDeactivateChainsaw` | `UnityEvent` | – |
| `eventOnRotateWeapon` | `UnityEvent` | – |
