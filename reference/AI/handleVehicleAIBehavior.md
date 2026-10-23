# handleVehicleAIBehavior

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `AIBehaviorInfo`
- **ソース**: `AI/Custom AI Behavior/handleVehicleAIBehavior.cs:6`

**概要**: AIが車両を探して乗り降りする行動を扱う。更新コルーチンで車両探索・搭乗・降車を監視し、`usingDevicesManager`経由で運転席に乗せる。

## インスペクター設定

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Character On Vehicle | `characterOnVehicle` | `bool` | – | – |

### Custom Driver Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Search Vehicle Enabled | `searchVehicleEnabled` | `bool` | true | – |
| Start Game Searching For Vehicle | `startGameSearchingForVehicle` | `bool` | – | – |
| Set Vehicle To Start | `setVehicleToStart` | `bool` | – | – |
| Vehicle To Start | `vehicleToStart` | `GameObject` | – | – |
| Use Max Distance To Get Vehicle | `useMaxDistanceToGetVehicle` | `bool` | – | – |
| Max Distance To Get Vehicle | `maxDistanceToGetVehicle` | `float` | – | – |
| Min Distance To Get On Current Vehicle | `minDistanceToGetOnCurrentVehicle` | `float` | 3.5f | – |
| Ignore Check Vehicle If Target To Attack Found | `ignoreCheckVehicleIfTargetToAttackFound` | `bool` | – | – |
| Stop Behavior Update On Get Off From Vehicle | `stopBehaviorUpdateOnGetOffFromVehicle` | `bool` | true | – |
| Stop Behavior Update On Vehicle Reached | `stopBehaviorUpdateOnVehicleReached` | `bool` | true | – |

### AI Driver Debug Info

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Searching Vehicle | `searchingVehicle` | `bool` | – | – |
| Vehicle To Reach Found | `vehicleToReachFound` | `bool` | – | – |
| Current Vehicle AI Navmesh Located | `currentVehicleAINavmeshLocated` | `bool` | – | – |
| Get Off From Vehicle On Destiny Reached | `getOffFromVehicleOnDestinyReached` | `bool` | – | – |
| Current Vehicle To Get | `currentVehicleToGet` | `Transform` | – | – |
| Current Vehicle AI Nav Mesh | `currentVehicleAINavMesh` | `vehicleAINavMesh` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On No Vehicle To Pick From Scene | `useEventOnNoVehicleToPickFromScene` | `bool` | – | – |
| Event On No Vehicle To Pick From Scene | `eventOnNoVehicleToPickFromScene` | `UnityEvent` | – | – |

### Custom Passenger Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check AI Passenger State Enabled | `checkAIPassengerStateEnabled` | `bool` | true | – |
| Ignore Check Partner On Vehicle | `ignoreCheckPartnerOnVehicle` | `bool` | – | – |

### AI Passenger Debug Info

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Vehicle HUD Manager | `currentVehicleHUDManager` | `vehicleHUDManager` | – | – |
| Current Vehicle To Attack | `currentVehicleToAttack` | `vehicleHUDManager` | – | – |
| Current Vehicle | `currentVehicle` | `GameObject` | – | – |
| Player Controller Partner | `playerControllerPartner` | `playerController` | – | – |
| AI Character Wasnt Able To Enter On Partner Vehicle | `AICharacterWasntAbleToEnterOnPartnerVehicle` | `bool` | – | – |
| Partner Found | `partnerFound` | `bool` | – | – |
| Following Partner Driving On Foot | `followingPartnerDrivingOnFoot` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| AI Transform | `AITransform` | `Transform` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main AI Navmesh Manager | `mainAINavmeshManager` | `AINavMesh` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Using Devices Manager | `usingDevicesManager` | `usingDevicesSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`があれば停止するだけ。 |
| `setGetOffFromVehicleOnDestinyReachedState(bool state)` | `getOffFromVehicleOnDestinyReached`を設定するだけ。 |
| `setIgnoreCheckPartnerOnVehicleState(bool state)` | `ignoreCheckPartnerOnVehicle`を設定するだけ。 |
| `setCheckAIPassengerStateEnabledState(bool state)` | `checkAIPassengerStateEnabled`を設定するだけ。 |
| `enterOnVehicle(GameObject newVehicleObject)` | `pauseAI`で移動を止め、`usingDevicesManager`で車両を搭乗デバイスとして使用し、結果に応じて搭乗状態を更新する。 |
| `isCharacterOnVehicle()` | `characterOnVehicle`を返すだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnNoVehicleToPickFromScene` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`activateAIBehavior()`, `deactivateAIBehavior()`, `getOffFromVehicle()`, `removeStateOnVehicle()`, `setAICharacterOnVehicle(GameObject newVehicle)`, `setCurrentPlayerControllerPartner(playerController newPlayerController)`, `setSystemActiveState(bool state)`, `setWaitToActivateAttackActiveState(bool state)`, `updateAI()`, `updateAIAttackState(bool canUseAttack)`, `updateAIBehaviorState()`, `updateAIPassengerBehavior()`

</details>
