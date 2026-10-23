# openStructure

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Demo/openStructure.cs:5`

**概要**: `objectsToFade`のアルファを徐々に変化させ、透明シェーダーとColliderの有効/無効で構造物の出入りを可能にするデモ用コンポーネント。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Objects To Fade | `objectsToFade` | `List<GameObject>` | new List<GameObject> () | – |
| Transparent | `transparent` | `Shader` | – | – |
| Normal Shader | `normalShader` | `Shader` | – | – |
| Activate | `activate` | `bool` | – | – |
| Changed | `changed` | `bool` | – | – |
| Option | `option` | `int` | 1 | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `changeStructureState()` | `option`の符号を反転して`activate`をtrueにし、Updateのフェード処理を開始する。 |
