# sliceObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/New Weapon Behaviors/sliceObject.cs:5`

**概要**: 近接武器などに付け、トリガー内の物体を任意平面でスライスしたりダメージを与えたりする挙動。対象の`surfaceToSlice`設定に従う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slice Active | `sliceActive` | `bool` | – | – |
| Disable Slice After First Cut Enabled | `disableSliceAfterFirstCutEnabled` | `bool` | true | – |
| Default Slice Material | `defaultSliceMaterial` | `Material` | – | – |
| Cut Overlap Box Size | `cutOverlapBoxSize` | `Vector3` | new Vector3 (5, 0.1f, 5) | – |
| Min Delay To Slice Same Object | `minDelayToSliceSameObject` | `float` | 0.3f | – |
| Activate Rigidbodies On New Objects | `activateRigidbodiesOnNewObjects` | `bool` | true | – |
| Slice Regular Objects Enabled | `sliceRegularObjectsEnabled` | `bool` | true | – |
| Slice Characters Enabled | `sliceCharactersEnabled` | `bool` | true | – |

### Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Damage On Slice | `activateDamageOnSlice` | `bool` | – | – |
| Damage Amount To Apply On Slice | `damageAmountToApplyOnSlice` | `float` | – | – |
| Ignore Shield On Damage | `ignoreShieldOnDamage` | `bool` | true | – |
| Can Activate Reaction System Temporally | `canActivateReactionSystemTemporally` | `bool` | – | – |
| Damage Reaction ID | `damageReactionID` | `int` | -1 | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |

### Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Update Last Object Speed | `updateLastObjectSpeed` | `bool` | – | – |
| Force To Apply To Cut Part | `forceToApplyToCutPart` | `float` | – | – |
| Force Mode | `forceMode` | `ForceMode` | – | – |
| Force Radius | `forceRadius` | `float` | – | – |
| Force Up | `forceUp` | `float` | – | – |
| Disable Time After Collision | `disableTimeAfterCollision` | `float` | – | – |
| Target To Damage Layer | `targetToDamageLayer` | `LayerMask` | – | – |
| Apply Forces On Objects Detected | `applyForcesOnObjectsDetected` | `bool` | – | – |
| Add Force Multiplier | `addForceMultiplier` | `float` | – | – |
| Apply Impact Force To Vehicles | `applyImpactForceToVehicles` | `bool` | – | – |
| Impact Force To Vehicles Multiplier | `impactForceToVehiclesMultiplier` | `float` | – | – |
| Check Object Layer And Tag To Apply Forces | `checkObjectLayerAndTagToApplyForces` | `bool` | – | – |
| Target To Apply Force Layer | `targetToApplyForceLayer` | `LayerMask` | – | – |
| Taget To Apply Force Tag List | `tagetToApplyForceTagList` | `List<string>` | new List<string> () | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Cut Multiple Times Active | `cutMultipleTimesActive` | `bool` | true | – |
| Ignore Objects Already Slice | `ignoreObjectsAlreadySlice` | `bool` | – | – |
| Min Wait Time To Activate Slice | `minWaitTimeToActivateSlice` | `float` | 0.4f | – |
| Use Objects To Ignore List | `useObjectsToIgnoreList` | `bool` | – | – |
| Objects To Ignore List | `objectsToIgnoreList` | `List<GameObject>` | new List<GameObject> () | – |

### Bullet Time Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Time Bullet On Regular Slice | `ignoreTimeBulletOnRegularSlice` | `bool` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remote Event Name List | `remoteEventNameList` | `List<string>` | new List<string> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Show Debug Wait Time Print | `showDebugWaitTimePrint` | `bool` | – | – |
| Objects Detected | `objectsDetected` | `List<GameObject>` | new List<GameObject> () | – |
| Colliders To Ignore List | `collidersToIgnoreList` | `List<Collider>` | new List<Collider> () | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.red | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Collider | `mainCollider` | `Collider` | – | – |
| Trigger Collider | `triggerCollider` | `Collider` | – | – |
| Cut Position Transform | `cutPositionTransform` | `Transform` | – | – |
| Cut Direction Transform | `cutDirectionTransform` | `Transform` | – | – |
| Plane Definer1 | `planeDefiner1` | `Transform` | – | – |
| Plane Definer2 | `planeDefiner2` | `Transform` | – | – |
| Plane Definer3 | `planeDefiner3` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `processObject(GameObject obj, Collider objectCollider, Vector3 slicePosition)` | 対象の`surfaceToSlice`と切断可否・方向を確認して切断し、不可なら設定に応じてダメージと力を与える。 |
| `toggleSliceActiveState()` | `sliceActive`を反転して`setSliceActiveState`を呼ぶだけ。 |
| `setSliceActiveState(bool state)` | `sliceActive`を設定し、有効時はコライダーを切り替え、無効時は無視リストを初期化する。 |
| `checkObjectDetected(Collider col)` | 対象レイヤーと無視リストを確認し、切断位置を更新して`processObject`へ渡す。 |
| `sliceCurrentObject(GameObject obj, Collider objectCollider, Material crossSectionMaterial, Vector3 slicePosition)` | キャラなら`processCharacter`、それ以外は`sliceSystemUtils`で二分割し、破片の生成と力の適用を行う。 |
| `stopDisableSliceActiveWithDelay()` | `disableSliceCoroutine`があれば停止するだけ。 |
| `disableSliceActiveWithDelay()` | 既存の遅延処理を止め、0.5秒と`disableTimeAfterCollision`の後に切断を切るコルーチンを開始する。 |
| `disableIgnoreCollisionList()` | 衝突無視リストと検出済みリストを空にし、トリガーコライダーを無効にする。 |
| `checkForceToApplyOnObject(GameObject objectToDamage)` | 切断方向と倍率から質量に応じた力を加え、乗物なら専用の倍率を掛ける。 |
