# customNoiseSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Foot Step/customNoiseSystem.cs:6`

**概要**: 名前付きのノイズ状態リストを持ち、指定した状態の半径やデシベルでノイズ検知・ノイズメッシュ・イベントを発生させるコンポーネント。

## インスペクター設定

### Noise State Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Noise State Info List | `noiseStateInfoList` | `List<noiseStateInfo>` | new List<noiseStateInfo> () | – |
| Use Noise Mesh | `useNoiseMesh` | `bool` | true | – |
| Main Noise Mesh Manager Name | `mainNoiseMeshManagerName` | `string` | "Noise Mesh Manager" | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Noise Origin Transform | `noiseOriginTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setNoiseState(string stateName)` | 名前が一致して有効なノイズ状態をカレントに設定し、その場で`activateNoise`を呼ぶ。 |
| `activateNoise()` | カレントのノイズ状態が有効なら、ノイズ検知の送信とノイズメッシュ生成、設定時のイベント発火を行う。 |

## 内部型

- `noiseStateInfo`（class）
