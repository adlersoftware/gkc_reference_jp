# simpleThrowFireWaveAbility

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/simpleThrowFireWaveAbility.cs:6`

**概要**: 状態フラグと開始・終了イベントだけを持つ単純な火炎波アビリティ。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current State | `currentState` | `bool` | – | – |
| Event On Activate State | `eventOnActivateState` | `UnityEvent` | – | – |
| Event On Deactivate State | `eventOnDeactivateState` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `toggleCurrentState()` | `currentState` を反転して `setCurrentState` を呼ぶだけ。 |
| `setCurrentState(bool state)` | 状態が変わる時だけ `currentState` を更新し、開始・終了イベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnActivateState` | `UnityEvent` | – |
| `eventOnDeactivateState` | `UnityEvent` | – |
