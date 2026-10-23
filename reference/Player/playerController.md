# playerController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/playerController.cs:7`

**概要**: プレイヤーの移動・回転・ジャンプ・接地判定・カメラ方向注視やIK・メッシュ・各種状態フラグを統括する中核コンポーネント。武器やカメラなど外部マネージャーへの問い合わせと設定を公開する。

**公式ドキュメント抜粋**（[Player Controller](../../docs/player-controller-components/player-controller.md)）

> This is the main player gameObject itself, though the humanoid AI uses most of the same components than the player to work, which allows to make these components easy to manage and extend, and have available any element/system that is added to the player for the AI, without major modifications or additions. This contains the next main elements:

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Movement Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Air Speed | `airSpeed` | `float` | 6 | 空中で入力に応じて出る横移動の速度。 |
| Air Control | `airControl` | `float` | 2 | 空中で速度を入力方向へ寄せる補間の強さ。 |
| Ignore Player Extra Rotation On Air Enabled | `ignorePlayerExtraRotationOnAirEnabled` | `bool` | – | オンにすると空中では移動方向への追加回転を止める。 |
| Stationary Turn Speed | `stationaryTurnSpeed` | `float` | 180 | 停止時に体を回す速さ（度/秒）。 |
| Moving Turn Speed | `movingTurnSpeed` | `float` | 200 | 移動中に進行方向へ体を回す速さ（度/秒）。 |
| Use Turn Speed On Aim | `useTurnSpeedOnAim` | `bool` | true | オンにするとエイム中も上記の旋回速度を使う。 |
| Auto Turn Speed | `autoTurnSpeed` | `float` | 2 | カメラ方向へ自動で向きを変える補間の速さ。 |
| Aim Turn Speed | `aimTurnSpeed` | `float` | 10 | エイム中にカメラ方向へ向く補間の速さ。 |
| Threshold Angle Difference | `thresholdAngleDifference` | `float` | 5 | カメラとの角度差がこの値を超えると旋回を始める閾値。 |
| Regular Movement On Bullet Time | `regularMovementOnBulletTime` | `bool` | – | オンにするとバレットタイム中も通常の速度で動く。 |
| Use Move Inpupt Magnitede To Forward Amount | `useMoveInpuptMagnitedeToForwardAmount` | `bool` | – | オンにすると入力の大きさを前進量として扱う。 |

### Main Capsule Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Custom Capsule Center | `setCustomCapsuleCenter` | `bool` | – | オンにすると`CapsuleCollider`の中心を手動値で設定する。 |
| Custom Capsule Center | `customCapsuleCenter` | `Vector3` | – | 立ち状態でのカプセル中心の位置。 / 表示条件: `setCustomCapsuleCenter` がオンのとき |
| Custom Capsule Center On Crouch | `customCapsuleCenterOnCrouch` | `Vector3` | – | しゃがみ状態でのカプセル中心の位置。 / 表示条件: `setCustomCapsuleCenter` がオンのとき |

### Animator Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Base Layer Index | `baseLayerIndex` | `int` | 0 | 状態取得に使うAnimatorのベースレイヤー番号。 |
| Input Horizontal Lerp Speed | `inputHorizontalLerpSpeed` | `float` | 0.03f | 水平入力のAnimator値の補間時間（秒）。 |
| Input Vertical Lerp Speed | `inputVerticalLerpSpeed` | `float` | 0.03f | 垂直入力のAnimator値の補間時間（秒）。 |
| Input Strafe Horizontal Lerp Speed | `inputStrafeHorizontalLerpSpeed` | `float` | 0.3f | ストレイフ時の水平入力値の補間時間。 |
| Input Strafe Vertical Lerp Speed | `inputStrafeVerticalLerpSpeed` | `float` | 0.3f | ストレイフ時の垂直入力値の補間時間。 |
| Animator Forward Input Lerp Speed | `animatorForwardInputLerpSpeed` | `float` | 0.1f | `Forward`パラメータを補間して渡す時間。 |
| Animator Turn Input Lerp Speed | `animatorTurnInputLerpSpeed` | `float` | 0.1f | `Turn`パラメータを補間して渡す時間。 |
| Move Speed Multiplier | `moveSpeedMultiplier` | `float` | 1 | ルートモーションの移動量に掛ける倍率。 |
| Anim Speed Multiplier | `animSpeedMultiplier` | `float` | 1 | 移動中のAnimator再生速度に掛ける倍率。 |
| Min Time To Set Idle On Strafe | `minTimeToSetIdleOnStrafe` | `float` | 0.5f | 入力停止から待機と判定するまでの待ち時間。 |
| Override Animation Speed Active | `overrideAnimationSpeedActive` | `bool` | – | オンにすると常に上記倍率でAnimatorを再生する。 |
| Character Radius | `characterRadius` | `float` | – | 汎用モデル使用時に接地判定へ渡すカプセル半径。 |

### Animator ID State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Idle ID | `currentIdleID` | `float` | – | 待機アニメの種類を選ぶAnimatorのID値。 |
| Current Strafe ID | `currentStrafeID` | `int` | – | ストレイフアニメの種類を選ぶAnimatorのID値。 |
| Current Air ID | `currentAirID` | `int` | – | 空中アニメの種類を選ぶAnimatorのID値。 |
| Current Crouch ID | `currentCrouchID` | `int` | – | しゃがみアニメの種類を選ぶAnimatorのID値。 |
| Current Use Strafe Landing | `currentUseStrafeLanding` | `int` | 0 | 着地にストレイフ用アニメを使うか示すID値。 |

### Tank Controls Animator Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Input Tank Controls Horizontal Lerp Speed | `inputTankControlsHorizontalLerpSpeed` | `float` | 0.3f | タンク操作時の水平入力値の補間時間。 |
| Input Tank Controls Vertical Lerp Speed | `inputTankControlsVerticalLerpSpeed` | `float` | 0.3f | タンク操作時の垂直入力値の補間時間。 |
| Input Tank Controls Horizontal Strafe Lerp Speed | `inputTankControlsHorizontalStrafeLerpSpeed` | `float` | 0.06f | タンク操作のストレイフ水平値の補間時間。 |
| Input Tank Controls Vertical Strafe Lerp Speed | `inputTankControlsVerticalStrafeLerpSpeed` | `float` | 0.06f | タンク操作のストレイフ垂直値の補間時間。 |

### Player Status ID Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Status ID | `playerStatusID` | `int` | – | 状態に応じたアニメを切り替えるAnimatorのID。 |
| Player Status ID Lerp Speed | `playerStatusIDLerpSpeed` | `float` | 0.1f | 状態IDの値を補間して切り替える速さ。 |

### Ground Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | 地面判定のレイキャストが対象とするレイヤー。 |
| Ray Distance | `rayDistance` | `float` | – | 足元の地面を探すレイキャストの距離。 |
| Update Foot Step State Active | `updateFootStepStateActive` | `bool` | true | オンにすると足音の状態を`stepManager`へ通知する。 |
| Check If Surface Below Is Terrain Enabled | `checkIfSurfaceBelowIsTerrainEnabled` | `bool` | true | オンにすると足元が`Terrain`かどうかを判定する。 |
| Use Sphere Raycast For Ground Detection | `useSphereRaycastForGroundDetection` | `bool` | – | オンにすると地面判定を球体キャストで行う。 |
| Sphere Cast Radius | `sphereCastRadius` | `float` | 0.4f | 地面判定の球体キャストの半径。 / 表示条件: `useSphereRaycastForGroundDetection` がオンのとき |
| Max Distance Sphere Cast | `maxDistanceSphereCast` | `float` | 0.5f | 球体キャストで地面を探す最大距離。 / 表示条件: `useSphereRaycastForGroundDetection` がオンのとき |
| Sphere Cast Offset | `sphereCastOffset` | `float` | – | 球体キャストの開始位置を上下にずらす量。 / 表示条件: `useSphereRaycastForGroundDetection` がオンのとき |
| Max Extra Raycast Distance To Ground Detection | `maxExtraRaycastDistanceToGroundDetection` | `float` | 0.4f | 地面判定に追加する余分なレイ距離。 |

### Ground Adherence Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use New Ground Adherence Enabled | `useNewGroundAdherenceEnabled` | `bool` | – | オンにすると新しい地面追従システムを使う。 / Improved ground adherence with better settings and movement |
| Ground Raycast Distance | `groundRaycastDistance` | `float` | 2f | 頭上から地面までの距離で行う探索の長さ。 / 表示条件: `useNewGroundAdherenceEnabled` がオンのとき / Distance to check the ground below the player with raycast |
| Ground Lerp Speed | `groundLerpSpeed` | `float` | 15f | 地面の高さへ位置を合わせる補間速度。 / 表示条件: `useNewGroundAdherenceEnabled` がオンのとき / Speed to adjust the player to the surface detected on the movement or idle |
| Max Step Height | `maxStepHeight` | `float` | 0.5f | 乗り越えられる段差の最大高さ。 / 表示条件: `useNewGroundAdherenceEnabled` がオンのとき / Max height for steps or stairs on the surface |
| Max Slope Angle | `maxSlopeAngle` | `float` | 45f | 歩行できる坂の傾斜角の上限値。 / 表示条件: `useNewGroundAdherenceEnabled` がオンのとき / Max surface slope that the player can walk |
| Raycast Distance On Sphere Cast On Idle | `raycastDistanceOnSphereCastOnIdle` | `float` | 0.75f | 待機時に地面を探す球体キャストの距離。 / 表示条件: `useNewGroundAdherenceEnabled` がオンのとき / Raycast distance to check surface below the player on idle |
| Height Diff Raycast Radius | `heightDiffRaycastRadius` | `float` | 1.5f | 段差検出のため周囲の高さ差を調べる半径。 / 表示条件: `useNewGroundAdherenceEnabled` がオンのとき / Radius to check for height difference around the player center position, to check for steps |
| Raycast Position Range | `raycastPositionRange` | `float` | 1 | 移動入力方向へレイ判定位置をずらす割合。 / 表示条件: `useNewGroundAdherenceEnabled` がオンのとき / Raycast range around the player position used for the movement input / Range (0, 1) |
| Min Angle To Used Input Normalized | `minAngleToUsedInputNormalized` | `float` | 25 | この角度以上の坂で正規化入力を補正に使う閾値。 / 表示条件: `useNewGroundAdherenceEnabled` がオンのとき / Min angle to use normalized input value, to allow better movement on slopes |
| Duration To Walk To Step | `durationToWalkToStep` | `float` | 0.5f | 検出した段差へ移動し終えるまでの時間。 / 表示条件: `useNewGroundAdherenceEnabled` がオンのとき / Duration that the player takes to be moved to the step detected |
| Check Step Raycast Height | `checkStepRaycastHeight` | `float` | 0.2f | 段差確認レイの足元からの高さ。 / 表示条件: `useNewGroundAdherenceEnabled` がオンのとき / Min height to check for steps in front of the player, using the feet as center position |
| Check Step Raycast Distance | `checkStepRaycastDistance` | `float` | 0.2f | 段差確認レイに足す追加の探索距離。 / 表示条件: `useNewGroundAdherenceEnabled` がオンのとき / Extra distance to check for steps around player's center |
| Use Max Walk Surface Angle | `useMaxWalkSurfaceAngle` | `bool` | – | オンにすると歩ける角度の上限を超えたら空中状態にする。 / 表示条件: `useNewGroundAdherenceEnabled` がオンのとき / Max surface to walk, higher slopes will make the player to enter on air state |
| Max Walk Surface Angle | `maxWalkSurfaceAngle` | `float` | – | 歩行可能な地面の傾斜角の上限値。 / 表示条件: `useNewGroundAdherenceEnabled.boolValue && useMaxWalkSurfaceAngle.boolValue` |
| Use Max Distance To Check Surface Angle | `useMaxDistanceToCheckSurfaceAngle` | `bool` | – | オンにすると角度上限の判定に地面との距離も使う。 / 表示条件: `useNewGroundAdherenceEnabled.boolValue && useMaxWalkSurfaceAngle.boolValue` |
| Max Distance To Check Surface Angle | `maxDistanceToCheckSurfaceAngle` | `float` | – | 角度上限を判定する時の地面との距離閾値。 / 表示条件: `useMaxWalkSurfaceAngle.boolValue && useMaxDistanceToCheckSurfaceAngle.boolValue` |
| Regular Ground Adherence | `regularGroundAdherence` | `float` | 5 | 平地で地面の高さへ吸い付く速度。 |
| Slopes Ground Adherence Up | `slopesGroundAdherenceUp` | `float` | 2 | 上り坂で地面の高さへ吸い付く速度。 |
| Slopes Ground Adherence Down | `slopesGroundAdherenceDown` | `float` | 4 | 下り坂で地面の高さへ吸い付く速度。 |
| Max Ray Distance Range | `maxRayDistanceRange` | `float` | 0.5f | レイ位置を移動入力方向へずらす最大量。 / Range (0, 1) |
| Max Slope Ray Distance | `maxSlopeRayDistance` | `float` | 0.5f | 坂でレイ位置をずらす最大の距離。 / Range (0, 1) |
| Max Stairs Ray Distance | `maxStairsRayDistance` | `float` | 0.5f | 階段でレイ位置をずらす最大量。 / Range (0, 1) |
| Use Max Walk Surface Angle | `useMaxWalkSurfaceAngle` | `bool` | – | オンにすると歩ける角度の上限を超えたら空中状態にする。 / Max surface to walk, higher slopes will make the player to enter on air state |
| Max Walk Surface Angle | `maxWalkSurfaceAngle` | `float` | – | 歩行可能な地面の傾斜角の上限値。 / 表示条件: `useMaxWalkSurfaceAngle` がオンのとき |
| Use Max Distance To Check Surface Angle | `useMaxDistanceToCheckSurfaceAngle` | `bool` | – | オンにすると角度上限の判定に地面との距離も使う。 / 表示条件: `useMaxWalkSurfaceAngle` がオンのとき |
| Max Distance To Check Surface Angle | `maxDistanceToCheckSurfaceAngle` | `float` | – | 角度上限を判定する時の地面との距離閾値。 / 表示条件: `useMaxWalkSurfaceAngle.boolValue && useMaxDistanceToCheckSurfaceAngle.boolValue` |
| Use Max Slope Inclination | `useMaxSlopeInclination` | `bool` | true | オンにすると坂の角度が範囲外なら接地扱いにしない。 |
| Max Slope Inclination | `maxSlopeInclination` | `float` | 80 | 接地と見なす坂の傾斜角の上限値。 / 表示条件: `useMaxSlopeInclination` がオンのとき |
| Min Slope Inclination | `minSlopeInclination` | `float` | -80 | 接地と見なす坂の最小傾斜角（下り側）。 / 表示条件: `useMaxSlopeInclination` がオンのとき |

### Stairs Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Stairs Min Value | `stairsMinValue` | `float` | 0.2f | 段差と判定する高さの下限の値。 |
| Stairs Max Value | `stairsMaxValue` | `float` | 0.25f | 段差と判定する高さの上限の値。 |
| Stairs Ground Adherence | `stairsGroundAdherence` | `float` | 8 | 階段を上る時に地面へ追従する速度。 |
| Check Stairs With Inclination | `checkStairsWithInclination` | `bool` | – | オンにすると傾斜角で階段かどうかを判定する。 |
| Min Stair Inclination | `minStairInclination` | `float` | -10 | 階段と判定する傾斜角の下限値。 / 表示条件: `checkStairsWithInclination` がオンのとき |
| Max Stair Inclination | `maxStairInclination` | `float` | 10 | 階段と判定する傾斜角の上限値。 / 表示条件: `checkStairsWithInclination` がオンのとき |
| Check For Stair Adherence System | `checkForStairAdherenceSystem` | `bool` | – | オンにすると足元の`stairAdherenceSystem`の値を使う。 |

### Current Stairs Adherence (DEBUG)

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Stair Adherence System Min Value | `currentStairAdherenceSystemMinValue` | `float` | – | 取得した階段判定の下限値（デバッグ表示）。 / 表示条件: `checkForStairAdherenceSystem` がオンのとき |
| Current Stair Adherence System Max Value | `currentStairAdherenceSystemMaxValue` | `float` | – | 取得した階段判定の上限値（デバッグ表示）。 / 表示条件: `checkForStairAdherenceSystem` がオンのとき |
| Current Stair Adherence System Adherence Value | `currentStairAdherenceSystemAdherenceValue` | `float` | – | 取得した階段の追従速度（デバッグ表示）。 / 表示条件: `checkForStairAdherenceSystem` がオンのとき |

### Walk/Run/Sprint Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Walk Speed | `walkSpeed` | `float` | 1 | 移動入力に掛ける速度係数（0〜1）。 / Range (0, 1) |
| Increase Walk Speed Enabled | `increaseWalkSpeedEnabled` | `bool` | – | オンにすると走り入力で増速アクションを使える。 |
| Increase Walk Speed Value | `increaseWalkSpeedValue` | `float` | 1 | 増速時に設定する速度係数の値。 / 表示条件: `increaseWalkSpeedEnabled` がオンのとき |
| Hold Button To Keep Increased Walk Speed | `holdButtonToKeepIncreasedWalkSpeed` | `bool` | – | オンにするとボタンを押している間だけ増速する。 / 表示条件: `increaseWalkSpeedEnabled` がオンのとき |
| Walk Run Tip | `walkRunTip` | `string` | "Set 'Sprint Enabled' field to false … | 歩きと走りの設定例を示すInspector用メモ。 / TextArea (3, 8) |

### Sprint Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sprint Enabled | `sprintEnabled` | `bool` | true | オンにするとスプリントできる。 |
| Change Camera Fov On Sprint | `changeCameraFovOnSprint` | `bool` | true | オンにすると三人称でスプリント中にFOVを変える。 / 表示条件: `sprintEnabled` がオンのとき |
| Shake Camera On Sprint Third Person | `shakeCameraOnSprintThirdPerson` | `bool` | true | オンにすると三人称でスプリント中にカメラを揺らす。 / 表示条件: `sprintEnabled` がオンのとき |
| Sprint Third Person Camera Shake Name | `sprintThirdPersonCameraShakeName` | `string` | "Sprint Shake" | スプリント時に使うカメラシェイクの名前。 / 表示条件: `sprintEnabled` がオンのとき |
| Use Secondary Sprint Values | `useSecondarySprintValues` | `bool` | true | オンにするとスプリント専用の移動値を使う。 / 表示条件: `sprintEnabled` がオンのとき |
| Sprint Velocity | `sprintVelocity` | `float` | 1 | スプリント時に設定する速度係数。 / 表示条件: `sprintEnabled.boolValue && useSecondarySprintValues.boolValue` |
| Sprint Jump Power | `sprintJumpPower` | `float` | 15 | スプリント中に適用されるジャンプ力。 / 表示条件: `sprintEnabled.boolValue && useSecondarySprintValues.boolValue` |
| Sprint Air Speed | `sprintAirSpeed` | `float` | 20 | スプリント中に適用される空中速度。 / 表示条件: `sprintEnabled.boolValue && useSecondarySprintValues.boolValue` |
| Sprint Air Control | `sprintAirControl` | `float` | 4 | スプリント中の空中での操作の効き。 / 表示条件: `sprintEnabled.boolValue && useSecondarySprintValues.boolValue` |
| Run On Crouch Enabled | `runOnCrouchEnabled` | `bool` | true | オンにするとしゃがんだまま走れる。 / 表示条件: `sprintEnabled` がオンのとき |

### Root Motion Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Root Motion Active | `useRootMotionActive` | `bool` | true | オンにするとアニメのルートモーションで移動する。 |
| No Root Lerp Speed | `noRootLerpSpeed` | `float` | – | ルートモーション無効時に移動速度を補間する速さ。 / 表示条件: `useRootMotionActive` がオフのとき |
| No Root Walk Movement Speed | `noRootWalkMovementSpeed` | `float` | – | ルートモーション無効時の歩き速度。 / 表示条件: `useRootMotionActive` がオフのとき |
| No Root Run Movement Speed | `noRootRunMovementSpeed` | `float` | – | ルートモーション無効時の走り速度。 / 表示条件: `useRootMotionActive` がオフのとき |
| No Root Sprint Movement Speed | `noRootSprintMovementSpeed` | `float` | – | ルートモーション無効時のスプリント速度。 / 表示条件: `useRootMotionActive` がオフのとき |
| No Root Crouch Movement Speed | `noRootCrouchMovementSpeed` | `float` | – | ルートモーション無効時のしゃがみ速度。 / 表示条件: `useRootMotionActive` がオフのとき |
| No Root Crouch Run Movement Speed | `noRootCrouchRunMovementSpeed` | `float` | 4 | ルートモーション無効時のしゃがみ走り速度。 / 表示条件: `useRootMotionActive` がオフのとき |
| No Root Walk Strafe Movement Speed | `noRootWalkStrafeMovementSpeed` | `float` | – | ルートモーション無効時のストレイフ歩き速度。 / 表示条件: `useRootMotionActive` がオフのとき |
| No Root Run Strafe Movement Speed | `noRootRunStrafeMovementSpeed` | `float` | – | ルートモーション無効時のストレイフ走り速度。 / 表示条件: `useRootMotionActive` がオフのとき |
| No Root Delay To Move On Land | `noRootDelayToMoveOnLand` | `float` | 0.2f | 着地後、移動を再開するまでの待ち時間。 / 表示条件: `useRootMotionActive` がオフのとき |
| Disable Root Motion Temporaly On Land Third Person | `disableRootMotionTemporalyOnLandThirdPerson` | `bool` | – | オンにすると三人称の着地時にルートモーションを止める。 |
| Duration Disable Root Motion Temporaly On Land Third Person | `durationDisableRootMotionTemporalyOnLandThirdPerson` | `float` | – | 着地時にルートモーションを止めておく時間。 / 表示条件: `disableRootMotionTemporalyOnLandThirdPerson` がオンのとき |
| Wait To Disable Root Motion Temporaly On Land Third Person | `waitToDisableRootMotionTemporalyOnLandThirdPerson` | `float` | – | 着地してからルートモーションを止めるまでの待ち時間。 / 表示条件: `disableRootMotionTemporalyOnLandThirdPerson` がオンのとき |
| Use Root Motion On Full Body Awareness | `useRootMotionOnFullBodyAwareness` | `bool` | – | オンにすると`FBA`中もルートモーションで動く。 |

### Player ID Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player ID | `playerID` | `int` | – | このプレイヤーを識別するID。 |
| Player Is Non Local Avatar | `playerIsNonLocalAvatar` | `bool` | – | オンにするとこのキャラを他プレイヤーのアバターとして扱う。 |
| Player Non Local Avatar ID | `playerNonLocalAvatarID` | `int` | – | 非ローカルアバターとしての識別ID。 |

### AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Used By AI | `usedByAI` | `bool` | – | オンにすると入力の代わりにAIがこのプレイヤーを動かす。 |

### First Person No Animator Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| No Animator Speed | `noAnimatorSpeed` | `float` | – | アニメーター無し移動で速度に掛ける係数。 |
| No Animator Walk Movement Speed | `noAnimatorWalkMovementSpeed` | `float` | – | アニメーター無し時の歩き速度。 |
| No Animator Run Movement Speed | `noAnimatorRunMovementSpeed` | `float` | – | アニメーター無し時の走り速度。 / 表示条件: `noAnimatorCanRun` がオンのとき |
| No Animator Crouch Movement Speed | `noAnimatorCrouchMovementSpeed` | `float` | – | アニメーター無し時のしゃがみ速度。 |
| No Animator Run Crouch Movement Speed | `noAnimatorRunCrouchMovementSpeed` | `float` | – | アニメーター無し時のしゃがみ走り速度。 |
| No Animator Strafe Movement Speed | `noAnimatorStrafeMovementSpeed` | `float` | – | アニメーター無し時のストレイフ速度。 |
| No Animator Can Run | `noAnimatorCanRun` | `bool` | – | オンにするとアニメーター無しでも走れる。 |
| No Animator Walk Backward Movement Speed | `noAnimatorWalkBackwardMovementSpeed` | `float` | – | アニメーター無し時の後退歩き速度。 |
| No Animator Run Backward Movement Speed | `noAnimatorRunBackwardMovementSpeed` | `float` | – | アニメーター無し時の後退走り速度。 / 表示条件: `noAnimatorCanRunBackwards` がオンのとき |
| No Animator Crouch Backward Movement Speed | `noAnimatorCrouchBackwardMovementSpeed` | `float` | – | アニメーター無し時の後退しゃがみ速度。 |
| No Animator Run Crouch Backward Movement Speed | `noAnimatorRunCrouchBackwardMovementSpeed` | `float` | – | アニメーター無し時の後退しゃがみ走り速度。 |
| No Animator Strafe Backward Movement Speed | `noAnimatorStrafeBackwardMovementSpeed` | `float` | – | アニメーター無し時の後退ストレイフ速度。 |
| No Animator Can Run Backwards | `noAnimatorCanRunBackwards` | `bool` | – | オンにすると後退時にも走れる。 |
| No Animator Air Speed | `noAnimatorAirSpeed` | `float` | 11 | アニメーター無し時の空中移動速度。 |
| Max Velocity Change | `maxVelocityChange` | `float` | – | 物理移動で一度に加える速度変化の上限。 |
| No Animator Movement Speed Multiplier | `noAnimatorMovementSpeedMultiplier` | `float` | 1 | アニメーター無し移動の速度に掛ける倍率。 |

### Ground Adherence Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| No Animator Slopes Ground Adherence Up | `noAnimatorSlopesGroundAdherenceUp` | `float` | 1 | アニメーター無し時の上り坂の追従速度。 / 表示条件: `useNewGroundAdherenceEnabled` がオフのとき |
| No Animator Slopes Ground Adherence Down | `noAnimatorSlopesGroundAdherenceDown` | `float` | 8 | アニメーター無し時の下り坂の追従速度。 / 表示条件: `useNewGroundAdherenceEnabled` がオフのとき |
| No Animator Stairs Ground Adherence | `noAnimatorStairsGroundAdherence` | `float` | 2 | アニメーター無し時の階段の追従速度。 / 表示条件: `useNewGroundAdherenceEnabled` がオフのとき |

### Sprint Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Sprint | `useEventOnSprint` | `bool` | – | オンにするとスプリント開始と終了でイベントを呼ぶ。 / 表示条件: `sprintEnabled` がオンのとき |
| Event On Start Sprint | `eventOnStartSprint` | `UnityEvent` | – | スプリント開始時に実行する処理。 / 表示条件: `sprintEnabled.boolValue && useEventOnSprint.boolValue` |
| Event On Stop Sprint | `eventOnStopSprint` | `UnityEvent` | – | スプリント終了時に実行する処理。 / 表示条件: `sprintEnabled.boolValue && useEventOnSprint.boolValue` |

### Look In Camera Direction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Look Always In Camera Direction | `lookAlwaysInCameraDirection` | `bool` | – | オンにすると常にカメラの向きへ体を向ける。 |
| Look In Camera Direction If Looking At Target | `lookInCameraDirectionIfLookingAtTarget` | `bool` | – | オンにするとカメラが対象を捉えている間だけ向ける。 |
| Look Only If Moving | `lookOnlyIfMoving` | `bool` | – | オンにすると移動入力がある時だけカメラ方向を向く。 / 表示条件: `lookAlwaysInCameraDirection.boolValue \|\| lookInCameraDirectionIfLookingAtTarget.boolValue` |
| Disable Look Always In Camera Direction If Increase Walk Speed Active | `disableLookAlwaysInCameraDirectionIfIncreaseWalkSpeedActive` | `bool` | – | オンにすると増速中はカメラ方向を向かない。 / 表示条件: `lookAlwaysInCameraDirection.boolValue \|\| lookInCameraDirectionIfLookingAtTarget.boolValue` |
| Look In Camera Direction On Crouch State | `lookInCameraDirectionOnCrouchState` | `bool` | – | オンにするとしゃがみ中もカメラ方向を向く。 / 表示条件: `lookAlwaysInCameraDirection.boolValue \|\| lookInCameraDirectionIfLookingAtTarget.boolValue` |
| Default Strafe Walk Speed | `defaultStrafeWalkSpeed` | `float` | 1 | ストレイフ歩き時にAnimatorへ渡す速度値。 |
| Default Strafe Run Speed | `defaultStrafeRunSpeed` | `float` | 2 | ストレイフ走り時にAnimatorへ渡す速度値。 |
| Rotate Directly Toward Camera On Strafe | `rotateDirectlyTowardCameraOnStrafe` | `bool` | – | オンにするとストレイフ中は直接カメラ方向へ回転する。 |
| Strafe Lerp Speed | `strafeLerpSpeed` | `float` | 0.1f | 速度値をAnimatorへ補間して渡す速さ。 |
| Ignore Strafe State On Air Enabled | `ignoreStrafeStateOnAirEnabled` | `bool` | true | オンにすると空中でもストレイフ状態を維持する。 |
| Update Use Strafe Landing Enabled | `updateUseStrafeLandingEnabled` | `bool` | – | オンにすると着地用ストレイフ値の更新を行う。 |

### Quick Movement Turn Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Quick Movement Turn180 Degrees On Run | `checkQuickMovementTurn180DegreesOnRun` | `bool` | – | オンにすると走行中の180度切り返しを検出する。 |
| Min Delay To Activate Quick Movement Turn180 On Run | `minDelayToActivateQuickMovementTurn180OnRun` | `float` | 2 | 切り返しと判定するまでの最小入力間隔（秒）。 / 表示条件: `checkQuickMovementTurn180DegreesOnRun` がオンのとき |
| Quick Turn Movement Duration Walking | `quickTurnMovementDurationWalking` | `float` | 1 | 歩き時のクイックターンの再生時間。 / 表示条件: `checkQuickMovementTurn180DegreesOnRun` がオンのとき |
| Quick Turn Movement Duration Running | `quickTurnMovementDurationRunning` | `float` | 0.8f | 走り時のクイックターンの再生時間。 / 表示条件: `checkQuickMovementTurn180DegreesOnRun` がオンのとき |
| Quick Turn Movement Duration Sprinting | `quickTurnMovementDurationSprinting` | `float` | 2.1f | スプリント時のクイックターンの再生時間。 / 表示条件: `checkQuickMovementTurn180DegreesOnRun` がオンのとき |
| Quick Turn Movement Rotation Speed | `quickTurnMovementRotationSpeed` | `float` | 2 | クイックターン中の回転の補間速度。 / 表示条件: `checkQuickMovementTurn180DegreesOnRun` がオンのとき |

### Character Mesh Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Mesh Game Object | `characterMeshGameObject` | `GameObject` | – | 表示と非表示を切り替えるキャラのメッシュ。 |
| Head | `head` | `Transform` | – | 頭の`Transform`で、一人称時に非表示にする。 |
| Character Meshes List To Disable On Event | `characterMeshesListToDisableOnEvent` | `eventParameters.eventToCallWithBool` | – | メッシュ切替を外部へ通知するイベント。 |
| Check Character Mesh If Generated On Start | `checkCharacterMeshIfGeneratedOnStart` | `bool` | – | オンにすると開始時に子階層からメッシュを自動収集する。 |
| Object To Check Character If Generated On Start | `objectToCheckCharacterIfGeneratedOnStart` | `GameObject` | – | メッシュを探す対象のルートオブジェクト。 / 表示条件: `checkCharacterMeshIfGeneratedOnStart` がオンのとき |
| Use Events On Enable Disable Character Meshes | `useEventsOnEnableDisableCharacterMeshes` | `bool` | – | オンにするとメッシュ切替時にイベントを呼ぶ。 |
| Event On Enable Character Meshes | `eventOnEnableCharacterMeshes` | `UnityEvent` | – | メッシュ有効時に実行する処理。 / 表示条件: `useEventsOnEnableDisableCharacterMeshes` がオンのとき |
| Event On Disable Character Meshes | `eventOnDisableCharacterMeshes` | `UnityEvent` | – | メッシュ無効時に実行する処理。 / 表示条件: `useEventsOnEnableDisableCharacterMeshes` がオンのとき |
| Event On Enable Character Meshes On Editor | `eventOnEnableCharacterMeshesOnEditor` | `UnityEvent` | – | エディタ上でメッシュ有効時に実行する処理。 / 表示条件: `useEventsOnEnableDisableCharacterMeshes` がオンのとき |
| Event On Disable Character Meshes On Editor | `eventOnDisableCharacterMeshesOnEditor` | `UnityEvent` | – | エディタ上でメッシュ無効時に実行する処理。 / 表示条件: `useEventsOnEnableDisableCharacterMeshes` がオンのとき |

### Move While Aim Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Move While Aim First Person | `canMoveWhileAimFirstPerson` | `bool` | true | オンにすると一人称でエイム中も移動できる。 |
| Can Move While Aim Third Person | `canMoveWhileAimThirdPerson` | `bool` | true | オンにすると三人称でエイム中も移動できる。 |
| Can Move While Free Fire On Third Person | `canMoveWhileFreeFireOnThirdPerson` | `bool` | true | オンにすると三人称のフリーファイア中も移動できる。 |

### Locked Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Locked Player Movement | `lockedPlayerMovement` | `lockedPlayerMovementMode` | – | ロックカメラ時の移動平面を3Dか2.5Dから選ぶ。 |
| Tank Mode Rotation Speed | `tankModeRotationSpeed` | `float` | – | タンク操作時の旋回速度に掛ける0〜1の倍率。 / 表示条件: `lockedPlayerMovement.enumValueIndex == 0` / Range (0, 1) |
| Can Move While Aim Locked Camera | `canMoveWhileAimLockedCamera` | `bool` | true | ロックカメラでエイム中も移動できるようにする。 / 表示条件: `lockedPlayerMovement.enumValueIndex == 0` |
| Crouch Vertical Input2 5d Enabled | `crouchVerticalInput2_5dEnabled` | `bool` | – | 2.5Dで縦入力を下げるとしゃがみ、上げると立つ。 |
| Use Smooth Player Rotation Axis On2 5d Enabled | `useSmoothPlayerRotationAxisOn2_5dEnabled` | `bool` | true | 2.5Dの旋回を補間して滑らかにする。 |

### Gravity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Gravity Multiplier | `gravityMultiplier` | `float` | 2 | 基本重力に上乗せする追加重力の倍率。0で追加なし。 |
| Gravity Force | `gravityForce` | `float` | -9.8f | 毎フレーム加える重力加速度。負値で下方向。 |
| Use Max Fall Speed | `useMaxFallSpeed` | `bool` | – | 落下速度に上限を設けるかを切り替える。 |
| Max Fall Speed | `maxFallSpeed` | `float` | – | 落下速度の上限値。これを超えないよう制限する。 / 表示条件: `useMaxFallSpeed` がオンのとき |

### Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Zero Friction Material | `zeroFrictionMaterial` | `PhysicsMaterial` | – | 移動中にカプセルへ設定する摩擦ゼロの材質。 |
| High Friction Material | `highFrictionMaterial` | `PhysicsMaterial` | – | 停止中にカプセルへ設定する高摩擦の材質。 |

### Jump Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Jump Power | `jumpPower` | `float` | 12 | ジャンプ時に上方向へ加える初速の大きさ。 / Sets how high/far the player will jump under normal circumstances. |
| Enabled Regular Jump | `enabledRegularJump` | `bool` | – | 通常ジャンプの入力を有効にする。 |
| Hold Jump Slow Down Fall Enabled | `holdJumpSlowDownFallEnabled` | `bool` | true | 空中でジャンプボタンを押し続けると落下を遅くする。 |
| Slow Down Gravity Multiplier | `slowDownGravityMultiplier` | `float` | – | 落下を遅くしている間に使う重力倍率。 / 表示条件: `holdJumpSlowDownFallEnabled` がオンのとき |
| Jump Mass Multiplier | `jumpMassMultiplier` | `float` | 1 | ジャンプや落下の力に質量を掛ける0〜1の倍率。 / Range (0, 1) |
| Ready To Jump Time | `readyToJumpTime` | `float` | 0.25f | 着地後、次のジャンプ入力を受け付けるまでの秒数。 |
| Ignore Animator Ground State On Jump Check | `ignoreAnimatorGroundStateOnJumpCheck` | `bool` | – | ジャンプ判定でアニメーターの接地状態を無視する。 |
| Add Jump Force While Button Pressed | `addJumpForceWhileButtonPressed` | `bool` | – | ジャンプボタンを押し続けている間、追加の力を加える。 |
| Add Jump Force Duration | `addJumpForceDuration` | `float` | – | 押し続けで追加力を加える最大時間（秒）。 / 表示条件: `addJumpForceWhileButtonPressed` がオンのとき |
| Jump Force Amont While Button Pressed | `jumpForceAmontWhileButtonPressed` | `float` | – | 押し続け中に毎フレーム加える追加ジャンプ力。 / 表示条件: `addJumpForceWhileButtonPressed` がオンのとき |
| Min Wait To Add Jump Force After Button Pressed | `minWaitToAddJumpForceAfterButtonPressed` | `float` | – | 押下から追加力が発生するまでの待ち時間（秒）。 / 表示条件: `addJumpForceWhileButtonPressed` がオンのとき |
| Use Jump Force On Air Jump Enabled | `useJumpForceOnAirJumpEnabled` | `bool` | – | 空中ジャンプ時にも押し続けの追加力を有効にする。 / 表示条件: `addJumpForceWhileButtonPressed` がオンのとき |
| Keep Last Movement Input On Jump | `keepLastMovementInputOnJump` | `bool` | – | ジャンプ時の移動入力を保持し空中で慣性移動させる。 |
| Keep Last Movement Input On Jump Duration | `keepLastMovementInputOnJumpDuration` | `float` | – | ジャンプ時の移動入力を保持する秒数。 / 表示条件: `keepLastMovementInputOnJump` がオンのとき |
| Allow Regular Air Input Control On Air After Jump Duration | `allowRegularAirInputControlOnAirAfterJumpDuration` | `bool` | – | 保持時間の経過後は通常の空中入力制御を許可する。 / 表示条件: `keepLastMovementInputOnJump` がオンのとき |
| Use Delay On Ground Jump | `useDelayOnGroundJump` | `bool` | – | 地上ジャンプの発動を意図的に遅らせる。 |
| Delay On Ground Jump | `delayOnGroundJump` | `float` | – | 地上ジャンプを遅らせる秒数。0で遅延なし。 / 表示条件: `useDelayOnGroundJump` がオンのとき |
| Use Delay On Ground Jump Only If Not Moving | `useDelayOnGroundJumpOnlyIfNotMoving` | `bool` | – | 停止している時だけジャンプ遅延を適用する。 / 表示条件: `useDelayOnGroundJump` がオンのとき |
| Ignore Delay On Ground Jump On FBA | `ignoreDelayOnGroundJumpOnFBA` | `bool` | true | FBAモード中はジャンプ遅延を無視する。 / 表示条件: `useDelayOnGroundJump` がオンのとき |
| Use Event On Delay On Ground Jump | `useEventOnDelayOnGroundJump` | `bool` | – | ジャンプ遅延の開始時にイベントを呼ぶ。 / 表示条件: `useDelayOnGroundJump` がオンのとき |
| Event On Delay On Ground Jump | `eventOnDelayOnGroundJump` | `UnityEvent` | – | ジャンプ遅延の開始時に実行するイベント。 / 表示条件: `useDelayOnGroundJump.boolValue && useEventOnDelayOnGroundJump.boolValue` |
| Stop Crouch On Jump Enabled | `stopCrouchOnJumpEnabled` | `bool` | – | しゃがみ中にジャンプしたらしゃがみを解除する。 |
| Use Event On Jump | `useEventOnJump` | `bool` | – | ジャンプ時にイベントを呼ぶかを切り替える。 |
| Event On Jump | `eventOnJump` | `UnityEvent` | – | ジャンプ（二段ジャンプ含む）時に実行するイベント。 / 表示条件: `useEventOnJump` がオンのとき |
| Use Event On Ground Jump | `useEventOnGroundJump` | `bool` | – | 地上ジャンプ時に専用のイベントを呼ぶ。 |
| Event On Ground Jump | `eventOnGroundJump` | `UnityEvent` | – | 地上ジャンプ時に実行するイベント。 / 表示条件: `useEventOnGroundJump` がオンのとき |
| Use Event On Land From Jump Input | `useEventOnLandFromJumpInput` | `bool` | – | ジャンプ入力で跳んだ後の着地時にイベントを呼ぶ。 |
| Event On Land From Jump Input | `eventOnLandFromJumpInput` | `UnityEvent` | – | ジャンプ入力後の着地時に実行するイベント。 / 表示条件: `useEventOnLandFromJumpInput` がオンのとき |
| Use Event On Land | `useEventOnLand` | `bool` | – | 着地時にイベントを呼ぶかを切り替える。 |
| Event On Land | `eventOnLand` | `UnityEvent` | – | 着地した瞬間に実行するイベント。 / 表示条件: `useEventOnLand` がオンのとき |
| Check Obstacle Above Player On Jump Enabled | `checkObstacleAbovePlayerOnJumpEnabled` | `bool` | – | ジャンプ前に頭上の障害物をレイキャストで確認する。 |
| Check Obstacle Above Player On Jump Raycast Distance | `checkObstacleAbovePlayerOnJumpRaycastDistance` | `float` | – | 頭上確認レイキャストの距離（メートル）。 / 表示条件: `checkObstacleAbovePlayerOnJumpEnabled` がオンのとき |
| Check Obstacle Above Player On Jump Layermask | `checkObstacleAbovePlayerOnJumpLayermask` | `LayerMask` | – | 頭上確認レイキャストの対象レイヤー。 / 表示条件: `checkObstacleAbovePlayerOnJumpEnabled` がオンのとき |
| Use Event On Airborne | `useEventOnAirborne` | `bool` | – | 空中状態になった時にイベントを呼ぶ。 |
| Event On Airborne | `eventOnAirborne` | `UnityEvent` | – | 空中状態になった時に実行するイベント。 / 表示条件: `useEventOnAirborne` がオンのとき |

### Double Jump Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Enabled Double Jump | `enabledDoubleJump` | `bool` | – | 空中での再ジャンプ（二段ジャンプ）を許可する。 |
| Max Number Jumps In Air | `maxNumberJumpsInAir` | `int` | – | 空中で許可する追加ジャンプの回数。 / 表示条件: `enabledDoubleJump` がオンのとき |
| Use New Double Jump Power | `useNewDoubleJumpPower` | `bool` | – | 二段ジャンプに専用の跳躍力を使う。 |
| Double Jump Power | `doubleJumpPower` | `float` | 10 | 二段ジャンプ時に上方向へ加える力。 / 表示条件: `useNewDoubleJumpPower` がオンのとき |
| Remove Vertical Speed On Double Jump | `removeVerticalSpeedOnDoubleJump` | `bool` | – | 二段ジャンプの前に縦方向の速度を打ち消す。 |
| Ready To Double Jump Time | `readyToDoubleJumpTime` | `float` | 0.2f | ジャンプ後、二段ジャンプを受け付けるまでの秒数。 |
| Use Event On Double Jump | `useEventOnDoubleJump` | `bool` | – | 二段ジャンプ時にイベントを呼ぶ。 |
| Event On Double Jump | `eventOnDoubleJump` | `UnityEvent` | – | 二段ジャンプ時に実行するイベント。 / 表示条件: `useEventOnDoubleJump` がオンのとき |

### Fall Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fall Damage Enabled | `fallDamageEnabled` | `bool` | – | 落下ダメージの判定を有効にする。 |
| Max Time In Air Before Getting Damage | `maxTimeInAirBeforeGettingDamage` | `float` | 4 | ダメージ判定が始まるまでの滞空時間（秒）。 / 表示条件: `fallDamageEnabled` がオンのとき / The time a player can be in the air and falling before they may receive damage. |
| Falling Damage Multiplier | `fallingDamageMultiplier` | `float` | 0.2f | 滞空時間と速度から算出したダメージに掛ける倍率。 / 表示条件: `fallDamageEnabled` がオンのとき |
| Min Player Velocity To Apply Damage Third Person | `minPlayerVelocityToApplyDamageThirdPerson` | `float` | 15 | 三人称でダメージ判定を始める最低速度。 / 表示条件: `fallDamageEnabled` がオンのとき |
| Min Player Velocity To Apply Damage First Person | `minPlayerVelocityToApplyDamageFirstPerson` | `float` | 10 | 一人称でダメージ判定を始める最低速度。 / 表示条件: `fallDamageEnabled` がオンのとき |
| Ignore Shield On Fall Damage | `ignoreShieldOnFallDamage` | `bool` | – | シールドを無視して体力に直接ダメージを与える。 / 表示条件: `fallDamageEnabled` がオンのとき |
| Damage Type ID On Fall Damage | `damageTypeIDOnFallDamage` | `int` | -1 | 落下ダメージに使用するダメージタイプID。 / 表示条件: `fallDamageEnabled` がオンのとき |
| Apply Fall Damage Enabled | `applyFallDamageEnabled` | `bool` | true | 算出した落下ダメージを実際に体力へ適用する。 / 表示条件: `fallDamageEnabled` がオンのとき |
| Call Event On Fall Damage | `callEventOnFallDamage` | `bool` | – | 落下ダメージ時にイベントを呼ぶ。 / 表示条件: `fallDamageEnabled` がオンのとき |
| Min Time On Air To Use Event | `minTimeOnAirToUseEvent` | `float` | – | イベントを呼ぶのに必要な最低滞空時間（秒）。 / 表示条件: `fallDamageEnabled.boolValue && callEventOnFallDamage.boolValue` |
| Call Event Only If Player Alive | `callEventOnlyIfPlayerAlive` | `bool` | – | プレイヤーが生存している時だけイベントを呼ぶ。 / 表示条件: `fallDamageEnabled.boolValue && callEventOnFallDamage.boolValue` |
| Event On Fall Damage | `eventOnFallDamage` | `UnityEvent` | – | 落下ダメージ時に実行するイベント。 / 表示条件: `fallDamageEnabled.boolValue && callEventOnFallDamage.boolValue` |

### Ragdoll On Air Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Ragdoll On Fall State | `activateRagdollOnFallState` | `bool` | – | 一定条件の落下中にラグドールを起動する。 |
| Min Wait Time To Activate Ragdoll On Fall | `minWaitTimeToActivateRagdollOnFall` | `float` | – | ラグドール起動までの最低落下時間（秒）。 / 表示条件: `activateRagdollOnFallState` がオンのとき |
| Min Speed To Activate Ragdoll On Fall | `minSpeedToActivateRagdollOnFall` | `float` | – | ラグドール起動に必要な最低落下速度。 / 表示条件: `activateRagdollOnFallState` がオンのとき |
| Push Ragdoll Multiplier On Fall | `pushRagdollMultiplierOnFall` | `float` | – | 起動時にラグドールへ渡す速度に掛ける倍率。 / 表示条件: `activateRagdollOnFallState` がオンのとき |
| Event To Activate Ragdoll On Fall | `eventToActivateRagdollOnFall` | `eventParameters.eventToCallWithVector3` | – | 起動時に速度ベクトルを渡して呼ぶイベント。 / 表示条件: `activateRagdollOnFallState` がオンのとき |

### Land Mark Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Land Mark | `useLandMark` | `bool` | – | 空中で着地点マーカーを表示する。 |
| Max Land Distance | `maxLandDistance` | `float` | – | 着地点を探すレイキャストの最大距離。 / 表示条件: `useLandMark` がオンのとき |
| Min Distance Show Land Mark | `minDistanceShowLandMark` | `float` | – | マーカーを表示し始める最小距離。 / 表示条件: `useLandMark` がオンのとき |
| Land Mark | `landMark` | `GameObject` | – | 着地点に表示するマーカーのGameObject。 / 表示条件: `useLandMark` がオンのとき |
| Land Mark1 | `landMark1` | `Transform` | – | マーカーの中心で回転させるリングTransform。 / 表示条件: `useLandMark` がオンのとき |
| Land Mark2 | `landMark2` | `Transform` | – | マーカーのもう一方の回転リングTransform。 / 表示条件: `useLandMark` がオンのとき |

### Player Modes Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Use Sphere Mode | `canUseSphereMode` | `bool` | – | 球体モードへの切り替えを許可する。 |

### Vehicle Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Get On Vehicles | `canGetOnVehicles` | `bool` | – | ビークルへの搭乗を許可するかを切り替える。 |
| Can Drive | `canDrive` | `bool` | – | ビークルを運転する操作を許可する。 |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Update Headbob State | `updateHeadbobState` | `bool` | – | プレイヤー状態に応じてヘッドボブの状態を更新する。 |
| Use Extra Collider List | `useExtraColliderList` | `bool` | – | 追加コライダー一覧も衝突無視の対象にする。 |

### Crouch Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Capsule Height On Crouch | `capsuleHeightOnCrouch` | `float` | 1 | しゃがみ時のカプセルコライダーの高さ。 |
| Get Up If Jump On Crouch In Third Person | `getUpIfJumpOnCrouchInThirdPerson` | `bool` | – | 三人称でしゃがみ中にジャンプすると立ち上がる。 |
| Get Up If Jump On Crouch In First Person | `getUpIfJumpOnCrouchInFirstPerson` | `bool` | – | 一人称でしゃがみ中にジャンプすると立ち上がる。 |
| Use Auto Crouch | `useAutoCrouch` | `bool` | – | 天井が低い場所で自動的にしゃがむ。 |
| Layer To Crouch | `layerToCrouch` | `LayerMask` | – | オートしゃがみ判定レイキャストの対象レイヤー。 / 表示条件: `useAutoCrouch` がオンのとき |
| Raycast Distance To Auto Crouch | `raycastDistanceToAutoCrouch` | `float` | – | オートしゃがみ判定レイキャストの距離。 / 表示条件: `useAutoCrouch` がオンのとき |
| Auto Crouch Ray Position | `autoCrouchRayPosition` | `Transform` | – | オートしゃがみ判定レイの起点Transform。 / 表示条件: `useAutoCrouch` がオンのとき |
| Second Raycast Offset | `secondRaycastOffset` | `Vector3` | – | 2本目のオートしゃがみレイの位置オフセット。 / 表示条件: `useAutoCrouch` がオンのとき |
| Can Crouch When Using Weapons On Third Person | `canCrouchWhenUsingWeaponsOnThirdPerson` | `bool` | true | 三人称で武器使用中もしゃがみを許可する。 |
| Use Custom Layer To Check If Player Can Get Up From Crouch | `useCustomLayerToCheckIfPlayerCanGetUpFromCrouch` | `bool` | – | 立ち上がり可否の判定に専用レイヤーを使う。 |
| Custom Layer To Check If Player Can Get Up From Crouch | `customLayerToCheckIfPlayerCanGetUpFromCrouch` | `LayerMask` | – | 立ち上がり判定で使う専用レイヤー。 / 表示条件: `useCustomLayerToCheckIfPlayerCanGetUpFromCrouch` がオンのとき |

### Obstacle Detection To Avoid Movement Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Obstacle Detection To Avoid Movement | `useObstacleDetectionToAvoidMovement` | `bool` | – | 進行方向の障害物を検出して移動を止める。 |
| Obstacle Detection To Avoid Movement Raycast Distance | `obstacleDetectionToAvoidMovementRaycastDistance` | `float` | 0.5f | 前方の障害物検出レイの距離（メートル）。 / 表示条件: `useObstacleDetectionToAvoidMovement` がオンのとき |
| Obstacle Detection Raycast Distance Right And Left | `obstacleDetectionRaycastDistanceRightAndLeft` | `float` | 0.1f | 左右の検出レイの横方向オフセット。 / 表示条件: `useObstacleDetectionToAvoidMovement` がオンのとき |
| Obstacle Detection Raycast Height Offset | `obstacleDetectionRaycastHeightOffset` | `float` | – | 障害物検出レイの高さオフセット。 / 表示条件: `useObstacleDetectionToAvoidMovement` がオンのとき |
| Obstacle Detection To Avoid Movement Layermask | `obstacleDetectionToAvoidMovementLayermask` | `LayerMask` | – | 障害物検出レイキャストの対象レイヤー。 / 表示条件: `useObstacleDetectionToAvoidMovement` がオンのとき |

### Events On Walk/Run Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Walk | `useEventsOnWalk` | `bool` | – | 歩行の開始・終了時にイベントを呼ぶ。 |
| Event On Walk Start | `eventOnWalkStart` | `UnityEvent` | – | 歩行開始時に実行するイベント。 / 表示条件: `useEventsOnWalk` がオンのとき |
| Event On Walk End | `eventOnWalkEnd` | `UnityEvent` | – | 歩行終了時に実行するイベント。 / 表示条件: `useEventsOnWalk` がオンのとき |
| Use Events On Run | `useEventsOnRun` | `bool` | – | 走行の開始・終了時にイベントを呼ぶ。 |
| Event On Run Start | `eventOnRunStart` | `UnityEvent` | – | 走行開始時に実行するイベント。 / 表示条件: `useEventsOnRun` がオンのとき |
| Event On Run End | `eventOnRunEnd` | `UnityEvent` | – | 走行終了時に実行するイベント。 / 表示条件: `useEventsOnRun` がオンのとき |

### Full Body Awareness Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| FBA Walk Movement Speed | `FBAWalkMovementSpeed` | `float` | 4 | FBA時の歩き移動速度。ルートモーション無効時に使用。 |
| FBA Run Movement Speed | `FBARunMovementSpeed` | `float` | 8 | FBA時の走り移動速度。ルートモーション無効時に使用。 |
| FBA Sprint Movement Speed | `FBASprintMovementSpeed` | `float` | 12 | FBA時のスプリント速度。ルートモーション無効時に使用。 |
| FBA Crouch Movement Speed | `FBACrouchMovementSpeed` | `float` | 3 | FBA時のしゃがみ歩き速度。ルートモーション無効時用。 |
| FBA Crouch Run Movement Speed | `FBACrouchRunMovementSpeed` | `float` | 6 | FBA時のしゃがみ走り速度。ルートモーション無効時用。 |
| FBA Walk Strafe Movement Speed | `FBAWalkStrafeMovementSpeed` | `float` | 5 | FBA時のストレイフ歩き速度。ルートモーション無効時用。 |
| FBA Run Strafe Movement Speed | `FBARunStrafeMovementSpeed` | `float` | 9 | FBA時のストレイフ走り速度。ルートモーション無効時用。 |
| Use FBA Custom Move Speed Multiplier | `useFBACustomMoveSpeedMultiplier` | `bool` | – | FBA中に専用の移動速度倍率を使う。 |
| FBA Custom Move Speed Multiplier | `FBACustomMoveSpeedMultiplier` | `float` | – | FBA中に適用する移動速度倍率。 / 表示条件: `useFBACustomMoveSpeedMultiplier` がオンのとき |
| Ignore FBA Custom Move Speed Multiplier On Action Active | `ignoreFBACustomMoveSpeedMultiplierOnActionActive` | `bool` | true | アクション中もFBAの速度倍率を適用し続ける。 / 表示条件: `useFBACustomMoveSpeedMultiplier` がオンのとき |

### Animator Fields Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Forward Animator Name | `forwardAnimatorName` | `string` | "Forward" | 前方向の移動量を渡すAnimatorパラメータ名。 |
| Turn Animator Name | `turnAnimatorName` | `string` | "Turn" | 旋回量を渡すAnimatorのfloatパラメータ名。 |
| Horizontal Animator Name | `horizontalAnimatorName` | `string` | "Horizontal" | 横方向の入力値を渡すAnimatorパラメータ名。 |
| Vertical Animator Name | `verticalAnimatorName` | `string` | "Vertical" | 縦方向の入力値を渡すAnimatorパラメータ名。 |
| Horizontal Strafe Animator Name | `horizontalStrafeAnimatorName` | `string` | "Horizontal Strafe" | ストレイフ時の横入力用パラメータ名。 |
| Vertical Strafe Animator Name | `verticalStrafeAnimatorName` | `string` | "Vertical Strafe" | ストレイフ時の縦入力用パラメータ名。 |
| On Ground Animator Name | `onGroundAnimatorName` | `string` | "OnGround" | 接地状態を渡すboolパラメータ名。 |
| Crouch Animator Name | `crouchAnimatorName` | `string` | "Crouch" | しゃがみ状態を渡すboolパラメータ名。 |
| Moving Animator Name | `movingAnimatorName` | `string` | "Moving" | 移動中かどうかを渡すboolパラメータ名。 |
| Jump Animator Name | `jumpAnimatorName` | `string` | "Jump" | ジャンプ状態を渡すfloatパラメータ名。 |
| Jump Leg Animator Name | `jumpLegAnimatorName` | `string` | "JumpLeg" | ジャンプ時の脚を決めるfloatパラメータ名。 |
| Strafe Mode Active Animator Name | `strafeModeActiveAnimatorName` | `string` | "Strafe Mode Active" | ストレイフモード中かを渡すboolパラメータ名。 |
| Movement Input Active Animator Name | `movementInputActiveAnimatorName` | `string` | "Movement Input Active" | 移動入力があるかを渡すboolパラメータ名。 |
| Movement Relative To Camera Animator Name | `movementRelativeToCameraAnimatorName` | `string` | "Movement Relative To Camera" | カメラ基準の移動かを渡すboolパラメータ名。 |
| Movement ID Animator Name | `movementIDAnimatorName` | `string` | "Movement ID" | 移動IDを渡すfloatパラメータ名。 |
| Player Mode ID Animator Name | `playerModeIDAnimatorName` | `string` | "Player Mode ID" | プレイヤーモードIDを渡すパラメータ名。 |
| Movement Speed Animator Name | `movementSpeedAnimatorName` | `string` | "Movement Speed" | 現在の移動速度を渡すパラメータ名。 |
| Last Time Input Pressed Animator Name | `lastTimeInputPressedAnimatorName` | `string` | "Last Time Input Pressed" | 入力直後かを渡すboolパラメータ名。 |
| Carrying Weapon Animator Name | `carryingWeaponAnimatorName` | `string` | "Carrying Weapon" | 武器を構えているかを渡すboolパラメータ名。 |
| Aiming Mode Active Animator Name | `aimingModeActiveAnimatorName` | `string` | "Aiming Mode Active" | エイム中かを渡すboolパラメータ名。 |
| Player Status ID Animator Name | `playerStatusIDAnimatorName` | `string` | "Player Status ID" | プレイヤー状態IDを渡すfloatパラメータ名。 |
| Idle ID Animator Name | `idleIDAnimatorName` | `string` | "Idle ID" | 待機モーションIDを渡すfloatパラメータ名。 |
| Strafe ID Animator Name | `strafeIDAnimatorName` | `string` | "Strafe ID" | ストレイフIDを渡すfloatパラメータ名。 |
| Crouch ID Animator Name | `crouchIDAnimatorName` | `string` | "Crouch ID" | しゃがみIDを渡すfloatパラメータ名。 |
| Air ID Animator Name | `airIDAnimatorName` | `string` | "Air ID" | 空中状態IDを渡すfloatパラメータ名。 |
| Air Speed Animator Name | `airSpeedAnimatorName` | `string` | "Air Speed" | 空中での速度を渡すfloatパラメータ名。 |
| Quick Turn Right Direction Name | `quickTurnRightDirectionName` | `string` | "Quick Turn Right Direction" | 右クイックターンを再生するトリガー名。 |
| Quick Turn Left Direction Name | `quickTurnLeftDirectionName` | `string` | "Quick Turn Left Direction" | 左クイックターンを再生するトリガー名。 |
| Quick Turn Direction ID Speed Name | `quickTurnDirectionIDSpeedName` | `string` | "Quick Turn Direction ID" | クイックターンの方向IDを渡すintパラメータ名。 |
| Shield Active Animator Name | `shieldActiveAnimatorName` | `string` | "Shield Active" | シールド展開中かを渡すfloatパラメータ名。 |
| Input Amount Name | `inputAmountName` | `string` | "Input Amount" | 入力の有無を0/1で渡すfloatパラメータ名。 |
| Use Strafe Landing Name | `useStrafeLandingName` | `string` | "Use Strafe Landing" | ストレイフ着地を使うかを渡すパラメータ名。 |
| Weapon ID Animator Name | `weaponIDAnimatorName` | `string` | "Weapon ID" | 装備武器IDを渡すfloatパラメータ名。 |
| Right Armd ID Animator Name | `rightArmdIDAnimatorName` | `string` | "Right Arm ID" | 右腕のアニメーションIDを渡すintパラメータ名。 |
| Left Arm ID Animator Name | `leftArmIDAnimatorName` | `string` | "Left Arm ID" | 左腕のアニメーションIDを渡すintパラメータ名。 |
| Time On Air Animator Name | `timeOnAirAnimatorName` | `string` | "Time On Air" | 滞空時間を渡すfloatパラメータ名。 |
| Animator FBA Active Name | `animatorFBAActiveName` | `string` | "FBA Active" | FBAモード中かを渡すboolパラメータ名。 |

### Characters Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Camera Game Object | `playerCameraGameObject` | `GameObject` | – | プレイヤーカメラのGameObject参照。 |
| Player Camera Transform | `playerCameraTransform` | `Transform` | – | カメラ位置として使うTransform参照。 |
| Player Camera Manager | `playerCameraManager` | `cameraControllerManager` | – | カメラ制御を行う`cameraControllerManager`参照。 |
| Head Bob Manager | `headBobManager` | `headBob` | – | ヘッドボブを制御する`headBob`参照。 |
| Player Input | `playerInput` | `playerInputManager` | – | 入力を扱う`playerInputManager`参照。 |
| Player Transform | `playerTransform` | `Transform` | – | プレイヤーのTransform参照。 |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | 武器を管理する`playerWeaponsManager`参照。 |
| Health Manager | `healthManager` | `healthManagement` | – | 体力を管理する`healthManagement`参照。 |
| IK System Manager | `IKSystemManager` | `IKSystem` | – | IKを制御する`IKSystem`参照。 |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | 実際のカメラのTransform参照。 |
| Animator | `animator` | `Animator` | – | アニメーション制御に使う`Animator`参照。 |
| Step Manager | `stepManager` | `footStepManager` | – | 足音を管理する`footStepManager`参照。 |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | 移動に使う`Rigidbody`参照。 |
| Gravity Manager | `gravityManager` | `gravityObjectManager` | – | 重力方向を扱う`gravityObjectManager`参照。 |
| Character State Icon Manager | `characterStateIconManager` | `characterStateIconSystem` | – | 状態アイコンを出す`characterStateIconSystem`参照。 |
| Capsule | `capsule` | `CapsuleCollider` | – | メインの`CapsuleCollider`参照。 |
| Main Collider | `mainCollider` | `Collider` | – | 当たり判定に使うメインの`Collider`参照。 |
| AI Elements | `AIElements` | `GameObject` | – | AI制御時に有効化するAI用オブジェクト。 |
| Main Player Action System | `mainPlayerActionSystem` | `playerActionSystem` | – | カスタムアクションを実行する`playerActionSystem`参照。 |
| Main External Controller Behavior Manager | `mainExternalControllerBehaviorManager` | `externalControllerBehaviorManager` | – | 外部制御ビヘイビアの開始・終了を名前で通知する管理先。 |

### Crouch Sliding Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Crouch Sliding Enabled | `crouchSlidingEnabled` | `bool` | – | ONにすると走行中のしゃがみでスライディングが発動する。 |
| No Animator Crouch Sliding Speed | `noAnimatorCrouchSlidingSpeed` | `float` | – | アニメーター無効時のしゃがみスライディング速度。 / 表示条件: `crouchSlidingEnabled` がオンのとき |
| No Animator Crouch Sliding Duration | `noAnimatorCrouchSlidingDuration` | `float` | – | スライディングが持続する秒数。経過すると自動で終了する。 / 表示条件: `crouchSlidingEnabled` がオンのとき |
| No Animator Crouch Sliding Lerp Speed | `noAnimatorCrouchSlidingLerpSpeed` | `float` | – | スライディング速度を通常のしゃがみ走りへ戻す補間の速さ。 / 表示条件: `crouchSlidingEnabled` がオンのとき |
| No Animator Crouch Sliding Lerp Delay | `noAnimatorCrouchSlidingLerpDelay` | `float` | – | スライディング開始から減速補間が始まるまでの待ち時間。 / 表示条件: `crouchSlidingEnabled` がオンのとき |
| Get Up After Crouch Sliding End | `getUpAfterCrouchSlidingEnd` | `bool` | – | ONにするとスライディング終了時に自動で立ち上がる。 / 表示条件: `crouchSlidingEnabled` がオンのとき |
| Keep Crouch Sliding On Inclinated Surface | `keepCrouchSlidingOnInclinatedSurface` | `bool` | – | ONにすると傾斜面を滑る間はスライディング時間を延長する。 / 表示条件: `crouchSlidingEnabled` がオンのとき |
| Min Inclinitaon Surface Angle To Crouchc Sliding | `minInclinitaonSurfaceAngleToCrouchcSliding` | `float` | – | スライディングを維持する傾斜面とみなす最小角度。 / 表示条件: `crouchSlidingEnabled.boolValue && keepCrouchSlidingOnInclinatedSurface.boolValue` |
| Crouch Sliding On Air Enabled | `crouchSlidingOnAirEnabled` | `bool` | – | ONにすると空中でもしゃがみスライディングを発動できる。 / 表示条件: `crouchSlidingEnabled` がオンのとき |
| No Animator Crouch Sliding On Air Speed | `noAnimatorCrouchSlidingOnAirSpeed` | `float` | – | 空中スライディング中の移動速度。 / 表示条件: `crouchSlidingEnabled.boolValue && crouchSlidingOnAirEnabled.boolValue` |
| Use No Animator Crouch Sliding Duration On Air | `useNoAnimatorCrouchSlidingDurationOnAir` | `bool` | – | ONにすると空中スライディングにも制限時間を適用する。 / 表示条件: `crouchSlidingEnabled.boolValue && crouchSlidingOnAirEnabled.boolValue` |
| No Animator Crouch Sliding Duration On Air | `noAnimatorCrouchSlidingDurationOnAir` | `float` | – | 空中スライディングが持続する秒数。 / 表示条件: `crouchSlidingOnAirEnabled.boolValue && useNoAnimatorCrouchSlidingDurationOnAir.boolValue` |
| Event On Crouch Sliding Start | `eventOnCrouchSlidingStart` | `UnityEvent` | – | スライディング開始時に呼び出されるイベント。 / 表示条件: `crouchSlidingEnabled` がオンのとき |
| Event On Crouch Sliding End | `eventOnCrouchSlidingEnd` | `UnityEvent` | – | スライディング終了時に呼び出されるイベント。 / 表示条件: `crouchSlidingEnabled` がオンのとき |
| Use Crouch Sliding On Third Person Enabled | `useCrouchSlidingOnThirdPersonEnabled` | `bool` | – | ONにすると三人称視点でも走行中のしゃがみでスライディングする。 / 表示条件: `crouchSlidingEnabled` がオンのとき |
| Event On Crouch Sliding Third Person Start | `eventOnCrouchSlidingThirdPersonStart` | `UnityEvent` | – | 三人称スライディング開始時に呼ばれるイベント。 / 表示条件: `crouchSlidingEnabled.boolValue && useCrouchSlidingOnThirdPersonEnabled.boolValue` |
| Event On Crouch Sliding Third Person End | `eventOnCrouchSlidingThirdPersonEnd` | `UnityEvent` | – | 三人称スライディング終了時に呼ばれるイベント。 / 表示条件: `crouchSlidingEnabled.boolValue && useCrouchSlidingOnThirdPersonEnabled.boolValue` |

### Wall Running Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Wall Running Enabled | `wallRunningEnabled` | `bool` | – | ONにすると壁走り用の外部制御ビヘイビアを有効にする。 |
| Wall Running External Controller Behavior | `wallRunningExternalControllerBehavior` | `externalControllerBehavior` | – | 壁走りを制御する外部ビヘイビアの参照。 |

### Air Dash Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Air Dash Enabled | `airDashEnabled` | `bool` | – | ONにすると空中ダッシュを使えるようにする。 |
| Air Dash Force | `airDashForce` | `float` | 20 | 空中ダッシュ時に加える力の大きさ。 / 表示条件: `airDashEnabled` がオンのとき |
| Air Dash Cold Down | `airDashColdDown` | `float` | 0.5f | 連続で空中ダッシュできるまでの待ち時間（秒）。 / 表示条件: `airDashEnabled` がオンのとき |
| Pause Gravity Force | `pauseGravityForce` | `bool` | – | ONにするとダッシュ後に一定時間だけ重力を止める。 / 表示条件: `airDashEnabled` がオンのとき |
| Gravity Force Paused Time | `gravityForcePausedTime` | `float` | 1 | 重力を停止しておく時間（秒）。 / 表示条件: `airDashEnabled.boolValue && pauseGravityForce.boolValue` |
| Reset Gravity Force On Dash | `resetGravityForceOnDash` | `bool` | – | ONにするとダッシュ直前に落下速度をゼロにする。 / 表示条件: `airDashEnabled` がオンのとき |
| Use Dash Limit | `useDashLimit` | `bool` | – | ONにすると空中ダッシュの回数に上限を設ける。 / 表示条件: `airDashEnabled` がオンのとき |
| Dash Limit | `dashLimit` | `int` | – | 着地までに使える空中ダッシュの回数。 / 表示条件: `airDashEnabled.boolValue && useDashLimit.boolValue` |
| Change Camera Fov On Dash | `changeCameraFovOnDash` | `bool` | – | ONにするとダッシュ中にカメラのFOVを変更する。 / 表示条件: `airDashEnabled` がオンのとき |
| Camera Fov On Dash | `cameraFovOnDash` | `float` | – | ダッシュ中に設定するカメラのFOV値。 / 表示条件: `airDashEnabled.boolValue && changeCameraFovOnDash.boolValue` |
| Camera Fov On Dash Speed | `cameraFovOnDashSpeed` | `float` | – | FOVをダッシュ用の値へ切り替える速さ。 / 表示条件: `airDashEnabled.boolValue && changeCameraFovOnDash.boolValue` |
| Min Time On Air To Use Air Dash | `minTimeOnAirToUseAirDash` | `float` | 0.5f | 落下開始から空中ダッシュできるようになるまでの秒数。 / 表示条件: `airDashEnabled` がオンのとき |
| Use Events On Air Dash | `useEventsOnAirDash` | `bool` | – | ONにするとダッシュ成功時にイベントを呼び出す。 / 表示条件: `airDashEnabled` がオンのとき |
| Event On Air Dash Third Person | `eventOnAirDashThirdPerson` | `UnityEvent` | – | 三人称視点でダッシュした時に呼ばれるイベント。 / 表示条件: `airDashEnabled.boolValue && useEventsOnAirDash.boolValue` |
| Event On Air Dash First Person | `eventOnAirDashFirstPerson` | `UnityEvent` | – | 一人称視点でダッシュした時に呼ばれるイベント。 / 表示条件: `airDashEnabled.boolValue && useEventsOnAirDash.boolValue` |

### Zero Gravity Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Zero Gravity Movement Speed | `zeroGravityMovementSpeed` | `float` | – | 無重力モードでの移動速度の基準値。 |
| Zero Gravity Control Speed | `zeroGravityControlSpeed` | `float` | – | 無重力モードで入力速度へ近づく補間の速さ。 |
| Zero Gravity Look Camera Speed | `zeroGravityLookCameraSpeed` | `float` | – | 無重力モードで体をカメラ方向へ向ける速さ。 |
| Use Gravity Direction Land Mark | `useGravityDirectionLandMark` | `bool` | – | ONにすると無重力時に前方の面へ向けて着地マークを判定する。 |
| Forward Surface Ray Position | `forwardSurfaceRayPosition` | `Transform` | – | 無重力時のランドマーク判定に使う前方レイの起点。 / 表示条件: `useGravityDirectionLandMark` がオンのとき |
| Max Distance To Adjust | `maxDistanceToAdjust` | `float` | – | 無重力ランドマークを表示する最大距離。 / 表示条件: `useGravityDirectionLandMark` がオンのとき |
| Pause Check On Ground State ZG | `pauseCheckOnGroundStateZG` | `bool` | – | ONにすると無重力モード中は接地判定を一時停止する。 |
| Push Player When Zero Gravity Mode Is Enabled | `pushPlayerWhenZeroGravityModeIsEnabled` | `bool` | – | ONにすると無重力モード移行時に上方向へ押し出す。 |
| Push Zero Gravity Enabled Amount | `pushZeroGravityEnabledAmount` | `float` | – | 無重力モード移行時に加える上方向の力。 / 表示条件: `pushPlayerWhenZeroGravityModeIsEnabled` がオンのとき |
| Can Move Vertically On Zero Gravity | `canMoveVerticallyOnZeroGravity` | `bool` | – | ONにすると無重力時に上下方向へ移動できる。 |
| Can Move Vertically And Horizontal ZG | `canMoveVerticallyAndHorizontalZG` | `bool` | – | ONにすると上下移動を水平移動と同時に行える。 |
| Zero Gravity Speed Multiplier | `zeroGravitySpeedMultiplier` | `float` | 1.4f | 無重力時の速度に掛ける倍率。 |
| Zero Gravity Mode Vertical Speed | `zeroGravityModeVerticalSpeed` | `float` | 2 | 無重力時の上下移動の速さ。 |

### Zero Gravity And Free Floating Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Max Angle To Check On Ground State ZGFF | `useMaxAngleToCheckOnGroundStateZGFF` | `bool` | – | ONにすると無重力・浮遊時の接地判定に角度制限を設ける。 |
| Max Angle To Chek On Ground State ZGFF | `maxAngleToChekOnGroundStateZGFF` | `float` | – | 接地とみなす面の最大角度。 / 表示条件: `useMaxAngleToCheckOnGroundStateZGFF` がオンのとき |

### Free Floating Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Free Floating Movement Speed | `freeFloatingMovementSpeed` | `float` | – | フリーフロートモードでの移動速度の基準値。 |
| Free Floating Control Speed | `freeFloatingControlSpeed` | `float` | – | フリーフロートで入力速度へ近づく補間の速さ。 |
| Pause Check On Ground State FF | `pauseCheckOnGroundStateFF` | `bool` | – | ONにするとフリーフロート中は接地判定を一時停止する。 |
| Can Move Vertically On Free Floating | `canMoveVerticallyOnFreeFloating` | `bool` | – | ONにするとフリーフロート中に上下移動できる。 |
| Can Move Vertically And Horizontal FF | `canMoveVerticallyAndHorizontalFF` | `bool` | – | ONにすると上下移動を水平移動と同時に行える。 |
| Free Floating Speed Multiplier | `freeFloatingSpeedMultiplier` | `float` | 1.4f | フリーフロート時の速度に掛ける倍率。 |
| Push Free Floating Mode Enabled Amount | `pushFreeFloatingModeEnabledAmount` | `float` | – | フリーフロート開始時に上方向へ加える力。 |
| Free Floating Mode Vertical Speed | `freeFloatingModeVerticalSpeed` | `float` | 2 | フリーフロート時の上下移動の速さ。 |

### Zero Gravity And Free Floating Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Max Angle To Check On Ground State ZGFF | `useMaxAngleToCheckOnGroundStateZGFF` | `bool` | – | ONにすると無重力・浮遊時の接地判定に角度制限を設ける。 |
| Max Angle To Chek On Ground State ZGFF | `maxAngleToChekOnGroundStateZGFF` | `float` | – | 接地とみなす面の最大角度。 / 表示条件: `useMaxAngleToCheckOnGroundStateZGFF` がオンのとき |

### External Controller Behavior State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current External Controller Behavior | `currentExternalControllerBehavior` | `externalControllerBehavior` | – | 現在プレイヤーに適用中の外部制御ビヘイビア。 |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | ONにすると状態遷移のログをコンソールに出力する。 |
| Show Gizmo | `showGizmo` | `bool` | – | ONにするとシーンビューに判定用ギズモを描画する。 |
| Gizmo Color | `gizmoColor` | `Color` | – | 判定用ギズモの球やレイに使う色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | – | シーンビューのギズモラベルの文字色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Radius | `gizmoRadius` | `float` | – | ギズモで描画する球の半径サイズ。 / 表示条件: `showGizmo` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `usingAnimator` | `bool` | true | – |
| `currentAirSpeed` | `int` | 1 | – |
| `currentShieldActive` | `int` | – | – |
| `currentWeaponID` | `int` | 0 | – |
| `canRunThirdPersonActive` | `bool` | true | – |
| `characterModelID` | `int` | 0 | – |
| `extraCharacterMeshGameObject` | `List<GameObject>` | new List<GameObject> () | – |
| `allowAirControlOnKeepLastMovementInputOnJump` | `bool` | – | – |
| `ignoreSetCheckOnGrundStatePausedFFOrZGStateActive` | `bool` | – | – |
| `playerOnGround` | `bool` | – | – |
| `isMoving` | `bool` | – | – |
| `moveInput` | `Vector3` | – | – |
| `jump` | `bool` | – | – |
| `running` | `bool` | – | – |
| `crouching` | `bool` | false | – |
| `canMove` | `bool` | true | – |
| `slowingFall` | `bool` | – | – |
| `isDead` | `bool` | – | – |
| `playerSetAsChildOfParent` | `bool` | – | – |
| `useRelativeMovementToLockedCamera` | `bool` | – | – |
| `ladderFound` | `bool` | – | – |
| `ignoreCameraDirectionOnMovement` | `bool` | – | – |
| `strafeModeActive` | `bool` | – | – |
| `currentFootStepState` | `footStepState` | – | – |
| `currentHeadbobState` | `headbobState` | – | – |
| `actionActive` | `bool` | – | – |
| `rootMotionCurrentlyActive` | `bool` | – | – |
| `usingGenericModelActive` | `bool` | – | – |
| `canMoveAI` | `bool` | true | – |
| `adhereToGround` | `bool` | – | – |
| `distanceToGround` | `float` | – | – |
| `hitAngle` | `float` | – | – |
| `slopeFound` | `bool` | – | – |
| `movingOnSlopeUp` | `bool` | – | – |
| `movingOnSlopeDown` | `bool` | – | – |
| `stairsFound` | `bool` | – | – |
| `stairAdherenceSystemDetected` | `bool` | – | – |
| `wallRunningActive` | `bool` | – | – |
| `crouchSlidingActive` | `bool` | – | – |
| `terrainDetected` | `bool` | – | – |
| `isGrounded` | `bool` | – | – |
| `stickToGroundOnIdleResult` | `bool` | – | – |
| `adjustPositionResult` | `bool` | – | – |
| `groundHeightDifference` | `float` | – | – |
| `futureHasGround` | `bool` | – | – |
| `stepsDetected` | `bool` | – | – |
| `futureSurfaceAngle` | `float` | – | – |
| `movingTowardWall` | `bool` | – | – |
| `extraHeightDiffRaycastRadius` | `float` | 0 | – |
| `customMaxStepHeight` | `float` | 0 | – |
| `ignoreNewGroundAdherenceActive` | `bool` | – | – |
| `playerIsAiming` | `bool` | – | – |
| `aimingInThirdPerson` | `bool` | – | – |
| `aimingInFirstPerson` | `bool` | – | – |
| `usingFreeFireMode` | `bool` | – | – |
| `lookInCameraDirectionOnFreeFireActive` | `bool` | – | – |
| `playerUsingMeleeWeapons` | `bool` | – | – |
| `jetPackEquiped` | `bool` | – | – |
| `usingJetpack` | `bool` | – | – |
| `flyModeActive` | `bool` | – | – |
| `swimModeActive` | `bool` | – | – |
| `sphereModeActive` | `bool` | – | – |
| `freeClimbActive` | `bool` | – | – |
| `grabbingToSurfaceActive` | `bool` | – | – |
| `adjustingToSurfaceToGrabInProcess` | `bool` | – | – |
| `enableExternalForceOnSwimMode` | `bool` | – | – |
| `enableExternalForceOnFlyMode` | `bool` | – | – |
| `carryingPhysicalObject` | `bool` | – | – |
| `lockedCameraActive` | `bool` | – | – |
| `lookInCameraDirectionActive` | `bool` | – | – |
| `firstPersonActive` | `bool` | – | – |
| `update2_5dClampedPositionPaused` | `bool` | – | – |
| `usingDevice` | `bool` | – | – |
| `visibleToAI` | `bool` | true | – |
| `stealthModeActive` | `bool` | – | – |
| `playerNavMeshEnabled` | `bool` | – | – |
| `ignoreExternalActionsActiveState` | `bool` | – | – |
| `movingOnPlatformActive` | `bool` | – | – |
| `usingSubMenu` | `bool` | – | – |
| `playerMenuActive` | `bool` | – | – |
| `gamePaused` | `bool` | – | – |
| `driving` | `bool` | – | – |
| `drivingRemotely` | `bool` | – | – |
| `overridingElement` | `bool` | – | – |
| `currentVehicleName` | `string` | – | – |
| `gravityForcePaused` | `bool` | – | – |
| `zeroGravityModeOn` | `bool` | – | – |
| `freeFloatingModeOn` | `bool` | – | – |
| `currentNormal` | `Vector3` | new Vector3 (0, 1, 0) | – |
| `checkOnGroundStatePausedFFOrZG` | `bool` | – | – |
| `checkOnGroundStatePaused` | `bool` | – | – |
| `animatorDeathLayerName` | `string` | "Death" | – |
| `animatorDialogueLayerName` | `string` | "Dialogue" | – |
| `animatorArmsLayerName` | `string` | "Arms" | – |
| `animatorRightHandLayerName` | `string` | "Right Hand" | – |
| `animatorLeftHandLayerName` | `string` | "Left Hand" | – |
| `animatorRightArmLayerName` | `string` | "Right Arm" | – |
| `animatorLeftArmLayerName` | `string` | "Left Arm" | – |
| `extraColliderList` | `List<Collider>` | new List<Collider> () | – |
| `fullBodyAwarenessActive` | `bool` | – | – |
| `gravityPowerActive` | `bool` | – | – |
| `usingCloseCombatActive` | `bool` | – | – |
| `closeCombatAttackInProcess` | `bool` | – | – |
| `meleeAttackInProcess` | `bool` | – | – |
| `moveIputPaused` | `bool` | – | – |
| `currentVelocity` | `Vector3` | – | – |
| `useExternalControllerBehaviorPaused` | `bool` | – | – |
| `externalControllBehaviorActive` | `bool` | – | – |
| `externalCharacterMeshList` | `List<GameObject>` | new List<GameObject> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPauseMainRigidbodyVelocityUpdateState(bool state)` | `pauseMainRigidbodyVelocityUpdate` フラグを設定するだけ。 |
| `setUseMaxFallSpeedExternallyActiveState(bool state)` | `useMaxFallSpeedExternallyActive` フラグを設定するだけ。 |
| `setCustomMaxFallSpeedExternally(float newValue)` | `customMaxFallSpeedExternally` の値を設定するだけ。 |
| `setMainAxisValues()` | `playerInput` から取得した移動軸を `axisValues` に代入する。 |
| `setMainRawAxisValues()` | `playerInput` の生の移動軸を `rawAxisValues` に代入する。 |
| `setCustomAxisValues(Vector2 newValue)` | 本体が空の仮想メソッドで、何も処理しない。 |
| `setAIMainAxisValues()` | 入力の有効判定をせずAI用の移動軸を `axisValues` に代入する。 |
| `setMainAIRawAxisValues()` | 有効判定なしのAI用生軸を `rawAxisValues` に代入する。 |
| `updateOverrideInputValues(Vector2 inputValues, bool state)` | 入力上書きのため `playerInput.overrideInputValues` に値と状態を渡す。 |
| `setNewMainCameraTransform(Transform newTransform)` | `mainCameraTransform` を差し替えるだけ。 |
| `setNewPlayerCameraTransform(Transform newTransform)` | `playerCameraTransform` を差し替えるだけ。 |
| `setDisableStrafeModeExternallyIfIncreaseWalkSpeedActiveState(bool state)` | フラグを設定し `currentStrafeModeExternallyActive` を false にする。 |
| `checkObstacleToAvoidMovement()` | 左右2本のレイで進行方向の障害物を調べ、検出時は `currentMoveInput` をゼロにする。 |
| `isObstacleToAvoidMovementFound()` | `obstacleToAvoidMovementFound` を返すだけ。 |
| `getCurrentForwardDirection()` | `currentForwardDirection` を返すだけ。 |
| `getCurrentRightDirection()` | `currentRightDirection` を返すだけ。 |
| `isUseSmoothPlayerRotationAxisOn2_5dEnabled()` | `useSmoothPlayerRotationAxisOn2_5dEnabled` を返すだけ。 |
| `getCurrent2_5dRightDirection()` | `current2_5dRightDirection` を返すだけ。 |
| `setIgnoreLookInCameraDirectionValue(bool state)` | `ignoreLookInCameraDirection` フラグを設定するだけ。 |
| `setIgnoreStrafeModeInputCheckActiveState(bool state)` | `ignoreStrafeModeInputCheckActive` フラグを設定するだけ。 |
| `setTurnAmountClampValue(float newValue)` | `turnAmountClampValue` の値を設定するだけ。 |
| `setRotateInCameraDirectionOnAirOnExternalActionActiveState(bool state)` | 空中の外部アクション時にカメラ方向へ回るフラグを設定するだけ。 |
| `isLookCameraDirectionInFBAIsCurrentlyActive()` | FBAでカメラ方向注視が現在有効かを返すだけ。 |
| `setPausePlayerRotateToCameraDirectionOnFirstPersonActiveState(bool state)` | 一人称時のカメラ方向回転を止めるフラグを設定するだけ。 |
| `setCurrentNormalCharacter(Vector3 newNormal)` | `currentNormal` にキャラクターの法線を設定するだけ。 |
| `setApplyAnimatorVelocityWithoutMovingState(bool state)` | `applyAnimatorVelocityWithoutMoving` フラグを設定するだけ。 |
| `setIgnoreUseDelayOnGroundJumpActiveState(bool state)` | `ignoreUseDelayOnGroundJumpActive` フラグを設定するだけ。 |
| `enableOrDisableUseDelayOnGroundJumpState(bool state, float delayAmount)` | 接地ジャンプの遅延 `useDelayOnGroundJump` と `delayOnGroundJump` を設定する。 |
| `setApplyRootMotionAlwaysActiveState(bool state)` | `applyRootMotionAlwaysActive` フラグを設定するだけ。 |
| `updateAnimatorExternally()` | `animator` が有効なら `Update` と `updateAnimator` を呼び出して更新する。 |
| `setPlayerStatusIDValue(int newValue)` | `playerStatusID` を設定するだけ。 |
| `resetPlayerStatusID()` | `setPlayerStatusIDValue(0)` を呼び、状態IDを0に戻す。 |
| `getPlayerStatusID()` | `playerStatusID` を返すだけ。 |
| `setCurrentIdleIDValue(int newValue)` | `currentIdleID` を設定するだけ。 |
| `setCurrentIdleIDValueFloat(float newValue)` | `currentIdleID` にfloat値をそのまま設定するだけ。 |
| `getCurrentIdleID()` | `currentIdleID` を返すだけ。 |
| `setCurrentStrafeIDValue(int newValue)` | `currentStrafeID` を設定するだけ。 |
| `getCurrentStrafeIDValue()` | `currentStrafeID` を返すだけ。 |
| `setCurrentCrouchIDValue(int newValue)` | `currentCrouchID` を設定するだけ。 |
| `getCurrentCrouchIDValue()` | `currentCrouchID` を返すだけ。 |
| `setCurrentAirIDValue(int newValue)` | `currentAirID` を設定するだけ。 |
| `setOriginalAirIDValue()` | `currentAirID` を既定値 `regularAirboneID` に戻す。 |
| `setCurrentAirSpeedValue(int newValue)` | `currentAirSpeed` を設定するだけ。 |
| `setCurrentShieldActiveValue(int newValue)` | `currentShieldActive` を設定するだけ。 |
| `getCurrentAirID()` | `currentAirID` を返すだけ。 |
| `updatePlayerStatusIDOnAnimator()` | カスタムコントローラ未使用時のみ `playerStatusID` をAnimatorへ渡す。 |
| `updateIdleIDOnAnimator()` | カスタムコントローラ未使用時のみ `currentIdleID` をAnimatorへ渡す。 |
| `updateStrafeIDOnAnimator()` | カスタムコントローラ未使用時のみ `currentStrafeID` をAnimatorへ渡す。 |
| `updateAirIDOnAnimator()` | カスタムコントローラ未使用時のみ `currentAirID` をAnimatorへ渡す。 |
| `updateAirIDAnimatorID()` | `updateAirIDOnAnimator` と同じく `currentAirID` をAnimatorへ渡す。 |
| `setCurrentWeaponID(int newValue)` | `currentWeaponID` を設定するだけ。 |
| `updateWeaponID()` | 滑らか更新コルーチンを停止し、`currentWeaponID` をAnimatorへ即時反映する。 |
| `updateWeaponIDSmoothly()` | 既存コルーチンを止め、武器IDをAnimatorへ徐々に近づける処理を開始する。 |
| `setUsingNewWeaponID(bool state)` | `usingNewWeaponID` フラグを設定するだけ。 |
| `setAnimatorTrigger(int triggerID)` | `animator.SetTrigger(triggerID)` を呼ぶだけ。 |
| `setAnimatorTrigger(string triggerName)` | トリガー名をハッシュ化して `setAnimatorTrigger(int)` に渡す。 |
| `resetAnimatorTrigger(int triggerID)` | `animator.ResetTrigger(triggerID)` を呼ぶだけ。 |
| `resetAnimatorTrigger(string triggerName)` | トリガー名をハッシュ化して `resetAnimatorTrigger(int)` に渡す。 |
| `setPlayerOnGroundAnimatorStateOnOverrideOnGround(bool state)` | `playerOnGroundAnimatorStateOnOverrideOnGround` フラグを設定するだけ。 |
| `setPlayerOnGroundAnimatorStateOnOverrideOnGroundWithTime(bool state)` | `playerOnGroundAnimatorStateOnOverrideOnGroundWithTime` フラグを設定するだけ。 |
| `setPreviousValueOnGroundAnimatorStateValue(bool state)` | `previousValueOnGroundAnimatorState` フラグを設定するだけ。 |
| `overrideOnGroundAnimatorValue(float newOverrideOnGroundDuration)` | 上書き時間を設定して有効化し、開始時刻を `Time.time` で記録する。 |
| `disableOverrideOnGroundAnimatorValue()` | `overrideOnGroundAnimatorValueActive` を false にするだけ。 |
| `setIgnoreRootMotionDuringActionState(bool state)` | `ignoreRootMotionDuringAction` フラグを設定するだけ。 |
| `activateCustomAction(string actionName)` | アクションシステムがあれば `activateCustomAction` をそのまま呼ぶ。 |
| `stopCustomAction(string actionName)` | アクションシステムがあれば `stopCustomAction` をそのまま呼ぶ。 |
| `stopAllActionsOnActionSystem()` | アクションシステムがあれば `stopAllActions` を呼ぶ。 |
| `getCurrentActionName()` | アクションシステムの現在アクション名を返し、無ければ空文字を返す。 |
| `playCurrentAnimationOnPlayerActionSystem()` | アクションシステムの `inputPlayCurrentAnimation` を呼ぶ。 |
| `setExtraCharacterVelocity(Vector3 extraValue)` | `canRagdollMove` が false なら値をゼロにし、追加速度を設定して有効化する。 |
| `setActionCanHappenOnAirState(bool state)` | `actionCanHappenOnAir` フラグを設定するだけ。 |
| `setActionActiveState(bool state)` | `actionActive` を設定し、終了時は保留中のスクリプト状態変更を実行して時刻を記録する。 |
| `getLastTimeActionActive()` | `lastTimeActionActive` を返すだけ。 |
| `isActionActive()` | `actionActive` を返すだけ。 |
| `setNewActionIDExternally(int newID)` | アクションシステムがあれば `setNewActionIDExternally` にIDを渡す。 |
| `setActionActiveExternally(bool state)` | アクションシステムがあれば `setActionActiveExternally` に状態を渡す。 |
| `getCurrentActionCategoryActive()` | アクションシステムの現在カテゴリ名を返し、無ければ空文字を返す。 |
| `setCurrentCustomActionCategoryID(int newID)` | アクションシステムがあればカスタムアクションカテゴリIDを設定する。 |
| `setEnableChangeScriptStateAfterFinishActionState(bool state)` | `enableChangeScriptStateAfterFinishActionState` フラグを設定するだけ。 |
| `setDisableChangeScriptStateAfterFinishActionState(bool state)` | `disableChangeScriptStateAfterFinishActionState` フラグを設定するだけ。 |
| `setActionActiveWithMovementState(bool state)` | `actionActiveWithMovement` フラグを設定するだけ。 |
| `setIgnoreCameraDirectionOnMovementState(bool state)` | 有効化時はカメラの前・右方向を保存し、`ignoreCameraDirectionOnMovement` を設定する。 |
| `setIgnoreCameraDirectionOnStrafeMovementState(bool state)` | `ignoreCameraDirectionOnStrafeMovement` フラグを設定するだけ。 |
| `setUseRootMotionActiveState(bool state)` | `useRootMotionActive` フラグを設定するだけ。 |
| `setForceUseRootMotionActiveState(bool state)` | `forceUseRootMotionActive` フラグを設定するだけ。 |
| `setOriginalUseRootMotionActiveState()` | `useRootMotionActive` を初期値 `originalSetUseRootMotionActiveState` に戻す。 |
| `setNoRootMotionValues(float noRootWalkMovementSpeedValue, float noRootRunMovementSpeedValue, float noRootSprintMovementSpeedValue, float noRootCrouchMovementSpeedValue, float noRootCrouchRunMovementSpeedValue, float noRootWalkStrafeMovementSpeedValue, float noRootRunStrafeMovementSpeedValue)` | 7種類の非ルートモーション移動速度をまとめて設定する。 |
| `setOriginalNoRootMotionValues()` | 非ルートモーション移動速度を保存された初期値に戻す。 |
| `setDeactivateRootMotionOnStrafeActiveOnLockedViewState(bool state)` | フラグ設定と `previousStrafeModeActive` のリセット後、ルートモーションを切り替える。 |
| `setRotateDirectlyTowardCameraOnStrafeState(bool state)` | `rotateDirectlyTowardCameraOnStrafe` フラグを設定するだけ。 |
| `setAllowDownVelocityDuringActionState(bool state)` | `allowDownVelocityDuringAction` フラグを設定するだけ。 |
| `setPlayerControllerMovementValues(float moveSpeedMultiplierValue, float animSpeedMultiplierValue, float jumpPowerValue, float airSpeedValue, float airControlValue)` | 移動・アニメ速度、ジャンプ力、空中速度、空中制御をまとめて設定する。 |
| `resetPlayerControllerMovementValues()` | 移動系の値を保存された初期値へ戻す。 |
| `setAirSpeedValue(float newAirSpeedValue)` | `airSpeed` を設定するだけ。 |
| `setAirControlValue(float newAirControlValue)` | `airControl` を設定するだけ。 |
| `setOriginalAirSpeed()` | `airSpeed` を `originalAirSpeed` に戻す。 |
| `setOriginalAirControl()` | `airControl` を `originalAirControl` に戻す。 |
| `setIgnoreInputOnAirControlActiveState(bool state)` | `ignoreInputOnAirControlActive` フラグを設定するだけ。 |
| `setAnimatorSpeedUpdatePausedState(bool state)` | `animatorSpeedUpdatePaused` フラグを設定するだけ。 |
| `setOverrideAnimationSpeedActiveState(bool state)` | `overrideAnimationSpeedActive` フラグを設定するだけ。 |
| `updateCurrentAnimatorSpeed(float newSpeed)` | `currentAnimatorSpeed` を設定するだけ。 |
| `setNoAnimatorMovementSpeedMultiplierValue(float newValue)` | `noAnimatorMovementSpeedMultiplier` の値を設定するだけ。 |
| `setOriginalNoAnimatorMovementSpeedMultiplierValue()` | 上記の値を保存された初期値に戻す。 |
| `getCurrentSurfaceBelowPlayer()` | `currentSurfaceBelowPlayer` を返すだけ。 |
| `checkIfPlayerOnGroundWithRaycast()` | 足元上から1.3mのレイで接地を判定し、そのboolを返す。 |
| `setCheckOnGroungPausedState(bool state)` | `checkOnGroundPaused` フラグを設定するだけ。 |
| `isPlayerOnGround()` | `playerOnGround` を返すだけ。 |
| `setPlayerOnGroundState(bool state)` | `playerOnGround` を設定するだけ。 |
| `setOnGroundState(bool state)` | 接地状態を設定し、接地チェック停止中は false に上書きする。 |
| `isStrafeModeActive()` | `strafeModeActive` を返すだけ。 |
| `updateStrafeModeActiveState()` | エイム状態と接地・FBAからストレイフ状態 `strafeModeActive` を再計算する。 |
| `updateWallRunningState()` | 壁走りが有効なら外部コントローラの `updateControllerBehavior` を呼ぶ。 |
| `checkIfActivateWallRunningState()` | 壁走りが有効なら外部力の起動判定 `checkIfActivateExternalForce` を呼ぶ。 |
| `isWallRunningActive()` | `wallRunningActive` を返すだけ。 |
| `setWallRunningActiveValue(bool state)` | `wallRunningActive` を設定するだけ。 |
| `isExternalControlBehaviorForAirTypeActive()` | `externalControlBehaviorForAirTypeActive` を返すだけ。 |
| `setWallRunningActiveState(bool state)` | 壁走り有効時に外部力のアクティブ状態を設定する。 |
| `setWallRunningImpulseForce(Vector3 forceAmount, bool useCameraDirection)` | 壁走り有効時に追加インパルス力とカメラ方向使用有無を外部コントローラへ渡す。 |
| `setWallRunningEnabledState(bool state)` | 壁走り有効時に外部力の有効状態を設定する。 |
| `setPauseAllPlayerDownForces(bool state)` | `pauseAllPlayerDownForces` フラグを設定するだけ。 |
| `setLadderFoundState(bool state)` | 梯子状態を設定し、true時は壁走りを停止、false時はジャンプ入力をリセットする。 |
| `isLadderFound()` | `ladderFound` を返すだけ。 |
| `isPauseAllPlayerDownForcesActive()` | `pauseAllPlayerDownForces` を返すだけ。 |
| `setUseObstacleDetectionToAvoidMovementState(bool state)` | `useObstacleDetectionToAvoidMovement` フラグを設定するだけ。 |
| `setCheckQuickMovementTurn180DegreesOnRunState(bool state)` | `checkQuickMovementTurn180DegreesOnRun` フラグを設定するだけ。 |
| `setAirDashEnabledState(bool state)` | `airDashEnabled` フラグを設定するだけ。 |
| `doAirDash()` | 空中ダッシュを実行し、力を加えて重力停止・FOV変更・イベント発火を行う。 |
| `addExternalForce(Vector3 forceDireciton)` | 質量を掛けたインパルス力をRigidbodyに加える。 |
| `setGravityForcePuase(bool state)` | `gravityForcePaused` を設定し `unPauseGravityForceActive` を false にする。 |
| `isGravityForcePaused()` | `gravityForcePaused` を返すだけ。 |
| `setRigidbodyVelocityToZero()` | `mainRigidbody.linearVelocity` をゼロにするだけ。 |
| `getCurrentDeltaTime()` | バレットタイム補正を掛けた `Time.deltaTime` を返す。 |
| `getCurrentScaleTime()` | `GKC_Utils.getCurrentDeltaTime()` をそのまま返す。 |
| `setPlayerColliderCapsuleScale(float capsuleHeight)` | カプセルの高さと中心を設定し、`currentHeight` を更新する。 |
| `setPlayerColliderCapsuleScaleWithCenterAsRadius(float capsuleHeight)` | カプセル寸法を設定した上で、中心Yを半径未満にならないよう補正する。 |
| `setCapsuleHeightOnCrouch(float newValue)` | `capsuleHeightOnCrouch` を設定するだけ。 |
| `setPlayerColliderCapsuleCenter(Vector3 newValue)` | カプセルの中心位置を設定するだけ。 |
| `setPlayerCapsuleColliderDirection(int newDirection)` | カプセルの `direction` を設定するだけ。 |
| `setPlayerCapsuleColliderRadius(float newValue)` | カプセルの半径を設定するだけ。 |
| `setOriginalPlayerCapsuleColliderRadius()` | 半径を保存された初期値 `originalRadius` に戻す。 |
| `setOriginalPlayerColliderCapsuleScale()` | `scaleCapsule(false)` を呼び、立ち状態のカプセル寸法に戻す。 |
| `setOriginalPlayerColliderCapsuleScaleIfCrouchNotActive()` | しゃがみ中でなければ立ち寸法に戻し、しゃがみ中は `healthManager` に射撃位置の変更を依頼する。 |
| `getMainCapsuleCollider()` | `capsule` を返すだけ。 |
| `getMainCapsuleColliderBounds()` | `capsule.bounds` を返すだけ。 |
| `setCharacterRadius(float newValue)` | `characterRadius` を設定するだけ。 |
| `getCharacterRadius()` | `characterRadius` を返すだけ。 |
| `setCharacterCustomScale(float newValue)` | `characterScale` を設定し、1以外なら `customCharacterScaleActive` を有効化する。 |
| `setPlaceToShootPositionOffset(float newValue)` | 正値なら `healthManager` に射撃位置オフセットを設定し、0以下なら位置を戻す。 |
| `setPlaceToShootLocalPosition(Vector3 newValue)` | `healthManager` に射撃位置のローカル座標を設定する。 |
| `setCheckFallStatePausedState(bool state)` | `checkFallStatePaused` フラグを設定するだけ。 |
| `getMainCollider()` | `mainCollider` を返すだけ。 |
| `setMainColliderState(bool state)` | `canRagdollMove` が false で有効化要求なら無視し、それ以外は有効状態を設定する。 |
| `setMainColliderTriggerState(bool state)` | `mainCollider.isTrigger` を設定するだけ。 |
| `isMainColliderEnabled()` | `mainCollider.enabled` を返すだけ。 |
| `reactivateColliderIfPossible()` | `mainCollider` が有効なとき、一度無効化してから再度有効化し、コライダーを再アクティブ化する。 |
| `addOrRemoveExtraColliders(Collider newCollider, bool state)` | `extraColliderList` へコライダーを追加/削除し、リストが空かどうかで `useExtraColliderList` を更新する。 |
| `setIgnoreCollisionOnExternalCollider(Collider newCollider, bool state)` | 指定コライダーと `mainCollider` および追加コライダー群との衝突無視を `Physics.IgnoreCollision` で設定する。 |
| `setIgnoreCollisionOnExternalColliderOnlyWithExtraColliderList(Collider newCollider, bool state)` | `useExtraColliderList` が有効なとき、追加コライダー群との衝突無視だけを設定する。 |
| `isUseExtraColliderListActive()` | `useExtraColliderList` の値を返すだけ。 |
| `getExtraColliderList()` | `useExtraColliderList` が有効なら `extraColliderList` を、無効なら null を返す。 |
| `getCharacterLayer()` | プレイヤーの `gameObject.layer` を返すだけ。 |
| `setGravityMultiplierValue(bool setOriginal, float newValue)` | `setOriginal` なら元の重力倍率を、そうでなければ `newValue` を `gravityMultiplier` と `currentGravityMultiplier` に設定する。 |
| `setGravityMultiplierValueFromExternalFunction(float newValue)` | `gravityMultiplier` に `newValue` を設定するだけ（`currentGravityMultiplier` は変更しない）。 |
| `getGravityMultiplier()` | `gravityMultiplier` を返すだけ。 |
| `setGravityForceValue(bool setOriginal, float newValue)` | `setOriginal` なら `originalGravityForce`、そうでなければ `newValue` を `gravityForce` に設定する。 |
| `setOriginalGravityForceValue()` | `setGravityForceValue(true, 0)` を呼び、重力値を元に戻すだけ。 |
| `getGravityForce()` | `gravityForce` を返すだけ。 |
| `setSlowFallExternallyActiveState(bool state)` | `slowFallExternallyActive` フラグを設定するだけ。 |
| `isSlowFallExternallyActive()` | `slowFallExternallyActive` を返すだけ。 |
| `canUseInput()` | ジェットパック・飛行・AI操作・乗り物・水泳・近接攻撃中などでは false を返し、通常入力の可否を判定する。 |
| `inputCrouch()` | 入力停止フラグやメニュー・武器状態を確認したうえで `crouch()` を呼び、しゃがみを切り替える。 |
| `inputJump()` | 入力停止フラグと `canJumpActive`、頭上障害物のレイキャストを確認し、問題なければ `activateJump()` を呼ぶ。 |
| `isColliderPartOfCharacter(Collider newCollider)` | `mainCollider` か追加コライダーリストに含まれるコライダーなら true を返す。 |
| `inputReleaseJumpButton()` | 入力状態を確認したうえで `releaseJumpButton()` を呼び、ジャンプボタン長押しの加力を止める。 |
| `setJumpsAmountValue(int newValue)` | `jumpsAmount` に `newValue` を設定するだけ。 |
| `activateJump()` | `setJumpActive(false)` を呼ぶだけ。 |
| `setJumpActive(bool activateJumpOnAir)` | 壁走り・外部操作中はそちらへジャンプを委譲し、通常時は `jumpInput` と二段ジャンプ可否を設定して最終ジャンプ時刻を記録する。 |
| `releaseJumpButton()` | `addJumpForceWhileButtonPressed` が有効なら `jumpButtonHoldActive` を false にするだけ。 |
| `relaseJumpButtonIfAddForceWhileButtonPressedActive()` | 空中で長押し加力中なら `releaseJumpButton()` を呼んで加力を止める。 |
| `inputStartSlowDownFall()` | ボタン長押し減速が有効で待機時間を過ぎていれば `gravityMultiplier` を低下させ、`slowingFallInput` を立てる。 |
| `inputStopSlowDownFall()` | `gravityMultiplier` を `currentGravityMultiplier` に戻して減速落下を終了する。 |
| `inputAirDash()` | 各種フラグを確認し、条件を満たす空中で `doAirDash()` を実行して前方へ衝撃力を加える。 |
| `inputSetMoveVerticallyState(bool state)` | 無重力/自由浮遊モードで3D移動中のみ `movingVertically` を `state` に設定する。 |
| `inputSetChangeZeroGravityMovementSpeeState(bool state)` | 無重力モード時に `changeZeroGravityMovementVelocity(state)` を呼び、速度倍率とカメラFOVを切り替える。 |
| `inputSetChangeFreeFloatingMovementSpeeState(bool state)` | 自由浮遊モード時に `changeFreeFloatingMovementVelocity(state)` を呼び、速度倍率とカメラFOVを切り替える。 |
| `inputSetIncreaseMovementSpeedState(bool state)` | 長押し設定ならそのまま、そうでなければトグルで `increaseWalkSpeedActive` を反転し、歩行速度を変更する。 |
| `inputStartToRun()` | `runInputPaused` でなく、忙しくなく移動可能でスプリント有効なら `checkIfCanRun()` を呼ぶ。 |
| `inputStopToRun()` | 忙しくなく移動可能なときに `checkIfStopRun()` を呼ぶだけ。 |
| `inputToggleWalkAndRun()` | `toggleWalkRunState` を反転し、歩行速度とスプリント有効値をトグル状態に合わせて切り替える。 |
| `checkIfCanRun()` | 移動入力・接地・重力パワー等を条件に走行開始を判定し、可能なら `activateRun()` を呼んでタイマーを進める。 |
| `activateRun()` | `lastTimeMovingOnRun` を更新して走行状態を true にし、武器マネージャにも走行を通知する。 |
| `checkIfStopRun()` | 走行中にボタン押下タイマーが閾値を超えていれば `forceStopRun()` を呼ぶ。 |
| `forceStopRun()` | `stopRun()` を呼び、走行ボタンのタイマー類を 0 にリセットする。 |
| `stopRun()` | `setRunnningState(false)` を呼び、武器マネージャにも走行停止を通知する。 |
| `getRunButtonPressedTimer()` | `runButtonPressedTimer` を返すだけ。 |
| `playerIsBusy()` | デバイス使用中・サブメニュー・プレイヤーメニュー表示中なら true を返す（ターン制戦闘中は false）。 |
| `setSlidindOnThirdPersonActiveState(bool state)` | `slidindOnThirdPersonActive` フラグを設定するだけ。 |
| `crouch()` | スライディング状態を判定しつつ `crouching` を反転し、カプセル・IK・カメラを更新してスライディング系イベントを発火する。 |
| `checkIfActivateCrouchState()` | `playerCanGetUpFromCrouch()` が false かつ非しゃがみ状態なら `crouch()` を呼ぶ。 |
| `setCrouchState(bool state)` | 現在のしゃがみ状態と異なる場合のみ `crouch()` を呼んで切り替える。 |
| `setCrouchComponentsState(bool state)` | カメラのしゃがみ・射撃位置・カプセル高さを更新し、最終移動時刻を記録する。 |
| `stopCrouchSliding()` | スライディング中なら終了イベントを発火して各スライディングフラグを false にし、必要ならしゃがみを解除する。 |
| `setCrouchSlidingEnabledState(bool state)` | `crouchSlidingEnabled` フラグを設定するだけ。 |
| `playerCanGetUpFromCrouch()` | 頭上へ球体キャストを行い、障害物がなければ true（立ち上がり可能）を返す。 |
| `isCrouching()` | `crouching` を返すだけ。 |
| `isCanCrouchWhenUsingWeaponsOnThirdPerson()` | `canCrouchWhenUsingWeaponsOnThirdPerson` を返すだけ。 |
| `setChoosingGravityDirectionState(bool state)` | `choosingGravityDirection` フラグを設定するだけ。 |
| `setGravityPowerActiveState(bool state)` | `gravityPowerActive` フラグを設定するだけ。 |
| `isGravityPowerActive()` | `gravityPowerActive` を返すだけ。 |
| `isChoosingGravityDirection()` | `choosingGravityDirection` を返すだけ。 |
| `setUsingCloseCombatActiveState(bool state)` | `usingCloseCombatActive` フラグを設定するだけ。 |
| `isUsingCloseCombatActive()` | `usingCloseCombatActive` を返すだけ。 |
| `iscloseCombatAttackInProcess()` | `closeCombatAttackInProcess` を返すだけ。 |
| `setCloseCombatAttackInProcessState(bool state)` | `closeCombatAttackInProcess` フラグを設定するだけ。 |
| `isMeleeAttackInProcess()` | `meleeAttackInProcess` を返すだけ。 |
| `setMeleeAttackInProcessState(bool state)` | `meleeAttackInProcess` フラグを設定するだけ。 |
| `setJumpLegExternallyActiveState(bool state)` | `jumpLegExternallyActiveState` フラグを設定するだけ。 |
| `setIgnoreExternalActionsActiveState(bool state)` | `ignoreExternalActionsActiveState` フラグを設定するだけ。 |
| `isIgnoreExternalActionsActiveState()` | `ignoreExternalActionsActiveState` を返すだけ。 |
| `setRunnningState(bool state)` | `running` を設定し、スプリントイベント・移動値・FOV/ヘッドボブ・足音・スライディング停止をまとめて更新する。 |
| `isPlayerRunning()` | `running` を返すだけ。 |
| `setSprintEnabledState(bool state)` | `sprintEnabled` を設定するだけ。 |
| `setSprintCanBeUsedState(bool state)` | `sprintCanBeUsed` を設定するだけ。 |
| `stopSprint()` | `stopRun()` を呼ぶだけ。 |
| `isSprintEnabled()` | `sprintEnabled` と `sprintCanBeUsed` の論理積を返す。 |
| `setOriginalSprintEnabledValue()` | 元のスプリント設定が無効なら走行を停止し、`sprintEnabled` を元の値に戻す。 |
| `setWalkBydefaultFromEditor()` | 歩行速度を 0.5 に設定し、スプリントを無効化する。 |
| `setRunAndWalkToggleBydefaultFromEditor()` | `increaseWalkSpeedValue` を 0.5 にし、スプリントを無効化する。 |
| `enableOrDisableSphereMode(bool state)` | `canUseSphereMode` が真のときのみ `sphereModeActive` を設定する。 |
| `isSphereModeActive()` | `sphereModeActive` を返すだけ。 |
| `setLastTimeMoved()` | `lastTimeMoved` に現在時刻を記録するだけ。 |
| `setLastTimeFalling()` | `lastTimeFalling` に現在時刻を記録するだけ。 |
| `getLastTimeFalling()` | `lastTimeFalling` を返すだけ。 |
| `getLastJumpTime()` | `lastJumpTime` を返すだけ。 |
| `getLastDoubleJumpTime()` | `lastDoubleJumpTime` を返すだけ。 |
| `setLastTimeFiring()` | `lastTimeFiring` に現在時刻を記録するだけ。 |
| `getLastTimeFiring()` | `lastTimeFiring` を返すだけ。 |
| `setAimingPowersState(bool state)` | `aimingPowers` フラグを設定するだけ。 |
| `setUsingPowersState(bool state)` | `usingPowers` フラグを設定するだけ。 |
| `checkWeaponsState()` | 一人称なら true、パワー照準中や三人称で武器使用中などは false を返す武器状態の判定。 |
| `setUsingFreeFireModeState(bool state)` | `usingFreeFireMode` フラグを設定するだけ。 |
| `isUsingFreeFireMode()` | `usingFreeFireMode` を返すだけ。 |
| `checkAnimatorIsEnabled(bool state)` | 一人称なら `state`=true でアニメーターを無効化し、`usingAnimator` と足音タイプを更新する。 |
| `setUseFirstPersonPhysicsInThirdPersonActiveState(bool state)` | `useFirstPersonPhysicsInThirdPersonActive` フラグを設定するだけ。 |
| `setFootStepManagerState(bool state)` | 足音更新が有効なとき、`state` が true なら足音コンポーネントを即時無効化し、false なら遅延して有効化する。 |
| `setCurrentFootStepsState()` | 走行・しゃがみ状態から足音ステートを選び、現在値と異なる場合のみ `stepManager` に通知する。 |
| `setCurrentHeadBobState()` | 移動・走行・しゃがみからヘッドボブ状態を選び、待機時は時間条件で動的/静的アイドルを切り替える。 |
| `resetHeadBodState()` | `currentHeadbobState` を `None` に戻すだけ。 |
| `isLastJumpActivatedExternally()` | `lastJumpActivatedExternally` を返すだけ。 |
| `ejectPlayerFromVehicle(float force)` | 外部ジャンプ用の力を設定し、`jumpInput` と `lastJumpActivatedExternally` を立てて車両から射出する。 |
| `useJumpPlatform(Vector3 direction, ForceMode forceMode)` | `jumpInput` を立て、速度変更モードなら速度を 0 にしてから指定方向へ `AddForce` する。 |
| `useJumpPlatformWithKeyButton(bool state, float newJumpPower)` | `state` に応じてジャンプ力を `newJumpPower` に設定するか、元の値へ戻す。 |
| `setJumpPower(float newValue)` | `jumpPower` とその半分の `halfJumpPower` を設定する。 |
| `setOriginalJumpPower()` | `setJumpPower(originalJumpPower)` を呼ぶだけ。 |
| `getCurrentNormal()` | `gravityManager.getCurrentNormal()` を返すだけ。 |
| `externalForce(Vector3 direction)` | `externalForceActive` を立てて `externalForceValue` に方向を設定するだけ。 |
| `setExternalForceOnAir(Vector3 direction, float externalForceOnAirControl)` | 空中外力のフラグ・方向・制御値を設定するだけ。 |
| `disableExternalForceOnAirActive()` | `externalForceOnAirActive` を false にするだけ。 |
| `changeHeadScale(bool state)` | 遠隔操作中やFBA中は無視し、`state` に応じて頭のスケールを 0 か 1 にして `headScaleChanged` を設定する。 |
| `isHeadScaleChanged()` | `headScaleChanged` を返すだけ。 |
| `setDrivingState(bool state, GameObject vehicle, string vehicleName, Transform vehicleCameraControllerTransform)` | `driving` と車両情報を設定し、アニメーターの移動値を 0 にしてカメラ側へ運転状態を通知する。 |
| `getLastTimeDriving()` | `lastTimeDriving` を返すだけ。 |
| `setTemporalVehicle(GameObject newVehicle)` | `currentTemporaVehicle` を設定するだけ。 |
| `getTemporalVehicle()` | `currentTemporaVehicle` を返すだけ。 |
| `isPlayerRotatingToSurface()` | `characterRotatingToSurface` を返すだけ。 |
| `setCharacterRotatingToSurfaceState(bool state)` | `characterRotatingToSurface` を設定するだけ。 |
| `isPlayerDriving()` | `driving` を返すだけ。 |
| `isDrivingRemotely()` | `drivingRemotely` を返すだけ。 |
| `setDrivingRemotelyState(bool state)` | `drivingRemotely` を設定するだけ。 |
| `isOverridingElement()` | `overridingElement` を返すだけ。 |
| `setOverridingElementState(bool state)` | `overridingElement` を設定し、FBA時のヘッドコライダー状態を反転して反映する。 |
| `setUsingDeviceState(bool state)` | `usingDevice` を設定し、ヘッドコライダーと傾き状態を更新して最終移動時刻を記録する。 |
| `setUsingGeneralDriveRiderSystem(bool state)` | `usingGeneralDriveRiderSystem` を設定するだけ。 |
| `isUsingGeneralDriveRiderSystem()` | `usingGeneralDriveRiderSystem` を返すだけ。 |
| `isUsingDevice()` | `usingDevice` を返すだけ。 |
| `setUsingSubMenuState(bool state)` | `usingSubMenu` を設定するだけ。 |
| `isUsingSubMenu()` | `usingSubMenu` を返すだけ。 |
| `setPlayerMenuActiveState(bool state)` | `playerMenuActive` を設定し、体力マネージャにも同じ状態を通知する。 |
| `isPlayerMenuActive()` | `playerMenuActive` を返すだけ。 |
| `setGamePausedState(bool state)` | `gamePaused` を設定し、最終移動時刻を更新するだけ。 |
| `isGamePaused()` | `gamePaused` を返すだけ。 |
| `setHeadBobPausedState(bool state)` | `headBobPaused` を設定するだけ。 |
| `getCurrentVehicle()` | `currentVehicle` を返すだけ。 |
| `getCurrentVehicleCameraControllerTransform()` | `currentVehicleCameraControllerTransform` を返すだけ。 |
| `getCurrentVehicleName()` | `currentVehicleName` を返すだけ。 |
| `changeScriptState(bool state)` | アニメーターの前後・旋回値を 0 にし、`isMoving` を止めて `setCanMoveState` と入力リセットを行う。 |
| `removeJumpInputState()` | `jumpInput` と `lastJumpActivatedExternally` を false にするだけ。 |
| `resetOtherInputFields()` | ジャンプ・減速落下・重力倍率などの入力系フィールドを初期状態に戻す。 |
| `setCanMoveState(bool state)` | `canMove` を設定し、カスタムコントローラー使用時はそちらにも同じ状態を通知する。 |
| `setCanMoveAIState(bool state)` | `canMoveAI` を設定し、デバッグ表示が有効ならログを出す。 |
| `setPlayerVelocityToZero()` | `mainRigidbody.linearVelocity`・`currentVelocity`・`velocityChange` を 0 にする。 |
| `setCurrentVelocityValue(Vector3 newValue)` | `currentVelocity` を設定するだけ。 |
| `setVelocityChangeValue(Vector3 newValue)` | `velocityChange` を設定するだけ。 |
| `smoothChangeScriptState(bool state)` | `canMove` を設定し、無効化時は入力のスムーズリセット、有効化時はそのコルーチンを停止する。 |
| `canPlayerMove()` | `canMove` を返すだけ。 |
| `setMoveInputPausedState(bool state)` | `moveIputPaused` を設定するだけ。 |
| `setMoveInputPausedWithDuration(bool state, float newDuration)` | 期間付き移動入力停止のフラグ・継続時間・開始時刻を設定するだけ。 |
| `canPlayerRagdollMove()` | `canRagdollMove` を返すだけ。 |
| `setCanRagdollMoveState(bool state)` | `canRagdollMove` を設定するだけ。 |
| `setRagdollCurrentlyActiveState(bool state)` | `ragdollCurrentlyActive` を設定し、カスタムコントローラーとFBAのヘッドコライダーへ反映する。 |
| `isRagdollCurrentlyActive()` | `ragdollCurrentlyActive` を返すだけ。 |
| `setPlayerActionsInputEnabledState(bool state)` | `playerActionsInputEnabled` を設定するだけ。 |
| `enablePlayerActionsInput()` | `playerActionsInputEnabled` を true にするだけ。 |
| `disablePlayerActionsInput()` | `playerActionsInputEnabled` を false にするだけ。 |
| `smoothResetPlayerControllerInput()` | 既存コルーチンを止め、縦横入力を徐々に 0 に近づけるコルーチンを開始する。 |
| `enableOrDisablePlayerControllerScript(bool state)` | コンポーネントの `enabled` を設定し、無効化時はアニメーターパラメータを 0 にリセットする。 |
| `resetAnimatorState()` | しゃがみを解除し、ジャンプ・旋回・前後・接地のアニメーターパラメータを初期化する。 |
| `setPauseResetAnimatorStateFOrGroundAnimatorState(bool state)` | `pauseResetAnimatorStateFOrGroundAnimator` を設定するだけ。 |
| `setOnGroundAnimatorIDValue(bool state)` | カスタムコントローラー未使用時に接地アニメーターパラメータと空中時間を更新する。 |
| `setOnGroundAnimatorIDValueWithoutCheck(bool state)` | `onGroundAnimatorID` をアニメータへ直接設定し、空中時間の値も更新する。 |
| `setJumpAnimatorIDValue(float newValue)` | 前回値と異なる場合のみ、ジャンプ用のアニメータfloat値を更新する。 |
| `setRightArmdIDAnimatorIDValue(int newValue)` | `rightArmdIDAnimatorID` のint値をアニメータへ設定するだけ。 |
| `setLeftArmIDAnimatorIDValue(int newValue)` | `leftArmIDAnimatorID` のint値をアニメータへ設定するだけ。 |
| `setTimeOnAirAnimatorIDValue()` | `lastTimeOnAirAnimator` からの経過秒を空中時間としてアニメータへ設定する。 |
| `equipJetpack(bool state)` | `jetPackEquiped` フラグを設定するだけ。 |
| `setUsingJetpackState(bool state)` | `usingJetpack` フラグを設定するだけ。 |
| `isJetpackEquiped()` | `jetPackEquiped` の値を返すだけ。 |
| `isUsingJetpack()` | `usingJetpack` の値を返すだけ。 |
| `enableOrDisableFlyingMode(bool state)` | `flyModeActive` を切り替え、非水泳時は飛行中の外力を無効化する。 |
| `isFlyingActive()` | `flyModeActive` の値を返すだけ。 |
| `enableOrDisableFlyModeTurbo(bool state)` | 本体が空のため何も処理しない。 |
| `setFreeClimbActiveState(bool state)` | `freeClimbActive` を設定し、FBAの頭コライダーを反転して切り替える。 |
| `isFreeClimbActive()` | `freeClimbActive` の値を返すだけ。 |
| `setGrabbingToSurfaceActiveState(bool state)` | `grabbingToSurfaceActive` フラグを設定するだけ。 |
| `isGrabbingToSurfaceActive()` | `grabbingToSurfaceActive` の値を返すだけ。 |
| `setAdjustingToSurfaceToGrabInProcessState(bool state)` | `adjustingToSurfaceToGrabInProcess` フラグを設定するだけ。 |
| `isAjustingToSurfaceToGrabInProcess()` | `adjustingToSurfaceToGrabInProcess` の値を返すだけ。 |
| `setCarryingPhysicalObjectState(bool state)` | `carryingPhysicalObject` フラグを設定するだけ。 |
| `isCarryingPhysicalObject()` | `carryingPhysicalObject` の値を返すだけ。 |
| `enableOrDisableSwimMode(bool state)` | `swimModeActive` を切り替え、終了時は水泳中の外力を無効化する。 |
| `isSwimModeActive()` | `swimModeActive` の値を返すだけ。 |
| `setEnableExternalForceOnSwimModeState(bool state)` | `enableExternalForceOnSwimMode` フラグを設定するだけ。 |
| `setEnableExternalForceOnFlyModeState(bool state)` | `enableExternalForceOnFlyMode` フラグを設定するだけ。 |
| `setTurnAndForwardAnimatorValuesPausedState(bool state)` | `turnAndForwardAnimatorValuesPaused` フラグを設定するだけ。 |
| `setPauseCameraShakeFromGravityActiveState(bool state)` | `pauseCameraShakeFromGravityActive` フラグを設定するだけ。 |
| `isPauseCameraShakeFromGravityActive()` | `pauseCameraShakeFromGravityActive` の値を返すだけ。 |
| `setExternalControllerBehavior(externalControllerBehavior newExternalControllerBehavior)` | 外部制御behaviorを設定し、名前と有効状態を更新して管理側へ通知、ジャンプ入力を解放する。 |
| `getCurrentExternalControllerBehavior()` | 現在の外部制御behaviorを返すだけ。 |
| `isExternalControllBehaviorActive()` | `externalControllBehaviorActive` の値を返すだけ。 |
| `getCurrentExternalControllerBehaviorName()` | 現在の外部制御behavior名を返すだけ。 |
| `setUseExternalControllerBehaviorPausedState(bool state)` | `useExternalControllerBehaviorPaused` フラグを設定するだけ。 |
| `isUseExternalControllerBehaviorPaused()` | `useExternalControllerBehaviorPaused` の値を返すだけ。 |
| `getExternalControllerBehaviorWallRunning()` | `wallRunningExternalControllerBehavior` を返すだけ。 |
| `checkChangeCameraViewStateOnExternalControllerBehavior()` | 外部制御が有効な時のみ、そのbehaviorのカメラ視点チェックを呼び出す。 |
| `setAvoidListOfExternalControllerStatesActiveState(bool state, List<string> newList)` | 回避リストの有効フラグと文字列リストをまとめて差し替える。 |
| `isAvoidListOfExternalControllerStatesActive()` | `avoidListOfExternalControllerStatesActive` の値を返すだけ。 |
| `getExternalControllerToAvoidList()` | `externalControllerToAvoidList` を返すだけ。 |
| `checkIfInsideExternalControllerToAvoidList(string nameToCheck)` | 回避リストに指定名が含まれるかを判定して返す。 |
| `setCustomCharacterControllerActiveState(bool state, customCharacterControllerBase customCharacterControllerBaseInfo)` | カスタム制御の有効状態と参照を設定し、移動可否とラグドール状態を同期する。 |
| `isCustomCharacterControllerActive()` | `customCharacterControllerActive` の値を返すだけ。 |
| `setExternalControlBehaviorForAirTypeActiveState(bool state)` | `externalControlBehaviorForAirTypeActive` フラグを設定するだけ。 |
| `enableOrDisableAiminig(bool state)` | 一人称か三人称かに応じて照準を切り替え、解除時は最終入力時刻をリセットする。 |
| `enableOrDisableAimingInFirstPerson(bool state)` | `aimingInFirstPerson` を設定し、`playerIsAiming` を再計算する。 |
| `enableOrDisableAimingInThirdPerson(bool state)` | `aimingInThirdPerson` を設定し、`playerIsAiming` の再計算と空中ID調整を行う。 |
| `isPlayerAiming()` | 一人称・三人称いずれかの照準が有効かを返す。 |
| `isPlayerAimingInThirdPerson()` | `aimingInThirdPerson` の値を返すだけ。 |
| `isPlayerAimingInFirstPerson()` | `aimingInFirstPerson` の値を返すだけ。 |
| `checkOtherStatesOnAirID(bool state)` | 照準状態に応じて通常の空中IDへ切り替え、以前の状態を記録する。 |
| `isLookingInCameraDirection()` | 照準・一人称・注視フラグからカメラ方向を向く状態かを判定して返す。 |
| `getPlayerCameraManager()` | `playerCameraManager` を `playerCamera` として返すだけ。 |
| `getPlayerCameraGameObject()` | `playerCameraGameObject` を返すだけ。 |
| `isPlayerOnFirstPerson()` | `firstPersonActive` の値を返すだけ。 |
| `setFirstPersonViewActiveState(bool state)` | `firstPersonActive` を設定し、頭部状態をリセットしてIKを一人称/三人称へ切り替える。 |
| `setFullBodyAwarenessActiveStateAtStart(bool state)` | 開始時用の `fullBodyAwarenessActiveAtStart` を設定するだけ。 |
| `setFullBodyAwarenessActiveStateExternally(bool state)` | `fullBodyAwarenessActive` を設定するだけ。 |
| `setFullBodyAwarenessActiveState(bool state)` | FBAを切り替え、ストレイフ・ルートモーション・速度・カメラ・IK・アニメータを連動更新する。 |
| `isFullBodyAwarenessActive()` | `fullBodyAwarenessActive` の値を返すだけ。 |
| `setPivotCameraTransformParentCurrentTransformToFollow()` | ピボットカメラの親を追従対象へ切り替えるようカメラ側へ委譲する。 |
| `setPivotCameraTransformOriginalParent()` | ピボットカメラの親を元の親へ戻すようカメラ側へ委譲する。 |
| `resetPivotCameraTransformLocalRotation()` | ピボットカメラのローカル回転をリセットするようカメラ側へ委譲する。 |
| `setNewPlayerCharacterPositionAndRotation(Vector3 targetPosition, Vector3 targetRotation)` | プレイヤーとカメラの位置・回転を指定値へ直接設定する。 |
| `stopShakeCamera()` | カメラの揺れを停止するようカメラ管理側へ委譲する。 |
| `getForwardAmount()` | `forwardAmount` の値を返すだけ。 |
| `setForwardAmountExternally(float newValue)` | 前進量をアニメータのfloat値へ直接設定する。 |
| `isPlayerMoving(float movingTolerance)` | 水平・垂直入力の絶対値が許容値を超えるかで移動中を判定する。 |
| `isPlayerMovingHorizontal(float movingTolerance)` | 水平入力の絶対値が許容値を超えるかだけを判定する。 |
| `isPlayerMovingVertical(float movingTolerance)` | 垂直入力の絶対値が許容値を超えるかだけを判定する。 |
| `isPlayerUsingInput()` | 生の入力軸がX・Yとも0以外かどうかを返す。 |
| `isPlayerUsingVerticalInput()` | 生の垂直入力が0以外かどうかを返す。 |
| `isPlayerUsingHorizontalInput()` | 生の水平入力が0以外かどうかを返す。 |
| `getAxisValues()` | `axisValues` を返すだけ。 |
| `getRawAxisValues()` | `rawAxisValues` を返すだけ。 |
| `resetPlayerControllerInput()` | `horizontalInput` と `verticalInput` を0にリセットする。 |
| `resetLastMoveInputOnJumpValue()` | ジャンプ時の最後の移動入力ベクトルと無視フラグを初期化する。 |
| `overrideMainCameraTransformDirection(Transform newCameraDirection, bool overrideState)` | カメラ方向の上書き対象Transformと有効フラグを設定する。 |
| `setUseForwardDirectionForCameraDirectionState(bool state)` | `useForwardDirectionForCameraDirection` フラグを設定するだけ。 |
| `setUseRightDirectionForCameraDirectionState(bool state)` | `useRightDirectionForCameraDirection` フラグを設定するだけ。 |
| `setOverrideTurnAmount(float newTurnAmount, bool newOverrideTurnAmountActiveState)` | 旋回量の上書き値と有効フラグを設定する。 |
| `setLockedCameraState(bool state, bool useTankControlsValue, bool useRelativeMovementToLockedCameraValue, bool playerCanMoveOnAimInTankModeValue, bool keepCameraRelativeMovementWhenNotAimingValue)` | ロックカメラ関連の各フラグとタンク操作状態を一括設定し、解除時は切替フラグを立てる。 |
| `isLockedCameraStateActive()` | `lockedCameraActive` の値を返すだけ。 |
| `setUpdate2_5dClampedPositionPausedState(bool state)` | `update2_5dClampedPositionPaused` フラグを設定するだけ。 |
| `isTankModeActive()` | `useTankControls` とロックカメラの両方が有効かを返す。 |
| `canCharacterGetOnVehicles()` | `canGetOnVehicles` の値を返すだけ。 |
| `setCanCharacterGetOnVehiclesState(bool state)` | `canGetOnVehicles` フラグを設定するだけ。 |
| `setOriginalCanCharacterGetOnVehiclesState()` | `originalCanCharacterGetOnVehiclesState` の値へ戻す。 |
| `isActionToGetOnVehicleActive()` | `actionToGetOnVehicleActive` の値を返すだけ。 |
| `setActionToGetOnVehicleActiveState(bool state)` | `actionToGetOnVehicleActive` フラグを設定するだけ。 |
| `isActionToGetOffFromVehicleActive()` | `actionToGetOffFromVehicleActive` の値を返すだけ。 |
| `setActionToGetOffFromVehicleActiveState(bool state)` | `actionToGetOffFromVehicleActive` フラグを設定するだけ。 |
| `canCharacterDrive()` | `canDrive` の値を返すだけ。 |
| `setCanDriveState(bool state)` | `canDrive` フラグを設定するだけ。 |
| `setOriginalCanDriveState()` | `originalCanDrive` の値へ戻す。 |
| `setCanMoveWhileAimLockedCameraValue(bool state)` | `canMoveWhileAimLockedCamera` フラグを設定するだけ。 |
| `setOriginalCanMoveWhileAimLockedCameraValue()` | `originalCanMoveWhileAimLockedCamera` の値へ戻す。 |
| `getPlayerManagersParentGameObject()` | 管理用親GameObjectを返し、未設定ならプレイヤーの親を返す。 |
| `setPlayerAndCameraParent(Transform newParent)` | プレイヤーとカメラの親を変更し、子状態フラグと現在の親を更新する。 |
| `setPlayerAndCameraAndFBAPivotTransformParent(Transform newParent)` | プレイヤーとカメラに加え、FBAピボットの親も同じ親へ設定する。 |
| `getCurrentTemporalPlayerParent()` | `currentTemporalPlayerParent` を返すだけ。 |
| `setMovingOnPlatformActiveState(bool state)` | `movingOnPlatformActive` フラグを設定するだけ。 |
| `setUpdatePlayerCameraPositionOnLateUpdateActiveState(bool state)` | LateUpdateでのカメラ位置更新の有効状態をカメラ側へ設定する。 |
| `setUpdatePlayerCameraPositionOnFixedUpdateActiveState(bool state)` | FixedUpdateでのカメラ位置更新の有効状態をカメラ側へ設定する。 |
| `setMovingInsideVehicleState(bool state)` | `movingInsideVehicle` フラグを設定するだけ。 |
| `isMovingInsideVehicle()` | `movingInsideVehicle` の値を返すだけ。 |
| `setMovingInsideVehicleState(Vector3 externalForceInsideVehicleValue)` | 車内で受ける外力ベクトル `externalForceInsideVehicle` を設定する。 |
| `isMovingOnPlatformActive()` | `movingOnPlatformActive` の値を返すだけ。 |
| `setReducedVelocity(float newValue)` | `setAnimSpeedMultiplierValue` 経由でアニメ速度倍率を変更する。 |
| `setNormalVelocity()` | アニメ速度倍率を元の `originalAnimationSpeed` に戻す。 |
| `getAnimSpeedMultiplier()` | `animSpeedMultiplier` の値を返すだけ。 |
| `setMoveSpeedMultiplierValue(float newValue)` | `moveSpeedMultiplier` の値を設定するだけ。 |
| `setOriginalMoveSpeedMultiplierValue()` | `originalMoveSpeedMultiplier` の値へ戻す。 |
| `setNewAnimSpeedMultiplierDuringXTime(float newValue)` | 既存コルーチンを停止し、指定時間だけ倍率を変えるコルーチンを開始する。 |
| `setRegularAnimSpeedMultiplier()` | 上書き中ならコルーチンを止め、速度とAI移動可否を通常状態へ戻す。 |
| `isAnimSpeedMultiplierChangedDuringXTimeActive()` | `animSpeedMultiplierChangedDuringXTimeActive` の値を返すだけ。 |
| `setPauseCharacterPriorityValue(int newValue)` | `pauseCharacterPriority` の値を設定するだけ。 |
| `getPauseCharacterPriorityValue()` | `pauseCharacterPriority` の値を返すだけ。 |
| `changeControlInputType(bool value)` | `usedByAI` を切り替え、AI時は入力リセット、非AI時は入力上書きを解除する。 |
| `setAIElementsEnabledState(bool state)` | `AIElements` のアクティブ状態を、変化がある時のみ切り替える。 |
| `setUsedByAIState(bool state)` | `usedByAI` を設定し、AIでなくなったら入力上書きを解除する。 |
| `startOverride()` | `overrideCharacterControlState(true)` を呼ぶだけ。 |
| `stopOverride()` | `overrideCharacterControlState(false)` を呼ぶだけ。 |
| `overrideCharacterControlState(bool state)` | `usedByAI` と上書きフラグを設定し、非AI時は入力上書きを解除する。 |
| `isCharacterUsedByAI()` | `usedByAI` の値を返すだけ。 |
| `isCharacterControlOverrideActive()` | `characterControlOverrideActive` の値を返すだけ。 |
| `getHorizontalInput()` | `horizontalInput` の値を返すだけ。 |
| `getVerticalInput()` | `verticalInput` の値を返すだけ。 |
| `getMoveInputDirection()` | `currentMoveInput` を返すだけ。 |
| `setLookInCameraDirectionState(bool state)` | `lookInCameraDirection` フラグを設定するだけ。 |
| `Move(AINavMeshMoveInfo inputInfo)` | AI入力の移動ベクトルを正規化して設定し、ジャンプ・注視・ストレイフ状態を反映する。 |
| `setVisibleToAIState(bool state)` | `visibleToAI` フラグを設定するだけ。 |
| `isCharacterInVisibleState()` | `visibleToAI` の値を返すだけ。 |
| `isCharacterVisibleToAI()` | 可視状態かつ非ステルス状態かどうかを返す。 |
| `setStealthModeActiveState(bool state)` | `stealthModeActive` フラグを設定するだけ。 |
| `isCharacterInStealthMode()` | `stealthModeActive` の値を返すだけ。 |
| `setCharacterStateIcon(string stateName)` | アイコン管理が存在すれば、指定名の状態アイコンを表示させる。 |
| `disableCharacterStateIcon()` | アイコン管理が存在すれば、状態アイコンの表示を止める。 |
| `getPlayerID()` | `playerID` の値を返すだけ。 |
| `setPlayerID(int newID)` | `playerID` を設定するだけ。 |
| `setCharacterModelID(int newID)` | `characterModelID` を設定するだけ。 |
| `getCharacterModelID()` | `characterModelID` の値を返すだけ。 |
| `isPlayerNonLocalAvatar()` | `playerIsNonLocalAvatar` の値を返すだけ。 |
| `setPlayerIsNonLocalAvatarState(bool state)` | `playerIsNonLocalAvatar` フラグを設定するだけ。 |
| `getPlayerNonLocalAvatarID()` | `playerNonLocalAvatarID` の値を返すだけ。 |
| `setPlayerNonLocalAvatarID(int newID)` | `playerNonLocalAvatarID` を設定するだけ。 |
| `setPlayerDeadState(bool state)` | 死亡状態を設定し、死亡時は走り・しゃがみを解除、復帰時は蘇生時刻を記録する。 |
| `isPlayerDead()` | `isDead` の値を返すだけ。 |
| `getLastTimeResurrect()` | `lastTimeResurrect` の値を返すだけ。 |
| `setFallDamageCheckPausedState(bool state)` | `fallDamageCheckPaused` フラグを設定するだけ。 |
| `setFallDamageCheckOnHealthPausedState(bool state)` | `fallDamageCheckOnHealthPaused` フラグを設定するだけ。 |
| `checkIfPlayerDeadFromHealthComponent()` | 体力管理コンポーネントの死亡判定をそのまま返す。 |
| `setDamageReactionPausedState(bool state)` | `healthManager` のダメージリアクション停止状態を設定するだけ。 |
| `setPlayerUsingWeaponsState(bool state)` | `playerUsingWeapons` フラグを設定するだけ。 |
| `isPlayerUsingWeapons()` | 武器マネージャー検出済みなら `playerUsingWeapons` を返し、未検出なら false を返す。 |
| `isPlayerUsingPowers()` | `usingPowers` フラグをそのまま返すだけ。 |
| `isPlayerUsingMeleeWeapons()` | `playerUsingMeleeWeapons` フラグをそのまま返すだけ。 |
| `isPlayerMeleeWeaponThrown()` | `playerMeleeWeaponThrown` フラグをそのまま返すだけ。 |
| `setPlayerMeleeWeaponThrownState(bool state)` | `playerMeleeWeaponThrown` フラグを設定するだけ。 |
| `setPlayerUsingMeleeWeaponsState(bool state)` | `playerUsingMeleeWeapons` フラグを設定するだけ。 |
| `setPlayerNavMeshEnabledState(bool state)` | `playerNavMeshEnabled` を設定し、入力リセット後、無効時は入力値をゼロで上書きする。 |
| `isPlayerNavMeshEnabled()` | `playerNavMeshEnabled` を返すだけ。 |
| `enableOrDisableDoubleJump(bool state)` | `enabledDoubleJump`（二段ジャンプの可否）を設定するだけ。 |
| `setMaxNumberJumpsInAir(float amount)` | 空中ジャンプ回数 `maxNumberJumpsInAir` を `amount` の整数値で設定するだけ。 |
| `enableOrDisableJump(bool state)` | `enabledRegularJump`（通常ジャンプの可否）を設定するだけ。 |
| `setcanJumpActiveState(bool state)` | `canJumpActive` を設定するだけ。 |
| `setJumpInputPausedState(bool state)` | `jumpInputPaused` を設定し、ジャンプ入力の停止を切り替えるだけ。 |
| `setHoldJumpSlowDownFallEnabledState(bool state)` | `holdJumpSlowDownFallEnabled`（長押しで落下を緩める設定）を設定するだけ。 |
| `setRunInputPausedState(bool state)` | `runInputPaused` を設定し、走行入力の停止を切り替えるだけ。 |
| `setPhysicMaterialAssigmentPausedState(bool state)` | `physicMaterialAssigmentPaused` を設定し、物理マテリアル割当の一時停止を切り替える。 |
| `setUsingAbilityActiveState(bool state)` | `usingAbilityActive` を設定するだけ。 |
| `isUsingAbilityActive()` | `usingAbilityActive` を返すだけ。 |
| `setCrouchInputPausedState(bool state)` | `crouchInputPaused` を設定し、しゃがみ入力の停止を切り替えるだけ。 |
| `setHighFrictionMaterial()` | 未適用ならカプセルの物理マテリアルを `highFrictionMaterial` に差し替え、フラグを立てる。 |
| `setZeroFrictionMaterial()` | 高摩擦適用中ならカプセルの物理マテリアルを `zeroFrictionMaterial` に戻す。 |
| `playerCanRunNow()` | 三人称は `canRunThirdPersonActive`、一人称は前入力か後退許可で走行可否を返す。 |
| `setNoAnimatorWalkMovementSpeed(float newValue, bool setOriginalValue)` | `setOriginalValue` なら元の歩き速度、そうでなければ元値×`newValue` を設定するだけ。 |
| `setNoAnimatorRunMovementSpeed(float newValue, bool setOriginalValue)` | `setOriginalValue` なら元の走り速度、そうでなければ元値×`newValue` を設定するだけ。 |
| `setNoAnimatorCrouchMovementSpeed(float newValue, bool setOriginalValue)` | `setOriginalValue` なら元のしゃがみ速度、そうでなければ元値×`newValue` を設定するだけ。 |
| `setNoAnimatorStrafeMovementSpeed(float newValue, bool setOriginalValue)` | `setOriginalValue` なら元のストレイフ速度、そうでなければ元値×`newValue` を設定する。 |
| `setNoAnimatorWalkBackwardMovementSpeed(float newValue, bool setOriginalValue)` | `setOriginalValue` なら元の後退歩き速度、そうでなければ元値×`newValue` を設定する。 |
| `setNoAnimatorRunBackwardMovementSpeed(float newValue, bool setOriginalValue)` | `setOriginalValue` なら元の後退走り速度、そうでなければ元値×`newValue` を設定する。 |
| `setNoAnimatorCrouchBackwardMovementSpeed(float newValue, bool setOriginalValue)` | `setOriginalValue` なら元の後退しゃがみ速度、そうでなければ元値×`newValue` を設定する。 |
| `setNoAnimatorStrafeBackwardMovementSpeed(float newValue, bool setOriginalValue)` | `setOriginalValue` なら元の後退ストレイフ速度、そうでなければ元値×`newValue` を設定する。 |
| `setNoAnimatorCanRunState(bool newState, bool setOriginalValue)` | `setOriginalValue` 時は元の許可値、他は `newState` を `noAnimatorCanRun` に設定。 |
| `setNoAnimatorGeneralMovementSpeed(float newValue, bool setOriginalValue)` | アニメーター無しの移動速度8種のセッターを同じ引数でまとめて呼び出す。 |
| `setNoAnimatorSpeedValue(float newValue)` | `noAnimatorSpeed` を設定するだけ。 |
| `setAnimatorCanRunState(bool newState, bool setOriginalValue)` | `setOriginalValue` 時は true、他は `newState` を `canRunThirdPersonActive` に設定。 |
| `setAnimatorGeneralMovementSpeed(float newValue, bool setOriginalValue)` | `setOriginalValue` なら元の歩行速度、そうでなければ `newValue` を歩行速度に設定する。 |
| `hasToLookInCameraDirection()` | カメラ方向注視の各フラグと接地・フルボディ状態を組み合わせて注視要否を返す。 |
| `setIgnoreLookInCameraDirectionOnFreeFireActiveState(bool state)` | `ignoreLookInCameraDirectionOnFreeFireActive` を設定するだけ。 |
| `hasToLookInCameraDirectionOnFreeFire()` | 無視フラグが立っていれば false、そうでなければフリーファイア状態から注視要否を返す。 |
| `isPlayerLookingAtTarget()` | `playerCameraManager` の注視対象判定をそのまま返すだけ。 |
| `istargetToLookLocated()` | `playerCameraManager` の注視対象存在判定をそのまま返すだけ。 |
| `getCurrentTargetToLook()` | `playerCameraManager` が保持する現在の注視対象トランスフォームを返すだけ。 |
| `getOriginalLockedCameraPivotPosition()` | `playerCameraManager` のロックカメラピボット元位置をそのまま返すだけ。 |
| `setCheckToKeepWeaponAfterAimingWeaponFromShootingState(bool state)` | フラグを設定し、false にした時は `lastTimeCheckToKeepWeapon` を現在時刻に更新する。 |
| `isCheckToKeepWeaponAfterAimingWeaponFromShooting()` | `checkToKeepWeaponAfterAimingWeaponFromShooting` を返すだけ。 |
| `setLookAlwaysInCameraDirectionState(bool state)` | `lookAlwaysInCameraDirection` を設定するだけ。 |
| `isLookAlwaysInCameraDirectionActive()` | `lookAlwaysInCameraDirection` を返すだけ。 |
| `setOriginalLookAlwaysInCameraDirectionState()` | フルボディアウェアネス中は true、そうでなければ保存された元の値に戻す。 |
| `setLookInCameraDirectionIfLookingAtTargetState(bool state)` | `lookInCameraDirectionIfLookingAtTarget` を設定するだけ。 |
| `setLookOnlyIfMovingState(bool state)` | `lookOnlyIfMoving` を設定するだけ。 |
| `setOriginalLookOnlyIfMovingState()` | フルボディアウェアネス中は false、そうでなければ保存された元の値に戻す。 |
| `activateOrDeactivateStrafeModeDuringActionSystem(bool state)` | `state` に応じて `activateStrafeMode` か `deactivateStrafeMode` を呼び分けるだけ。 |
| `activateOrDeactivateStrafeMode(bool state)` | フルボディ中は解除を無視し、それ以外は切替えて `strafeModeActivatedExternally` を更新する。 |
| `activateStrafeMode()` | カメラ方向注視を有効にし、移動時のみ注視を無効化してストレイフを有効にする。 |
| `deactivateStrafeMode()` | 保存された元の注視設定へ戻してストレイフを解除する。 |
| `setZeroGravityModeOnState(bool state)` | `zeroGravityModeOn` を設定し、押し出し・接地判定停止・IK・足音・空中状態を連動更新する。 |
| `setPushPlayerWhenZeroGravityModeIsEnabledState(bool state)` | `pushPlayerWhenZeroGravityModeIsEnabled` を設定するだけ。 |
| `isPlayerOnZeroGravityMode()` | `zeroGravityModeOn` を返すだけ。 |
| `changeZeroGravityMovementVelocity(bool value)` | `value` に応じて零重力速度倍率を切替え、カメラFOVと `movementSpeedIncreased` を更新する。 |
| `setCheckOnGrundStatePausedFFOrZGState(bool state)` | 零重力/浮遊中で該当フラグ有効時のみ true にし、false は常に接地判定停止へ反映する。 |
| `setIgnoreSetCheckOnGrundStatePausedFFOrZGStateActive(bool state)` | `ignoreSetCheckOnGrundStatePausedFFOrZGStateActive` を設定するだけ。 |
| `setcheckOnGroundStatePausedState(bool state)` | `checkOnGroundStatePaused` を設定するだけ。 |
| `isPauseCheckOnGroundStateZGActive()` | `pauseCheckOnGroundStateZG` を返すだけ。 |
| `setfreeFloatingModeOnState(bool state)` | `freeFloatingModeOn` を設定し、押し出し・接地判定・IK・足音・FOVを連動更新する。 |
| `enableOrDisableIKSystemManagerState(bool state)` | `IKSystemManager` の有効/無効をそのまま委譲するだけ。 |
| `setIKBodyPausedState(bool state)` | `IKSystemManager` のIKボディ一時停止状態を委譲して設定するだけ。 |
| `isPlayerOnFreeFloatingMode()` | `freeFloatingModeOn` を返すだけ。 |
| `changeFreeFloatingMovementVelocity(bool value)` | `value` に応じて浮遊速度倍率を切替え、カメラFOVと `movementSpeedIncreased` を更新する。 |
| `changeSprintFovThirdPerson(bool value)` | `value` に応じて `playerCameraManager.changeCameraFov` を呼び分けるだけ。 |
| `isPlayerOnFFOrZeroGravityModeOn()` | 零重力か浮遊のどちらかが有効なら true を返す。 |
| `isMovementSpeedIncreased()` | `movementSpeedIncreased` を返すだけ。 |
| `getCharacterHeight()` | 元のキャラクター身長 `originalHeight` を返すだけ。 |
| `getVerticalSpeed()` | Rigidbody の速度をプレイヤー基準に変換したY成分（垂直速度）を返す。 |
| `getCurrentSurfaceHitAngle()` | `hitAngle`（現在の着地面の角度）を返すだけ。 |
| `setWalkSpeedValue(float newValue)` | `walkSpeed` を 0〜1 にクランプして設定するだけ。 |
| `setOriginalWalkSpeed()` | `originalWalkSpeedValue` で歩行速度を元に戻すだけ。 |
| `setWalkByDefaultState(bool state)` | true なら歩き速度を `half`、false なら 1 に設定するだけ。 |
| `setIncreaseMovementSpeedState(bool state)` | true なら `increaseWalkSpeedValue`、false なら元の歩行速度に戻すだけ。 |
| `setIncreaseWalkSpeedValue(float newValue)` | 値を設定し、元の速度より小さい場合に `increaseWalkSpeedActive` を true にする。 |
| `setIncreaseWalkSpeedEnabled(bool state)` | `increaseWalkSpeedEnabled` を設定し、`increaseWalkSpeedActive` を false に戻す。 |
| `setOriginalIncreaseWalkSpeedEnabledValue()` | 保存された元の `increaseWalkSpeedEnabled` 値へ戻すだけ。 |
| `setNewStationaryTurnSpeedValue(float newValue)` | `stationaryTurnSpeed` を設定するだけ。 |
| `setOriginalStationaryTurnSpeed()` | 保存された元の `stationaryTurnSpeed` へ戻すだけ。 |
| `setStairsValues(float stairsMin, float stairsMax, float stairsAdherence)` | 階段順応の最小・最大・順応度の3値をまとめて設定するだけ。 |
| `setUsingExternalCharacterMeshListState(bool state)` | `usingExternalCharacterMeshList` を設定するだけ。 |
| `setExternalCharacterMeshList(List<GameObject> newList)` | `externalCharacterMeshList` にリスト参照を代入するだけ。 |
| `setCharacterMeshGameObjectStateOnlyIfThirdPersonActive(bool state)` | 一人称視点が有効なら何もせず、そうでなければメッシュ表示状態を設定する。 |
| `setExternalCharacterMeshListGameObjectState(bool state)` | 外部メッシュリスト使用時のみ、リスト内各GameObjectの表示を `state` に揃える。 |
| `setCharacterMeshGameObjectState(bool state)` | メッシュの表示を一括切替し、生成メッシュの収集と有効/無効イベント発火も行う。 |
| `setCharacterMeshesListToDisableOnEventState(bool state)` | `characterMeshesListToDisableOnEvent` イベントを `state` 付きで発火するだけ。 |
| `setUsingGenericModelActiveState(bool state)` | `usingGenericModelActive` を設定するだけ。 |
| `isUsingGenericModelActive()` | `usingGenericModelActive` を返すだけ。 |
| `setExtraHeightDiffRaycastRadius(float newValue)` | `extraHeightDiffRaycastRadius` を設定するだけ。 |
| `setCustomMaxStepHeight(float newValue)` | `customMaxStepHeight` を設定するだけ。 |
| `setNewRayDistance(float newValue)` | `rayDistance` を設定するだけ。 |
| `setOriginalRayDistance()` | 保存された `originalRayDistance` へ戻すだけ。 |
| `getGravityCenter()` | `gravityManager` の重力中心をそのまま返すだけ。 |
| `isUsingRegularGravity()` | `gravityManager` に通常重力を使用中かを問い合わせて返すだけ。 |
| `getCharacterMeshGameObject()` | `characterMeshGameObject` を返すだけ。 |
| `getCharacterHumanBone(HumanBodyBones boneToFind)` | `animator.GetBoneTransform` で指定ヒューマンボーンを取得して返すだけ。 |
| `getRightHandTransform()` | 右手ボーンが取れればそれを、無ければ `weaponsManager` の右手を返す。 |
| `getLeftHandTransform()` | 左手ボーンが取れればそれを、無ければ `weaponsManager` の左手を返す。 |
| `checkPlayerIsNotCarringWeapons()` | 武器マネージャー検出時のみ武器非所持判定を委譲し、未検出なら false を返す。 |
| `getCharacterAnimator()` | `animator` を返すだけ。 |
| `setNewRuntimeAnimatorController(RuntimeAnimatorController newRuntimeAnimatorController)` | 現在と異なる場合のみ `animator.runtimeAnimatorController` を差し替える。 |
| `setAnimatorState(bool state)` | `animator.enabled` を設定するだけ。 |
| `resetAnimator()` | フルボディアウェアネス有効時は何もせず、それ以外はアニメーターを再バインドする。 |
| `resetAnimatorEvenIfFullBodyAwarenessActive()` | フルボディアウェアネスの状態に関係なくアニメーターを再バインドする。 |
| `setAnimatorUnscaledTimeState(bool state)` | `animator.updateMode` を UnscaledTime か Normal に切り替えるだけ。 |
| `playerCrossFadeInFixedTime(string actionName)` | `actionName` へ `updateSetFloatAnimatorSpeed` の時間でクロスフェードする。 |
| `setAnimatorLayerWeight(string animatorLayerName, float animatorLayerWeight)` | レイヤー名から index を引いて `animator.SetLayerWeight` を設定するだけ。 |
| `enableAnimatorLayerWeight(string animatorLayerName)` | 指定レイヤーの重みを 1 にするだけ。 |
| `disableAnimatorLayerWeight(string animatorLayerName)` | 指定レイヤーの重みを 0 にするだけ。 |
| `getPlayerInput()` | `playerInput` を返すだけ。 |
| `set3dOr2_5dWorldType(bool movingOn3dWorld)` | `lockedPlayerMovement` を3Dか2.5Dのワールド種別に切り替えるだけ。 |
| `setMoveInXAxisOn2_5dState(bool state)` | `moveInXAxisOn2_5d` を設定するだけ。 |
| `isMoveInXAxisOn2_5d()` | `moveInXAxisOn2_5d` を返すだけ。 |
| `isPlayerMovingOn3dWorld()` | ワールド種別が `world3d` かどうかを返すだけ。 |
| `isPlayerMovingOn2_5dWorld()` | ワールド種別が `world2_5d` かどうかを返すだけ。 |
| `isPlayerLookingAtRightOn2_5d()` | 2.5D時、前方とカメラ右方向のなす角が10度未満なら true を返す。 |
| `setFollowSplinePathActiveState(bool state)` | `followSplinePathActive` を設定するだけ。 |
| `isPlayerSetAsChildOfParent()` | `playerSetAsChildOfParent` を返すだけ。 |
| `getRigidbody()` | `mainRigidbody` を返すだけ。 |
| `setPlayerSetAsChildOfParentState(bool state)` | `playerSetAsChildOfParent` を設定するだけ。 |
| `setHeadTrackCanBeUsedState(bool state)` | `headTrackCanBeUsed` を設定するだけ。 |
| `canHeadTrackBeUsed()` | `headTrackCanBeUsed` を返すだけ。 |
| `setAddExtraRotationPausedState(bool state)` | `addExtraRotationPaused` を設定するだけ。 |
| `setAutoTurnSpeed(float newValue)` | `autoTurnSpeed` を設定するだけ。 |
| `setAimTurnSpeed(float newValue)` | `aimTurnSpeed` を設定するだけ。 |
| `updateLandMark()` | 接地マークの位置と向きをレイで更新し、距離に応じて表示切替とリング回転を行う。 |
| `setUseLandMarkState(bool state)` | `useLandMark` を設定するだけ。 |
| `rotateCharacterTowardDirection(Transform directionTransform, float minRotationAngle, float minRotationAmount, float maxRotationAmount)` | 既存の回転コルーチンを止め、指定トランスフォーム方向への回転を開始する。 |
| `stopRotateCharacterTowardDirectionCoroutine()` | 回転コルーチンを停止し、アクションフラグを解除して移動を許可し直す。 |
| `isTurnBasedCombatActionActive()` | `turnBasedCombatActionActive` を返すだけ。 |
| `setTurnBasedCombatActionActiveState(bool state)` | `turnBasedCombatActionActive` を設定するだけ。 |
| `isTerrainDetected()` | `terrainDetected` を返すだけ。 |
| `setTerrainDetectedState(bool state)` | `terrainDetected` を設定するだけ。 |
| `destroyCharacterAtOnce()` | プレイヤー管理親・カメラ・自身のGameObjectを即座に破棄する。 |
| `setCharacterMeshGameObject(GameObject characterMesh)` | `characterMeshGameObject` を設定し、エディタ用にコンポーネントを更新する。 |
| `setStrafeModeFromEditor(bool state)` | カメラ方向注視を `state` に設定し、移動時のみ注視を false にして更新通知する。 |
| `setCrouchSlidingEnabledStateFromEditor(bool state)` | `setCrouchSlidingEnabledState` を呼び、エディタ用にコンポーネントを更新する。 |
| `setAirDashEnabledStateFromEditor(bool state)` | `setAirDashEnabledState` を呼び、エディタ用にコンポーネントを更新する。 |
| `setWallRunningEnabledStateFromEditor(bool state)` | `wallRunningEnabled` を設定し、エディタ用にコンポーネントを更新する。 |
| `setUseObstacleDetectionToAvoidMovementStateFromEditor(bool state)` | `setUseObstacleDetectionToAvoidMovementState` を呼び、エディタ用に更新する。 |
| `setCheckQuickMovementTurn180DegreesOnRunStateFromEditor(bool state)` | `setCheckQuickMovementTurn180DegreesOnRunState` を呼び、エディタ用に更新する。 |
| `enableOrDisableDoubleJumpFromEditor(bool state)` | `enableOrDisableDoubleJump` を呼び、エディタ用にコンポーネントを更新する。 |
| `setUseLandMarkStateFromEditor(bool state)` | `setUseLandMarkState` を呼び、エディタ用にコンポーネントを更新する。 |
| `setSprintEnabledStateFromEditor(bool state)` | `setSprintEnabledState` を呼び、エディタ用にコンポーネントを更新する。 |
| `setIgnoreNewGroundAdherenceActiveState(bool state)` | `ignoreNewGroundAdherenceActive` を設定するだけ。 |
| `setInoreInputOnNewGroundAdherenceActive(bool state)` | `ignoreInputOnNewGroundAdherenceActive` を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartSprint` | `UnityEvent` | – |
| `eventOnStopSprint` | `UnityEvent` | – |
| `eventOnDelayOnGroundJump` | `UnityEvent` | – |
| `eventOnJump` | `UnityEvent` | – |
| `eventOnGroundJump` | `UnityEvent` | – |
| `eventOnLandFromJumpInput` | `UnityEvent` | – |
| `eventOnLand` | `UnityEvent` | – |
| `eventOnDoubleJump` | `UnityEvent` | – |
| `eventOnAirborne` | `UnityEvent` | – |
| `eventOnFallDamage` | `UnityEvent` | – |
| `eventOnCrouchSlidingStart` | `UnityEvent` | – |
| `eventOnCrouchSlidingEnd` | `UnityEvent` | – |
| `eventOnCrouchSlidingThirdPersonStart` | `UnityEvent` | – |
| `eventOnCrouchSlidingThirdPersonEnd` | `UnityEvent` | – |
| `eventOnAirDashThirdPerson` | `UnityEvent` | – |
| `eventOnAirDashFirstPerson` | `UnityEvent` | – |
| `eventOnWalkStart` | `UnityEvent` | – |
| `eventOnWalkEnd` | `UnityEvent` | – |
| `eventOnRunStart` | `UnityEvent` | – |
| `eventOnRunEnd` | `UnityEvent` | – |
| `eventOnEnableCharacterMeshes` | `UnityEvent` | – |
| `eventOnDisableCharacterMeshes` | `UnityEvent` | – |
| `eventOnEnableCharacterMeshesOnEditor` | `UnityEvent` | – |
| `eventOnDisableCharacterMeshesOnEditor` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnAnimatorMove()`

</details>

## 内部型

- `lockedPlayerMovementMode`（enum）
- `footStepState`（enum）
- `headbobState`（enum）
