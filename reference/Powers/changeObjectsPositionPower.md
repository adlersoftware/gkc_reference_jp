# changeObjectsPositionPower

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/New Powers Behaviors/changeObjectsPositionPower.cs:5`

**概要**: 狙ったオブジェクトとプレイヤーの位置を入れ替えるパワー。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Power Enabled | `powerEnabled` | `bool` | true | – |
| Layer | `layer` | `LayerMask` | – | – |
| Ground Layer | `groundLayer` | `LayerMask` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Powers Manager | `powersManager` | `otherPowers` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Player Camera Transform | `playerCameraTransform` | `Transform` | – | – |
| Gravity Manager | `gravityManager` | `gravitySystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activatePower()` | カメラ前方の対象とプレイヤーの位置を交換し、地面へ再配置する。 |
