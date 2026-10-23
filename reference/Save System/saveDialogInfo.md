# saveDialogInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `saveGameInfo`
- **ソース**: `Save System/Custom Class To Save/saveDialogInfo.cs:8`

**概要**: `dialogManager`の対話進行（`dialogContentSystem`ごとの現在インデックス）をスロット／プレイヤー別に保存し、ロード時に完了位置を復元する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Dialog Manager | `mainDialogManager` | `dialogManager` | – | – |
| Main Dialog Manager Name | `mainDialogManagerName` | `string` | "Dialog Manager" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Persistance Info List | `persistanceInfoList` | `List<persistanceDialogContentInfo>` | – | – |
| Temporal Persistance Player Dialog Content Info | `temporalPersistancePlayerDialogContentInfo` | `persistancePlayerDialogContentInfo` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveGameContent(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)` | 現在シーンの`dialogContentSystem`から対話ID・シーン・現在インデックスを集め、同一スロット・`playerID`の既存データを差し替えて`BinaryFormatter`で保存する。 |
| `loadGameContent(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 保存ファイルから`playerID`の対話リストを読み、現在シーン分だけ`persistanceInfoList`に入れて`setCompleteDialogIndex`で進行を反映する。 |
| `getPersistanceList(int playerID, bool showDebugInfo)` | `mainDialogManager`の`dialogContentSystemList`を走査し、`dialogContentID`・`dialogContentScene`・`currentDialogIndex`を`persistancePlayerDialogContentInfo`に詰める。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`loadGame(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `saveGame(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)`

</details>
