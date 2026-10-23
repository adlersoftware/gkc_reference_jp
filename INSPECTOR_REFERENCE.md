# インスペクター設定 日本語解説索引

カスタムエディタで表示される設定項目に、コードの使われ方から書いた日本語の一行説明を付けました。説明は各コンポーネントページの「インスペクター設定」表の「補足」列に入っています。

- 対象: **35 システム / 102 コンポーネント / 4,085 項目**

## システム一覧

| システム | コンポーネント | 項目数 |
| --- | --- | --- |
| [Player](#player) | 7 | 626 |
| [Weapons](#weapons) | 7 | 416 |
| [Devices](#devices) | 11 | 352 |
| [Camera](#camera) | 6 | 336 |
| [Vehicles](#vehicles) | 7 | 321 |
| [Grab Objects](#grab-objects) | 3 | 287 |
| [Map](#map) | 5 | 245 |
| [Inventory](#inventory) | 6 | 230 |
| [Gravity](#gravity) | 3 | 183 |
| [Input](#input) | 4 | 113 |
| [PickUps](#pickups) | 5 | 113 |
| [Health](#health) | 1 | 103 |
| [Combat System](#combat-system) | 1 | 88 |
| [Objectives Mission System](#objectives-mission-system) | 2 | 77 |
| [Powers](#powers) | 1 | 73 |
| [Experience System](#experience-system) | 1 | 61 |
| [Action System](#action-system) | 1 | 52 |
| [Others](#others) | 7 | 51 |
| [Hide System](#hide-system) | 1 | 40 |
| [Foot Step](#foot-step) | 1 | 38 |
| [Event System](#event-system) | 3 | 37 |
| [Head Track](#head-track) | 1 | 36 |
| [Game Manager](#game-manager) | 2 | 30 |
| [Skills System](#skills-system) | 2 | 30 |
| [AI](#ai) | 2 | 22 |
| [Dialog System](#dialog-system) | 1 | 20 |
| [Checkpoint](#checkpoint) | 1 | 15 |
| [Menu](#menu) | 1 | 15 |
| [Override System](#override-system) | 1 | 14 |
| [Tutorial System](#tutorial-system) | 2 | 14 |
| [Decal](#decal) | 2 | 13 |
| [Puzzles](#puzzles) | 1 | 11 |
| [Vendor System](#vendor-system) | 1 | 9 |
| [Stats System](#stats-system) | 1 | 7 |
| [Turn Based Combat](#turn-based-combat) | 1 | 7 |

## Player

プレイヤーの移動・状態・入力・IK・カメラ連携。

`Player/` — 7 コンポーネント / 626 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`playerController`](reference/Player/playerController.md) | 400 | `Player/playerController.cs` |
| [`ragdollActivator`](reference/Player/ragdollActivator.md) | 74 | `Player/ragdollActivator.cs` |
| [`usingDevicesSystem`](reference/Player/usingDevicesSystem.md) | 72 | `Player/usingDevicesSystem.cs` |
| [`playerStatesManager`](reference/Player/playerStatesManager.md) | 40 | `Player/playerStatesManager.cs` |
| [`buildPlayer`](reference/Player/buildPlayer.md) | 35 | `Player/Character Builder/buildPlayer.cs` |
| [`playerStateSystem`](reference/Player/playerStateSystem.md) | 4 | `Player/playerStateSystem.cs` |
| [`customCharacterControllerBaseBuilder`](reference/Player/customCharacterControllerBaseBuilder.md) | 1 | `Player/Generic Model Controller/customCharacterControllerBaseBuilder.cs` |

## Weapons

射撃・近接武器、IK、投射物、アタッチメント。

`Weapons/` — 7 コンポーネント / 416 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`playerWeaponsManager`](reference/Weapons/playerWeaponsManager.md) | 195 | `Weapons/playerWeaponsManager.cs` |
| [`IKWeaponSystem`](reference/Weapons/IKWeaponSystem.md) | 94 | `Weapons/IKWeaponSystem.cs` |
| [`playerWeaponSystem`](reference/Weapons/playerWeaponSystem.md) | 40 | `Weapons/playerWeaponSystem.cs` |
| [`weaponAttachmentSystem`](reference/Weapons/weaponAttachmentSystem.md) | 31 | `Weapons/Attachments/weaponAttachmentSystem.cs` |
| [`projectileSystem`](reference/Weapons/projectileSystem.md) | 28 | `Weapons/Projectiles/projectileSystem.cs` |
| [`weaponBuilder`](reference/Weapons/weaponBuilder.md) | 21 | `Weapons/weaponBuilder.cs` |
| [`weaponTransformInfoSystem`](reference/Weapons/weaponTransformInfoSystem.md) | 7 | `Weapons/weaponTransformInfoSystem.cs` |

## Devices

扉、端末、南京錠、エレベータ、固定カメラ、監視カメラ。

`Devices/` — 11 コンポーネント / 352 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`deviceStringAction`](reference/Devices/deviceStringAction.md) | 52 | `Devices/deviceStringAction.cs` |
| [`moveCameraToDevice`](reference/Devices/moveCameraToDevice.md) | 47 | `Devices/moveCameraToDevice.cs` |
| [`doorSystem`](reference/Devices/doorSystem.md) | 42 | `Devices/doorSystem.cs` |
| [`electronicDevice`](reference/Devices/electronicDevice.md) | 41 | `Devices/electronicDevice.cs` |
| [`waypointPlayerPathSystem`](reference/Devices/waypointPlayerPathSystem.md) | 36 | `Devices/waypointPlayerPathSystem.cs` |
| [`moveDeviceToCamera`](reference/Devices/moveDeviceToCamera.md) | 32 | `Devices/moveDeviceToCamera.cs` |
| [`waypointPlatform`](reference/Devices/waypointPlatform.md) | 29 | `Devices/waypointPlatform.cs` |
| [`lockedCameraSystem`](reference/Devices/lockedCameraSystem.md) | 26 | `Devices/lockedCameraSystem.cs` |
| [`simpleSwitch`](reference/Devices/simpleSwitch.md) | 20 | `Devices/simpleSwitch.cs` |
| [`elevatorSystem`](reference/Devices/elevatorSystem.md) | 18 | `Devices/elevatorSystem.cs` |
| [`closetSystem`](reference/Devices/closetSystem.md) | 9 | `Devices/closetSystem.cs` |

## Camera

視点、カメラステート、車両カメラ、カットシーン、エフェクト。

`Camera/` — 6 コンポーネント / 336 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`playerCamera`](reference/Camera/playerCamera.md) | 224 | `Camera/Player Camera/playerCamera.cs` |
| [`vehicleCameraController`](reference/Camera/vehicleCameraController.md) | 45 | `Camera/Vehicles/vehicleCameraController.cs` |
| [`cameraWaypointSystem`](reference/Camera/cameraWaypointSystem.md) | 30 | `Camera/Cutscene/cameraWaypointSystem.cs` |
| [`headBob`](reference/Camera/headBob.md) | 22 | `Camera/Player Camera/headBob.cs` |
| [`externalCameraShakeSystem`](reference/Camera/externalCameraShakeSystem.md) | 13 | `Camera/Player Camera/externalCameraShakeSystem.cs` |
| [`vehicleCameraShake`](reference/Camera/vehicleCameraShake.md) | 2 | `Camera/Vehicles/vehicleCameraShake.cs` |

## Vehicles

車両 HUD、運転 IK、車載武器、車種別コントローラ。

`Vehicles/` — 7 コンポーネント / 321 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`vehicleHUDManager`](reference/Vehicles/vehicleHUDManager.md) | 148 | `Vehicles/vehicleHUDManager.cs` |
| [`IKDrivingSystem`](reference/Vehicles/IKDrivingSystem.md) | 80 | `Vehicles/IKDrivingSystem.cs` |
| [`vehicleWeaponSystem`](reference/Vehicles/vehicleWeaponSystem.md) | 42 | `Vehicles/vehicleWeaponSystem.cs` |
| [`hoverBoardWayPoints`](reference/Vehicles/hoverBoardWayPoints.md) | 20 | `Vehicles/hoverBoardWayPoints.cs` |
| [`vehicleBuilder`](reference/Vehicles/vehicleBuilder.md) | 13 | `Vehicles/vehicleBuilder.cs` |
| [`WaypointCircuit`](reference/Vehicles/WaypointCircuit.md) | 9 | `Vehicles/AI/WaypointCircuit.cs` |
| [`vehicleInterface`](reference/Vehicles/vehicleInterface.md) | 9 | `Vehicles/vehicleInterface.cs` |

## Grab Objects

物を掴む・運ぶ・投げる・近接攻撃。

`Grab Objects/` — 3 コンポーネント / 287 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`grabbedObjectMeleeAttackSystem`](reference/Grab%20Objects/grabbedObjectMeleeAttackSystem.md) | 126 | `Grab Objects/grabbedObjectMeleeAttackSystem.cs` |
| [`grabObjects`](reference/Grab%20Objects/grabObjects.md) | 121 | `Grab Objects/grabObjects.cs` |
| [`putObjectSystem`](reference/Grab%20Objects/putObjectSystem.md) | 40 | `Grab Objects/putObjectSystem.cs` |

## Map

マップ生成・表示・マップオブジェクト。

`Map/` — 5 コンポーネント / 245 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`mapSystem`](reference/Map/mapSystem.md) | 129 | `Map/mapSystem.cs` |
| [`mapObjectInformation`](reference/Map/mapObjectInformation.md) | 50 | `Map/mapObjectInformation.cs` |
| [`mapCreator`](reference/Map/mapCreator.md) | 39 | `Map/mapCreator.cs` |
| [`mapTileBuilder`](reference/Map/mapTileBuilder.md) | 26 | `Map/mapTileBuilder.cs` |
| [`mapZoneUnlocker`](reference/Map/mapZoneUnlocker.md) | 1 | `Map/mapZoneUnlocker.cs` |

## Inventory

所持品、装備、銀行、通貨、重量、UI。

`Inventory/` — 6 コンポーネント / 230 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`inventoryManager`](reference/Inventory/inventoryManager.md) | 144 | `Inventory/inventoryManager.cs` |
| [`useInventoryObject`](reference/Inventory/useInventoryObject.md) | 33 | `Inventory/useInventoryObject.cs` |
| [`inventoryBankSystem`](reference/Inventory/inventoryBankSystem.md) | 27 | `Inventory/inventoryBankSystem.cs` |
| [`inventoryListManager`](reference/Inventory/inventoryListManager.md) | 17 | `Inventory/inventoryListManager.cs` |
| [`inventoryBankManager`](reference/Inventory/inventoryBankManager.md) | 6 | `Inventory/inventoryBankManager.cs` |
| [`inventoryMenuPanelsSystem`](reference/Inventory/inventoryMenuPanelsSystem.md) | 3 | `Inventory/inventoryMenuPanelsSystem.cs` |

## Gravity

重力方向の変更、無重力エリア、車両の重力制御。

`Gravity/` — 3 コンポーネント / 183 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`gravitySystem`](reference/Gravity/gravitySystem.md) | 86 | `Gravity/gravitySystem.cs` |
| [`zeroGravityRoomSystem`](reference/Gravity/zeroGravityRoomSystem.md) | 49 | `Gravity/zeroGravityRoomSystem.cs` |
| [`setGravity`](reference/Gravity/setGravity.md) | 48 | `Gravity/setGravity.cs` |

## Input

キー割り当て、アクション判定、タッチ、カーソル。

`Input/` — 4 コンポーネント / 113 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`playerInputManager`](reference/Input/playerInputManager.md) | 47 | `Input/playerInputManager.cs` |
| [`inputManager`](reference/Input/inputManager.md) | 39 | `Input/inputManager.cs` |
| [`inputActionManager`](reference/Input/inputActionManager.md) | 20 | `Input/inputActionManager.cs` |
| [`playerInputPanelSystem`](reference/Input/playerInputPanelSystem.md) | 7 | `Input/playerInputPanelSystem.cs` |

## PickUps

`PickUps/` — 5 コンポーネント / 113 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`pickUpObject`](reference/PickUps/pickUpObject.md) | 41 | `PickUps/pickUpObject.cs` |
| [`chestSystem`](reference/PickUps/chestSystem.md) | 33 | `PickUps/chestSystem.cs` |
| [`dropPickUpSystem`](reference/PickUps/dropPickUpSystem.md) | 21 | `PickUps/dropPickUpSystem.cs` |
| [`pickUpsScreenInfo`](reference/PickUps/pickUpsScreenInfo.md) | 17 | `PickUps/pickUpsScreenInfo.cs` |
| [`pickUpManager`](reference/PickUps/pickUpManager.md) | 1 | `PickUps/pickUpManager.cs` |

## Health

体力・シールド・HP バー・被弾演出。

`Health/` — 1 コンポーネント / 103 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`health`](reference/Health/health.md) | 103 | `Health/health.cs` |

## Combat System

近接武器、素手コンボ、投擲、スライス、盾。

`Combat System/` — 1 コンポーネント / 88 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`closeCombatSystem`](reference/Combat%20System/closeCombatSystem.md) | 88 | `Combat System/closeCombatSystem.cs` |

## Objectives Mission System

ミッション、目標ログ、目標ステーション UI。

`Objectives Mission System/` — 2 コンポーネント / 77 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`objectiveEventSystem`](reference/Objectives%20Mission%20System/objectiveEventSystem.md) | 75 | `Objectives Mission System/objectiveEventSystem.cs` |
| [`screenObjectivesSystem`](reference/Objectives%20Mission%20System/screenObjectivesSystem.md) | 2 | `Objectives Mission System/screenObjectivesSystem.cs` |

## Powers

テレキネシス、時間操作、重力操作などの特殊能力。

`Powers/` — 1 コンポーネント / 73 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`otherPowers`](reference/Powers/otherPowers.md) | 73 | `Powers/otherPowers.cs` |

## Experience System

`Experience System/` — 1 コンポーネント / 61 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`playerExperienceSystem`](reference/Experience%20System/playerExperienceSystem.md) | 61 | `Experience System/playerExperienceSystem.cs` |

## Action System

汎用アクション、共有アクション。

`Action System/` — 1 コンポーネント / 52 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`actionSystem`](reference/Action%20System/actionSystem.md) | 52 | `Action System/actionSystem.cs` |

## Others

共通ユーティリティ、スポナー、スキャナー、UI 補助。

`Others/` — 7 コンポーネント / 51 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`consoleMode`](reference/Others/consoleMode.md) | 30 | `Others/Console Mode/consoleMode.cs` |
| [`BezierSpline`](reference/Others/BezierSpline.md) | 9 | `Others/BezierSpline.cs` |
| [`playerOptionsEditorSystem`](reference/Others/playerOptionsEditorSystem.md) | 4 | `Others/playerOptionsEditorSystem.cs` |
| [`tagLayerSystem`](reference/Others/tagLayerSystem.md) | 3 | `Others/tagLayerSystem.cs` |
| [`GKCUIManager`](reference/Others/GKCUIManager.md) | 2 | `Others/GKCUIManager.cs` |
| [`nonEssentialCharacterElementsManager`](reference/Others/nonEssentialCharacterElementsManager.md) | 2 | `Others/nonEssentialCharacterElementsManager.cs` |
| [`featuresManager`](reference/Others/featuresManager.md) | 1 | `Others/featuresManager.cs` |

## Hide System

`Hide System/` — 1 コンポーネント / 40 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`hideCharacterFixedPlaceSystem`](reference/Hide%20System/hideCharacterFixedPlaceSystem.md) | 40 | `Hide System/hideCharacterFixedPlaceSystem.cs` |

## Foot Step

`Foot Step/` — 1 コンポーネント / 38 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`footStepManager`](reference/Foot%20Step/footStepManager.md) | 38 | `Foot Step/footStepManager.cs` |

## Event System

`Event System/` — 3 コンポーネント / 37 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`eventTriggerSystem`](reference/Event%20System/eventTriggerSystem.md) | 23 | `Event System/eventTriggerSystem.cs` |
| [`eventInfoSystem`](reference/Event%20System/eventInfoSystem.md) | 8 | `Event System/eventInfoSystem.cs` |
| [`remoteEventSystem`](reference/Event%20System/remoteEventSystem.md) | 6 | `Event System/remoteEventSystem.cs` |

## Head Track

`Head Track/` — 1 コンポーネント / 36 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`headTrack`](reference/Head%20Track/headTrack.md) | 36 | `Head Track/headTrack.cs` |

## Game Manager

ゲーム全体の管理（ポーズ、設定、シーン）。

`Game Manager/` — 2 コンポーネント / 30 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`playerCharactersManager`](reference/Game%20Manager/playerCharactersManager.md) | 24 | `Game Manager/playerCharactersManager.cs` |
| [`prefabsManager`](reference/Game%20Manager/prefabsManager.md) | 6 | `Game Manager/prefabsManager.cs` |

## Skills System

`Skills System/` — 2 コンポーネント / 30 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`playerSkillsUISystem`](reference/Skills%20System/playerSkillsUISystem.md) | 23 | `Skills System/playerSkillsUISystem.cs` |
| [`playerSkillsSystem`](reference/Skills%20System/playerSkillsSystem.md) | 7 | `Skills System/playerSkillsSystem.cs` |

## AI

索敵、ナビゲーション、攻撃ブレイン、ファクション。

`AI/` — 2 コンポーネント / 22 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`AIWayPointPatrol`](reference/AI/AIWayPointPatrol.md) | 11 | `AI/AIWayPointPatrol.cs` |
| [`characterFactionManager`](reference/AI/characterFactionManager.md) | 11 | `AI/Faction/characterFactionManager.cs` |

## Dialog System

`Dialog System/` — 1 コンポーネント / 20 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`dialogContentSystem`](reference/Dialog%20System/dialogContentSystem.md) | 20 | `Dialog System/dialogContentSystem.cs` |

## Checkpoint

`Checkpoint/` — 1 コンポーネント / 15 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`checkpointSystem`](reference/Checkpoint/checkpointSystem.md) | 15 | `Checkpoint/checkpointSystem.cs` |

## Menu

ポーズメニュー、インゲームメニュー、シーンロード。

`Menu/` — 1 コンポーネント / 15 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`sceneLoadSystem`](reference/Menu/sceneLoadSystem.md) | 15 | `Menu/sceneLoadSystem.cs` |

## Override System

`Override System/` — 1 コンポーネント / 14 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`overrideInputManager`](reference/Override%20System/overrideInputManager.md) | 14 | `Override System/overrideInputManager.cs` |

## Tutorial System

`Tutorial System/` — 2 コンポーネント / 14 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`playerTutorialSystem`](reference/Tutorial%20System/playerTutorialSystem.md) | 10 | `Tutorial System/playerTutorialSystem.cs` |
| [`tutorialUISystem`](reference/Tutorial%20System/tutorialUISystem.md) | 4 | `Tutorial System/tutorialUISystem.cs` |

## Decal

`Decal/` — 2 コンポーネント / 13 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`decalManager`](reference/Decal/decalManager.md) | 7 | `Decal/decalManager.cs` |
| [`decalTypeInformation`](reference/Decal/decalTypeInformation.md) | 6 | `Decal/decalTypeInformation.cs` |

## Puzzles

`Puzzles/` — 1 コンポーネント / 11 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`pressObjectsInOrderSystem`](reference/Puzzles/pressObjectsInOrderSystem.md) | 11 | `Puzzles/pressObjectsInOrderSystem.cs` |

## Vendor System

`Vendor System/` — 1 コンポーネント / 9 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`vendorSystem`](reference/Vendor%20System/vendorSystem.md) | 9 | `Vendor System/vendorSystem.cs` |

## Stats System

`Stats System/` — 1 コンポーネント / 7 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`playerStatsSystem`](reference/Stats%20System/playerStatsSystem.md) | 7 | `Stats System/playerStatsSystem.cs` |

## Turn Based Combat

ターン制戦闘の進行とコマンド選択。

`Turn Based Combat/` — 1 コンポーネント / 7 項目

| コンポーネント | 項目数 | ソース |
| --- | --- | --- |
| [`turnBasedCombatSystem`](reference/Turn%20Based%20Combat/turnBasedCombatSystem.md) | 7 | `Turn Based Combat/turnBasedCombatSystem.cs` |

## 読み方

- 「補足」列の先頭が日本語説明で、その後に `[Tooltip]` や表示条件が続きます。

- 「表示条件」は、そのチェックがオンのときだけ表示される項目です。

- 未使用の項目は「実行時参照なし」などと明記しています。

