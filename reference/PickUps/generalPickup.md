# generalPickup

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `pickupType`
- **ソース**: `PickUps/Pickups Behaviour/generalPickup.cs:5`

**概要**: 汎用ピックアップ。インベントリへ保存するか、プレイヤーステータスの加算、リモートイベント、アビリティ解放、設計図追加を直接実行するかを選べる。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Stat Info List | `statInfoList` | `List<statInfo>` | new List<statInfo> () | – |
| Pickup Name | `pickupName` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setConsumableName(string newConsumableName)` | `pickupName` を設定するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkIfCanBePicked()`, `confirmTakePickup()`, `renameObject(string newName)`

</details>

## 内部型

- `statInfo`（class）
