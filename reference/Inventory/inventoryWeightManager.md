# inventoryWeightManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/inventoryWeightManager.cs:9`

**概要**: プレイヤーの所持重量と重量上限を管理するコンポーネント。インベントリ全体の重量を集計して UI とイベントに反映し、オブジェクトを運べるかも判定する。

**公式ドキュメント抜粋**（[Inventory Weight Manager](../../docs/player-controller-components/essential-components/inventory-weight-manager.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Inventory Weight Enabled | `useInventoryWeightEnabled` | `bool` | true | – |
| Use Inventory Weight Limit | `useInventoryWeightLimit` | `bool` | – | – |
| Inventory Weight Limit | `inventoryWeightLimit` | `float` | – | – |
| Weight Unit | `weightUnit` | `string` | "Kg" | – |
| Current Total Weight | `currentTotalWeight` | `float` | – | – |
| Use Max Object Weight To Pick | `useMaxObjectWeightToPick` | `bool` | – | – |
| Max Object Weight To Pick | `maxObjectWeightToPick` | `float` | – | – |
| Inventory Weight Limit Stat Name | `inventoryWeightLimitStatName` | `string` | "Inventory Weight Limit" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Weight Limit Reached | `weightLimitReached` | `bool` | – | – |
| Weight Limit Reached Previously | `weightLimitReachedPreviously` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Regular Weight | `eventOnRegularWeight` | `UnityEvent` | – | – |
| Even On Weight Limit Reached | `evenOnWeightLimitReached` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory Weight Panel | `inventoryWeightPanel` | `GameObject` | – | – |
| Current Object Weight Text | `currentObjectWeightText` | `Text` | – | – |
| Total Inventory Weight Text | `totalInventoryWeightText` | `Text` | – | – |
| Total Inventory Weight Slider | `totalInventoryWeightSlider` | `Slider` | – | – |
| Main Inventory Manager | `mainInventoryManager` | `inventoryManager` | – | – |
| Current Inventory Object Weight Panel | `currentInventoryObjectWeightPanel` | `GameObject` | – | – |
| Player Stats Manager | `playerStatsManager` | `playerStatsSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateCurrentInventoryObjectWeight()` | 重量有効時、選択中オブジェクトの単重と合計重量を計算してパネルに表示し、対象が無ければパネルを隠す。 |
| `disableCurrentInventoryObjectWeight()` | `currentInventoryObjectWeightPanel` が表示中なら非表示にするだけ。 |
| `updateInventoryWeight()` | 重量有効時、実行中の更新コルーチンを止めて再集計コルーチンを開始する。 |
| `checkIfCanCarryObjectWeight(inventoryInfo inventoryInfoToCheck)` | 重量上限までの空きから運べる数量を `int` で返し、機能無効時は -1 を返す。 |
| `checkIfCanCarrySingleObjectWeight(inventoryInfo inventoryInfoToCheck)` | 単体重量が `maxObjectWeightToPick` を超える場合だけ false を返す（機能無効時は true）。 |
| `initializeInventoryWeightLimitAmount(float newValue)` | `inventoryWeightLimit` を `newValue` にするだけ。 |
| `increaseInventoryWeightLimitAmount(float newValue)` | 上限に `newValue` を加算し、`updateInventoryWeight` で再集計する。 |
| `updateInventoryWeightLimitAmountWithoutUpdatingStatManager(int statId, float amount)` | ステータスを更新せず上限を `amount` にするだけ。`statId` は未使用。 |
| `increaseInventoryBagWeight(float newValue)` | 重量有効時、上限を加算したうえで `playerStatsManager` の重量上限ステータスを更新する。 |
| `setUseInventoryWeightEnabledState(bool state)` | `useInventoryWeightEnabled` を `state` にするだけ。 |
| `setUseInventoryWeightEnabledStateFromEditor(bool state)` | 有効フラグを設定したうえで `updateComponent` を呼ぶ。 |
| `updateComponent()` | `GKC_Utils.updateComponent` と `updateDirtyScene` でインスペクタとシーンを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnRegularWeight` | `UnityEvent` | – |
| `evenOnWeightLimitReached` | `UnityEvent` | – |
