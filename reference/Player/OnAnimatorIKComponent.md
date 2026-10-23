# OnAnimatorIKComponent

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Animator IK/OnAnimatorIKComponent.cs:5`

**概要**: IKコンポーネントの基底クラス。更新可否フラグと、派生クラスが上書きする仮想メソッド（状態設定・手の有効化・キャラクター要素設定）を提供する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Update IK Enabled | `updateIKEnabled` | `bool` | true | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateOnAnimatorIKState()` | 基底の仮想メソッドで、`updateIKEnabled` が false なら即 return するだけで他は何もしない。 |
| `setUpdateIKEnabledState(bool state)` | `updateIKEnabled` を設定するだけ。 |
| `isUpdateIKEnabled()` | `updateIKEnabled` の値を返すだけ。 |
| `setActiveState(bool state)` | 中身が空の仮想メソッドで、派生クラスでの実装用。 |
| `enableBothHands()` | `enableOrDisableRightOrLeftHand(true, false, true)` を呼ぶだけ。 |
| `enableOnlyLeftHand()` | `enableOrDisableRightOrLeftHand(true, false, false)` を呼ぶだけ。 |
| `enableOnlyRightHand()` | `enableOrDisableRightOrLeftHand(true, true, false)` を呼ぶだけ。 |
| `enableOrDisableRightOrLeftHand(bool state, bool isRightHand, bool setStateOnBothHands)` | 中身が空の仮想メソッドで、派生クラスが手の有効化を実装する。 |
| `setCharacterElements(GameObject newCharacter)` | 中身が空の仮想メソッドで、派生クラスがキャラクター参照を受け取る。 |
