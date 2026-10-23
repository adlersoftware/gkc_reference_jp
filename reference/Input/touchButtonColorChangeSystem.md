# touchButtonColorChangeSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Input/touchButtonColorChangeSystem.cs:6`

**概要**: タッチボタンの`RawImage` 色を通常時と押下時で切り替えるだけの小コンポーネント。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Image | `mainImage` | `RawImage` | – | – |
| Regular Color | `regularColor` | `Color` | – | – |
| Pressed Color | `pressedColor` | `Color` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setRegularColor()` | `mainImage` の色を`regularColor` にするだけ。 |
| `setPressedColor()` | `mainImage` の色を`pressedColor` にするだけ。 |
