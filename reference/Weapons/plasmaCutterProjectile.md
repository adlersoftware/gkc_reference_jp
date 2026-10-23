# plasmaCutterProjectile

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `projectileSystem`
- **ソース**: `Weapons/Projectiles/plasmaCutterProjectile.cs:6`

**概要**: プラズマカッター用の投射物で、命中した物体をスライスまたは粉砕し、切断方向へ力を加える。切断回数の上限も持つ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Default Slice Material | `defaultSliceMaterial` | `Material` | – | – |
| Force To Apply To Cut Part | `forceToApplyToCutPart` | `float` | – | – |
| Force Mode | `forceMode` | `ForceMode` | – | – |
| Force Radius | `forceRadius` | `float` | – | – |
| Cut Multiple Times Active | `cutMultipleTimesActive` | `bool` | – | – |
| Use Cut Limit | `useCutLimit` | `bool` | – | – |
| Cut Limit | `cutLimit` | `int` | – | – |
| Activate Rigidbodies On New Objects | `activateRigidbodiesOnNewObjects` | `bool` | true | – |

### Shatter Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shatter Object Active | `shatterObjectActive` | `bool` | – | – |
| Shatter Amount | `shatterAmount` | `int` | – | – |
| Apply Force On Shatter | `applyForceOnShatter` | `bool` | – | – |
| Add Slice Component To Pieces | `addSliceComponentToPieces` | `bool` | true | – |

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
| Min Delay To Slice Same Object | `minDelayToSliceSameObject` | `float` | 0.01f | – |
| Cut Position Transform | `cutPositionTransform` | `Transform` | – | – |
| Cut Overlap Box Size | `cutOverlapBoxSize` | `Vector3` | new Vector3 (5, 0.1f, 5) | – |
| Add Rigidbody To Both Sliced Objects | `addRigidbodyToBothSlicedObjects` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Objects Detected | `objectsDetected` | `List<GameObject>` | new List<GameObject> () | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.red | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Cut Direction Transform | `cutDirectionTransform` | `Transform` | – | – |
| Plane Definer1 | `planeDefiner1` | `Transform` | – | – |
| Plane Definer2 | `planeDefiner2` | `Transform` | – | – |
| Plane Definer3 | `planeDefiner3` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkObjectDetected(Collider col)` | 着弾音の後`processObject`で切断し、多重切断の上限に達したら自身を破棄する。 |
| `processObject(GameObject objectToCheck, Collider objectCollider, Vector3 slicePosition)` | 対象の`surfaceToSlice`と切断条件を確認して切断を試み、不可なら設定に応じてダメージと力を与える。 |
| `sliceCurrentObject(GameObject objectToCheck, Collider objectCollider, Material crossSectionMaterial, Vector3 slicePosition)` | 回数を数え、キャラは`processCharacter`、粉砕設定は`shatterObject`、他は二分割して破片を整える。 |
| `checkForceToApplyOnObject(GameObject objectToDamage)` | 切断方向と`addForceMultiplier`で質量に応じた力を加え、乗物なら専用の倍率を掛ける。 |
| `setShatterObjectActiveState(bool state)` | `shatterObjectActive`を`state`にするだけ。 |
| `shatterObject(GameObject objectToCheck, Material crossSectionMaterial)` | 未粉砕なら対象を親から外して破片リストへ入れ、`shatterAmount`回`randomShatter`を実行して粉砕済みにする。 |
| `randomShatter(Material crossSectionMaterial)` | 粉砕対象リストの各要素を`randomShatterSingle`で分割し、元を消して新しい破片をリストへ差し替える。 |
| `randomShatterSingle(GameObject objectToShatter, Material crossSectionMaterial)` | 対象を分割し、破片へMeshColliderとRigidbodyを付け、必要なら爆発力を加えて配列を返す。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetProjectile()`, `setProjectileSpecialActionActiveState(bool state)`

</details>
