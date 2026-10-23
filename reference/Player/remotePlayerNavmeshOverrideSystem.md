# remotePlayerNavmeshOverrideSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/remotePlayerNavmeshOverrideSystem.cs:5`

**概要**: シーン内の `remotePlayerNavmeshOverride` を探して、リモートプレイヤーのNavMesh有効化と目的地（ウェイポイントまたはTransform）を設定する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Navmesh | `activateNavmesh` | `bool` | – | – |

### Navmesh Target Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Navmesh Target Transform | `navmeshTargetTransform` | `Transform` | – | – |
| Use Waypoint List | `useWaypointList` | `bool` | – | – |
| Waypoint List | `waypointList` | `List<Transform>` | new List<Transform> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Remote Player Navmesh Override | `mainRemotePlayerNavmeshOverride` | `remotePlayerNavmeshOverride` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setRemoteNavmeshState()` | `activateNavmesh` を引数に `setRemoteNavmeshStateExternally` を呼ぶだけ。 |
| `setRemoteNavmeshStateExternally(bool state)` | true なら有効化、false なら無効化のメソッドを呼ぶ。 |
| `activateRemoteNavmesh()` | 参照が無ければ `FindObjectOfType` で取得し、有効化したうえでウェイポイントか対象Transformを設定する。 |
| `disableRemoteNavmesh()` | 参照を確保してNavMeshを無効化し、ウェイポイント使用時はリストを null にする。 |
