# FloatingObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `objectOnWater`
- **ソース**: `Others/FloatingObject.cs:6`

**概要**: 水面（`waterSurfaceSystem`）上でRigidbodyにボクセル単位の浮力を加え、水中の抵抗や外部力を処理する浮遊オブジェクト。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Calculate Density | `calculateDensity` | `bool` | false | – |
| Density | `density` | `float` | 0.75f | – |
| Max Density | `maxDensity` | `float` | 0 | – |
| Min Density | `minDensity` | `float` | 0 | – |
| Normalized Voxel Size | `normalizedVoxelSize` | `float` | 0.5f | Range (0f, 1f) |
| Drag In Water | `dragInWater` | `float` | 1f | – |
| Angular Drag In Water | `angularDragInWater` | `float` | 1f | – |
| Update Bounds Values From Collider | `updateBoundsValuesFromCollider` | `bool` | true | – |
| Bounds | `bounds` | `Bounds` | – | – |

### Gravity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Update Gravity Froce From Water Volume | `updateGravityFroceFromWaterVolume` | `bool` | true | – |
| Gravity Force | `gravityForce` | `Vector3` | new Vector3 (0, -9.8f, 0) | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Object On Water Active | `objectOnWaterActive` | `bool` | – | – |
| External Forces Active | `externalForcesActive` | `bool` | – | – |
| External Forces Value | `externalForcesValue` | `Vector3` | – | – |
| External Rotation Force Active | `externalRotationForceActive` | `bool` | – | – |
| External Rotation Force | `externalRotationForce` | `float` | – | – |
| External Rotation Force Point | `externalRotationForcePoint` | `Vector3` | – | – |
| Current Rotation Axis | `currentRotationAxis` | `Vector3` | – | – |
| Initial Values Assigned | `initialValuesAssigned` | `bool` | – | – |
| Apply Buoyancy Active | `applyBuoyancyActive` | `bool` | true | – |
| Max Buoyancy Force | `maxBuoyancyForce` | `Vector3` | – | – |
| Main Water Surface System | `mainWaterSurfaceSystem` | `waterSurfaceSystem` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Enter Exit Water | `useEventsOnEnterExitWater` | `bool` | – | – |
| Eventon Enter Water | `eventonEnterWater` | `UnityEvent` | – | – |
| Event On Exit Water | `eventOnExitWater` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Collider | `mainCollider` | `Collider` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Main Mesh Filter | `mainMeshFilter` | `MeshFilter` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の`updateCoroutine`があれば停止するだけ。 |
| `setWaterVolumeState(waterSurfaceSystem newWaterSurfaceSystem, bool state)` | `state`で水面判定を切り替え、有効化時は水面設定と密度・ボクセルを初期化して浮力コルーチンを開始する。 |
| `setNewGravityForce(Vector3 newValues)` | `gravityForce`を`newValues`にするだけ。 |
| `updateMaxBuoyancyForce()` | `mass / density`と水面の密度・重力から`maxBuoyancyForce`を再計算する。 |
| `setApplyBuoyancyActiveState(bool state)` | `applyBuoyancyActive`を`state`にするだけ。 |
| `checkObjectStateOnWater()` | 本体が空の`virtual`メソッドで、更新ごとに派生先から呼ばれる。 |
| `checkObjectStateOnWaterEnterOrExit(bool state)` | 本体が空の`virtual`メソッドで、入水・出水時に呼ばれる。 |
| `getMainCollider()` | `mainCollider`を返すだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventonEnterWater` | `UnityEvent` | – |
| `eventOnExitWater` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`addOrRemoveDensity(float newValue)`, `getDensity()`, `isObjectOnWaterActive()`, `setNewDensity(float newValue)`, `setOriginalDensity()`, `updateExternalForces(Vector3 newValues, bool externalForcesActiveValue)`, `updateExternalRotationForces(float rotationAmount, Vector3 rotationAxis, Vector3 externalRotationForcePointValue)`

</details>
