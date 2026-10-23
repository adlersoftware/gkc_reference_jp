# hoverBoardController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `vehicleController`
- **ソース**: `Vehicles/Vehicle Controllers/hoverBoardController.cs:6`

**概要**: ホバーボード用コントローラ。複数のホバーエンジン推力、車体安定化トルク、ジャンプ、ブースト、搭乗者アニメーション連携を扱う。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hover Engine List | `hoverEngineList` | `List<hoverEngineSettings>` | new List<hoverEngineSettings> () | – |
| Other Car Parts | `otherCarParts` | `OtherCarParts` | – | – |
| Settings | `settings` | `hoverCraftSettings` | – | – |
| Stability Force | `stabilityForce` | `float` | 1 | – |
| Stability Speed | `stabilitySpeed` | `float` | 2 | – |
| Min Steer Input Idle | `minSteerInputIdle` | `float` | 0.4f | – |
| Min Steer Input Moving | `minSteerInputMoving` | `float` | 0.4f | – |
| Main Hover Board Animation System | `mainHoverBoardAnimationSystem` | `hoverBoardAnimationSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `useVehicleJumpPlatform(Vector3 direction)` | `jumpInputPressed`を0.5秒立て、`direction`×質量のImpulseを与える。 |
| `useJumpPlatformParable(Vector3 direction)` | `direction`を`ForceMode.VelocityChange`で加え、質量非依存の跳ね上げを与える。 |
| `setNewJumpPower(float newJumpPower)` | `jumpPower`を`newJumpPower`で直接上書きするだけ（×100変換なし）。 |
| `setOriginalJumpPower()` | `jumpPower`を保存済みの`originalJumpPower`に戻すだけ。 |
| `setCanJumpState(bool state)` | ジャンプ可否`canJump`を`state`にするだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`Awake()`, `InitializeAudioElements()`, `Start()`, `changeGravityControlUse(bool state)`, `changeVehicleState()`, `disableVehicle()`, `endBrakeVehicleToStopCompletely()`, `enterOrExitFromWayPoint(bool state)`, `getCurrentSpeed()`, `getLastTimeReleasedFromWaypoint()`, `inputHoldOrReleaseBrake(bool holdingButton)`, `inputHoldOrReleaseTurbo(bool holdingButton)`, `inputJump()`, `inputSetTurnOnState()`, `isDrivingActive()`, `isUsingHoverBoardWaypoint()`, `receiveWayPoints(hoverBoardWayPoints wayPoints)`, `setCollisionDetected(Collision currentCollision)`, `setEngineOnOrOffState()`, `setTurnOffState(bool previouslyTurnedOn)`, `setTurnOnState()`, `startBrakeVehicleToStopCompletely()`, `turnOnOrOff(bool state, bool previouslyTurnedOn)`, `updateCameraSteerState()`, `usingBoosting()`, `vehicleUpdate()`

</details>

## 内部型

- `hoverEngineSettings`（class）
- `OtherCarParts`（class）
- `hoverCraftSettings`（class）
