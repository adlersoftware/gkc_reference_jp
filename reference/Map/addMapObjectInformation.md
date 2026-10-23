# addMapObjectInformation

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Map/addMapObjectInformation.cs:5`

**概要**: 実行時に`mapObjectInformation`を追加し、マップアイコンや画面目標アイコンを登録する補助コンポーネント。`addMapIcon`が無効なら画面目標のみを追加する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate At Start | `activateAtStart` | `bool` | – | – |
| Activate On Enable | `activateOnEnable` | `bool` | – | – |
| Call Create Map Icon Info If Component Exists | `callCreateMapIconInfoIfComponentExists` | `bool` | – | – |
| Main Map Creator Manager Name | `mainMapCreatorManagerName` | `string` | "Map Creator" | – |

### Map Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Map Icon | `addMapIcon` | `bool` | – | – |
| Map Object Name | `mapObjectName` | `string` | – | – |
| Map Object Type Name | `mapObjectTypeName` | `string` | – | – |
| Description | `description` | `string` | – | TextArea (3, 10) |
| Visible In All Buildings | `visibleInAllBuildings` | `bool` | – | – |
| Visible In All Floors | `visibleInAllFloors` | `bool` | – | – |
| Calculate Floor At Start | `calculateFloorAtStart` | `bool` | – | – |
| Set Floor Number | `setFloorNumber` | `bool` | – | – |
| Building Index | `buildingIndex` | `int` | – | – |
| Floor Number | `floorNumber` | `int` | – | – |

### Objective Screen Icon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Icon On Screen | `addIconOnScreen` | `bool` | – | – |
| Trigger Radius | `triggerRadius` | `float` | – | – |
| Show Off Screen Icon | `showOffScreenIcon` | `bool` | – | – |
| Use Close Distance | `useCloseDistance` | `bool` | – | – |
| Show Map Window Icon | `showMapWindowIcon` | `bool` | – | – |
| Show Distance | `showDistance` | `bool` | – | – |
| Show Distance Off Screen | `showDistanceOffScreen` | `bool` | – | – |
| Objective Icon Name | `objectiveIconName` | `string` | – | – |
| Objective Offset | `objectiveOffset` | `float` | – | – |
| Use Custom Objective Color | `useCustomObjectiveColor` | `bool` | – | – |
| Objective Color | `objectiveColor` | `Color` | – | – |
| Remove Custom Objective Color | `removeCustomObjectiveColor` | `bool` | – | – |
| Main Manager Name | `mainManagerName` | `string` | "Screen Objectives Manager" | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkGetMapCreatorManager()` | `mapCreator.Instance`の取得・生成・検索により`mapCreatorManager`を取得する。 |
| `activateMapObject()` | `mapObjectInformation`を追加・設定してIDやアイコン型、目標表示を登録し、マップアイコンを有効にする。 |
| `removeMapObject()` | `screenObjectivesSystem`の画面目標リストからこの`GameObject`を外す。 |
