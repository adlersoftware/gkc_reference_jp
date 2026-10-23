# inventoryCaptureManagerTransparent

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/inventoryCaptureManagerTransparent.cs:10`

**概要**: `UNITY_EDITOR` 時のみ有効な、背景透過アイコン生成用コンポーネント。白背景と黒背景の 2 枚からアルファを算出して透過 PNG を書き出す。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| File Name | `fileName` | `string` | "New Capture" | – |
| Relative Path Captures | `relativePathCaptures` | `string` | "" | – |
| Extra Name | `extraName` | `string` | "(Inventory Capture)" | – |
| Object To Capture Parent | `objectToCaptureParent` | `Transform` | – | – |
| Use Object Name | `useObjectName` | `bool` | – | – |

### Others

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Explanation | `explanation` | `string` | – | TextArea (10, 15) |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `takeCapture()` | `EditorApplication.isPlaying` を true にして再生を開始するだけ（撮影は再生中のコルーチンが行う）。 |
