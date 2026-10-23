# craftingBlueprintInfoTemplate

- **種別**: ScriptableObject（データアセット）
- **継承 / 実装**: `ScriptableObject`
- **ソース**: `Crafting System/craftingBlueprintInfoTemplate.cs:5`
- **属性**: `CreateAssetMenu (fileName = "Crafting Blueprint Template", menuName = "GKC/Create Crafting Blueprint Template", order = 51)`

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Name | `Name` | `string` | – | – |
| ID | `ID` | `int` | 0 | – |
| Amount Obtained | `amountObtained` | `int` | 1 | – |
| Is Raw Material | `isRawMaterial` | `bool` | – | – |

### Object To Place Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Object To Place | `useObjectToPlace` | `bool` | – | – |
| Object To Place | `objectToPlace` | `GameObject` | – | – |
| Object To Place Position Offset | `objectToPlacePositionOffset` | `Vector3` | – | – |
| Use Custom Layer Mask To Place Object | `useCustomLayerMaskToPlaceObject` | `bool` | – | – |
| Custom Layer Mask To Place Object | `customLayerMaskToPlaceObject` | `LayerMask` | – | – |
| Layer Mask To Attach Object | `layerMaskToAttachObject` | `LayerMask` | – | – |
| Object Can Be Rotated On Y Axis | `objectCanBeRotatedOnYAxis` | `bool` | true | – |
| Object Can Be Rotated On X Axis | `objectCanBeRotatedOnXAxis` | `bool` | – | – |

### Craft Object In Time Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Craft Object In Time | `craftObjectInTime` | `bool` | – | – |
| Time To Craft Object | `timeToCraftObject` | `float` | – | – |

### Craft Ingredients Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Crafting Ingredient Object Info List | `craftingIngredientObjectInfoList` | `List<craftingIngredientObjectInfo>` | new List<craftingIngredientObjectInfo… | – |

### Repair Ingredients Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Repair Ingredient Object Info List | `repairIngredientObjectInfoList` | `List<craftingIngredientObjectInfo>` | new List<craftingIngredientObjectInfo… | – |

### Broken Ingredients Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Broken Ingredient Object Info List | `brokenIngredientObjectInfoList` | `List<craftingIngredientObjectInfo>` | new List<craftingIngredientObjectInfo… | – |

### Disassemble Ingredients Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disassemble Ingredient Object Info List | `disassembleIngredientObjectInfoList` | `List<craftingIngredientObjectInfo>` | new List<craftingIngredientObjectInfo… | – |

### Stats Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Stats Info To Craft | `checkStatsInfoToCraft` | `bool` | – | – |
| Crafting Stat Info To Craft List | `craftingStatInfoToCraftList` | `List<craftingStatInfo>` | new List<craftingStatInfo> () | – |

### Process Material Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Process Material Info List | `processMaterialInfoList` | `List<processMaterialInfo>` | new List<processMaterialInfo> () | – |
