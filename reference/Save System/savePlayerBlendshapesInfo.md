# savePlayerBlendshapesInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `saveGameInfo`
- **ソース**: `Save System/Custom Class To Save/savePlayerBlendshapesInfo.cs:8`

**概要**: プレイヤーのブレンドシェイプ値・アクセサリ・`characterModelID`を保存し、ロード時にキャラクターカスタマイズへ反映する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Character Customization Blendshapes Helper | `mainCharacterCustomizationBlendshapesHelper` | `characterCustomizationBlendshapesHelper` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveGameContent(int currentSaveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)` | `storeBlendshapesCustomization`で現在値を取り込み、`getPersistanceList`の結果をスロットへ格納して保存する。 |
| `loadGameContent(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)` | 保存スロットから`blendshapesList`・`accessoriesList`・`characterModelID`を読み、`loadInfoFound`を立てて`loadInfoOnMainComponent`へ渡す。 |
| `getPersistanceList(int playerID, bool showDebugInfo)` | `temporalBlendshapeInfoList`から`Name`と`blendShapeValue`を写し、`temporalCurrentAccessoriesList`と`characterModelID`も詰めて返す。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`initializeValuesOnComponent()`, `loadGame(int saveNumberToLoad, int playerID, string currentSaveDataPath, bool showDebugInfo)`, `saveGame(int saveNumber, int playerID, string currentSaveDataPath, bool showDebugInfo, bool savingGameToChangeScene)`

</details>
