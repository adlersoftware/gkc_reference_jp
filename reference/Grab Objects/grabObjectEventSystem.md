# grabObjectEventSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Grab Objects/grabObjectEventSystem.cs:6`

**概要**: 把持・解放時に UnityEvent を呼ぶだけの小規模なイベント中継コンポーネント。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Grab | `useEventOnGrab` | `bool` | true | – |
| Event On Grab | `eventOnGrab` | `UnityEvent` | – | – |
| Use Event On Drop | `useEventOnDrop` | `bool` | – | – |
| Event On Drop | `eventOnDrop` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `callEventOnGrab()` | `useEventOnGrab` が有効なら `eventOnGrab` を発火するだけ。 |
| `callEventOnDrop()` | `useEventOnDrop` が有効なら `eventOnDrop` を発火するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnGrab` | `UnityEvent` | – |
| `eventOnDrop` | `UnityEvent` | – |
