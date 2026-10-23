# GKC_Utils

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/GKC_Utils.cs:21`

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static float getCurrentDeltaTime()` | – |
| `static float getCurrentScaleTime()` | – |
| `static void checkAudioSourcePitch(AudioSource audioSourceToCheck)` | – |
| `static float distance(Vector3 positionA, Vector3 positionB)` | – |
| `static void ForGizmo(Vector3 pos, Vector3 direction, float arrowHeadLength = 0.25f, float arrowHeadAngle = 20.0f)` | – |
| `static void drawGizmoArrow(Vector3 pos, Vector3 direction, Color color, float arrowHeadLength, float arrowHeadAngle)` | – |
| `static void ForDebug(Vector3 pos, Vector3 direction, float arrowHeadLength = 0.25f, float arrowHeadAngle = 20.0f)` | – |
| `static void ForDebug(Vector3 pos, Vector3 direction, Color color, float arrowHeadLength = 0.25f, float arrowHeadAngle = 20.0f)` | – |
| `static void drawCapsuleGizmo(Vector3 point1, Vector3 point2, float capsuleCastRadius, Color sphereColor, Color cubeColor, Vector3 currentRayTargetPosition, Vector3 rayDirection, float distanceToTarget)` | – |
| `static void drawRectangleGizmo(Vector3 rectanglePosition, Quaternion rectangleRotation, Vector3 positionOffset, Vector3 rectangleScale, Color rectangleColor)` | – |
| `static void DrawWireCapsule(Vector3 point1, Vector3 point2, float radius)` | – |
| `static void checkDropObject(GameObject objectToDrop)` | – |
| `static void dropObject(GameObject currentPlayer, GameObject objectToDrop)` | – |
| `static bool checkIfObjectCanBePlaced(GameObject currentPlayer, GameObject objectToDrop)` | – |
| `static void dropObject(GameObject currentPlayer)` | – |
| `static void dropObjectIfNotGrabbedPhysically(GameObject currentPlayer, bool dropIfGrabbedPhysicallyWithIK)` | – |
| `static void checkIfKeepGrabbedObjectDuringAction(GameObject currentPlayer, bool keepGrabbedObjectOnActionIfNotDropped, bool keepGrabbedObject)` | – |
| `static void disableKeepGrabbedObjectStateAfterAction(GameObject currentPlayer)` | – |
| `static void keepMeleeWeaponGrabbed(GameObject currentPlayer)` | – |
| `static void drawMeleeWeaponGrabbed(GameObject currentPlayer)` | – |
| `static void checkIfDropThrownWeaponWhenUsingDevice(GameObject currentPlayer)` | – |
| `static void drawMeleeWeaponGrabbedCheckingAnimationDelay(GameObject currentPlayer)` | – |
| `static void drawOrHolsterWeapon(GameObject currentCharacter, bool state, string weaponName, bool isFireWeapon, bool useQuickDrawHolster, bool equipWeaponIfNotEquipped)` | – |
| `static bool isCharacterUsingMeleeWeapons(GameObject currentCharacter, string weaponName)` | – |
| `static bool isCharacterUsingFireWeapons(GameObject currentCharacter, string weaponName)` | – |
| `static bool isCharacterUsingSphereMode(GameObject currentCharacter)` | – |
| `static void disableCurrentAttackInProcess(GameObject currentPlayer)` | – |
| `static void resetIdleStateOnCloseCombat(GameObject currentPlayer)` | – |
| `static void grabPhysicalObjectExternally(GameObject currentPlayer, GameObject objectToGrab)` | – |
| `static void enableOrDisableMeleeWeaponMeshActiveState(GameObject currentPlayer, bool state)` | – |
| `static void enableOrDisableFireWeaponMeshActiveState(GameObject currentPlayer, bool state)` | – |
| `static bool enableOrDisableIKOnWeaponsDuringAction(GameObject currentPlayer, bool state)` | – |
| `static void stopMatchPlayerToTargetMovementIfActive(GameObject currentPlayer)` | – |
| `static void checkIfStopUseDevice(GameObject currentPlayer)` | – |
| `static void useObjectExternally(GameObject currentPlayer, GameObject objectToUse)` | – |
| `static void useDeviceObjectExternally(GameObject currentPlayer, GameObject objectToUse)` | – |
| `static Vector2 getScreenResolution()` | – |
| `static void createInventoryWeaponAmmo(string weaponName, string ammoName, GameObject weaponAmmoMesh, Texture weaponAmmoIconTexture, string inventoryAmmoCategoryName, int ammoAmountPerPickup, string customAmmoDescription)` | – |
| `static void createInventoryWeapon(string weaponName, string inventoryWeaponCategoryName, GameObject weaponMesh, string weaponDescription, Texture weaponIconTexture, string relativePathWeaponsMesh, bool isMeleeWeapon, bool useDurabilityValue, float durabilityAmountValue, float maxDurabilityAmountValue, float objectWeight, bool canBeSold, float sellPrice, float vendorPrice)` | – |
| `static void createInventoryArmorClothPiece(string objectName, string inventoryObjectCategoryName, string categoryName, GameObject objectMeshPrefab, string objectDescription, Texture objectIconTexture, string relativePathObjectMesh)` | – |
| `static void createInventoryObject(string objectName, string inventoryCategoryName, GameObject objectMesh, string objectDescription, Texture iconTexture, string relativePathMesh, bool canBeEquipped, bool canBeDropped, bool canBeDiscarded, bool useDurability, float durabilityAmount, float maxDurabilityAmount, bool isMeleeShield, bool canBePlaceOnQuickAccessSlot, float objectWeight, bool canBeSold, float sellPrice, float vendorPrice)` | – |
| `static GameObject getInventoryPrefabByName(string objectName)` | – |
| `static GameObject getInventoryMeshByName(string objectName)` | – |
| `static inventoryInfo getInventoryInfoFromName(string objectName)` | – |
| `static bool checkIfInventoryObjectNameExits(string objectName)` | – |
| `static float getMaxDurabilityValueOnObjectByName(string objectName)` | – |
| `static Texture getInventoryObjectIconByName(string inventoryObjectName)` | – |
| `static GameObject createPrefab(string prefabPath, string prefabName, GameObject prefabToCreate)` | – |
| `static GameObject instantiatePrefabInScene(string prefabPath, string prefabName, LayerMask layerToPlaceObjects)` | – |
| `static void createSettingsListTemplate(string characterTemplateDataPath, string characterTemplateName, int characterTemplateID, List<buildPlayer.settingsInfoCategory> settingsInfoCategoryList)` | – |
| `static GameObject findMainPlayerOnScene()` | – |
| `static Transform findMainPlayerTransformOnScene()` | – |
| `static playerCamera findMainPlayerCameraOnScene()` | – |
| `static Camera findMainPlayerCameraComponentOnScene()` | – |
| `static Transform findMainPlayerCameraTransformOnScene()` | – |
| `static menuPause findMainPlayergetPauseManagerOnScene()` | – |
| `static void updateCanvasValuesByPlayer(GameObject playerControllerGameObject, GameObject pauseManagerObject, GameObject newCanvasPanel)` | – |
| `static void removeDeviceFromListOnAllPlayersOnSceneWithoutDisablingDevice(GameObject deviceToRemove)` | – |
| `static void updateMainPlayerComponentsOnGameManager(GameObject newPlayerParent)` | – |
| `static void updateComponent(UnityEngine.Object componentToUpdate)` | – |
| `static void updateComponent(MonoBehaviour componentToUpdate)` | – |
| `static void setActiveGameObjectInEditor(GameObject objectToSelect)` | – |
| `static void setActiveGameObjectInEditorWithoutCheckNull(GameObject objectToSelect)` | – |
| `static GameObject getActiveGameObjectInEditor()` | – |
| `static bool isCurrentSelectionActiveGameObject(GameObject objectToSelect)` | – |
| `static Camera getCameraEditor()` | – |
| `static GameObject getLoadAssetAtPath(string objectPath)` | – |
| `static void alignViewToObject(Transform transformToUse)` | – |
| `static void alignViewToPositionRotation(Vector3 cameraTargetPosition, Quaternion cameraTargetRotation)` | – |
| `static bool isApplicationPlaying()` | – |
| `static void pauseOrResumeAIOnScene(bool state, int pauseCharacterPriority)` | – |
| `static void pauseOrResumeAIOnSceneWithExceptionList(bool state, int pauseCharacterPriority, List<GameObject> AIExceptionList)` | – |
| `static void pauseOrResumeEnemyAIOnScene(bool state, string playerFactionName, int pauseCharacterPriority)` | – |
| `static void pauseOrResumeCharacter(bool state, playerController currentPlayerController, int pauseCharacterPriority)` | – |
| `static void pauseOrResumeAllCharactersScene(bool state)` | – |
| `static Vector3 ClampMagnitude(Vector3 v, float max, float min)` | – |
| `static string getCharacterFactionName(GameObject newTarget)` | – |
| `static void setGravityValueOnObjectFromPlayerValues(artificialObjectGravity newArtificialObjectGravity, GameObject currentPlayer, float gravityForceForCircumnavigationOnProjectile)` | – |
| `static void enableOrDisableFreeFloatingModeOnState(GameObject currentPlayer, bool state)` | – |
| `static weaponObjectInfo getMeleeWeaponObjectInfo(string weaponName, meleeWeaponsGrabbedManager mainMeleeWeaponsGrabbedManager)` | – |
| `static float Abs(float f)` | – |
| `static void addAllMainManagersToScene()` | – |
| `static void instantiateMainManagerOnSceneWithType(string mainManagerName, Type typeToSearch)` | – |
| `static void instantiateMainManagerOnSceneWithTypeOnApplicationPlaying(string mainManagerName, Type typeToSearch, bool callGetComponentInstance)` | – |
| `static void activateTimeBulletXSeconds(float timeBulletDuration, float timeScale)` | – |
| `static void loadScene(int newSceneIndex, bool useLoadScreen, int loadScreenScene, string sceneToLoadAsyncPrefsName, bool useLastSceneIndexAsLoadScreen, bool checkLoadingScreenSceneConfigured, string loadingScreenSceneName)` | – |
| `static void reloadSceneOnEditor()` | – |
| `static string getSceneNameFromIndex(int sceneIndex)` | – |
| `static void updateDirtyScene(string recordObjectName, GameObject gameObjectToRecord)` | – |
| `static void updateDirtyScene()` | – |
| `static string getRandomString(int length)` | – |
| `static void removeEnemiesFromNewFriendFaction(Transform characterTransform)` | – |
| `static void eventOnPressingKeyboardInput(int controllerNumber)` | – |
| `static void eventOnPressingGamepadInput(int controllerNumber)` | – |
| `static void enableOrDisableAbilityGroupByName(Transform characterTransform, bool state, List<string> abilityNameList)` | – |
| `static void increaseStatsByList(Transform characterTransform, bool state, List<objectExperienceSystem.statInfo> statInfoList)` | – |
| `static void increaseStat(Transform characterTransform, string statName, float statAmount)` | – |
| `static void activateAbilityByName(Transform characterTransform, string abilityName, bool abilityIsTemporallyActivated, bool ignoreCheckMenusState)` | – |
| `static bool checkIfAbilitiesOnUseOrCooldown(Transform characterTransform, string abilityName)` | – |
| `static void setUnlockStateOnSkill(Transform characterTransform, string skillName, bool state)` | – |
| `static void setUnlockStateOnSkillList(Transform characterTransform, List<string> skillNameList, bool state)` | – |
| `static GameObject createSliceRagdollPrefab(GameObject characterMeshPrefab, string newPrefabsPath, Material newSliceMaterial, bool setTagOnSkeletonRigidbodiesValue, string tagOnSkeletonRigidbodiesValue)` | – |
| `static Transform getMountPointTransformByName(string mountPointName, Transform characterTransform)` | – |
| `static Transform getHumanBoneMountPointTransformByName(string mountPointName, Transform characterTransform)` | – |
| `static void activateBrainWashOnCharacter(GameObject currentCharacter, string factionToConfigure, string newTag, bool setNewName, string newName, bool AIIsFriend, bool followPartnerOnTriggerEnabled, bool setPlayerAsPartner, GameObject newPartner, bool useRemoteEvents, List<string> remoteEventNameList)` | – |
| `static remoteEventSystem getRemoteEventSystemFromObject(GameObject objectToCheck, bool checkForRemoteEventSocket)` | – |
| `static void activateRemoteEvent(string remoteEventName, GameObject objectToCheck)` | – |
| `static void activateRemoteEvents(List<string> remoteEventNameList, GameObject objectToCheck)` | – |
| `static float getCharacterRadius(Transform characterToCheck)` | – |
| `static List<Collider> getCharacterExtraColliderList(Transform characterToCheck)` | – |
| `static bool checkIfObjectIsOnCharacterExtraColliderList(Collider colliderToCheck, GameObject characterToCheck)` | – |
| `static bool checkIfObjectIsOnCharacterExtraColliderList(Collider colliderToCheck, playerController currentPlayerController)` | – |
| `static float getAngle(Vector3 v1, Vector3 v2)` | – |
| `static string getCurrentLanguage()` | – |
| `static void setCurrentLanguage(string newLanguage)` | – |
| `static void updateAllLanguageElementCheckerOnScene()` | – |
| `static bool isUpdateElementsOnLanguageChangeActive()` | – |
| `static void removeNullGameObjectsFromList(List<GameObject> listToCheck)` | – |
| `static List<string> getCurrentLanguageList()` | – |
| `static void addLanguage(string newName)` | – |
| `static void removeLanguage(string newName)` | – |
| `static void refreshAssetDatabase()` | – |
| `static List<T> FindObjectsOfTypeAll<T>()` | – |
| `static List<T> FindObjectOfTypeAll<T>()` | – |
| `static float getStateValueByName(string statNameToShow, GameObject playerGameobject)` | – |
| `static float getInventoryObjectAmountByName(string objectNameToShow, GameObject playerGameobject)` | – |
| `static inventoryManager getInventoryManagerFromCharacter(GameObject playerGameobject)` | – |
| `static GameObject spawnObjectFromPrefabsManager(string objectToSpawnName)` | – |
| `static prefabsManager addPrefabsManagerToScene()` | – |
| `static void unpackPrefabObjectByCheckingTransformRoot(GameObject currentObject)` | – |
| `static void unpackPrefabObject(GameObject currentObject)` | – |
| `static void setSelectedGameObjectOnUI(bool ignoreCheckGamepad, bool isUsingGamepad, GameObject newGameObject, bool showDebugPrint)` | – |
| `static string getMainDataPath()` | – |
| `static void addElementToPlayerScreenObjectivesManager(GameObject currentPlayer, GameObject placeToShoot, string locatedEnemyIconName)` | – |
| `static void removeElementToPlayerScreenObjectivesManager(GameObject currentPlayer, GameObject objectToRemove)` | – |
| `static void removeElementListToPlayerScreenObjectivesManager(GameObject currentPlayer, List<Transform> objectToRemoveList)` | – |
| `static void removeTargetFromAIEnemyList(GameObject objectToRemove)` | – |
| `static void removeTargetFromAICharacter(GameObject objectToRemove, GameObject currentAICharacter)` | – |
| `static void setAICharacterOnVehicle(GameObject newVehicle, GameObject currentCharacter)` | – |
| `static void getOffFromVehicleToDriverAI(Transform currentCharacter)` | – |
| `static void createPieceMeshesObjectsFromSetByName(GameObject objectToCreate, string objectName)` | – |
| `static void addNewBlueprintsUnlockedElement(GameObject currentPlayer, string newBlueprintsUnlockedElement)` | – |
| `static void addNewBlueprintsUnlockedList(GameObject currentPlayer, List<string> craftingRecipesList)` | – |
| `static void setBlueprintsUnlockedListValue(GameObject currentPlayer, List<string> craftingRecipesList)` | – |
| `static List<string> getBlueprintsUnlockedListValue(GameObject currentPlayer)` | – |
| `static bool isUseOnlyBlueprintsUnlockedActive(GameObject currentPlayer)` | – |
| `static bool anyObjectToCraftInTimeActive(GameObject currentPlayer)` | – |
| `static void setUseOnlyBlueprintsUnlockedState(GameObject currentPlayer, bool state)` | – |
| `static List<craftObjectInTimeSimpleInfo> getCraftObjectInTimeInfoList(GameObject currentPlayer)` | – |
| `static void setCraftObjectInTimeInfoList(GameObject currentPlayer, List<craftObjectInTimeSimpleInfo> newCraftObjectInTimeSimpleInfoList)` | – |
| `static List<string> getObjectCategoriesToCraftAvailableAtAnyMomentValue(GameObject currentPlayer)` | – |
| `static void setObjectCategoriesToCraftAvailableAtAnyMomentValue(GameObject currentPlayer, List<string> newList)` | – |
| `static Vector3 getParableSpeed(Vector3 origin, Vector3 target, Vector3 cameraDirection, Transform cameraDirectoinTransform, bool objectiveFoundOnRaycast, bool useMaxDistanceWhenNoSurfaceFound, float maxDistanceWhenNoSurfaceFound)` | – |
| `static GameObject getHudElementParent(GameObject playerGameObject, string mainPanelName)` | – |
| `static headTrack getCharacterHeadTrack(GameObject playerGameObject)` | – |
| `static Animator getCharacterAnimator(GameObject playerGameObject)` | – |
| `static bool isActionActiveOnCharacter(GameObject playerGameObject)` | – |
| `static bool isSharedActionActiveOnCharacter(GameObject playerGameObject)` | – |
| `static void setAnimatorTriggerOnCharacter(GameObject playerGameObject, string triggerName)` | – |
| `static void resetAnimatorTriggerOnCharacter(GameObject playerGameObject, string triggerName)` | – |
| `static void deletePlayerPrefByName(string newName)` | – |
| `static string getPlayerTag()` | – |
| `static string getFriendTag()` | – |
| `static string getEnemyTag()` | – |
| `static string getCurrentPlayersModeName(Transform characterTransform)` | – |
| `static void checkPlayerStates(GameObject character)` | – |
| `static void checkAndSet2_5dModeOnAiIfCurrentViewInSceneActive(findObjectivesSystem currentFindObjectivesSystem)` | – |
| `static void pauseOrResumeAttackActiveStateOnAllAIOnScene(List<GameObject> listOfCharactersToIgnore, bool state, bool useRandomWalkEnabled)` | – |
| `static string checkFullArmorClothState(fullArmorClothTemplateData mainFullArmorClothTemplateData, List<string> currentPiecesList, bool showDebugPrint)` | – |
| `static void removeElementFromEditorList(SerializedProperty editorList, int index)` | – |
| `static void checkUnpackPrefabToDestroyObject(GameObject mainObjectParent, GameObject objectToDestroy)` | – |
| `static string getInteractionObjectsLocalizationManagerLocalizedText(string textContent)` | – |
| `static void renameAsset(GameObject currentObject, string newName)` | – |
| `static void renameAsset(UnityEngine.Object currentObject, string newName)` | – |
| `static void replacePrefabNameBased(GameObject newPrefab, UnityEngine.Object currentPrefabObject)` | – |
| `static void replacePrefabConnectToPrefab(GameObject newPrefab, string prefabFilePath)` | – |
| `static void enableOrDisableOptionsWithCustomShaders(bool state)` | – |

## 内部型

- `swipeDirections`（class）
