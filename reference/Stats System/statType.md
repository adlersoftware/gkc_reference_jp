# statType

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Stats System/statType.cs:5`

**概要**: ステータス変化を受け取るvirtualフック集で、既定実装はすべて空。派生クラスが初期化・増減・使用・bool切替の処理を実装する。

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `eventToInitializeStat(float newValue)` | 本体が空のvirtualで、初期値`newValue`の利用は派生クラスが実装する。 |
| `eventToIncreaseStat(float newValue)` | 本体が空で、増加量`newValue`の処理は派生クラスに委ねる。 |
| `eventToUseStat(float newValue)` | 本体が空で、使用量`newValue`の処理は派生クラスに委ねる。 |
| `eventToAddAmount(float newValue)` | 本体が空で、加算量`newValue`の処理は派生クラスに委ねる。 |
| `eventToInitializeBoolStat(bool newValue)` | 本体が空で、boolの初期値`newValue`の利用は派生クラスが実装する。 |
| `eventToActivateBoolStat(bool newValue)` | 本体が空で、bool状態`newValue`の反映は派生クラスが実装する。 |
| `eventToInitializeStatOnComponent()` | 本体が空で、コンポーネント側の初期化は派生クラスが実装する。 |
| `eventToInitializeBoolStatOnComponent()` | 本体が空で、bool用のコンポーネント初期化は派生クラスが実装する。 |
| `updateStatAmountWithoutUpdatingStatManager(int statId, float amount)` | 本体が空で、`statId`と`amount`によるマネージャー非経由の更新は派生クラスが実装する。 |
