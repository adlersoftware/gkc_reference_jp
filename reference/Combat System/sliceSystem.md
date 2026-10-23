# sliceSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/Slice System/sliceSystem.cs:5`

**概要**: オーバーラップボックスで対象を検出してメッシュを切断し、破片の剛体・力・ダメージ・イベントを処理する中核コンポーネント。

**公式ドキュメント抜粋**（[(Optional) Download External Files](../../docs/quick-start/get-started/optional-download-external-files.md)）

> The action system can be used with any type of humanoid animation. To work on this system, example animations from Mixamo were used as placeholders to configure multiple examples of the action system. Due to Mixamo animations can’t be included on asset, you can find the animations used on these examples on the public repository of Game Kit Controller on Github. <https://github.com/sr3888/GKC-Public-Repository These animations are already with the regular settings applied to work on root motion properly (like rotation based on current pose, loop time, adjust speed, etc…). No extra setting is needed to try these examples. All those animations and copyrights belong to Mixamo. You can get those animations and more at the official website of Mixamo: <https://www.mixamo.com// Of course, on this action system, you can use your own animations, from the asset store or any other store or web. Ther…

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Cut Overlap Box Size | `cutOverlapBoxSize` | `Vector3` | new Vector3 (5, 0.1f, 5) | – |
| Activate Rigidbodies On New Objects | `activateRigidbodiesOnNewObjects` | `bool` | – | – |
| Min Delay To Slice Same Object | `minDelayToSliceSameObject` | `float` | 0.3f | – |

### Objects To Affect Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Target To Damage Layer | `targetToDamageLayer` | `LayerMask` | – | – |
| Use Objects To Ignore List | `useObjectsToIgnoreList` | `bool` | – | – |
| Objects To Ignore List | `objectsToIgnoreList` | `List<GameObject>` | new List<GameObject> () | – |

### Force Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Force To Apply To Cut Part | `forceToApplyToCutPart` | `float` | – | – |
| Force Mode | `forceMode` | `ForceMode` | – | – |
| Force Radius | `forceRadius` | `float` | – | – |
| Force Up | `forceUp` | `float` | – | – |

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

### Slice Transform Values Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slice Transform Values Info List | `sliceTransformValuesInfoList` | `List<sliceTransformValuesInfo>` | new List<sliceTransformValuesInfo> () | – |

### Bullet Time Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Time Bullet On Regular Slice | `ignoreTimeBulletOnRegularSlice` | `bool` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.red | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Game Object | `playerGameObject` | `GameObject` | – | – |
| Default Slice Material | `defaultSliceMaterial` | `Material` | – | – |
| Cut Position Transform | `cutPositionTransform` | `Transform` | – | – |
| Cut Direction Transform | `cutDirectionTransform` | `Transform` | – | – |
| Plane Definer1 | `planeDefiner1` | `Transform` | – | – |
| Plane Definer2 | `planeDefiner2` | `Transform` | – | – |
| Plane Definer3 | `planeDefiner3` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCustomSliceTransformValues(string sliceInfoName)` | `sliceTransformValuesInfoList`から名前一致かつ有効な設定を探し、その切断値で`activateCut`を実行する。 |
| `setCustomCutTransformValues(Vector3 newCutOverlapBoxSize, Transform newcutPositionTransform, Transform newCutDirectionTransform, Transform newPlaneDefiner1, Transform newPlaneDefiner2, Transform newPlaneDefiner3)` | カスタム切断用の位置・回転・方向・平面定義3点・ボックスサイズを内部値へ取り込み、以降の`activateCut`で使う。 |
| `activateCutExternally()` | 外部起点フラグを立ててから`activateCut`を呼び、バレットタイム判定を通常斬撃と区別する。 |
| `activateCut()` | `OverlapBox`で検出した各コライダーを`processObject`へ渡し、検出有無と最終切断時刻を記録する。 |
| `getLastCollidersListDetected()` | 前回の検出コライダーをGameObjectリストとして返し、2回目以降は空を返す。 |
| `processObject(GameObject obj, Collider objectCollider, Vector3 slicePosition)` | 無視リストと`surfaceToSlice`の可否を判定し、切断可なら`sliceCurrentObject`、不可ならダメージや力を適用する。 |
| `sliceCurrentObject(GameObject obj, Collider objectCollider, Material crossSectionMaterial, Vector3 slicePosition)` | キャラクタは死亡時にラグドール化して`activateSlice`、通常物は2分割し破片に剛体とコライダーを付ける。 |
| `checkForceToApplyOnObject(GameObject objectToDamage)` | 切断方向`currentCutDirection`×`addForceMultiplier`の力を質量に掛け、車両には専用倍率を適用して加える。 |
| `anyObjectDetectedOnLastSlice()` | 直前の`activateCut`で切断対象が検出されたか`objectsDetectedOnLastSlice`を返すだけ。 |

## 内部型

- `sliceTransformValuesInfo`（class）
