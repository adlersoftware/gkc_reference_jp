# rotateObjectSmoothlySystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/rotateObjectSmoothlySystem.cs:5`

**概要**: 複数の回転状態を名前で切り替え、コルーチンで滑らかに回転させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Rotate Object System Enabled | `rotateObjectSystemEnabled` | `bool` | true | – |
| Transform To Rotate | `transformToRotate` | `Transform` | – | – |
| Avoid Rotation If Already In Process | `avoidRotationIfAlreadyInProcess` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Rotation In Process | `rotationInProcess` | `bool` | – | – |

### Rotation State List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Rotation State Info List | `objectRotationStateInfoList` | `List<objectRotationStateInfo>` | new List<objectRotationStateInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `rotateObjectToRandomRotationState()` | 有効時、必要なら処理中かを確認し、リストからランダムな回転状態名でコルーチンを開始する。 |
| `rotateObjectToRotation(string rotationName)` | 有効時、実行中コルーチンを止めて`rotationName`の回転状態へ向かうコルーチンを開始する。 |
| `stopRotateObjectToRotationCoroutine()` | `rotationCoroutine`があれば停止し、`rotationInProcess`を`false`にする。 |

## 内部型

- `objectRotationStateInfo`（class）
