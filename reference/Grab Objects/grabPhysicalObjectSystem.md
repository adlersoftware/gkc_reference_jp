# grabPhysicalObjectSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Grab Objects/grabPhysicalObjectSystem.cs:6`

**概要**: 掴める物理オブジェクト側に付き、プレイヤーの`grabObjects`へ検出・掴み・ドロップを通知するコンポーネント。質量やレイヤー、キネマティック、IK/アニメ設定、イベントやリモートイベントを掴み状態に応じて切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grab Object Physically | `grabObjectPhysically` | `bool` | true | – |
| Object Name | `objectName` | `string` | – | – |
| Layer For Users | `layerForUsers` | `LayerMask` | – | – |
| Collider Scale | `colliderScale` | `Vector3` | – | – |
| Collider Offset | `colliderOffset` | `Vector3` | – | – |
| Tag For Object When Active | `tagForObjectWhenActive` | `string` | – | – |
| Tag For Object When Inactive | `tagForObjectWhenInactive` | `string` | – | – |
| Carry Object Out Of Player Body | `carryObjectOutOfPlayerBody` | `bool` | – | – |
| Disable Object Collider While Grabbed | `disableObjectColliderWhileGrabbed` | `bool` | – | – |
| Ignore To Grab Physically If Picked With Aiming Mode | `ignoreToGrabPhysicallyIfPickedWithAimingMode` | `bool` | – | – |

### Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Rigidbody Mass Value | `setRigidbodyMassValue` | `bool` | – | – |
| Rigidbody Mass Value | `rigidbodyMassValue` | `float` | 1 | – |
| Set Custom Layer On Colliders On Grab | `setCustomLayerOnCollidersOnGrab` | `bool` | – | – |
| Custom Layer On Colliders On Grab | `customLayerOnCollidersOnGrab` | `string` | – | – |
| Use Custom Rigidbodies Parent | `useCustomRigidbodiesParent` | `bool` | – | – |
| Custom Rigidbodies Parent | `customRigidbodiesParent` | `Transform` | – | – |

### Grab Object Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Animation Speed | `changeAnimationSpeed` | `bool` | – | – |
| Animation Speed | `animationSpeed` | `float` | 1 | Range (0, 1) |
| Set New Movement Tree ID | `setNewMovementTreeID` | `bool` | – | – |
| New Movement Tree ID | `newMovementTreeID` | `int` | – | – |
| Apply Animator Velocity Without Moving | `applyAnimatorVelocityWithoutMoving` | `bool` | – | – |
| Disable Jump On Grabbed Object | `disableJumpOnGrabbedObject` | `bool` | – | – |
| Disable Run On Grabbed Object | `disableRunOnGrabbedObject` | `bool` | – | – |
| Disable Crouch On Grabbed Objet | `disableCrouchOnGrabbedObjet` | `bool` | – | – |

### Grab Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check View To Grab Object | `checkViewToGrabObject` | `bool` | – | – |
| Can Be Grabbed On First Person | `canBeGrabbedOnFirstPerson` | `bool` | true | – |
| Can Be Grabbed On Third Person | `canBeGrabbedOnThirdPerson` | `bool` | true | – |

### Transform Reference Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Reference Position | `referencePosition` | `Transform` | – | – |
| Use Reference Position For Every View | `useReferencePositionForEveryView` | `bool` | – | – |
| Reference Position Third Person | `referencePositionThirdPerson` | `Transform` | – | – |
| Reference Position First Person | `referencePositionFirstPerson` | `Transform` | – | – |
| Reference Position FBA | `referencePositionFBA` | `Transform` | – | – |
| Reference Position To Keep Object | `referencePositionToKeepObject` | `Transform` | – | – |

### Mount Point Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Bone To Keep Object | `useBoneToKeepObject` | `bool` | – | – |
| Bone To Keep Object | `boneToKeepObject` | `HumanBodyBones` | – | – |
| Use Mount Point To Keep Object | `useMountPointToKeepObject` | `bool` | – | – |
| Mount Point Tokeep Object Name | `mountPointTokeepObjectName` | `string` | – | – |

### Generic Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Be Grabbed On Generic Mode | `canBeGrabbedOnGenericMode` | `bool` | – | – |
| Mount Point Name To Carry On Generic Mode | `mountPointNameToCarryOnGenericMode` | `string` | "Mouth" | – |
| Set Custom Object Scale On Generic Mode | `setCustomObjectScaleOnGenericMode` | `bool` | – | – |
| Custom Object Scale On Generic Mode | `customObjectScaleOnGenericMode` | `Vector3` | – | – |

### IK Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| IK System Enabled | `IKSystemEnabled` | `bool` | true | – |
| Use Right Hand | `useRightHand` | `bool` | true | – |
| Use Left Hand | `useLeftHand` | `bool` | true | – |
| Right Hand Position | `rightHandPosition` | `Transform` | – | – |
| Lef Hand Position | `lefHandPosition` | `Transform` | – | – |
| Use Right Elbow | `useRightElbow` | `bool` | – | – |
| Use Left Elbow | `useLeftElbow` | `bool` | – | – |
| Right Elbow Position | `rightElbowPosition` | `Transform` | – | – |
| Lef Elbow Position | `lefElbowPosition` | `Transform` | – | – |

### Hands Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Animation Grabbing Hand | `useAnimationGrabbingHand` | `bool` | – | – |
| Right Grabbing Hand ID | `rightGrabbingHandID` | `int` | – | – |
| Left Grabbing Hand ID | `leftGrabbingHandID` | `int` | – | – |

### Grab Object Parent Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Right Hand For Object Parent | `useRightHandForObjectParent` | `bool` | true | – |

### Kinematic List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Extra List Kinematic | `setExtraListKinematic` | `bool` | – | – |
| Extra List Kinematic | `extraListKinematic` | `List<Rigidbody>` | new List<Rigidbody> () | – |

### Melee Weapons Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Melee Attack System | `useMeleeAttackSystem` | `bool` | – | – |
| Main Grab Physical Object Melee Attack System | `mainGrabPhysicalObjectMeleeAttackSystem` | `grabPhysicalObjectMeleeAttackSystem` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Enable Transparency On FBA | `enableTransparencyOnFBA` | `bool` | – | – |
| Use Throw Animation On Character Enabled | `useThrowAnimationOnCharacterEnabled` | `bool` | – | – |
| Throw Animation One Hand | `throwAnimationOneHand` | `string` | "Throw Physical Object One Hand" | – |
| Throw Animation Two Hands | `throwAnimationTwoHands` | `string` | "Throw Physical Object Two Hands" | – |
| Use Delay To Throw Object During Animation | `useDelayToThrowObjectDuringAnimation` | `bool` | – | – |
| Delay To Throw Object During Animation | `delayToThrowObjectDuringAnimation` | `float` | – | – |
| Ignore Show Object Name On Grab Objects System | `ignoreShowObjectNameOnGrabObjectsSystem` | `bool` | – | – |

### Extra Collider Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Uses Extra Collider List | `objectUsesExtraColliderList` | `bool` | – | – |
| Extra Collider List | `extraColliderList` | `List<Collider>` | new List<Collider> () | – |
| Check Extra Colliders In Parent | `checkExtraCollidersInParent` | `bool` | – | – |
| Extra Colliders Parent | `extraCollidersParent` | `Transform` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Grabed | `objectGrabed` | `bool` | – | – |
| Object Is Character | `objectIsCharacter` | `bool` | – | – |
| Character | `character` | `GameObject` | – | – |
| Character Body | `characterBody` | `Transform` | – | – |
| Keep Grabbed Object State | `keepGrabbedObjectState` | `bool` | – | – |
| Grab Objects List | `grabObjectsList` | `List<grabObjects>` | new List<grabObjects> () | – |
| Current Object Parent | `currentObjectParent` | `Transform` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Grab Drop | `useEventsOnGrabDrop` | `bool` | – | – |
| Event On Grab | `eventOnGrab` | `UnityEvent` | – | – |
| Event On Drop | `eventOnDrop` | `UnityEvent` | – | – |
| Use Event To Send Player | `useEventToSendPlayer` | `bool` | – | – |
| Event To Send Player | `eventToSendPlayer` | `eventParameters.eventToCallWithGameObject` | – | – |

### Remote Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remote Event Name List On Start | `remoteEventNameListOnStart` | `List<string>` | new List<string> () | – |
| Remote Event Name List On End | `remoteEventNameListOnEnd` | `List<string>` | new List<string> () | – |

### Grab Object Type Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Mesh Inside Main Parent | `objectMeshInsideMainParent` | `bool` | – | – |
| Object Mesh Main Parent | `objectMeshMainParent` | `Transform` | – | – |
| Use Mesh Collider | `useMeshCollider` | `bool` | – | – |
| Use Box Collider | `useBoxCollider` | `bool` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.red | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Grab Parent | `objectToGrabParent` | `GameObject` | – | – |
| Grab Object Trigger | `grabObjectTrigger` | `Collider` | – | – |
| Main Collider | `mainCollider` | `Collider` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `assignObjectToGrabParentIfNull()` | `objectToGrabParent`がnullなら自身のGameObjectを設定するだけ。 |
| `setRigidbodyList()` | `rigidbodyList`が空のとき、対象の子のRigidbodyと質量・レイヤーを収集して保持する。 |
| `grabObject(GameObject currentPlayer)` | `currentPlayer`の`grabObjects`へ掴み情報を渡し、質量/レイヤー変更やイベント発火も行う。 |
| `dropObject()` | 掴みを解除して`grabObjectsManager`へ通知し、質量・レイヤーを戻してイベントを発火する。 |
| `checkParentAssignedState()` | `objectToGrabParent`の親を引数に`checkNewParentAssignedState`を呼ぶだけ。 |
| `checkNewParentAssignedState(Transform newParent)` | 本体が空で何もしない。 |
| `isUseReferencePositionForEveryViewActive()` | `useReferencePositionForEveryView`の値を返すだけ。 |
| `getReferencePositionThirdPerson()` | `referencePositionThirdPerson`の参照を返すだけ。 |
| `getReferencePositionFirstPerson()` | `referencePositionFirstPerson`の参照を返すだけ。 |
| `getReferencePositionFBA()` | `referencePositionFBA`の参照を返すだけ。 |
| `getReferencePosition()` | `referencePosition`の参照を返すだけ。 |
| `getObjectName()` | `objectName`が空ならGameObject名で補完してから返す。 |
| `isIgnoreShowObjectNameOnGrabObjectsSystemActive()` | `ignoreShowObjectNameOnGrabObjectsSystem`の値を返すだけ。 |
| `isCanBeGrabbedOnGenericModeEnabled()` | `canBeGrabbedOnGenericMode`の値を返すだけ。 |
| `isIgnoreToGrabPhysicallyIfPickedWithAimingModeActive()` | `ignoreToGrabPhysicallyIfPickedWithAimingMode`の値を返すだけ。 |
| `checkTriggerInfo(Collider col, bool isEnter)` | 対象レイヤーの`grabObjects`を検出し、進入で登録・退出で解除するが、掴み中は何もしない。 |
| `removeAllGrabObjectsFound()` | 検出済みの`grabObjects`全てに掴み解除と対象削除を指示し、リストを空にする。 |
| `setCurrentPlayer(GameObject newPlayer)` | `newPlayer`のColliderを使い、進入扱いで`checkTriggerInfo`を呼ぶだけ。 |
| `isGrabObjectPhysicallyEnabled()` | `grabObjectPhysically`の値を返すだけ。 |
| `isCanBeGrabbedOnFirstPersonEnabled()` | `canBeGrabbedOnFirstPerson`の値を返すだけ。 |
| `isCanBeGrabbedOnThirdPersonEnabled()` | `canBeGrabbedOnThirdPerson`の値を返すだけ。 |
| `disableGrabPhysicalObject()` | `grabObjectPhysically`をfalseにし、`currentUser`から対象登録を外す。 |
| `setGrabObjectPhysicallyEnabledState(bool state)` | `grabObjectPhysically`を`state`に設定するだけ。 |
| `setGrabObjectPhysicallyEnabledStateFromEditor(bool state)` | 値を設定してから`updateComponent`でエディタ表示を更新する。 |
| `setMainColliderEnabledState(bool state)` | `mainCollider`がnullでなければ`enabled`を`state`にするだけ。 |
| `setGrabObjectTriggerState(bool state)` | `grabObjectTrigger`がnullでなければ`enabled`を`state`にするだけ。 |
| `setGrabObjectTriggerStateFromEditor(bool state)` | トリガーの有効状態を設定してから`updateComponent`でエディタ表示を更新する。 |
| `setCharacterBody(Transform newCharacterBody)` | `characterBody`を`newCharacterBody`に設定し、コンポーネントを更新するだけ。 |
| `setCharacter(GameObject newCharacter)` | `character`を`newCharacter`に設定し、コンポーネントを更新するだけ。 |
| `setObjectToGrabParent(GameObject newObjectToGrabParent)` | `objectToGrabParent`を差し替え、コンポーネントを更新するだけ。 |
| `setActiveOrInactiveObjectState(bool state)` | `state`に応じてタグ未設定なら既定値を入れ、`objectToGrabParent`のタグを有効/無効用へ変える。 |
| `checkEventsOnGrabDrop(bool state)` | `useEventsOnGrabDrop`が有効なとき、`state`で掴み/ドロップのイベントを発火する。 |
| `disableGrabPhysicalObjectComponent()` | `removeAllGrabObjectsFound`で解除し、トリガーとタグを無効状態にする。 |
| `isUseRightHandActive()` | `useRightHand`の値を返すだけ。 |
| `isUseLeftHandActive()` | `useLeftHand`の値を返すだけ。 |
| `hasObjectMeleeAttackSystem()` | `useMeleeAttackSystem`の値を返すだけ。 |
| `getMainGrabPhysicalObjectMeleeAttackSystem()` | `mainGrabPhysicalObjectMeleeAttackSystem`の参照を返すだけ。 |
| `activateReturnProjectilesOnContact()` | `grabObjectsManager`があれば弾反射接触処理を委譲するだけ。 |
| `checkRemoteEvents(bool state)` | `state`に応じて開始用/終了用のリモートイベント送信を呼び分ける。 |
| `checkRemoteEventOnStart()` | 有効時、`currentUser`の`remoteEventSystem`で開始イベント名を送る。 |
| `checkRemoteEventOnEnd()` | 有効時、`currentUser`の`remoteEventSystem`で終了イベント名を送る。 |
| `setKeepOrCarryGrabbebObjectState(bool state)` | 掴み中のみ`keepGrabbedObjectState`を更新し、近接武器システムにも伝える。 |
| `assignObjectParent(Transform newParent)` | `currentObjectParent`を`newParent`に設定するだけ。 |
| `getCurrentObjectParent()` | `currentObjectParent`の参照を返すだけ。 |
| `getLastPositionBeforeGrabbed()` | `lastPositionBeforeGrabbed`の値を返すだけ。 |
| `getLastRotationBeforeGrabbed()` | `lastRotationBeforeGrabbed`の値を返すだけ。 |
| `getLastPositionBeforeDropped()` | `lastPositionBeforeDropped`の値を返すだけ。 |
| `getLastRotationBeforeDropped()` | `lastRotationBeforeDropped`の値を返すだけ。 |
| `setLastParentAssigned(Transform newParent)` | `lastParentAssigned`を`newParent`に設定するだけ。 |
| `getLastParentAssigned()` | `lastParentAssigned`の参照を返すだけ。 |
| `grabPhysicalObjectExternally(GameObject currentPlayer)` | `currentPlayer`がnullでなければ`GKC_Utils`の外部グラブ処理に委譲する。 |
| `getMainRigidbody()` | `mainRigidbody`があればそれを、無ければ`objectToGrabParent`のRigidbodyを返す。 |
| `setCustomScale(Vector3 newValue)` | 元スケールが未保存なら現在値を記録してから`localScale`を`newValue`に変更する。 |
| `setOriginalScale()` | 記録済みの元スケールがあれば`setCustomScale`で元の大きさに戻す。 |
| `getExtraColliderList()` | 追加コライダー使用時、明示リストと`extraCollidersParent`の非トリガーColliderを返し、無ければnull。 |
| `getObjectUsesExtraColliderListState()` | `objectUsesExtraColliderList`の値を返すだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnGrab` | `UnityEvent` | – |
| `eventOnDrop` | `UnityEvent` | – |

## 内部型

- `grabPhysicalObjectInfo`（class）
