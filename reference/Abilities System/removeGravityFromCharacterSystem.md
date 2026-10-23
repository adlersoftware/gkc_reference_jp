# removeGravityFromCharacterSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/Custom Abilities/removeGravityFromCharacterSystem.cs:5`

**概要**: ラグドール化したキャラクターの重力を一定時間だけ切り、上方向の力とトルクを加えるコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remove Gravity Duration | `removeGravityDuration` | `float` | 5 | – |
| Extra Gravity Force | `extraGravityForce` | `float` | 5 | – |
| Extra Torque Force | `extraTorqueForce` | `float` | 8 | – |
| Torque Force Mode | `torqueForceMode` | `ForceMode` | – | – |
| Pause Extra Force After Delay | `pauseExtraForceAfterDelay` | `bool` | – | – |
| Pause Extra Force Delay | `pauseExtraForceDelay` | `float` | – | – |
| Pause Extra Force Speed | `pauseExtraForceSpeed` | `float` | 3 | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Ragdoll Activator | `mainRagdollActivator` | `ragdollActivator` | – | – |
| Character Transform | `characterTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateRemoveGravity()` | 既存のコルーチンを止め、一定時間だけラグドールの重力を切って上方向の力とトルクを加える処理を開始する。 |
