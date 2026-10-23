# mapUISystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `ingameMenuPanel`
- **ソース**: `Map/mapUISystem.cs:7`

**概要**: マップ画面のUI部品参照を保持し、表示切替やボタン操作を`mapSystem`へ中継するコンポーネント。

## インスペクター設定

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Components Assigned | `componentsAssigned` | `bool` | – | – |
| Menu Opened | `menuOpened` | `bool` | – | – |
| Main Map System Assigned | `mainMapSystemAssigned` | `bool` | – | – |

### Main Map Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Map Content | `mapContent` | `GameObject` | – | – |
| Map Menu | `mapMenu` | `GameObject` | – | – |
| Map Window Target Position | `mapWindowTargetPosition` | `RectTransform` | – | – |
| Map Render | `mapRender` | `RectTransform` | – | – |
| Map Window | `mapWindow` | `RectTransform` | – | – |
| Player Map Icon | `playerMapIcon` | `RectTransform` | – | – |
| Player Icon Child | `playerIconChild` | `RectTransform` | – | – |
| Remove Mark Button Image | `removeMarkButtonImage` | `Image` | – | – |
| Quick Travel Button Image | `quickTravelButtonImage` | `Image` | – | – |
| Map Object Name Field | `mapObjectNameField` | `Text` | – | – |
| Map Object Info Field | `mapObjectInfoField` | `Text` | – | – |
| Current Floor Number Text | `currentFloorNumberText` | `Text` | – | – |
| Current Map Zone Text | `currentMapZoneText` | `Text` | – | – |
| Map Index Window | `mapIndexWindow` | `GameObject` | – | – |
| Map Index Window Content | `mapIndexWindowContent` | `GameObject` | – | – |
| Map Index Window Scroller | `mapIndexWindowScroller` | `Scrollbar` | – | – |

### Other Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Map Window Mask | `mapWindowMask` | `RectTransform` | – | – |
| Map Cursor | `mapCursor` | `GameObject` | – | – |
| Map Cursor Rect Transform | `mapCursorRectTransform` | `RectTransform` | – | – |
| Curren Map Icon Pressed | `currenMapIconPressed` | `GameObject` | – | – |
| Zoom Scrollbar | `zoomScrollbar` | `Scrollbar` | – | – |
| Map Circle Transform | `mapCircleTransform` | `Transform` | – | – |

### Compass Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Compass Window | `compassWindow` | `RectTransform` | – | – |
| Compass Elements Parent | `compassElementsParent` | `RectTransform` | – | – |
| North | `north` | `RectTransform` | – | – |
| South | `south` | `RectTransform` | – | – |
| East | `east` | `RectTransform` | – | – |
| West | `west` | `RectTransform` | – | – |
| North East | `northEast` | `RectTransform` | – | – |
| South West | `southWest` | `RectTransform` | – | – |
| South East | `southEast` | `RectTransform` | – | – |
| North West | `northWest` | `RectTransform` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Map System | `mainMapSystem` | `mapSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setMapContentActiveState(bool state)` | `mapContent`のアクティブ状態を`state`に切り替えるだけ。 |
| `setMapMenuActiveState(bool state)` | `mapMenu`の表示状態を`state`に切り替えるだけ。 |
| `getMapMenuTransform()` | `mapMenu`のTransformを返すだけ。 |
| `removeMapObjectInfo()` | オブジェクト情報と名前のテキストを空にするだけ。 |
| `setMapObjectInfoText(string mapObjectInfoFieldText, string mapObjectNameFieldText)` | 説明文と名前の2つのテキストを指定文字列に差し替える。 |
| `setCurrentFloorNumberText(string newText)` | 現在階数の表示テキストを`newText`に更新するだけ。 |
| `setCurrentMapZoneText(string newText)` | 現在マップゾーンの表示テキストを`newText`に更新するだけ。 |
| `setMapIndexWindowScrollerValue(int newValue)` | マップ索引ウィンドウのスクロール値を`newValue`にするだけ。 |
| `setZoomScrollbarValue(float newValue)` | ズーム用スクロールバーの値を`newValue`にするだけ。 |
| `enableOrDisableCompass(bool state)` | コンパスウィンドウの表示を`state`で切り替える。 |
| `getCompassElementsParent()` | コンパス要素の親`RectTransform`を返すだけ。 |
| `disableMainCompassDirections()` | コンパスの斜め4方向（`northEast`など）の表示をまとめて無効化する。 |
| `checkCurrentMapIconPressedParent()` | 押下中アイコンを`mapWindow`の子へ戻し、非表示にする。 |
| `currenMapIconPressedActiveState(bool state)` | 押下中アイコンの表示を`state`に切り替えるだけ。 |
| `checkCurrentIconPressed(bool state, Transform mapIconTransform)` | `state`が真なら押下中アイコンを対象アイコン配下に置き、表示状態を設定する。 |
| `getMapCursorRectTransformPosition()` | マップカーソルのワールド座標を返すだけ。 |
| `setMapCursorActiveState(bool state)` | `mapCursor`がnullでなければ表示を`state`に切り替える。 |
| `setMapCursorAsLastSibling()` | マップカーソルを最前面の兄弟要素へ移動するだけ。 |
| `setMapIndexWindowActiveState(bool state)` | マップ索引ウィンドウの表示を`state`に切り替える。 |
| `setRemoveMarkButtonImageColor(Color newColor)` | マーク削除ボタンの画像色を`newColor`にするだけ。 |
| `setQuickTravelButtonImageColor(Color newColor)` | クイックトラベルボタンの画像色を`newColor`にするだけ。 |
| `getMapRender()` | `mapRender`を返すだけ。 |
| `getMapWindow()` | `mapWindow`を返すだけ。 |
| `getPlayerMapIcon()` | `playerMapIcon`を返すだけ。 |
| `getPlayerIconChild()` | `playerIconChild`を返すだけ。 |
| `getRemoveMarkButtonImage()` | `removeMarkButtonImage`を返すだけ。 |
| `getQuickTravelButtonImage()` | `quickTravelButtonImage`を返すだけ。 |
| `changeMapIndexWindowState()` | マップ索引ウィンドウの開閉を`mainMapSystem`に委譲するだけ。 |
| `enableOrDisableAllMapIconType(Slider iconSlider)` | 全アイコン種別の一括切替を`iconSlider`ごと`mainMapSystem`に委譲する。 |
| `enableOrDisableMapIconType(Slider iconSlider)` | 単一アイコン種別の切替を`iconSlider`ごと`mainMapSystem`に委譲する。 |
| `zoomInEnabled()` | ズームイン開始処理を`mainMapSystem`へ委譲するだけ。 |
| `zoomInDisabled()` | ズームイン終了処理を`mainMapSystem`へ委譲するだけ。 |
| `zoomOutEnabled()` | ズームアウト開始処理を`mainMapSystem`へ委譲するだけ。 |
| `zoomOutDisabled()` | ズームアウト終了処理を`mainMapSystem`へ委譲するだけ。 |
| `checkNextFloor()` | 次の階への切替を`mainMapSystem`に委譲するだけ。 |
| `checkPrevoiusFloor()` | 前の階への切替を`mainMapSystem`に委譲するだけ。 |
| `placeMark()` | マーク設置を`mainMapSystem`に委譲するだけ。 |
| `removeMark()` | マーク削除を`mainMapSystem`に委譲するだけ。 |
| `activateQuickTravel()` | クイックトラベル実行を`mainMapSystem`に委譲するだけ。 |
| `set2dOr3ddMapView(bool state)` | 2D/3Dマップ表示の切替を`state`付きで`mainMapSystem`に委譲する。 |
| `recenterCameraPosition()` | カメラ位置の再センタリングを`mainMapSystem`に委譲するだけ。 |
| `setUsingScrollbarZoomState(bool state)` | スクロールバーでズームするかどうかの設定を`mainMapSystem`に委譲する。 |
| `setZoomByScrollBar(Scrollbar mainZoomScrollbar)` | `mainZoomScrollbar`によるズーム処理を`mainMapSystem`に委譲する。 |
| `checkNextBuilding()` | 次の建物への切替を`mainMapSystem`に委譲するだけ。 |
| `checkPrevoiusBuilding()` | 前の建物への切替を`mainMapSystem`に委譲するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkAllMenusClosed()`, `checkMenuIfCurrentOpened()`, `checkMenuIfNotCurrentOpened()`, `initializeMenuPanel()`, `openOrCloseMenuPanel(bool state)`

</details>
