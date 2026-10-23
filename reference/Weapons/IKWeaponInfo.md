# IKWeaponInfo

- **種別**: class
- **ソース**: `Weapons/IKWeaponInfo.cs:6`
- **属性**: `System.Serializable`

**概要**: 近接武器のIKや攻撃時サーフェス音を保持する情報クラス。音は`InitializeAudioElements`で`AudioElement`へ複写する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon | `weapon` | `GameObject` | – | – |
| Aim Position | `aimPosition` | `Transform` | – | – |
| Walk Position | `walkPosition` | `Transform` | – | – |
| Keep Position | `keepPosition` | `Transform` | – | – |
| Aim Recoil Position | `aimRecoilPosition` | `Transform` | – | – |
| Walk Recoil Position | `walkRecoilPosition` | `Transform` | – | – |
| Check Surface Collision | `checkSurfaceCollision` | `bool` | – | – |
| Collision Ray Distance | `collisionRayDistance` | `float` | 0.54f | – |
| Collision Movement Speed | `collisionMovementSpeed` | `float` | 10 | – |
| Surface Collision Position | `surfaceCollisionPosition` | `Transform` | – | – |
| Surface Collision Ray Position | `surfaceCollisionRayPosition` | `Transform` | – | – |
| Hide Cursor On Collision | `hideCursorOnCollision` | `bool` | – | – |
| Check Surface Only On Aiming | `checkSurfaceOnlyOnAiming` | `bool` | – | – |
| Avoid Shoot On Surface Detected | `avoidShootOnSurfaceDetected` | `bool` | – | – |
| Avoid Aiming If Surface Detected | `avoidAimingIfSurfaceDetected` | `bool` | – | – |
| Lower Weapon Position | `lowerWeaponPosition` | `Transform` | – | – |
| Use Sway Info | `useSwayInfo` | `bool` | true | – |
| Use Run Position | `useRunPosition` | `bool` | – | – |
| Run Movement Speed | `runMovementSpeed` | `float` | 10 | – |
| Run Position | `runPosition` | `Transform` | – | – |
| Hide Cursor On Run | `hideCursorOnRun` | `bool` | – | – |
| Use Run Sway Info | `useRunSwayInfo` | `bool` | – | – |
| Use Jump Positions | `useJumpPositions` | `bool` | – | – |
| Jump Start Position | `jumpStartPosition` | `Transform` | – | – |
| Jump End Position | `jumpEndPosition` | `Transform` | – | – |
| Jump Start Movement Speed | `jumpStartMovementSpeed` | `float` | 3 | – |
| Jump Endt Movement Speed | `jumpEndtMovementSpeed` | `float` | 3 | – |
| Reset Jump Movement Sped | `resetJumpMovementSped` | `float` | 3 | – |
| Delay At Jump End | `delayAtJumpEnd` | `float` | 0.4f | – |
| Use Reload Movement | `useReloadMovement` | `bool` | – | – |
| Reload Spline | `reloadSpline` | `BezierSpline` | – | – |
| Reload Duration | `reloadDuration` | `float` | 1 | – |
| Reload Look Direction Speed | `reloadLookDirectionSpeed` | `float` | 11 | – |
| Use New Fov On Run | `useNewFovOnRun` | `bool` | – | – |
| Change Fov Speed | `changeFovSpeed` | `float` | – | – |
| New Fov On Run | `newFovOnRun` | `float` | – | – |
| Use Melee Attack | `useMeleeAttack` | `bool` | – | – |
| Use Custom Melee Attack Layer | `useCustomMeleeAttackLayer` | `bool` | – | – |
| Custom Melee Attack Layer | `customMeleeAttackLayer` | `LayerMask` | – | – |
| Use Capsule Raycast | `useCapsuleRaycast` | `bool` | – | – |
| Melee Attack Position | `meleeAttackPosition` | `Transform` | – | – |
| Melee Attack Start Movement Speed | `meleeAttackStartMovementSpeed` | `float` | – | – |
| Melee Attack End Movement Speed | `meleeAttackEndMovementSpeed` | `float` | – | – |
| Melee Attack End Delay | `meleeAttackEndDelay` | `float` | – | – |
| Melee Attack Raycast Position | `meleeAttackRaycastPosition` | `Transform` | – | – |
| Melee Attack Raycast Distance | `meleeAttackRaycastDistance` | `float` | – | – |
| Melee Attack Capsule Distance | `meleeAttackCapsuleDistance` | `float` | 1.5f | – |
| Melee Attack Raycast Radius | `meleeAttackRaycastRadius` | `float` | – | – |
| Melee Attack Damage Amount | `meleeAttackDamageAmount` | `float` | – | – |
| Melee Attack Ignore Shield | `meleeAttackIgnoreShield` | `bool` | – | – |
| Use Melee Attack Shake Info | `useMeleeAttackShakeInfo` | `bool` | – | – |
| Apply Melee Atack Force | `applyMeleeAtackForce` | `bool` | – | – |
| Melee Attack Force Amount | `meleeAttackForceAmount` | `float` | – | – |
| Melee Attack Force Mode | `meleeAttackForceMode` | `ForceMode` | – | – |
| Melee Attack Apply Force To Vehicles | `meleeAttackApplyForceToVehicles` | `bool` | – | – |
| Mele Attack Force To Vehicles | `meleAttackForceToVehicles` | `float` | – | – |
| Use Melee Attack Sound | `useMeleeAttackSound` | `bool` | – | – |
| Melee Attack Surface Sound | `meleeAttackSurfaceSound` | `AudioClip` | – | – |
| Melee Attack Surface Audio Element | `meleeAttackSurfaceAudioElement` | `AudioElement` | – | – |
| Melee Attack Air Sound | `meleeAttackAirSound` | `AudioClip` | – | – |
| Melee Attack Air Audio Element | `meleeAttackAirAudioElement` | `AudioElement` | – | – |
| Use Melee Attack Particles | `useMeleeAttackParticles` | `bool` | – | – |
| Melee Attack Particles | `meleeAttackParticles` | `GameObject` | – | – |
| Can Activate Reaction System Temporally | `canActivateReactionSystemTemporally` | `bool` | – | – |
| Damage Reaction ID | `damageReactionID` | `int` | -1 | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |
| Use Action System For Melee Attack | `useActionSystemForMeleeAttack` | `bool` | – | – |
| Melee Attack Action Name | `meleeAttackActionName` | `string` | – | – |
| Ignore Damage Value On Layer | `ignoreDamageValueOnLayer` | `bool` | – | – |
| Layer To Ignore Damage | `layerToIgnoreDamage` | `LayerMask` | – | – |
| Check Objects To Use Remote Events On Damage | `checkObjectsToUseRemoteEventsOnDamage` | `bool` | – | – |
| Layer To Use Remote Events On Damage | `layerToUseRemoteEventsOnDamage` | `LayerMask` | – | – |
| Use Remote Event | `useRemoteEvent` | `bool` | – | – |
| Remote Event Name List | `remoteEventNameList` | `List<string>` | – | – |
| Use Remote Event To Enable Parry Interaction | `useRemoteEventToEnableParryInteraction` | `bool` | – | – |
| Remote Event To Enable Parry Interaction Name List | `remoteEventToEnableParryInteractionNameList` | `List<string>` | – | – |
| Show Melee Attack Gizmo | `showMeleeAttackGizmo` | `bool` | – | – |
| Has Attachments | `hasAttachments` | `bool` | – | – |
| Edit Attachment Position | `editAttachmentPosition` | `Transform` | – | – |
| Attachment Camera Position | `attachmentCameraPosition` | `Transform` | – | – |
| Left Hand Mesh | `leftHandMesh` | `GameObject` | – | – |
| Extra Left Hand Mesh | `extraLeftHandMesh` | `GameObject` | – | – |
| Left Hand Edit Position | `leftHandEditPosition` | `Transform` | – | – |
| Left Hand Parent | `leftHandParent` | `Transform` | – | – |
| Extra Left Hand Mesh Parent | `extraLeftHandMeshParent` | `Transform` | – | – |
| Edit Attachment Movement Speed | `editAttachmentMovementSpeed` | `float` | 2 | – |
| Edit Attachment Hand Speed | `editAttachmentHandSpeed` | `float` | 6 | – |
| Using Second Position For Hand | `usingSecondPositionForHand` | `bool` | – | – |
| Second Position For Hand | `secondPositionForHand` | `Transform` | – | – |
| Use Sight Position | `useSightPosition` | `bool` | – | – |
| Sight Position | `sightPosition` | `Transform` | – | – |
| Sight Recoil Position | `sightRecoilPosition` | `Transform` | – | – |
| Can Run While Carrying | `canRunWhileCarrying` | `bool` | true | – |
| Can Run While Aiming | `canRunWhileAiming` | `bool` | true | – |
| Use New Carry Speed | `useNewCarrySpeed` | `bool` | – | – |
| New Carry Speed | `newCarrySpeed` | `float` | – | – |
| Use New Aim Speed | `useNewAimSpeed` | `bool` | – | – |
| New Aim Speed | `newAimSpeed` | `float` | – | – |
| Deactivate IK If Not Aiming | `deactivateIKIfNotAiming` | `bool` | – | – |
| Place Weapon On Walk Position Before Deactivate IK | `placeWeaponOnWalkPositionBeforeDeactivateIK` | `bool` | true | – |
| Deactivate IK Draw Path | `deactivateIKDrawPath` | `List<Transform>` | new List<Transform> () | – |
| Weapon Position In Hand For Deactivate IK | `weaponPositionInHandForDeactivateIK` | `Transform` | – | – |
| Draw Weapon Movement Speed | `drawWeaponMovementSpeed` | `float` | 2 | – |
| Aim Movement Speed | `aimMovementSpeed` | `float` | – | – |
| Weapon Has Recoil | `weaponHasRecoil` | `bool` | true | – |
| Recoil Speed | `recoilSpeed` | `float` | 5 | – |
| End Recoil Speed | `endRecoilSpeed` | `float` | 4 | – |
| Use Extra Random Recoil | `useExtraRandomRecoil` | `bool` | – | – |
| Use Extra Random Recoil Position | `useExtraRandomRecoilPosition` | `bool` | true | – |
| Extra Random Recoil Position | `extraRandomRecoilPosition` | `Vector3` | – | – |
| Use Extra Random Recoil Rotation | `useExtraRandomRecoilRotation` | `bool` | true | – |
| Extra Random Recoil Rotation | `extraRandomRecoilRotation` | `Vector3` | – | – |
| Reset Weapon Position After Reload Speed | `resetWeaponPositionAfterReloadSpeed` | `float` | 3 | – |
| Reset Weapon Position After Action Speed | `resetWeaponPositionAfterActionSpeed` | `float` | 5 | – |
| Resume Weapon IK Position After Action Speed | `resumeWeaponIKPositionAfterActionSpeed` | `float` | 8 | – |
| Use Quick Draw Keep Weapon | `useQuickDrawKeepWeapon` | `bool` | – | – |
| Use Bezier Curve | `useBezierCurve` | `bool` | – | – |
| Spline | `spline` | `BezierSpline` | – | – |
| Bezier Duration | `bezierDuration` | `float` | 0.5f | – |
| Look Direction Speed | `lookDirectionSpeed` | `float` | 11 | – |
| Keep Path | `keepPath` | `List<Transform>` | new List<Transform> () | – |
| Hands Info | `handsInfo` | `List<IKWeaponsPosition>` | new List<IKWeaponsPosition> () | – |
| Hands In Position | `handsInPosition` | `bool` | – | – |
| Use Weapon Rotation Point | `useWeaponRotationPoint` | `bool` | – | – |
| Weapon Rotation Point | `weaponRotationPoint` | `Transform` | – | – |
| Weapon Rotation Point Holder | `weaponRotationPointHolder` | `Transform` | – | – |
| Weapon Rotation Point Head Look Target | `weaponRotationPointHeadLookTarget` | `Transform` | – | – |
| Rotation Point Info | `rotationPointInfo` | `weaponRotationPointInfo` | – | – |
| Weapon Pivot Point | `weaponPivotPoint` | `Transform` | – | – |
| Use Crouch Position | `useCrouchPosition` | `bool` | – | – |
| Crouch Position | `crouchPosition` | `Transform` | – | – |
| Crouch Recoil Position | `crouchRecoilPosition` | `Transform` | – | – |
| Crouch Movement Speed | `crouchMovementSpeed` | `float` | 5 | – |
| Use Handle | `useHandle` | `bool` | – | – |
| Handle Radius | `handleRadius` | `float` | – | Range (0, 0.1f) |
| Handle Gizmo Color | `handleGizmoColor` | `Color` | – | – |
| Use Position Handle | `usePositionHandle` | `bool` | true | – |
| Dual Weapon Active | `dualWeaponActive` | `bool` | – | – |
| Used On Right Hand | `usedOnRightHand` | `bool` | – | – |
| Can Be Used As Dual Weapon | `canBeUsedAsDualWeapon` | `bool` | – | – |
| Right Hand Dual Weaopn Info | `rightHandDualWeaopnInfo` | `dualWeaponInfo` | – | – |
| Left Hand Dual Weapon Info | `leftHandDualWeaponInfo` | `dualWeaponInfo` | – | – |
| Change One Or Two Hand Wield Speed | `changeOneOrTwoHandWieldSpeed` | `float` | 5 | – |
| Using Weapon As One Hand Wield | `usingWeaponAsOneHandWield` | `bool` | – | – |
| Show Single Weapon Settings | `showSingleWeaponSettings` | `bool` | – | – |
| Show Dual Weapon Settings | `showDualWeaponSettings` | `bool` | – | – |
| Use Custom Third Person Aim Active | `useCustomThirdPersonAimActive` | `bool` | – | – |
| Custom Default Third Person Aim Right State Name | `customDefaultThirdPersonAimRightStateName` | `string` | – | – |
| Custom Default Third Person Aim Left State Name | `customDefaultThirdPersonAimLeftStateName` | `string` | – | – |
| Use Custom Third Person Aim Crouch Active | `useCustomThirdPersonAimCrouchActive` | `bool` | – | – |
| Custom Default Third Person Aim Right Crouch State Name | `customDefaultThirdPersonAimRightCrouchStateName` | `string` | – | – |
| Custom Default Third Person Aim Left Crouch State Name | `customDefaultThirdPersonAimLeftCrouchStateName` | `string` | – | – |
| Use Custom Third Person Without Aim Active | `useCustomThirdPersonWithoutAimActive` | `bool` | – | – |
| Custom Default Third Person Without Aim Right State Name | `customDefaultThirdPersonWithoutAimRightStateName` | `string` | – | – |
| Custom Default Third Person Without Aim Left State Name | `customDefaultThirdPersonWithoutAimLeftStateName` | `string` | – | – |
| Use Custom Third Person Without Aim Crouch Active | `useCustomThirdPersonWithoutAimCrouchActive` | `bool` | – | – |
| Custom Default Third Person Without Aim Right Crouch State Name | `customDefaultThirdPersonWithoutAimRightCrouchStateName` | `string` | – | – |
| Custom Default Third Person Without Aim Left Crouch State Name | `customDefaultThirdPersonWithoutAimLeftCrouchStateName` | `string` | – | – |
| Use New Idle ID | `useNewIdleID` | `bool` | – | – |
| New Idle ID | `newIdleID` | `int` | – | – |
| Use Draw Keep Weapon Animation | `useDrawKeepWeaponAnimation` | `bool` | – | – |
| Draw Weapon Action Name | `drawWeaponActionName` | `string` | – | – |
| Keep Weapon Action Name | `keepWeaponActionName` | `string` | – | – |
| Delay To Place Weapon On Hand On Draw Animation | `delayToPlaceWeaponOnHandOnDrawAnimation` | `float` | 1 | – |
| Delay To Place Weapon On Keep Animation | `delayToPlaceWeaponOnKeepAnimation` | `float` | 1 | – |
| FBA Walk Position Offset | `FBAWalkPositionOffset` | `Vector3` | – | – |
| FBA Walk Rotation Offset | `FBAWalkRotationOffset` | `Vector3` | – | – |
| FBA Walk Recoil Position Offset | `FBAWalkRecoilPositionOffset` | `Vector3` | – | – |
| FBA Walk Recoil Rotation Offset | `FBAWalkRecoilRotationOffset` | `Vector3` | – | – |
| FBA Run Position Offset | `FBARunPositionOffset` | `Vector3` | – | – |
| FBA Run Rotation Offset | `FBARunRotationOffset` | `Vector3` | – | – |
| FBA Aim Position Offset | `FBAAimPositionOffset` | `Vector3` | – | – |
| FBA Aim Rotation Offset | `FBAAimRotationOffset` | `Vector3` | – | – |
| FBA Aim Recoil Position Offset | `FBAAimRecoilPositionOffset` | `Vector3` | – | – |
| FBA Aim Recoil Rotation Offset | `FBAAimRecoilRotationOffset` | `Vector3` | – | – |
| FBA Crouch Position Offset | `FBACrouchPositionOffset` | `Vector3` | – | – |
| FBA Crouch Rotation Offset | `FBACrouchRotationOffset` | `Vector3` | – | – |
| FBA Crouch Recoil Position Offset | `FBACrouchRecoilPositionOffset` | `Vector3` | – | – |
| FBA Crouch Recoil Rotation Offset | `FBACrouchRecoilRotationOffset` | `Vector3` | – | – |
| FBA Jump Start Position Offset | `FBAJumpStartPositionOffset` | `Vector3` | – | – |
| FBA Jump Start Rotation Offset | `FBAJumpStartRotationOffset` | `Vector3` | – | – |
| FBA Jump End Position Offset | `FBAJumpEndPositionOffset` | `Vector3` | – | – |
| FBA Jump End Rotation Offset | `FBAJumpEndRotationOffset` | `Vector3` | – | – |
| FBA Obstacle Position Offset | `FBAObstaclePositionOffset` | `Vector3` | – | – |
| FBA Obstacle Rotation Offset | `FBAObstacleRotationOffset` | `Vector3` | – | – |
| FBA Move Walk Position Speed | `FBAMoveWalkPositionSpeed` | `float` | 20 | – |
| Override FBA Values For Offset | `overrideFBAValuesForOffset` | `bool` | – | – |
| FBA Random Recoil Walk Position Multiplier | `FBARandomRecoilWalkPositionMultiplier` | `float` | 1 | – |
| FBA Random Recoil Aim Position Multiplier | `FBARandomRecoilAimPositionMultiplier` | `float` | 1 | – |
| Use FBA Run Position | `useFBARunPosition` | `bool` | – | – |
| Ignore IK Elbows On FBA | `ignoreIKElbowsOnFBA` | `bool` | – | – |
| FBA Aim Info List | `FBAAimInfoList` | `List<FBAAimInfo>` | new List<FBAAimInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `InitializeAudioElements()` | 2つの近接攻撃音が設定されていれば、対応する`AudioElement.clip`へ代入する。 |
