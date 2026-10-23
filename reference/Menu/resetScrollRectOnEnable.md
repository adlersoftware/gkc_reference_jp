# resetScrollRectOnEnable

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Menu/resetScrollRectOnEnable.cs:6`

**概要**: 有効化時にレイアウトを再構築し、スクロール位置を指定値へ戻す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Reset Enabled | `resetEnabled` | `bool` | true | – |
| Use Vertical Position | `useVerticalPosition` | `bool` | – | – |
| Position Value | `positionValue` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Rect Transform | `mainRectTransform` | `RectTransform` | – | – |
| Main Scroll Rect | `mainScrollRect` | `ScrollRect` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `resetRectTransform()` | 自身がアクティブなら位置リセットのコルーチンを開始するだけ。 |
