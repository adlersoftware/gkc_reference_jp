# moveObjectSmoothlySystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/moveObjectSmoothlySystem.cs:5`

**概要**: 登録した位置状態へコルーチンでオブジェクトを滑らかに移動させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Move Object System Enabled | `moveObjectSystemEnabled` | `bool` | true | – |
| Transform To Move | `transformToMove` | `Transform` | – | – |

### Position State List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Position State Info List | `objectPositionStateInfoList` | `List<objectPositionStateInfo>` | new List<objectPositionStateInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `moveObjectToPosition(string positionName)` | 有効かつ自身がアクティブなら、既存コルーチンを止めて`positionName`向けの移動コルーチンを開始する。 |
| `stopMoveObjectToPositionCoroutine()` | `movementCoroutine`があれば停止するだけ。 |

## 内部型

- `objectPositionStateInfo`（class）
