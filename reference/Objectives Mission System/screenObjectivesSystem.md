# screenObjectivesSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Objectives Mission System/screenObjectivesSystem.cs:6`

**概要**: シーン内の目標アイコンを一元管理するシングルトン。目標の追加/削除、ID採番、色変更、マップ連携、各プレイヤーUIへの配信を行う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Objectives Active | `showObjectivesActive` | `bool` | true | オンで画面上の目標アイコン表示システム全体を有効化。 |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Map Creator Manager Name | `mainMapCreatorManagerName` | `string` | "Map Creator" | マップ生成マネージャー名の指定。本クラスでは参照されない。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `objectiveIconList` | `List<objectiveIconElement>` | new List<objectiveIconElement> () | – |
| `objectiveList` | `List<objectiveInfo>` | new List<objectiveInfo> () | – |
| `playerScreenObjectivesList` | `List<playerScreenObjectivesSystem>` | new List<playerScreenObjectivesSystem… | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | シングルトンを初期化し、既に別インスタンスがあればこのGameObjectを破棄する。 |
| `addNewPlayer(playerScreenObjectivesSystem newPlayer)` | プレイヤーを一覧に追加し、既存の目標をそのプレイヤーのアイコン一覧へ追加する。 |
| `addElementToScreenObjectiveList(GameObject obj, bool useCloseDistance, float radiusDistance, bool showOffScreen, bool showDistanceInfo, bool showDistanceOffScreen, string objectiveIconName, bool useCustomObjectiveColor, Color objectiveColor, bool removeCustomObjectiveColor, float iconOffset)` | 目標を新規IDで登録し、アイコン設定に従って距離/画面外表示やマテリアル色を適用して全プレイヤーに配信し、IDを進める。 |
| `getCurrentID()` | 現在の目標IDを返すだけ。 |
| `increaseCurrentID()` | 目標IDを1増やすだけ。 |
| `addElementFromPlayerList(objectiveInfo newObjectiveInfo, objectiveIconElement currentObjectiveIconElement, Transform currentPlayer, bool addIconOnRestOfPlayers)` | プレイヤー側で作られた目標を一覧に追加し、必要なら他のプレイヤーにもアイコンを追加する。 |
| `removeElementFromList(objectiveInfo objectiveListElement)` | 未削除ならマップ情報を解除し、色を戻すコルーチンか即時削除で目標一覧から外す。 |
| `removeGameObjectFromList(GameObject objectToSearch)` | 指定GameObjectに一致する目標をすべて`removeElementFromList`で削除する。 |
| `removeGameObjectListFromList(List<GameObject> list)` | 各GameObjectについてマップ上のオブジェクトを外し、一致する目標を一覧から即時削除する。 |
| `removeElementFromObjectiveList(objectiveInfo objectiveListElement)` | 全プレイヤーのアイコンをIDで削除し、目標一覧からも同じIDの要素を取り除く。 |
| `removeElementFromObjectiveListCalledByPlayer(int objectId, GameObject currentPlayer)` | 指定IDの目標をマップから外し、色を戻すか即時削除した後、他プレイヤーのアイコンも削除する。 |
| `checkObjectiveInfoOnMapSystem(objectiveInfo objectiveListElement)` | マップオブジェクトの到達イベントを呼び、パス要素か判定してマップ管理から削除し、削除済みにする。 |
| `setScreenObjectiveVisibleState(bool state, GameObject mapObject)` | 指定`mapObject`に一致する目標の表示一時停止フラグ`showIconPaused`をstateに設定するだけ。 |
| `checkGetMapCreatorManager()` | `mapCreator`をシングルトンやシーン検索から取得し、なければ生成して参照を確保する。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |

## 内部型

- `objectiveInfo`（class）
- `objectiveIconElement`（class）
