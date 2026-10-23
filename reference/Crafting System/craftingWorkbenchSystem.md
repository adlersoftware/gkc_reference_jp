# craftingWorkbenchSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Crafting System/craftingWorkbenchSystem.cs:6`

**概要**: 作業台。プレイヤーの`craftingSystem`に自身を現在の作業台として登録し、クラフト画面の開放/終了と在庫バンクへの格納を扱う。

## インスペクター設定

### Main Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Workbench ID | `workbenchID` | `int` | – | – |
| Allow To Craft All Objects On Current Bench | `allowToCraftAllObjectsOnCurrentBench` | `bool` | – | – |
| Set Object Categories To Craft Available On Current Bench | `setObjectCategoriesToCraftAvailableOnCurrentBench` | `bool` | – | – |
| Object Categories To Craft Available On Current Bench | `objectCategoriesToCraftAvailableOnCurrentBench` | `List<string>` | new List<string> () | – |

### Repair/Disassemble/Upgrade Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Repair Objects Only On Workbench Enabled | `repairObjectsOnlyOnWorkbenchEnabled` | `bool` | true | – |
| Disassemble Objects Only On Workbench Enabled | `disassembleObjectsOnlyOnWorkbenchEnabled` | `bool` | true | – |
| Upgrade Objects Only On Workbenche Enabled | `upgradeObjectsOnlyOnWorkbencheEnabled` | `bool` | true | – |

### Other Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Current Object Mesh | `showCurrentObjectMesh` | `bool` | – | – |
| Current Object Mesh Place Transform | `currentObjectMeshPlaceTransform` | `Transform` | – | – |

### Inventory Bank Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Store Crafted Objects On Inventory Bank | `storeCraftedObjectsOnInventoryBank` | `bool` | – | – |
| Store Crafted Objects On Inventory Bank Only If Player Inventory Is Full | `storeCraftedObjectsOnInventoryBankOnlyIfPlayerInventoryIsFull` | `bool` | – | – |
| Main Inventory Bank System | `mainInventoryBankSystem` | `inventoryBankSystem` | – | – |

### Event Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Stop Using Workbench On Damage Received | `eventToStopUsingWorkbenchOnDamageReceived` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateWorkbench(GameObject currentPlayer)` | `currentPlayer`の`craftingSystem`に自身を作業台として登録し、作業台経由のクラフト画面を開く。 |
| `deactivateWorkBench(GameObject currentPlayer)` | `currentPlayer`の作業台登録を解除し、作業台経由のクラフト画面を閉じる。 |
| `addInventoryObjectByName(string objectName, int amountToMove)` | `mainInventoryBankSystem`にオブジェクト名と数量を渡して追加するだけ。 |
| `checkEventToStopUsingWorkbenchOnDamageReceived()` | `eventToStopUsingWorkbenchOnDamageReceived`を発火するだけ。 |
| `getWorkbenchID()` | `workbenchID`を返すだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToStopUsingWorkbenchOnDamageReceived` | `UnityEvent` | – |
