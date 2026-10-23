# touchScreenPinchSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Input/touchScreenPinchSystem.cs:6`

**公式ドキュメント抜粋**（[Touch Screen Pinch System](../../docs/player-controller-components/elements-used-by-other-components/touch-screen-pinch-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pinch Enabled | `pinchEnabled` | `bool` | true | – |
| Min Distance To Update Pinch | `minDistanceToUpdatePinch` | `float` | 5 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| First Mouse Touch Active | `firstMouseTouchActive` | `bool` | – | – |
| Secondary Mouse Touch Active | `secondaryMouseTouchActive` | `bool` | – | – |
| Current Number Of Touch Buttons Pressed | `currentNumberOfTouchButtonsPressed` | `int` | – | – |
| Initial Distance | `initialDistance` | `float` | – | – |
| Current Distance | `currentDistance` | `float` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Pinch In | `eventOnPinchIn` | `UnityEvent` | – | – |
| Event On Pinch Out | `eventOnPinchOut` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Input | `input` | `inputManager` | – | – |
| Player Input | `playerInput` | `playerInputManager` | – | – |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnPinchIn` | `UnityEvent` | – |
| `eventOnPinchOut` | `UnityEvent` | – |
