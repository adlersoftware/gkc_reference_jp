# motorBikeController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `vehicleController`
- **ソース**: `Vehicles/Vehicle Controllers/motorBikeController.cs:6`

**概要**: 二輪車用コントローラ。低速時の車体リーンと足の接地調整、スタンドアニメーション、エンジン音、スキッド／排気パーティクルを扱う。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Wheels List | `wheelsList` | `List<Wheels>` | new List<Wheels> () | – |
| Gears List | `gearsList` | `List<Gears>` | new List<Gears> () | – |
| Other Car Parts | `otherCarParts` | `OtherCarParts` | – | – |
| Settings | `settings` | `motorBikeSettings` | – | – |
| Stability Speed | `stabilitySpeed` | `float` | 220 | – |
| Stability Force | `stabilityForce` | `float` | 36 | – |
| Current Gear | `currentGear` | `int` | – | – |
| Current RPM | `currentRPM` | `float` | 0 | – |

### IK and Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Place Driver Feet On Ground On Low Speed | `placeDriverFeetOnGroundOnLowSpeed` | `bool` | – | – |
| Low Speed Chassis Rotation Amount | `lowSpeedChassisRotationAmount` | `float` | 20 | – |
| Minimum Low Speed | `minimumLowSpeed` | `float` | 5 | – |
| Chassis Rotation Speed | `chassisRotationSpeed` | `float` | 1 | – |
| Right Raycast Position To Feet | `rightRaycastPositionToFeet` | `Transform` | – | – |
| Left Raycast Position To Feet | `leftRaycastPositionToFeet` | `Transform` | – | – |
| Foot On Ground Position Offset | `footOnGroundPositionOffset` | `Vector3` | – | – |
| Adjust Feet To Ground Speed | `adjustFeetToGroundSpeed` | `float` | 4 | – |
| Right Foot Transform | `rightFootTransform` | `Transform` | – | – |
| Lef Foot Transform | `lefFootTransform` | `Transform` | – | – |
| Original Right Foot Position | `originalRightFootPosition` | `Transform` | – | – |
| Original Left Foot Position | `originalLeftFootPosition` | `Transform` | – | – |
| Foot Position On Ground Parent | `footPositionOnGroundParent` | `Transform` | – | – |
| Foot Position On Ground | `footPositionOnGround` | `Transform` | – | – |
| Use Stand Animation | `useStandAnimation` | `bool` | – | – |
| Stand Animation Name | `standAnimationName` | `string` | – | – |
| Main Animation | `mainAnimation` | `Animation` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Any On Ground | `anyOnGround` | `bool` | – | – |
| Reversing | `reversing` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Skid Marks Manager | `skidMarksManager` | `skidsManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkDriverFootPosition()` | 低速判定が切り替わった時、進行方向の傾きから接地する足を選び、レイキャスト位置へ足とシャシー傾きを合わせる。 |
| `playStandAnimation(bool playForward)` | `useStandAnimation`が有効なら、スタンドアニメを順再生／逆再生して再生する。 |
| `stopVehicleParticles()` | 全車輪のスキッド粒子と通常・強排気の粒子を停止する。 |
| `useVehicleJumpPlatform(Vector3 direction)` | `direction`に質量を掛けた力を`ForceMode.Impulse`で加えて跳ね上げる。 |
| `useJumpPlatformParable(Vector3 direction)` | `direction`を`ForceMode.VelocityChange`で加え、質量非依存の跳ね上げを与える。 |
| `setNewJumpPower(float newJumpPower)` | `jumpPower`を`newJumpPower`×100に変換して設定するだけ。 |
| `setOriginalJumpPower()` | `jumpPower`を保存済みの`originalJumpPower`に戻すだけ。 |
| `setChassisRotation(Vector3 rotationAmount)` | 進行中の回転を止め、シャシーを`rotationAmount`の角度へ補間するコルーチンを開始する。 |
| `stopSetChassisRotationCoroutine()` | シャシー回転コルーチンがあれば停止するだけ（角度は戻さない）。 |
| `adjustFeetToGround(bool adjustToGround)` | 足位置コルーチンを止め、接地位置（`adjustToGround`がfalseなら元の位置）へ足を補間移動する。 |
| `stopAdjustHoldOnLedgeCoroutine()` | 足位置調整コルーチンがあれば停止するだけ。 |
| `setCanJumpState(bool state)` | ジャンプ可否`canJump`を`state`にするだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`Awake()`, `InitializeAudioElements()`, `Start()`, `changeGravityControlUse(bool state)`, `changeVehicleState()`, `disableVehicle()`, `endBrakeVehicleToStopCompletely()`, `getCurrentSpeed()`, `inputHoldOrReleaseBrake(bool holdingButton)`, `inputHoldOrReleaseTurbo(bool holdingButton)`, `inputHorn()`, `inputJump()`, `inputSetTurnOnState()`, `isDrivingActive()`, `pressHorn()`, `setCollisionDetected(Collision currentCollision)`, `setEngineOnOrOffState()`, `setTurnOffState(bool previouslyTurnedOn)`, `setTurnOnState()`, `startBrakeVehicleToStopCompletely()`, `turnOnOrOff(bool state, bool previouslyTurnedOn)`, `usingBoosting()`, `vehicleUpdate()`

</details>

## 内部型

- `Wheels`（class）
- `wheelType`（enum）
- `OtherCarParts`（class）
- `Gears`（class）
- `motorBikeSettings`（class）
