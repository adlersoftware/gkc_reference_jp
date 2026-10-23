# playerComponentsManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/playerComponentsManager.cs:5`

**概要**: プレイヤーを構成する各コンポーネントへの参照を1か所に集約し、他スクリプトへgetterで公開するハブ。自身は処理を持たず、参照の受け渡しだけを担う。

## インスペクター設定

### Main Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Inventory Manager | `mainInventoryManager` | `inventoryManager` | – | – |
| Main Player Input Manager | `mainPlayerInputManager` | `playerInputManager` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Using Devices System | `mainUsingDevicesSystem` | `usingDevicesSystem` | – | – |
| Main Foot Step Manager | `mainFootStepManager` | `footStepManager` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |
| Main Other Powers | `mainOtherPowers` | `otherPowers` | – | – |
| Main Gravity System | `mainGravitySystem` | `gravitySystem` | – | – |
| Main Grab Objects | `mainGrabObjects` | `grabObjects` | – | – |
| Main IK System | `mainIKSystem` | `IKSystem` | – | – |
| Main Player States Manager | `mainPlayerStatesManager` | `playerStatesManager` | – | – |
| Main Health | `mainHealth` | `health` | – | – |
| Main Character Faction Manager | `mainCharacterFactionManager` | `characterFactionManager` | – | – |
| Main Player Info Panel On Screen System | `mainPlayerInfoPanelOnScreenSystem` | `playerInfoPanelOnScreenSystem` | – | – |
| Main Ragdoll Activator | `mainRagdollActivator` | `ragdollActivator` | – | – |
| Main Player Action System | `mainPlayerActionSystem` | `playerActionSystem` | – | – |
| Main Remote Event System | `mainRemoteEventSystem` | `remoteEventSystem` | – | – |
| Main Damage Hit Reaction System | `mainDamageHitReactionSystem` | `damageHitReactionSystem` | – | – |
| Main Character Properties System | `mainCharacterPropertiesSystem` | `characterPropertiesSystem` | – | – |
| Main GKC Condition System | `mainGKCConditionSystem` | `GKCConditionSystem` | – | – |
| Main Close Combat System | `mainCloseCombatSystem` | `closeCombatSystem` | – | – |

### Camera Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Head Bob | `mainHeadBob` | `headBob` | – | – |

### Stats Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Experience System | `mainPlayerExperienceSystem` | `playerExperienceSystem` | – | – |
| Main Currency System | `mainCurrencySystem` | `currencySystem` | – | – |
| Main Inventory Bank UI System | `mainInventoryBankUISystem` | `inventoryBankUISystem` | – | – |
| Main Vendor UI System | `mainVendorUISystem` | `vendorUISystem` | – | – |
| Main Player HUD Manager | `mainPlayerHUDManager` | `playerHUDManager` | – | – |
| Main Stamina System | `mainStaminaSystem` | `staminaSystem` | – | – |
| Main Oxygen System | `mainOxygenSystem` | `oxygenSystem` | – | – |
| Main Player Stats System | `mainPlayerStatsSystem` | `playerStatsSystem` | – | – |
| Main Player Skills System | `mainPlayerSkillsSystem` | `playerSkillsSystem` | – | – |
| Main Inventory Weight Manager | `mainInventoryWeightManager` | `inventoryWeightManager` | – | – |
| Main Player Abilities System | `mainPlayerAbilitiesSystem` | `playerAbilitiesSystem` | – | – |

### Character Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Save Game System | `mainSaveGameSystem` | `saveGameSystem` | – | – |
| Main Map System | `mainMapSystem` | `mapSystem` | – | – |
| Main Pause Manager | `mainPauseManager` | `menuPause` | – | – |
| Game Info Hud Manager | `gameInfoHudManager` | `showGameInfoHud` | – | – |
| Main Objective Station UI System | `mainObjectiveStationUISystem` | `objectiveStationUISystem` | – | – |
| Main Body Mount Points System | `mainBodyMountPointsSystem` | `bodyMountPointsSystem` | – | – |
| Main Build Player | `mainBuildPlayer` | `buildPlayer` | – | – |
| Main Inventory Character Customization System | `mainInventoryCharacterCustomizationSystem` | `inventoryCharacterCustomizationSystem` | – | – |
| Main Crafting UI System | `mainCraftingUISystem` | `craftingUISystem` | – | – |
| Main Crafting System | `mainCraftingSystem` | `craftingSystem` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main Character To Receive Orders | `mainCharacterToReceiveOrders` | `characterToReceiveOrders` | – | – |
| Main AI Patrol System | `mainAIPatrolSystem` | `AIPatrolSystem` | – | – |

### Others Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Objective Log System | `mainObjectiveLogSystem` | `objectiveLogSystem` | – | – |
| Main Player Tutorial System | `mainPlayerTutorialSystem` | `playerTutorialSystem` | – | – |
| Main Player Screen Objectives System | `mainPlayerScreenObjectivesSystem` | `playerScreenObjectivesSystem` | – | – |
| Main Player Ladder System | `mainPlayerLadderSystem` | `playerLadderSystem` | – | – |
| Main Pick Ups Screen Info | `mainPickUpsScreenInfo` | `pickUpsScreenInfo` | – | – |
| Main Friend List Manager | `mainFriendListManager` | `friendListManager` | – | – |
| Main Override Element Control System | `mainOverrideElementControlSystem` | `overrideElementControlSystem` | – | – |
| Main Travel Station UI System | `mainTravelStationUISystem` | `travelStationUISystem` | – | – |
| Main Player Options Editor System | `mainPlayerOptionsEditorSystem` | `playerOptionsEditorSystem` | – | – |
| Main Grabbed Object Melee Attack System | `mainGrabbedObjectMeleeAttackSystem` | `grabbedObjectMeleeAttackSystem` | – | – |
| Main Melee Weapons Grabbed Manager | `mainMeleeWeaponsGrabbedManager` | `meleeWeaponsGrabbedManager` | – | – |
| Main Remote Player Navmesh Override | `mainRemotePlayerNavmeshOverride` | `remotePlayerNavmeshOverride` | – | – |
| Main Switch Companion System | `mainSwitchCompanionSystem` | `switchCompanionSystem` | – | – |
| Main AI Around Manager | `mainAIAroundManager` | `AIAroundManager` | – | – |
| Main Turn Based Combat Team Info | `mainTurnBasedCombatTeamInfo` | `turnBasedCombatTeamInfo` | – | – |
| Main Turn Based Combat Actions System | `mainTurnBasedCombatActionsSystem` | `turnBasedCombatActionsSystem` | – | – |
| Main Vehicle Passenger Underwater | `mainVehiclePassengerUnderwater` | `vehiclePassengerUnderwater` | – | – |

### Secondary Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Jetpack System | `mainJetpackSystem` | `jetpackSystem` | – | – |
| Main Fly System | `mainFlySystem` | `flySystem` | – | – |
| Main Hide Character Fixed Place System Player Management | `mainHideCharacterFixedPlaceSystemPlayerManagement` | `hideCharacterFixedPlaceSystemPlayerManagement` | – | – |
| Main Examine Object System Player Management | `mainExamineObjectSystemPlayerManagement` | `examineObjectSystemPlayerManagement` | – | – |
| Main Puzzle System Player Management | `mainPuzzleSystemPlayerManagement` | `puzzleSystemPlayerManagement` | – | – |
| Main Padlock System Player Management | `mainPadlockSystemPlayerManagement` | `padlockSystemPlayerManagement` | – | – |
| Main Grappling Hook Targets System | `mainGrapplingHookTargetsSystem` | `grapplingHookTargetsSystem` | – | – |
| Main Set Transparent Surfaces | `mainSetTransparentSurfaces` | `setTransparentSurfaces` | – | – |
| Main Weapons Attachment UI Manager | `mainWeaponsAttachmentUIManager` | `weaponsAttachmentUIManager` | – | – |
| Main Climb Ledge System | `mainClimbLedgeSystem` | `climbLedgeSystem` | – | – |
| Main Damage In Screen | `mainDamageInScreen` | `damageInScreen` | – | – |
| Main Damage Screen System | `mainDamageScreenSystem` | `damageScreenSystem` | – | – |
| Main Dialog System | `mainDialogSystem` | `dialogSystem` | – | – |
| Main Projectiles On Character Body Manager | `mainProjectilesOnCharacterBodyManager` | `projectilesOnCharacterBodyManager` | – | – |
| Main Paraglider System | `mainParagliderSystem` | `paragliderSystem` | – | – |
| Main Camera Capture System | `mainCameraCaptureSystem` | `cameraCaptureSystem` | – | – |
| Main Custom Character Controller Manager | `mainCustomCharacterControllerManager` | `customCharacterControllerManager` | – | – |
| Main Player Nav Mesh System | `mainPlayerNavMeshSystem` | `playerNavMeshSystem` | – | – |
| Main Object To Attract With Grappling Hook | `mainObjectToAttractWithGrapplingHook` | `objectToAttractWithGrapplingHook` | – | – |
| Main Override Input Manager | `mainOverrideInputManager` | `overrideInputManager` | – | – |
| Main Gravity Wall Run System | `mainGravityWallRunSystem` | `gravityWallRunSystem` | – | – |
| Main Objects Stats System | `mainObjectsStatsSystem` | `objectsStatsSystem` | – | – |
| Main Match Player To Target System | `mainMatchPlayerToTargetSystem` | `matchPlayerToTargetSystem` | – | – |
| Main Character Model List Manager | `mainCharacterModelListManager` | `characterModelListManager` | – | – |

### External Controller Behavior Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Wall Running External Controller Behavior | `wallRunningExternalControllerBehavior` | `externalControllerBehavior` | – | – |
| Swim External Controller Behavior | `swimExternalControllerBehavior` | `externalControllerBehavior` | – | – |
| Slide External Controller Behavior | `slideExternalControllerBehavior` | `externalControllerBehavior` | – | – |
| Wall Slide Jump Exteral Controller Behavior | `wallSlideJumpExteralControllerBehavior` | `externalControllerBehavior` | – | – |
| Rail External Controller Behavior | `railExternalControllerBehavior` | `externalControllerBehavior` | – | – |
| Walk On Balance Externa Controller Behavior | `walkOnBalanceExternaControllerBehavior` | `externalControllerBehavior` | – | – |
| Climb Rope Externa Controller Behavior | `climbRopeExternaControllerBehavior` | `externalControllerBehavior` | – | – |
| Free Climb System Behavior | `freeClimbSystemBehavior` | `externalControllerBehavior` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getPlayerExperienceSystem()` | `mainPlayerExperienceSystem` をそのまま返すだけ。 |
| `getCurrencySystem()` | `mainCurrencySystem` をそのまま返すだけ。 |
| `getVendorUISystem()` | `mainVendorUISystem` をそのまま返すだけ。 |
| `getPlayerHUDManager()` | `mainPlayerHUDManager` をそのまま返すだけ。 |
| `getMapSystem()` | `mainMapSystem` をそのまま返すだけ。 |
| `getInventoryManager()` | `mainInventoryManager` をそのまま返すだけ。 |
| `getPauseManager()` | `mainPauseManager` をそのまま返すだけ。 |
| `getGameInfoHudManager()` | `gameInfoHudManager` をそのまま返すだけ。 |
| `getPlayerInputManager()` | `mainPlayerInputManager` をそのまま返すだけ。 |
| `getObjectiveLogSystem()` | `mainObjectiveLogSystem` をそのまま返すだけ。 |
| `getPlayerTutorialSystem()` | `mainPlayerTutorialSystem` をそのまま返すだけ。 |
| `getPlayerScreenObjectivesSystem()` | `mainPlayerScreenObjectivesSystem` をそのまま返すだけ。 |
| `getStaminaSystem()` | `mainStaminaSystem` をそのまま返すだけ。 |
| `getPlayerLadderSystem()` | `mainPlayerLadderSystem` をそのまま返すだけ。 |
| `getOxygenSystem()` | `mainOxygenSystem` をそのまま返すだけ。 |
| `getObjectiveStationUISystem()` | `mainObjectiveStationUISystem` をそのまま返すだけ。 |
| `getPlayerStatsSystem()` | `mainPlayerStatsSystem` をそのまま返すだけ。 |
| `getPlayerSkillsSystem()` | `mainPlayerSkillsSystem` をそのまま返すだけ。 |
| `getPickUpsScreenInfo()` | `mainPickUpsScreenInfo` をそのまま返すだけ。 |
| `getSaveGameSystem()` | `mainSaveGameSystem` をそのまま返すだけ。 |
| `getPlayerWeaponsManager()` | `mainPlayerWeaponsManager` をそのまま返すだけ。 |
| `getPlayerController()` | `mainPlayerController` をそのまま返すだけ。 |
| `getPlayerCamera()` | `mainPlayerCamera` をそのまま返すだけ。 |
| `getUsingDevicesSystem()` | `mainUsingDevicesSystem` をそのまま返すだけ。 |
| `getFootStepManager()` | `mainFootStepManager` をそのまま返すだけ。 |
| `getHeadTrack()` | `mainHeadTrack` をそのまま返すだけ。 |
| `getOtherPowers()` | `mainOtherPowers` をそのまま返すだけ。 |
| `getHeadBob()` | `mainHeadBob` をそのまま返すだけ。 |
| `getGravitySystem()` | `mainGravitySystem` をそのまま返すだけ。 |
| `getGrabObjects()` | `mainGrabObjects` をそのまま返すだけ。 |
| `getIKSystem()` | `mainIKSystem` をそのまま返すだけ。 |
| `getPlayerStatesManager()` | `mainPlayerStatesManager` をそのまま返すだけ。 |
| `getFriendListManager()` | `mainFriendListManager` をそのまま返すだけ。 |
| `getHealth()` | `mainHealth` をそのまま返すだけ。 |
| `getJetpackSystem()` | `mainJetpackSystem` をそのまま返すだけ。 |
| `getCharacterFactionManager()` | `mainCharacterFactionManager` をそのまま返すだけ。 |
| `getHideCharacterFixedPlaceSystemPlayerManagement()` | `mainHideCharacterFixedPlaceSystemPlayerManagement` をそのまま返すだけ。 |
| `getExamineObjectSystemPlayerManagement()` | `mainExamineObjectSystemPlayerManagement` をそのまま返すだけ。 |
| `getPuzzleSystemPlayerManagement()` | `mainPuzzleSystemPlayerManagement` をそのまま返すだけ。 |
| `getPadlockSystemPlayerManagement()` | `mainPadlockSystemPlayerManagement` をそのまま返すだけ。 |
| `getOverrideElementControlSystem()` | `mainOverrideElementControlSystem` をそのまま返すだけ。 |
| `getPlayerInfoPanelOnScreenSystem()` | `mainPlayerInfoPanelOnScreenSystem` をそのまま返すだけ。 |
| `getInventoryWeightManager()` | `mainInventoryWeightManager` をそのまま返すだけ。 |
| `getTravelStationUISystem()` | `mainTravelStationUISystem` をそのまま返すだけ。 |
| `getInventoryBankUISystem()` | `mainInventoryBankUISystem` をそのまま返すだけ。 |
| `getRagdollActivator()` | `mainRagdollActivator` をそのまま返すだけ。 |
| `getPlayerActionSystem()` | `mainPlayerActionSystem` をそのまま返すだけ。 |
| `getPlayerAbilitiesSystem()` | `mainPlayerAbilitiesSystem` をそのまま返すだけ。 |
| `getRemoteEventSystem()` | `mainRemoteEventSystem` をそのまま返すだけ。 |
| `getGrapplingHookTargetsSystem()` | `mainGrapplingHookTargetsSystem` をそのまま返すだけ。 |
| `getSetTransparentSurfaces()` | `mainSetTransparentSurfaces` をそのまま返すだけ。 |
| `getPlayerOptionsEditorSystem()` | `mainPlayerOptionsEditorSystem` をそのまま返すだけ。 |
| `getWeaponsAttachmentUIManager()` | `mainWeaponsAttachmentUIManager` をそのまま返すだけ。 |
| `getGrabbedObjectMeleeAttackSystem()` | `mainGrabbedObjectMeleeAttackSystem` をそのまま返すだけ。 |
| `getDamageHitReactionSystem()` | `mainDamageHitReactionSystem` をそのまま返すだけ。 |
| `getFlySystem()` | `mainFlySystem` をそのまま返すだけ。 |
| `getCharacterPropertiesSystem()` | `mainCharacterPropertiesSystem` をそのまま返すだけ。 |
| `getMeleeWeaponsGrabbedManager()` | `mainMeleeWeaponsGrabbedManager` をそのまま返すだけ。 |
| `getRemotePlayerNavmeshOverride()` | `mainRemotePlayerNavmeshOverride` をそのまま返すだけ。 |
| `getClimbLedgeSystem()` | `mainClimbLedgeSystem` をそのまま返すだけ。 |
| `getDamageInScreen()` | `mainDamageInScreen` をそのまま返すだけ。 |
| `getDamageScreenSystem()` | `mainDamageScreenSystem` をそのまま返すだけ。 |
| `getMainDialogSystem()` | `mainDialogSystem` をそのまま返すだけ。 |
| `getProjectilesOnCharacterBodyManager()` | `mainProjectilesOnCharacterBodyManager` をそのまま返すだけ。 |
| `getParagliderSystem()` | `mainParagliderSystem` をそのまま返すだけ。 |
| `getGKCConditionSystem()` | `mainGKCConditionSystem` をそのまま返すだけ。 |
| `getCameraCaptureSystem()` | `mainCameraCaptureSystem` をそのまま返すだけ。 |
| `getWallRunningExternalControllerBehavior()` | `wallRunningExternalControllerBehavior` をそのまま返すだけ。 |
| `getSwimExternalControllerBehavior()` | `swimExternalControllerBehavior` をそのまま返すだけ。 |
| `getSlideExternalControllerBehavior()` | `slideExternalControllerBehavior` をそのまま返すだけ。 |
| `getCustomCharacterControllerManager()` | `mainCustomCharacterControllerManager` をそのまま返すだけ。 |
| `getBodyMountPointsSystem()` | `mainBodyMountPointsSystem` をそのまま返すだけ。 |
| `getWallSlideJumpExteralControllerBehavior()` | `wallSlideJumpExteralControllerBehavior` をそのまま返すだけ。 |
| `getBuildPlayer()` | `mainBuildPlayer` をそのまま返すだけ。 |
| `getInventoryCharacterCustomizationSystem()` | `mainInventoryCharacterCustomizationSystem` をそのまま返すだけ。 |
| `getRailExternalControllerBehavior()` | `railExternalControllerBehavior` をそのまま返すだけ。 |
| `getWalkOnBalanceExternaControllerBehavior()` | `walkOnBalanceExternaControllerBehavior` をそのまま返すだけ。 |
| `getClimbRopeExternaControllerBehavior()` | `climbRopeExternaControllerBehavior` をそのまま返すだけ。 |
| `getPlayerNavMeshSystem()` | `mainPlayerNavMeshSystem` をそのまま返すだけ。 |
| `getObjectToAttractWithGrapplingHook()` | `mainObjectToAttractWithGrapplingHook` をそのまま返すだけ。 |
| `getOverrideInputManager()` | `mainOverrideInputManager` をそのまま返すだけ。 |
| `getGravityWallRunSystem()` | `mainGravityWallRunSystem` をそのまま返すだけ。 |
| `getFreeClimbExternalControllerBehavior()` | `freeClimbSystemBehavior` をそのまま返すだけ。 |
| `getCloseCombatSystem()` | `mainCloseCombatSystem` をそのまま返すだけ。 |
| `getCraftingUISystem()` | `mainCraftingUISystem` をそのまま返すだけ。 |
| `getCraftingSystem()` | `mainCraftingSystem` をそのまま返すだけ。 |
| `getObjectsStatsSystem()` | `mainObjectsStatsSystem` をそのまま返すだけ。 |
| `getFindObjectivesSystem()` | `mainFindObjectivesSystem` をそのまま返すだけ。 |
| `getSwitchCompanionSystem()` | `mainSwitchCompanionSystem` をそのまま返すだけ。 |
| `getCharacterToReceiveOrders()` | `mainCharacterToReceiveOrders` をそのまま返すだけ。 |
| `getAIPatrolSystem()` | `mainAIPatrolSystem` をそのまま返すだけ。 |
| `getAIAroundManager()` | `mainAIAroundManager` をそのまま返すだけ。 |
| `getTurnBasedCombatTeamInfo()` | `mainTurnBasedCombatTeamInfo` をそのまま返すだけ。 |
| `getTurnBasedCombatActionsSystem()` | `mainTurnBasedCombatActionsSystem` をそのまま返すだけ。 |
| `getMatchPlayerToTargetSystem()` | `mainMatchPlayerToTargetSystem` をそのまま返すだけ。 |
| `getVehiclePassengerUnderwater()` | `mainVehiclePassengerUnderwater` をそのまま返すだけ。 |
| `getCharacterModelListManager()` | `mainCharacterModelListManager` をそのまま返すだけ。 |
