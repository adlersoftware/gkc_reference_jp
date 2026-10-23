# checkpointSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Checkpoint/checkpointSystem.cs:5`

**概要**: チェックポイントの管理役。現在の要素を保持して死亡時の再出現やシーン再読み込みを行い、エディタでの追加・削除も担う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Checkpoint System Enabled | `checkpointSystemEnabled` | `bool` | true | チェックポイント機能全体の有効無効。オフ時は保存も死亡時の復帰も行わない。 |
| Checkpoint Scene ID | `checkpointSceneID` | `int` | – | チェックポイント保存時に記録するシーン識別ID。同名IDの重複保存を防ぐ。 |
| Check Point Prefab | `checkPointPrefab` | `GameObject` | – | 新規チェックポイント追加時に生成するプレハブ。 |
| Layer To Place New Checkpoints | `layerToPlaceNewCheckpoints` | `LayerMask` | – | シーンカメラからレイを飛ばして配置先を決める対象レイヤー。 |
| Checkpoints Position Offset | `checkpointsPositionOffset` | `Vector3` | – | 配置位置をレイの当たった地点からずらすオフセット。 |
| Trigger Scale | `triggerScale` | `Vector3` | – | 生成するチェックポイントの`BoxCollider`トリガーのサイズ。 |

### Respawn Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Death Loack Checkpoint Type | `deathLoackCheckpointType` | `deathLoadCheckpoint` | – | 死亡時の処理方法。シーン再読込・その場リスポーン・何もしない。 |
| Layer To Respawn | `layerToRespawn` | `LayerMask` | – | リスポーン位置を地面に合わせるレイキャストの対象レイヤー。 |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Checkpoint Element | `currentCheckpointElement` | `checkpointElement` | – | 現在到達しているチェックポイント。デバッグ用の参照。 |

### Gizmo Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | チェックポイント位置のギズモを表示するか。 |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.black | シーンビューでギズモに添えるラベルの文字色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Radius | `gizmoRadius` | `float` | – | チェックポイント位置に描く球ギズモの半径。 / 表示条件: `showGizmo` がオンのとき |
| Use Handle For Vertex | `useHandleForVertex` | `bool` | – | シーンビューでチェックポイントをハンドル操作で移動できるようにするか。 / 表示条件: `showGizmo` がオンのとき |
| Handle Radius | `handleRadius` | `float` | – | ハンドルをクリック判定する円の半径。 / 表示条件: `showGizmo.boolValue && useHandleForVertex.boolValue` |
| Handle Gizmo Color | `handleGizmoColor` | `Color` | – | チェックポイント移動ハンドルの表示色。 / 表示条件: `showGizmo.boolValue && useHandleForVertex.boolValue` |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `checkPointList` | `List<Transform>` | new List<Transform> () | – |
| `checkPoinElementtList` | `List<checkpointElement>` | new List<checkpointElement> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentCheckpointElement(Transform currentCheckpoint)` | `checkPointList`内で一致する位置の`checkpointElement`を現在のチェックポイントにする。 |
| `respawnPlayer(GameObject currentPlayer)` | 現在のチェックポイント位置へプレイヤーとカメラを移し、速度を0にして落下時間をリセットする。 |
| `thereIsLastCheckpoint()` | `currentCheckpointElement`が設定済みかどうかを返す。 |
| `disableCheckPoint(int checkpointID)` | `checkpointID`が一致する要素だけ無効化し、他のチェックポイントは有効化する。 |
| `setCheckpointSystemEnabledState(bool state)` | `checkpointSystemEnabled`を設定するだけ。 |
| `isCheckpointSystemEnabled()` | `checkpointSystemEnabled`を返すだけ。 |
| `checkCheckpointStateOnCharacterGetUp(ragdollActivator currentRagdollActivator, GameObject characterGameObject)` | 死亡時の設定に応じて即起き上がり・再出現・シーン再読み込み・通常起き上がりを選び、使用有無を返す。 |
| `isDeathLoadCheckpointRespawnActivee()` | `deathLoackCheckpointType`が`respawn`かどうかを返す。 |
| `addNewCheckpoint()` | カメラのレイ先か前回位置に新しいチェックポイントを生成し、IDと管理者を設定して一覧へ追加する。 |
| `removeCheckpoint(int checkpointIndex)` | 指定位置のチェックポイントを即時破棄し、位置と要素の一覧から削除する。 |
| `removeAllCheckpoints()` | 全チェックポイントを即時破棄し、位置と要素の一覧を空にする。 |
| `updateComponent()` | `GKC_Utils.updateComponent`を呼び、シーンをダーティとして更新する。 |

## 内部型

- `deathLoadCheckpoint`（enum）
