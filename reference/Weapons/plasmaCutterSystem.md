# plasmaCutterSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/New Weapon Behaviors/plasmaCutterSystem.cs:6`

**概要**: プラズマカッターのローター角度を手動・自動で回転させ、射撃イベントを発火する武器挙動。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Rotor | `mainRotor` | `Transform` | – | – |
| Initial Rotor Rotation | `initialRotorRotation` | `float` | – | – |
| Use Fixed Vertical Horizontal Rotations | `useFixedVerticalHorizontalRotations` | `bool` | – | – |
| Angle Rotation Amount | `angleRotationAmount` | `float` | – | – |
| Rotation Speed | `rotationSpeed` | `float` | – | – |
| Manual Rotation Amount | `manualRotationAmount` | `float` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Fire Weapon | `eventOnFireWeapon` | `UnityEvent` | – | – |
| Event On Rotate Weapon | `eventOnRotateWeapon` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `firePlasmaCutter()` | `eventOnFireWeapon`を発火するだけ。 |
| `rotateRotorToRight()` | `mainRotor`を`manualRotationAmount`だけZ軸正方向へ回す。 |
| `rotateRotorToLeft()` | `mainRotor`を`manualRotationAmount`だけZ軸負方向へ回す。 |
| `changeRotorRotation()` | 回転中でなければ角度を決めて回転イベントを出し、`mainRotor`を目標角へ補間するコルーチンを開始する。 |
| `stopChangeRotorRotation()` | `rotationCoroutine`があれば停止するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnFireWeapon` | `UnityEvent` | – |
| `eventOnRotateWeapon` | `UnityEvent` | – |
