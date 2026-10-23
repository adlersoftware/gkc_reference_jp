# actionInputDelaySystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Input/actionInputDelaySystem.cs:6`

**概要**: 入力の押下・解放から一定時間後にイベントを発火する遅延システム。長押し判定の`hold`と、離した時判定の`up`を切り替えて使う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Input Enabled | `checkInputEnabled` | `bool` | true | – |
| Action Delay | `actionDelay` | `float` | – | – |
| Use Lower Delay | `useLowerDelay` | `bool` | – | – |
| Press Type Check | `pressTypeCheck` | `pressType` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pressed Down | `pressedDown` | `bool` | – | – |
| Previous Pressed Down | `previousPressedDown` | `bool` | – | – |
| Event Triggered | `eventTriggered` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Action Event | `actionEvent` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `inputSetPressedDownState()` | 押下フラグと押下時刻を更新し、`hold`設定で遅延時間を超えていれば`actionEvent` を一度だけ発火する。 |
| `inpuSetPressedUpState()` | 押下フラグをfalseにし、`up`設定なら`useLowerDelay` に応じて遅延前後の経過でイベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `actionEvent` | `UnityEvent` | – |

## 内部型

- `pressType`（enum）
