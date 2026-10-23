# AIWalkToPosition

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/AIWalkToPosition.cs:6`

**概要**: 指定位置までAIを歩かせ、到達やプレイヤー死亡時にNavMesh設定とAI状態を元へ戻す。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Walk To Position Enabled | `walkToPositionEnabled` | `bool` | true | – |
| Max Walk Speed | `maxWalkSpeed` | `float` | 1 | – |
| Walk Position Transform | `walkPositionTransform` | `Transform` | – | – |
| Activate Dynamic Obstacle Detection | `activateDynamicObstacleDetection` | `bool` | – | – |
| Assign Partner If Found On Position Reached | `assignPartnerIfFoundOnPositionReached` | `bool` | – | – |
| Remove Partner If Found On Position Reached | `removePartnerIfFoundOnPositionReached` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Walk To Position In Process | `walkToPositionInProcess` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Transform | `characterTransform` | `Transform` | – | – |
| Main AI Navmesh | `mainAINavmesh` | `AINavMesh` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateWalkToPosition()` | 有効時はAIを停止して目的地への移動と速度を設定し、到達を監視するコルーチンを開始する。 |
| `stopActivateWalkPosition()` | 移動中ならコルーチンを止めてAI状態を復帰し、`walkToPositionInProcess`をfalseにする。 |
| `stopUpdateCoroutine()` | `updateCoroutine`が実行中なら停止するだけ。 |
