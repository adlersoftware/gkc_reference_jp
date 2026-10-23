# simpleTurretRobot

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Demo/simpleTurretRobot.cs:4`

**概要**: 機銃と主砲の`Animation`を`CrossFade`で正転/逆転させ、ウェポンの展開と収納を演出するデモ用コンポーネント。`pressButton`で`activated`を反転して両アニメの再生方向を切り替える。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Machine Gun | `machineGun` | `GameObject` | – | – |
| Cannon | `cannon` | `GameObject` | – | – |
| Activated | `activated` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `pressButton()` | `activated`を反転し、trueなら`activateWeapon`、falseなら`deactivateWeapon`を呼ぶ。 |
| `stopAnimations()` | 機銃と主砲の2つの`Animation`を`Stop`するだけ。 |
| `activateWeapon()` | 両アニメの`speed`を1に戻し、`CrossFade`で`activateMachineGun`と`activateCannon`を再生する。 |
| `deactivateWeapon()` | 両アニメの`speed`を-1にし、停止中は末尾の`time`から、再生中は`CrossFade`で逆再生する。 |
