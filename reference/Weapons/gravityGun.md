# gravityGun

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/New Weapon Behaviors/gravityGun.cs:7`

**概要**: カメラ前方のレイキャストで掴めるオブジェクトを検出し、`Rigidbody`の重力や回転固定を切り替えて保持・投擲・重力変更を行う武器コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hold Distance | `holdDistance` | `float` | 3 | – |
| Max Distance Held | `maxDistanceHeld` | `float` | 4 | – |
| Max Distance Grab | `maxDistanceGrab` | `float` | 10 | – |
| Hold Speed | `holdSpeed` | `float` | 10 | – |
| Rotation Speed | `rotationSpeed` | `float` | – | – |
| Current Grab Mode | `currentGrabMode` | `grabMode` | – | – |
| Grabbed Object Tag | `grabbedObjectTag` | `string` | – | – |
| Grabbed Object Layer | `grabbedObjectLayer` | `string` | – | – |
| Layer | `layer` | `LayerMask` | – | – |
| Gravity Objects Layer | `gravityObjectsLayer` | `LayerMask` | – | – |
| Layer For Custom Gravity Object | `layerForCustomGravityObject` | `string` | – | – |
| Change Gravity Objects Enabled | `changeGravityObjectsEnabled` | `bool` | true | – |
| Able To Grab Tags | `ableToGrabTags` | `List<string>` | new List<string> () | – |
| Rotor Rotation Speed | `rotorRotationSpeed` | `float` | 20 | – |
| Rotor Rotation Speed On Throw Charge | `rotorRotationSpeedOnThrowCharge` | `float` | 40 | – |

### Throw Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Min Time To Increase Throw Force | `minTimeToIncreaseThrowForce` | `float` | 300 | – |
| Increase Throw Force Speed | `increaseThrowForceSpeed` | `float` | 1500 | – |
| Extra Thorw Force | `extraThorwForce` | `float` | 10 | – |
| Max Throw Force | `maxThrowForce` | `float` | 3500 | – |
| Power Force Mode | `powerForceMode` | `ForceMode` | – | – |
| Use Throw Objects Layer | `useThrowObjectsLayer` | `bool` | true | – |
| Throw Objects Layer To Check | `throwObjectsLayerToCheck` | `LayerMask` | – | – |
| Throw Power | `throwPower` | `float` | – | – |
| Realistic Force Mode | `realisticForceMode` | `ForceMode` | – | – |

### Grab In Fixed Position Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grab In Fixed Position | `grabInFixedPosition` | `bool` | – | – |
| Rotate To Camera In Fixed Position | `rotateToCameraInFixedPosition` | `bool` | – | – |
| Rotate To Camera In Free Position | `rotateToCameraInFreePosition` | `bool` | – | – |
| Closest Hold Distance In Fixed Position | `closestHoldDistanceInFixedPosition` | `float` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remote Event Name List On Grab Object | `remoteEventNameListOnGrabObject` | `List<string>` | new List<string> () | – |
| Remote Event Name List On Drop Object | `remoteEventNameListOnDropObject` | `List<string>` | new List<string> () | – |

### Drop Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Force When Object Dropped | `useForceWhenObjectDropped` | `bool` | – | – |
| Use Force When Object Dropped On First Person | `useForceWhenObjectDroppedOnFirstPerson` | `bool` | – | – |
| Use Force When Object Dropped On Third Person | `useForceWhenObjectDroppedOnThirdPerson` | `bool` | – | – |
| Force When Object Dropped On First Person | `forceWhenObjectDroppedOnFirstPerson` | `float` | – | – |
| Force When Object Dropped On Third Person | `forceWhenObjectDroppedOnThirdPerson` | `float` | – | – |

### Transparency Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Alpha Transparency | `alphaTransparency` | `float` | 0.5f | – |
| Enable Transparency | `enableTransparency` | `bool` | true | – |
| Pickable Shader | `pickableShader` | `Shader` | – | – |

### Noise Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Launched Objects Can Make Noise | `launchedObjectsCanMakeNoise` | `bool` | – | – |
| Min Object Speed To Activate Noise | `minObjectSpeedToActivateNoise` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Can Use Weapon | `canUseWeapon` | `bool` | true | – |
| Object Is Vehicle | `objectIsVehicle` | `bool` | – | – |
| Object Focus | `objectFocus` | `bool` | – | – |
| Grabbed | `grabbed` | `bool` | – | – |
| Current Max Distance Held | `currentMaxDistanceHeld` | `float` | – | – |
| Current Distance To Grabbed Object | `currentDistanceToGrabbedObject` | `float` | – | – |
| Charging Throw Object | `chargingThrowObject` | `bool` | – | – |
| Object Held | `objectHeld` | `GameObject` | – | – |
| Current Object To Grab Found | `currentObjectToGrabFound` | `GameObject` | – | – |
| Weapon Active | `weaponActive` | `bool` | – | – |

### Main Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Object Found | `useEventOnObjectFound` | `bool` | – | – |
| Event On Object Found | `eventOnObjectFound` | `UnityEvent` | – | – |
| Event On Object Lost | `eventOnObjectLost` | `UnityEvent` | – | – |
| Use Event On Object Grabbed Dropped | `useEventOnObjectGrabbedDropped` | `bool` | – | – |
| Event On Object Grabbed | `eventOnObjectGrabbed` | `UnityEvent` | – | – |
| Event On Object Dropped | `eventOnObjectDropped` | `UnityEvent` | – | – |
| Use Event On Launch Objects | `useEventOnLaunchObjects` | `bool` | – | – |
| Event On Launch Objects | `eventOnLaunchObjects` | `UnityEvent` | – | – |
| Use Event On Change Gravity Gun Active State | `useEventOnChangeGravityGunActiveState` | `bool` | – | – |
| Event On Gravity Gun Active | `eventOnGravityGunActive` | `UnityEvent` | – | – |
| Event On Gravity Gun Deactivate | `eventOnGravityGunDeactivate` | `UnityEvent` | – | – |

### Secondary Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Secondary Function Event Press Down | `secondaryFunctionEventPressDown` | `UnityEvent` | – | – |
| Secondary Function Event Press | `secondaryFunctionEventPress` | `UnityEvent` | – | – |
| Secondary Function Event Press Up | `secondaryFunctionEventPressUp` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | – |
| Main Player Weapon System | `mainPlayerWeaponSystem` | `playerWeaponSystem` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Animation System | `animationSystem` | `simpleAnimationSystem` | – | – |
| Power Slider | `powerSlider` | `Slider` | – | – |
| Use Rotor | `useRotor` | `bool` | true | – |
| Rotor | `rotor` | `Transform` | – | – |
| Grab Zone Transform | `grabZoneTransform` | `Transform` | – | – |
| High Friction Material | `highFrictionMaterial` | `PhysicsMaterial` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkObjectFoundOrLostState()` | オブジェクト検出イベントが有効なら、`objectFocus`に応じて発見・見失いイベントを呼び分けるだけ。 |
| `grabObject()` | カメラ前方へ`maxDistanceGrab`までレイキャストし、対象を検出済みなら`grabCurrenObject`で掴む。 |
| `grabCurrenObject(GameObject objectToGrab)` | 対象の種類を判定して保持し、タグ・レイヤー退避、重力と回転固定の変更、各イベント呼び出しを行う。 |
| `checkTypeObject(GameObject objectToCheck)` | 掴めるタグか車両か、`characterDamageReceiver`のキャラか`grabObjectParent`付きかを判定して返す。 |
| `dropObject()` | 保持を解除してタグ・レイヤー・重力・回転固定を復元し、各種イベント呼び出しと参照クリアを行う。 |
| `checkJointsInObject(GameObject objectToThrow, float force)` | `CharacterJoint`があれば接続先へ再帰し、最終的な`Rigidbody`に力を加える。 |
| `addForceToThrownRigidbody(GameObject objectToThrow, float force)` | 配下の非キネマティックな`Rigidbody`すべてに質量考慮の力を加え、速度に応じて衝突ノイズを有効化する。 |
| `throwRealisticGrabbedObject()` | 保持オブジェクトをドロップしてから`throwPower`と質量に応じた力を加え、ノイズ判定を行う。 |
| `resetFixedGrabedTransformPosition()` | 固定保持位置の移動コルーチンを止めてから、元の保持距離へ戻すコルーチンを開始する。 |
| `stopResetFixedGrabedTransformPositionCoroutine()` | 固定保持位置の移動コルーチンを停止するだけ。 |
| `checkIfDropObject(GameObject objectToCheck)` | 保持中のオブジェクトが引数と一致する場合のみ`dropObject`を呼ぶ。 |
| `setWeaponActiveState(bool state)` | 武器の有効状態を設定して初期化とドロップを行い、有効・無効に応じたイベントを発火する。 |
| `getGrabbedObject()` | 保持中のオブジェクトを返すだけ。 |
| `isGrabbedObject()` | 保持中かどうかを返すだけ。 |
| `checkIfEnableNoiseOnCollision(GameObject objectToCheck, float launchSpeed)` | 投擲速度が閾値以上なら対象の`noiseSystem`のノイズ使用を有効にする。 |
| `addForceToLaunchObject()` | `powers`モードのとき、長押し時間に応じて`powerSlider`と`holdTimer`を増やしてチャージ状態にする。 |
| `launchObject()` | チャージ量に応じて対象をドロップし、力を加えて投擲し、`launchedObjects`の付与やイベント発火を行う。 |
| `isCurrentObjectToGrabFound(GameObject objectToCheck)` | 引数が現在の検出対象と一致するかを返すだけ。 |
| `inputGrabObject()` | デバイス未使用・武器有効・非保持・使用可能の条件で`grabObject`を呼ぶ。 |
| `inputHoldToLaunchObject()` | 保持中かつ武器有効なら`addForceToLaunchObject`でチャージを進めるだけ。 |
| `inputReleaseToLaunchObject()` | 武器有効時、保持中なら`launchObject`で投擲し、保持有無に応じたイベントを発火する。 |
| `inputResetFixedGrabedTransformPosition()` | 保持中かつ武器有効なら固定保持位置のリセットを実行する。 |
| `activateSecondaryFunctionPressDown()` | 武器有効なら`secondaryFunctionEventPressDown`を発火するだけ。 |
| `activateSecondaryFunctionPress()` | 武器有効なら`secondaryFunctionEventPress`を発火するだけ。 |
| `activateSecondaryFunctionPressUp()` | 武器有効なら`secondaryFunctionEventPressUp`を発火するだけ。 |
| `setNewGravityToGrabbedObject()` | 重力変更が有効なら保持を解除し、車両は重力制御、通常物は`artificialObjectGravity`を付与して前方へ重力を向ける。 |
| `isCarryingObject()` | `grabbed`フラグを返すだけ。 |
| `setCanUseWeaponState(bool state)` | 使用可否を設定して初期化し、使用不可なら保持解除と対象検出のリセットを行う。 |
| `rotateRotor(float newSpeed)` | ローターが有効ならZ軸周りに`Time.deltaTime * newSpeed`で回転させるだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnObjectFound` | `UnityEvent` | – |
| `eventOnObjectLost` | `UnityEvent` | – |
| `eventOnObjectGrabbed` | `UnityEvent` | – |
| `eventOnObjectDropped` | `UnityEvent` | – |
| `eventOnLaunchObjects` | `UnityEvent` | – |
| `eventOnGravityGunActive` | `UnityEvent` | – |
| `eventOnGravityGunDeactivate` | `UnityEvent` | – |
| `secondaryFunctionEventPressDown` | `UnityEvent` | – |
| `secondaryFunctionEventPress` | `UnityEvent` | – |
| `secondaryFunctionEventPressUp` | `UnityEvent` | – |

## 内部型

- `grabMode`（enum）
