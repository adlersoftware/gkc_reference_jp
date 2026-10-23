# randomEventSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Event System/randomEventSystem.cs:6`

**概要**: 名前指定か乱数で選んだ要素の`UnityEvent`を、全体有効フラグと確率判定を経て発火する。順番に発火するためのインデックスも保持する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Random Events Enabled | `randomEventsEnabled` | `bool` | true | – |
| Use Same Index Value | `useSameIndexValue` | `bool` | – | – |
| Same Index Value To Use | `sameIndexValueToUse` | `int` | – | – |
| Current Event Index In Order | `currentEventIndexInOrder` | `int` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Ignore Random Event Active | `ignoreRandomEventActive` | `bool` | – | – |

### Random Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Random Event Info List | `randomEventInfoList` | `List<randomEventInfo>` | new List<randomEventInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `callEventInOrderByIndex(int newValue)` | `currentEventIndexInOrder`に値を代入してから`callEventInOrder`を呼ぶ。 |
| `callEventInOrder()` | 現在のインデックスのイベントを発火し、インデックスを進めて末尾に達したら0へ戻す。 |
| `setEventIndexInOrderValue(int newValue)` | 値を設定し、リスト数以上なら0に戻す。 |
| `resetEventIndexInOrder()` | `currentEventIndexInOrder`を0にするだけ。 |
| `callRandomEventIgnoringProbabilityByName(string eventName)` | 確率判定を無視する内部フラグを立てて名前指定の発火を行い、終了後にフラグを戻す。 |
| `callRandomEventByName(string eventName)` | 無視フラグや全体無効時は何もせず、名前が一致する要素を探して`activateEvent`を呼ぶ。 |
| `callRandomEvent()` | 無視フラグや全体無効時は何もせず、乱数（`useSameIndexValue`なら固定値）で要素を選び`activateEvent`を呼ぶ。 |
| `setRandomEventsEnabledState(bool state)` | `randomEventsEnabled`を設定するだけの薄いセッター。 |
| `setIgnoreRandomEventActiveState(bool state)` | `ignoreRandomEventActive`を設定するだけの薄いセッター。 |

## 内部型

- `randomEventInfo`（class）
