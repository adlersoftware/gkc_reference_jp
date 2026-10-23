# travelStationUISystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Level Manager/travelStationUISystem.cs:7`

**概要**: トラベルステーションのメニューUIを管理し、発見済みステーションのパネル生成・選択・メニュー開閉・移動先シーンのチェックポイント保存を行う。物理ステーションに触れた際は発見パネルを表示する。

**公式ドキュメント抜粋**（[Travel Station UI System](../../docs/character-level-components/character/travel-station-ui-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Travel Station UI Active | `travelStationUIActive` | `bool` | true | – |
| Menu Opened | `menuOpened` | `bool` | – | – |
| Use Blur UI Panel | `useBlurUIPanel` | `bool` | – | – |
| Save Current Travel Station To Save File | `saveCurrentTravelStationToSaveFile` | `bool` | true | – |
| All Stations Unlocked | `allStationsUnlocked` | `bool` | – | – |
| Show Travel Station Found Panel | `showTravelStationFoundPanel` | `bool` | – | – |
| Show Trave Station Panel Duration | `showTraveStationPanelDuration` | `float` | 1 | – |
| Travel Station Found Extra Message | `travelStationFoundExtraMessage` | `string` | "Travel Station Found" | – |
| Menu Panel Name | `menuPanelName` | `string` | "Travel Station System" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Found Travel Station Info List | `foundTravelStationInfoList` | `List<foundTravelStationInfo>` | new List<foundTravelStationInfo> () | – |
| Current Travel Station System | `currentTravelStationSystem` | `travelStationSystem` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event If System Disabled | `useEventIfSystemDisabled` | `bool` | – | – |
| Event If System Disabled | `eventIfSystemDisabled` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Travel Station Menu | `travelStationMenu` | `GameObject` | – | – |
| Travel Station Panel Prefab | `travelStationPanelPrefab` | `GameObject` | – | – |
| Travel Station Panel Parent | `travelStationPanelParent` | `Transform` | – | – |
| Travel Station Found Panel | `travelStationFoundPanel` | `GameObject` | – | – |
| Travel Station Found Panel Text | `travelStationFoundPanelText` | `Text` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Main Save Game System | `mainSaveGameSystem` | `saveGameSystem` | – | – |
| Using Devices Manager | `usingDevicesManager` | `usingDevicesSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `initializeTravelStationValues()` | `travelStationUIActive`がfalseの時だけ警告用の無効イベントを実行してreturnし、trueなら何もしない。 |
| `checkEventOnSystemDisabled()` | `useEventIfSystemDisabled`がtrueの時、`eventIfSystemDisabled`をInvokeするだけ。 |
| `checkPressedButton(GameObject buttonToCheck)` | 前回パネルの押下アイコンを消し、一致するパネルのアイコンを表示して`currentTravelStationPanelInfo`に保持する。 |
| `confirmTravelToStationSelected()` | 選択パネルの移動先が現在地と違う場合のみ、そのシーン番号とレベルIDでチェックポイントを保存し`activateAutoLoad`で移動する。 |
| `setCurrentTravelStationSystem(travelStationSystem newTravelStationSystem, bool settingPhysicalStation)` | 対象の情報リストを取得し、物理ステーション時は未発見なら発見リストへ追加、`zoneFound`を設定し、新規発見なら発見パネルを表示する。 |
| `openOrCloseTravelStationMenu(bool state)` | メニュー使用可否を確認して`menuOpened`を更新し、ポーズメニュー・パネル表示・プレイヤー操作を切り替え、開く時はリスト生成と初期選択を行う。 |
| `setTravelStationInfoList()` | 既存パネルを破棄し、未設定なら`travelStationSystem`を検索して設定、発見済み分のパネルを生成し名前と番号を入れる。 |
| `openOrCloseTravelStationMenuFromTouch()` | 閉じている時のみ使用可否を確認し、`menuOpened`を反転してメニューを開閉し、タッチ用のポーズ状態を設定する。 |
| `checkOpenOrCloseTravelStationMenuByButton()` | 同名のポーズメニューが開いている時は何もせず、そうでなければ`oopenOrCloseTravelStationMenuByButton`を呼ぶ。 |
| `oopenOrCloseTravelStationMenuByButton()` | デバイス使用中なら`useDevice`とステーションの使用状態設定を、そうでなければタッチ用の開閉を呼ぶ。 |
| `showTravelStationFound(string travelStationName)` | 表示設定が無ければreturnし、実行中のコルーチンを止め、指定秒数だけ発見パネルに名前を出すコルーチンを開始する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventIfSystemDisabled` | `UnityEvent` | – |

## 内部型

- `foundTravelStationInfo`（class）
