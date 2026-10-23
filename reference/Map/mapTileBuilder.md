# mapTileBuilder

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Map/mapTileBuilder.cs:5`

**概要**: マップの1パーツ(部屋や区画)を表し、頂点列からタイルメッシュと押し出し3Dメッシュを生成する。有効/無効の切り替え、色設定、テキストやイベントトリガーの管理も担当する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Map Part Parent | `mapPartParent` | `Transform` | – | マップパーツを配置するフロアの親。 |
| Map Part Building Index | `mapPartBuildingIndex` | `int` | – | このパーツが属する建物のインデックス。 |
| Map Part Floor Index | `mapPartFloorIndex` | `int` | – | このパーツが属するフロアのインデックス。 |
| Map Part Index | `mapPartIndex` | `int` | – | フロア内でのパーツのインデックス。 |
| Map Part Renderer Offset | `mapPartRendererOffset` | `float` | – | 2Dタイルメッシュを奥へずらす距離。 |
| New Position Offset | `newPositionOffset` | `Vector2` | – | 新しい頂点を追加する際の位置オフセット。 |
| Map Part Enabled | `mapPartEnabled` | `bool` | true | このマップパーツを有効にする。 |
| Use Other Color If Map Part Disabled | `useOtherColorIfMapPartDisabled` | `bool` | – | 無効時に非表示ではなく色を変える。 / 表示条件: `mapPartEnabled` がオフのとき |
| Color If Map Part Disabled | `colorIfMapPartDisabled` | `Color` | – | 無効時にパーツへ適用する表示色。 / 表示条件: `!mapPartEnabled.boolValue && useOtherColorIfMapPartDisabled.boolValue` |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | true | シーンビューにギズモを表示する。 |
| Show Enabled Trigger | `showEnabledTrigger` | `bool` | true | 有効化トリガーのギズモを表示する。 / 表示条件: `showGizmo` がオンのとき |
| Show Vertex Distance | `showVerticesDistance` | `bool` | – | 頂点間の距離をシーンに表示する。 / 表示条件: `showGizmo` がオンのとき |
| Map Lines Color | `mapLinesColor` | `Color` | Color.yellow | マップ輪郭線を描くギズモの色。 / 表示条件: `showGizmo` がオンのとき |
| Map Part Material Color | `mapPartMaterialColor` | `Color` | Color.white | パーツのマテリアルとギズモの色。 / 表示条件: `showGizmo` がオンのとき |
| Cube Gizmo Scale | `cubeGizmoScale` | `Vector3` | Vector3.one | 中心キューブギズモの表示大きさ。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.white | ギズモに表示するラベルの文字色。 / 表示条件: `showGizmo` がオンのとき |
| Show Vertex Handles | `showVertexHandles` | `bool` | – | 頂点の移動ハンドルを表示する。 / 表示条件: `showGizmo` がオンのとき |

### Handle Vertex Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Handle For Vertex | `useHandleForVertex` | `bool` | – | 頂点をフリームーブハンドルで操作する。 / 表示条件: `showGizmo` がオンのとき |
| Handle Radius | `handleRadius` | `float` | 0.1f | 頂点操作ハンドルの半径サイズ。 / 表示条件: `showGizmo.boolValue && useHandleForVertex.boolValue` |

### Rename Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Map Part Name | `mapPartName` | `string` | – | パーツ名の末尾に付ける表示名。 |

### Map Part 3d Mesh Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Generate3d Map Part Mesh | `generate3dMapPartMesh` | `bool` | – | このパーツの3Dメッシュを生成する。 |
| Only Use3d Map Part Mesh | `onlyUse3dMapPartMesh` | `bool` | – | 2Dタイルを隠し3Dメッシュだけを使う。 / 表示条件: `generate3dMapPartMesh` がオンのとき |
| Generate3d Meshes Show Gizmo | `generate3dMeshesShowGizmo` | `bool` | – | 生成3Dメッシュの高さギズモを表示する。 / 表示条件: `generate3dMapPartMesh` がオンのとき |
| Map Part3d Height | `mapPart3dHeight` | `float` | 1 | 3Dメッシュの押し出し高さを指定する。 / 表示条件: `generate3dMapPartMesh` がオンのとき |
| Map Part3d Offset | `mapPart3dOffset` | `Vector3` | – | 3Dメッシュの位置オフセット。 / 表示条件: `generate3dMapPartMesh` がオンのとき |
| Map Part3d Game Object | `mapPart3dGameObject` | `GameObject` | – | 生成された3Dメッシュの`GameObject`。 / 表示条件: `generate3dMapPartMesh.boolValue && mapPart3dMeshCreated.boolValue` |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `verticesPosition` | `List<Transform>` | new List<Transform> () | – |
| `eventTriggerList` | `List<GameObject>` | new List<GameObject> () | – |
| `extraMapPartsToActive` | `List<GameObject>` | new List<GameObject> () | – |
| `mapManager` | `mapCreator` | – | – |
| `textMeshList` | `List<GameObject>` | new List<GameObject> () | – |
| `center` | `Vector3` | – | – |
| `internalName` | `string` | – | – |
| `mapPart3dMeshCreated` | `bool` | – | – |
| `mapTileRenderer` | `GameObject` | – | – |
| `mapTileMeshFilter` | `MeshFilter` | – | – |
| `mapTileCreated` | `bool` | – | – |
| `mainMeshRenderer` | `MeshRenderer` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `createMapTileElement()` | 未生成なら`calculateMapTileMesh`と3Dメッシュ生成を行い、パーツ無効時は色変更や非表示に切り替える。 |
| `calculateMapTileMesh()` | `verticesPosition`を三角分割してメッシュを作り、`Map Tile Renderer`を生成して床材質の色を反映する。 |
| `removeMapTileRenderer()` | 生成済みのタイルの`MeshRenderer`と`MeshFilter`を破棄し、`mapTileCreated`をfalseにして保存する。 |
| `setWallRendererMaterialColor(Color newColor)` | `mainMeshRenderer`の色を、再生中は`material`、編集中は`sharedMaterial`経由で`newColor`にするだけ。 |
| `set3dMapPartMaterialColor(Color newColor)` | 3Dメッシュの`MeshRenderer`があれば、その材質色を`newColor`にするだけ。 |
| `setOriginal3dMapPartMaterialColor()` | 3Dメッシュの材質色を、生成時に保存した`originalMapPart3dMeshRendererColor`へ戻す。 |
| `enableMapPart()` | タイル・テキスト・3Dメッシュを表示し、アイコンを有効化、`mapPartEnabled`をtrueにして現在パーツを通知する。 |
| `enableOrDisableEventTriggerList(bool state)` | `eventTriggerList`内の各トリガー`GameObject`を`state`に合わせて切り替えるだけ。 |
| `disableMapPart()` | タイルを非表示にしてテキストメッシュも消し、`mapPartEnabled`をfalseにする。 |
| `setMapPartEnabledState(bool state)` | `mapPartEnabled`に`state`を代入するだけ。 |
| `enableOrDisableTextMesh(bool state)` | `textMeshList`の各テキストを`state`で切り替え、無効時色の設定があれば壁色も更新する。 |
| `addEventTriggerToActive()` | `Player`タグでパーツを有効化する`BoxCollider`トリガーを生成し、`eventTriggerList`に追加して保存する。 |
| `setMapPartEnabledStateFromEditor(bool state)` | `mapPartEnabled`を設定し`updateComponent`でシーンを保存するだけ。 |
| `removeEventTrigger(int eventTriggerIndex)` | 指定インデックスのトリガーを破棄してリストから除き、残りが無ければ親も削除して保存する。 |
| `removeAllEventTriggers()` | 全てのトリガーとその親オブジェクトを破棄し、`eventTriggerList`を空にして保存する。 |
| `addMapPartTextMesh()` | `mapPartTextMesh`プレハブを複製して`textMeshParent`配下に置き、`textMeshList`へ追加する。 |
| `removeTextMesh(int textMeshIndex)` | 指定テキストメッシュを破棄してリストから除き、最後の1つなら親も削除して保存する。 |
| `removeAllTextMesh()` | 全てのテキストメッシュと親オブジェクトを破棄し、リストを空にしてシーンを更新する。 |
| `addNewVertex(int insertAtIndex)` | 頂点`Transform`を新規作成し、`insertAtIndex`が-1以上ならその直後に挿入して名前を振り直す。 |
| `removeVertex(int vertexIndex)` | 指定インデックスの頂点`GameObject`を破棄し、リストから除いて保存する。 |
| `removeAllVertex()` | 全ての頂点`GameObject`を破棄して`verticesPosition`を空にし、保存する。 |
| `renameAllVertex()` | 各頂点`Transform`の名前を3桁の連番に振り直して保存するだけ。 |
| `reverVertexOrder()` | `verticesPosition`の並び順を反転させて保存するだけ。 |
| `setInternalName(string nameToConfigure)` | `internalName`を設定したうえで`renameMapPart`を呼び、`GameObject`名を更新する。 |
| `renameMapPart()` | `internalName`と`mapPartName`から`GameObject`名を組み立てて設定し、保存する。 |
| `updateMapPart3dMeshPositionFromEditor()` | `mapPart3dOffset`を引数に`updateMapPart3dMeshPosition`を呼ぶだけ。 |
| `updateMapPart3dMeshPosition(Vector3 offset)` | 3Dメッシュ生成済みなら`mapPart3dGameObject`を`center`+`offset`の位置へ移動する。 |
| `enableOrDisableMapPart3dMesh(bool state)` | 3Dメッシュ生成済みなら`mapPart3dGameObject`のアクティブ状態を`state`に合わせる。 |
| `removeMapPart3dMesh()` | 生成済みの3Dメッシュ`GameObject`を破棄し、`mapPart3dMeshCreated`をfalseにする。 |
| `removeMapPart3dMeshFromEditor()` | 3Dメッシュを破棄して生成フラグを戻し、`updateComponent`でシーンを保存する。 |
| `setGenerate3dMapPartMeshState(bool state)` | `generate3dMapPartMesh`に`state`を代入するだけ。 |
| `setGenerate3dMapPartMeshStateFromEditor(bool state)` | `generate3dMapPartMesh`を設定してシーンを保存するだけ。 |
| `generateMapPart3dMeshFromEditor()` | `mapPart3dHeight`を高さに3Dメッシュを生成し、シーンを保存する。 |
| `generateMapPart3dMesh(float meshHeight)` | 生成設定が有効なとき、頂点列から押し出し3Dメッシュを作り`mapManager`のフロア親へ登録する。 |
| `setMapManager(mapCreator currentMapManager)` | `mapManager`に`currentMapManager`を設定して保存するだけ。 |
| `setMapPartParent(Transform currentMapPartParent)` | `mapPartParent`を設定して保存するだけ。 |
| `setMapPartBuildingIndex(int newIndex)` | `mapPartBuildingIndex`を設定して保存するだけ。 |
| `setMapPartFlooorIndex(int newIndex)` | `mapPartFloorIndex`を設定して保存するだけ。 |
| `setMapPartIndex(int newIndex)` | `mapPartIndex`を設定して保存するだけ。 |
| `setRandomMapPartColor()` | `mapPartMaterialColor`にランダムな不透明色を設定して保存するだけ。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`で変更を保存しシーンをダーティにするだけ。 |
