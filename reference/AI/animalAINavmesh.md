# animalAINavmesh

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `AINavMesh`
- **ソース**: `AI/animalAINavmesh.cs:5`

**概要**: 動物AI用に、AIの移動入力を入力上書きと`playerControllerManager`の移動へ変換する派生クラス。

## インスペクター設定

### AI Navmesh Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Input Action Manager | `mainInputActionManager` | `inputActionManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `disableOverrideInputValues()` | `overrideInputValues`をゼロ入力かつ無効で呼び、入力の上書きを解除する。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`updateAICameraInputValues()`, `updateAIControllerInputValues()`

</details>
