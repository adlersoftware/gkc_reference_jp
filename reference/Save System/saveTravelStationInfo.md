# saveTravelStationInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `saveGameInfo`
- **ソース**: `Save System/Custom Class To Save/saveTravelStationInfo.cs:8`

**概要**: 発見済みトラベルステーションの遷移先シーン番号と`levelManagerID`を保存し、ロード時に発見リストへ戻す。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Travel Station UI System | `mainTravelStationUISystem` | `travelStationUISystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveGameContent(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)` | `foundTravelStationInfoList`の遷移先シーン番号と`levelManagerID`を集め、同一スロット・`playerID`のリストを置換して保存する。 |
| `loadGameContent(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 保存スロットから`playerID`の`travelStationList`を`persistanceInfoList`へ読み込み、`loadInfoOnMainComponent`で発見リストへ追加する。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`initializeValuesOnComponent()`, `loadGame(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `saveGame(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)`

</details>
