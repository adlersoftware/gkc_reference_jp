# UIMouseHoverEvent

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`, `IPointerEnterHandler`, `IPointerExitHandler`
- **ソース**: `Others/UIMouseHoverEvent.cs:7`

**概要**: UIへのポインタ進入・退出を検知してUnityEventを呼ぶだけのコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Trigger Enter Enabled | `eventOnTriggerEnterEnabled` | `bool` | true | – |
| Event On Trigger Exit Enabled | `eventOnTriggerExitEnabled` | `bool` | true | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Trigger Enter | `eventOnTriggerEnter` | `UnityEvent` | – | – |
| Event On Trigger Exit | `eventOnTriggerExit` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `OnPointerEnter(PointerEventData pointerEventData)` | `eventOnTriggerEnterEnabled`が`true`なら`eventOnTriggerEnter`を発火する。 |
| `OnPointerExit(PointerEventData pointerEventData)` | `eventOnTriggerExitEnabled`が`true`なら`eventOnTriggerExit`を発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnTriggerEnter` | `UnityEvent` | – |
| `eventOnTriggerExit` | `UnityEvent` | – |
