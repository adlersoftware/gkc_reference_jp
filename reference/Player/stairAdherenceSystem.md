# stairAdherenceSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/stairAdherenceSystem.cs:5`

**概要**: 階段の昇降判定値をプレイヤーへ適用する小さなコンポーネント。最小/最大値と地面吸着力を渡す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Modify Stairs Values On Player | `modifyStairsValuesOnPlayer` | `bool` | true | – |
| Stairs Min Value | `stairsMinValue` | `float` | 0.08f | – |
| Stairs Max Value | `stairsMaxValue` | `float` | 0.25f | – |
| Stairs Ground Adherence | `stairsGroundAdherence` | `float` | 6.5f | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setStairsValuesOnPlayer(playerController newPlayerController)` | `setStairsValues` に最小値・最大値・地面吸着力を渡すだけ。 |
