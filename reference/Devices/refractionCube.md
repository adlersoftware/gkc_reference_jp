# refractionCube

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/refractionCube.cs:4`

**概要**: レーザーを屈折させるプリズム。設定色を自身へ反映し、屈折中かどうかを外部へ公開する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Refraction Cube Color | `refractionCubeColor` | `Color` | – | – |
| Cube Laser Device Game Object | `cubeLaserDeviceGameObject` | `GameObject` | – | – |
| Cube Laser Connector Game Object | `cubeLaserConnectorGameObject` | `GameObject` | – | – |
| Refracting Laser | `refractingLaser` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setRefractingLaserState(bool state)` | `refractingLaser`を設定するだけ。 |
| `isRefracting()` | `refractingLaser`を返すだけ。 |
