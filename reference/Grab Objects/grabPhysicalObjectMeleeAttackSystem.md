# grabPhysicalObjectMeleeAttackSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `weaponObjectInfo`
- **ソース**: `Grab Objects/grabPhysicalObjectMeleeAttackSystem.cs:6`

**概要**: 近接武器（剣・槍など）の攻撃情報、投擲と返却、防御、耐久値、追加アクション、被弾面のリモートイベントをまとめて管理する武器コンポーネント。`grabPhysicalObjectSystem`と連携し、攻撃リストやトレイル、ダメージ属性を実行時に切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Name | `weaponName` | `string` | – | – |
| Use Random Attack Index | `useRandomAttackIndex` | `bool` | – | – |
| Only Attack If No Previous Attack In Process | `onlyAttackIfNoPreviousAttackInProcess` | `bool` | – | – |
| Min Delay Between Attacks | `minDelayBetweenAttacks` | `float` | 0.5f | – |
| Reset Index If Not Attack After Delay | `resetIndexIfNotAttackAfterDelay` | `bool` | – | – |
| Delay To Reset Index After Attack | `delayToResetIndexAfterAttack` | `float` | – | – |
| Weapon Info Name | `weaponInfoName` | `string` | – | – |
| Object Uses Stamina On Attacks | `objectUsesStaminaOnAttacks` | `bool` | true | – |
| Hide Weapon Mesh When Not Used | `hideWeaponMeshWhenNotUsed` | `bool` | – | – |
| Disable Melee Object Collider | `disableMeleeObjectCollider` | `bool` | true | – |
| Ignore Use IK On Hands | `ignoreUseIKOnHands` | `bool` | – | – |

### Block Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Use Block | `canUseBlock` | `bool` | – | – |
| Block Action Name | `blockActionName` | `string` | – | – |
| Block Damage Protection Amount | `blockDamageProtectionAmount` | `float` | 1 | – |
| Use Max Block Range Angle | `useMaxBlockRangeAngle` | `bool` | – | – |
| Max Block Range Angle | `maxBlockRangeAngle` | `float` | 360 | – |
| Block ID | `blockID` | `int` | – | – |
| Reduced Block Damage Protection Amount | `reducedBlockDamageProtectionAmount` | `float` | 0.1f | – |

### Shield Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Use Shield Block | `canUseShieldBlock` | `bool` | – | – |
| Shield Block Action Name | `shieldBlockActionName` | `string` | – | – |
| Shield Block ID | `shieldBlockID` | `int` | – | – |

### Match Target Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Match Position System On All Attacks | `useMatchPositionSystemOnAllAttacks` | `bool` | – | – |
| Match Position Offset On All Attacks | `matchPositionOffsetOnAllAttacks` | `float` | 1.6f | – |

### Throw/Return Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hold To Throw Object Enabled | `holdToThrowObjectEnabled` | `bool` | – | – |
| Locate Objectst To Track On Hold Enabled | `locateObjectstToTrackOnHoldEnabled` | `bool` | – | – |
| Layer To Locate Objects To Track | `layerToLocateObjectsToTrack` | `LayerMask` | – | – |
| Max Raycast Distance To Locate Object To Track | `maxRaycastDistanceToLocateObjectToTrack` | `float` | – | – |
| Can Throw Object | `canThrowObject` | `bool` | – | – |
| Can Return Object | `canReturnObject` | `bool` | – | – |
| Can Re Use Object If Not Return Active | `canReUseObjectIfNotReturnActive` | `bool` | true | – |
| Throw Speed | `throwSpeed` | `float` | – | – |
| Return Speed | `returnSpeed` | `float` | – | – |
| Use Down Force On Weapon Travel | `useDownForceOnWeaponTravel` | `bool` | – | – |
| Down Force On Weapon Travel | `downForceOnWeaponTravel` | `float` | – | – |
| Return Spline Speed | `returnSplineSpeed` | `float` | – | – |
| Reset Object Rotation Speed | `resetObjectRotationSpeed` | `float` | – | – |
| Delay To Throw Object | `delayToThrowObject` | `float` | – | – |
| Delay To Return Object | `delayToReturnObject` | `float` | – | – |
| Max Time On Air If No Surface Found | `maxTimeOnAirIfNoSurfaceFound` | `float` | – | – |
| Ignore Rigidbodies On Throw Weapon | `ignoreRigidbodiesOnThrowWeapon` | `bool` | – | – |
| Ignore Attach To Located Object On Throw | `ignoreAttachToLocatedObjectOnThrow` | `bool` | – | – |
| Follow Object On Throw Melee Weapon Speed | `followObjectOnThrowMeleeWeaponSpeed` | `float` | 45 | – |

### Throw/Return Push Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Push Characters Detected On Ignore Rigidbodies On Throw Weapon | `pushCharactersDetectedOnIgnoreRigidbodiesOnThrowWeapon` | `bool` | – | – |
| Push Characters Detected On Ignore Rigidbodies On Throw Weapon Multiplier | `pushCharactersDetectedOnIgnoreRigidbodiesOnThrowWeaponMultiplier` | `float` | 1 | – |
| Push Characters Detected On Ignore Rigidbodies On Throw Weapon Message Name To Send | `pushCharactersDetectedOnIgnoreRigidbodiesOnThrowWeaponMessageNameToSend` | `string` | "pushCharacter" | – |
| Push Characters Detected On Ignore Rigidbodies On Return Weapon | `pushCharactersDetectedOnIgnoreRigidbodiesOnReturnWeapon` | `bool` | – | – |
| Push Characters Detected On Ignore Rigidbodies On Return Weapon Multiplier | `pushCharactersDetectedOnIgnoreRigidbodiesOnReturnWeaponMultiplier` | `float` | 1 | – |
| Push Characters Detected On Ignore Rigidbodies On Return Weapon Message Name To Send | `pushCharactersDetectedOnIgnoreRigidbodiesOnReturnWeaponMessageNameToSend` | `string` | "pushCharacter" | – |

### Other Throw/Return Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Throw Object With Rotation | `throwObjectWithRotation` | `bool` | true | – |
| Throw Object Rotation Speed | `throwObjectRotationSpeed` | `float` | 500 | – |
| Return Object With Rotation | `returnObjectWithRotation` | `bool` | true | – |
| Return Object Rotation Speed | `returnObjectRotationSpeed` | `float` | 500 | – |
| Rotate Object To Throw Direction | `rotateObjectToThrowDirection` | `bool` | – | – |
| Use Spline For Return | `useSplineForReturn` | `bool` | true | – |
| Can Return Weapon If No Surface Found | `canReturnWeaponIfNoSurfaceFound` | `bool` | – | – |
| Ignore If Surface Found To Return Weapon | `ignoreIfSurfaceFoundToReturnWeapon` | `bool` | – | – |
| Rotate Weapon To Surface Located When Close Enough | `rotateWeaponToSurfaceLocatedWhenCloseEnough` | `bool` | – | – |
| Attach To Surface Adjust Speed | `attachToSurfaceAdjustSpeed` | `float` | 5 | – |
| Use Cut On Throw Object | `useCutOnThrowObject` | `bool` | – | – |
| Use Cut On Return Object | `useCutOnReturnObject` | `bool` | – | – |
| Return Weapon If Object Detected | `returnWeaponIfObjectDetected` | `bool` | – | – |

### Throw/Return Action Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Throw Action Name | `useThrowActionName` | `bool` | – | – |
| Throw Action Name | `throwActionName` | `string` | – | – |
| Use Start Return Action Name | `useStartReturnActionName` | `bool` | – | – |
| Start Return Action Name | `startReturnActionName` | `string` | – | – |
| Use End Return Action Name | `useEndReturnActionName` | `bool` | – | – |
| End Return Action Name | `endReturnActionName` | `string` | – | – |

### Throw/Return Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Force To Apply To Surface Found | `forceToApplyToSurfaceFound` | `float` | – | – |
| Force Extra To Apply On Vehicles Found | `forceExtraToApplyOnVehiclesFound` | `float` | – | – |
| Capsule Cast Radius | `capsuleCastRadius` | `float` | 1 | – |
| Capsule Cast Distance | `capsuleCastDistance` | `float` | 2 | – |

### Throw/Return Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Damage On Surface Detected On Throw | `damageOnSurfaceDetectedOnThrow` | `float` | – | – |
| Apply Damage On Surface Detected On Return | `applyDamageOnSurfaceDetectedOnReturn` | `bool` | – | – |
| Damage On Surface Detected On Return | `damageOnSurfaceDetectedOnReturn` | `float` | – | – |
| Apply Damage On Object Return Path | `applyDamageOnObjectReturnPath` | `bool` | true | – |
| Damage On Object Return Path | `damageOnObjectReturnPath` | `float` | 20 | – |

### Throw/Return Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Throw Return | `useEventsOnThrowReturn` | `bool` | – | – |
| Event On Throw Start | `eventOnThrowStart` | `UnityEvent` | – | – |
| Event On Throw End | `eventOnThrowEnd` | `UnityEvent` | – | – |
| Event On Return Start | `eventOnReturnStart` | `UnityEvent` | – | – |
| Event On Return End | `eventOnReturnEnd` | `UnityEvent` | – | – |

### Throw/Return Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Throw | `useRemoteEventOnThrow` | `bool` | – | – |
| Remote Event On Throw Name List | `remoteEventOnThrowNameList` | `List<string>` | new List<string> () | – |
| Use Remote Event On Return | `useRemoteEventOnReturn` | `bool` | – | – |
| Remote Event On Return Name List | `remoteEventOnReturnNameList` | `List<string>` | new List<string> () | – |

### Teleport Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Teleport Player On Throw Enabled | `teleportPlayerOnThrowEnabled` | `bool` | true | – |
| Throw Weapon Quickly And Teleport If Surface Found | `throwWeaponQuicklyAndTeleportIfSurfaceFound` | `bool` | – | – |
| Extra Speed On Throw Weapon Quickly And Teleport | `extraSpeedOnThrowWeaponQuicklyAndTeleport` | `float` | 6 | – |

### Trail Renderer Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Trail Speed | `trailSpeed` | `float` | 10 | – |
| Use Trail On Throw Return | `useTrailOnThrowReturn` | `bool` | – | – |

### Keep/Draw Weapon Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Keep Or Draw Melee Weapon | `useEventsOnKeepOrDrawMeleeWeapon` | `bool` | – | – |
| Events On Keep Melee Weapon | `eventsOnKeepMeleeWeapon` | `UnityEvent` | – | – |
| Events On Draw Melee Weapon | `eventsOnDrawMeleeWeapon` | `UnityEvent` | – | – |

### Cutting Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Activate Cutting Mode | `canActivateCuttingMode` | `bool` | – | – |
| Cut Overlap Box Size | `cutOverlapBoxSize` | `Vector3` | – | – |
| Cut Position Transform | `cutPositionTransform` | `Transform` | – | – |
| Cut Direction Transform | `cutDirectionTransform` | `Transform` | – | – |
| Plane Definer1 | `planeDefiner1` | `Transform` | – | – |
| Plane Definer2 | `planeDefiner2` | `Transform` | – | – |
| Plane Definer3 | `planeDefiner3` | `Transform` | – | – |

### Attack List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attacks Enabled | `attacksEnabled` | `bool` | true | – |
| Use Animation Percentage Duration | `useAnimationPercentageDuration` | `bool` | – | – |
| Use Animation Percentage Over100 | `useAnimationPercentageOver100` | `bool` | – | – |
| Use General Damage Type ID | `useGeneralDamageTypeID` | `bool` | – | – |
| General Damage Type ID | `generalDamageTypeID` | `int` | -1 | – |
| Attack Info List | `attackInfoList` | `List<attackInfo>` | new List<attackInfo> () | – |
| Use Events On All Attacks | `useEventsOnAllAttacks` | `bool` | – | – |
| Event On Attack Start | `eventOnAttackStart` | `UnityEvent` | – | – |
| Event On Attack End | `eventOnAttackEnd` | `UnityEvent` | – | – |

### Dual Wield Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Is Dual Wield Weapon | `isDualWieldWeapon` | `bool` | – | – |
| Main Dual Wield Melee Weapon Object System | `mainDualWieldMeleeWeaponObjectSystem` | `dualWieldMeleeWeaponObjectSystem` | – | – |

### Melee Attack Info Template Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Melee Weapon Attack Info Template | `useMeleeWeaponAttackInfoTemplate` | `bool` | – | – |
| Main Melee Weapon Attack Info Template | `mainMeleeWeaponAttackInfoTemplate` | `meleeWeaponAttackInfo` | – | – |

### Damage Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Raycast Check Transfrom List | `raycastCheckTransfromList` | `List<Transform>` | new List<Transform> () | – |
| Use Custom Surface Info On Melee Attack Name For Swing On Air | `useCustomSurfaceInfoOnMeleeAttackNameForSwingOnAir` | `bool` | – | – |
| Custom Surface Info On Melee Attack Name For Swing On Air | `customSurfaceInfoOnMeleeAttackNameForSwingOnAir` | `string` | – | – |

### Damage Type And Reaction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Damage Type And Reaction Info List | `damageTypeAndReactionInfoList` | `List<damageTypeAndReactionInfo>` | new List<damageTypeAndReactionInfo> () | – |

### Melee Weapon Mesh Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Mesh | `weaponMesh` | `GameObject` | – | – |
| Use Custom Weapon Mesh To Instantiate | `useCustomWeaponMeshToInstantiate` | `bool` | – | – |
| Custom Weapon Mesh To Instantiate | `customWeaponMeshToInstantiate` | `GameObject` | – | – |

### Deflect Projectiles Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Deflect Projectiles Enabled | `deflectProjectilesEnabled` | `bool` | – | – |
| Main Armore Surface System | `mainArmoreSurfaceSystem` | `armorSurfaceSystem` | – | – |
| Deflect Projectiles On Block Enabled | `deflectProjectilesOnBlockEnabled` | `bool` | – | – |
| Use Duration To Deflect Projectiles On Block | `useDurationToDeflectProjectilesOnBlock` | `bool` | – | – |
| Duration To Defleclt Projectiles On Block | `durationToDeflecltProjectilesOnBlock` | `float` | – | – |
| Adjust Trigger Scale Values Enabled | `adjustTriggerScaleValuesEnabled` | `bool` | – | – |
| Deflect Projectiles Trigger Center | `deflectProjectilesTriggerCenter` | `Vector3` | – | – |
| Deflect Projectiles Trigger Size | `deflectProjectilesTriggerSize` | `Vector3` | – | – |
| Deflect Projectiles On Block Trigger Center | `deflectProjectilesOnBlockTriggerCenter` | `Vector3` | – | – |
| Deflect Projectiles On Block Trigger Size | `deflectProjectilesOnBlockTriggerSize` | `Vector3` | – | – |

### Draw/Keep Weapon Settings Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Draw Keep Weapon Animation | `useDrawKeepWeaponAnimation` | `bool` | – | – |
| Draw Weapon Action Name | `drawWeaponActionName` | `string` | – | – |
| Keep Weapon Action Name | `keepWeaponActionName` | `string` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Surfaces Detected | `useRemoteEventOnSurfacesDetected` | `bool` | – | – |
| Remote Event Name List On Surface Detected | `remoteEventNameListOnSurfaceDetected` | `List<remoteEventOnSurfaceDetectedInfo>` | new List<remoteEventOnSurfaceDetected… | – |

### Enable/Disable Abilities on Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Abilities List To Enable On Weapon | `useAbilitiesListToEnableOnWeapon` | `bool` | – | – |
| Abilities List To Enable On Weapon | `abilitiesListToEnableOnWeapon` | `List<string>` | new List<string> () | – |
| Use Abilities List To Disable On Weapon | `useAbilitiesListToDisableOnWeapon` | `bool` | – | – |
| Abilities List To Disable On Weapon | `abilitiesListToDisableOnWeapon` | `List<string>` | new List<string> () | – |

### Extra Actions List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Extra Actions | `useExtraActions` | `bool` | – | – |
| Current Extra Action Index | `currentExtraActionIndex` | `int` | – | – |
| Use Default Extra Action Index | `useDefaultExtraActionIndex` | `bool` | – | – |
| Default Extra Action Index | `defaultExtraActionIndex` | `int` | – | – |
| Extra Action Melee Weapon Info List | `extraActionMeleeWeaponInfoList` | `List<extraActionMeleeWeaponInfo>` | new List<extraActionMeleeWeaponInfo> () | – |

### Durability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Object Durability On Attack | `useObjectDurabilityOnAttack` | `bool` | – | – |
| Durability Used On Attack | `durabilityUsedOnAttack` | `float` | 1 | – |
| Use Object Durability On Block | `useObjectDurabilityOnBlock` | `bool` | – | – |
| Durability Used On Block | `durabilityUsedOnBlock` | `float` | 1 | – |
| Main Durability Info | `mainDurabilityInfo` | `durabilityInfo` | – | – |

### Object Stats Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Object Stats System Enabled | `useObjectStatsSystemEnabled` | `bool` | – | – |
| Main Object Stats System | `mainObjectStatsSystem` | `objectStatsSystem` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Keep Grabbed Object State | `keepGrabbedObjectState` | `bool` | – | – |
| Object Thrown | `objectThrown` | `bool` | – | – |
| Previous Strafe Mode | `previousStrafeMode` | `bool` | – | – |
| Secondary Ability Active | `secondaryAbilityActive` | `bool` | – | – |
| Current Character | `currentCharacter` | `GameObject` | – | – |
| Use Custom Reference Position To Keep Object Mesh | `useCustomReferencePositionToKeepObjectMesh` | `bool` | – | – |
| Custom Reference Position To Keep Object Mesh | `customReferencePositionToKeepObjectMesh` | `Transform` | – | – |
| Custom Reference To Keep Object Mesh Position | `customReferenceToKeepObjectMeshPosition` | `Vector3` | – | – |
| Custom Reference To Keep Object Mesh Euler | `customReferenceToKeepObjectMeshEuler` | `Vector3` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Hit Combat | `mainHitCombat` | `hitCombat` | – | – |
| Main Object Collider | `mainObjectCollider` | `Collider` | – | – |
| Object Rotation Point | `objectRotationPoint` | `Transform` | – | – |
| Raycast Check Transfrom | `raycastCheckTransfrom` | `Transform` | – | – |
| Object Rotation Point Parent | `objectRotationPointParent` | `Transform` | – | – |
| Raycast Check Transform Parent | `raycastCheckTransformParent` | `Transform` | – | – |
| Main Traile Renderer | `mainTraileRenderer` | `TrailRenderer` | – | – |
| Attach To Characters Reference Transform | `attachToCharactersReferenceTransform` | `Transform` | – | – |
| Main Damage Position Transform | `mainDamagePositionTransform` | `Transform` | – | – |
| Reference Position To Keep Object Mesh | `referencePositionToKeepObjectMesh` | `Transform` | – | – |
| Main Grab Physical Object System | `mainGrabPhysicalObjectSystem` | `grabPhysicalObjectSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setRegularDeflectProjectilesTriggerScaleValues()` | `adjustTriggerScaleValuesEnabled`有効時、通常の弾反射トリガー範囲を`mainArmoreSurfaceSystem`へ適用する。 |
| `setBlockDeflectProjectilesTriggerScaleValues()` | 調整が有効ならブロック時の弾反射トリガーの中心とサイズを`mainArmoreSurfaceSystem`に適用する。 |
| `setMainObjectColliderEnabledState(bool state)` | `mainObjectCollider`がnullでなければ`enabled`を`state`に切り替えるだけ。 |
| `getAttackListCount()` | `attackInfoList`の要素数を返すだけ。 |
| `getMainHitCombat()` | `mainHitCombat`の参照を返すだけ。 |
| `setKeepOrCarryGrabbebObjectState(bool state)` | `keepGrabbedObjectState`を`state`に設定するだけ。 |
| `iskeepGrabbedObjectStateActive()` | `keepGrabbedObjectState`の値を返すだけ。 |
| `setObjectThrownState(bool state)` | `objectThrown`を`state`に設定するだけ。 |
| `isObjectThrown()` | `objectThrown`の値を返すだけ。 |
| `checkEventOnThrow(bool state)` | 投擲イベント有効時は`state`で開始/終了イベントを発火し、トレイル設定時はトレイルも切り替える。 |
| `checkEventOnReturn(bool state)` | 返却イベント有効時は`state`で開始/終了イベントを発火し、トレイル設定時はトレイルも切り替える。 |
| `checkEventOnAttackStartAndEnd(bool state)` | `useEventsOnAllAttacks`が有効なとき、`state`に応じて攻撃開始/終了イベントを発火するだけ。 |
| `checkEventWhenKeepingOrDrawingMeleeWeapon(bool state)` | 有効時、`state`で武器をしまう/抜くイベントを発火するだけ。 |
| `setUseCustomReferencePositionToKeepObjectMesh(bool state, Transform newTransform)` | カスタム参照`Transform`の使用可否を設定し、設定時はそのローカル位置と角度を保持する。 |
| `setUseCustomReferencePositionToKeepObjectMesh(bool state, Vector3 localPosition, Vector3 localEulerAngles)` | 使用可否と、保持するローカル位置・角度を直接設定するだけ。 |
| `getCustomReferenceToKeepObjectMeshPosition()` | `customReferenceToKeepObjectMeshPosition`の値を返すだけ。 |
| `getCustomReferenceToKeepObjectMeshEuler()` | `customReferenceToKeepObjectMeshEuler`の値を返すだけ。 |
| `checkDisableTrail()` | `useTrailOnThrowReturn`が有効なら軌跡を無効化するだけ。 |
| `setTrailActiveState(bool state)` | 軌跡用コルーチンを止め、trueなら有効化して`time`を1に、falseなら即無効かフェードコルーチンを開始する。 |
| `setPreviousStrafeModeState(bool state)` | `previousStrafeMode`を`state`に設定するだけ。 |
| `wasStrafeModeActivePreviously()` | `previousStrafeMode`の値を返すだけ。 |
| `getGrabPhysicalObjectMeleeAttackSystem()` | `mainGrabPhysicalObjectSystem`の参照を返すだけ。 |
| `renameWeapon(string newWeaponName)` | `weaponName`を`newWeaponName`に書き換えるだけ。 |
| `enableOrDisableRemoteEventsOnSurfacesDetected(bool state)` | `useRemoteEventOnSurfacesDetected`を`state`に設定するだけ。 |
| `enableOrDisableRemoteEventsOnSurfacesDetectedElement(bool state, string remoteEventName)` | 接触時リモートイベントのリストから同名要素を探し、`remoteEventActive`を`state`にする。 |
| `enableRemoteEventsOnSurfacesDetectedElement(string remoteEventName)` | `remoteEventName`の接触時リモートイベントを有効にするだけ。 |
| `disableRemoteEventsOnSurfacesDetectedElement(string remoteEventName)` | `remoteEventName`の接触時リモートイベントを無効にするだけ。 |
| `isRemoteEventIncluded(string remoteEventName)` | 有効かつ同名の`remoteEventName`がリストにあるかを返す。 |
| `enableOrDisableRemoteEventsOnAttackList(bool state)` | `attackInfoList`の全要素の`useRemoteEvent`を`state`に揃えるだけ。 |
| `setSecondaryAbilityActiveState(bool state)` | `secondaryAbilityActive`を`state`に設定するだけ。 |
| `isSecondaryAbilityActive()` | `secondaryAbilityActive`の値を返すだけ。 |
| `setNewGeneralDamageTypeID(int newValue)` | `generalDamageTypeID`を`newValue`に設定するだけ。 |
| `setDamageTypeAndReactionInfo(string newBuffObjectName)` | `newBuffObjectName`の属性を有効化して他を解除し、ID設定・イベント・持続処理を行って成否を返す。 |
| `activateReturnProjectilesOnContact()` | 弾反射が有効なら`mainGrabPhysicalObjectSystem`の同名メソッドを呼ぶだけ。 |
| `sendReturnProjectilesOnContactInfo(Transform playerTransform, Transform mainCameraTransform)` | 弾反射有効時、防御面の所有者を`playerTransform`にし、カメラ方向へストック弾を発射する。 |
| `setNewArmorOwner(Transform playerTransform)` | 弾反射が有効で`mainArmoreSurfaceSystem`があれば、その所有者を`playerTransform`に変更する。 |
| `enableOrDisableWeaponMeshActiveState(bool state)` | `weaponMesh`のアクティブ状態を`state`に切り替えるだけ。 |
| `setNextExtraActionOnMeleeWeapon(remoteEventSystem currentRemoteEventSystem)` | 有効な追加アクションを循環探索し、見つかったインデックスで`setNewExtraActionByIndex`を呼ぶ。 |
| `setNewExtraActionByIndex(int newIndex, remoteEventSystem currentRemoteEventSystem)` | 現在の追加アクションを解除し、`newIndex`のものを有効化して対応するリモートイベントを送る。 |
| `getActionIconTexture()` | 追加アクション有効かつアイコン使用時は`actionIcon`を返し、それ以外はnullを返す。 |
| `getCurrentExtraActionIndex()` | `currentExtraActionIndex`の値を返すだけ。 |
| `activateCurrentExtraActionOnMeleeWeapon(remoteEventSystem currentRemoteEventSystem)` | `currentRemoteEventSystem`で現在の追加アクションの起動イベントを送り、設定時はイベントも発火する。 |
| `checkIfCarryingMeleeWeaponToActivateAction()` | 追加アクション有効時、現在アクションの`checkIfCarryingMeleeWeaponToActivateAction`値を返す。 |
| `enableExtraActionByName(string actionName)` | `actionName`に一致する追加アクションを有効化するだけ。 |
| `disableExtraActionByName(string actionName)` | `actionName`に一致する追加アクションを無効化するだけ。 |
| `enableOrDisableExtraActionByName(string actionName, bool state)` | `actionName`に一致する追加アクションの`actionEnabled`を`state`にする。 |
| `checkDurabilityOnAttack(float extraMultiplier)` | 攻撃時耐久が有効なら`extraMultiplier`倍で耐久を減らし、0以下でtrueを返す。 |
| `checkDurabilityOnBlock(float extraMultiplier)` | 防御時耐久が有効なら`extraMultiplier`倍で耐久を減らし、0以下でtrueを返す。 |
| `updateDurabilityAmountState()` | 攻撃か防御で耐久を使う設定なら`mainDurabilityInfo`の耐久表示を更新する。 |
| `getDurabilityAmount()` | 耐久使用時は`mainDurabilityInfo`の耐久値を返し、未使用時は-1を返す。 |
| `initializeDurabilityValue(float newAmount, int currentObjectIndex)` | 耐久使用時、初期耐久値とインベントリ番号を`mainDurabilityInfo`に設定する。 |
| `setInventoryObjectIndex(int currentObjectIndex)` | 耐久使用時、`mainDurabilityInfo`にインベントリ番号を設定するだけ。 |
| `repairObjectFully()` | 耐久使用時、`mainDurabilityInfo`で武器を完全に修復する。 |
| `breakFullDurabilityOnCurrentWeapon()` | 耐久使用時、`mainDurabilityInfo`で現在の武器の耐久を0まで破壊する。 |
| `setObjectNameFromEditor(string newName)` | 耐久使用時、`mainDurabilityInfo`のオブジェクト名を`newName`に変更する。 |
| `setDurabilityAmountFromEditor(float newValue)` | 耐久使用時、`mainDurabilityInfo`の現在耐久値を`newValue`に変更する。 |
| `setMaxDurabilityAmountFromEditor(float newValue)` | 耐久使用時、`mainDurabilityInfo`の最大耐久値を`newValue`に変更する。 |
| `addObjectStatsToMainManager()` | `useObjectStatsSystemEnabled`有効時、`mainObjectStatsSystem`へ登録を依頼する。 |
| `setCurrentCharacter(GameObject newObject)` | `currentCharacter`を`newObject`に設定するだけ。 |
| `getCurrentCharacter()` | `currentCharacter`の参照を返すだけ。 |
| `isWeaponCarriedByCharacter()` | `currentCharacter`がnullでないか、つまり武器が所持されているかを返す。 |
| `getLastTimeWeaponDropped()` | `lastTimeWeaponDropped`の値を返すだけ。 |
| `setLastTimeWeaponDropped()` | 現在の`Time.time`を`lastTimeWeaponDropped`に記録するだけ。 |
| `setUseObjectDurabilityOnAttackValue(bool newValue)` | `useObjectDurabilityOnAttack`を`newValue`に設定するだけ。 |
| `setDurabilityUsedOnAttackValue(float newValue)` | `durabilityUsedOnAttack`を`newValue`に設定するだけ。 |
| `setUseObjectDurabilityOnBlockValue(bool newValue)` | `useObjectDurabilityOnBlock`を`newValue`に設定するだけ。 |
| `setDurabilityUsedOnBlockValue(float newValue)` | `durabilityUsedOnBlock`を`newValue`に設定するだけ。 |
| `setReferencePositionToKeepObjectMeshPositionFromEditor(Vector3 newPosition, Quaternion newRotation)` | `referencePositionToKeepObjectMesh`のローカル位置と回転を設定し、エディタを更新する。 |
| `setUseObjectDurabilityOnAttackValueFromEditor(bool newValue)` | 攻撃時耐久の使用可否を設定し、`updateComponent`でエディタ表示を更新する。 |
| `setDurabilityUsedOnAttackValueFromEditor(float newValue)` | 攻撃時における耐久減少量を設定し、`updateComponent`でエディタ表示を更新する。 |
| `setUseObjectDurabilityOnBlockValueFromEditor(bool newValue)` | 防御時耐久の使用可否を設定し、`updateComponent`でエディタ表示を更新する。 |
| `setDurabilityUsedOnBlockValueFromEditor(float newValue)` | 防御時における耐久減少量を設定し、`updateComponent`でエディタ表示を更新する。 |
| `copyWeaponInfoToTemplate(bool settingInfoOnEditorTime)` | `mainMeleeWeaponAttackInfoTemplate`があれば武器名と`attackInfoList`を複製し、エディタ時は更新する。 |
| `copyTemplateToWeaponAttackInfo(bool settingInfoOnEditorTime)` | テンプレートの`mainAttackInfoList`を`attackInfoList`へ複製し、エディタ時設定なら更新する。 |
| `setNewMeleeWeaponAttackInfoTemplate(meleeWeaponAttackInfo newMeleeWeaponAttackInfo, bool settingInfoOnEditorTime)` | `mainMeleeWeaponAttackInfoTemplate`を`newMeleeWeaponAttackInfo`に差し替え、エディタ時は更新する。 |
| `updateMeleeAttackInfo(int attackListIndex, float attackDamage, string attackType, string actionSystemAnimationName, float actionSystemDuration, float actionSystemSpeed, List<damageTriggerActiveInfo> damageTriggerActiveInfoList)` | `attackListIndex`の攻撃にダメージ・種別・アニメ・時間・速度・トリガーを設定して更新する。 |
| `renameWeaponFromEditor(string newWeaponName)` | 武器名を変更し、`GKC_Utils.renameAsset`でアセット名も変えてからコンポーネントを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnThrowStart` | `UnityEvent` | – |
| `eventOnThrowEnd` | `UnityEvent` | – |
| `eventOnReturnStart` | `UnityEvent` | – |
| `eventOnReturnEnd` | `UnityEvent` | – |
| `eventsOnKeepMeleeWeapon` | `UnityEvent` | – |
| `eventsOnDrawMeleeWeapon` | `UnityEvent` | – |
| `eventOnAttackStart` | `UnityEvent` | – |
| `eventOnAttackEnd` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`getWeaponName()`, `isMeleeWeapon()`

</details>

## 内部型

- `attackInfo`（class）
- `damageTriggerActiveInfo`（class）
- `damageTypeAndReactionInfo`（class）
- `remoteEventOnSurfaceDetectedInfo`（class）
- `extraActionMeleeWeaponInfo`（class）
