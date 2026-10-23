# coinPocketSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/coinPocketSystem.cs:6`

**概要**: キャラクターが所持するコイン枚数を管理し、取得時と全ドロップ時にイベントを発火する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Coint Amount | `currentCointAmount` | `int` | – | – |
| Pick Coins Enabled | `pickCoinsEnabled` | `bool` | true | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Drop All Coins | `eventOnDropAllCoins` | `UnityEvent` | – | – |
| Event To Set Amount Of Coins | `eventToSetAmountOfCoins` | `eventParameters.eventToCallWithInteger` | – | – |
| Use Events On Picked Coin | `useEventsOnPickedCoin` | `bool` | – | – |
| Event On Picked Coin | `eventOnPickedCoin` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getCoinAmount()` | `currentCointAmount`をそのまま返すだけ。 |
| `addCoinAmount(int newAmount)` | `currentCointAmount`に`newAmount`を加算し、取得イベント設定時は`eventOnPickedCoin`を発火する。 |
| `dropAllCoins()` | 所持数が0より大きい時、枚数を引数に`eventToSetAmountOfCoins`と`eventOnDropAllCoins`を発火してから0に戻す。 |
| `canPickCoins()` | `pickCoinsEnabled`をそのまま返すだけ。 |
| `setPickCoinsEnabledState(bool state)` | `pickCoinsEnabled`に`state`を代入するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnDropAllCoins` | `UnityEvent` | – |
| `eventOnPickedCoin` | `UnityEvent` | – |
