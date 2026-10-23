# mapCreator

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Map/mapCreator.cs:5`

**概要**: 建物・階・マップパーツ・アイコン・各種トリガーをまとめて管理するマップ生成の中心コンポーネントで、各プレイヤーの`mapSystem`へ処理を中継する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Floor Material | `floorMaterial` | `Material` | – | マップタイルメッシュに割り当てる床マテリアル。 |
| Map Layer | `mapLayer` | `string` | – | マップタイルと3Dメッシュに設定するレイヤー。 |
| Trigger To Change Building Prefab | `triggerToChangeBuildingPrefab` | `GameObject` | – | 建物切り替えトリガーを生成するときのプレハブ。 |
| Trigger To Change Floor Prefab | `triggerToChangeFloorPrefab` | `GameObject` | – | 階切り替えトリガーを生成するときのプレハブ。 |
| Trigger To Change Dynamic Object Prefab | `triggerToChangeDynamicObjectPrefab` | `GameObject` | – | 動的オブジェクト用トリガーを生成するプレハブ。 |
| Map Part3d Mesh Material | `mapPart3dMeshMaterial` | `Material` | – | 3Dメッシュ生成時に割り当てるマテリアル。 |
| Map Part3d Material Color | `mapPart3dMaterialColor` | `Color` | Color.white | 3Dメッシュ用マテリアルに設定する色。 |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer To Place Elements | `layerToPlaceElements` | `LayerMask` | – | トリガー自動配置のレイキャスト対象レイヤー。 |
| Use Raycast To Place Elements | `useRaycastToPlaceElements` | `bool` | – | 生成したトリガーをレイキャストの着地点に置く。 |
| Map Part Enabled Trigger Scale | `mapPartEnabledTriggerScale` | `Vector3` | – | 生成する切り替えトリガーに設定するスケール。 |
| Enabled Trigger Gizmo Color | `enabledTriggerGizmoColor` | `Color` | – | 有効化トリガーの範囲を示すギズモ色。 |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | マップのギズモと編集ハンドルを表示する。 |
| Update All Map Tiles Every Frame | `updateAllMapTilesEveryFrame` | `bool` | – | 全マップタイルのメッシュを毎フレーム再計算する。 / 表示条件: `showGizmo` がオンのとき |
| Show Map Parts Gizmo | `showMapPartsGizmo` | `bool` | – | 各マップパーツのギズモを表示する。 / 表示条件: `showGizmo` がオンのとき |
| Use Same Line Color | `useSameLineColor` | `bool` | – | 全パーツの線色を`mapLinesColor`に統一する。 / 表示条件: `showGizmo` がオンのとき |
| Map Lines Color | `mapLinesColor` | `Color` | – | `useSameLineColor`有効時のパーツ輪郭線の色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | – | 床の移動ハンドルを描くときの色。 / 表示条件: `showGizmo` がオンのとき |
| Show Map Parts Text Gizmo | `showMapPartsTextGizmo` | `bool` | – | マップパーツのテキスト位置にギズモを表示する。 / 表示条件: `showGizmo` がオンのとき |

### Handle Vertex Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Handle For Vertex | `useHandleForVertex` | `bool` | – | 床の位置をシーンビューでドラッグ移動できるようにする。 / 表示条件: `showGizmo` がオンのとき |
| Handle Radius | `handleRadius` | `float` | – | 床移動ハンドルの当たり判定半径。 / 表示条件: `showGizmo.boolValue && useHandleForVertex.boolValue` |
| Show Vertex Handles | `showVertexHandles` | `bool` | – | 頂点ハンドルの表示を切り替える。 / 表示条件: `showGizmo` がオンのとき |

### Building Triggers Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Building Triggers Line | `showBuildingTriggersLine` | `bool` | – | 建物親から建物トリガーへ線を描く。 / 表示条件: `showGizmo` がオンのとき |
| Building Triggers Line Color | `buildingTriggersLineColor` | `Color` | – | 建物トリガーへ引く線に使う色。 / 表示条件: `showGizmo.boolValue && showBuildingTriggersLine.boolValue` |
| Show Building Triggers | `showBuildingTriggers` | `bool` | – | 建物トリガー位置に球とラベルを表示する。 / 表示条件: `showGizmo` がオンのとき |
| Building Triggers Color | `buildingTriggersColor` | `Color` | – | 建物トリガー位置に描く球の色。 / 表示条件: `showGizmo.boolValue && showBuildingTriggers.boolValue` |
| Show Building Triggers Cubes | `showBuildingTriggersCubes` | `bool` | – | 建物トリガーの範囲を立方体で表示する。 / 表示条件: `showGizmo` がオンのとき |
| Building Triggers Cubes Color | `buildingTriggersCubesColor` | `Color` | – | 建物トリガーの立方体に使う色。 / 表示条件: `showGizmo.boolValue && showBuildingTriggersCubes.boolValue` |

### Floors Triggers Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Floor Triggers Line | `showFloorTriggersLine` | `bool` | – | 各階から階トリガーへ線を描く。 / 表示条件: `showGizmo` がオンのとき |
| Floor Triggers Line Color | `floorTriggersLineColor` | `Color` | – | 階トリガーへ引く線に設定する色。 / 表示条件: `showGizmo.boolValue && showFloorTriggersLine.boolValue` |
| Show Floor Triggers | `showFloorTriggers` | `bool` | – | 階トリガー位置に球とラベルを表示する。 / 表示条件: `showGizmo` がオンのとき |
| Floor Triggers Color | `floorTriggersColor` | `Color` | – | 階トリガー位置に描く球の表示色。 / 表示条件: `showGizmo.boolValue && showFloorTriggers.boolValue` |
| Show Floor Triggers Cubes | `showFloorTriggersCubes` | `bool` | – | 階トリガーの範囲を立方体で表示する。 / 表示条件: `showGizmo` がオンのとき |
| Floor Triggers Cubes Color | `floorTriggersCubesColor` | `Color` | – | 階トリガーの立方体に設定する色。 / 表示条件: `showGizmo.boolValue && showFloorTriggersCubes.boolValue` |
| Show Map Part Enabled Trigger | `showMapPartEnabledTrigger` | `bool` | – | パーツ有効化トリガーの範囲を表示する。 / 表示条件: `showGizmo` がオンのとき |

### Map Part 3d Mesh Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Generate3d Meshes Active | `generate3dMeshesActive` | `bool` | – | マップパーツの3Dメッシュ生成を有効にする。 / 表示条件: `show3dSettings` がオンのとき |
| Generate3d Meshes Show Gizmo | `generate3dMeshesShowGizmo` | `bool` | – | 3Dメッシュの高さと範囲のギズモを表示する。 / 表示条件: `show3dSettings.boolValue && generate3dMeshesActive.boolValue` |
| Generate Full3d Map Meshes | `generateFull3dMapMeshes` | `bool` | – | 個別指定がなくても全パーツの3Dメッシュを生成する。 / 表示条件: `show3dSettings.boolValue && generate3dMeshesActive.boolValue` |
| Map Part3d Height | `mapPart3dHeight` | `float` | 1 | 生成する3Dメッシュの高さを指定する。 / 表示条件: `show3dSettings.boolValue && generate3dMeshesActive.boolValue` |
| Map Part3d Offset | `mapPart3dOffset` | `Vector3` | – | パーツ中心から3Dメッシュ底面までの位置ずれ。 / 表示条件: `show3dSettings.boolValue && generate3dMeshesActive.boolValue` |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `buildingList` | `List<buildingInfo>` | new List<buildingInfo> () | – |
| `mapSystemList` | `List<mapSystem>` | new List<mapSystem> () | – |
| `mapSystemInfoList` | `List<mapSystemInfo>` | new List<mapSystemInfo> () | – |
| `mapIconTypes` | `List<mapIconType>` | new List<mapIconType> () | – |
| `generate3dMapPartMesh` | `bool` | – | – |
| `show3dSettings` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | シングルトンとして自身を登録し、既に別インスタンスがあれば自身のGameObjectを破棄する。 |
| `updateMainMapSystemList()` | `mapSystemInfoList`の各`mainMapSystem`を`mapSystemList`へ重複なく追加する。 |
| `getAndIncreaselastMapObjectInformationIDAssigned()` | `lastMapObjectInformationIDAssigned`を1増やして返し、次のマップオブジェクト用IDを発行する。 |
| `setlastMapObjectInformationIDAssignedValue(int newValue)` | `lastMapObjectInformationIDAssigned`に値を代入するだけ。 |
| `addMapObject(bool visibleInAllBuildings, bool visibleInAllFloors, bool calculateFloorAtStart, GameObject obj, string type, Vector3 offset, int ID, int mapPartIndex, int buildingIndex, float extraIconSizeOnMap, bool followCameraRotation, bool followObjectRotation, bool setCustomCompassSettings, bool useCompassIcon, GameObject compassIconPrefab, float verticalOffset)` | 全設定を各`mapSystem.addMapObject`へ転送し、対象オブジェクトのアイコンを登録する。 |
| `removeMapObject(GameObject obj, bool isPathElement)` | 各マップシステムから指定オブジェクトのアイコン削除を実行する。 |
| `enableOrDisableSingleMapIconByID(int ID, bool value)` | 各マップシステムでID指定のアイコン表示を`value`に切り替える。 |
| `changeMapObjectIconFloor(GameObject objectToSearch, int newFloorIndex)` | 各マップシステムで指定オブジェクトのアイコンを`newFloorIndex`の階へ移動する。 |
| `changeMapObjectIconFloorByPosition(GameObject objectToSearch)` | 各マップシステムでオブジェクトの現在位置から階を判定しアイコンの階を更新する。 |
| `setnewBuilingAndFloorIndexToMapObject(mapSystem.mapObjectInfo mapObjectInfoToModify, int newBuildingIndex, int newFloorIndex)` | 各マップシステムで指定`mapObjectInfo`の建物・階インデックスを新しい値に設定する。 |
| `getBuldingIndexByName(string buildingName)` | 名前が一致する建物のインデックスを返し、見つからなければ-1を返す。 |
| `getAllBuildings()` | 全建物・全階について`GetAllFloorParts`を呼び、階パーツ情報を再収集する。 |
| `changeCurrentFloor(GameObject currentTriggerFloor)` | トリガーに対応する階を有効化し、検出中のプレイヤーのマップシステムの現在階と階数表示を更新する。 |
| `setCurrentFloorByFloorNumber(int buildingIndex, int floorNumber)` | 指定建物内で`floorNumber`に一致する階だけをアクティブにし他の階を非アクティブにする。 |
| `setCurrentFloorByFloorIndex(int buildingIndex, int floorIndex)` | インデックスが負なら何もせず、指定階だけをアクティブにして他の階を無効化する。 |
| `setFloorActiveState(int buildingIndex, int floorIndex, bool state)` | インデックスが負なら何もせず、指定した1階の`floor`オブジェクトのアクティブ状態だけを変更する。 |
| `enableOrDisableSingleMapIconByMapPartIndex(int mapPartBuildingIndex, int mapPartIndex, int mapPartFloorIndex, bool value)` | 各マップシステムで建物・パーツ・階の位置を指定して単一アイコンの表示を切り替える。 |
| `enableOrDisabled2dMap(bool state, int buildingIndex)` | 指定建物の`buildingFloorsParent`だけを`state`でアクティブ/非アクティブにする。 |
| `setCurrentObjectToChangeBuildingInfo(GameObject newCharacter)` | `currentCharacterToUse`を新しいキャラクターに差し替えるだけ。 |
| `setCurrentMapPartIndex(int newValue)` | 変更対象キャラクターに対応するマップシステムの現在マップパーツインデックスを`newValue`に更新する。 |
| `getPlayerGameObject(GameObject newPlayerDetected)` | `currentPlayerDetected`に検出したプレイヤーを代入するだけ。 |
| `changeCurrentBuilding(GameObject currentTriggerBuilding)` | トリガーに対応する建物を有効化し、検出中のプレイヤーのマップシステムの建物と階数表示を更新する。 |
| `changeCurrentBuilding(int newCurrentBuildingIndex, GameObject newCharacter)` | 指定インデックスの建物を有効化し、指定キャラクターのマップシステムの建物と階数表示を更新する。 |
| `setCurrentBuildingByBuildingIndex(int buildingIndex)` | 指定建物の`buildingFloorsParent`だけをアクティブにし他の建物を非アクティブにする。 |
| `setBuildingAndFloorInfoToObject(GameObject objectToCheck, Transform buildingParent, Transform floorParent)` | 対象の`mapObjectInformation`に、親Transformが一致する建物と階のインデックスを設定する。 |
| `addMapPart3dMeshToFloorParent(GameObject mapPart3dMesh, GameObject mapPartGameObject)` | 3Dメッシュを該当階の`mapPart3dMeshesParent`配下へ移し、必要なら親を生成して非表示にする。 |
| `enableOrDisabled3dMap(bool state, int buildingIndex)` | 指定建物の各階の`mapPart3dMeshesParent`を`state`でまとめて表示切替する。 |
| `updateMapPart3dMeshPosition()` | 無効化された階の全パーツの3Dメッシュ位置を`mapPart3dOffset`で更新する。 |
| `enableOrDisableMapPart3dMesh(bool state)` | 無効化された階の全パーツで3Dメッシュの表示を`state`に合わせる。 |
| `set3dMapPartMeshColor(Color newColor, bool setOriginalColor, int currentBuildingIndex, int currentFloorIndex, int currentMapPartIndex)` | 指定パーツの3Dメッシュ色を`newColor`に変更し、`setOriginalColor`が真なら元の色へ戻す。 |
| `removeMapPart3dMesh()` | 無効化された階の全パーツから3Dメッシュを削除する。 |
| `generateMapPart3dMesh()` | 無効化された階の全パーツで`mapPart3dHeight`を使い3Dメッシュを生成する。 |
| `setGenerate3dMapPartMeshState()` | `generate3dMapPartMesh`を反転し、全パーツのビルダーへその状態を反映する。 |
| `setGenerate3dMapPartMeshStateFromEditor()` | エディタ用にフラグを反転し、全パーツのビルダーへエディタ版の設定を反映する。 |
| `setGenerate3dMapPartMeshStateToFloor(bool value, int buildingIndex, int floorIndex)` | 指定建物・階の全パーツに3Dメッシュ生成状態`value`を設定する。 |
| `setGenerate3dMapPartMeshStateToFloorFromEditor(bool value, int buildingIndex, int floorIndex)` | 指定階の全パーツにエディタ版の生成状態`value`を設定しコンポーネントを更新する。 |
| `addNewMapPart(Transform mapPartParent)` | 指定階の子として90度回転したパーツを生成し、`mapTileBuilder`を付けて両リストへ登録する。 |
| `addNewMapPartFromMapCreator(int buildingIndex, int floorIndex)` | 指定建物・階に新しいマップパーツを生成して両リストへ追加しコンポーネントを更新する。 |
| `removeMapPart(int buildingIndex, int floorIndex, int mapPartIndex)` | 指定パーツを即時破棄してリストから除き、`GetAllFloorParts`で階情報を再構築する。 |
| `removeMapPart(Transform mapPartParent, GameObject mapPartToDelete)` | 親から階を特定して対象パーツをリストから外して破棄し、階情報を再収集する。 |
| `removeAllMapParts(int buildingIndex, int floorIndex)` | 指定階の全パーツを即時破棄し、パーツリストを空にして更新する。 |
| `duplicateMapPart(Transform mapPartParent, GameObject mapPartToDuplicate)` | パーツを複製して同じ階に配置し、名前とインデックスを振り直して両リストへ追加する。 |
| `addNewFloor(int buildingIndex)` | 指定建物に`Floor-XXX`の階と初期パーツを生成し、階数とリストを更新する。 |
| `removeFloor(int buildingIndex, int floorIndex)` | 階の全パーツと切替トリガーを削除して階情報を外し、残りの階情報を再収集する。 |
| `removeAllFloors(int buildingIndex)` | 指定建物の全階パーツとトリガー・階オブジェクトを破棄し、階リストを空にする。 |
| `renameFloor(int buildingIndex, int floorIndex)` | `floorInfo`の`Name`を階オブジェクト名へ反映し、コンポーネントを更新する。 |
| `addTriggerToChangeFloor(int buildingIndex, int floorIndex)` | 階切替トリガーをプレハブから生成し、対象階を送るよう設定して親とリストへ登録する。 |
| `removeTriggerToChangeFloor(int buildingIndex, int floorIndex, int triggerIndex)` | 指定トリガーを破棄してリストから除き、最後の1つなら親オブジェクトも破棄する。 |
| `removeTriggerToChangeFloorList(int buildingIndex, int floorIndex)` | 階の全切替トリガーと親オブジェクトを破棄し、リストを空にする。 |
| `enableOrDisableAllFloorParts(bool state, int buildingIndex, int floorIndex)` | 指定階の全パーツの有効状態をエディタ用設定で`state`に揃える。 |
| `enableOrDisableFloorPart(bool state, int buildingIndex, int floorIndex, int mapPartIndex)` | 指定した1パーツの有効状態をエディタ用設定で`state`に変更する。 |
| `renameBuilding(int index)` | `buildingInfo`の`Name`を建物親オブジェクト名へ反映する。 |
| `addNewBuilding()` | 建物親と`Building Content`を生成してリストへ追加し、最初の階も作成する。 |
| `removeBuilding(int buildingIndex)` | 指定建物の全パーツを削除してリストから外し、建物親を破棄して建物情報を再収集する。 |
| `removeAllBuildings()` | 全建物の階・パーツ・トリガー・親オブジェクトを破棄し、建物リストを空にする。 |
| `enableOrDisableAllBuildings(bool state)` | 全建物に対して`enableOrDisableBuilding`を呼び、まとめて有効状態を変更する。 |
| `enableOrDisableBuilding(bool state, int buildingIndex)` | 指定建物の全階全パーツの有効状態を`state`に変更して更新する。 |
| `addTriggerToChangeBuilding(int buildingIndex)` | 建物切替トリガーを生成し、建物親を送るよう設定して親とリストへ登録する。 |
| `removeTriggerToChangeBuilding(int buildingIndex, int triggerIndex)` | 指定トリガーを破棄してリストから除き、最後の1つなら親オブジェクトも破棄する。 |
| `removeTriggerToChangeBuildingList(int buildingIndex)` | 建物の全切替トリガーと親オブジェクトを破棄し、リストを空にする。 |
| `addTriggerToDynamicObject(int buildingIndex, int floorIndex)` | 動的オブジェクト用トリガーを生成し、建物と階の情報を設定してリストへ追加する。 |
| `removeTriggerToDynamicObject(int buildingIndex, int triggerIndex)` | 指定トリガーを破棄してリストから除き、最後の1つなら親オブジェクトも破棄する。 |
| `removeTriggerToDynamicObjectList(int buildingIndex)` | 建物の全動的オブジェクトトリガーと親オブジェクトを破棄し、リストを空にする。 |
| `GetAllFloorParts(int buildingIndex, int floorIndex)` | 階の子オブジェクトを走査して名前と`mapTileBuilder`のインデックスを振り直し、パーツ両リストを再構築する。 |
| `calculateAllMapTileMesh()` | 全建物・全階のパーツで`calculateMapTileMesh`を呼び、タイルメッシュを再計算する。 |
| `removeAllMapTileMesh()` | 全パーツで`removeMapTileRenderer`を呼び、タイルメッシュを削除する。 |
| `setMapObjectInformationID()` | シーン内の全`mapObjectInformation`に1から連番IDを割り当て、次に使うID値を保存する。 |
| `getMapIconTypes()` | 保持している`mapIconTypes`リストを返すだけ。 |
| `setMapIconTypes(int mapSystemIndex)` | 指定マップシステムの`mapIconTypes`をこのリストへコピーする。 |
| `updateMapIconTypesOnMapSystem()` | この`mapIconTypes`の内容を全マップシステムへ反映する。 |
| `addCameraPositionOnMapMenu(int buildingIndex)` | 建物配下にマップメニュー用カメラ位置を生成し、建物情報へ登録する。 |
| `addNewPlayer(mapSystem newMapSystem, GameObject newPlayer, bool callingFunctionOnEditor)` | nullのプレイヤー情報を除去し、既存なら更新・新規なら`mapSystemInfo`を追加する。 |
| `selectChangeBuildingTrigger(int buildingIndex, int triggerIndex)` | 建物切替トリガーをエディタで選択状態にするだけ。 |
| `selectDynamicObjectsTrigger(int buildingIndex, int triggerIndex)` | 動的オブジェクト用トリガーをエディタで選択状態にするだけ。 |
| `selectCurrentFloorTrigger(int buildingIndex, int floorIndex, int triggerIndex)` | 階切替トリガーをエディタで選択状態にするだけ。 |
| `selectCurrentMapPart(int buildingIndex, int floorIndex, int mapPartIndex)` | 指定マップパーツをエディタで選択状態にするだけ。 |
| `updateMapObjectInformationMapSystem()` | シーン内の全`mapObjectInformation`にマップ管理参照を再取得させる。 |
| `updateComponent()` | インスペクタ表示を更新し、シーンを`Update Map Creator`としてダーティにする。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |

## 内部型

- `floorInfo`（class）
- `buildingInfo`（class）
- `mapSystemInfo`（class）
