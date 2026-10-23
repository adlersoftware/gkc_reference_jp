# ingameMenuPanel

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Menu/ingameMenuPanel.cs:6`

**概要**: インゲームメニューの1パネルを表す基底クラス。開閉時に`menuPause`へ状態を通知し、表示・イベント・パネル移動・キャンバスのソート順を制御する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Menu Panel Name | `menuPanelName` | `string` | – | – |
| Close Menu If Game Paused | `closeMenuIfGamePaused` | `bool` | true | – |
| Player Can Move State Paused On Menu Opened | `playerCanMoveStatePausedOnMenuOpened` | `bool` | true | – |

### Canvas Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Blur UI Panel | `useBlurUIPanel` | `bool` | – | – |
| Set Sort Order On Open Close Menu | `setSortOrderOnOpenCloseMenu` | `bool` | – | – |
| Sort Order On Menu Opened | `sortOrderOnMenuOpened` | `int` | – | – |
| Sort Order On Menu Closed | `sortOrderOnMenuClosed` | `int` | – | – |
| Main Canvas | `mainCanvas` | `Canvas` | – | – |

### Move Panels

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Move Panels Enabled | `movePanelsEnabled` | `bool` | – | – |
| Main Panel To Move Transform | `mainPanelToMoveTransform` | `RectTransform` | – | – |
| Screen Limit Offset | `screenLimitOffset` | `float` | 20 | – |
| Use Screen Limit Offsets | `useScreenLimitOffsets` | `bool` | – | – |
| Left Screen Limit Offset | `leftScreenLimitOffset` | `float` | – | – |
| Right Screen Limit Offset | `rightScreenLimitOffset` | `float` | – | – |
| Up Screen Limit Offset | `upScreenLimitOffset` | `float` | – | – |
| Down Screen Limit Offset | `downScreenLimitOffset` | `float` | – | – |

### Enable/disable Panel Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Enable Disable Panels Enabled | `enableDisablePanelsEnabled` | `bool` | – | – |
| Menu Panel Info List | `menuPanelInfoList` | `List<menuPanelInfo>` | new List<menuPanelInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Menu Panel Opened | `menuPanelOpened` | `bool` | – | – |
| Moving Panel Active | `movingPanelActive` | `bool` | – | – |
| New Position | `newPosition` | `Vector2` | – | – |
| Screen Limit | `screenLimit` | `Vector2` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Menu Panel Object | `menuPanelObject` | `GameObject` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Events On Open State | `activateEventsOnOpenState` | `bool` | – | – |
| Use Events On Open Clost Menu | `useEventsOnOpenClostMenu` | `bool` | – | – |
| Event On Open Menu | `eventOnOpenMenu` | `UnityEvent` | – | – |
| Event On Close Menu | `eventOnCloseMenu` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `closeMenuPanelIfOpened()` | `menuPanelOpened`が真なら`openOrCloseMenuPanel`で閉じるだけ。 |
| `openOrCloseMenuPanel(bool state)` | パネル表示と`menuPause`への通知、開閉イベント、移動停止、キャンバスのソート順をまとめて切り替える。 |
| `openOrCloseMenuFromTouch()` | パネルの開閉を反転し、`pauseManager`にイベント付きで開閉状態を通知する。 |
| `openOrCloseMenuFromTouchExternally()` | 本体が空で何もしない。 |
| `openMenuPanelState()` | 本体が空の仮想メソッドで何もしない。 |
| `closeMenuPanelState()` | 本体が空の仮想メソッドで何もしない。 |
| `setPauseManager(menuPause currentMenuPause)` | `pauseManager`を設定して`initializeMenuPanel`を呼ぶ。 |
| `initializeMenuPanel()` | 本体が空の仮想メソッドで何もしない。 |
| `checkMenuIfCurrentOpened()` | 本体が空の仮想メソッドで何もしない。 |
| `checkMenuIfNotCurrentOpened()` | 本体が空の仮想メソッドで何もしない。 |
| `checkAllMenusClosed()` | 本体が空の仮想メソッドで何もしない。 |
| `openNextPlayerOpenMenu()` | `pauseManager`があれば次のプレイヤーメニューを開くよう依頼する。 |
| `openPreviousPlayerOpenMenu()` | `pauseManager`があれば前のプレイヤーメニューを開くよう依頼する。 |
| `closePlayerMenuByName(string menuName)` | `pauseManager`に名前指定のプレイヤーメニュー閉鎖を依頼する。 |
| `checkEventsOnStateChange(bool state)` | `useEventsOnOpenClostMenu`が有効なら開閉イベントを発火するだけ。 |
| `stopUpdateCoroutine()` | 実行中の`updateCoroutine`があれば停止するだけ。 |
| `enableMovePanel(RectTransform panelToMove)` | 移動が有効なら画面サイズとタッチ環境を取得し、パネルを親替えして追従コルーチンを開始する。 |
| `disableMovePanel()` | 追従コルーチンを止め、移動中のパネルを元の親に戻して`movingPanelActive`を下ろす。 |
| `toggleMenuPanelActiveState(GameObject buttonObject)` | ボタンに対応するパネルの表示を反転し、`disabledPanel`があれば逆状態にする。 |
| `openOrCloseAllMenuPanels(bool state)` | 有効なら全メニューパネルを`state`に揃える。 |
| `setMenuPanelActive(GameObject panelGameObject)` | `setMenuPanelActiveState`で対象パネルを有効にするだけ。 |
| `setMenuPanelDeactive(GameObject panelGameObject)` | `setMenuPanelActiveState`で対象パネルを無効にするだけ。 |
| `setMenuPanelActiveState(bool state, GameObject buttonObject)` | `buttonObject`に対応するパネルを`state`にし、`disabledPanel`は逆の状態にする。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnOpenMenu` | `UnityEvent` | – |
| `eventOnCloseMenu` | `UnityEvent` | – |

## 内部型

- `menuPanelInfo`（class）
