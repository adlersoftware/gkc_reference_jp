# saveSkillsInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `saveGameInfo`
- **ソース**: `Save System/Custom Class To Save/saveSkillsInfo.cs:8`

**概要**: `playerSkillsSystem`のカテゴリ別スキル状態（解放・有効・完了・現在値・レベル）を保存し、ロード時に復元する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Skills System | `mainPlayerSkillsSystem` | `playerSkillsSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveGameContent(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)` | `getPersistanceList`でカテゴリ別スキル状態を集め、同一`saveNumber`・`playerID`の`categorySkillsList`を置き換えて保存する。 |
| `loadGameContent(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 保存スロットから`playerID`の`categorySkillsList`を`persistanceInfoList`へ読み込み、`loadInfoOnMainComponent`で各スキルへ反映する。 |
| `getPersistanceList(int playerID, bool showDebugInfo)` | `skillCategoryInfoList`を二重に走査し、各`skillInfo`の解放／有効／完了フラグ・`currentValue`・`currentSkillLevel`を写す。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`initializeValuesOnComponent()`, `loadGame(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `saveGame(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)`

</details>
