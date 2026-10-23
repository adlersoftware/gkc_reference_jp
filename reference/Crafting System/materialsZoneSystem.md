# materialsZoneSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Crafting System/materialsZoneSystem.cs:6`

**概要**: 採取可能な素材量を素材ごとに持つゾーン。採取で残量が減り、空になると無効化と任意の遅延再補充を行い、外部要素からの採取も処理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Materials Zone Enabled | `materialsZoneEnabled` | `bool` | true | – |
| Materials Zone Can Change Position | `materialsZoneCanChangePosition` | `bool` | – | – |
| Material Zone ID | `materialZoneID` | `int` | – | – |

### Extraction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Material Extraction Rate | `materialExtractionRate` | `float` | – | – |
| Material Extraction Amount | `materialExtractionAmount` | `int` | – | – |

### Spawn Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Max Radius To Instantiate | `maxRadiusToInstantiate` | `float` | 1 | – |
| Position To Spawn Extracted Objects | `positionToSpawnExtractedObjects` | `Transform` | – | – |
| Add Force To Spawned Objects | `addForceToSpawnedObjects` | `bool` | – | – |
| Force Mode On Spawned Objects | `forceModeOnSpawnedObjects` | `ForceMode` | – | – |
| Force Amount On Spawned Objects | `forceAmountOnSpawnedObjects` | `float` | – | – |
| Force Radius On Spawned Objects | `forceRadiusOnSpawnedObjects` | `float` | – | – |

### Material Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Material Zone Info List | `materialZoneInfoList` | `List<materialZoneInfo>` | new List<materialZoneInfo> () | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Refill Materials Zone After Delay On Empty | `refillMaterialsZoneAfterDelayOnEmpty` | `bool` | – | – |
| Delay To Refill Materials On Empty | `delayToRefillMaterialsOnEmpty` | `float` | – | – |
| Can Be Extracted By External Elements Enabled | `canBeExtractedByExternalElementsEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remain Materials Amount | `remainMaterialsAmount` | `int` | – | – |
| Materials Zone Empty | `materialsZoneEmpty` | `bool` | – | – |
| Materials Zone Full | `materialsZoneFull` | `bool` | true | – |
| Materials Zone Extraction In Process | `materialsZoneExtractionInProcess` | `bool` | – | – |
| Material Extraction Stations Active | `materialExtractionStationsActive` | `int` | – | – |
| Refill In Process | `refillInProcess` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Zone Empty | `useEventOnZoneEmpty` | `bool` | – | – |
| Event On Zone Empty | `eventOnZoneEmpty` | `UnityEvent` | – | – |
| Use Event On Zone Refilled | `useEventOnZoneRefilled` | `bool` | – | – |
| Event On Zone Refilled | `eventOnZoneRefilled` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setMaterialsZoneExtractionInProcessState(bool state)` | 採取中ステーション数を増減してフラグを更新し、採取開始時に満杯なら残量を数えて`materialsZoneFull`を解除する。 |
| `getRemainMaterialsAmount()` | `materialZoneInfoList`の素材量を合計して`remainMaterialsAmount`に格納し返す。 |
| `setMaterialsZoneFullState(bool state)` | フラグを設定し、trueなら全素材を最大量に戻して有効化し、補充イベントを発火する。 |
| `isMaterialsZoneEnabled()` | `materialsZoneEnabled`を返すだけ。 |
| `setMaterialsZoneEmptyState(bool state)` | 素材が残っていれば空状態を解除し、完全に空なら空イベント発火・無効化・遅延再補充コルーチン開始を行う。 |
| `isMaterialsZoneEmpty()` | `materialsZoneEmpty`を返すだけ。 |
| `isCanBeExtractedByExternalElementsEnabled()` | `canBeExtractedByExternalElementsEnabled`を返すだけ。 |
| `getMaterialZoneID()` | `materialZoneID`を返すだけ。 |
| `stopRefillMaterialsZoneCoroutine()` | 再補充コルーチンを停止し`refillInProcess`をfalseにするだけ。 |
| `checkMaterialZoneToExtractExternally()` | 空でなければ各素材を採取量分減らして在庫オブジェクトを生成・散布し、全素材が尽きたら空状態にする。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnZoneEmpty` | `UnityEvent` | – |
| `eventOnZoneRefilled` | `UnityEvent` | – |

## 内部型

- `materialZoneInfo`（class）
