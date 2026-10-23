# IKSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Animator IK/IKSystem.cs:6`

**概要**: AnimatorのIK（手・肘・頭・体幹）の重みと目標位置を制御し、武器の抜刀/納刀・運転・把持・ジップラインなど各状態に応じた手の配置を切り替える。

## インスペクター設定

### Main Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| IK Speed | `IKSpeed` | `float` | – | Range (1, 10) |
| Right Hand Grabbing ID Name | `rightHandGrabbingIDName` | `string` | "Right Hand Grabbing ID" | – |
| Left Hand Grabbing ID Name | `leftHandGrabbingIDName` | `string` | "Left Hand Grabbing ID" | – |

### IK Body Info State List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| IK Body Info State List | `IKBodyInfoStateList` | `List<IKBodyInfoState>` | new List<IKBodyInfoState> () | – |

### Fire Weapons IK Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fire Weapons Head Weight | `fireWeaponsHeadWeight` | `float` | 1 | – |
| Fire Weapons Body Weight | `fireWeaponsBodyWeight` | `float` | 0 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Current Aim Mode | `currentAimMode` | `aimMode` | – | – |
| Using Hands | `usingHands` | `bool` | – | – |
| Using Weapons | `usingWeapons` | `bool` | – | – |
| Using Dual Weapon | `usingDualWeapon` | `bool` | – | – |
| Disabling Dual Weapons | `disablingDualWeapons` | `bool` | – | – |
| Using Arms | `usingArms` | `bool` | – | – |
| Driving | `driving` | `bool` | – | – |
| Using Zipline | `usingZipline` | `bool` | – | – |
| Disable Weapons | `disableWeapons` | `bool` | – | – |
| IK Body Info Active | `IKBodyInfoActive` | `bool` | – | – |
| Disabling IK Body Info Active | `disablingIKBodyInfoActive` | `bool` | – | – |
| Object Grabbed | `objectGrabbed` | `bool` | – | – |
| IK System Enabled To Grab | `IKSystemEnabledToGrab` | `bool` | – | – |
| Is Third Person View | `isThirdPersonView` | `bool` | – | – |
| Current Head Weight | `currentHeadWeight` | `float` | – | – |
| Head Weight Target | `headWeightTarget` | `float` | – | – |
| IK Body Paused | `IKBodyPaused` | `bool` | – | – |
| Temporal On Animator IK Component | `temporalOnAnimatorIKComponent` | `OnAnimatorIKComponent` | – | – |
| Temporal On Animator IK Component Assigned | `temporalOnAnimatorIKComponentAssigned` | `bool` | – | – |
| Full Body Awareness Active | `fullBodyAwarenessActive` | `bool` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |

### Mount Points Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Right Hand Mount Point | `rightHandMountPoint` | `Transform` | – | – |
| Left Hand Mount Point | `leftHandMountPoint` | `Transform` | – | – |
| Right Lower Arm Mount Point | `rightLowerArmMountPoint` | `Transform` | – | – |
| Left Lower Arm Mount Point | `leftLowerArmMountPoint` | `Transform` | – | – |

### On Animator IK Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hands On Surface IK Component | `handsOnSurfaceIKComponent` | `OnAnimatorIKComponent` | – | – |
| IK Foot System Component | `IKFootSystemComponent` | `OnAnimatorIKComponent` | – | – |
| Head Track IK Component | `headTrackIKComponent` | `OnAnimatorIKComponent` | – | – |
| Bullet Time IK Component | `bulletTimeIKComponent` | `OnAnimatorIKComponent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Right Hand IK Pos | `rightHandIKPos` | `Transform` | – | – |
| Left Hand IK Pos | `leftHandIKPos` | `Transform` | – | – |
| Current Hand IK Pos | `currentHandIKPos` | `Transform` | – | – |
| Right Elbow IK Pos | `rightElbowIKPos` | `Transform` | – | – |
| Left Elbow IK Pos | `leftElbowIKPos` | `Transform` | – | – |
| Current Elbow IK Pos | `currentElbowIKPos` | `Transform` | – | – |
| IK Body COM | `IKBodyCOM` | `Transform` | – | – |
| Animator | `animator` | `Animator` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | – |
| Powers Manager | `powersManager` | `otherPowers` | – | – |
| Settings | `settings` | `IKSettings` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `isFullBodyAwarenessActive()` | `fullBodyAwarenessActive` を返すだけ。 |
| `setFullBodyAwarenessActiveState(bool state)` | `fullBodyAwarenessActive` を設定するだけ。 |
| `setHeadLookState(bool state, float newHeadLookSpeed, Transform newHeadLookTarget)` | 頭の注視を有効化して重み目標を1にし、速度と注視対象を設定する（無効時は目標0）。 |
| `getUsingHands()` | `usingHands` を返すだけ。 |
| `isObjectGrabbed()` | `objectGrabbed` を返すだけ。 |
| `getHeadWeight()` | `currentHeadWeight` を返すだけ。 |
| `isUsingWeapons()` | `usingWeapons` を返すだけ。 |
| `changeArmState(float value)` | 武器照準以外なら `usingArms` を立て、腕のIK目標値を `value` にする（ジップライン中は1）。 |
| `disableArmsState()` | `usingArms` をfalseにし、`IKWeightTargetValue` と `IKWeight` を0にする。 |
| `changeArmSide(bool value)` | 右/左の手と肘のIK位置・ゴール・ヒントを切り替え、距離の初期値を更新する。 |
| `setDrivingState(bool state, IKDrivingSystem.IKDrivingInformation IKPositions)` | 運転状態を切り替え、有効時は座席情報を保存して掴み手IDを設定、無効時はIDとステアリング値をリセットする。 |
| `checkIfDeactivateIKIfNotAimingActive(IKWeaponInfo IKPositions)` | フルボディならfalse、しゃがみ中や `deactivateIKIfNotAiming` 設定時はtrueを返す判定。 |
| `setIKWeaponState(bool state, IKWeaponInfo IKPositions, bool useHandToDrawWeapon, string weaponName)` | 抜刀/納刀に応じて手の移動コルーチンを開始し、`usingWeapons` や掴み手の状態を切り替える。 |
| `checkGrabbingHandsState(bool drawingWeapon, bool useGrabbingHandID, int grabbingHandID, bool isRightHand)` | 掴み手IDを使う設定のとき、抜刀中はIDを設定し、納刀中は0にする。 |
| `setGrabbingHandState(int grabbingHandID, bool isRightHand)` | 無効時は何もせず、右/左のAnimatorの掴み手IDパラメータを設定する。 |
| `checkHandsInPosition(bool drawingWeapon)` | 両手（両武器）が目標位置に着いたかを見て、`handsInPosition` と掴み手IDを更新する。 |
| `setGrabbingHandStateOnSingleHand(bool carryingWeapon, bool isRightHand, bool handInPosition)` | 指定した手に対応する武器の手だけで、位置に応じた掴み手状態を設定する。 |
| `stopIKWeaponsActions()` | 武器用の手移動コルーチンを全て止め、使用中・二丁持ち・無効化の各フラグを解除する。 |
| `quickDrawWeaponState(IKWeaponInfo IKPositions)` | 手移動コルーチンを止めたうえで、即座にIK重みを1（非照準設定時は0）にして武器を構えさせる。 |
| `quickDrawWeaponStateDualWeapon(IKWeaponInfo IKPositions, bool isRigthWeapon)` | 二丁持ちの片側について手移動を止め、即座にIK重みを設定して構え状態にする。 |
| `resetWeaponHandIKWeight()` | `IKWeaponsSettings` 内の全手の `HandIKWeight` を0にする。 |
| `stopIKWeaponHandMovementCoroutine(IKWeaponsPosition IKWeaponPositionToCheck)` | 指定の手に動きコルーチンがあれば停止するだけ。 |
| `quickKeepWeaponState()` | `setDisableWeaponsState(true)` を呼ぶだけ。 |
| `setDisableWeaponsState(bool state)` | 単発・二丁持ち両方の `disable` フラグを `state` に設定する。 |
| `setDisableSingleWeaponState(bool state)` | `disableWeapons` を設定するだけ。 |
| `setDisableDualWeaponsState(bool state)` | `disablingDualWeapons` を設定するだけ。 |
| `disableIKWeight()` | 頭のIK重み（`headWeightTarget` と `currentHeadWeight`）を0にする。 |
| `setUsingWeaponsState(bool state)` | `usingWeapons` を設定するだけ。 |
| `setUsingDualWeaponState(bool state)` | `true` なら `usingDualWeapon`、`false` なら `disablingDualWeapons` を立てる。 |
| `disableUsingDualWeaponState()` | `usingDualWeapon` と `disablingDualWeapons` をfalseにする。 |
| `setIKWeaponsRightHandSettings(IKWeaponInfo IKPositions)` | `IKWeaponsRightHandSettings` を設定するだけ。 |
| `setIKWeaponsLeftHandSettings(IKWeaponInfo IKPositions)` | `IKWeaponsLeftHandSettings` を設定するだけ。 |
| `startRecoil(float recoilSpeed, float recoilAmount)` | 手を銃の反動方向へ後退させて戻すコルーチンを開始し、既存のリコイルは停止する。 |
| `setElbowsIKTargetValue(float leftValue, float rightValue)` | 左手/右手それぞれの肘のIK目標値を設定する。 |
| `setIKHandTargetValue(IKWeaponsPosition IKWeaponPositionToCheck, float newTargetValue)` | 指定の手のIK目標値 `targetValue` を設定するだけ。 |
| `ziplineState(bool state, zipline.IKZiplineInfo IKPositions)` | ジップライン状態を切り替え、有効時は重み目標を1にして設定を保存、無効時は0にしてnullにする。 |
| `setGrabedObjectState(bool state, bool IKSystemEnabledToGrabState, List<grabObjects.handInfo> handInfo)` | 把持状態を設定し、把持中は手ごとの掴み手IDを、解除時は左右ともIDを0にする。 |
| `setIKBodyInfoListOriginalPosition()` | 未取得なら各IKボディ対象の初期ローカル位置を保存する（初回のみ）。 |
| `setIKBodyPausedState(bool state)` | `IKBodyPaused` を設定するだけ。 |
| `isIKBodyPaused()` | `IKBodyPaused` を返すだけ。 |
| `setIKBodyState(bool state, string IKBodyStateName)` | 名前でIKボディ状態を選び、開始位置オフセットと手の重みを設定し、終了時は体の回転を戻す。 |
| `resetBodyRotation()` | `IKBodyCOM` の回転を `IKBodyCOMRotationSpeed` で徐々に元へ戻すコルーチンを開始する。 |
| `getIKBodyCOM()` | `IKBodyCOM` を返すだけ。 |
| `getRightHandMountPoint()` | `rightHandMountPoint` を返すだけ。 |
| `getLeftHandMountPoint()` | `leftHandMountPoint` を返すだけ。 |
| `getRightLowerArmMountPoint()` | `rightLowerArmMountPoint` を返すだけ。 |
| `getLeftLowerArmMountPoint()` | `leftLowerArmMountPoint` を返すだけ。 |
| `setCurrentAimModeType(string newAimModeTypeName)` | `Weapons` なら `aimMode.weapons`、`Powers` なら `aimMode.hands` を設定する。 |
| `stopAllMovementCoroutines()` | リコイル・体回転・武器手移動の各コルーチンをまとめて停止する。 |
| `enableOrDisableIKSystemManagerState(bool state)` | 無効化時は全IK状態を解除し、`enabled` と `componentEnabled` を `state` に合わせる。 |
| `disableAllIKStates()` | 武器・手・頭・IKボディ・運転・ジップライン・把持の各IK状態をまとめて解除する。 |
| `setTemporalOnAnimatorIKComponentActive(OnAnimatorIKComponent newTemporalOnAnimatorIKComponent)` | `setTemporalOnAnimatorIKComponent` を `true` で呼ぶだけ。 |
| `setTemporalOnAnimatorIKComponentDeactivate(OnAnimatorIKComponent newTemporalOnAnimatorIKComponent)` | `setTemporalOnAnimatorIKComponent` を `false` で呼ぶだけ。 |
| `setTemporalOnAnimatorIKComponentActiveIfNotInUse(OnAnimatorIKComponent newTemporalOnAnimatorIKComponent)` | 未割当か同じコンポーネントの場合のみ、一時IKコンポーネントを有効化する。 |
| `removeThisTemporalOnAnimatorIKComponentIfIsCurrent(OnAnimatorIKComponent newTemporalOnAnimatorIKComponent)` | 現在の一時IKコンポーネントと一致する場合のみ解除する。 |
| `setTemporalOnAnimatorIKComponent(OnAnimatorIKComponent newTemporalOnAnimatorIKComponent, bool state)` | 一時IKコンポーネントを保存して `setActiveState(state)` を呼び、割当フラグを更新する。 |
| `checkIfTemporalOnAnimatorIKComponentIfIsCurrent(OnAnimatorIKComponent newTemporalOnAnimatorIKComponent)` | 渡したコンポーネントが現在の一時IKコンポーネントと同一かを返す。 |
| `setIsThirdPersonViewState(bool state)` | `isThirdPersonView` を設定するだけ。 |
| `setFireWeaponsHeadWeight(float newValue)` | `fireWeaponsHeadWeight` を設定するだけ。 |

## 内部型

- `aimMode`（enum）
- `IKSettings`（class）
- `IKBodyInfoState`（class）
- `IKBodyInfo`（class）
