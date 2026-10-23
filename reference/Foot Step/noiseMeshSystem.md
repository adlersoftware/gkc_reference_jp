# noiseMeshSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Foot Step/noiseMeshSystem.cs:5`

**概要**: シングルトンとしてノイズの広がりを表すメッシュを生成し、指定倍率まで拡大させてから破棄するマネージャー。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Noise Meshes Enabled | `noiseMeshesEnabled` | `bool` | true | – |
| Noise Mesh Parent Name | `noiseMeshParentName` | `string` | "Noise Mesh Parent" | – |
| Noise Mesh Prefab | `noiseMeshPrefab` | `GameObject` | – | – |
| Noise Meshes Parent | `noiseMeshesParent` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 未初期化なら自身をシングルトンに設定し、別インスタンスが既にあれば自身を破棄する。 |
| `addNoiseMesh(float scaleMultiplier, Vector3 noisePosition, float noiseExpandSpeed)` | `scaleMultiplier`まで`noiseExpandSpeed`で広がるノイズメッシュを`noisePosition`に生成する。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |

## 内部型

- `footStepState`（class）
