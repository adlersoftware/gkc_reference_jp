# customOrderBehavior

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Custom Orders/customOrderBehavior.cs:6`

**概要**: 注文ビヘイビアの基底クラスで、対象の取得や注文実行、ボタン表示条件を派生クラスが上書きする。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Order Enabled | `orderEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Current Target | `currentTarget` | `Transform` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event To Send Target | `useEventToSendTarget` | `bool` | – | – |
| Event To Send Target | `eventToSendTarget` | `eventParameters.eventToCallWithTransform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateOrder(Transform character)` | 中身が空のvirtualメソッドで、派生クラスでの上書きを前提とする。 |
| `activateOrder(Transform character, Transform orderOwner)` | 中身が空のvirtualメソッドで、注文発行者を伴う上書き用に用意されている。 |
| `getCustomTarget(Transform character, Transform orderOwner)` | 何もせずnullを返すだけのvirtualメソッド。 |
| `setCustomTarget(Transform newTarget)` | `currentTarget`に設定し、`useEventToSendTarget`が有効なら対象をイベントで送る。 |
| `checkConditionToShowOrderButton(Transform character)` | 常にfalseを返すだけのvirtualメソッド。 |
