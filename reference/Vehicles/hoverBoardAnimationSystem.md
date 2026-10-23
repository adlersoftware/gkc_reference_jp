# hoverBoardAnimationSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/Vehicle Controllers/hoverBoardAnimationSystem.cs:5`

**概要**: ホバーボード搭乗中のプレイヤーの`Animator`と上半身IKを制御する補助コンポーネント。頭・腕・胴の向きをボードの動きに追従させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Extra Body Rotation | `extraBodyRotation` | `float` | -20 | – |
| Extra Spine Rotation | `extraSpineRotation` | `float` | 30 | – |
| Limit Body Rotation X | `limitBodyRotationX` | `float` | 30 | – |
| Limit Body Rotation Z | `limitBodyRotationZ` | `float` | 30 | – |
| Min Spine Rotation X | `minSpineRotationX` | `float` | 20 | – |
| Max Spine Rotation X | `maxSpineRotationX` | `float` | 330 | – |
| Max Arms Rotation | `maxArmsRotation` | `float` | 25 | – |
| Add Movement To Body | `addMovementToBody` | `bool` | – | – |
| Add Extra Movement To Body | `addExtraMovementToBody` | `bool` | – | – |
| Add Movement To Arms | `addMovementToArms` | `bool` | – | – |
| Add Movement To Head | `addMovementToHead` | `bool` | – | – |
| Max Head Rotation Backward | `maxHeadRotationBackward` | `float` | – | – |
| Head Rotation Speed | `headRotationSpeed` | `float` | – | – |
| Min Backward Velocity To Head Rotation | `minBackwardVelocityToHeadRotation` | `float` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Head Look Center | `headLookCenter` | `Transform` | – | – |
| Body Look Center | `bodyLookCenter` | `Transform` | – | – |
| Body Look Pivot | `bodyLookPivot` | `Transform` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Main Hover Board Controller | `mainHoverBoardController` | `hoverBoardController` | – | – |
| Hover Board Transform | `hoverBoardTransform` | `Transform` | – | – |
| Player Gravity Center | `playerGravityCenter` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `changeVehicleState(bool state)` | 搭乗状態を反映し、Animatorと上半身IKの有効化・注視対象を切り替える。 |
