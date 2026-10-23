# laserConnector

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `laser`
- **ソース**: `Devices/laserConnector.cs:4`

**概要**: 偏向されたレーザーを反射先まで伸ばすコネクタ。ヒット先がレシーバーかプリズムかで接続状態を切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `disableRefractionState()` | 反射レーザーとキューブの屈折状態を解除し、`laserDevice`の割当とレシーバー接続を無効化して自身を非アクティブにする。 |
| `setColor()` | `currentLaser`の`_TintColor`を自身のマテリアルへコピーする。 |
| `setCurrentLaser(GameObject laser)` | `currentLaser`を保持するだけ。 |
| `setCubeRefractionLaser(GameObject cube)` | `cubeRefractionLaser`を保持するだけ。 |
