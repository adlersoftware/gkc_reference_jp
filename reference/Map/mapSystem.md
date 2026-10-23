# mapSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Map/mapSystem.cs:8`

**概要**: `mapUISystem`と`mapCreator`の建物・階情報を仲介し、2D/3Dマップカメラ、プレイヤーやアイコンの追従、コンパス、ズーム、建物・階の切替えをまとめて管理するMonoBehaviour。`mapObjects`に登録した各アイコンへ建物・階・`ID`・マップパーツの情報を付け、マップ表示全体の状態を一元制御する。

**公式ドキュメント抜粋**（[Map System](../../docs/major-systems/map-system.md)）

> The GKC system for creating a Map system for your Player and Points of Interest. Once a new player has been created, if you want to use the map system, you need to drag and drop the Map System prefab (with the same name) in the folder Assets/Game Kit Controller/Prefabs/Map System. Once the hierarchy contains these two elements: Then, go to Character gameObject, Map System inspector, and press the button Map Floor and Icons. Go to Floors, and press the button Search Floor List. The floors configured in the Map Creator inspector will be configured automatically. If you don’t need to use the map system, don’t configure the above steps and it will be disabled. Map Creator Component Map System Component

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Map Enabled | `mapEnabled` | `bool` | – | マップ機能全体の有効状態を切り替える。 |
| Open Menu Enabled | `openMenuEnabled` | `bool` | true | マップメニューを開く入力を許可する。 |
| Change Floor With Triggers | `changeFloorWithTriggers` | `bool` | true | フロア変更トリガーで現在フロアを更新する。 |
| Show Warning Messages | `showWarningMessages` | `bool` | – | 設定不備の警告をログに出力する。 |
| Update Map Icon Types On Start | `updateMapIconTypesOnStart` | `bool` | true | 起動時にアイコン種別を`Map Creator`から取得する。 |
| Search Building List If Not Assigned | `searchBuildingListIfNotAssigned` | `bool` | – | 建物リスト未設定時に自動で検索する。 |
| Check Elements On Awake Enabled | `checkElementsOnAwakeEnabled` | `bool` | true | `Awake`時にUIなどの要素を自動チェックする。 |
| Main Screen Objectives Manager Name | `mainScreenObjectivesManagerName` | `string` | "Screen Objectives Manager" | 画面目標マネージャーの名前を指定する文字列。 |
| Main Map Creator Manager Name | `mainMapCreatorManagerName` | `string` | "Map Creator" | `Map Creator`の名前を指定する文字列。 |
| Ingame Menu Name | `ingameMenuName` | `string` | "Map System" | マップUIを持つゲーム内メニューの名前。 |
| Beacon Icon Type Name | `beaconIconTypeName` | `string` | "Beacon" | ビーコン判定に使うアイコン種別名。 |
| Mark Icon Type Name | `markIconTypeName` | `string` | "Mark" | マーク判定に使うアイコン種別名。 |

### Player Position In Map Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Map Creator Manager | `mapCreatorManager` | `mapCreator` | – | マップデータを管理する`mapCreator`への参照。 |
| Map Camera | `mapCamera` | `GameObject` | – | マップ上を移動するカメラの`GameObject`。 / 表示条件: `showMapComponents` がオンのとき |
| Map System Pivot Transform | `mapSystemPivotTransform` | `Transform` | – | 3Dマップ回転の中心となるピボット。 / 表示条件: `showMapComponents` がオンのとき |
| Map System Camera Transform | `mapSystemCameraTransform` | `Transform` | – | 3Dマップのカメラ角度を受け持つ`Transform`。 / 表示条件: `showMapComponents` がオンのとき |
| Player | `player` | `GameObject` | – | マップに位置を表示するプレイヤー。 / 表示条件: `showMapComponents` がオンのとき |
| Map Render | `mapRender` | `RectTransform` | – | マップ画像を表示する`RectTransform`。 / 表示条件: `showMapComponents` がオンのとき |
| Map Window | `mapWindow` | `RectTransform` | – | マップ表示ウィンドウの`RectTransform`。 / 表示条件: `showMapComponents` がオンのとき |
| Player Map Icon | `playerMapIcon` | `RectTransform` | – | プレイヤーアイコンの`RectTransform`。 / 表示条件: `showMapComponents` がオンのとき |
| Player Icon Child | `playerIconChild` | `RectTransform` | – | プレイヤーアイコンの拡大縮小対象。 / 表示条件: `showMapComponents` がオンのとき |
| Remove Mark Button Image | `removeMarkButtonImage` | `Image` | – | マーク削除ボタンの`Image`。 / 表示条件: `showMapComponents` がオンのとき |
| Quick Travel Button Image | `quickTravelButtonImage` | `Image` | – | クイックトラベルボタンの`Image`。 / 表示条件: `showMapComponents` がオンのとき |
| Use Map Index Window | `useMapIndexWindow` | `bool` | – | マップにアイコン種別一覧を表示する。 / 表示条件: `showMapComponents` がオンのとき |
| Map Object Text Icon | `mapObjectTextIcon` | `GameObject` | – | アイコンのテキスト表示に使うプレハブ。 / 表示条件: `showMapComponents` がオンのとき |
| Use Blur UI Panel | `useBlurUIPanel` | `bool` | true | マップ表示時に背景UIをぼかす。 / 表示条件: `showMapComponents` がオンのとき |
| Player Input | `playerInput` | `playerInputManager` | – | プレイヤーの入力マネージャーへの参照。 / 表示条件: `showMapComponents` がオンのとき |
| Pause Manager | `pauseManager` | `menuPause` | – | メニュー管理の`menuPause`への参照。 / 表示条件: `showMapComponents` がオンのとき |
| Screen Objectives Manager | `screenObjectivesManager` | `screenObjectivesSystem` | – | 目標管理の`screenObjectivesSystem`への参照。 / 表示条件: `showMapComponents` がオンのとき |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | 一人称や運転状態を判定する`playerController`。 / 表示条件: `showMapComponents` がオンのとき |
| Map Creator Manager | `mapCreatorManager` | `mapCreator` | – | マップデータを管理する`mapCreator`への参照。 / 表示条件: `showMapComponents` がオンのとき |
| Player Map Object Information | `playerMapObjectInformation` | `mapObjectInformation` | – | プレイヤーの`mapObjectInformation`への参照。 / 表示条件: `showMapComponents` がオンのとき |
| Main Map Camera | `mainMapCamera` | `Camera` | – | マップを描画する`Camera`。 / 表示条件: `showMapComponents` がオンのとき |
| Map Creator Prefab | `mapCreatorPrefab` | `GameObject` | – | マップ生成に使う`mapCreator`プレハブ。 / 表示条件: `showMapComponents` がオンのとき |

### CONTROL

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Icon Movement Speed | `playerIconMovementSpeed` | `float` | – | マップカメラのプレイヤー追従速度。 / 表示条件: `showMapSettings` がオンのとき |
| Open Map Speed | `openMapSpeed` | `float` | – | マップを開くときのアニメーション速度。 / 表示条件: `showMapSettings` がオンのとき |
| Mouse Drag Map Speed | `mouseDragMapSpeed` | `float` | 4 | マウスドラッグでのマップ移動速度。 / 表示条件: `showMapSettings` がオンのとき |
| Keys Drag Map Speed | `keysDragMapSpeed` | `float` | 1 | キー入力でマップを動かす速度。 / 表示条件: `showMapSettings` がオンのとき |
| Get Closest Floor To Player By Distance | `getClosestFloorToPlayerByDistance` | `bool` | – | プレイヤーに最も近いフロアを自動選択する。 / 表示条件: `showMapSettings` がオンのとき |
| Map Camera Movement Type | `mapCameraMovementType` | `mapCameraMovement` | – | マップカメラを配置する平面の向き。 / 表示条件: `showMapSettings` がオンのとき |
| Recenter Camera Speed | `recenterCameraSpeed` | `float` | 2 | カメラをプレイヤー位置へ戻す速度。 / 表示条件: `showMapSettings` がオンのとき |

### ROTATION

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Rotate Map | `rotateMap` | `bool` | – | マップをプレイヤーの向きに合わせて回転する。 / 表示条件: `showMapSettings` がオンのとき |
| Smooth Rotation Map | `smoothRotationMap` | `bool` | – | マップ回転を補間して滑らかにする。 / 表示条件: `showMapSettings.boolValue && rotateMap.boolValue` |
| Rotation Speed | `rotationSpeed` | `float` | – | マップ回転の補間速度を決める値。 / 表示条件: `showMapSettings.boolValue && rotateMap.boolValue` |

### CIRCLE MAP

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Circle Map | `usingCircleMap` | `bool` | – | ミニマップを円形の表示に切り替える。 / 表示条件: `showMapSettings` がオンのとき |
| Circle Map Radius | `circleMapRadius` | `float` | – | サークルマップの表示半径（UI座標）。 / 表示条件: `showMapSettings.boolValue && usingCircleMap.boolValue` |

### ICONS

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Off Screen Icons | `showOffScreenIcons` | `bool` | – | 画面外のアイコンを端に表示する。 / 表示条件: `showMapSettings` がオンのとき |
| Icon Size | `iconSize` | `float` | – | マップ上のアイコンの基本サイズ。 / 表示条件: `showMapSettings` がオンのとき |
| Max Icon Size | `maxIconSize` | `float` | – | テキスト位置計算の基準となるアイコンサイズ。 / 表示条件: `showMapSettings` がオンのとき |
| Off Screen Icon Size | `offScreenIconSize` | `float` | – | 画面外に出たアイコンの表示サイズ。 / 表示条件: `showMapSettings` がオンのとき |
| Open Map Icon Size Multiplier | `openMapIconSizeMultiplier` | `float` | – | マップを開いたときのアイコン倍率。 / 表示条件: `showMapSettings` がオンのとき |
| Change Icon Size Speed | `changeIconSizeSpeed` | `float` | – | アイコンサイズ変化の補間速度。 / 表示条件: `showMapSettings` がオンのとき |
| Show Icons By Floor | `showIconsByFloor` | `bool` | – | 現在のフロアのアイコンだけ表示する。 / 表示条件: `showMapSettings` がオンのとき |
| Border Off Screen | `borderOffScreen` | `float` | – | 画面端に寄せるアイコンの内側余白。 / 表示条件: `showMapSettings` がオンのとき |
| Use Text In Icons | `useTextInIcons` | `bool` | – | アイコンに名前テキストを表示する。 / 表示条件: `showMapSettings` がオンのとき |
| Text Icons Offset | `textIconsOffset` | `Vector2` | – | アイコンからのテキスト位置オフセット。 / 表示条件: `showMapSettings` がオンのとき |
| Map Object Text Icon Color | `mapObjectTextIconColor` | `Color` | Color.white | アイコンに添えるテキストの色。 / 表示条件: `showMapSettings` がオンのとき |
| Map Object Text Size | `mapObjectTextSize` | `int` | 20 | アイコンテキストの文字サイズ。 / 表示条件: `showMapSettings` がオンのとき |
| Player Use Map Object Information | `playerUseMapObjectInformation` | `bool` | – | プレイヤーアイコンを`mapObjectInformation`で管理する。 / 表示条件: `showMapSettings` がオンのとき |
| Player Icon Offset | `playerIconOffset` | `Vector3` | – | プレイヤーアイコンの位置補正値。 / 表示条件: `showMapSettings` がオンのとき |
| Use Current Map Icon Pressed | `useCurrentMapIconPressed` | `bool` | – | 押したアイコンに選択マーカーを追従させる。 / 表示条件: `showMapSettings` がオンのとき |
| Mini Map Window Enabled In Game | `miniMapWindowEnabledInGame` | `bool` | true | ゲーム中にミニマップを表示する。 / 表示条件: `showMapSettings` がオンのとき |
| Mini Map Window Smooth Opening | `miniMapWindowSmoothOpening` | `bool` | true | ミニマップ開閉を滑らかに補間する。 / 表示条件: `showMapSettings` がオンのとき |
| Mini Map Window With Mask | `miniMapWindowWithMask` | `bool` | – | マップ表示をマスク枠で切り抜く。 / 表示条件: `showMapSettings` がオンのとき |
| Check Minimap Window Active State On Other Menus Enabled | `checkMinimapWindowActiveStateOnOtherMenusEnabled` | `bool` | – | 他のメニュー表示中はミニマップを隠す。 / 表示条件: `showMapSettings` がオンのとき |

### MAP CURSOR SETTINGS

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Map Cursor | `useMapCursor` | `bool` | – | マップ上にカーソルを表示する。 / 表示条件: `showMapSettings` がオンのとき |
| Show Info Icon Inside Cursor | `showInfoIconInsideCursor` | `bool` | – | カーソル付近のアイコン情報を表示する。 / 表示条件: `showMapSettings.boolValue && useMapCursor.boolValue` |
| Max Distance To Map Icon | `maxDistanceToMapIcon` | `int` | – | カーソルがアイコン情報を拾う距離。 / 表示条件: `useMapCursor.boolValue && showInfoIconInsideCursor.boolValue` |

### 2D ZOOM SETTINGS

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Zoom When Open | `zoomWhenOpen` | `float` | – | マップを開いたときのズーム値。 / 表示条件: `showMapSettings` がオンのとき |
| Zoom When Close | `zoomWhenClose` | `float` | – | マップを閉じたときのズーム値。 / 表示条件: `showMapSettings` がオンのとき |
| Open Close Zoom Speed | `openCloseZoomSpeed` | `float` | – | マップ開閉時のズーム補間速度。 / 表示条件: `showMapSettings` がオンのとき |
| Zoom Speed | `zoomSpeed` | `float` | – | ズーム操作1秒あたりの変化量。 / 表示条件: `showMapSettings` がオンのとき |
| Max Zoom | `maxZoom` | `float` | – | 2Dマップで拡大できる最大ズーム値。 / 表示条件: `showMapSettings` がオンのとき / Range (0, 200) |
| Min Zoom | `minZoom` | `float` | – | 2Dマップで縮小できる最小ズーム値。 / 表示条件: `showMapSettings` がオンのとき / Range (0, 200) |
| Zoom To Activate Icons | `zoomToActivateIcons` | `float` | – | このズーム値以下でアイコンを表示する。 / 表示条件: `showMapSettings` がオンのとき |
| Zoom To Activate Text Icons | `zoomToActivateTextIcons` | `float` | 100 | このズーム値以下でテキストを表示する。 / 表示条件: `showMapSettings` がオンのとき |

### 3D ZOOM SETTINGS

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Zoom When Open3d | `zoomWhenOpen3d` | `float` | – | 3Dマップを開いたときのズーム値。 / 表示条件: `showMapSettings` がオンのとき |
| Zoom When Close3d | `zoomWhenClose3d` | `float` | – | 3Dマップを閉じたときのズーム値。 / 表示条件: `showMapSettings` がオンのとき |
| Open Close Zoom Speed3d | `openCloseZoomSpeed3d` | `float` | – | 3Dマップ開閉時のズーム補間速度。 / 表示条件: `showMapSettings` がオンのとき |
| Zoom Speed3d | `zoomSpeed3d` | `float` | – | 3Dズーム操作1秒あたりの変化量。 / 表示条件: `showMapSettings` がオンのとき |
| Max Zoom3d | `maxZoom3d` | `float` | – | 3Dマップで拡大できる最大ズーム値。 / 表示条件: `showMapSettings` がオンのとき / Range (0, 200) |
| Min Zoom3d | `minZoom3d` | `float` | – | 3Dマップで縮小できる最小ズーム値。 / 表示条件: `showMapSettings` がオンのとき / Range (0, 200) |
| Zoom To Activate Icons3d | `zoomToActivateIcons3d` | `float` | – | このズーム値以下で3Dアイコンを表示する。 / 表示条件: `showMapSettings` がオンのとき |
| Zoom To Activate Text Icons3d | `zoomToActivateTextIcons3d` | `float` | 100 | このズーム値以下で3Dテキストを表示する。 / 表示条件: `showMapSettings` がオンのとき |
| Set Color On Current3d Map Part | `setColorOnCurrent3dMapPart` | `bool` | – | 現在の3Dマップパーツに色を付ける。 / 表示条件: `showMapSettings` がオンのとき |
| Color On Current3d Map Part | `colorOnCurrent3dMapPart` | `Color` | Color.blue | 現在の3Dマップパーツに付ける色。 / 表示条件: `showMapSettings.boolValue && setColorOnCurrent3dMapPart.boolValue` |

### MARKS

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disabled Remove Mark Color | `disabledRemoveMarkColor` | `Color` | – | マーク削除ボタンの無効時の表示色。 / 表示条件: `showMapSettings` がオンのとき |
| Disabled Quick Travel Color | `disabledQuickTravelColor` | `Color` | – | クイックトラベルボタンの無効時色。 / 表示条件: `showMapSettings` がオンのとき |

### 3D Map Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Map3d Enabled | `map3dEnabled` | `bool` | – | 3Dマップ表示の有効状態を切り替える。 / 表示条件: `showMapSettings` がオンのとき |
| Map3d Position Speed | `map3dPositionSpeed` | `float` | 30 | 3Dマップ表示時の移動速度を決める。 / 表示条件: `showMapSettings.boolValue && map3dEnabled.boolValue` |
| Map3d Rotation Speed | `map3dRotationSpeed` | `float` | 10 | 3Dマップ表示時の回転速度を決める。 / 表示条件: `showMapSettings.boolValue && map3dEnabled.boolValue` |
| Range Angle X | `rangeAngleX` | `Vector2` | – | 3Dマップの上下回転の制限範囲。 / 表示条件: `showMapSettings.boolValue && map3dEnabled.boolValue` |
| Range Angle Y | `rangeAngleY` | `Vector2` | – | 3Dマップの左右回転の制限範囲。 / 表示条件: `showMapSettings.boolValue && map3dEnabled.boolValue` |
| Transtion To3d Speed | `transtionTo3dSpeed` | `float` | 0.5f | 2Dと3Dの表示切替の補間速度。 / 表示条件: `showMapSettings.boolValue && map3dEnabled.boolValue` |
| Max Time Between Transition | `maxTimeBetweenTransition` | `float` | 0.5f | 2Dと3Dの切替にかける時間。 / 表示条件: `showMapSettings.boolValue && map3dEnabled.boolValue` |
| Reset3d Camera Speed | `reset3dCameraSpeed` | `float` | 20 | 3Dカメラ角度を初期状態へ戻す速度。 / 表示条件: `showMapSettings.boolValue && map3dEnabled.boolValue` |
| Inital3d Camera Rotation | `inital3dCameraRotation` | `Vector2` | – | 3D表示開始時のカメラ初期角度。 / 表示条件: `showMapSettings.boolValue && map3dEnabled.boolValue` |
| Hide Offscreen Icons On3d View | `hideOffscreenIconsOn3dView` | `bool` | – | 3D表示で画面外アイコンを隠す。 / 表示条件: `showMapSettings.boolValue && map3dEnabled.boolValue` |
| Show Icons On3d View | `showIconsOn3dView` | `bool` | – | 3D表示でもアイコンを表示する。 / 表示条件: `showMapSettings.boolValue && map3dEnabled.boolValue` |
| Use3d Mesh For Player | `use3dMeshForPlayer` | `bool` | – | 3D表示でプレイヤーメッシュを使う。 / 表示条件: `showMapSettings.boolValue && map3dEnabled.boolValue` |
| Player3d Mesh | `player3dMesh` | `GameObject` | – | 3D表示に使うプレイヤーメッシュ。 / 表示条件: `showMapSettings.boolValue && map3dEnabled.boolValue` |

### Map Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event If Map Enabled | `useEventIfMapEnabled` | `bool` | – | マップ有効時にイベントを実行する。 / 表示条件: `showMapSettings` がオンのとき |
| Event If Map Enabled | `eventIfMapEnabled` | `UnityEvent` | – | マップ有効時に呼び出すイベント。 / 表示条件: `showMapSettings.boolValue && useEventIfMapEnabled.boolValue` |
| Use Event If Map Disabled | `useEventIfMapDisabled` | `bool` | – | マップ無効時にイベントを実行する。 / 表示条件: `showMapSettings` がオンのとき |
| Event If Map Disabled | `eventIfMapDisabled` | `UnityEvent` | – | マップ無効時に呼び出すイベント。 / 表示条件: `showMapSettings.boolValue && useEventIfMapDisabled.boolValue` |
| Mark Prefab | `markPrefab` | `GameObject` | – | マーク設置時に生成するプレハブ。 / 表示条件: `showMarkSettings` がオンのとき |
| Set Mark On Curren Building | `setMarkOnCurrenBuilding` | `bool` | – | マークに現在の建物情報を紐付ける。 / 表示条件: `showMarkSettings` がオンのとき |
| Set Mark On Current Floor | `setMarkOnCurrentFloor` | `bool` | – | マークに現在のフロア情報を紐付ける。 / 表示条件: `showMarkSettings` がオンのとき |
| Raycast Distance To Place Mark | `raycastDistanceToPlaceMark` | `float` | 1000 | マーク設置レイキャストの距離。 / 表示条件: `showMarkSettings` がオンのとき |
| Layer Mask To Place Mark | `layerMaskToPlaceMark` | `LayerMask` | 1 << 0 \| 1 << 23 | マーク設置レイキャストの対象レイヤー。 / 表示条件: `showMarkSettings` がオンのとき |
| Use Raycast To Place Mark On2d Map | `useRaycastToPlaceMarkOn2dMap` | `bool` | – | 2Dマップでもレイキャストで位置を決める。 / 表示条件: `showMarkSettings` がオンのとき |
| Use Map Camera As Raycast Poisition On2d Map | `useMapCameraAsRaycastPoisitionOn2dMap` | `bool` | – | 2Dマップのレイキャスト起点にマップカメラを使う。 / 表示条件: `showMarkSettings` がオンのとき |
| Compass Directions | `compassDirections` | `Transform` | – | コンパスアイコンの基準となる`Transform`。 / 表示条件: `showCompassComponents` がオンのとき |
| North Game Object | `northGameObject` | `GameObject` | – | 北方向としてコンパスに表示する`GameObject`。 / 表示条件: `showCompassComponents` がオンのとき |
| South Game Object | `southGameObject` | `GameObject` | – | 南方向としてコンパスに表示する`GameObject`。 / 表示条件: `showCompassComponents` がオンのとき |
| East Game Object | `eastGameObject` | `GameObject` | – | 東方向としてコンパスに表示する`GameObject`。 / 表示条件: `showCompassComponents` がオンのとき |
| West Game Object | `westGameObject` | `GameObject` | – | 西方向としてコンパスに表示する`GameObject`。 / 表示条件: `showCompassComponents` がオンのとき |
| North East Game Object | `northEastGameObject` | `GameObject` | – | 北東方向としてコンパスに表示する`GameObject`。 / 表示条件: `showCompassComponents` がオンのとき |
| South West Game Object | `southWestGameObject` | `GameObject` | – | 南西方向としてコンパスに表示する`GameObject`。 / 表示条件: `showCompassComponents` がオンのとき |
| South East Game Object | `southEastGameObject` | `GameObject` | – | 南東方向としてコンパスに表示する`GameObject`。 / 表示条件: `showCompassComponents` がオンのとき |
| Northwest Game Object | `northwestGameObject` | `GameObject` | – | 北西方向としてコンパスに表示する`GameObject`。 / 表示条件: `showCompassComponents` がオンのとき |

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Compass Enabled | `compassEnabled` | `bool` | – | 方位コンパスを画面に表示する。 / 表示条件: `showCompassSettings` がオンのとき |
| Compass Offset | `compassOffset` | `float` | – | コンパスアイコンの上下オフセット。 / 表示条件: `showCompassSettings` がオンのとき |
| Compass Scale | `compassScale` | `float` | 1 | コンパスアイコン間隔を広げる倍率。 / 表示条件: `showCompassSettings` がオンのとき |
| Show Intermediate Directions | `showIntermediateDirections` | `bool` | – | 斜め方角もコンパスに表示する。 / 表示条件: `showCompassSettings` がオンのとき |
| Maximum Left Distance | `maximumLeftDistance` | `float` | – | コンパスの左方向への最大移動距離。 / 表示条件: `showCompassSettings` がオンのとき |
| Maximum Right Distance | `maximumRightDistance` | `float` | – | コンパスの右方向への最大移動距離。 / 表示条件: `showCompassSettings` がオンのとき |

### Compass Orientation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Player Transform Orientation On Compass On Third Person | `usePlayerTransformOrientationOnCompassOnThirdPerson` | `bool` | – | 三人称時にプレイヤーの向きを基準にする。 / 表示条件: `showCompassSettings` がオンのとき |
| Use Player Transform Orientation On Compass On First Person | `usePlayerTransformOrientationOnCompassOnFirstPerson` | `bool` | true | 一人称時にプレイヤーの向きを基準にする。 / 表示条件: `showCompassSettings` がオンのとき |
| Use Player Transform Orientation On Compass On Locked Camera | `usePlayerTransformOrientationOnCompassOnLockedCamera` | `bool` | true | ロックカメラ時にプレイヤーの向きを基準にする。 / 表示条件: `showCompassSettings` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `mainMapUISystem` | `mapUISystem` | – | – |
| `near` | `float` | .3f | – |
| `far` | `float` | 1000f | – |
| `compassIconList` | `List<compassIconInfo>` | new List<compassIconInfo> () | – |
| `floors` | `List<floorInfo>` | new List<floorInfo> () | – |
| `buildingList` | `List<buildingInfo>` | new List<buildingInfo> () | – |
| `mapIconTypes` | `List<mapIconType>` | new List<mapIconType> () | – |
| `markList` | `List<markInfo>` | new List<markInfo> () | – |
| `glossaryList` | `List<glossaryElementInfo>` | new List<glossaryElementInfo> () | – |
| `currentBuildingName` | `string` | – | – |
| `currentBuildingIndex` | `int` | – | – |
| `currentMapPartIndex` | `int` | – | – |
| `previousBuildingIndex` | `int` | – | – |
| `currentFloorIndex` | `int` | – | – |
| `currentFloorNumber` | `int` | – | – |
| `mapOpened` | `bool` | – | – |
| `mapObjects` | `List<mapObjectInfo>` | new List<mapObjectInfo> () | – |
| `showMapComponents` | `bool` | – | – |
| `showMapSettings` | `bool` | – | – |
| `showCompassComponents` | `bool` | – | – |
| `showCompassSettings` | `bool` | – | – |
| `showMapFloorAndIcons` | `bool` | – | – |
| `showMarkSettings` | `bool` | – | – |
| `buildingListString` | `string []` | – | – |
| `floorListString` | `string []` | – | – |
| `currentFloorName` | `string` | – | – |
| `mapPartListString` | `string []` | – | – |
| `currentMapPartName` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkElementsOnAwake()` | 初期化済みなら即返し、アイコン型を取得して`mainMapUISystem`を補完し、初期化済みフラグを立てる。 |
| `checkMapSystemAddedOnMapCreator()` | `mapCreatorManager`を取得し、このマップシステムをプレイヤーとして登録してメインのマップシステム一覧を更新する。 |
| `setSearchBuildingListIfNotAssignedState(bool state)` | `searchBuildingListIfNotAssigned`を指定状態にするだけ。 |
| `setMapContentActiveState(bool state)` | `mainMapUISystem`が割り当て済みならマップ内容の表示状態をそのまま委譲する。 |
| `setMapMenuActiveState(bool state)` | `mainMapUISystem`が割り当て済みならマップメニューの表示状態を委譲して切り替える。 |
| `setMiniMapWindowEnabledInGameState(bool state)` | `miniMapWindowEnabledInGame`を設定するだけ。 |
| `setMiniMapWindowEnabledInGameStateAndUpdateState(bool state)` | ミニマップ有効フラグを設定し、`enableOrDisableMapWindow`でマップウィンドウへ即反映する。 |
| `setMapEnabledState(bool state)` | `mapEnabled`を設定するだけ。 |
| `setCompassEnabledState(bool state)` | `compassEnabled`を設定するだけ。 |
| `setCompassEnabledStateAndUpdateState(bool state)` | コンパス有効フラグを設定し、`updateCompassCurrentEnabledState`で実際の表示へ反映する。 |
| `setMapEnabledStateAndUpdateState(bool state)` | 設定不備なら中断し、`mapEnabled`を設定して有効時は要素を初期化、最後にマップ有効状態を更新する。 |
| `updateMapCurrentEnabledState()` | `mapEnabled`の値でマップウィンドウの表示を切り替える。 |
| `updateCompassCurrentEnabledState()` | `compassEnabled`でコンパスを切り替え、有効なら方位要素を初期化する。 |
| `setCompassInitialState()` | コンパス状態を更新し、マップ無効時は`mapCreatorManager`からアイコン型を取り直す。 |
| `getCameraPosition()` | プレイヤー位置を基準に、`mapCameraMovementType`に応じて`cameraOffset`を加えたマップカメラ位置を返す。 |
| `checkCurrentMapIconPressedParent()` | `useCurrentMapIconPressed`が有効なら`mainMapUISystem`へアイコン押下親の確認を委譲する。 |
| `checkUpdateCompass()` | コンパス有効かつマップ未展開のときだけ`updateCompassIcons`を呼ぶ。 |
| `checkCurrentIconPressed(bool state, Transform mapIconTransform)` | アイコン押下機能が有効なら状態と対象`Transform`を`mainMapUISystem`へ渡す。 |
| `updateCompassIcons()` | プレイヤー位置と向きから各コンパスアイコンの角度を求め、`anchoredPosition`を更新、対象が消えたアイコンは破棄する。 |
| `checkCompassIcon(int index)` | 指定`mapObjects`のコンパスアイコンを一覧から外して破棄する。 |
| `addCompassIcon(GameObject objectToFollow, GameObject newCompassIcon, float verticalOffset, bool useCompassClamp)` | 追従対象とアイコンから`compassIconInfo`を作って`compassIconList`に追加し返す。`verticalOffset`は高さ。 |
| `setCameraSize(float value)` | 実行中のコルーチンを停止し、2Dなら正射影サイズ、3DならFOVを目標値へ補間するコルーチンを開始する。 |
| `assignMapCameraFovValue(float value)` | 3D移行後は射影行列を`Perspective`で作り直し、未移行なら`fieldOfView`を設定、最後に`currentFieldOfView`を更新する。 |
| `assignMapCameraOrthographicValue(float value)` | 3D移行後は正射影行列を設定し、未移行なら`orthographicSize`を更新する。マップ閉時は`currentCameraSize`も同期。 |
| `setNewObjectToFollow(GameObject newObject)` | 追従対象`player`を新しいオブジェクトに差し替えるだけ。 |
| `set2dOr3ddMapView(bool state)` | 2D/3D表示を切り替え、建物メッシュ、射影行列、階アイコン、プレイヤーメッシュの表示を更新する。 |
| `setCurrentMapPartIndex(int newValue)` | `currentMapPartIndex`を設定するだけ。 |
| `setQuick2dMap()` | 強制的に2D表示へ切り替え、3Dマップを無効化して正射影行列を設定、カメラ回転を初期化する。 |
| `BlendToMatrix(Matrix4x4 targetMatrix, float duration)` | 実行中の射影変更を停止し、現在の射影行列から目標行列へ`duration`秒で補間するコルーチンを開始する。 |
| `resetMapCamera3dValues()` | マップカメラを`mapCreatorManager`の子に戻して回転を初期化し、ピボット・カメラ角度・ルック値をリセットする。 |
| `resetCameraPivotRotation(Vector3 pivotEulerRotation, Vector3 cameraEulerRotation, bool resetCameraValues)` | ピボットとカメラを目標角度へ補間し、`resetCameraValues`ならカメラ値も初期化、2D時は射影行列を再ブレンドする。 |
| `recenterCameraPosition()` | 2Dではマップカメラ、3Dではピボットをプレイヤー位置へ`recenterCameraSpeed`で寄せるコルーチンを開始する。 |
| `zoomInEnabled()` | `zoomingIn`をtrueにするだけ。 |
| `zoomInDisabled()` | `zoomingIn`をfalseにするだけ。 |
| `zoomOutEnabled()` | `zoomingOut`をtrueにするだけ。 |
| `zoomOutDisabled()` | `zoomingOut`をfalseにするだけ。 |
| `setUsingScrollbarZoomState(bool state)` | `usingScrollbarZoom`を設定するだけ。 |
| `setZoomByScrollBar(Scrollbar mainZoomScrollbar)` | スクロールバー値×`maxZoom`を2D/3Dの最小・最大ズームでクランプし、`currentCameraSize`を決める。 |
| `addMapObject(bool visibleInAllBuildings, bool visibleInAllFloors, bool calculateFloorAtStart, GameObject obj, string type, Vector3 offset, int ID, int mapPartIndex, int buildingIndex, float extraIconSizeOnMap, bool followCameraRotation, bool followObjectRotation, bool setCustomCompassSettings, bool useCompassIcon, GameObject compassIconPrefab, float verticalOffset)` | 指定型のアイコンとコンパスアイコンを生成し、建物・階・`ID`などの情報を`mapObjects`へ登録する。既存なら作り直す。 |
| `removeMapObject(GameObject obj, bool isPathElement)` | 対象のマップアイコンとコンパスアイコンを破棄し、マークならオブジェクト自体も削除、`mapObjects`から外す。 |
| `setnewBuilingAndFloorIndexToMapObject(mapObjectInfo mapObjectInfoToModify, int newBuildingIndex, int newFloorIndex)` | `mapObjectInfo`の建物・階インデックスと階番号を更新し、`mapObjectInformation`へ階変更イベントを通知する。 |
| `addMapTextIcon(mapObjectInfo newMapObject)` | アイコン位置にテキストアイコンを生成し、名前・色・サイズを設定して非表示にした上で返す。 |
| `placeMark()` | 現在の階でカメラ位置からレイキャストしてマークを生成し、`markList`へ登録してアイコン情報を作成する。 |
| `removeMark()` | `currentMark`を一覧と`mapObjects`から外し、マーク・アイコン・コンパスアイコンを破棄して削除ボタンを無効色にする。 |
| `changeMapObjectIconFloor(GameObject objectToSearch, int newFloorIndex)` | 該当オブジェクトの`floorNumber`を新しい階インデックスの値に書き換えるだけ。 |
| `changeMapObjectIconFloorByPosition(GameObject objectToSearch)` | マップ有効時、対象位置に最も近い階を求めてその`floorNumber`を設定する。 |
| `getClosestFloorToMapObject(Transform mapObjectTransform)` | Y座標が最も近い階のインデックスを返し、対象がnullなら警告して-1を返す。 |
| `getIconTypeIndexByName(string iconTypeName)` | `mapIconTypes`から一致する型名のインデックスを返し、見つからなければ-1を返す。 |
| `setOpenMenuEnabled(bool state)` | `openMenuEnabled`を設定するだけ。 |
| `inputOpenOrCloseMapMenu()` | 開閉可否・ポーズ・デバイス状態を確認し、可能ならマップメニューの開閉を切り替える。 |
| `inputNextFloor()` | マップ有効かつ開いているとき`checkNextFloor`を呼ぶ。 |
| `inputPreviousFloor()` | マップ有効かつ開いているとき`checkPrevoiusFloor`を呼ぶ。 |
| `inputZoomIn()` | マップ有効かつ開いているとき`currentMouseWheelPositiveValue`をtrueにしてズームインを要求する。 |
| `inputZoomOut()` | マップ有効かつ開いているとき`currentMouseWheelNegativeValue`をtrueにしてズームアウトを要求する。 |
| `enableOrDisableAllMapIconType(Slider iconSlider)` | スライダー値0で無効、それ以外で有効とし、`glossaryList`の全アイコン型へ一括適用する。 |
| `enableOrDisableMapIconType(Slider iconSlider)` | スライダーに対応する`glossaryList`の型名を探し、その型のアイコンだけを一括で切り替える。 |
| `enableOrDisableMapIconTypeByName(bool value, string typeName)` | 指定型名の`isActivated`を更新し、同名スライダーの値も0/1に同期する。 |
| `enableOrDisableAllFloorsFoundMapIcon(bool value)` | 現在の建物でマップパーツが見つかった全アイコンの`canBeShowTemporaly`を設定する。 |
| `enableOrDisableSingleMapIconByID(int ID, bool value)` | `ID`が一致するアイコンの`isActivated`と`mapPartOwnerFound`を設定する。 |
| `enableOrDisableSingleMapIconByMapPartIndex(int mapPartBuildingIndex, int mapPartIndex, int mapFloorIndex, bool value)` | 建物・階・マップパーツのインデックスがすべて一致するアイコンの有効状態を設定する。 |
| `checkEventOnChangeFloorForMapObjectInformation()` | 階変更イベントを使う全マップオブジェクトへ、現在の建物・階でイベント確認を行うよう通知する。 |
| `enableOrDisableTextInIcons(Slider textInIconsSlider)` | スライダー値が0なら`useTextInIcons`をfalse、それ以外ならtrueにする。 |
| `getMapObjectInfo(int mapObjectIndex)` | 指定アイコンの情報をUIへ表示し、ビーコンならクイックトラベル、マークなら削除ボタンを有効化する。 |
| `assignMapWindowBorder()` | ミニマップがマスク付きでマップ展開中ならマスクを、そうでなければマップウィンドウを境界として割り当てる。 |
| `activateQuickTravel()` | 選択中のクイックトラベル地点へプレイヤーまたは車両を移動させ、メニューを閉じて建物・階情報を更新する。 |
| `openOrCloseMap(bool state)` | 可否判定後`mapOpened`を更新し、窓枠・2D化・サイズ・建物と階・カーソル・ウィンドウ表示をまとめて切り替える。 |
| `openOrCLoseMapFromTouch()` | `mapOpened`を反転して`mainMapUISystem`のメニュー開閉を呼ぶ。 |
| `openOrCloseMapExternally(bool state)` | 指定状態で`mainMapUISystem`のメニュー開閉を呼ぶ。 |
| `removeMapObjectInfo()` | `mainMapUISystem`が割り当て済みならオブジェクト情報表示の解除を委譲する。 |
| `checkChangeMapPositionCoroutine()` | `mainMapUISystem`未割り当てなら中断し、既存コルーチンを止めてマップ位置・サイズ変更コルーチンを開始する。 |
| `checkMapWindowActiveIfOtherMenuOpened()` | マップ有効かつ未展開のとき、他のメニューが開いていればマップウィンドウを隠し、なければ表示する。 |
| `setMapWindowActiveState(bool state)` | `mainMapUISystem`が割り当て済みなら`mapWindow`のアクティブ状態を指定値に合わせる。 |
| `getDeltaTime()` | 通常のタイムスケールなら`Time.deltaTime`、そうでなければ`unscaledDeltaTime`を返す。 |
| `enableOrDisableMapRotation(Slider mapRotationSlider)` | スライダー値で`rotateMap`を切り替え、無効にしたときは`mapCamera`のローカル角度を0に戻す。 |
| `enableOrDisableMiniMap(bool state)` | ミニマップ有効時のみマップウィンドウを、コンパス有効ならコンパスも同時に表示または非表示にする。 |
| `enableOrDisableCompass(bool state)` | `mainMapUISystem`が割り当て済みならコンパスの表示切り替えを委譲する。 |
| `enableOrDisableHUD(bool state)` | マップ有効ならミニマップを、コンパス有効ならコンパスを指定状態に切り替える。 |
| `changeMapIndexWindowState()` | `mapIndexEnabled`を反転してマップ索引ウィンドウの表示を切り替える。 |
| `showOrHideMapIndexWindow(bool state)` | UIへ索引ウィンドウの表示切り替えを委譲し、`mapIndexEnabled`を更新する。 |
| `disableButtons()` | マーク削除とクイックトラベルのボタン色を無効色にする。 |
| `setMapGameObjectState(GameObject mapObject, bool state)` | 指定`GameObject`のアクティブ状態を、現在と異なる場合のみ変更する。 |
| `getClosestFloorToPlayer()` | プレイヤーに最も近い階のインデックスを返し、見つかれば`currentFloorNumber`も更新する。 |
| `checkNextFloor()` | 2D表示時のみ階インデックスを1つ進め（上限あり）、`updateCurrentFloorNumber`を呼ぶ。 |
| `checkPrevoiusFloor()` | 2D表示時のみ階インデックスを1つ戻し（下限あり）、`updateCurrentFloorNumber`を呼ぶ。 |
| `updateCurrentFloorNumber()` | 階表示を更新し、範囲内なら`currentFloorNumber`と建物名テキストを更新、最後に階変更イベントを通知する。 |
| `updateCurrentFloorEnabledState()` | `mapCreatorManager`へ現在の建物・階インデックスを渡して表示する階を切り替える。 |
| `setCurrentFloorNumber(int floorNumber)` | `currentFloorNumber`を設定するだけ。 |
| `setCurrentFloorIndex(int floorIndex)` | `currentFloorIndex`を設定するだけ。 |
| `checkNextBuilding()` | 3D時は現建物の3Dマップと全階アイコンを止め、建物インデックスを進めて`updateCurrentBuildingNumber`を呼ぶ。 |
| `checkPrevoiusBuilding()` | 3D時は現建物の3Dマップと全階アイコンを止め、建物インデックスを戻して`updateCurrentBuildingNumber`を呼ぶ。 |
| `updateCurrentBuildingNumber()` | 建物情報を更新し、専用カメラ位置を適用、3D時は建物メッシュと階アイコンの表示を切り替える。 |
| `updateCurrentBuildingEnabledState()` | `mapCreatorManager`に現在の建物インデックスを渡して表示する建物を切り替える。 |
| `updateCurrentBuilding(int buildingIndex)` | 範囲外なら警告して中断し、建物と階リストを差し替え、プレイヤー直近の階を求めて各種表示を更新する。 |
| `updateCurrentBuildingNameText()` | 建物名と階名を大文字にして`mainMapUISystem`のゾーンテキストへ設定する。 |
| `setCurrentBuildingName(string newName)` | `currentBuildingName`を設定するだけ。 |
| `setMapOrientation(int mapCameraMovementTypeIndex, Transform mapOrientationTransform)` | 向きが変わったときだけ軸タイプとカメラオフセットを更新し、マップカメラの位置と角度をその`Transform`に合わせる。 |
| `searchBuildingList()` | `mapCreator`から建物・階リストを作り直して現在マップの階を設定し、`updateComponent`で表示を更新する。 |
| `addPlayerMapSystemToMapCreator()` | `mapCreatorManager`を取得し、`updateComponent`の後にこのマップシステムをプレイヤーとして登録する。 |
| `addNewMapCreator()` | `mapCreatorManager`を取得して`updateComponent`後、`addPlayerMapSystemToMapCreator`を呼ぶだけ。 |
| `selectMapCreatorObject()` | `mapCreatorManager`が存在すればエディタ上でそのオブジェクトを選択する。 |
| `checkGetMapCreatorManager()` | 未割り当てなら`mapCreator.Instance`、シーン生成、`FindObjectOfType`の順で取得を試みる。 |
| `updateEditorMapInfo()` | エディタ用に建物・階・マップパーツの各リストを再取得する。 |
| `getEditorBuildingList()` | 建物名の文字列配列を作り直し、建物が無ければ警告して空配列にし、`updateComponent`を呼ぶ。 |
| `getEditorFloorList()` | 現在の建物の階名配列を作り、階インデックスが範囲外なら0に戻して`updateComponent`を呼ぶ。 |
| `getEditorMapPartList()` | 現在の建物・階のマップパーツ名配列を作り、見つからなければ階インデックスを0にして空配列にする。 |
| `updateMapIconTypes(List<mapIconType> newMapIconTypes)` | `mapIconTypes`を新しいリストに差し替え、`updateComponent`でエディタ表示を更新する。 |
| `setMiniMapWindowEnabledInGameStateFromEditor(bool state)` | ミニマップ有効フラグを設定し、`updateComponent`でエディタに反映する。 |
| `setCompassEnabledStateFromEditor(bool state)` | コンパス有効フラグを設定し、`updateComponent`でエディタに反映する。 |
| `setMapEnabledStateFromEditor(bool state)` | マップ有効フラグを設定し、`updateComponent`でエディタに反映する。 |
| `setOpenMenuEnabledFromEditor(bool state)` | メニュー開閉可否フラグを設定し、`updateComponent`でエディタに反映する。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static Matrix4x4 MatrixLerp(Matrix4x4 from, Matrix4x4 to, float time)` | – |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventIfMapDisabled` | `UnityEvent` | – |
| `eventIfMapEnabled` | `UnityEvent` | – |

## 内部型

- `mapCameraMovement`（enum）
- `mapObjectInfo`（class）
- `floorInfo`（class）
- `buildingInfo`（class）
- `markInfo`（class）
- `glossaryElementInfo`（class）
- `compassIconInfo`（class）
