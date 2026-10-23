# inputPanelUISystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Input/inputPanelUISystem.cs:5`

**概要**: 入力パネルのGameObjectとアクション画面情報を保持し、`playerInputPanelSystem` と相互に参照し合うUI側コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Input Panel System | `mainPlayerInputPanelSystem` | `playerInputPanelSystem` | – | – |
| Input Panel Game Object | `inputPanelGameObject` | `GameObject` | – | – |
| Screen Action Parent | `screenActionParent` | `GameObject` | – | – |

### Screen Action Panel Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Screen Action Info List | `screenActionInfoList` | `List<screenActionInfo>` | new List<screenActionInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setInputPanelGameObjectActiveState(bool state)` | `inputPanelGameObject` の表示を`state`にするだけ。 |
| `setMainPlayerInputPanelSystem(playerInputPanelSystem newplayerInputPanelSystem)` | `mainPlayerInputPanelSystem` を設定して`updateComponent` を呼ぶだけ。 |
| `searchPlayerInputPanelSystem(playerInputPanelSystem newPlayerInputPanelSystem)` | 渡された値かシーンから`playerInputPanelSystem` を探して保持し、見つかれば自分を登録させる。 |
