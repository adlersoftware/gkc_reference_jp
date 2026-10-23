# materialExtractionStationSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `craftingStationSystem`
- **ソース**: `Crafting System/materialExtractionStationSystem.cs:6`

**概要**: `craftingStationSystem`を継承した採取ステーション。周囲の`materialsZoneSystem`を探して一定間隔で素材を在庫バンクかスポーンで取り出し、エネルギー消費と供給元を扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Station Enabled | `stationEnabled` | `bool` | true | – |
| Activate Station At Start | `activateStationAtStart` | `bool` | – | – |
| Max Detection Distance | `maxDetectionDistance` | `float` | 10 | – |
| Extraction Zone Transform | `extractionZoneTransform` | `Transform` | – | – |
| Use Max Material Zones To Extract At Same Time | `useMaxMaterialZonesToExtractAtSameTime` | `bool` | – | – |
| Max Material Zones To Extract At Same Time | `maxMaterialZonesToExtractAtSameTime` | `int` | – | – |

### Extraction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use General Material Extraction Rate | `useGeneralMaterialExtractionRate` | `bool` | – | – |
| General Material Extraction Rate | `generalMaterialExtractionRate` | `float` | – | – |
| Use General Material Extraction Amount | `useGeneralMaterialExtractionAmount` | `bool` | – | – |
| General Material Extraction Amount | `generalMaterialExtractionAmount` | `int` | – | – |
| Station Can Only Extract Custom Material List | `stationCanOnlyExtractCustomMaterialList` | `bool` | – | – |
| Custom Material List To Extract | `customMaterialListToExtract` | `List<string>` | new List<string> () | – |

### Custom Materials Zone To Use Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Material Zones Found | `ignoreMaterialZonesFound` | `bool` | – | – |
| Extract Materials Even If Not Zone Found | `extractMaterialsEvenIfNotZoneFound` | `bool` | – | – |
| Custom Material Zone System | `customMaterialZoneSystem` | `materialsZoneSystem` | – | – |

### Extraction Conditions Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore To Extract Materials From ID List | `ignoreToExtractMaterialsFromIDList` | `bool` | – | – |
| Materials ID List To Ignore | `materialsIDListToIgnore` | `List<int>` | new List<int> () | – |

### Spawn Extracted Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Spawn Extracted Objects | `spawnExtractedObjects` | `bool` | – | – |
| Position To Spawn Extracted Objects | `positionToSpawnExtractedObjects` | `Transform` | – | – |
| Add Force To Spawned Objects | `addForceToSpawnedObjects` | `bool` | – | – |
| Force Mode On Spawned Objects | `forceModeOnSpawnedObjects` | `ForceMode` | – | – |
| Force Amount On Spawned Objects | `forceAmountOnSpawnedObjects` | `float` | – | – |
| Pack Extracted Objects Before Spawn | `packExtractedObjectsBeforeSpawn` | `bool` | – | – |
| Min Amount To Pack To Spawn | `minAmountToPackToSpawn` | `int` | – | – |

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
| Materials Zone System Located List | `materialsZoneSystemLocatedList` | `List<materialsZoneSystem>` | new List<materialsZoneSystem> () | – |
| Energy Source Located | `energySourceLocated` | `bool` | – | – |
| Number Of Zones Located | `numberOfZonesLocated` | `int` | – | – |
| Material Zones Systems ID To Ignore List | `materialZonesSystemsIDToIgnoreList` | `List<int>` | new List<int> () | – |
| Extracted Material Info List | `extractedMaterialInfoList` | `List<extractedMaterialInfo>` | new List<extractedMaterialInfo> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Activate Station | `eventOnActivateStation` | `UnityEvent` | – | – |
| Eventon Deactivate Station | `eventonDeactivateStation` | `UnityEvent` | – | – |
| Event On Energy Empty | `eventOnEnergyEmpty` | `UnityEvent` | – | – |
| Event On Energy Recharge | `eventOnEnergyRecharge` | `UnityEvent` | – | – |
| Event On Energy Refilled | `eventOnEnergyRefilled` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Inventory Bank System | `mainInventoryBankSystem` | `inventoryBankSystem` | – | – |
| Inventory Bank Energy Source | `inventoryBankEnergySource` | `inventoryBankSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `toggleExtraction()` | `setExtractionActiveState(!stationActive)`を呼ぶだけ。 |
| `setExtractionActiveState(bool state)` | 開始時はエネルギー確認後に周囲ゾーンを探索し、停止時はコルーチン停止と各ゾーンの採取中フラグ解除を行う。 |
| `stopUpdateCoroutine()` | 実行中の`updateCoroutine`を`StopCoroutine`で止めるだけ。 |
| `addEnergy(float newValue)` | エネルギー制なら量を加算して上限でクランプし、満タンなら補充イベント、未満なら充電イベントを発火する。 |
| `refullEnergy()` | `addEnergy`に最大量を渡して満タンにするだけ。 |
| `removeEnergySource()` | エネルギー供給バンクを外し、現在量を無限設定なら1、通常は0にする。 |
| `getCurrentEnergyAmount()` | `currentEnergyAmount`を返すだけ。 |
| `getMaxEnergyAmount()` | `maxEnergyAmount`を返すだけ。 |
| `setEnergySource(inventoryBankSystem newBank)` | `inventoryBankEnergySource`を設定して`energySourceLocated`を更新するだけ。 |
| `canExtractMaterial(string materialName)` | カスタム素材限定なら`customMaterialListToExtract`に含まれるかを返し、限定なしならtrueを返す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnActivateStation` | `UnityEvent` | – |
| `eventonDeactivateStation` | `UnityEvent` | – |
| `eventOnEnergyEmpty` | `UnityEvent` | – |
| `eventOnEnergyRecharge` | `UnityEvent` | – |
| `eventOnEnergyRefilled` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkEnergyStationOnStateChange()`, `sendEnergyValue(float newAmount)`

</details>

## 内部型

- `extractedMaterialInfo`（class）
