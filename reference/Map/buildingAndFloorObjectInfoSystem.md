# buildingAndFloorObjectInfoSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Map/buildingAndFloorObjectInfoSystem.cs:5`

**概要**: 対象`GameObject`に建物とフロアの親情報を設定するための中継コンポーネント。値を保持し、実際の処理は`mapCreator`へ委譲する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Map Creator Manager | `mapCreatorManager` | `mapCreator` | – | – |
| Building Parent | `buildingParent` | `Transform` | – | – |
| Floor Parent | `floorParent` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentObjectToChangeBuildingInfo(GameObject newObject)` | 建物・フロア情報を設定する対象`GameObject`を保持するだけ。 |
| `setBuildingAndFloorInfoToObject()` | 保持した対象オブジェクトに、`mapCreator`経由で建物とフロアの親情報を設定する。 |
| `setBuildingFloorInfo(Transform newBuildingParent, Transform newFloorParent, mapCreator newMapCreator)` | `mapCreator`と建物・フロアの親`Transform`をまとめて保持するだけ。 |
