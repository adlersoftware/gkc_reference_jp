# createMeshDuplicate

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/createMeshDuplicate.cs:6`

**概要**: `SkinnedMeshRenderer`をベイクして静的メッシュの複製を作り、基準オブジェクトの子としてまとめる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Skinned Mesh Renderer | `mainSkinnedMeshRenderer` | `List<SkinnedMeshRenderer>` | new List<SkinnedMeshRenderer> () | – |
| Use New Material | `useNewMaterial` | `bool` | – | – |
| Duplicate Material | `duplicateMaterial` | `Material` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Create Duplicate | `eventOnCreateDuplicate` | `UnityEvent` | – | – |
| Use Event To Sent Duplicated Meshes | `useEventToSentDuplicatedMeshes` | `bool` | – | – |
| Event To Sent Duplicated Meshes | `eventToSentDuplicatedMeshes` | `eventParameters.eventToCallWithGameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Duplicate Base Game Object | `duplicateBaseGameObject` | `GameObject` | – | – |
| Mesh Transform | `meshTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `createDuplicate()` | 各`SkinnedMeshRenderer`を`BakeMesh`して複製を作り、`duplicateBaseGameObject`のインスタンス下にまとめてイベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCreateDuplicate` | `UnityEvent` | – |
