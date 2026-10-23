# remotePlayerNavmeshOverride

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/remotePlayerNavmeshOverride.cs:5`

**概要**: リモートプレイヤーのNavMesh目的地や有効状態を外部から操作するためのプロキシ。処理は `mainPlayerNavMeshSystem` へ委譲する。

**公式ドキュメント抜粋**（[Remote Player Navmesh Override](../../docs/player-controller-components/elements-used-by-other-components/remote-player-navmesh-override.md)）

> It allows you to change between free control of the player and movement based on navmesh, setting a specific position of the scene to be reached by the player, though events for example.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Nav Mesh System | `mainPlayerNavMeshSystem` | `playerNavMeshSystem` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Nav Mesh Active | `playerNavMeshActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPlayerNavMeshWaypointTargetPosition(List<Transform> waypointList)` | `mainPlayerNavMeshSystem.setNewWaypointList` にウェイポイントリストを渡すだけ。 |
| `setPlayerNavMeshTransformTargetPosition(Transform newTransformPosition)` | 指定Transformの位置でレイキャスト位置チェックを呼ぶ。 |
| `setPlayerNavMeshTargetPosition()` | 自身の位置でレイキャスト位置チェックを呼ぶ。 |
| `enablePlayerNavMeshState()` | `setPlayerNavMeshEnabledState(true)` を呼ぶだけ。 |
| `disablePlayerNavMeshState()` | `setPlayerNavMeshEnabledState(false)` を呼ぶだけ。 |
| `setPlayerNavMeshEnabledState(bool state)` | 外部使用フラグとNavMesh有効状態を設定し、`playerNavMeshActive` を更新する。 |
