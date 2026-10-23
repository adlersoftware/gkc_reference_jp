# setCharacterParentOnMovingObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/setCharacterParentOnMovingObject.cs:5`

**概要**: 動くオブジェクトに乗ったプレイヤーや車両を親子付けし、移動プラットフォームとして扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Tag | `playerTag` | `string` | "Player" | – |
| Vehicle Tag | `vehicleTag` | `string` | "vehicle" | – |
| Platform Transform | `platformTransform` | `Transform` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Passengers Info List | `passengersInfoList` | `List<waypointPlatform.passengersInfo>` | new List<waypointPlatform.passengersI… | – |
| Vehicles Info List | `vehiclesInfoList` | `List<waypointPlatform.vehiclesInfo>` | new List<waypointPlatform.vehiclesInf… | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `addPassenger(Transform newPassenger)` | 未登録なら`passengersInfoList`に`playerTransform`と`playerController`を組にした情報を追加する。 |
| `addVehicle(Transform newVehicle)` | 未登録なら`vehiclesInfoList`に`vehicleTransform`と`vehicleHUDManager`を組にした情報を追加する。 |
