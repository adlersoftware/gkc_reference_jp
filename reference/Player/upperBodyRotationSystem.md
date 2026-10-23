# upperBodyRotationSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/upperBodyRotationSystem.cs:5`

**概要**: 武器の照準方向へ上半身を曲げるIK制御。`objectToFollow` への角度を求め、しきい値・曲げ倍率・最大角でクランプして回転ポイントを補間する。

**公式ドキュメント抜粋**（[Upper Body Rotation System](../../docs/player-controller-components/player-controller/upper-body-rotation-system.md)）

> It manages the upper body orientation when using weapons or powers that requires the player to aim in third person, so its upper body can rotate separately from the lower body to aim up, down, and to the sides, as any other third-person game does.

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shake Upper Body Enabled | `shakeUpperBodyEnabled` | `bool` | true | – |

### Head Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Head Look Vector | `headLookVector` | `Vector3` | Vector3.forward | – |
| Head Up Vector | `headUpVector` | `Vector3` | Vector3.up | – |

### Rotation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Horizontal Threshold Angle Difference | `horizontalThresholdAngleDifference` | `float` | 5 | – |
| Vertical Threshold Angle Difference | `verticalThresholdAngleDifference` | `float` | 5 | – |
| Horizontal Bending Multiplier | `horizontalBendingMultiplier` | `float` | 1 | – |
| Vertical Bending Multiplier | `verticalBendingMultiplier` | `float` | 1 | – |
| Horizontal Max Angle Difference | `horizontalMaxAngleDifference` | `float` | 90 | – |
| Vertical Max Angle Difference | `verticalMaxAngleDifference` | `float` | 90 | – |
| Max Bending Angle | `maxBendingAngle` | `float` | 90 | – |
| Horizontal Responsiveness | `horizontalResponsiveness` | `float` | 10 | – |
| Vertical Responsiveness | `verticalResponsiveness` | `float` | 10 | – |
| Upper Body Rotation Speed | `upperBodyRotationSpeed` | `float` | 5 | – |
| Rotation Speed | `rotationSpeed` | `float` | 5 | – |
| Chest Rotation Enabled | `chestRotationEnabled` | `bool` | true | – |
| Spine Rotation Enabled | `spineRotationEnabled` | `bool` | true | – |
| Extra Horizontal Rotation Enabled | `extraHorizontalRotationEnabled` | `bool` | true | – |
| Horizontal Rotation Enabled | `horizontalRotationEnabled` | `bool` | true | – |
| Vertical Rotation Enabled | `verticalRotationEnabled` | `bool` | true | – |
| Use Smooth Rotation Point Value | `useSmoothRotationPointValue` | `bool` | – | – |
| Smooth Rotation Point Value | `smoothRotationPointValue` | `float` | 0.1f | – |

### Chest Orientation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Chest Up Vector | `chestUpVector` | `Vector3` | new Vector3 (0, 0, 1) | – |

### Spine And Chest Transforms

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Spine Transform | `spineTransform` | `Transform` | – | – |
| Chest Transform | `chestTransform` | `Transform` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Follow Full Rotation Point Direction | `followFullRotationPointDirection` | `bool` | – | – |
| Follow Full Rotation Point Multipliers | `followFullRotationPointMultipliers` | `Vector3` | Vector3.one | – |
| Use Follow Full Rotation Clamp | `useFollowFullRotationClamp` | `bool` | – | – |
| Follow Full Rotation Clamp X | `followFullRotationClampX` | `Vector2` | – | – |
| Follow Full Rotation Clamp Y | `followFullRotationClampY` | `Vector2` | – | – |
| Follow Full Rotation Clamp Z | `followFullRotationClampZ` | `Vector2` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| IK Upper Body Active | `IKUpperBodyActive` | `bool` | – | – |
| Current Extra Rotation | `currentExtraRotation` | `float` | – | – |
| Using Weapon Rotation Point | `usingWeaponRotationPoint` | `bool` | – | – |
| Using Temporal Object To Follow | `usingTemporalObjectToFollow` | `bool` | – | – |
| Temporal Object To Follow | `temporalObjectToFollow` | `Transform` | – | – |
| Current Weapon Rotation Point | `currentWeaponRotationPoint` | `Transform` | – | – |
| Full Body Awareness Active | `fullBodyAwarenessActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Follow | `objectToFollow` | `Transform` | – | – |
| Weapon Rotation Point To Follow | `weaponRotationPointToFollow` | `Transform` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `calculateCharacterRotationValues()` | spineの親回転から参照用のlook/up方向と逆回転を計算し、`dirUp` を初期化する。 |
| `setCurrentBodyRotation(float bodyRotation)` | `currentExtraRotation` と `auxCurrentExtraRotation` に同じ値を設定するだけ。 |
| `enableOrDisableIKUpperBody(bool value)` | trueなら即座に有効化し、`maxBendingAngle` を目標値へ補間するコルーチンを開始/停止する。 |
| `isIKUpperBodyActive()` | `IKUpperBodyActive` の値を返すだけ。 |
| `checkShakeUpperBodyRotationCoroutine(float extraAngleValue, float speedValue)` | 有効かつIK動作中なら、既存を止めて指定角度と速度で揺らすコルーチンを開始する。 |
| `stopShakeUpperBodyRotation()` | 揺らすコルーチンを停止するだけ。 |
| `setCurrentWeaponRotationPoint(Transform newWeaponRotationPoint, weaponRotationPointInfo newRotationPointInfo, int newRotationDirection)` | 武器の回転ポイント、回転ポイント情報、回転方向をまとめて設定する。 |
| `setUsingWeaponRotationPointState(bool state)` | `usingWeaponRotationPoint` を設定するだけ。 |
| `setUsingDualWeaponState(bool state)` | `usingDualWeapon` を設定するだけ。 |
| `setCurrentRightWeaponRotationPoint(Transform newWeaponRotationPoint, weaponRotationPointInfo newRotationPointInfo, int newRotationDirection)` | 右手用の回転ポイント、情報、回転方向を設定する。 |
| `setCurrentLeftWeaponRotationPoint(Transform newWeaponRotationPoint, weaponRotationPointInfo newRotationPointInfo, int newRotationDirection)` | 左手用の回転ポイント、情報、回転方向を設定する。 |
| `setTemporalObjectToFollow(Transform newObject)` | `temporalObjectToFollow` を設定し、nullでなければ追従フラグを立てる。 |
| `setHorizontalBendingMultiplierValue(float newValue)` | `horizontalBendingMultiplier` を設定するだけ。 |
| `setOriginalHorizontalBendingMultiplier()` | 保存した初期の横曲げ倍率に戻すだけ。 |
| `setVerticalBendingMultiplierValue(float newValue)` | `verticalBendingMultiplier` を設定するだけ。 |
| `setOriginalVerticalBendingMultiplier()` | 保存した初期の縦曲げ倍率に戻すだけ。 |
| `setFollowFullRotationPointDirectionState(bool state)` | `followFullRotationPointDirection` を設定するだけ。 |
| `setUseFollowFullRotationClampState(bool state)` | `useFollowFullRotationClamp` を設定するだけ。 |
| `setNewFollowFullRotationClampX(Vector2 newFollowFullRotationClampXValues)` | X軸の回転クランプ範囲を設定するだけ。 |
| `setNewFollowFullRotationClampY(Vector2 newFollowFullRotationClampYValues)` | Y軸の回転クランプ範囲を設定するだけ。 |
| `setNewFollowFullRotationClampZ(Vector2 newFollowFullRotationClampZValues)` | Z軸の回転クランプ範囲を設定するだけ。 |
| `setExtraHorizontalRotationEnabledState(bool state)` | `extraHorizontalRotationEnabled` を設定するだけ。 |
| `setHorizontalMaxAngleDifference(float newValue)` | `horizontalMaxAngleDifference` を設定するだけ。 |
| `setVerticalMaxAngleDifference(float newValue)` | `verticalMaxAngleDifference` を設定するだけ。 |
| `setOriginalHorizontalMaxAngleDifference()` | 保存した初期の横方向最大角度差に戻すだけ。 |
| `setOriginalVerticalMaxAngleDifference()` | 保存した初期の縦方向最大角度差に戻すだけ。 |
| `setFullBodyAwarenessActiveState(bool state)` | FBAフラグを設定し、有効時は武器回転ポイントの回転をリセットして使用を止める。 |
| `getChestTransform()` | `chestTransform` を返すだけ。 |
| `setNewChestUpVectorValueOnRuntime(Vector3 newValue)` | `chestUpVector` を設定するだけ（エディタ更新は行わない）。 |
| `setNewChestUpVectorValue(Vector3 newValue)` | `chestUpVector` を設定してコンポーネントを更新する。 |
| `setSpineTransform(Transform newTransform)` | `spineTransform` を設定してコンポーネントを更新する。 |
| `setChestTransform(Transform newTransform)` | `chestTransform` を設定してコンポーネントを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent` とシーンのダーティ更新を行うだけ。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static float AngleAroundAxis(Vector3 dirA, Vector3 dirB, Vector3 axis)` | – |
