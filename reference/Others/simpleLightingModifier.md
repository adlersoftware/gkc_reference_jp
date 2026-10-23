# simpleLightingModifier

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/simpleLightingModifier.cs:6`

**概要**: 環境光（アンビエント）の色を一括で変更するだけの小さな設定コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Lighting Ambient Equator Setting Enabled | `lightingAmbientEquatorSettingEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setAmbientColor(Color newColor)` | 設定有効時、`RenderSettings`のambient/equator/groundカラーをすべて`newColor`に揃える。 |
| `setAmbientColor(Vector4 newValue)` | 現在のequatorカラーに`newValue`のRGBAを流し込み、`Color`版の`setAmbientColor`へ渡す。 |
| `setAmbientColor(float newValue)` | `newValue`をRGBAすべてに使った`Vector4`を作り、`setAmbientColor`へ渡す。 |
