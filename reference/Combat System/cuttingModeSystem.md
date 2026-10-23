# cuttingModeSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/Slice System/cuttingModeSystem.cs:6`

**概要**: スライス用のカットモードを管理し、パネル回転・カメラ・アニメータ・スタミナ・バレットタイムを連動させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Cutting Panel Rotation Speed | `cuttingPanelRotationSpeed` | `float` | 5 | – |
| Cutting Speed | `cuttingSpeed` | `float` | 10 | – |
| Player Can Move On Cutting Mode Active | `playerCanMoveOnCuttingModeActive` | `bool` | true | – |
| Use Camera State On Cutting Mode | `useCameraStateOnCuttingMode` | `bool` | – | – |
| Camera State Name On Cutting Mode | `cameraStateNameOnCuttingMode` | `string` | – | – |
| Set Bullet Time | `setBulletTime` | `bool` | – | – |
| Bullet Time Scale | `bulletTimeScale` | `float` | – | – |
| Delay To Set Bullet Time | `delayToSetBulletTime` | `float` | – | – |
| Can Toggle Camera Rotation | `canToggleCameraRotation` | `bool` | – | – |
| Pause Camera Rotation At Start On Cut Mode Active | `pauseCameraRotationAtStartOnCutModeActive` | `bool` | true | – |

### Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Cutting Mode State ID | `cuttingModeStateID` | `int` | 50000 | – |
| Cutting Mode Action Active Name | `cuttingModeActionActiveName` | `string` | "Action Active Upper Body" | – |
| Cutting Mode Action ID Name | `cuttingModeActionIDName` | `string` | "Action ID" | – |
| Horizontal Animator Name | `horizontalAnimatorName` | `string` | "Horizontal Action" | – |
| Vertical Animator Name | `verticalAnimatorName` | `string` | "Vertical Action" | – |

### Stamina Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Stamina On Slice Enabled | `useStaminaOnSliceEnabled` | `bool` | true | – |
| Slice Stamina State | `sliceStaminaState` | `string` | "Slice Object" | – |
| Stamina To Use On Slice | `staminaToUseOnSlice` | `float` | 10 | – |
| Custom Refill Stamina Delay After Slice | `customRefillStaminaDelayAfterSlice` | `float` | – | – |
| General Stamina Use Multiplier | `generalStaminaUseMultiplier` | `float` | 1 | – |

### Other

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Head Track Body Weight On Aim | `headTrackBodyWeightOnAim` | `float` | 1 | – |
| Custom Aim Reticle Name | `customAimReticleName` | `string` | "Reticle 1" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Cutting Mode Active | `cuttingModeActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Cutting Mode Start | `eventOnCuttingModeStart` | `UnityEvent` | – | – |
| Event On Cutting Mode End | `eventOnCuttingModeEnd` | `UnityEvent` | – | – |
| Event On Cutting | `eventOnCutting` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Cut Particles Parent | `cutParticlesParent` | `Transform` | – | – |
| Cutting Panel Game Object | `cuttingPanelGameObject` | `GameObject` | – | – |
| Cutting Panel Transform | `cuttingPanelTransform` | `Transform` | – | – |
| Cutting Panel Transform Reference | `cuttingPanelTransformReference` | `Transform` | – | – |
| Cutting Panel First Reference Transform | `cuttingPanelFirstReferenceTransform` | `Transform` | – | – |
| Cutting Panel Second Reference Transform | `cuttingPanelSecondReferenceTransform` | `Transform` | – | – |
| Cutting Direction Transform | `cuttingDirectionTransform` | `Transform` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Player Input Manager | `mainPlayerInputManager` | `playerInputManager` | – | – |
| Time Bullet Manager | `timeBulletManager` | `timeBullet` | – | – |
| Main Stamina System | `mainStaminaSystem` | `staminaSystem` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setSliceInputPausedForStaminaState(bool state)` | スタミナ不足で斬撃入力を止めるかどうかのフラグ`sliceInputPausedForStamina`を設定するだけ。 |
| `inputToggleCameraRotation()` | カットモード中かつ`canToggleCameraRotation`が有効なとき、パネル回転とカメラ回転状態を反転させる。 |
| `inputActivateCut()` | カットモード中ならスタミナを消費して斬撃コルーチンを開始し、パーティクルと切断方向を180度反転して`eventOnCutting`を呼ぶ。 |
| `setCuttingModeActiveState(bool state)` | カットモードを開始/終了し、パネル表示・カメラ状態・アニメータ・移動可否・バレットタイム・イベントをまとめて切り替える。 |
| `checkSetBulletTime()` | `setBulletTime`が有効ならコルーチンを止め、モード中は遅延後に開始、終了時は即解除する。 |
| `stopCheckSetBulletTimeCoroutine()` | バレットタイム設定用コルーチン`bulletTimeCoroutine`を停止するだけ。 |
| `stopActivateCutCoroutine()` | 斬撃パネル移動コルーチン`moveReferencePanelOnCutCoroutine`を停止するだけ。 |
| `setGeneralStaminaUseMultiplierValue(float newValue)` | 斬撃時のスタミナ消費に掛ける`generalStaminaUseMultiplier`を設定するだけ。 |
| `setUseStaminaOnSliceEnabledState(bool state)` | 斬撃でスタミナを消費するか`useStaminaOnSliceEnabled`を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCuttingModeStart` | `UnityEvent` | – |
| `eventOnCuttingModeEnd` | `UnityEvent` | – |
| `eventOnCutting` | `UnityEvent` | – |
