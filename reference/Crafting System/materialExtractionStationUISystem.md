# materialExtractionStationUISystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Crafting System/materialExtractionStationUISystem.cs:6`

**概要**: 採取ステーションのUI。ゾーン数・各ゾーン残量・エネルギー量のテキストを更新し、稼働中はコルーチンで追従する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Station Enabled | `stationEnabled` | `bool` | true | – |
| No Zones Located String | `noZonesLocatedString` | `string` | "No Material Zons Located" | – |
| Show Max And Remain Energy Amount | `showMaxAndRemainEnergyAmount` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Station Active | `stationActive` | `bool` | – | – |
| Current Energy Amount | `currentEnergyAmount` | `float` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Number Of Zones Located Text | `numberOfZonesLocatedText` | `Text` | – | – |
| Materials Zones State Text | `materialsZonesStateText` | `Text` | – | – |
| Station Energy Amount Text | `stationEnergyAmountText` | `Text` | – | – |
| Main Material Extraction Station System | `mainMaterialExtractionStationSystem` | `materialExtractionStationSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setExtractionActiveState(bool state)` | 稼働状態を切り替えて更新コルーチンを停止し、開始時は再開、停止時はエネルギー表示を更新する。 |
| `stopUpdateCoroutine()` | 実行中の`updateCoroutine`を`StopCoroutine`で止めるだけ。 |
