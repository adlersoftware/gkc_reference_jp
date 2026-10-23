# adjustCharacterHeightSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Character Builder/adjustCharacterHeightSystem.cs:6`

**概要**: キャラクターの身長に合わせて、モデル/カプセル/武器/カメラピボット/追加コライダーなどを一括調整するコンポーネント。エディタと実行時の両方で使える。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Adjust Character Height | `adjustCharacterHeight` | `bool` | – | – |
| Character Height | `characterHeight` | `float` | 2 | – |
| Set Character Model Scale | `setCharacterModelScale` | `bool` | – | – |
| Character Model Scale | `characterModelScale` | `float` | 1 | – |
| Reset Mount Point Local Positions | `resetMountPointLocalPositions` | `bool` | – | – |
| Capsule Height | `capsuleHeight` | `float` | 2 | – |
| Capsule Radius | `capsuleRadius` | `float` | 0.3f | – |
| Capsule Height On Crouch | `capsuleHeightOnCrouch` | `float` | 1 | – |
| Character Radius | `characterRadius` | `float` | – | – |
| Enable Head Track | `enableHeadTrack` | `bool` | – | – |

### Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera State Height Info List | `cameraStateHeightInfoList` | `List<cameraStateHeightInfo>` | new List<cameraStateHeightInfo> () | – |

### Character Transform Parts Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Transform Part Info List | `transformPartInfoList` | `List<transformPartInfo>` | new List<transformPartInfo> () | – |

### Fire Weapons Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Apply Scale To Fire Weapons | `applyScaleToFireWeapons` | `bool` | – | – |
| Scale For Fire Weapons | `scaleForFireWeapons` | `float` | – | – |
| Offset Parent Third Person | `offsetParentThirdPerson` | `Vector3` | – | – |
| Set Fixed Offset Parent Third Person | `setFixedOffsetParentThirdPerson` | `bool` | – | – |
| Fixed Offset Parent Third Person | `fixedOffsetParentThirdPerson` | `Vector3` | – | – |
| Fire Weapon Transform Reference Scale | `fireWeaponTransformReferenceScale` | `float` | 1 | – |

### Melee Weapons Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Apply Scale To Melee Wapons | `applyScaleToMeleeWapons` | `bool` | – | – |
| Scale For Melee Weapons | `scaleForMeleeWeapons` | `float` | – | – |
| Place Trigger In Front Of Character On All Melee Attacks | `placeTriggerInFrontOfCharacterOnAllMeleeAttacks` | `bool` | – | – |
| Use Extra Trigger Multiplier Scale On All Melee Attacks Active | `useExtraTriggerMultiplierScaleOnAllMeleeAttacksActive` | `bool` | – | – |
| Extra Trigger Multiplier Scale On All Melee Attacks Amount | `extraTriggerMultiplierScaleOnAllMeleeAttacksAmount` | `float` | – | – |

### Close Combat Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Close Combat Trigger Radius | `setNewCloseCombatTriggerRadius` | `bool` | – | – |
| New Close Combat Trigger Radius | `newCloseCombatTriggerRadius` | `float` | – | – |
| Place Trigger In Front Of Character On All Close Combat Attacks | `placeTriggerInFrontOfCharacterOnAllCloseCombatAttacks` | `bool` | – | – |

### AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Is AI | `characterIsAI` | `bool` | – | – |
| Character Uses Extra Colliders | `characterUsesExtraColliders` | `bool` | – | – |
| Extra Collider List | `extraColliderList` | `List<Collider>` | new List<Collider> () | – |
| Use New Min Distance To Target | `useNewMinDistanceToTarget` | `bool` | – | – |
| New Min Distance To Enemy Using Close Combat | `newMinDistanceToEnemyUsingCloseCombat` | `float` | – | – |
| New Min Distance To Close Combat | `newMinDistanceToCloseCombat` | `float` | – | – |
| New Min Distance To Melee | `newMinDistanceToMelee` | `float` | – | – |
| New Min Distance To Enemy Using Melee | `newMinDistanceToEnemyUsingMelee` | `float` | – | – |
| Set New Agent Radius | `setNewAgentRadius` | `bool` | – | – |
| New Agent Radius | `newAgentRadius` | `float` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Components Manager | `mainPlayerComponentsManager` | `playerComponentsManager` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Melee Weapons Grabbed Manager | `mainMeleeWeaponsGrabbedManager` | `meleeWeaponsGrabbedManager` | – | – |
| Main Body Mount Point System | `mainBodyMountPointSystem` | `bodyMountPointsSystem` | – | – |
| Main Build Player | `mainBuildPlayer` | `buildPlayer` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |
| Main IK System | `mainIKSystem` | `IKSystem` | – | – |
| Main Health | `mainHealth` | `health` | – | – |
| Main Close Combat System | `mainCloseCombatSystem` | `closeCombatSystem` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main AI Navmesh | `mainAINavmesh` | `AINavMesh` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `adjustHeightValueInRuntime()` | 実行中フラグを立てて身長・カメラ・武器スケールを調整し、設定時は武器オフセットと参照位置も調整してフラグを戻す。 |
| `adjustHeightValue()` | モデル、マウントポイント、武器、カプセル、頭追従、NavMesh、追加コライダー、近接設定をまとめて更新する。 |
| `adjustFireWeaponsScale()` | 設定時、全射撃武器のメッシュスケールを設定し、エディタ時は `updateComponent` を呼ぶ。 |
| `adjustFireWeaponsOffset()` | 三人称オフセット値を設定して全射撃武器の位置を調整し、エディタ時は `updateComponent` を呼ぶ。 |
| `adjustFireWeaponsTransformReferences()` | 全射撃武器の参照Transform位置をスケールで調整し、エディタ時は更新する。 |
| `adjustCameraStates()` | カメラ状態ごとのピボットYを身長割合から再計算し、現在のカメラ状態のピボット位置にも反映する。 |

## 内部型

- `transformPartInfo`（class）
- `cameraStateHeightInfo`（class）
