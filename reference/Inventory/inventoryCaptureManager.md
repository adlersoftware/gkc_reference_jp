# inventoryCaptureManager

- **種別**: class
- **継承 / 実装**: `EditorWindow`
- **ソース**: `Inventory/inventoryCaptureManager.cs:11`

**概要**: `UNITY_EDITOR` 時のみ有効なエディタ用 `EditorWindow`。インベントリアイテムのアイコン用キャプチャを撮影して PNG 保存し、`inventoryListManager` に設定する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Capture Resolution | `captureResolution` | `Vector2` | new Vector2 (512, 512) | – |
| Rotation Offset | `rotationOffset` | `Vector3` | – | – |
| Position Offset | `positionOffset` | `Vector3` | – | – |
| File Name | `fileName` | `string` | "New Capture" | – |
| Inventory Layer Name | `inventoryLayerName` | `string` | "inventory" | – |
| Main Inventory Manager Name | `mainInventoryManagerName` | `string` | "Main Inventory Manager" | – |
| Main Inventory List Manager | `mainInventoryListManager` | `inventoryListManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `init()` | 画面解像度からウィンドウ寸法を決め、`inventoryListManager` とカメラ・配置用トランスフォームを取得してキャプチャツールを開状態にする。 |
| `getCapture()` | カメラを RenderTexture に描画して PNG を保存し、カメラ設定を戻して取り込み待ちフラグを立てる。 |
| `closeWindow()` | 補助メッシュを破棄してからウィンドウを閉じるだけ。 |
| `destroyAuxObjects()` | `DestroyImmediate` で `currentInventoryObjectMesh` を削除するだけ。 |
| `setCurrentInventoryObjectInfo(inventoryInfo info, string savePath)` | 情報と保存先を保持し、`inventoryGameObject` を複製して配置し、レイヤーが一致しているかも確認する。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnDisable()`

</details>
