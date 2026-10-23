# simpleUIButtonInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Menu/simpleUIButtonInfo.cs:6`

**概要**: ボタンの表示名などを保持するだけの小さな情報コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Name | `currentName` | `string` | – | – |
| ID | `ID` | `int` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Button Object | `buttonObject` | `GameObject` | – | – |
| Main Text | `mainText` | `Text` | – | – |
| Main Icon | `mainIcon` | `RawImage` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentName(string newValue)` | `currentName`に`newValue`を設定するだけ。 |
| `getCurrentName()` | `currentName`を返すだけ。 |
