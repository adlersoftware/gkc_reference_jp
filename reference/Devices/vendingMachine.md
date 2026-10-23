# vendingMachine

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/vendingMachine.cs:5`

**概要**: 自販機型のオブジェクト生成器。有効時のみ、指定位置（半径内のランダム位置も可）にプレハブを出現させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vending Machine Enabled | `vendingMachineEnabled` | `bool` | true | – |
| Radius To Spawn | `radiusToSpawn` | `float` | – | – |
| Use Spawn Limit Amount | `useSpawnLimitAmount` | `bool` | – | – |
| Spawn Limit Amount | `spawnLimitAmount` | `int` | – | – |

### Object To Spawn Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Spawn | `objectToSpawn` | `GameObject` | – | – |
| Spawn Position | `spawnPosition` | `Transform` | – | – |
| Spawn Object List | `spawnObjectList` | `bool` | – | – |
| Object List To Spawn | `objectListToSpawn` | `List<GameObject>` | new List<GameObject> () | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setVendingMachineEnabledState(bool state)` | `vendingMachineEnabled`を設定するだけ。 |
| `getObject()` | リスト使用時は全要素、そうでなければ`objectToSpawn`を`spawnObject`へ渡す。 |
| `spawnObject(GameObject newObject)` | 有効時のみ生成上限を確認し、`spawnPosition`周辺に複製して名前とアクティブ状態を整える。 |
