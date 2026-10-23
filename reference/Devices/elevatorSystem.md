# elevatorSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/elevatorSystem.cs:6`

**概要**: 階リスト間を移動するエレベータで、内外扉の閉鎖完了を待ってから移動を始める。乗客の親子付け、階ボタン `callElevator`、階の追加削除も管理する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Elevator System Enabled | `elevatorSystemEnabled` | `bool` | true | オフにすると上下ボタンやフロア移動の全操作を受け付けなくする。 |
| Can Use Elevator Buttons Without Player Inside | `canUseElevatorButtonsWithoutPlayerInside` | `bool` | – | オンにすると乗員がいなくても外のボタンでエレベーターを動かせる。 |
| Current Floor | `currentFloor` | `int` | – | 現在のフロア番号（`floors`のインデックス）。移動先計算の基準になる。 |
| Elevator Speed | `elevatorSpeed` | `float` | 20 | フロア間の移動速度。大きいほど移動時間が短くなる。 |
| Floor Height | `floorHeight` | `float` | 5 | フロア追加時に階間として積み上げる高さ。 |
| Has Inside Elevator Door | `hasInsideElevatorDoor` | `bool` | – | オンにすると内部ドアの参照欄を設定できるようになる。 |
| Inside Elevator Door | `insideElevatorDoor` | `GameObject` | – | 昇降機内側のドア。`doorSystem`を取得し、閉まるまで移動を待つ。 / 表示条件: `hasInsideElevatorDoor` がオンのとき |
| Elevator Switch Prefab | `elevatorSwitchPrefab` | `GameObject` | – | 新規フロア追加時に生成する階ボタン用のプレハブ。 |
| Elevator Door Prefab | `elevatorDoorPrefab` | `GameObject` | – | 新規フロア追加時に生成する外扉用のプレハブ。 |
| Add Switch In New Floors | `addSwitchInNewFloors` | `bool` | – | オンにするとフロア追加時に階ボタンを自動生成する。 |
| Add Door In New Floors | `addDoorInNewFloors` | `bool` | – | オンにするとフロア追加時に外扉を自動生成する。 |
| Doors Closed | `doorsClosed` | `bool` | true | ドアが閉じているかの状態。呼び出し時に開閉動作を行うかの判定に使う。 |
| Change Icon Floor When Moving | `changeIconFloorWhenMoving` | `bool` | – | オンにするとフロア到着時にマップアイコンの階表示を更新する。 |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Move Start And End | `useEventsOnMoveStartAndEnd` | `bool` | – | オンにすると移動開始・終了のイベントを実行する。 |
| Event On Move Start | `eventOnMoveStart` | `UnityEvent` | – | 移動開始時に実行するイベント。 / 表示条件: `useEventsOnMoveStartAndEnd` がオンのとき |
| Event On Move End | `eventOnMoveEnd` | `UnityEvent` | – | 移動終了時に実行するイベント。 / 表示条件: `useEventsOnMoveStartAndEnd` がオンのとき |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | オンにするとシーンビューにフロア位置のギズモを表示する。 |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | – | シーンビューに表示するフロア名ラベルの文字色。 / 表示条件: `showGizmo` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `floors` | `List<floorInfo>` | new List<floorInfo> () | – |
| `tagToCheckToMove` | `List<string>` | new List<string> () | – |
| `moving` | `bool` | – | – |
| `passengersInfoList` | `List<passengersInfo>` | new List<passengersInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `nextFloor()` | 有効時のみ `getFloorNumberToMove(1)` を呼び、1 つ上の階への移動を要求する。 |
| `previousFloor()` | 有効時のみ `getFloorNumberToMove(-1)` を呼び、1 つ下の階への移動を要求する。 |
| `moveBetweenTwoPositions()` | `currentDirectionToMove` 方向へ移動を要求し、次回用に方向を反転させる。 |
| `checkIfInsideElevatorDoorSystem()` | 現在階の外扉の `doorSystem` を未取得なら取得してキャッシュし、有無フラグを更新する。 |
| `goToNumberFloor(int floorNumber)` | 条件を満たすとき扉を操作して目的階を設定し、乗客を親子付けして閉扉後の移動を準備、成否を返す。 |
| `callElevator(GameObject button)` | `button` の階を探し、現在階の外扉が施錠でなければ目的階を設定して移動、同階なら扉を開閉する。 |
| `addPassenger(Transform newPassenger)` | 未登録なら `passengersInfoList` に乗客と `playerController` を追加する。 |
| `setElevatorSystemEnabledState(bool state)` | `elevatorSystemEnabled` を `state` にするだけ。 |
| `addNewFloor()` | 最上階の `floorHeight` 上に階を作り、設定に応じスイッチと扉を生成して `floors` に追加する。 |
| `removeFloor(int floorIndex)` | `floorIndex` の階オブジェクトを即時破棄してリストから除き、シーンを更新する。 |
| `removeAllFloors()` | 全階のオブジェクトを即時破棄して `floors` を空にし、シーンを更新する。 |
| `checkEventsOnMove(bool state)` | `useEventsOnMoveStartAndEnd` が有効なとき、`state` で開始か終了のイベントを発火する。 |
| `updateComponent()` | `GKC_Utils.updateComponent` でこのコンポーネントの表示を更新するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnMoveStart` | `UnityEvent` | – |
| `eventOnMoveEnd` | `UnityEvent` | – |

## 内部型

- `floorInfo`（class）
- `passengersInfo`（class）
