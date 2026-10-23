# combineMeshSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/combineMeshSystem.cs:5`
- **属性**: `RequireComponent (typeof (MeshFilter))`, `RequireComponent (typeof (MeshRenderer))`

**概要**: 子階層の`MeshFilter`を集めて1つのメッシュに結合し、必要なら`MeshCollider`も付ける。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Mesh Filter List | `useMeshFilterList` | `bool` | – | – |
| List Mesh Filter | `listMeshFilter` | `List<MeshFilter>` | – | – |
| Use Custom Parent List To Get Mesh Filter List | `useCustomParentListToGetMeshFilterList` | `bool` | – | – |
| Custom Parent List To Get Mesh Filter List | `customParentListToGetMeshFilterList` | `List<Transform>` | – | – |
| Mesh Filters To Skip | `meshFiltersToSkip` | `MeshFilter []` | new MeshFilter [0] | MeshFilters with Meshes which we don't want to combine into one Mesh. |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Create Multi Material Mesh | `createMultiMaterialMesh` | `bool` | false | – |
| Combine Inactive Children | `combineInactiveChildren` | `bool` | false | – |
| Deactivate Combined Children | `deactivateCombinedChildren` | `bool` | true | – |
| Deactivate Combined Children Mesh Renderers | `deactivateCombinedChildrenMeshRenderers` | `bool` | false | – |
| Generate UV Map | `generateUVMap` | `bool` | false | – |
| Destroy Combined Children | `destroyCombinedChildren` | `bool` | false | – |
| Add Mesh Collider To Combined Mesh | `addMeshColliderToCombinedMesh` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Send Combined Object On Event | `sendCombinedObjectOnEvent` | `bool` | – | – |
| Event To Send Combined Object | `eventToSendCombinedObject` | `eventParameters.eventToCallWithGameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `CombineMeshes(bool showCreatedMeshInfo)` | 親から外してTransformを原点に戻し、メッシュを結合して元の状態へ戻す。`showCreatedMeshInfo`は生成情報の出力可否。 |
| `getObjectMeshes()` | 対象の`MeshFilter`を集めて`listMeshFilter`を作り直し、パーティクルと自身のものを除外する。 |
| `clearMeshList()` | `listMeshFilter`を空にして`updateComponent`でエディタ表示を更新する。 |
