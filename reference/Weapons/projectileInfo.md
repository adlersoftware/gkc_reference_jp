# projectileInfo

- **種別**: class
- **ソース**: `Weapons/Projectiles/projectileInfo.cs:6`
- **属性**: `System.Serializable`

**概要**: 投射物の速度・ダメージ・音・切断設定などを保持する情報クラスで、コピー用コンストラクタも持つ。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Is Homming Projectile | `isHommingProjectile` | `bool` | – | – |
| Is Seeker | `isSeeker` | `bool` | – | – |
| Target On Screen For Seeker | `targetOnScreenForSeeker` | `bool` | true | – |
| Wait Time To Search Target | `waitTimeToSearchTarget` | `float` | – | – |
| Use Raycast Checking On Rigidbody | `useRaycastCheckingOnRigidbody` | `bool` | – | – |
| Custom Raycast Checking Rate | `customRaycastCheckingRate` | `float` | – | – |
| Custom Raycast Checking Distance | `customRaycastCheckingDistance` | `float` | 0.1f | – |
| Use Ray Cast Shoot | `useRayCastShoot` | `bool` | – | – |
| Use Raycast Shoot Delay | `useRaycastShootDelay` | `bool` | – | – |
| Raycast Shoot Delay | `raycastShootDelay` | `float` | – | – |
| Get Delay With Distance | `getDelayWithDistance` | `bool` | – | – |
| Delay With Distance Speed | `delayWithDistanceSpeed` | `float` | – | – |
| Max Delay With Distance | `maxDelayWithDistance` | `float` | – | – |
| Use Fake Projectile Trails | `useFakeProjectileTrails` | `bool` | – | – |
| Ignore Use Trail Renderer | `ignoreUseTrailRenderer` | `bool` | – | – |
| Projectile Damage | `projectileDamage` | `float` | – | – |
| Projectile Speed | `projectileSpeed` | `float` | – | – |
| Impact Force Applied | `impactForceApplied` | `float` | – | – |
| Force Mode | `forceMode` | `ForceMode` | – | – |
| Apply Impact Force To Vehicles | `applyImpactForceToVehicles` | `bool` | – | – |
| Impact Force To Vehicles Multiplier | `impactForceToVehiclesMultiplier` | `float` | – | – |
| Check Objects With Multiple Damage Receivers Enabled | `checkObjectsWithMultipleDamageReceiversEnabled` | `bool` | true | – |
| Force Mass Multiplier | `forceMassMultiplier` | `float` | 1 | – |
| Projectile With Ability | `projectileWithAbility` | `bool` | – | – |
| Impact Sound Effect | `impactSoundEffect` | `AudioClip` | – | – |
| Impact Audio Element | `impactAudioElement` | `AudioElement` | – | – |
| Scorch | `scorch` | `GameObject` | – | – |
| Owner | `owner` | `GameObject` | – | – |
| Projectile Particles | `projectileParticles` | `GameObject` | – | – |
| Impact Particles | `impactParticles` | `GameObject` | – | – |
| Is Explosive | `isExplosive` | `bool` | – | – |
| Is Implosive | `isImplosive` | `bool` | – | – |
| Explosion Force | `explosionForce` | `float` | – | – |
| Explosion Radius | `explosionRadius` | `float` | – | – |
| Use Explosion Delay | `useExplosionDelay` | `bool` | – | – |
| Explosion Delay | `explosionDelay` | `float` | – | – |
| Explosion Damage | `explosionDamage` | `float` | – | – |
| Push Characters | `pushCharacters` | `bool` | – | – |
| Can Damage Projectile Owner | `canDamageProjectileOwner` | `bool` | – | – |
| Apply Explosion Force To Vehicles | `applyExplosionForceToVehicles` | `bool` | – | – |
| Explosion Force To Vehicles Multiplier | `explosionForceToVehiclesMultiplier` | `float` | – | – |
| Search Closest Weak Spot | `searchClosestWeakSpot` | `bool` | – | – |
| Kill In One Shot | `killInOneShot` | `bool` | – | – |
| Use Disable Timer | `useDisableTimer` | `bool` | – | – |
| No Impact Disable Timer | `noImpactDisableTimer` | `float` | – | – |
| Impact Disable Timer | `impactDisableTimer` | `float` | – | – |
| Use Custom Ignore Tags | `useCustomIgnoreTags` | `bool` | – | – |
| Custom Tags To Ignore List | `customTagsToIgnoreList` | `List<string>` | new List<string> () | – |
| Target To Damage Layer | `targetToDamageLayer` | `LayerMask` | – | – |
| Target For Scorch Layer | `targetForScorchLayer` | `LayerMask` | – | – |
| Scorch Ray Cast Distance | `scorchRayCastDistance` | `float` | – | – |
| Impact Decal Index | `impactDecalIndex` | `int` | – | – |
| Launch Projectile | `launchProjectile` | `bool` | – | – |
| Adhere To Surface | `adhereToSurface` | `bool` | – | – |
| Adhere To Limbs | `adhereToLimbs` | `bool` | – | – |
| Ignore Set Projectile Position On Impact | `ignoreSetProjectilePositionOnImpact` | `bool` | – | – |
| Use Gravity On Launch | `useGravityOnLaunch` | `bool` | – | – |
| Use Graivty On Impact | `useGraivtyOnImpact` | `bool` | – | – |
| Break Through Objects | `breakThroughObjects` | `bool` | – | – |
| Can Break Through Armor Surface | `canBreakThroughArmorSurface` | `bool` | – | – |
| Break Through Armor Surface Priority Value | `breakThroughArmorSurfacePriorityValue` | `int` | -1 | – |
| Infinite Number Of Impacts | `infiniteNumberOfImpacts` | `bool` | – | – |
| Number Of Impacts | `numberOfImpacts` | `int` | – | – |
| Can Damage Same Object Multiple Times | `canDamageSameObjectMultipleTimes` | `bool` | – | – |
| Forward Direction | `forwardDirection` | `Vector3` | – | – |
| Ignore New Rotation On Projectile Impact | `ignoreNewRotationOnProjectileImpact` | `bool` | – | – |
| Stop Break Through Objects On Layer | `stopBreakThroughObjectsOnLayer` | `bool` | – | – |
| Layer To Stop Breaht Through Objects | `layerToStopBreahtThroughObjects` | `LayerMask` | – | – |
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
| Set Projectile Mesh Rotation To Fire Rotation | `setProjectileMeshRotationToFireRotation` | `bool` | – | – |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remote Event Name List | `remoteEventNameList` | `List<string>` | new List<string> () | – |
| Use Remote Event On Objects Found On Explosion | `useRemoteEventOnObjectsFoundOnExplosion` | `bool` | – | – |
| Remote Event Name On Explosion | `remoteEventNameOnExplosion` | `string` | – | – |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Can Activate Reaction System Temporally | `canActivateReactionSystemTemporally` | `bool` | – | – |
| Damage Reaction ID | `damageReactionID` | `int` | -1 | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |
| Projectiles Pool Enabled | `projectilesPoolEnabled` | `bool` | – | – |
| Max Amount Of Pool Elements On Weapon | `maxAmountOfPoolElementsOnWeapon` | `int` | – | – |
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

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `InitializeAudioElements()` | `impactSoundEffect`があれば`impactAudioElement.clip`に代入する。 |
