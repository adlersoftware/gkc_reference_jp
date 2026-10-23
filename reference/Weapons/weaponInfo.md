# weaponInfo

- **種別**: class
- **ソース**: `Weapons/weaponInfo.cs:8`
- **属性**: `System.Serializable`

**概要**: 武器1種の名前・モデル・弾薬・エフェクト・音・イベントなどを保持する中心的な情報クラス。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Name | `Name` | `string` | – | – |
| Number Key | `numberKey` | `int` | – | – |
| Use Ray Cast Shoot | `useRayCastShoot` | `bool` | – | – |
| Use Infinite Raycast Distance | `useInfiniteRaycastDistance` | `bool` | true | – |
| Max Raycast Distance | `maxRaycastDistance` | `float` | 200 | – |
| Check If Surfaces Close To Weapon | `checkIfSurfacesCloseToWeapon` | `bool` | – | – |
| Min Distance To Check | `minDistanceToCheck` | `float` | 2 | – |
| Use Raycast Shoot Delay | `useRaycastShootDelay` | `bool` | – | – |
| Raycast Shoot Delay | `raycastShootDelay` | `float` | – | – |
| Get Delay With Distance | `getDelayWithDistance` | `bool` | – | – |
| Delay With Distance Speed | `delayWithDistanceSpeed` | `float` | – | – |
| Max Delay With Distance | `maxDelayWithDistance` | `float` | – | – |
| Use Fake Projectile Trails | `useFakeProjectileTrails` | `bool` | – | – |
| Ignore Use Trail Renderer | `ignoreUseTrailRenderer` | `bool` | – | – |
| Fire Weapon Forward | `fireWeaponForward` | `bool` | – | – |
| Use Raycast Checking On Rigidbody | `useRaycastCheckingOnRigidbody` | `bool` | – | – |
| Custom Raycast Checking Rate | `customRaycastCheckingRate` | `float` | – | – |
| Custom Raycast Checking Distance | `customRaycastCheckingDistance` | `float` | 0.1f | – |
| Weapon Uses Ammo | `weaponUsesAmmo` | `bool` | true | – |
| Ammo Per Clip | `ammoPerClip` | `int` | – | – |
| Remove Previous Ammo On Clip | `removePreviousAmmoOnClip` | `bool` | – | – |
| Infinite Ammo | `infiniteAmmo` | `bool` | – | – |
| Use Remain Ammo From Inventory | `useRemainAmmoFromInventory` | `bool` | – | – |
| Remain Ammo | `remainAmmo` | `int` | – | – |
| Clip Size | `clipSize` | `int` | – | – |
| Start With Empty Clip | `startWithEmptyClip` | `bool` | – | – |
| Use Ammo Limit | `useAmmoLimit` | `bool` | – | – |
| Ammo Limit | `ammoLimit` | `int` | – | – |
| Aux Remain Ammo | `auxRemainAmmo` | `int` | – | – |
| Ammo Name | `ammoName` | `string` | – | – |
| Ignore Any Wait Time On Reload | `ignoreAnyWaitTimeOnReload` | `bool` | – | – |
| Shoot A Projectile | `shootAProjectile` | `bool` | – | – |
| Launch Projectile | `launchProjectile` | `bool` | – | – |
| Projectile With Ability | `projectileWithAbility` | `bool` | – | – |
| Weapon With Ability | `weaponWithAbility` | `bool` | – | – |
| Set Projectile Mesh Rotation To Fire Rotation | `setProjectileMeshRotationToFireRotation` | `bool` | – | – |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Can Activate Reaction System Temporally | `canActivateReactionSystemTemporally` | `bool` | – | – |
| Damage Reaction ID | `damageReactionID` | `int` | -1 | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |
| Automatic | `automatic` | `bool` | – | – |
| Use Burst | `useBurst` | `bool` | – | – |
| Burst Amount | `burstAmount` | `int` | – | – |
| Fire Rate | `fireRate` | `float` | – | – |
| Projectile Damage | `projectileDamage` | `float` | – | – |
| Projectile Speed | `projectileSpeed` | `float` | – | – |
| Projectiles Per Shoot | `projectilesPerShoot` | `int` | – | – |
| Use Projectile Spread | `useProjectileSpread` | `bool` | – | – |
| Third Person Spread Amount Aiming | `thirdPersonSpreadAmountAiming` | `float` | – | – |
| Third Person Spread Amount No Aiming | `thirdPersonSpreadAmountNoAiming` | `float` | – | – |
| First Person Spread Amount Aiming | `firstPersonSpreadAmountAiming` | `float` | – | – |
| First Person Spread Amount No Aiming | `firstPersonSpreadAmountNoAiming` | `float` | – | – |
| Check Objects With Multiple Damage Receivers Enabled | `checkObjectsWithMultipleDamageReceiversEnabled` | `bool` | – | – |
| Is Implosive | `isImplosive` | `bool` | – | – |
| Is Explosive | `isExplosive` | `bool` | – | – |
| Explosion Force | `explosionForce` | `float` | – | – |
| Explosion Radius | `explosionRadius` | `float` | – | – |
| Use Explosion Delay | `useExplosionDelay` | `bool` | – | – |
| Explosion Delay | `explosionDelay` | `float` | – | – |
| Explosion Damage | `explosionDamage` | `float` | – | – |
| Push Characters | `pushCharacters` | `bool` | – | – |
| Can Damage Projectile Owner | `canDamageProjectileOwner` | `bool` | true | – |
| Apply Explosion Force To Vehicles | `applyExplosionForceToVehicles` | `bool` | true | – |
| Explosion Force To Vehicles Multiplier | `explosionForceToVehiclesMultiplier` | `float` | 0.2f | – |
| Search Closest Weak Spot | `searchClosestWeakSpot` | `bool` | – | – |
| Projectile Position | `projectilePosition` | `List<Transform>` | new List<Transform> () | – |
| Check Crossing Surfaces On Camera Direction | `checkCrossingSurfacesOnCameraDirection` | `bool` | true | – |
| Apply Force At Shoot | `applyForceAtShoot` | `bool` | – | – |
| Force Direction | `forceDirection` | `Vector3` | – | – |
| Force Amount | `forceAmount` | `float` | – | – |
| Is Homming Projectile | `isHommingProjectile` | `bool` | – | – |
| Is Seeker | `isSeeker` | `bool` | – | – |
| Target On Screen For Seeker | `targetOnScreenForSeeker` | `bool` | true | – |
| Wait Time To Search Target | `waitTimeToSearchTarget` | `float` | – | – |
| Impact Force Applied | `impactForceApplied` | `float` | – | – |
| Force Mode | `forceMode` | `ForceMode` | – | – |
| Apply Impact Force To Vehicles | `applyImpactForceToVehicles` | `bool` | – | – |
| Impact Force To Vehicles Multiplier | `impactForceToVehiclesMultiplier` | `float` | 1 | – |
| Force Mass Multiplier | `forceMassMultiplier` | `float` | 1 | – |
| Kill In One Shot | `killInOneShot` | `bool` | – | – |
| Use Disable Timer | `useDisableTimer` | `bool` | – | – |
| No Impact Disable Timer | `noImpactDisableTimer` | `float` | – | – |
| Impact Disable Timer | `impactDisableTimer` | `float` | – | – |
| Located Enemy Icon Name | `locatedEnemyIconName` | `string` | "Homing Located Enemy" | – |
| Tag To Locate | `tagToLocate` | `List<string>` | new List<string> () | – |
| Activate Launch Parable Third Person | `activateLaunchParableThirdPerson` | `bool` | – | – |
| Activate Launch Parable First Person | `activateLaunchParableFirstPerson` | `bool` | – | – |
| Use Parable Speed | `useParableSpeed` | `bool` | – | – |
| Parable Direction Transform | `parableDirectionTransform` | `Transform` | – | – |
| Use Max Distance When No Surface Found | `useMaxDistanceWhenNoSurfaceFound` | `bool` | – | – |
| Max Distance When No Surface Found | `maxDistanceWhenNoSurfaceFound` | `float` | – | – |
| Check Gravity System On Projectile | `checkGravitySystemOnProjectile` | `bool` | true | – |
| Check Circumnavigation Values On Projectile | `checkCircumnavigationValuesOnProjectile` | `bool` | – | – |
| Gravity Force For Circumnavigation On Projectile | `gravityForceForCircumnavigationOnProjectile` | `float` | 9.8f | – |
| Adhere To Surface | `adhereToSurface` | `bool` | – | – |
| Adhere To Limbs | `adhereToLimbs` | `bool` | – | – |
| Ignore Set Projectile Position On Impact | `ignoreSetProjectilePositionOnImpact` | `bool` | – | – |
| Use Gravity On Launch | `useGravityOnLaunch` | `bool` | – | – |
| Use Graivty On Impact | `useGraivtyOnImpact` | `bool` | – | – |
| Break Through Objects | `breakThroughObjects` | `bool` | – | – |
| Infinite Number Of Impacts | `infiniteNumberOfImpacts` | `bool` | – | – |
| Number Of Impacts | `numberOfImpacts` | `int` | – | – |
| Can Damage Same Object Multiple Times | `canDamageSameObjectMultipleTimes` | `bool` | – | – |
| Stop Break Through Objects On Layer | `stopBreakThroughObjectsOnLayer` | `bool` | – | – |
| Layer To Stop Breaht Through Objects | `layerToStopBreahtThroughObjects` | `LayerMask` | – | – |
| Ignore New Rotation On Projectile Impact | `ignoreNewRotationOnProjectileImpact` | `bool` | – | – |
| Can Break Through Armor Surface | `canBreakThroughArmorSurface` | `bool` | – | – |
| Break Through Armor Surface Priority Value | `breakThroughArmorSurfacePriorityValue` | `int` | -1 | – |
| Damage Target Over Time | `damageTargetOverTime` | `bool` | – | – |
| Damage Over Time Delay | `damageOverTimeDelay` | `float` | – | – |
| Damage Over Time Duration | `damageOverTimeDuration` | `float` | – | – |
| Damage Over Time Amount | `damageOverTimeAmount` | `float` | – | – |
| Damage Over Time Rate | `damageOverTimeRate` | `float` | – | – |
| Damage Over Time To Death | `damageOverTimeToDeath` | `bool` | – | – |
| Remove Damage Over Time State | `removeDamageOverTimeState` | `bool` | – | – |
| Sedate Characters | `sedateCharacters` | `bool` | – | – |
| Sedate Delay | `sedateDelay` | `float` | – | – |
| Use Weak Spot To Reduce Delay | `useWeakSpotToReduceDelay` | `bool` | – | – |
| Sedate Until Receive Damage | `sedateUntilReceiveDamage` | `bool` | – | – |
| Sedate Duration | `sedateDuration` | `float` | – | – |
| Push Character | `pushCharacter` | `bool` | – | – |
| Push Character Force | `pushCharacterForce` | `float` | – | – |
| Push Character Ragdoll Force | `pushCharacterRagdollForce` | `float` | – | – |
| Use Noise | `useNoise` | `bool` | – | – |
| Noise Radius | `noiseRadius` | `float` | – | – |
| Noise Expand Speed | `noiseExpandSpeed` | `float` | – | – |
| Use Noise Detection | `useNoiseDetection` | `bool` | – | – |
| Noise Detection Layer | `noiseDetectionLayer` | `LayerMask` | – | – |
| Show Noise Detection Gizmo | `showNoiseDetectionGizmo` | `bool` | – | – |
| Noise ID | `noiseID` | `int` | -1 | – |
| Use Noise Mesh | `useNoiseMesh` | `bool` | true | – |
| Noise Decibels | `noiseDecibels` | `float` | 1 | Range (0, 2) |
| Force Noise Detection | `forceNoiseDetection` | `bool` | – | – |
| Auto Shoot On Tag | `autoShootOnTag` | `bool` | – | – |
| Layer To Auto Shoot | `layerToAutoShoot` | `LayerMask` | – | – |
| Auto Shoot Tag List | `autoShootTagList` | `List<string>` | new List<string> () | – |
| Max Distance To Raycast | `maxDistanceToRaycast` | `float` | – | – |
| Shoot At Layer Too | `shootAtLayerToo` | `bool` | – | – |
| Avoid Shoot At Tag | `avoidShootAtTag` | `bool` | – | – |
| Layert To Avoid Shoot | `layertToAvoidShoot` | `LayerMask` | – | – |
| Avoid Shoot Tag List | `avoidShootTagList` | `List<string>` | new List<string> () | – |
| Avoid Shoot Max Distance To Raycast | `avoidShootMaxDistanceToRaycast` | `float` | – | – |
| Avoid Shoot At Layer Too | `avoidShootAtLayerToo` | `bool` | – | – |
| Use Lower Position On Avoid Shoot | `useLowerPositionOnAvoidShoot` | `bool` | – | – |
| Weapon Mesh | `weaponMesh` | `GameObject` | – | – |
| Weapon Parent | `weaponParent` | `Transform` | – | – |
| Use Fire Animation | `useFireAnimation` | `bool` | true | – |
| Animation | `animation` | `string` | – | – |
| Animation Speed | `animationSpeed` | `float` | 1 | – |
| Use Reload Animation | `useReloadAnimation` | `bool` | – | – |
| Use Reload On Third Person | `useReloadOnThirdPerson` | `bool` | true | – |
| Use Reload On First Person | `useReloadOnFirstPerson` | `bool` | true | – |
| Reload Animation Name | `reloadAnimationName` | `string` | – | – |
| Reload Animation Speed | `reloadAnimationSpeed` | `float` | – | – |
| Play Animation Backward | `playAnimationBackward` | `bool` | true | – |
| Drop Clip When Reload | `dropClipWhenReload` | `bool` | – | – |
| Drop Clip When Reload First Person | `dropClipWhenReloadFirstPerson` | `bool` | true | – |
| Drop Clip When Reload Third Person | `dropClipWhenReloadThirdPerson` | `bool` | true | – |
| Position To Drop Clip | `positionToDropClip` | `Transform` | – | – |
| Clip Model | `clipModel` | `GameObject` | – | – |
| Auto Reload When Clip Empty | `autoReloadWhenClipEmpty` | `bool` | true | – |
| Delay Drop Clip When Reload Third Person | `delayDropClipWhenReloadThirdPerson` | `float` | – | – |
| Delay Drop Clip When Reload First Person | `delayDropClipWhenReloadFirstPerson` | `float` | – | – |
| Magazine In Hand Transform | `magazineInHandTransform` | `Transform` | – | – |
| Magazine In Hand Game Object | `magazineInHandGameObject` | `GameObject` | – | – |
| Scorch | `scorch` | `GameObject` | – | – |
| Scorch Ray Cast Distance | `scorchRayCastDistance` | `float` | – | – |
| Reload Time Third Person | `reloadTimeThirdPerson` | `float` | 1 | – |
| Reload Time First Person | `reloadTimeFirstPerson` | `float` | 1 | – |
| Use Reload Delay Third Person | `useReloadDelayThirdPerson` | `bool` | – | – |
| Reload Delay Third Person | `reloadDelayThirdPerson` | `float` | – | – |
| Use Reload Delay First Person | `useReloadDelayFirstPerson` | `bool` | – | – |
| Reload Delay First Person | `reloadDelayFirstPerson` | `float` | – | – |
| Use Pre Reload Delay Third Person | `usePreReloadDelayThirdPerson` | `bool` | – | – |
| Pre Reload Delay Third Person | `preReloadDelayThirdPerson` | `float` | – | – |
| Use Pre Reload Delay First Person | `usePreReloadDelayFirstPerson` | `bool` | – | – |
| Pre Reload Delay First Person | `preReloadDelayFirstPerson` | `float` | – | – |
| Shake Upper Body While Shooting | `shakeUpperBodyWhileShooting` | `bool` | – | – |
| Shake Amount | `shakeAmount` | `float` | – | – |
| Shake Speed | `shakeSpeed` | `float` | – | – |
| Shake Upper Body Shooting Dual Weapons | `shakeUpperBodyShootingDualWeapons` | `bool` | – | – |
| Dual Weapon Shake Amount | `dualWeaponShakeAmount` | `float` | – | – |
| Dual Weapon Shake Speed | `dualWeaponShakeSpeed` | `float` | – | – |
| Use Shell On Weapon Shoot Enabled | `useShellOnWeaponShootEnabled` | `bool` | true | – |
| Shell | `shell` | `GameObject` | – | – |
| Shell Position | `shellPosition` | `List<Transform>` | new List<Transform> () | – |
| Shell Ejection Force | `shellEjectionForce` | `float` | 100 | – |
| Shell Drop Sound List | `shellDropSoundList` | `List<AudioClip>` | new List<AudioClip> () | – |
| Shell Drop Audio Elements | `shellDropAudioElements` | `List<AudioElement>` | new List<AudioElement> () | – |
| Use Shell Delay | `useShellDelay` | `bool` | – | – |
| Shell Delay Third Person | `shellDelayThirdPerson` | `float` | – | – |
| Shell Delay Firs Person | `shellDelayFirsPerson` | `float` | – | – |
| Create Shells On Reload | `createShellsOnReload` | `bool` | – | – |
| Check To Create Shells If No Remain Ammo | `checkToCreateShellsIfNoRemainAmmo` | `bool` | – | – |
| Remove Dropped Shells After Time | `removeDroppedShellsAfterTime` | `bool` | true | – |
| Create Shells On Reload Delay Third Person | `createShellsOnReloadDelayThirdPerson` | `float` | – | – |
| Create Shells On Reload Delay First Person | `createShellsOnReloadDelayFirstPerson` | `float` | – | – |
| Max Amount Of Shells Before Remove Them | `maxAmountOfShellsBeforeRemoveThem` | `int` | 15 | – |
| Use Sound On Draw Keep Weapon | `useSoundOnDrawKeepWeapon` | `bool` | – | – |
| Draw Weapon Sound | `drawWeaponSound` | `AudioClip` | – | – |
| Draw Weapon Audio Element | `drawWeaponAudioElement` | `AudioElement` | – | – |
| Keep Weapon Sound | `keepWeaponSound` | `AudioClip` | – | – |
| Keep Weapon Audio Element | `keepWeaponAudioElement` | `AudioElement` | – | – |
| Use Muzzle Flash | `useMuzzleFlash` | `bool` | – | – |
| Muzzle Flahs Light | `muzzleFlahsLight` | `Light` | – | – |
| Muzzle Flahs Duration | `muzzleFlahsDuration` | `float` | – | – |
| Reload Sound Effect | `reloadSoundEffect` | `AudioClip` | – | – |
| Reload Audio Element | `reloadAudioElement` | `AudioElement` | – | – |
| Cock Sound | `cockSound` | `AudioClip` | – | – |
| Cock Sound Audio Element | `cockSoundAudioElement` | `AudioElement` | – | – |
| Shoot Sound Effect | `shootSoundEffect` | `AudioClip` | – | – |
| Use Random Shoot Sound | `useRandomShootSound` | `bool` | – | – |
| Random Shoot Sound List | `randomShootSoundList` | `AudioClip []` | – | – |
| Shoot Audio Element | `shootAudioElement` | `AudioElement` | – | – |
| Impact Sound Effect | `impactSoundEffect` | `AudioClip` | – | – |
| Impact Audio Element | `impactAudioElement` | `AudioElement` | – | – |
| Silencer Shoot Effect | `silencerShootEffect` | `AudioClip` | – | – |
| Silencer Shoot Audio Element | `silencerShootAudioElement` | `AudioElement` | – | – |
| Use Sounds Pool | `useSoundsPool` | `bool` | – | – |
| Max Sounds Pool Amount | `maxSoundsPoolAmount` | `int` | – | – |
| Weapon Effect Source Prefab | `weaponEffectSourcePrefab` | `GameObject` | – | – |
| Weapon Effect Source Parent | `weaponEffectSourceParent` | `Transform` | – | – |
| Set Shoot Particles Layer On First Person | `setShootParticlesLayerOnFirstPerson` | `bool` | – | – |
| Shoot Particles | `shootParticles` | `GameObject` | – | – |
| Projectile Particles | `projectileParticles` | `GameObject` | – | – |
| Impact Particles | `impactParticles` | `GameObject` | – | – |
| Weapon Icon | `weaponIcon` | `Texture` | – | – |
| Weapon Inventory Slot Icon | `weaponInventorySlotIcon` | `Texture` | – | – |
| Weapon I Con HUD | `weaponIConHUD` | `Texture` | – | – |
| Show Weapon Name In HUD | `showWeaponNameInHUD` | `bool` | true | – |
| Show Weapon Icon In HUD | `showWeaponIconInHUD` | `bool` | true | – |
| Show Weapon Ammo Slider In HUD | `showWeaponAmmoSliderInHUD` | `bool` | true | – |
| Show Weapon Ammo Text In HUD | `showWeaponAmmoTextInHUD` | `bool` | true | – |
| Use Reticle Third Person | `useReticleThirdPerson` | `bool` | – | – |
| Use Aim Reticle Third Person | `useAimReticleThirdPerson` | `bool` | true | – |
| Use Reticle First Person | `useReticleFirstPerson` | `bool` | true | – |
| Use Aim Reticle First Person | `useAimReticleFirstPerson` | `bool` | true | – |
| Use Custom Reticle | `useCustomReticle` | `bool` | – | – |
| Regular Custom Reticle | `regularCustomReticle` | `Texture` | – | – |
| Use Aim Custom Reticle | `useAimCustomReticle` | `bool` | – | – |
| Aim Custom Reticle | `aimCustomReticle` | `Texture` | – | – |
| Use Dynamic Reticle | `useDynamicReticle` | `bool` | – | – |
| Dynamic Reticle Name | `dynamicReticleName` | `string` | – | – |
| Sniper Sight Third Person Enabled | `sniperSightThirdPersonEnabled` | `bool` | – | – |
| Sniper Sight First Person Enabled | `sniperSightFirstPersonEnabled` | `bool` | – | – |
| Use Canvas HUD | `useCanvasHUD` | `bool` | true | – |
| Clip Size Text | `clipSizeText` | `Text` | – | – |
| Remain Ammo Text | `remainAmmoText` | `Text` | – | – |
| HUD | `HUD` | `GameObject` | – | – |
| Ammo Info HUD | `ammoInfoHUD` | `GameObject` | – | – |
| Use HUD | `useHUD` | `bool` | – | – |
| Change HUD Position | `changeHUDPosition` | `bool` | – | – |
| Disable HUD In First Person Aim | `disableHUDInFirstPersonAim` | `bool` | – | – |
| HUD Transform In Third Person | `HUDTransformInThirdPerson` | `Transform` | – | – |
| HUD Transform In First Person | `HUDTransformInFirstPerson` | `Transform` | – | – |
| Use HUD On FBA | `useHUDOnFBA` | `bool` | – | – |
| Use HUD Dual Weapon Third Person | `useHUDDualWeaponThirdPerson` | `bool` | – | – |
| Use HUD Dual Weapon First Person | `useHUDDualWeaponFirstPerson` | `bool` | – | – |
| Change HUD Position Dual Weapon | `changeHUDPositionDualWeapon` | `bool` | – | – |
| HUD Right Hand Transform Third Person | `HUDRightHandTransformThirdPerson` | `Transform` | – | – |
| HUD Left Hand Transform Third Person | `HUDLeftHandTransformThirdPerson` | `Transform` | – | – |
| HUD Right Hand Transform First Person | `HUDRightHandTransformFirstPerson` | `Transform` | – | – |
| HUD Left Hand Transform First Person | `HUDLeftHandTransformFirstPerson` | `Transform` | – | – |
| Use Down Button | `useDownButton` | `bool` | – | – |
| Down Button Action | `downButtonAction` | `UnityEvent` | – | – |
| Use Hold Button | `useHoldButton` | `bool` | – | – |
| Hold Button Action | `holdButtonAction` | `UnityEvent` | – | – |
| Use Up Button | `useUpButton` | `bool` | – | – |
| Up Button Action | `upButtonAction` | `UnityEvent` | – | – |
| Ignore Up Button Action On FBA | `ignoreUpButtonActionOnFBA` | `bool` | – | – |
| Use Event On Fire Weapon | `useEventOnFireWeapon` | `bool` | – | – |
| Event On Fire Weapon | `eventOnFireWeapon` | `UnityEvent` | – | – |
| Use Event On Input Down | `useEventOnInputDown` | `bool` | – | – |
| Use Event On Input Up | `useEventOnInputUp` | `bool` | – | – |
| Event On Input Down | `eventOnInputDown` | `UnityEvent` | – | – |
| Event On Input Up | `eventOnInputUp` | `UnityEvent` | – | – |
| Use Start Draw Action | `useStartDrawAction` | `bool` | – | – |
| Start Draw Action | `startDrawAction` | `UnityEvent` | – | – |
| Use Stop Draw Action | `useStopDrawAction` | `bool` | – | – |
| Stop Draw Action | `stopDrawAction` | `UnityEvent` | – | – |
| Use Start Draw Action Third Person | `useStartDrawActionThirdPerson` | `bool` | – | – |
| Start Draw Action Third Person | `startDrawActionThirdPerson` | `UnityEvent` | – | – |
| Use Stop Draw Action Third Person | `useStopDrawActionThirdPerson` | `bool` | – | – |
| Stop Draw Action Third Person | `stopDrawActionThirdPerson` | `UnityEvent` | – | – |
| Use Start Draw Action First Person | `useStartDrawActionFirstPerson` | `bool` | – | – |
| Start Draw Action First Person | `startDrawActionFirstPerson` | `UnityEvent` | – | – |
| Use Stop Draw Action First Person | `useStopDrawActionFirstPerson` | `bool` | – | – |
| Stop Draw Action First Person | `stopDrawActionFirstPerson` | `UnityEvent` | – | – |
| Use Start Aim Action Third Person | `useStartAimActionThirdPerson` | `bool` | – | – |
| Start Aim Action Third Person | `startAimActionThirdPerson` | `UnityEvent` | – | – |
| Use Stop Aim Action Third Person | `useStopAimActionThirdPerson` | `bool` | – | – |
| Stop Aim Action Third Person | `stopAimActionThirdPerson` | `UnityEvent` | – | – |
| Use Start Aim Action First Person | `useStartAimActionFirstPerson` | `bool` | – | – |
| Start Aim Action First Person | `startAimActionFirstPerson` | `UnityEvent` | – | – |
| Use Stop Aim Action First Person | `useStopAimActionFirstPerson` | `bool` | – | – |
| Stop Aim Action First Person | `stopAimActionFirstPerson` | `UnityEvent` | – | – |
| Use Secondary Action | `useSecondaryAction` | `bool` | – | – |
| Secondary Action | `secondaryAction` | `UnityEvent` | – | – |
| Use Secondary Action On Down Press | `useSecondaryActionOnDownPress` | `bool` | – | – |
| Secondary Action On Down Press | `secondaryActionOnDownPress` | `UnityEvent` | – | – |
| Use Secondary Action On Up Press | `useSecondaryActionOnUpPress` | `bool` | – | – |
| Secondary Action On Up Press | `secondaryActionOnUpPress` | `UnityEvent` | – | – |
| Use Secondary Action On Hold Press | `useSecondaryActionOnHoldPress` | `bool` | – | – |
| Secondary Action On Hold Press | `secondaryActionOnHoldPress` | `UnityEvent` | – | – |
| Use Secondary Actions Only Aiming Third Person | `useSecondaryActionsOnlyAimingThirdPerson` | `bool` | – | – |
| Allow Use Secondary Action On FBA | `allowUseSecondaryActionOnFBA` | `bool` | – | – |
| Use Forward Action Event | `useForwardActionEvent` | `bool` | – | – |
| Forward Action Event | `forwardActionEvent` | `UnityEvent` | – | – |
| Use Backward Action Event | `useBackwardActionEvent` | `bool` | – | – |
| Backward Action Event | `backwardActionEvent` | `UnityEvent` | – | – |
| Use Reload Event | `useReloadEvent` | `bool` | – | – |
| Use Reload Event Third Person | `useReloadEventThirdPerson` | `bool` | – | – |
| Use Reload Event First Person | `useReloadEventFirstPerson` | `bool` | – | – |
| Reload Single Weapon Third Person Event | `reloadSingleWeaponThirdPersonEvent` | `UnityEvent` | – | – |
| Reload Dual Weapon Third Person Event | `reloadDualWeaponThirdPersonEvent` | `UnityEvent` | – | – |
| Reload Single Weapon First Person Event | `reloadSingleWeaponFirstPersonEvent` | `UnityEvent` | – | – |
| Reload Dual Weapon First Person Event | `reloadDualWeaponFirstPersonEvent` | `UnityEvent` | – | – |
| Use Third Person Event On Reload On FBA View | `useThirdPersonEventOnReloadOnFBAView` | `bool` | true | – |
| Use Event On Cancel Reload | `useEventOnCancelReload` | `bool` | – | – |
| Event On Cancel Reload | `eventOnCancelReload` | `UnityEvent` | – | – |
| Use Event On Weapon Activated | `useEventOnWeaponActivated` | `bool` | – | – |
| Event On Weapon Activated | `eventOnWeaponActivated` | `UnityEvent` | – | – |
| Use Event On Weapon Deactivated | `useEventOnWeaponDeactivated` | `bool` | – | – |
| Event On Weapon Deactivated | `eventOnWeaponDeactivated` | `UnityEvent` | – | – |
| Allow Damage For Projectile Owner | `allowDamageForProjectileOwner` | `bool` | – | – |
| Projectile Can Be Deflected | `projectileCanBeDeflected` | `bool` | true | – |
| Slice Objects Detected | `sliceObjectsDetected` | `bool` | – | – |
| Layer To Slice | `layerToSlice` | `LayerMask` | – | – |
| Use Body Parts Slice List | `useBodyPartsSliceList` | `bool` | – | – |
| Body Parts Slice List | `bodyPartsSliceList` | `List<string>` | new List<string> () | – |
| Max Distance To Body Part | `maxDistanceToBodyPart` | `float` | – | – |
| Random Slice Direction | `randomSliceDirection` | `bool` | – | – |
| Show Slice Gizmo | `showSliceGizmo` | `bool` | – | – |
| Activate Rigidbodies On New Objects | `activateRigidbodiesOnNewObjects` | `bool` | true | – |
| Use General Probability Slice Objects | `useGeneralProbabilitySliceObjects` | `bool` | – | – |
| General Probability Slice Objects | `generalProbabilitySliceObjects` | `float` | – | Range (0, 100) |
| Show Inpu Event Settings | `showInpuEventSettings` | `bool` | – | – |
| Show Ability Event Settings | `showAbilityEventSettings` | `bool` | – | – |
| Show Draw Aim Function Settings | `showDrawAimFunctionSettings` | `bool` | – | – |
| Show Reload Events Settings | `showReloadEventsSettings` | `bool` | – | – |
| Show Secondary Action Events Settings | `showSecondaryActionEventsSettings` | `bool` | – | – |
| Show Forward Backward Events Settings | `showForwardBackwardEventsSettings` | `bool` | – | – |
| Show Remote Events Settings | `showRemoteEventsSettings` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `InitializeAudioElements()` | 各サウンドが設定されていれば対応する`AudioElement`のclipへ複写し、薬莢音はリストへ追加する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `downButtonAction` | `UnityEvent` | – |
| `holdButtonAction` | `UnityEvent` | – |
| `upButtonAction` | `UnityEvent` | – |
| `eventOnFireWeapon` | `UnityEvent` | – |
| `eventOnInputDown` | `UnityEvent` | – |
| `eventOnInputUp` | `UnityEvent` | – |
| `startDrawAction` | `UnityEvent` | – |
| `stopDrawAction` | `UnityEvent` | – |
| `startDrawActionThirdPerson` | `UnityEvent` | – |
| `stopDrawActionThirdPerson` | `UnityEvent` | – |
| `startDrawActionFirstPerson` | `UnityEvent` | – |
| `stopDrawActionFirstPerson` | `UnityEvent` | – |
| `startAimActionThirdPerson` | `UnityEvent` | – |
| `stopAimActionThirdPerson` | `UnityEvent` | – |
| `startAimActionFirstPerson` | `UnityEvent` | – |
| `stopAimActionFirstPerson` | `UnityEvent` | – |
| `secondaryAction` | `UnityEvent` | – |
| `secondaryActionOnDownPress` | `UnityEvent` | – |
| `secondaryActionOnUpPress` | `UnityEvent` | – |
| `secondaryActionOnHoldPress` | `UnityEvent` | – |
| `forwardActionEvent` | `UnityEvent` | – |
| `backwardActionEvent` | `UnityEvent` | – |
| `reloadSingleWeaponThirdPersonEvent` | `UnityEvent` | – |
| `reloadDualWeaponThirdPersonEvent` | `UnityEvent` | – |
| `reloadSingleWeaponFirstPersonEvent` | `UnityEvent` | – |
| `reloadDualWeaponFirstPersonEvent` | `UnityEvent` | – |
| `eventOnCancelReload` | `UnityEvent` | – |
| `eventOnWeaponActivated` | `UnityEvent` | – |
| `eventOnWeaponDeactivated` | `UnityEvent` | – |
