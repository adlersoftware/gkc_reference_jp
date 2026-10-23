# characterToReceiveOrders

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Custom Orders/characterToReceiveOrders.cs:6`

**概要**: 注文名ごとにイベント・継続時間・簡易AIアクションを登録し、キャラクターが注文を受け付ける仕組みを提供する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Receive Orders Enabled | `receiveOrdersEnabled` | `bool` | true | – |

### Order Info Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Order Info List | `characterOrderInfoList` | `List<characterOrderInfo>` | new List<characterOrderInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Order In Process | `orderInProcess` | `bool` | – | – |
| Current Target | `currentTarget` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `containsOrderName(string orderName)` | 同名の注文が存在し、かつ`orderEnabled`がtrueの場合のみtrueを返す。 |
| `activateOrder(string orderName)` | 一致する有効な注文の受領イベントを呼び、継続時間コルーチンの開始と簡易AIアクションの起動を行う。 |
| `setCustomTarget(Transform newTarget)` | `currentTarget`に設定し、注文設定に応じて対象送信イベントと簡易AIアクションへ対象を渡す。 |
| `isOrderInProcess()` | `orderInProcess`の値を返すだけ。 |

## 内部型

- `characterOrderInfo`（class）
