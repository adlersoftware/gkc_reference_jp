# inventoryManagerInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/inventoryManagerInfo.cs:5`

**概要**: プレイヤーのインベントリ情報（スロット数・無限スロット・保存/読込設定・最後の武器名・空状態）を保持する基底コンポーネント。多くの処理は派生クラス向けの空実装として用意されている。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Save Current Player Inventory To Save File | `saveCurrentPlayerInventoryToSaveFile` | `bool` | true | – |
| Load Current Player Inventory From Save File | `loadCurrentPlayerInventoryFromSaveFile` | `bool` | true | – |
| Set Infinite Slot Values On Save Load | `setInfiniteSlotValuesOnSaveLoad` | `bool` | true | – |
| Inventory Slot Amount | `inventorySlotAmount` | `int` | – | – |
| Infinite Slots | `infiniteSlots` | `bool` | – | – |
| Inventory List | `inventoryList` | `List<inventoryInfo>` | new List<inventoryInfo> () | – |
| Is Loading Game | `isLoadingGame` | `bool` | – | – |
| Last Weapon Carried On Hands Name | `lastWeaponCarriedOnHandsName` | `string` | "" | – |
| Inventory Was Empty When Saved | `inventoryWasEmptyWhenSaved` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `InitializeAudioElements()` | – |
| `isSaveCurrentPlayerInventoryToSaveFileActive()` | `saveCurrentPlayerInventoryToSaveFile`を返すだけ。 |
| `isLoadCurrentPlayerInventoryFromSaveFileActive()` | `loadCurrentPlayerInventoryFromSaveFile`を返すだけ。 |
| `setInventorySlotAmountValue(int newValue)` | `inventorySlotAmount`を設定するだけ。 |
| `getInventorySlotAmount()` | `inventorySlotAmount`を返すだけ。 |
| `setInfiniteSlotsState(bool state)` | `infiniteSlots`を設定するだけ。 |
| `isSetInfiniteSlotValuesOnSaveLoadActive()` | `setInfiniteSlotValuesOnSaveLoad`を返すだけ。 |
| `isInfiniteSlotsActive()` | `infiniteSlots`を返すだけ。 |
| `initializeInventoryValues()` | 本体が空で何もしない。初期化を派生クラスで実装する仮想メソッド。 |
| `getInventoryList()` | `inventoryList`を返すだけ。 |
| `getCurrentInventoryListManagerList()` | 本体が空で常にnullを返す。派生クラスで実装する仮想メソッド。 |
| `setNewInventoryListManagerList(List<inventoryListElement> newList)` | 本体が空で何もしない。派生クラスで実装する仮想メソッド。 |
| `setIsLoadingGameState(bool state)` | `isLoadingGame`を設定するだけ。 |
| `isLoadingGameState()` | `isLoadingGame`を返すだけ。 |
| `updateDurabilityAmountStateOnAllInventoryObjects()` | 本体が空で何もしない。耐久値の反映を派生クラスで実装する仮想メソッド。 |
| `getLastWeaponCarriedOnHandsName()` | `lastWeaponCarriedOnHandsName`を返すだけ。 |
| `setLastWeaponCarriedOnHandsName(string objectName)` | `lastWeaponCarriedOnHandsName`を設定するだけ。 |
| `setInventoryWasEmptyWhenSavedState(bool state)` | `inventoryWasEmptyWhenSaved`を設定するだけ。 |
| `getInventoryWasEmptyWhenSaved()` | `inventoryWasEmptyWhenSaved`を返すだけ。 |
