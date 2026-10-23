# currencySystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/currencySystem.cs:7`

**概要**: 所持金 `currentMoneyAmount` を保持し、加算・使用・所持金パネル表示・`playerStatsSystem` への反映をまとめて行う通貨管理コンポーネント。金額変化時には文字列付きイベントも発火する。

**公式ドキュメント抜粋**（[Currency System](../../docs/player-controller-components/non-essential-components/currency-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Money Amount | `currentMoneyAmount` | `int` | – | – |
| Stat Name | `statName` | `string` | "Money" | – |
| Extra String Content | `extraStringContent` | `string` | "$" | – |
| Show Total Money Amount On Change | `showTotalMoneyAmountOnChange` | `bool` | – | – |
| Increase Money Text Smoothly | `increaseMoneyTextSmoothly` | `bool` | – | – |
| Increase Money Text Rate | `increaseMoneyTextRate` | `float` | 0.01f | – |
| Delay To Start Increas Money Text | `delayToStartIncreasMoneyText` | `float` | 0.5f | – |
| Time To Show Total Money Amount | `timeToShowTotalMoneyAmount` | `float` | – | – |
| Hide Total Amount Money P Anel After Delay | `hideTotalAmountMoneyPAnelAfterDelay` | `bool` | true | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Receive Money | `eventOnReceiveMoney` | `UnityEvent` | – | – |
| Event On Receive Money With String | `eventOnReceiveMoneyWithString` | `eventParameters.eventToCallWithString` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Total Money Amount Panel | `totalMoneyAmountPanel` | `GameObject` | – | – |
| Total Money Amount Text | `totalMoneyAmountText` | `Text` | – | – |
| Player Stats Manager | `playerStatsManager` | `playerStatsSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `increaseTotalMoneyAmount(float extraValue, float customMoneyChangeSpeedValue)` | `customMoneyChangeSpeed` に速度を設定してから、単一引数の `increaseTotalMoneyAmount` を呼び出すだけ。 |
| `increaseTotalMoneyAmount(float extraValue)` | `extraValue` を所持金に加算し、受取イベントを発火して `statName` のステータスを更新し、設定に応じて所持金パネルを表示する。 |
| `initializeMoneyAmount(float newValue)` | `currentMoneyAmount` を `newValue` の整数値にして金額テキストを更新する。 |
| `updateMoneyAmountWithoutUpdatingStatManager(int statId, float amount)` | ステータスは触らずに金額を `amount` に置き換え、テキストのみ更新する。`statId` は未使用。 |
| `useMoney(float amountToUse)` | 所持金が `amountToUse` 以上なら差し引いてステータスを更新し true を返し、不足なら false を返す。 |
| `getCurrentMoneyAmount()` | `currentMoneyAmount` を `float` にキャストして返すだけ。 |
| `canSpendMoneyAmount(float amountToSpend)` | 所持金が `amountToSpend` 以上かどうかを判定して返すだけ。 |
| `showTotalMoneyAmountPanel()` | 実行中の表示コルーチンを止めてから、所持金パネル表示コルーチンを新たに開始する。 |
| `stopShowTotalMoneyAmountPanelCoroutine()` | `showTotalMoneyCoroutine` が null でなければ停止するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnReceiveMoney` | `UnityEvent` | – |
