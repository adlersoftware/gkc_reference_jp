# touchButtonEventSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`, `IPointerDownHandler`, `IPointerUpHandler`
- **ソース**: `Input/touchButtonEventSystem.cs:8`
- **属性**: `System.Serializable`

**概要**: UIのタッチボタン押下・解放を検知してUnityEventを発火する。無効化時に押下中なら解放イベントを送って状態を戻す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event Enabled | `eventEnabled` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Button Pressed | `buttonPressed` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Press Down | `eventOnPressDown` | `UnityEvent` | – | – |
| Event On Press Up | `eventOnPressUp` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `OnPointerDown(PointerEventData eventData)` | `eventEnabled` なら`eventOnPressDown` を発火し、`buttonPressed` をtrueにする。 |
| `OnPointerUp(PointerEventData eventData)` | `eventEnabled` なら`eventOnPressUp` を発火し、`buttonPressed` をfalseにする。 |
| `setEventEnabledState(bool state)` | `eventEnabled` を`state`にし、押下中なら`eventOnPressUp` を発火して押下状態を解除する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnPressDown` | `UnityEvent` | – |
| `eventOnPressUp` | `UnityEvent` | – |
