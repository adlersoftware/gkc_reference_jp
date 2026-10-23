# skidsManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/skidsManager.cs:4`

**概要**: タイヤ痕を1つのメッシュに蓄積して描画するスキッドマーク管理。追加された節点から頂点・法線・UV・三角形を組み直す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Skids Enabled | `skidsEnabled` | `bool` | true | – |
| Max Marks | `maxMarks` | `int` | 1000 | – |
| Mark Width | `markWidth` | `float` | 0.3f | – |
| Ground Offset | `groundOffset` | `float` | 0.02f | – |
| Min Distance | `minDistance` | `float` | 0.1f | – |

### Debugs

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Original Mesh | `originalMesh` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `AddSkidMark(Vector3 pos, Vector3 normal, float intensity, int lastIndex)` | 無効なら-1を返し、円環インデックスに節点を記録して幅方向の左右頂点を計算し、更新フラグを立てて通し番号を返す。 |
| `setSkidsEnabledState(bool state)` | `skidsEnabled`を設定するだけ。 |

## 内部型

- `markSection`（class）
