# puzzleSystemPlayerManagement

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Puzzles/puzzleSystemPlayerManagement.cs:6`

**概要**: プレイヤー側で使用中の`puzzleSystem`を保持し、入力をそこへ転送する窓口コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Puzzle | `usingPuzzle` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On State Change | `useEventsOnStateChange` | `bool` | – | – |
| Even On State Enabled | `evenOnStateEnabled` | `UnityEvent` | – | – |
| Event On State Disabled | `eventOnStateDisabled` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setcurrentPuzzleSystem(puzzleSystem newPuzzleObject)` | 現在の`puzzleSystem`参照を保持するだけ。 |
| `setUsingPuzzleState(bool state)` | 使用中フラグを設定し、状態変化イベントの確認を行う。 |
| `puzzleObjectInputSetRotateObjectState(bool state)` | 使用中で参照があれば、回転状態の入力をパズルへ転送する。 |
| `puzzleObjectInputIncreaseObjectHolDistanceByButton(bool state)` | 使用中で参照があれば、距離を広げる入力をパズルへ転送する。 |
| `puzzleObjectInputDecreaseObjectHolDistanceByButton(bool state)` | 使用中で参照があれば、距離を狭める入力をパズルへ転送する。 |
| `puzzleObjectInputSetObjectHolDistanceByMouseWheel(bool state)` | 使用中で参照があれば、ホイールによる距離変更入力をパズルへ転送する。 |
| `puzzleObjectInputResetPuzzle()` | 使用中で参照があれば、パズルのリセット入力を呼ぶ。 |
| `checkEventsOnStateChange(bool state)` | イベントが有効なら、`state`に応じて有効化・無効化イベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `evenOnStateEnabled` | `UnityEvent` | – |
| `eventOnStateDisabled` | `UnityEvent` | – |
