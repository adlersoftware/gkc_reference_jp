# playerScreenObjectivesSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Objectives Mission System/playerScreenObjectivesSystem.cs:6`

**概要**: プレイヤーごとの目標アイコン(HUD)を生成・削除する。距離や画面内外の表示、色変更、マップアイコン追加、表示の一時停止を担う。

**公式ドキュメント抜粋**（[Player Screen Objectives System](../../docs/character-level-components/character/player-screen-objectives-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Objectives Active | `showObjectivesActive` | `bool` | true | – |
| Show Objectives Paused | `showObjectivesPaused` | `bool` | – | – |
| Icon Offset | `iconOffset` | `float` | – | Range (0, 1) |
| Min Difference To Update Distance To Object | `minDifferenceToUpdateDistanceToObject` | `float` | 0.4f | – |
| Hide Objectives If Max Distance Reached | `hideObjectivesIfMaxDistanceReached` | `bool` | – | – |
| Max Distance To Hide Objectives | `maxDistanceToHideObjectives` | `float` | 2000 | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Manager Name | `mainManagerName` | `string` | "Screen Objectives Manager" | – |
| Main Panel Name | `mainPanelName` | `string` | "Screen Objectives Info" | – |
| Main Map Creator Manager Name | `mainMapCreatorManagerName` | `string` | "Map Creator" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Objective List | `objectiveList` | `List<screenObjectivesSystem.objectiveInfo>` | new List<screenObjectivesSystem.objec… | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Objective Icon Parent | `objectiveIconParent` | `Transform` | – | – |
| Player | `player` | `Transform` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Screen Objectives Manager | `screenObjectivesManager` | `screenObjectivesSystem` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Map Creator Manager | `mapCreatorManager` | `mapCreator` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `addElementToList(screenObjectivesSystem.objectiveInfo newObjectiveToAdd, GameObject screenIconPrefab, int objectID)` | HUD親を確保し、同IDがなければアイコンプレハブを生成して目標情報を複製・一覧に追加し、一時停止中なら親を隠す。 |
| `removeElementFromList(int objectID)` | 指定IDの目標アイコンを破棄してプレイヤーの一覧から取り除く。 |
| `removeElementFromListByPlayer(screenObjectivesSystem.objectiveInfo objectiveListElement)` | 対象のアイコンを破棄し、マネージャーへ削除を通知してから自分の一覧から外す。 |
| `pauseOrResumeShowObjectives(bool state)` | `showObjectivesPaused`を設定し、アイコン親の表示をその逆に切り替える。 |
| `pauseOrResumeShowObjectivesFromEditor(bool state)` | `pauseOrResumeShowObjectives`を呼んだ後、コンポーネントとシーンを更新する。 |
| `addElementToPlayerList(GameObject obj, bool addMapIcon, bool useCloseDistance, float radiusDistance, bool showOffScreen, bool showMapWindowIcon, bool showDistanceInfo, bool showDistanceOffScreenInfo, string objectiveIconName, bool useCustomObjectiveColor, Color objectiveColor, bool removeCustomObjectiveColor, int buildingIndex, float iconOffset, bool addIconOnRestOfPlayers)` | 多数の表示設定を指定して目標を新規IDで作り、必要ならマテリアル色とマップアイコンを適用し、自プレイヤーと他プレイヤーに追加する。 |
| `checkGetMapCreatorManager()` | `mapCreator`の参照を確保し、未設定ならシングルトン取得・生成・シーン検索を行ってフラグを立てる。 |
| `objectAlreadyOnList(GameObject objectToCheck)` | 無効時やnull、同じ`mapObject`が既に一覧にあればtrueを返す。 |
| `removeElementFromListByPlayer(GameObject objectToCheck)` | 一致する目標のアイコンを破棄して一覧から削除し、IDをマネージャーに通知する。 |
| `removeElementListFromListByPlayer(List<Transform> objectToCheckList)` | Transformリストの各要素についてGameObject版の削除処理を呼ぶだけ。 |
| `setShowObjectivesActiveState(bool state)` | `showObjectivesActive`を指定状態に設定するだけ。 |
| `setShowObjectivesActiveStateFromEditor(bool state)` | `setShowObjectivesActiveState`を呼んだ後、コンポーネントとシーンを更新する。 |
