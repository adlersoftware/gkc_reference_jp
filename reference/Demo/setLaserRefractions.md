# setLaserRefractions

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Demo/setLaserRefractions.cs:5`

**概要**: UIスライダーの値から、プレイヤーの`Shield`能力(`playerShieldSystem`)のレーザー屈折上限を変更するデモ用コンポーネント。変更値は同時にテキストへ表示する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Change | `objectToChange` | `GameObject` | – | – |
| Text Value | `textValue` | `Text` | – | – |
| Shield Ability Name | `shieldAbilityName` | `string` | "Shield" | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getSliderValue(Slider info)` | スライダー値をintにして`setLaserRefractionLimit`へ渡し、同じ値を`textValue`に表示する。 |
| `setCurrentPlayer(GameObject newPlayer)` | プレイヤーを`objectToChange`に保持し、`Shield`能力の`playerShieldSystem`を取得しておく。 |
