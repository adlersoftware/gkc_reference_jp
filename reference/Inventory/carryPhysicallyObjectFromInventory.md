# carryPhysicallyObjectFromInventory

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `objectOnInventory`
- **ソース**: `Inventory/carryPhysicallyObjectFromInventory.cs:5`

**概要**: `objectOnInventory` を継承し、インベントリから取り出したオブジェクトをプレイヤーに物理的に持たせる処理を担当する。掴む／落とす瞬間のインタラクションパネル表示の切り替えも行う。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disable Interaction Panel While Grabbed | `disableInteractionPanelWhileGrabbed` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Player | `currentPlayer` | `GameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Grab Physical Object System | `mainGrabPhysicalObjectSystem` | `grabPhysicalObjectSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentPlayer(GameObject newPlayer)` | `currentPlayer` に `newPlayer` を代入するだけ。 |
| `checkObjectStateOnGrab()` | フラグが有効なら、`deviceStringAction` のアイコンを隠し、プレイヤーの `usingDevicesSystem` を更新する。 |
| `checkObjectStateOnDrop()` | フラグが有効なら、`deviceStringAction` のアイコンを表示し直し、プレイヤーの `usingDevicesSystem` を更新する。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`carryPhysicalObjectFromInventory(GameObject newPlayer)`

</details>
