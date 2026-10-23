# zipline

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/zipline.cs:5`

**概要**: プレイヤーがぶら下がって移動するジップライン。IK、親子付け、速度制御、接続状態を管理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Extra Distance | `extraDistance` | `float` | – | – |
| Speed | `speed` | `float` | – | – |
| Max Speed | `maxSpeed` | `float` | – | – |
| Min Speed | `minSpeed` | `float` | – | – |
| Zipline Connected | `ziplineConnected` | `bool` | true | – |
| Connect Zipline Speed | `connectZiplineSpeed` | `float` | 5 | – |

### IK Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| IK Zipline | `IKZipline` | `IKZiplineInfo` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Zipline | `usingZipline` | `bool` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Gizmo Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Device Manager | `deviceManager` | `electronicDevice` | – | – |
| Trigger | `trigger` | `Collider` | – | – |
| Final Position | `finalPosition` | `Transform` | – | – |
| Initial Position | `initialPosition` | `Transform` | – | – |
| Moving Transform | `movingTransform` | `Transform` | – | – |
| Middle Line | `middleLine` | `Transform` | – | – |
| Middle Line Pivot | `middleLinePivot` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の`mainCoroutine`を停止するだけ。 |
| `activateZipLine()` | 使用状態を反転し、開始時は速度更新コルーチンを、終了時は停止扱いで`changeZiplineState`を呼ぶ。 |
| `changeZiplineState(bool state)` | IK・コライダー・親子付け・`isKinematic`・入力停止を切り替え、開始/終了位置への移動を再開する。 |
| `setCurrentPlayer(GameObject player)` | プレイヤーを保持し、制御・入力・IK・デバイス操作の各コンポーネントを取得する。 |
| `checkZiplineMovement()` | 実行中の移動コルーチンを止め、`movingTransform`を目標位置へ動かすコルーチンを開始する。 |
| `setZiplineConnectedState(bool state)` | `ziplineConnected`とトリガーを設定し、接続時は`connectZipine`を呼ぶ。 |
| `connectZipine()` | 実行中の接続コルーチンを止め、ワイヤーを伸ばす`connectZipineCoroutine`を開始する。 |

## 内部型

- `IKZiplineInfo`（class）
- `IKGoalsZiplinePositions`（class）
- `IKHintsZiplinePositions`（class）
