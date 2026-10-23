# mapObjectInformation

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Map/mapObjectInformation.cs:6`

**概要**: マップ上に表示するオブジェクトのアイコン情報(種類・建物・フロア・表示設定)を保持するコンポーネント。`mapCreator`と`screenObjectivesSystem`への登録・削除や、到達イベントを扱う。

**公式ドキュメント抜粋**（[Map Object Information](../../docs/player-controller-components/player-controller/map-object-information.md)）

> Used to configure an object as an element to be shown in the map system as an icon, like a door, an AI, the player, an elevator, etc.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Map Object Name | `mapObjectName` | `string` | – | マップや目標に表示するオブジェクト名。 |
| Description | `description` | `string` | – | マップUIの情報欄に表示する説明文。 / TextArea (3, 10) |
| Map Object | `mapObject` | `GameObject` | – | アイコンが追従する対象オブジェクト。 |
| Main Screen Objectives Manager Name | `mainScreenObjectivesManagerName` | `string` | "Screen Objectives Manager" | 画面目標マネージャーを名前で指定する設定。 |
| Main Map Creator Manager Name | `mainMapCreatorManagerName` | `string` | "Map Creator" | マップクリエイターを名前で指定する設定。 |

### Map Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Visible In All Buildings | `visibleInAllBuildings` | `bool` | – | 建物に関係なく常にアイコンを表示する。 |
| Visible In All Floors | `visibleInAllFloors` | `bool` | – | 階に関係なく常にアイコンを表示する。 |
| Calculate Floor At Start | `calculateFloorAtStart` | `bool` | – | 開始時に最寄りの階から所属階を自動計算する。 |
| Use Custom Values | `useCustomValues` | `bool` | – | 画面目標リストにも独自設定で登録する。 |
| Offset | `offset` | `Vector3` | – | マップ上のアイコン位置をオブジェクトからずらす。 |
| Extra Icon Size On Map | `extraIconSizeOnMap` | `float` | – | マップアイコンのサイズに加算する値。 |
| Follow Camera Rotation | `followCameraRotation` | `bool` | – | マップアイコンをカメラのY回転に合わせて回す。 |
| Follow Object Rotation | `followObjectRotation` | `bool` | – | マップアイコンをオブジェクトのY回転に合わせる。 |
| Can Change Building And Floor | `canChangeBuildingAndFloor` | `bool` | – | 実行中に建物と階のインデックス変更を許可する。 |
| Activate At Start | `activateAtStart` | `bool` | true | 開始時にマップアイコンを自動で生成する。 |
| Check If Included On Screen Objective On Remove Map Object | `checkIfIncludedOnScreenObjectiveOnRemoveMapObject` | `bool` | – | マップから削除する際、画面目標からも除外する。 |

### Advanced Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disable When Player Has Reached | `disableWhenPlayerHasReached` | `bool` | – | プレイヤー到達で無効になる目標として扱う。 |
| Use Close Distance | `useCloseDistance` | `bool` | true | `triggerRadius`以内に近づくと目標を解除する。 / 表示条件: `disableWhenPlayerHasReached` がオンのとき |
| Show Off Screen Icon | `showOffScreenIcon` | `bool` | true | 目標が画面外のとき方向アイコンを表示する。 / 表示条件: `disableWhenPlayerHasReached` がオンのとき |
| Show Map Window Icon | `showMapWindowIcon` | `bool` | true | 目標をマップ画面のアイコンにも表示する。 / 表示条件: `disableWhenPlayerHasReached` がオンのとき |
| Show Distance | `showDistance` | `bool` | true | 目標が画面内にあるとき距離を表示する。 / 表示条件: `disableWhenPlayerHasReached` がオンのとき |
| Show Distance Off Screen | `showDistanceOffScreen` | `bool` | – | 目標が画面外でも距離を表示する。 / 表示条件: `disableWhenPlayerHasReached` がオンのとき |
| Trigger Radius | `triggerRadius` | `float` | 5 | プレイヤーが目標に到達したと判定する距離。 / 表示条件: `disableWhenPlayerHasReached` がオンのとき |
| Trigger Color | `triggerColor` | `Color` | Color.blue | 到達判定の範囲表示に用いる色。 / 表示条件: `disableWhenPlayerHasReached` がオンのとき |
| Objective Offset | `objectiveOffset` | `float` | – | 目標アイコンをオブジェクトの上方向へずらす。 / 表示条件: `disableWhenPlayerHasReached` がオンのとき |
| Remove Component When Objective Reached | `removeComponentWhenObjectiveReached` | `bool` | true | 目標達成時にこのコンポーネントを削除する。 / 表示条件: `disableWhenPlayerHasReached` がオンのとき |
| Set Custom Compass Settings | `setCustomCompassSettings` | `bool` | – | アイコン種別の設定ではなく独自のコンパス設定を使う。 / 表示条件: `disableWhenPlayerHasReached` がオンのとき |
| Use Compass Icon | `useCompassIcon` | `bool` | – | コンパスに表示するアイコンを生成する。 / 表示条件: `disableWhenPlayerHasReached.boolValue && setCustomCompassSettings.boolValue` |
| Compass Icon Prefab | `compassIconPrefab` | `GameObject` | – | コンパス用アイコンとして生成するプレハブ。 / 表示条件: `disableWhenPlayerHasReached.boolValue && setCustomCompassSettings.boolValue` |
| Vertical Offset | `verticalOffset` | `float` | – | コンパスアイコンの縦方向の表示位置を調整する。 / 表示条件: `disableWhenPlayerHasReached.boolValue && setCustomCompassSettings.boolValue` |
| Use Custom Objective Color | `useCustomObjectiveColor` | `bool` | – | アイコン種別の色ではなく`objectiveColor`を使う。 / 表示条件: `disableWhenPlayerHasReached` がオンのとき |
| Remove Custom Objective Color | `removeCustomObjectiveColor` | `bool` | – | 目標の色を変更せず元のままにする。 / 表示条件: `disableWhenPlayerHasReached.boolValue && useCustomObjectiveColor.boolValue` |
| Objective Color | `objectiveColor` | `Color` | – | 目標オブジェクトのマテリアルに適用する色。 / 表示条件: `useCustomObjectiveColor.boolValue && !removeCustomObjectiveColor.boolValue` |

### Unity Event When Point Reached Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Call Event When Point Reached | `callEventWhenPointReached` | `bool` | – | 目標地点に到達したときにイベントを呼び出す。 / 表示条件: `disableWhenPlayerHasReached` がオンのとき |
| Point Reached Event | `pointReachedEvent` | `UnityEvent` | new UnityEvent () | 到達時に実行する`UnityEvent`。 / 表示条件: `disableWhenPlayerHasReached.boolValue && callEventWhenPointReached.boolValue` |

### Map Part Owner Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Belong To Map Part | `belongToMapPart` | `bool` | – | 所属マップパーツの有効状態に連動させる。 |

### Floor Changed Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Change Floor | `useEventsOnChangeFloor` | `bool` | – | 階が切り替わったときにイベントを実行する。 |
| Use Event On Enabled Floor | `useEventOnEnabledFloor` | `bool` | – | 自分の階が有効になったときのイベントを有効にする。 / 表示条件: `useEventsOnChangeFloor` がオンのとき |
| Even On Enabled Floor | `evenOnEnabledFloor` | `UnityEvent` | – | 自分の階が有効になったときに実行するイベント。 / 表示条件: `useEventsOnChangeFloor.boolValue && useEventOnEnabledFloor.boolValue` |
| Use Event On Disabled Floor | `useEventOnDisabledFloor` | `bool` | – | 自分の階から外れたときのイベントを有効にする。 / 表示条件: `useEventsOnChangeFloor` がオンのとき |
| Even On Disabled Floor | `evenOnDisabledFloor` | `UnityEvent` | – | 自分の階から外れたときに実行するイベント。 / 表示条件: `useEventsOnChangeFloor.boolValue && useEventOnDisabledFloor.boolValue` |

### Debug Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Building Index | `buildingIndex` | `int` | – | アイコンを配置する建物のインデックス。 |
| Floor Index | `floorIndex` | `int` | – | アイコンを配置する階のインデックス。 |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | 到達範囲などを示すギズモを表示する。 |
| Gizmo Label Offset | `gizmoLabelOffset` | `float` | – | 目標ラベルを上方向へずらす量。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.white | 到達目標ラベルの文字に使う色。 / 表示条件: `showGizmo` がオンのとき |
| Offset Show Gizmo | `offsetShowGizmo` | `bool` | – | `offset`位置のギズモ表示を有効にする。 / 表示条件: `showGizmo.boolValue && offset.vector3Value != Vector3.zero` |
| Offset Gizmo Color | `offsetGizmoColor` | `Color` | – | オフセット位置のギズモに使う色。 / 表示条件: `offset.vector3Value != Vector3.zero && offsetShowGizmo.boolValue` |
| Offset Radius | `offsetRadius` | `float` | – | オフセット位置に描くギズモ球の半径。 / 表示条件: `offset.vector3Value != Vector3.zero && offsetShowGizmo.boolValue` |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Map Creator Manager | `mapCreatorManager` | `mapCreator` | – | 使用する`mapCreator`への参照。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `isActivate` | `bool` | true | – |
| `typeIndex` | `int` | – | – |
| `typeName` | `string` | – | – |
| `typeNameList` | `string[]` | – | – |
| `currentFloor` | `string` | – | – |
| `floorList` | `string[]` | – | – |
| `mapManager` | `mapSystem` | – | – |
| `buildingName` | `string` | – | – |
| `buildingList` | `string[]` | – | – |
| `currentBuilding` | `string` | – | – |
| `mapPartName` | `string` | – | – |
| `mapPartList` | `string[]` | – | – |
| `mapPartIndex` | `int` | – | – |
| `ID` | `int` | – | – |
| `currentMapObjectInfo` | `mapSystem.mapObjectInfo` | – | – |
| `mapObjectAssigned` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkAssignMapObject()` | 未割り当てなら`mapObject`に自身の`GameObject`を入れ、`mapObjectAssigned`をtrueにする。 |
| `createMapIconInfo()` | 型名が空でなければ`mapCreator`へアイコンを登録し、必要なら画面目標リストにも要素を追加する。 |
| `getScreenObjectivesManager()` | `screenObjectivesSystem`のインスタンスを取得し、無ければシーン上に生成して保持する。 |
| `addMapObject(string mapIconType)` | 現在の設定と`mapIconType`を渡して`mapCreatorManager`にマップアイコンを登録する。 |
| `removeMapObject()` | 画面目標リストとマップからこのオブジェクトを削除し、`mapObjectRemoved`をtrueにする。 |
| `setPathElementInfo(bool showOffScreenIconInfo, bool showMapWindowIconInfo, bool showDistanceInfo)` | 型名を`Path Element`にし、3つの引数で画面外・マップ・距離表示を設定する。 |
| `getMapIconTypeList()` | `mapManager`のアイコン型名を`typeNameList`へ複製して保存する。 |
| `getBuildingList()` | `mapManager`の建物名を`buildingList`へ複製し、建物が無ければ警告を表示する。 |
| `getFloorList()` | 現在の建物のフロア名を`floorList`へ複製し、マップパーツ所属なら`getMapPartList`も呼ぶ。 |
| `checkGetMapManager()` | `mapManager`がnullなら`FindObjectOfType`で`mapSystem`を探して代入する。 |
| `checkGetMapCreatorManager()` | `mapCreator.Instance`の取得・生成・検索で`mapCreatorManager`を確保し、割り当て状態を更新する。 |
| `getCurrentMapManager()` | `mapSystem`と`mapCreator`の参照を取得し直してシーンを保存する。 |
| `getMapPartList()` | 建物・フロアに対応するマップパーツ名を`mapPartList`へ複製し、不正なら0に戻す。 |
| `getIconTypeIndexByName(string iconTypeName)` | 名前からアイコン型のインデックスを引き、見つかれば`typeIndex`と`typeName`を更新する。 |
| `getMapObjectInformation()` | 建物・フロア・アイコン型の各リストをまとめて取得し直す。 |
| `checkIfMapObjectInformationFound()` | `buildingIndex`や`floorIndex`が範囲外なら0などに補正して保存する。 |
| `setCustomValues(bool visibleInAllBuildingsValue, bool visibleInAllFloorsValue, bool calculateFloorAtStartValue, bool useCloseDistanceValue, float triggerRadiusValue, bool showOffScreenIconValue, bool showMapWindowIconValue, bool showDistanceValue, bool showDistanceOffScreenValue, string objectiveIconNameValue, bool useCustomObjectiveColorValue, Color objectiveColorValue, bool removeCustomObjectiveColorValue)` | `useCustomValues`をtrueにし、引数の建物・表示・距離・目標色の設定を一括で反映する。 |
| `changeMapObjectIconFloor(int newFloorIndex)` | `mapCreatorManager`に依頼してこのアイコンの表示フロアを`newFloorIndex`へ変更する。 |
| `changeMapObjectIconFloorByPosition()` | 現在位置から階を判定させ、このアイコンの表示フロアを更新する。 |
| `enableSingleMapIconByID()` | `ID`を指定して`mapCreatorManager`の単一マップアイコンを有効化する。 |
| `assignID(int newID)` | `ID`に`newID`を設定して保存するだけ。 |
| `checkPointReachedEvent()` | 到達イベントが有効で登録があれば`pointReachedEvent`を発火する。 |
| `checkEventOnChangeFloor(int currentBuildingIndex, int currentFloorIndex)` | 現在の建物・フロアが一致するかで有効時と無効時のイベントを呼び分ける。 |
| `setCurrentMapObjectInfo(mapSystem.mapObjectInfo newMapObjectInfo)` | 建物・フロア変更が許可されていれば`currentMapObjectInfo`に参照を保持する。 |
| `setNewBuildingAndFloorIndex(int newBuildingIndex, int newFloorIndex)` | 変更可なら建物・フロア番号を更新し、`mapCreator`側のアイコン情報にも反映する。 |
| `setNewBuildingAndFloorIndexByInspector()` | 変更可ならインスペクタ値の建物・フロア番号を`mapCreator`側のアイコン情報へ反映する。 |
| `setNewBuildingIndex(int newBuildingIndex)` | `buildingIndex`を設定するだけ。 |
| `setNewFloorIndex(int newFloorIndex)` | `floorIndex`を設定するだけ。 |
| `getBuildingIndex()` | `buildingIndex`を返すだけ。 |
| `getFloorIndex()` | `floorIndex`を返すだけ。 |
| `removeComponentWhenObjectiveReachedEnabled()` | `removeComponentWhenObjectiveReached`の値を返すだけ。 |
| `setMapObjectName(string newName)` | `mapObjectName`を設定するだけ。 |
| `getMapObjectName()` | `mapObjectName`が空なら自身の名前、そうでなければその値を返す。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`で変更を保存しシーンを更新するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `pointReachedEvent` | `UnityEvent` | – |
| `evenOnEnabledFloor` | `UnityEvent` | – |
| `evenOnDisabledFloor` | `UnityEvent` | – |
