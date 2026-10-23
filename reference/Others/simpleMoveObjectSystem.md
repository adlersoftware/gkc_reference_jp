# simpleMoveObjectSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/simpleMoveObjectSystem.cs:5`

**概要**: 対象オブジェクトを目標Transformの位置・回転へ速度に応じて補間移動する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Movement Enabled | `movementEnabled` | `bool` | true | – |
| Movement Speed | `movementSpeed` | `float` | 5 | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Target Position Transform | `targetPositionTransform` | `Transform` | – | – |
| Object To Move | `objectToMove` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateMovement()` | 有効時、既存コルーチンを止めて`targetPositionTransform`へ向かう移動コルーチンを開始する。 |
