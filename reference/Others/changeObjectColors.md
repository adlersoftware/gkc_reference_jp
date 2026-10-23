# changeObjectColors

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/changeObjectColors.cs:5`

**概要**: マテリアル群の色を元の色へ時間をかけて戻す補間処理を持つ。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Materials | `materials` | `List<Material>` | new List<Material> () | – |
| Original Color | `originalColor` | `List<Color>` | new List<Color> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentColors(List<Material> materialsList, List<Color> originalColorList)` | 対象マテリアルと元色のリストを差し替え、`Update`の色補間を有効にする。 |
