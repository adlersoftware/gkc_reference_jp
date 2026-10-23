# savePlayerWeaponsInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `saveGameInfo`
- **ソース**: `Save System/Custom Class To Save/savePlayerWeaponsInfo.cs:8`

**概要**: プレイヤー武器の有効状態・現在装備・残弾・アタッチメント構成を保存し、ロード時に各武器へ反映する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveGameContent(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)` | `getPersistanceList`で武器リストを作り、同一`saveNumber`・`playerID`の`weaponList`を上書きして保存する。 |
| `loadGameContent(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 保存スロットから`playerID`の`weaponList`を`persistanceInfoList`へ読み込み、`loadInfoOnMainComponent`で武器状態を復元する。 |
| `getPersistanceList(int playerID, bool showDebugInfo)` | `weaponsList`を走査し、武器名・`isWeaponEnabled`・`isCurrentWeapon`・残弾・アタッチメント情報を`persistanceWeaponInfo`へ写す。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`initializeValuesOnComponent()`, `loadGame(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `saveGame(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)`

</details>
