# simpleDeviceStationSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `craftingStationSystem`
- **ソース**: `Crafting System/simpleDeviceStationSystem.cs:6`

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Station Enabled | `stationEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Station Active | `stationActive` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Connect Input | `eventOnConnectInput` | `UnityEvent` | – | – |
| Event On Disconnect Input | `eventOnDisconnectInput` | `UnityEvent` | – | – |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnConnectInput` | `UnityEvent` | – |
| `eventOnDisconnectInput` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkStateOnRemoveInput()`, `checkStateOnSetInput()`

</details>
