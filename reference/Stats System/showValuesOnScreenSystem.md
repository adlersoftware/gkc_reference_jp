# showValuesOnScreenSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Stats System/showValuesOnScreenSystem.cs:6`

**概要**: ステータス値やインベントリ個数を`Text`へ表示するHUDコンポーネント。パネルの表示制御と前後付加文字を扱う。

**公式ドキュメント抜粋**（[Show Values On Screen System](../../docs/player-controller-components/elements-used-by-other-components/show-values-on-screen-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Value Enabled | `showValueEnabled` | `bool` | true | – |
| Add Extra String | `addExtraString` | `bool` | – | – |
| Extra String | `extraString` | `string` | – | – |
| Add Extra String At Start | `addExtraStringAtStart` | `bool` | – | – |

### Stats Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Stat Name To Show | `statNameToShow` | `string` | – | – |
| Show Stat Value On Start | `showStatValueOnStart` | `bool` | – | – |

### Inventory Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory Object Name To Show | `inventoryObjectNameToShow` | `string` | – | – |
| Show Inventory Object Amount On Start | `showInventoryObjectAmountOnStart` | `bool` | – | – |

### HUD Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Value Text Panel | `valueTextPanel` | `GameObject` | – | – |
| Value Text | `valueText` | `Text` | – | – |
| Player Game Object | `playerGameObject` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `showInventoryObjectAmountByName()` | インベントリ名から個数を取得し、-1より大きければ画面表示を更新する。 |
| `showStatByName()` | `statNameToShow`の値を取得し、-1より大きければ画面表示を更新する。 |
| `updateValueAmount(int IDValue, float newValue)` | `IDValue`を無視して`updateValueAmount(float)`へ委譲する。 |
| `updateValueAmount(float newValue)` | パネルを表示して数値を文字列化し、前後付加文字を付けて`valueText`へ設定する。 |
