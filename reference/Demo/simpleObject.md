# simpleObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Demo/simpleObject.cs:4`

**概要**: `working`がtrueの間、Updateで`mainAnimation`の`animationName`を再生し、再生終了ごとに速度の符号を反転して往復させるデモ用コンポーネント。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Animation Name | `animationName` | `string` | "piston" | – |
| Working | `working` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activate()` | `working`をtrueにするだけ。 |
| `changeState()` | `working`を現在値の反転に切り替えるだけ。 |
