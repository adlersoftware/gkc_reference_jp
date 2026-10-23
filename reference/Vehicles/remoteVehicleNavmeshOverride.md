# remoteVehicleNavmeshOverride

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/AI/remoteVehicleNavmeshOverride.cs:5`

**概要**: 外部オブジェクトから`vehicleAINavMesh`へ追従ターゲットを設定/解除する小さなブリッジ。目標の種別や自動ブレーキ設定も一緒に渡す。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Target Is Friendly | `targetIsFriendly` | `bool` | – | – |
| Target Is Object | `targetIsObject` | `bool` | – | – |
| Set Auto Brake On Remove Target State | `setAutoBrakeOnRemoveTargetState` | `bool` | – | – |
| Auto Brake On Remove Target | `autoBrakeOnRemoveTarget` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Vehicle AI Nav Mesh | `mainVehicleAINavMesh` | `vehicleAINavMesh` | – | – |
| Target Tranform | `targetTranform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setVehicleNavMeshTargetPosition()` | `targetTranform`（未設定なら自身）を追従させ、種別と自動ブレーキ設定も反映する。 |
| `removeVehicleNavmeshTarget()` | 自動ブレーキ設定を反映したうえで`removeTarget`を呼び、追従対象を解除する。 |
