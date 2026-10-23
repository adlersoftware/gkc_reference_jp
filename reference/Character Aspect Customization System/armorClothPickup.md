# armorClothPickup

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `pickupType`
- **ソース**: `Character Aspect Customization System/armorClothPickup.cs:5`

**概要**: `pickupType`を継承したアーマー/服のピックアップで、プレイヤーの`inventoryCharacterCustomizationSystem`の有無でインベントリ格納可否を判定します。取得時にはメッセージ表示、サウンド再生、レベルからの削除を行います。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Name | `objectName` | `string` | – | – |
| Category Name | `categoryName` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setObjectName(string newName)` | `objectName`を`newName`に代入するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkIfCanBePicked()`, `confirmTakePickup()`, `renameObject(string newName)`

</details>
