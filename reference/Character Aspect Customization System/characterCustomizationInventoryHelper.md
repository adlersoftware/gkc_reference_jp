# characterCustomizationInventoryHelper

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `inventoryManagerInfo`
- **ソース**: `Character Aspect Customization System/characterCustomizationInventoryHelper.cs:6`

**概要**: 現在装備中のカスタマイズ要素を`inventoryInfo`としてインベントリ用リストに変換する補助コンポーネントです。フルアーマーセットが完成している場合は`extraInventoryInfoList`から追加アイテムも加えます。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Character Elements Equipped | `setCharacterElementsEquipped` | `bool` | true | – |
| Amount On Elements | `amountOnElements` | `int` | 1 | – |

### Extra Inventory Objects

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Extra Inventory Objects For Armor Set | `useExtraInventoryObjectsForArmorSet` | `bool` | – | – |
| Extra Inventory Info List | `extraInventoryInfoList` | `List<extraInventoryInfo>` | new List<extraInventoryInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Character Customization Manager | `mainCharacterCustomizationManager` | `characterCustomizationManager` | – | – |
| Main Inventory List Manager | `mainInventoryListManager` | `inventoryListManager` | – | – |
| Main Full Armor Cloth Template Data | `mainFullArmorClothTemplateData` | `fullArmorClothTemplateData` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `storeCustomizationElementsAsInventory()` | `inventoryList`を空にし、装備中パーツを数量・装備状態付きで追加、フルセット時は追加アイテムも加える。 |
| `setMainCharacterCustomizationManager(characterCustomizationManager newCharacterCustomizationManager)` | `mainCharacterCustomizationManager`を代入するだけ。 |
| `setMainFullArmorClothTemplateData(fullArmorClothTemplateData newFullArmorClothTemplateData)` | `mainFullArmorClothTemplateData`を代入するだけ。 |
| `setNewCharacterModel(GameObject newObject)` | 新モデルの`characterCustomizationManager`を設定し、あればフルアーマーテンプレートも差し替える。 |

## 内部型

- `extraInventoryInfo`（class）
