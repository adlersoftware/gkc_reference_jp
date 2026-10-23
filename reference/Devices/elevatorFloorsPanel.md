# elevatorFloorsPanel

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/elevatorFloorsPanel.cs:6`

**概要**: エレベーターの階数ボタンを階数分だけ生成し、押された階へ`elevatorSystem`経由で移動させるUIパネル。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Elevator | `elevator` | `GameObject` | – | – |
| Floor Button | `floorButton` | `GameObject` | – | – |
| Floor List Content | `floorListContent` | `RectTransform` | – | – |
| Elevator Manager | `elevatorManager` | `elevatorSystem` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Floor Button List | `floorButtonList` | `List<GameObject>` | new List<GameObject> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateElevatorFloorPanel()` | `usingPanel`を反転するだけ。 |
| `goToFloor(Button button)` | 押下ボタンに対応する階数インデックスを求め、移動に成功すれば`electronicDevice`を停止する。 |
