# simpleInventoryContentManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/simpleInventoryContentManager.cs:5`

**概要**: インベントリ内容を簡易リスト `simpleInventoryInfoList` として保持し、武器・弾薬の数量同期やセーブ用リスト生成を行うコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Initial Inventory List Enabled | `setInitialInventoryListEnabled` | `bool` | – | – |

### List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Simple Inventory Info List | `simpleInventoryInfoList` | `List<simpleInventoryInfo>` | new List<simpleInventoryInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Weapon Info | `currentWeaponInfo` | `simpleInventoryInfo` | – | – |
| Current Weapon Info Assigned | `currentWeaponInfoAssigned` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Inventory Manager | `mainInventoryManager` | `inventoryManager` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentWeaponObject(string weaponName)` | リストを更新したうえで、`weaponName` に一致する要素を現在武器に設定する。 |
| `updateCurrentWeaponRemainMagazine(int amount)` | 現在武器が設定済みなら、その `projectilesInMagazine` を `amount` にする。 |
| `updateSimpleInventoryObjectInfo(string objectName, int amount)` | 同名要素が見つかれば `amount` を代入するだけ。 |
| `updateCurrentSimpleInventoryList()` | 数量が 0 より大きい品から `simpleInventoryInfoList` を作り直し、武器の弾倉数も反映して現在武器を設定する。 |
| `getCurrentInventoryList()` | 数量が 0 より大きい品から、セーブ用の `inventoryListManagerList` を作り直す。 |
| `setCurrentAmmoValues(List<int> ammoAmountList)` | リストの各値を各武器の弾薬に上書き設定し、最後に簡易リストを更新する。 |
| `setCurrentAmmoValuesOnWeapon(int weaponIndex, int currentAmmoAmountToSet)` | 指定武器に対応する弾薬の在庫を新しい値で置き換え、武器と UI の弾薬表示を更新する。 |
| `addAmmoToWeapon(int weaponIndex, int ammoAmountToAdd)` | 内部フラグを加算モードにして `setCurrentAmmoValuesOnWeapon` を呼び、弾薬を追加する。 |

## 内部型

- `simpleInventoryInfo`（class）
