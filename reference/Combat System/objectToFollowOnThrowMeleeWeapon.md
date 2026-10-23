# objectToFollowOnThrowMeleeWeapon

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/objectToFollowOnThrowMeleeWeapon.cs:5`

**概要**: 投擲した近接武器が追従する対象トランスフォームを保持する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Object To Follow | `mainObjectToFollow` | `Transform` | – | – |
| Componented Added Temporaly | `componentedAddedTemporaly` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getMainObjectToFollow()` | `mainObjectToFollow`が未設定なら自身のトランスフォームを入れて返す。 |
| `setComponentedAddedTemporalyState(bool state)` | 一時的にコンポーネントを追加したか`componentedAddedTemporaly`を設定するだけ。 |
