# inventoryObjectToEquipInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/inventoryObjectToEquipInfo.cs:5`

**概要**: 装備対象オブジェクト用の基底 `MonoBehaviour`。3 メソッドとも virtual で、既定実装は false を返すか何もしないだけ。

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setObjectEquippedState(bool state)` | 何もせず `false` を返すだけの仮想メソッドで、実装は継承先に委ねる。 |
| `isObjectEquipped()` | `false` を返すだけの仮想メソッド。 |
| `updateObjectState()` | 本体が空で何もしない仮想メソッド。 |
