# inventoryMenuPanelsSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/inventoryMenuPanelsSystem.cs:7`

**概要**: インベントリ内の複数パネルを名前で切り替えるステート管理コンポーネント。選択中のパネルだけを有効にし、位置・スケール調整やイベント発火を行う。

**公式ドキュメント抜粋**（[Inventory Menu Panels System](../../docs/player-controller-components/essential-components/inventory-menu-panels-system.md)）

> Used to configure different designs of the inventory menu, mostly used to show a full inventory menu or a more simplified with the inventory grid on the side of the screen, to allow to see the actual world on the scene to use inventory objects on it, similar to last Resident Evil games and remakes.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set State On Start | `setStateOnStart` | `bool` | – | ONにすると開始時に指定したパネル状態へ切替える。 |
| State On Start | `stateOnStart` | `string` | – | 開始時に適用するパネルの名前。 |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current State | `currentState` | `string` | – | 現在表示中のパネル名(デバッグ表示用)。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `inventoryPanelsInfoList` | `List<inventoryPanelsInfo>` | new List<inventoryPanelsInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setInventoryPanelByName(string panelName)` | 指定名以外のパネルを無効化し、一致パネルを有効化して `currentState` とイベントを更新する。 |

## 内部型

- `inventoryPanelsInfo`（class）
- `inventoryPanelInfo`（class）
