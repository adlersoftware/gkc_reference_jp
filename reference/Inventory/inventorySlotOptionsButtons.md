# inventorySlotOptionsButtons

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/inventorySlotOptionsButtons.cs:6`

**概要**: インベントリスロットのオプション（使用・装備・破棄など）ボタンの表示を一括制御する UI コンポーネント。有効ボタン数に合わせてパネルの高さも再計算する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Button Height | `buttonHeight` | `int` | – | – |
| Extra Height | `extraHeight` | `int` | – | – |
| Panel Background Offset | `panelBackgroundOffset` | `int` | – | – |

### Show Buttons Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Button Enabled | `useButtonEnabled` | `bool` | true | – |
| Equip Button Enabled | `equipButtonEnabled` | `bool` | true | – |
| Un Equip Button Enabled | `unEquipButtonEnabled` | `bool` | true | – |
| Drop Button Enabled | `dropButtonEnabled` | `bool` | true | – |
| Combine Button Enabled | `combineButtonEnabled` | `bool` | true | – |
| Examine Button Enabled | `examineButtonEnabled` | `bool` | true | – |
| Hold Button Enabled | `holdButtonEnabled` | `bool` | true | – |
| Discard Button Enabled | `discardButtonEnabled` | `bool` | true | – |
| Set On Quick Slots Button Enabled | `setOnQuickSlotsButtonEnabled` | `bool` | true | – |
| Repair Button Enabled | `repairButtonEnabled` | `bool` | true | – |

### UI Components Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Button | `useButton` | `GameObject` | – | – |
| Equip Button | `equipButton` | `GameObject` | – | – |
| Un Equip Button | `unEquipButton` | `GameObject` | – | – |
| Drop Button | `dropButton` | `GameObject` | – | – |
| Combine Button | `combineButton` | `GameObject` | – | – |
| Examine Button | `examineButton` | `GameObject` | – | – |
| Hold Button | `holdButton` | `GameObject` | – | – |
| Discard Button | `discardButton` | `GameObject` | – | – |
| Set On Quick Slots Button | `setOnQuickSlotsButton` | `GameObject` | – | – |
| Repair Button | `repairButton` | `GameObject` | – | – |
| Options Panel | `optionsPanel` | `RectTransform` | – | – |
| Panel Background | `panelBackground` | `RectTransform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setButtonsState(bool useState, bool equipState, bool unEquipState, bool dropState, bool combineState, bool examineState, bool holdState, bool discardState, bool setOnQuickSlotsState, bool repairState)` | 各 `*ButtonEnabled` の無効分を false にして 10 個のボタン表示を切り替え、パネル高さも更新する。 |
