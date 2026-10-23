# inputDoubleClickEventSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Input/inputDoubleClickEventSystem.cs:6`

**概要**: クリック回数と制限時間から連打を判定し、規定回数に達したらイベントを発火する。全クリック共通の制限時間を使う方式にも切り替えられる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Double Click Enabled | `checkDoubleClickEnabled` | `bool` | true | – |
| Max Time Between Clicks | `maxTimeBetweenClicks` | `float` | 0.4f | – |
| Use Max Time During All Clicks | `useMaxTimeDuringAllClicks` | `bool` | – | – |
| Max Time For All Clicks | `maxTimeForAllClicks` | `float` | – | – |
| Number Of Clicks To Activate Input | `numberOfClicksToActivateInput` | `int` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Number Of Clicks | `currentNumberOfClicks` | `int` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Activate Input | `eventOnActivateInput` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkClickInput()` | クリック回数を増やし、規定回数に達した時に制限時間内なら`eventOnActivateInput` を発火してカウントを戻す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnActivateInput` | `UnityEvent` | – |
