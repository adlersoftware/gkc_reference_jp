# craftingSocket

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Crafting System/craftingSocket.cs:5`

**概要**: ステーションの入出力を表すソケット。接続先ステーションと、`LineRenderer`による接続線の表示・端点更新を管理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Is Input Socket | `isInputSocket` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Socket Assigned | `socketAssigned` | `bool` | – | – |
| Current Target Transform | `currentTargetTransform` | `Transform` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Crafting Station System Assigned | `currentCraftingStationSystemAssigned` | `craftingStationSystem` | – | – |
| Main Line Renderer | `mainLineRenderer` | `LineRenderer` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `assignCraftingStationSystem(craftingStationSystem newCraftingStationSystem)` | 接続先ステーションを設定し、`checkIfSocketAssigned`で割当状態を更新する。 |
| `removeCraftingStationSystem()` | `currentCraftingStationSystemAssigned`をnullにするだけ。 |
| `checkIfSocketAssigned()` | 接続先がnullかどうかで`socketAssigned`を更新するだけ。 |
| `enableOrDisableLineRenderer(bool state)` | `mainLineRenderer`があり状態が異なる場合のみ`enabled`を設定するだけ。 |
| `enableLineRendererIfSocketAssigned()` | ソケット割当済みなら`LineRenderer`を有効にするだけ。 |
| `updateLinerenderPositions()` | `currentTargetTransform`があれば、その位置を終点としてラインを更新する。 |
| `setLineRendererTargetPosition(Vector3 targetPosition)` | ラインの始点を自身の位置、終点を指定座標に設定するだけ。 |
| `setLineRendererTargetPosition(Transform targetTransform)` | `currentTargetTransform`を保存し、ラインの始点を自身、終点を対象位置に設定する。 |
