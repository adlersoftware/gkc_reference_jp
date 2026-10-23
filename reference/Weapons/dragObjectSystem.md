# dragObjectSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/New Weapon Behaviors/dragObjectSystem.cs:6`

**概要**: 掴んだ物体をプレイヤー前方の位置へ追従させ、距離が離れるとイベントを出す運搬用システム。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Distance To Player | `distanceToPlayer` | `float` | – | – |
| Check Obstacle Raycast Distance | `checkObstacleRaycastDistance` | `float` | – | – |
| Drag Object Speed | `dragObjectSpeed` | `float` | 36 | – |
| Obstacle Found | `obstacleFound` | `bool` | – | – |
| Min Distance To Drop Object | `minDistanceToDropObject` | `float` | 1 | – |
| Player Distance | `playerDistance` | `float` | – | – |
| Adjust Object Position Speed | `adjustObjectPositionSpeed` | `float` | 5 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Object Grabbed | `objectGrabbed` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Far From Object | `eventOnFarFromObject` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Player Drag Position | `playerDragPosition` | `Transform` | – | – |
| Right IK Hand Position | `rightIKHandPosition` | `Transform` | – | – |
| Left IK Hand Position | `leftIKHandPosition` | `Transform` | – | – |
| Main Transform | `mainTransform` | `Transform` | – | – |
| Obstacle Trigger | `obstacleTrigger` | `Collider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `mainUpdateCoroutine`があれば停止するだけ。 |
| `dragObject()` | プレイヤー前方の目標位置へRigidbodyを補間移動し、向きを合わせ、離れていれば`eventOnFarFromObject`を呼ぶ。 |
| `setCurrentPlayer(GameObject newPlayer)` | `currentPlayerTransform`と`playerInput`を新しいプレイヤーから取り直す。 |
| `grabObject()` | 掴み位置への移動を開始し、`objectGrabbed`を立てて更新コルーチンを始める。 |
| `dropObject()` | `objectGrabbed`を下ろし、位置調整中なら止めて更新コルーチンも停止する。 |
| `setObstacleFoundState(bool state)` | `obstacleFound`を設定し、併せて`mainRigidbody.isKinematic`を切り替える。 |
| `translateObjectToGrabPosition()` | 既存の移動を止めてから、掴み位置へ寄せるコルーチンを開始する。 |
| `stopTranslateObjectToGrabPosition()` | `objectMovement`コルーチンがあれば停止するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnFarFromObject` | `UnityEvent` | – |
