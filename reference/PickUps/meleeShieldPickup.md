# meleeShieldPickup

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `pickupType`
- **ソース**: `PickUps/Pickups Behaviour/meleeShieldPickup.cs:5`

**概要**: 盾用のピックアップ。`meleeWeaponsGrabbedManager` の設定に応じて装備かインベントリ保存かを切り替え、取得処理とメッセージ表示を行う。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shield Name | `shieldName` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setMeleeShieldName(string newShieldName)` | `shieldName` を設定するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkIfCanBePicked()`, `confirmTakePickup()`

</details>
