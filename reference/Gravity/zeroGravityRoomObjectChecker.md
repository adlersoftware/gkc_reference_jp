# zeroGravityRoomObjectChecker

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Gravity/zeroGravityRoomObjectChecker.cs:5`

**概要**: 無重力ルームとの紐付けを保持し、現在のルームへオブジェクトを追加するための小さな補助コンポーネント。

## インスペクター設定

### Main Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Gravity Room States Enabled | `checkGravityRoomStatesEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Inside Gravity Room | `objectInsideGravityRoom` | `bool` | – | – |
| Current Zero Gravity Room | `currentZeroGravityRoom` | `zeroGravityRoomSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentZeroGravityRoom(zeroGravityRoomSystem gravityRoom)` | チェック無効なら戻り、現在のルームと室内フラグを設定する。 |
| `checkAddObjectToCurrentRoom(GameObject newObject)` | チェック無効なら戻り、室内なら現在のルームへオブジェクトを追加する。 |
