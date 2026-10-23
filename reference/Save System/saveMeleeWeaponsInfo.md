# saveMeleeWeaponsInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `saveGameInfo`
- **ソース**: `Save System/Custom Class To Save/saveMeleeWeaponsInfo.cs:8`

**概要**: 拾得済み近接武器を`weaponPrefabIndex`と現在装備フラグで保存し、ロード時にプレハブから武器を再生成する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Melee Weapons Grabbed Manager | `mainMeleeWeaponsGrabbedManager` | `meleeWeaponsGrabbedManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveGameContent(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)` | `meleeWeaponGrabbedInfoList`の武器インデックスと装備状態を集め、同一スロット・`playerID`の`meleeList`を差し替えて保存する。 |
| `loadGameContent(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 保存スロットから`playerID`の`meleeList`を`persistanceInfoList`へ読み込み、`loadInfoOnMainComponent`で武器を再生成して適用する。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`initializeValuesOnComponent()`, `loadGame(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `saveGame(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)`

</details>
