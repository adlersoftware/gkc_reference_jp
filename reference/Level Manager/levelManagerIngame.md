# levelManagerIngame

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Level Manager/levelManagerIngame.cs:9`

**概要**: シーン遷移用のレベルマネージャで、`sceneNumberToLoad`と`levelManagerIDToLoad`の組み合わせで移動先シーンとプレイヤーの出現位置を指定する。`activateChangeOfLevel`でチェックポイントを保存してシーンを読み込む。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Scene Enabled | `changeSceneEnabled` | `bool` | true | – |
| Scene Number To Load | `sceneNumberToLoad` | `int` | – | – |
| Level Manager ID | `levelManagerID` | `int` | – | – |
| Level Manager ID To Load | `levelManagerIDToLoad` | `int` | – | – |
| Spaw Player Position Transform | `spawPlayerPositionTransform` | `Transform` | – | – |
| Change Level With Delay | `changeLevelWithDelay` | `bool` | – | – |
| Delay To Change Level | `delayToChangeLevel` | `float` | 0.1f | – |
| Auto Save Game On Scene Change Enabled | `autoSaveGameOnSceneChangeEnabled` | `bool` | true | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.red | – |
| Gizmo Radius | `gizmoRadius` | `float` | 0.06f | – |

### Other Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Scene Folder Path | `sceneFolderPath` | `string` | "Assets//Game Kit Controller/Scenes/" | – |
| Scene To Change Name | `sceneToChangeName` | `string` | "New Scene" | – |

### Player Manual Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Player Manually | `setPlayerManually` | `bool` | – | – |
| Search Player By Tag If Not Assigned | `searchPlayerByTagIfNotAssigned` | `bool` | true | – |
| Player To Configure | `playerToConfigure` | `GameObject` | – | – |
| Explanation | `explanation` | `string` | "Configure the Scene Number where the… | TextArea (5, 20) |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentPlayer(GameObject newPlayer)` | `currentPlayer`に`newPlayer`を代入するだけ。 |
| `setCurrentPlayerAndActivateChangeOfLevel(GameObject newPlayer)` | `currentPlayer`に`newPlayer`を代入してから`activateChangeOfLevel`を呼ぶ。 |
| `activateChangeOfLevel()` | プレイヤーを解決して`saveGameCheckpoint`で移動先IDとシーン番号を保存し、`changeSceneEnabled`なら`activateAutoLoad`で読み込む。 |
| `setChangeSceneEnabledState(bool state)` | `changeSceneEnabled`に`state`を代入するだけ。 |
| `openNextSceneOnEditor()` | `sceneFolderPath`と`sceneToChangeName`の`.unity`が存在する時だけエディタで開き、無ければ警告を出す。 |
