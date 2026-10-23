# replaceMaterialSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/replaceMaterialSystem.cs:5`

**概要**: 対象オブジェクトのマテリアルを一括で差し替え、元のマテリアルへ戻せるようにする。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Replace Materials Enabled | `replaceMaterialsEnabled` | `bool` | true | – |

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Use | `objectToUse` | `GameObject` | – | – |
| Material To Replace | `materialToReplace` | `Material` | – | – |
| Render Info List | `renderInfoList` | `List<renderInfo>` | new List<renderInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setMaterialState(bool state)` | `renderInfoList`の各`Renderer`で、`state`なら全スロットを`materialToReplace`に、そうでなければ保存したマテリアルに戻す。 |
| `checkObjectMaterials()` | `renderInfoList`が空の時、`objectToUse`配下の`Renderer`（パーティクル除く）とそのマテリアルを収集して記録する。 |

## 内部型

- `renderInfo`（class）
