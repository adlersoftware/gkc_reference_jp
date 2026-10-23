# mapZoneUnlocker

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Map/mapZoneUnlocker.cs:5`

**概要**: 複数の建物・フロア・マップパーツの有効状態をまとめて管理するコンポーネント。`mapCreator`の情報を複製して保持し、ゾーン単位でパーツを解放する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Map Creator Manager Name | `mainMapCreatorManagerName` | `string` | "Map Creator" | `Map Creator`の名前を指定する文字列。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `buildingList` | `List<buildingInfo>` | new List<buildingInfo> () | – |
| `initialIndex` | `float` | 0 | – |
| `finalIndex` | `float` | 0 | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkGetMapCreatorManager()` | `mapCreator.Instance`の取得・生成・検索により`mapCreatorManager`を確保する。 |
| `unlockMapZone()` | 有効なフロアの有効なマップパーツを全て`enableMapPart`で解放し、マップを表示する。 |
| `enableOrDisableAllFloorParts(bool state, int buildingIndex, int floorIndex)` | 指定建物・フロアの全パーツの`mapPartEnabled`を`state`にして保存する。 |
| `enableOrDisableMapPartsRange(bool state, int buildingIndex, int floorIndex)` | `initialIndex`から`finalIndex`までのパーツだけ`state`にし、範囲外は無効化する。 |
| `searchBuildingList()` | `mapCreator`の建物・フロア・パーツ情報を複製して`buildingList`を再構築する。 |
| `clearAllBuildingList()` | `buildingList`を空にして保存するだけ。 |
| `updateComponent()` | `GKC_Utils.updateComponent`で変更を保存するだけ。 |

## 内部型

- `floorInfo`（class）
- `buildingInfo`（class）
- `mapPartInfo`（class）
