# removeGravityFromObjectSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/Custom Abilities/removeGravityFromObjectSystem.cs:5`

**概要**: オブジェクトの重力を一定時間だけ解除して力を加え、減速・キネマティック切替の後に元の重力へ戻す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remove Gravity Duration | `removeGravityDuration` | `float` | 5 | – |
| Delay Before Freezing Velocity | `delayBeforeFreezingVelocity` | `float` | 3 | – |
| Pause Extra Force After Delay | `pauseExtraForceAfterDelay` | `bool` | – | – |
| Pause Extra Force Delay | `pauseExtraForceDelay` | `float` | – | – |
| Set Object As Kinematic On Zero Velocity | `setObjectAsKinematicOnZeroVelocity` | `bool` | – | – |
| Duration As Kinematic | `durationAsKinematic` | `float` | – | – |

### Force Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pause Extra Force Speed | `pauseExtraForceSpeed` | `float` | 3 | – |
| Extra Gravity Force | `extraGravityForce` | `float` | 5 | – |
| Extra Torque Force | `extraTorqueForce` | `float` | 8 | – |
| Torque Force Mode | `torqueForceMode` | `ForceMode` | – | – |
| Add Torque On Remove Gravity | `addTorqueOnRemoveGravity` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Remove Gravity Active | `removeGravityActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Rigibody | `mainRigibody` | `Rigidbody` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateRemoveGravity()` | 既存のコルーチンを止め、重力を切って力を加え、減速後に元の重力へ戻す一連の処理を開始する。 |
