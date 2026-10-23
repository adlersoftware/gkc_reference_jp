# applyDamage

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/applyDamage.cs:5`

**公式ドキュメント抜粋**（[Emerald AI](../../docs/integrations/current-integrations/emerald-ai.md)）

> This page covers the integration of Emerald AI and Game Kit Controller. Emerald AI allows developers to quickly create engaging dynamic AI with 100's of AAA quality features, all without having to write a single line of code! Emerald's editor is designed to make creating AI easy, yet incredibly customizable.\ \ Emerald caters to all kinds of developers and offers everything users would expect from an all-in-one AI system. You can find more information about Emerald AI, and its documentation and also purchase it over on the Unity Asset Store. Black Horizon Studios (The maker of Emerald AI) has a tutorial video showing the inspector changes needed to integration Emerald AI and Game Kit Controller. If you'd rather just get a step by step instructions for the inspector changes you can view these in the tab below labelled "Step by Step Instructions". While the video also covers the code chang…

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static void checkHealth(GameObject projectile, GameObject objectToDamage, float damageAmount, Vector3 direction, Vector3 position, GameObject projectileOwner, bool damageConstant, bool searchClosestWeakSpot, bool ignoreShield, bool ignoreDamageInScreen, bool damageCanBeBlocked, bool canActivateReactionSystemTemporally, int damageReactionID, int damageTypeID)` | – |
| `static bool checkCanBeDamaged(GameObject projectile, GameObject objectToDamage, float damageAmount, Vector3 direction, Vector3 position, GameObject projectileOwner, bool damageConstant, bool searchClosestWeakSpot, bool ignoreShield, bool ignoreDamageInScreen, bool damageCanBeBlocked, bool canActivateReactionSystemTemporally, int damageReactionID, int damageTypeID)` | – |
| `static void checkToDamageGKCCharacterExternally(float damageAmount, GameObject characterToDamage, GameObject attacker)` | – |
| `static bool checkIfDead(GameObject objectToCheck)` | – |
| `static bool checkIfDeadOnObjectChilds(GameObject objectToCheck)` | – |
| `static bool checkIfMaxHealth(GameObject objectToCheck)` | – |
| `static void setDamageTargetOverTimeState(GameObject objectToDamage, float damageOverTimeDelay, float damageOverTimeDuration, float damageOverTimeAmount, float damageOverTimeRate, bool damageOverTimeToDeath, int damageTypeID)` | – |
| `static void removeDamagetTargetOverTimeState(GameObject objectToDamage)` | – |
| `static void setDamageOrHealthTargetWithDelay(GameObject objectToDamage, float waitAmount, float valueAmount, int damageTypeID)` | – |
| `static void sedateCharacter(GameObject objectToDamage, Vector3 position, float sedateDelay, bool useWeakSpotToReduceDelay, bool sedateUntilReceiveDamage, float sedateDuration)` | – |
| `static void setHeal(float healAmount, GameObject objectToHeal)` | – |
| `static void setEnergy(float energyAmount, GameObject objectToRecharge)` | – |
| `static void removeEnergy(float energyAmount, GameObject objectToRecharge)` | – |
| `static void setFuel(float fuelAmount, GameObject vehicle)` | – |
| `static void removeFuel(float fuelAmount, GameObject vehicle)` | – |
| `static void setShield(float shieldAmount, GameObject objectToAddAmount)` | – |
| `static void setStamina(float staminaAmount, GameObject objectToAddAmount, bool refillFullStamina)` | – |
| `static void setOxygen(float oxygenAmount, GameObject objectToAddAmount)` | – |
| `static void setMoney(float moneyAmount, GameObject objectToAddAmount, bool useMoneyRandomRange, Vector2 moneyRandomRange)` | – |
| `static void setExperience(float experienceAmount, GameObject objectToAddAmount, Transform objectTransform, bool useExperienceRandomRange, Vector2 experienceRandomRange)` | – |
| `static void setExperienceMultiplier(float experienceMultiplierAmount, GameObject objectToAddAmount, float experienceMultiplierDuration)` | – |
| `static void setSkillPoints(float skillPointsAmount, GameObject objectToAddAmount)` | – |
| `static void increaseInventoryBagWeight(float weightToIncrease, GameObject objectToAddAmount)` | – |
| `static void increaseStrengthAmountAndUpdateStat(float strengthToIncrease, GameObject objectToAddAmount)` | – |
| `static bool canApplyForce(GameObject objectToCheck)` | – |
| `static bool isRagdollActive(GameObject objectToCheck)` | – |
| `static Rigidbody applyForce(GameObject objectToCheck)` | – |
| `static float getCurrentHealthAmount(GameObject character)` | – |
| `static float getMaxHealthAmount(GameObject character)` | – |
| `static float getAuxHealthAmount(GameObject character)` | – |
| `static void addAuxHealthAmount(GameObject character, float amount)` | – |
| `static float getHealthAmountToPick(GameObject character, float amount)` | – |
| `static float getShieldAmountToPick(GameObject character, float amount)` | – |
| `static float getStaminaAmountToPick(GameObject character, float amount)` | – |
| `static float getOxygenAmountToPick(GameObject character, float amount)` | – |
| `static void refillFullOxygen(GameObject character)` | – |
| `static void killCharacter(GameObject projectile, GameObject objectToDamage, Vector3 direction, Vector3 position, GameObject attacker, bool damageConstant)` | – |
| `static void killCharacter(GameObject objectToDamage)` | – |
| `static healthManagement getHealthManagement(GameObject objectToDamage)` | – |
| `static Transform getPlaceToShoot(GameObject objectToDamage)` | – |
| `static bool checkIfDamageReceiverBelongsToThisCharacter(GameObject characterToCheck, GameObject damageReceiverToCheckGameObject)` | – |
| `static bool checkIfWeakSpotListContainsTransform(GameObject objectToCheck, Transform transformToCheck)` | – |
| `static GameObject getPlaceToShootGameObject(GameObject objectToDamage)` | – |
| `static bool isCharacter(GameObject objectToCheck)` | – |
| `static bool isVehicle(GameObject objectToCheck)` | – |
| `static bool isRiderObject(GameObject objectToCheck)` | – |
| `static mainRiderSystem getMainRiderSystem(GameObject objectToCheck)` | – |
| `static bool checkIfDetectSurfaceBelongToRider(GameObject objectToCheck, Collider surfaceFound)` | – |
| `static float getVehicleRadius(GameObject objectToCheck)` | – |
| `static float getCustomCharacterRadius(GameObject objectToCheck)` | – |
| `static bool objectCanBeDamaged(GameObject objectToCheck)` | – |
| `static float getCharacterHeight(GameObject objectToCheck)` | – |
| `static playerController getPlayerControllerComponent(GameObject objectToCheck)` | – |
| `static bool isUsingGenericModelActive(GameObject objectToCheck)` | – |
| `static List<health.weakSpot> getCharacterWeakSpotList(GameObject objectToCheck)` | – |
| `static float getCurrentEnergyAmount(GameObject character)` | – |
| `static float getMaxEnergyAmount(GameObject character)` | – |
| `static float getAuxEnergyAmount(GameObject character)` | – |
| `static void addAuxEnergyAmount(GameObject character, float amount)` | – |
| `static float getEnergyAmountToPick(GameObject character, float amount)` | – |
| `static bool checkIfMaxEnergy(GameObject character)` | – |
| `static float getCurrentFuelAmount(GameObject vehicle)` | – |
| `static float getMaxFuelAmount(GameObject vehicle)` | – |
| `static float getAuxFuelAmount(GameObject vehicle)` | – |
| `static void addAuxFuelAmount(GameObject vehicle, float amount)` | – |
| `static float getFuelAmountToPick(GameObject vehicle, float amount)` | – |
| `static bool checkIfMaxFuel(GameObject vehicle)` | – |
| `static void pushCharacter(GameObject character, Vector3 direction)` | – |
| `static void pushCharacterWithoutForce(GameObject character)` | – |
| `static void pushCharacterWithoutForceAndPauseGetUp(GameObject character)` | – |
| `static void resurrectCharacter(GameObject character)` | – |
| `static bool checkIfCharacterCanBePushedOnExplosions(GameObject character)` | – |
| `static List<int> getBodyColliderLayerList(GameObject character)` | – |
| `static void setBodyColliderLayerList(GameObject character, List<int> newLayerList)` | – |
| `static void setBodyColliderLayerList(GameObject character, int newLayer)` | – |
| `static void pushRagdoll(GameObject character, Vector3 direction)` | – |
| `static bool isCharacterInRagdollState(GameObject character)` | – |
| `static Transform getCharacterRootMotionTransform(GameObject character)` | – |
| `static void pushAnyCharacter(GameObject character, float pushCharacterForce, float pushCharacterRagdollForce, Vector3 direction)` | – |
| `static bool attachObjectToSurfaceFound(Transform surfaceFound, Transform objectToAttach, Vector3 positionToCheck, bool checkRagdoll, Vector3 customObjectToAttachPosition)` | – |
| `static void checkParentToAssign(Transform objectToCheck, Transform newParent)` | – |
| `static bool setObjectParentOnDetectedSurface(Transform objectToSet, bool attachToLimbs, Transform surfaceDetected, bool ignoreCollisionsOnObjects)` | – |
| `static void setExplosion(Vector3 explosionPosition, float explosionRadius, bool userLayerMask, LayerMask layerToSearch, GameObject explosionOwner, bool canDamageProjectileOwner, GameObject projectileGameObject, bool killObjectsInRadius, bool isExplosive, bool isImplosive, float explosionDamage, bool pushCharacters, bool applyExplosionForceToVehicles, float explosionForceToVehiclesMultiplier, float explosionForce, ForceMode forceMode, bool checkObjectsInsideExplosionOwner, Transform explosionOwnerTransform, bool ignoreShield, bool checkForRemoteEventsOnObject, string remoteEventNameToActivate, int damageTypeID, bool damageTargetOverTime, float damageOverTimeDelay, float damageOverTimeDuration, float damageOverTimeAmount, float damageOverTimeRate, bool damageOverTimeToDeath, bool removeDamageOverTimeState, bool damageCanBeBlocked, bool searchClosestWeakSpot)` | – |
| `static GameObject getCharacterOrVehicle(GameObject objectToCheck)` | – |
| `static GameObject getCharacter(GameObject objectToCheck)` | – |
| `static GameObject getVehicle(GameObject objectToCheck)` | – |
| `static vehicleHUDManager getVehicleHUDManager(GameObject objectToCheck)` | – |
| `static void setVehicleInteractionTriggerState(GameObject objectToCheck, bool state)` | – |
| `static void ejectAllPassengersFromVehicle(GameObject objectToCheck)` | – |
| `static void activateSelfDestructionOnVehicleExternally(GameObject objectToCheck, float newSelfDestructDelayTime)` | – |
| `static void setNewVehicleGravityForce(GameObject objectToCheck, float newSelfDestructDelayTime)` | – |
| `static void setOriginalGravityForce(GameObject objectToCheck)` | – |
| `static void setReducedVehicleSpeed(GameObject objectToCheck, float reducedVehicleSpeedMultiplier)` | – |
| `static GameObject getVehicleDriver(GameObject objectToCheck)` | – |
| `static bool characterHasWeakSpotList(GameObject objectToCheck)` | – |
| `static bool checkIfDamagePositionIsCloseEnoughToWeakSpotByName(GameObject objectToCheck, Vector3 collisionPosition, List<string> weakSpotNameList, float maxDistanceToWeakSpot)` | – |
| `static Vector3 getClosestWeakSpotPositionToPosition(GameObject objectToCheck, Vector3 positionToCheck, List<string> weakListNameToCheck, bool checkWeakListName, float maxDistanceToBodyPart)` | – |
| `static AudioSource getAudioSource(GameObject objectToCheck, string audioSourceName)` | – |
| `static int getPlayerWeaponAmmoAmountToPick(playerWeaponsManager weaponsManager, string weaponName, int ammoAmuntToAdd)` | – |
| `static int getVehicleWeaponAmmoAmountToPick(vehicleWeaponSystem weaponsManager, string weaponName, int ammoAmuntToAdd)` | – |
| `static void killCharacterIfCurrentlyDrivingVehicle(GameObject objectToCheck)` | – |
| `static void activateGetOffFromVehicleIfDriving(GameObject objectToCheck)` | – |
| `static void explodeVehicleIfCharacterCurrentlyDriving(GameObject objectToCheck)` | – |
| `static bool isCharacterDriving(GameObject objectToCheck)` | – |
| `static GameObject getLastDriver(GameObject objectToCheck)` | – |
| `static GameObject getCharacterCurrentVehicle(GameObject objectToCheck)` | – |
| `static void sendNoiseSignal(float noiseRadius, Vector3 noisePosition, LayerMask noiseLyaer, float noiseDecibels, bool forceNoiseDetection, bool showNoiseDetectionGizmo, int noiseID)` | – |
| `static GameObject sendNoiseSignalToClosestAI(float noiseRadius, Vector3 noisePosition, LayerMask noiseLyaer, float noiseDecibels, bool forceNoiseDetection, bool showNoiseDetectionGizmo, int noiseID)` | – |
| `static bool giveInventoryObjectToCharacter(GameObject character, string inventoryObjectName, int inventoryObjectAmount, Transform positionToInstantiateInventoryObjectPickup, float forceAmount, float maxRadiusToInstantiate, ForceMode inventoryObjectForceMode, float forceRadius, bool spawnAllInventoryObjects, bool onlyRefillCertainAmountOfInventoryObjectAmount, bool spawnObjectIfNotEnoughSpaceOnInventory)` | – |
| `static bool addInventoryExtraSpace(GameObject character, int extraInventorySlotsAmount)` | – |
| `static void checkGravityRoomForGrabbedObject(GameObject grabbedObject, GameObject playerControllerGameObject)` | – |
| `static void checkIfPlayerIsLookingAtDeadTarget(Transform deadTarget, Transform placeToShoot)` | – |
| `static void sendCharacterAroundToAdd(GameObject currentPlayer, Transform targetToAdd, string sendCharacterAroundToAddName)` | – |
| `static void sendCharacterAroundToRemove(GameObject currentPlayer, Transform targetToRemove, string sendCharacterAroundToRemoveName)` | – |
| `static GameObject setSeekerProjectileInfo(Vector3 shootPosition, List<string> tagToLocate, bool usingScreenSpaceCamera, bool targetOnScreenForSeeker, Camera mainCamera, LayerMask targetToDamageLayer, Vector3 attackerPosition, bool checkIfAttackerLocatedOnRaycast, Collider attackerCollider)` | – |
| `static GameObject getCharacterFromPlaceToShoot(Transform placeToShoot)` | – |
