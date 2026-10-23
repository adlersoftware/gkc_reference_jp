# saveElementsOnSceneInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `saveGameInfo`
- **ソース**: `Save System/Custom Class To Save/saveElementsOnSceneInfo.cs:10`

**概要**: シーン上の`elementOnScene`のアクティブ状態・位置・回転・統計値・プレハブIDを保存し、ロード時に既存要素へ適用、必要ならプレハブから生成する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Element On Scene Manager | `mainElementOnSceneManager` | `elementOnSceneManager` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Persistance Info List | `persistanceInfoList` | `List<persistanceElementOnSceneInfo>` | – | – |
| Temporal Persistance Player Element On Scene Info | `temporalPersistancePlayerElementOnSceneInfo` | `persistancePlayerElementOnSceneInfo` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveGameContent(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)` | `getPersistanceList`で要素状態を取得し、同一スロットの同シーン分を削除してから追加し直し、保存ファイルへ書き出す。 |
| `loadGameContent(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 保存データから現在シーンの要素情報を`persistanceInfoList`へ抽出し、`loadInfoOnMainComponent`でシーン上の要素へ適用する。 |
| `getPersistanceList(int playerID, bool showDebugInfo)` | `elementOnSceneList`の保存対象を走査して状態・位置・回転・統計・`elementPrefabID`を写し、`temporalElementOnSceneInfoList`の状態も統合する。 |
| `setStatsSearchingByInfo(int currentElementScene, int currentElementID, elementOnScene currentElementOnScene)` | `elementScene`と`elementID`が一致する要素を一時保存リストから探し、統計値を設定して`setStatsOnLoad`を呼ぶ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`copyGameInfo(int saveNumberToStoreDuplicate, int saveNumberToDuplicate, int playerID, string currentSaveDataPath, bool copyAllInfoWithoutChecks, bool showDebugInfo)`, `deleteGameInfo(int saveNumberToDelete, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `initializeValuesOnComponent()`, `loadGame(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `saveGame(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)`, `showSaveInfoDebug(int saveNumberToShow, int playerID, string currentSaveDataPath, bool showAllGameInfo, bool showDebugInfo)`

</details>
