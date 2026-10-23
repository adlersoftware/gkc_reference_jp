# simpleCoinPickup

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/simpleCoinPickup.cs:5`

**概要**: コイン取得時にキャラクターの`coinPocketSystem`へ枚数を加算して自身を消す。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Coin Amount | `coinAmount` | `int` | 1 | – |
| Coin Pickup Game Object | `coinPickupGameObject` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkToPickCoin(GameObject characterDetected)` | `characterDetected`の`coinPocketSystem`が取得可能なら`coinAmount`を加算し、`coinPickupGameObject`を破棄する。 |
