# wolfCharacterController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `vehicleController`
- **ソース**: `Player/Generic Model Controller/wolfCharacterController.cs:5`

**概要**: 狼型のカスタムキャラクターコントローラ。`vehicleController` を継承し、表面へ向けたモデルの回転や位置補正を行う。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Custom Character Controller Base | `mainCustomCharacterControllerBase` | `customCharacterControllerBase` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Vehicle Transform | `vehicleTransform` | `Transform` | – | – |
| Vehicle Camera Transform | `vehicleCameraTransform` | `Transform` | – | – |

### Other Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Rotate Character Model To Surface Enabled | `rotateCharacterModelToSurfaceEnabled` | `bool` | – | – |
| Max Character X Rotation To Surface | `maxCharacterXRotationToSurface` | `float` | 40 | – |
| Max Character Z Rotation To Surface | `maxCharacterZRotationToSurface` | `float` | 40 | – |
| Character Rotation To Surface Speed | `characterRotationToSurfaceSpeed` | `float` | 10 | – |
| Character Position Adjustment To Surface Speed | `characterPositionAdjustmentToSurfaceSpeed` | `float` | 10 | – |
| Character Rotation To Surface Raycast Distance | `characterRotationToSurfaceRaycastDistance` | `float` | 2.5f | – |
| Min Surface Rotation | `minSurfaceRotation` | `float` | 5 | – |
| Use Reverse Rotation | `useReverseRotation` | `bool` | – | – |
| Ignore Local Z Axis Rotation Enabled | `ignoreLocalZAxisRotationEnabled` | `bool` | – | – |
| Adjust Model Position To Surface Enabled | `adjustModelPositionToSurfaceEnabled` | `bool` | true | – |
| Character Pivot Transform | `characterPivotTransform` | `Transform` | – | – |
| Surface Rotation Layermask | `surfaceRotationLayermask` | `LayerMask` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Turn Amount | `turnAmount` | `float` | – | – |
| Forward Amount | `forwardAmount` | `float` | – | – |
| Current Camera Pivot Transform | `currentCameraPivotTransform` | `Transform` | – | – |
| Current Main Camera Tranform | `currentMainCameraTranform` | `Transform` | – | – |
| Use Forward Direction For Camera Direction | `useForwardDirectionForCameraDirection` | `bool` | – | – |
| Use Right Direction For Camera Direction | `useRightDirectionForCameraDirection` | `bool` | – | – |
| Add Extra Rotation Paused | `addExtraRotationPaused` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCharacterPivotTransform(Transform newTransform)` | `characterPivotTransform` を設定するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`Start()`, `changeGravityControlUse(bool state)`, `changeVehicleState()`, `checkVehicleStateOnPassengerGettingOnOrOff(bool state)`, `disableVehicle()`, `inputHoldOrReleaseBrake(bool holdingButton)`, `inputHoldOrReleaseTurbo(bool holdingButton)`, `inputJump()`, `inputSetTurnOnState()`, `isDrivingActive()`, `setAddExtraRotationPausedState(bool state)`, `setEngineOnOrOffState()`, `setNewMainCameraTransform(Transform newTransform)`, `setNewPlayerCameraTransform(Transform newTransform)`, `setTurnOffState(bool previouslyTurnedOn)`, `setTurnOnState()`, `setUseForwardDirectionForCameraDirectionState(bool state)`, `setUseRightDirectionForCameraDirectionState(bool state)`, `turnOnOrOff(bool state, bool previouslyTurnedOn)`, `updateMovingState()`, `usingBoosting()`

</details>
