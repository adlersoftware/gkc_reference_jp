# placeObjectInCameraEditorPositionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/placeObjectInCameraEditorPositionSystem.cs:5`

**概要**: エディタカメラからのレイキャストでオブジェクトを面上に配置し、回転・整列・接地スナップを操作する編集用コンポーネント。

**公式ドキュメント抜粋**（[Place Object in Camera Editor Position System](../../docs/toplevelcomponents/player-and-game-management/place-object-in-camera-editor-position-system.md)）

> 

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Position Offset | `positionOffset` | `Vector3` | – | – |
| Rotation Amount | `rotationAmount` | `float` | 90 | – |
| Layer To Place Elements | `layerToPlaceElements` | `LayerMask` | – | – |

### Snap To Ground Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Object To Snap | `useCustomObjectToSnap` | `bool` | – | – |
| Custom Object To Snap | `customObjectToSnap` | `Transform` | – | – |

### Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Select | `objectToSelect` | `GameObject` | – | – |
| Objects To Move List | `objectsToMoveList` | `List<Transform>` | new List<Transform> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `moveObjects()` | エディタカメラの位置と前方へレイキャストし、`objectsToMoveList`を当たった面へ移動する。 |
| `snapToGrounSurface()` | 自身（または`customObjectToSnap`）の上から下向きにレイを飛ばし、オブジェクトを地面へ吸着させる。 |
| `rotateObject(int direction)` | 各オブジェクトをY軸回りに`direction * rotationAmount`度回転させる。 |
| `resetObjectRotation()` | 各オブジェクトの回転を`Quaternion.identity`に戻す。 |
| `addObjectToList(GameObject newObject)` | `newObject`がnullでなく未登録なら`objectsToMoveList`に追加する。 |
| `setDefaultLayermask()` | `layerToPlaceElements`にDefaultとTerrainのレイヤーを追加する。 |
| `selectObject()` | `objectToSelect`がnullでなければエディタ上で選択状態にする。 |
| `setOffsetFromRendererBound()` | `positionOffset.y`が0のとき、Rendererの高さ半分を縦オフセットに設定する。 |
