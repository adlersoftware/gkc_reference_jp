# travelStationSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Level Manager/travelStationSystem.cs:6`

**概要**: シーン内の移動拠点コンポーネントで、移動先ステーションのリスト(`travelStationInfo`)と自身のシーン番号・レベルIDを保持する。プレイヤーが触れるとUI側へ自身を登録し、メニュー開閉を仲介する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Scene Number To Load | `sceneNumberToLoad` | `int` | – | – |
| Level Manager ID To Load | `levelManagerIDToLoad` | `int` | – | – |
| All Stations Unlocked | `allStationsUnlocked` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Travel Station | `usingTravelStation` | `bool` | – | – |

### Travel Station Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Travel Station Info List | `travelStationInfoList` | `List<travelStationInfo>` | new List<travelStationInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentPlayer(GameObject player)` | プレイヤーを保持し、その`travelStationUISystem`へ自分を物理ステーションとして登録させる。 |
| `activateTravelStation()` | `usingTravelStation`を反転し、その値でUI側の`openOrCloseTravelStationMenu`を呼ぶ。 |
| `setUsingTravelStationSystemState(bool state)` | `usingTravelStation`に`state`を代入するだけ。 |
| `getTravelStationInfoList()` | 移動先リスト`travelStationInfoList`をそのまま返すだけ。 |

## 内部型

- `travelStationInfo`（class）
