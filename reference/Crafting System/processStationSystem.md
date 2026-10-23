# processStationSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `craftingStationSystem`
- **ソース**: `Crafting System/processStationSystem.cs:5`

**概要**: `craftingStationSystem`を継承した加工ステーション。素材バンクの素材をブループリントの加工情報に従って加工品バンクへ変換し、エネルギーを消費する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Station Enabled | `stationEnabled` | `bool` | true | – |
| Material Process Name List | `materialProcessNameList` | `List<string>` | new List<string> () | – |

### Process Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Process Rate | `processRate` | `float` | – | – |

### Energy Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Energy To Extract | `useEnergyToExtract` | `bool` | – | – |
| Max Energy Amount | `maxEnergyAmount` | `float` | – | – |
| Current Energy Amount | `currentEnergyAmount` | `float` | – | – |
| Use Energy Rate | `useEnergyRate` | `float` | – | – |
| Energy To Use Amount | `energyToUseAmount` | `float` | – | – |
| Use Energy From Inventory Bank | `useEnergyFromInventoryBank` | `bool` | – | – |
| Energy Object Name | `energyObjectName` | `string` | – | – |
| Check Energy Object Name On Energy Station | `checkEnergyObjectNameOnEnergyStation` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Station Active | `stationActive` | `bool` | – | – |
| Energy Source Located | `energySourceLocated` | `bool` | – | – |
| Material Info List | `materialInfoList` | `List<materialInfo>` | new List<materialInfo> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory Bank Materials Processed | `inventoryBankMaterialsProcessed` | `inventoryBankSystem` | – | – |
| Inventory Bank Materials Source | `inventoryBankMaterialsSource` | `inventoryBankSystem` | – | – |
| Inventory Bank Energy Source | `inventoryBankEnergySource` | `inventoryBankSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `toggleProcessStation()` | `setStationActiveState(!stationActive)`を呼ぶだけ。 |
| `setStationActiveState(bool state)` | 稼働状態を切り替え、エネルギー供給判定とブループリント取得を行い、稼働中のみ更新コルーチンを動かす。 |
| `stopUpdateCoroutine()` | 実行中の`updateCoroutine`を`StopCoroutine`で止めるだけ。 |
| `getProcessMaterialInfoByName(string objectName)` | ブループリントから名前一致かつ加工名リストに含まれる加工情報を探して返し、なければnullを返す。 |

## 内部型

- `materialInfo`（class）
