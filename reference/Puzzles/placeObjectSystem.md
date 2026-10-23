# placeObjectSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Puzzles/placeObjectSystem.cs:6`

**概要**: 対象オブジェクトがトリガー内で条件を満たすと、所定位置へ移動させて配置済みにするコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Place | `objectToPlace` | `GameObject` | – | – |
| Needs Other Object Placed Before | `needsOtherObjectPlacedBefore` | `bool` | – | – |
| Number Of Objects To Place Before | `numberOfObjectsToPlaceBefore` | `int` | – | – |

### Placement Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Rotation Limit | `useRotationLimit` | `bool` | – | – |
| Max Up Rotation Angle | `maxUpRotationAngle` | `float` | 30 | – |
| Max Forward Rotation Angle | `maxForwardRotationAngle` | `float` | 30 | – |
| Use Position Limit | `usePositionLimit` | `bool` | – | – |
| Max Position Distance | `maxPositionDistance` | `float` | – | – |
| Place Object Position Speed | `placeObjectPositionSpeed` | `float` | – | – |
| Place Object Rotation Speed | `placeObjectRotationSpeed` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Placed | `objectPlaced` | `bool` | – | – |
| Object Inside Trigger | `objectInsideTrigger` | `bool` | – | – |
| Moving Object | `movingObject` | `bool` | – | – |
| Current Number Objects Placed | `currentNumberObjectsPlaced` | `int` | – | – |
| Object In Correct Position | `objectInCorrectPosition` | `bool` | – | – |
| Object In Correct Rotation | `objectInCorrectRotation` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Placed Event | `objectPlacedEvent` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Puzzle Manager | `puzzleManager` | `puzzleSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkIfCanBePlaced()` | 前提個数などの条件を満たせば、パズル側の把持解除とRigidbody固定を行い、移動を開始して配置済みにする。 |
| `canBeDragged(GameObject objectToCheck)` | `objectToPlace`自身かその子なら対象を返し、それ以外はnullを返す。 |
| `moveObjectToPlace()` | 既存コルーチンを止め、このTransformの位置と回転へ移動するコルーチンを開始する。 |
| `increaseNumberObjectsPlaced()` | 配置数を1増やすだけ。 |
| `resetNumberObjectsPlaced()` | 移動コルーチンを止め、配置数と配置済み・トリガー内フラグを初期化する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `objectPlacedEvent` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnTriggerEnter(Collider col)`, `OnTriggerExit(Collider col)`

</details>
